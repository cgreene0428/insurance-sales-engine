"""
CRC Group Quick Quotes — flood quote automation + field mapping.

Portal flow (from the SOP "How to Create an Online Insurance Quote"):
  agent.crcgroup.com login -> Online Quoting > Flood -> Create a Quote
  -> Describe Your Risk ... -> Select Your Quote (quoting.crcgroup.com).

Two layers:
  1. PURE MAPPING (unit-tested below): turn our HubSpot + NFD data into the exact
     option strings CRC's form expects. Derived entirely from the written SOP, so
     it's verifiable without touching the site.
  2. BROWSER FLOW (CRCFloodQuoteProvider): drive the 9 SOP steps with Playwright.
     Field SELECTORS are TODO until a HAR / form HTML is captured, and are guarded
     so an unconfigured run fails loudly instead of silently.

Data sources:
  - applicant name + address  -> HubSpot contact
  - flood_zone / construction / year_built / stories / sqft / replacement_cost_est
                              -> scoring.enrich(NFD payload)
  - occupancy, contents_limit, foundation, prior_flood_losses -> see OPEN INPUTS
    (not derivable from NFD; must be supplied or defaulted — see module notes)
"""

from typing import Optional

# --------------------------------------------------------------------------
# PURE MAPPING — straight from the SOP. Unit-tested in test_crc.py.
# --------------------------------------------------------------------------

# Step 2 — RISK TYPE, chosen by how the property is occupied.
RISK_TYPE_BY_OCCUPANCY = {
    "primary": "Owner Occupied Residential",
    "owner": "Owner Occupied Residential",
    "secondary": "Seasonal Occupied Residential",
    "seasonal": "Seasonal Occupied Residential",
    "rental": "Tenant/Rental",
    "tenant": "Tenant/Rental",
}

# Step 8 — deductible is always $1,000 (higher barely moves the premium).
DEDUCTIBLE = 1000

# Deterministic underwriting answers (Steps 4, 5, 7) for a typical home.
FIXED_UW_ANSWERS = {
    "over_water": "No",             # Step 4 — always No
    "negatively_elevated": "No",    # Step 5
    "mobile_or_manufactured": "No",  # Step 5
    "elevated_above_ground": "No",  # Step 7 (typical home)
    "lowest_floor_height": 0,       # Step 7 — stays 0 when not elevated
}


def risk_type_for_occupancy(occupancy: Optional[str]) -> Optional[str]:
    """Map an occupancy label to the CRC RISK TYPE option. None if unknown."""
    if not occupancy:
        return None
    return RISK_TYPE_BY_OCCUPANCY.get(str(occupancy).strip().lower())


def crc_construction(desc) -> Optional[str]:
    """Step 7 Primary Construction. 'veneer' checked before 'brick' on purpose."""
    if not desc:
        return None
    d = str(desc).strip().lower()
    if "veneer" in d:
        return "Brick Veneer"
    if "brick" in d:
        return "Brick"
    if "frame" in d or "wood" in d:
        return "Frame"
    return None  # unknown construction -> leave for a human to pick


def crc_foundation(desc) -> Optional[str]:
    """Step 7 Foundation Type: slab -> Slab on Grade; basement/crawlspace -> Foundation Wall."""
    if not desc:
        return None
    d = str(desc).strip().lower()
    if "slab" in d:
        return "Slab on Grade"
    if "basement" in d or "crawl" in d:
        return "Foundation Wall"
    return None


def ale_from_building_limit(building_limit) -> Optional[int]:
    """Step 8 — Additional Living Expense defaults to 10% of the building limit."""
    if not building_limit or building_limit <= 0:
        return None
    return int(round(building_limit * 0.10))


