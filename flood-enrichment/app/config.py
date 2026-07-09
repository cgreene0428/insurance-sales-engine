"""
Central configuration for the flood-enrichment service.

Everything you'll want to tune lives here: scoring weights, the cost model,
and the mapping to HubSpot property internal names. Change values here rather
than digging through the scoring logic.
"""

import os

# --------------------------------------------------------------------------
# Credentials / endpoints (set these in your .env file, never hard-code)
# --------------------------------------------------------------------------
HUBSPOT_ACCESS_TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN", "")
HUBSPOT_WEBHOOK_SECRET = os.environ.get("HUBSPOT_WEBHOOK_SECRET", "")  # app client secret, for signature validation
NFD_API_KEY = os.environ.get("NFD_API_KEY", "")

# Argenia portal login (set in .env, never hard-code).
ARGENIA_USERNAME = os.environ.get("ARGENIA_USERNAME", "")
ARGENIA_PASSWORD = os.environ.get("ARGENIA_PASSWORD", "")

# CRC Group (agent.crcgroup.com) portal login.
CRC_USERNAME = os.environ.get("CRC_USERNAME", "")
CRC_PASSWORD = os.environ.get("CRC_PASSWORD", "")

# CRC quote defaults + the HubSpot source properties that feed it.
CONTENTS_LIMIT_DEFAULT = 100000  # Step 8 Contents Limit

# DEAL property internal names read to build the CRC quote (deal-based trigger).
# CONFIRM these match your portal's actual internal names (Settings -> Properties).
DEAL_SOURCE_PROPS = {
    "address": "flood_risk_address",       # property address to quote/enrich
    "property_type": "property_type",      # -> CRC risk type (occupancy)
    "foundation_type": "foundation_type",  # -> CRC foundation type
}

HUBSPOT_BASE = "https://api.hubapi.com"
NFD_DATA_URL = "https://api.nationalflooddata.com/v3/data"

# HubSpot contact property internal names that hold the source address.
# Adjust if your portal uses different fields.
ADDRESS_FIELDS = {
    "street": "address",
    "city": "city",
    "state": "state",
    "zip": "zip",
}

# --------------------------------------------------------------------------
# HubSpot custom property internal names we WRITE back to.
# Create these on the contact object before running (see README).
# --------------------------------------------------------------------------
OUT_PROPS = {
    "flood_zone": "flood_zone",
    "in_floodway": "in_floodway",
    "bfe": "base_flood_elevation",
    "property_elevation": "property_elevation",
    "dist_to_water_km": "dist_to_water_km",
    "storm_surge_cat": "storm_surge_cat",
    "flood_risk_score": "flood_risk_score",
    "replacement_cost_est": "replacement_cost_est",
    "updated_at": "flood_data_updated_at",
}

# --------------------------------------------------------------------------
# FLOOD RISK SCORE model (0-100, higher = riskier). Tune freely.
# --------------------------------------------------------------------------
ZONE_BASE_SCORE = {
    "V": 90, "VE": 90,
    "A": 70, "AE": 70, "AH": 70, "AO": 70, "AR": 70,
    "X500": 35, "B": 35,          # 0.2% annual chance (shaded X)
    "X": 10, "C": 10,             # minimal risk
    "D": 50,                      # undetermined -> treat as moderate-unknown
}
DEFAULT_ZONE_SCORE = 50  # used if zone is missing/unrecognized

# Regulatory floodway: the channel that must stay clear to pass floodwater.
# Highest-hazard designation within the floodplain. Applied as a final
# multiplier on the summed score (e.g. 1.35 = +35%), then clamped to 100.
FLOODWAY_MULTIPLIER = 1.35

# Storm surge: NFD returns categories 1-5 (lowest cat that floods the site).
# A site that floods at cat 1 is the most exposed.
SURGE_BONUS = {1: 15, 2: 15, 3: 10, 4: 5, 5: 5}

# Proximity to nearest body of water (linear fade from MAX at 0km to 0 at CUTOFF).
PROXIMITY_MAX_BONUS = 10
PROXIMITY_CUTOFF_KM = 2.0

# Elevation vs BFE adjustment (feet).
ELEV_BELOW_BFE_PENALTY = 10   # property elevation below BFE
ELEV_ABOVE_BFE_CREDIT = 5     # property comfortably (>= margin ft) above BFE
ELEV_SAFE_MARGIN_FT = 3.0

# --------------------------------------------------------------------------
# REPLACEMENT COST model. Starter values - override per region.
# cost = sqft * cost_per_sqft * construction_factor * story_factor
# --------------------------------------------------------------------------
# Override per state/region; falls back to DEFAULT. Values are $/sqft.
COST_PER_SQFT_BY_STATE = {
    "FL": 165,
    "TX": 150,
    "LA": 155,
    "default": 160,
}

# NFD `constructiondesc` may arrive as a text label ("Wood Frame", "Masonry")
# or a numeric-ish code. Keys below are matched case-insensitively, first by
# exact match, then by keyword-substring (so "Masonry/Brick Veneer" -> masonry).
#
# BEST-EFFORT STARTER MAP — the exact set of NFD constructiondesc values is not
# verified here. Once you inspect real responses, add the precise labels/codes
# you actually see (especially any numeric codes, which only match exactly).
CONSTRUCTION_FACTOR = {
    "frame": 1.00,          # wood frame - baseline
    "wood": 1.00,
    "masonry": 1.10,        # masonry / brick
    "brick": 1.10,
    "masonry veneer": 1.05,
    "concrete": 1.15,
    "steel": 1.20,
    "fire resistive": 1.25,
    "manufactured": 0.90,   # manufactured / mobile home
    "mobile": 0.90,
    "default": 1.00,
}


def construction_factor(desc) -> float:
    """Resolve an NFD constructiondesc (text label OR numeric code) to a cost
    factor. Exact case-insensitive match first, then keyword-substring, else
    DEFAULT. Numeric/int codes only match if present as exact keys above.
    """
    if desc is None:
        return CONSTRUCTION_FACTOR["default"]
    key = str(desc).strip().lower()
    if not key:
        return CONSTRUCTION_FACTOR["default"]
    if key in CONSTRUCTION_FACTOR:
        return CONSTRUCTION_FACTOR[key]
    for token, factor in CONSTRUCTION_FACTOR.items():
        if token != "default" and token in key:
            return factor
    return CONSTRUCTION_FACTOR["default"]

# Extra cost for multi-story complexity.
def story_factor(stories: float) -> float:
    if stories >= 3:
        return 1.10
    if stories >= 2:
        return 1.05
    return 1.00

NFD_DATA_INVALID_ELEVATION = -1000000  # NFD sentinel for "no elevation"
