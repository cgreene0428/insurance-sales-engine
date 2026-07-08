"""
National Flood Data API client (single-address, client-side rate-limited).

One `addressparcel` call with the elevation + property add-ons returns
everything scoring.py needs. Returns the raw JSON dict; scoring.parse_nfd()
handles the shape.

SCAFFOLD: the exact param names/add-on flags follow the README and NFD docs
but have not been exercised against the live API from here (sandbox blocks the
host). Confirm params + response shape against one real call before production.
"""

import threading
import time

import requests

from . import config

_TIMEOUT_S = 30
_MIN_INTERVAL_S = 0.25  # ~4 req/s ceiling; NFD plans are metered
_lock = threading.Lock()
_last_call = [0.0]


class NFDError(RuntimeError):
    """Raised on any non-200 or transport failure talking to NFD."""


def _throttle() -> None:
    with _lock:
        wait = _MIN_INTERVAL_S - (time.monotonic() - _last_call[0])
        if wait > 0:
            time.sleep(wait)
        _last_call[0] = time.monotonic()


def fetch_address(
    address: str,
    *,
    elevation: bool = True,
    property_: bool = True,
    loma: bool = True,
) -> dict:
    """Fetch flood + elevation + property data for one address.

    Returns the decoded JSON payload (with its top-level "result" block).
    Raises NFDError on failure.
    """
    if not config.NFD_API_KEY:
        raise NFDError("NFD_API_KEY is not set (see .env)")
    if not address:
        raise NFDError("empty address")

    params = {"address": address, "searchtype": "addressparcel"}
    if loma:
        params["loma"] = "true"
    if elevation:
        params["elevation"] = "true"
    if property_:
        params["property"] = "true"

    _throttle()
    try:
        resp = requests.get(
            config.NFD_DATA_URL,
            params=params,
            headers={"x-api-key": config.NFD_API_KEY},
            timeout=_TIMEOUT_S,
        )
    except requests.RequestException as exc:
        raise NFDError(f"NFD request failed: {exc}") from exc

    if resp.status_code != 200:
        raise NFDError(f"NFD returned {resp.status_code}: {resp.text[:300]}")
    try:
        return resp.json()
    except ValueError as exc:
        raise NFDError(f"NFD returned non-JSON body: {resp.text[:300]}") from exc
