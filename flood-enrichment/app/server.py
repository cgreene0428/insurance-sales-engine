"""
Webhook receiver + HubSpot V3 signature validation.

POST /webhook/hubspot   - enroll from a HubSpot "address changed" workflow
GET  /health            - liveness probe

process_contact() is the enrichment pipeline: read address -> NFD -> score/cost
-> write back. For high volume, push process_contact onto a queue and return 200
immediately (see README notes).

Run:  python -m app.server           (dev, :8000)
      gunicorn -w 2 -b 0.0.0.0:8000 app.server:app
"""

import base64
import hashlib
import hmac
import time

from flask import Flask, request, abort

from . import config
from . import nfd_client
from . import hubspot_client
from . import scoring

app = Flask(__name__)

_MAX_SKEW_MS = 5 * 60 * 1000  # reject requests older than 5 minutes (replay guard)


def _valid_signature(req) -> bool:
    """Validate X-HubSpot-Signature-V3 against the app client secret.

    HubSpot signs: method + full-URL + raw-body + timestamp, HMAC-SHA256,
    base64-encoded. Behind a TLS-terminating proxy, rebuild the https URL from
    X-Forwarded-Proto so the signed string matches.
    """
    secret = config.HUBSPOT_WEBHOOK_SECRET
    if not secret:
        return False
    sig = req.headers.get("X-HubSpot-Signature-V3")
    ts = req.headers.get("X-HubSpot-Request-Timestamp")
    if not sig or not ts:
        return False
    try:
        if abs(time.time() * 1000 - int(ts)) > _MAX_SKEW_MS:
            return False
    except ValueError:
        return False

    proto = req.headers.get("X-Forwarded-Proto", req.scheme)
    url = req.url
    if proto == "https" and url.startswith("http://"):
        url = "https://" + url[len("http://"):]

    base_string = req.method + url + req.get_data(as_text=True) + ts
    expected = base64.b64encode(
        hmac.new(secret.encode(), base_string.encode(), hashlib.sha256).digest()
    ).decode()
    return hmac.compare_digest(expected, sig)


def process_contact(contact_id: str) -> dict:
    """Read address -> NFD lookup -> enrich -> write back. Returns the enriched dict."""
    addr = hubspot_client.get_contact_address(contact_id)
    if not addr.get("address"):
        return {"skipped": "no address on contact", "contact_id": contact_id}
    payload = nfd_client.fetch_address(addr["address"])
    enriched = scoring.enrich(payload, addr.get("state"))
    hubspot_client.write_enrichment(contact_id, enriched)
    return enriched


@app.route("/webhook/hubspot", methods=["POST"])
def hubspot_webhook():
    if not _valid_signature(request):
        abort(401)
    body = request.get_json(silent=True)
    # HubSpot may send a single event object or a list of them.
    events = body if isinstance(body, list) else ([body] if body else [])
    for ev in events:
        object_id = (ev or {}).get("objectId")
        if object_id is None:
            continue
        try:
            process_contact(str(object_id))
        except Exception:  # never 500 back to HubSpot, or it will retry
            app.logger.exception("enrichment failed for objectId=%s", object_id)
    return ("", 200)


@app.route("/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
