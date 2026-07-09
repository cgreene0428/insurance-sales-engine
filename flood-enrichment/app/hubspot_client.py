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


def _get_contact_name(contact_id: str) -> str:
    """Read firstname/lastname for a contact and join them."""
    url = f"{config.HUBSPOT_BASE}/crm/v3/objects/contacts/{contact_id}"
    try:
        resp = requests.get(
            url, headers=_headers(),
            params={"properties": "firstname,lastname"}, timeout=_TIMEOUT_S,
        )
    except requests.RequestException as exc:
        raise HubSpotError(f"read contact name {contact_id} failed: {exc}") from exc
    if resp.status_code != 200:
        raise HubSpotError(
            f"read contact name {contact_id} -> {resp.status_code}: {resp.text[:300]}"
        )
    p = resp.json().get("properties", {}) or {}
    return " ".join(x for x in (p.get("firstname"), p.get("lastname")) if x).strip()


def get_deal_quote_data(deal_id: str) -> dict:
    """Read the CRC-quote source fields from a deal (deal-based trigger).

    Returns {address, property_type, foundation_type, name} where address/
    property_type/foundation_type come from deal properties (DEAL_SOURCE_PROPS)
    and name comes from the deal's primary associated contact.
    """
    props = list(config.DEAL_SOURCE_PROPS.values())
    url = f"{config.HUBSPOT_BASE}/crm/v3/objects/deals/{deal_id}"
    try:
        resp = requests.get(
            url, headers=_headers(),
            params={"properties": ",".join(props), "associations": "contacts"},
            timeout=_TIMEOUT_S,
        )
    except requests.RequestException as exc:
        raise HubSpotError(f"read deal {deal_id} failed: {exc}") from exc
    if resp.status_code != 200:
        raise HubSpotError(
            f"read deal {deal_id} -> {resp.status_code}: {resp.text[:300]}"
        )

    body = resp.json()
    p = body.get("properties", {}) or {}
    data = {logical: p.get(hs_name) for logical, hs_name in config.DEAL_SOURCE_PROPS.items()}

    data["name"] = None
    results = (((body.get("associations") or {}).get("contacts") or {}).get("results") or [])
    if results and results[0].get("id"):
        data["name"] = _get_contact_name(results[0]["id"])
    return data


# HUBSPOT_DEFINED association type id for Note -> Deal.
_NOTE_TO_DEAL_ASSOC_TYPE_ID = 214


def add_note_to_deal(deal_id: str, body: str) -> dict:
    """Create a Note engagement with `body` and associate it to a Deal.

    Used to drop the Private Market Flood quote number onto the deal record.
    Returns the created note object.
    """
    if not deal_id:
        raise HubSpotError("deal_id is required")
    payload = {
        "properties": {
            "hs_note_body": body,
            # HubSpot requires a timestamp on notes (ISO-8601 UTC accepted).
            "hs_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        },
        "associations": [
            {
                "to": {"id": str(deal_id)},
                "types": [
                    {
                        "associationCategory": "HUBSPOT_DEFINED",
                        "associationTypeId": _NOTE_TO_DEAL_ASSOC_TYPE_ID,
                    }
                ],
            }
        ],
    }
    url = f"{config.HUBSPOT_BASE}/crm/v3/objects/notes"
    try:
        resp = requests.post(url, headers=_headers(), json=payload, timeout=_TIMEOUT_S)
    except requests.RequestException as exc:
        raise HubSpotError(f"create note on deal {deal_id} failed: {exc}") from exc
    if resp.status_code not in (200, 201):
        raise HubSpotError(
            f"create note on deal {deal_id} -> {resp.status_code}: {resp.text[:300]}"
        )
    return resp.json()
