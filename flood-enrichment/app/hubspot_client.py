"""
HubSpot contact read/write for the enrichment service.

- get_contact_address(): read the source-address props (config.ADDRESS_FIELDS)
  and build a single-line address string for the NFD call.
- write_enrichment(): map the enriched dict onto config.OUT_PROPS internal
  names and PATCH the contact.

SCAFFOLD: uses the CRM v3 objects API with a Private App token. Property
internal names must exist on the Contact object (see README section 2).
"""

import datetime

import requests

from . import config

_TIMEOUT_S = 30


class HubSpotError(RuntimeError):
    """Raised on any non-2xx or transport failure talking to HubSpot."""


def _headers() -> dict:
    if not config.HUBSPOT_ACCESS_TOKEN:
        raise HubSpotError("HUBSPOT_ACCESS_TOKEN is not set (see .env)")
    return {
        "Authorization": f"Bearer {config.HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }


def get_contact_address(contact_id: str) -> dict:
    """Read address props from a contact.

    Returns {street, city, state, zip, address} where `address` is a single
    comma-joined line suitable for NFD.
    """
    props = list(config.ADDRESS_FIELDS.values())
    url = f"{config.HUBSPOT_BASE}/crm/v3/objects/contacts/{contact_id}"
    try:
        resp = requests.get(
            url, headers=_headers(),
            params={"properties": ",".join(props)}, timeout=_TIMEOUT_S,
        )
    except requests.RequestException as exc:
        raise HubSpotError(f"read contact {contact_id} failed: {exc}") from exc
    if resp.status_code != 200:
        raise HubSpotError(
            f"read contact {contact_id} -> {resp.status_code}: {resp.text[:300]}"
        )

    p = resp.json().get("properties", {}) or {}
    parts = {logical: p.get(hs_name) for logical, hs_name in config.ADDRESS_FIELDS.items()}
    parts["address"] = ", ".join(
        str(parts[k]) for k in ("street", "city", "state", "zip") if parts.get(k)
    )
    return parts


def write_enrichment(contact_id: str, enriched: dict) -> dict:
    """Map the enriched dict onto OUT_PROPS and PATCH the contact."""
    props = {}
    for src, hs_name in config.OUT_PROPS.items():
        if src == "updated_at":
            continue
        val = enriched.get(src)
        if val is None:
            continue
        if isinstance(val, bool):  # HubSpot checkbox wants "true"/"false"
            val = "true" if val else "false"
        props[hs_name] = val

    # HubSpot datetime properties accept ISO-8601 (UTC).
    props[config.OUT_PROPS["updated_at"]] = datetime.datetime.now(
        datetime.timezone.utc
    ).isoformat()

    url = f"{config.HUBSPOT_BASE}/crm/v3/objects/contacts/{contact_id}"
    try:
        resp = requests.patch(
            url, headers=_headers(), json={"properties": props}, timeout=_TIMEOUT_S
        )
    except requests.RequestException as exc:
        raise HubSpotError(f"write contact {contact_id} failed: {exc}") from exc
    if resp.status_code not in (200, 201):
        raise HubSpotError(
            f"write contact {contact_id} -> {resp.status_code}: {resp.text[:300]}"
        )
    return resp.json()