def build_quote_inputs(
    *,
    contact: dict,
    enriched: dict,
    occupancy: Optional[str],
    contents_limit,
    prior_flood_losses: bool = False,
    foundation_desc: Optional[str] = None,
    effective_date: Optional[str] = None,
) -> dict:
    """Assemble every value the CRC form needs, from our data + the SOP defaults.

    `contact` is a HubSpot contact dict (name + street/city/state/zip); `enriched`
    is scoring.enrich() output. Returns a flat dict of form-field -> value. Fields
    that pre-fill in the portal (flood_zone, year, stories, sqft) are included for
    verification. None means "not determined — needs a human or another source".
    """
    building_limit = enriched.get("replacement_cost_est")
    return {
        # Step 2
        "risk_type": risk_type_for_occupancy(occupancy),
        # Step 3 — applicant (zip drives city/state/county auto-fill)
        "applicant_name": contact.get("name"),
        "zip": contact.get("zip"),
        "street": contact.get("street"),
        # Step 4
        "over_water": FIXED_UW_ANSWERS["over_water"],
        "prior_flood_losses": "Yes" if prior_flood_losses else "No",
        # Step 5
        "effective_date": effective_date,  # None => leave portal default (today)
        "negatively_elevated": FIXED_UW_ANSWERS["negatively_elevated"],
        "mobile_or_manufactured": FIXED_UW_ANSWERS["mobile_or_manufactured"],
        # Step 6 — NFIP (verify)
        "flood_zone": enriched.get("flood_zone"),
        "construction_year": enriched.get("year_built"),
        # Step 7 — building
        "primary_construction": crc_construction(enriched.get("construction")),
        "stories": enriched.get("stories"),
        "sqft": enriched.get("sqft"),
        "elevated_above_ground": FIXED_UW_ANSWERS["elevated_above_ground"],
        "lowest_floor_height": FIXED_UW_ANSWERS["lowest_floor_height"],
        "foundation": crc_foundation(foundation_desc),
        "building_replacement_cost": building_limit,
        # Step 8 — coverage & deductible
        "building_limit": building_limit,
        "contents_limit": contents_limit,
        "additional_living_expense": ale_from_building_limit(building_limit),
        "deductible": DEDUCTIBLE,
    }


def pick_cheapest(quotes: list) -> Optional[dict]:
    """Step 9 — choose the carrier with the lowest premium.

    `quotes` is a list of dicts each with at least {'carrier', 'premium', 'total'}.
    """
    valid = [q for q in (quotes or []) if q.get("premium") is not None]
    if not valid:
        return None
    return min(valid, key=lambda q: q["premium"])


# --------------------------------------------------------------------------
# BROWSER FLOW — SKELETON. Fill SELECTORS from a captured HAR / form HTML.
# --------------------------------------------------------------------------
from . import config  # noqa: E402

_HEADLESS = True
_TIMEOUT_MS = 45_000
_TODO = ""

# Every value here is a placeholder until a real session is captured.
LOGIN_URL = _TODO      # TODO: agent.crcgroup.com login page
SELECTORS = {
    "username": _TODO,
    "password": _TODO,
    "login_submit": _TODO,
    # Step 1-2 navigation + risk type, Step 3 applicant, ... one entry per field.
    "quote_number": _TODO,  # TODO: where the resulting quote id/number renders
}


class CRCError(RuntimeError):
    pass


def _require(value, what):
    if value is None or value == _TODO:
        raise CRCError(
            f"{what} is not configured yet — capture a HAR/form HTML from CRC and "
            f"fill in the selector/URL in crc_client.py before running."
        )
    return value


class CRCFloodQuoteProvider:
    """Drives the CRC 9-step flood quote flow. Returns the chosen quote result."""

    name = "crc_group"

    def get_flood_quote(self, inputs: dict) -> dict:
        """Run the flow with pre-built `inputs` (see build_quote_inputs).

        Returns {'carrier', 'premium', 'total', 'quote_number'} for the cheapest
        carrier. Raises CRCError on any unconfigured selector or missing result.
        """
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:  # pragma: no cover
            raise CRCError(
                "playwright not installed (pip install -r requirements.txt && "
                "playwright install chromium)"
            ) from exc
        if not config.ARGENIA_USERNAME:  # NOTE: CRC creds — see OPEN INPUTS below
            pass  # placeholder; CRC login creds env vars TBD (CRC_USERNAME/PASSWORD)

        _require(LOGIN_URL, "CRC login URL")
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=_HEADLESS)
            try:
                page = browser.new_page()
                page.set_default_timeout(_TIMEOUT_MS)
                page.goto(LOGIN_URL)
                # --- Login (Step 1) ---
                page.fill(_require(SELECTORS.get("username"), "CRC username"), _require(
                    getattr(config, "CRC_USERNAME", ""), "CRC_USERNAME env var"))
                page.fill(_require(SELECTORS.get("password"), "CRC password"), _require(
                    getattr(config, "CRC_PASSWORD", ""), "CRC_PASSWORD env var"))
                page.click(_require(SELECTORS.get("login_submit"), "CRC login button"))
                # --- Steps 2-8: fill the form from `inputs` ---
                # TODO: implement each SOP step against real selectors, e.g.
                #   page.select_option(SELECTORS["risk_type"], inputs["risk_type"])
                #   page.fill(SELECTORS["zip"], inputs["zip"])  # auto-fills city/state/county
                #   ... Steps 4-8 ...
                # --- Step 9: read carriers, pick cheapest ---
                # quotes = self._scrape_quotes(page)  # TODO from real table markup
                # chosen = pick_cheapest(quotes)
                raise CRCError(
                    "CRC form steps not implemented — selectors pending a captured "
                    "session. Mapping layer (build_quote_inputs/pick_cheapest) is ready."
                )
            finally:
                browser.close()
