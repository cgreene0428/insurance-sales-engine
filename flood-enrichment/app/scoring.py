"""
Parse a National Flood Data response and compute:
  - a normalized set of fields for HubSpot
  - a flood risk score (0-100)
  - a replacement cost estimate ($)

All model knobs live in config.py. The functions here are pure (no I/O),
which makes them easy to unit-test against saved sample responses.
"""

from typing import Optional
from . import config


# --------------------------------------------------------------------------
# Extraction helpers - tolerant of missing/null fields in the NFD payload.
# --------------------------------------------------------------------------
def _safe_float(val) -> Optional[float]:
    try:
        if val is None:
            return None
        f = float(val)
        return f
    except (TypeError, ValueError):
        return None


def parse_nfd(payload: dict) -> dict:
    """Flatten the parts of the NFD response we care about into a flat dict."""
    result = payload.get("result", {}) or {}

    # Flood zone: first hazard-area record's fld_zone.
    # Floodway status lives in zone_subty (e.g. "FLOODWAY") on the same record.
    haz = result.get("flood.s_fld_haz_ar", []) or []
    fld_zone = haz[0].get("fld_zone") if haz else None
    zone_subty = (haz[0].get("zone_subty") or "") if haz else ""
    in_floodway = "FLOODWAY" in zone_subty.upper()

    elevation = result.get("elevation", {}) or {}
    prop_elev = _safe_float(elevation.get("propertyelevation"))
    if prop_elev == config.NFD_DATA_INVALID_ELEVATION:
        prop_elev = None

    # BFE: take the first base flood elevation value if present.
    bfe_list = elevation.get("flood.basefloodelevation", []) or []
    bfe = _safe_float(bfe_list[0].get("elevation")) if bfe_list else None

    # Nearest body of water distance (km).
    water = elevation.get("waterbody", []) or []
    dist_water = _safe_float(water[0].get("distkm")) if water else None

    # Storm surge: dict of {category: value-or-null}. Lowest category that
    # has a non-null value is the most-exposed category for the site.
    surge = elevation.get("stormsurge", {}) or {}
    surge_cat = None
    for cat in (1, 2, 3, 4, 5):
        if surge.get(str(cat)) is not None:
            surge_cat = cat
            break

    # Property data.
    prop = result.get("property", {}) or {}
    sqft = _safe_float(prop.get("sqft"))
    year_built = prop.get("yearbuilt")
    construction = prop.get("constructiondesc")
    stories = _safe_float(prop.get("storiescount")) or 1.0

    return {
        "flood_zone": fld_zone,
        "in_floodway": in_floodway,
        "property_elevation": prop_elev,
        "bfe": bfe,
        "dist_to_water_km": dist_water,
        "storm_surge_cat": surge_cat,
        "sqft": sqft,
        "year_built": year_built,
        "construction": construction,
        "stories": stories,
    }


# --------------------------------------------------------------------------
# Flood risk score
# --------------------------------------------------------------------------
def flood_risk_score(parsed: dict) -> int:
    zone = (parsed.get("flood_zone") or "").upper()
    score = config.ZONE_BASE_SCORE.get(zone, config.DEFAULT_ZONE_SCORE)

    # Storm surge exposure.
    cat = parsed.get("storm_surge_cat")
    if cat in config.SURGE_BONUS:
        score += config.SURGE_BONUS[cat]

    # Proximity to water (linear fade).
    dist = parsed.get("dist_to_water_km")
    if dist is not None and dist < config.PROXIMITY_CUTOFF_KM:
        frac = 1.0 - (dist / config.PROXIMITY_CUTOFF_KM)
        score += config.PROXIMITY_MAX_BONUS * frac

    # Elevation vs BFE.
    elev = parsed.get("property_elevation")
    bfe = parsed.get("bfe")
    if elev is not None and bfe is not None:
        if elev < bfe:
            score += config.ELEV_BELOW_BFE_PENALTY
        elif elev >= bfe + config.ELEV_SAFE_MARGIN_FT:
            score -= config.ELEV_ABOVE_BFE_CREDIT

    # Regulatory floodway = highest-hazard part of the floodplain.
    # Applied LAST as a multiplier so it scales the whole risk picture.
    if parsed.get("in_floodway"):
        score *= config.FLOODWAY_MULTIPLIER

    return int(max(0, min(100, round(score))))


# --------------------------------------------------------------------------
# Replacement cost estimate
# --------------------------------------------------------------------------
def replacement_cost(parsed: dict, state: Optional[str]) -> Optional[int]:
    sqft = parsed.get("sqft")
    if not sqft or sqft <= 0:
        return None  # can't estimate without floor area

    state_key = (state or "").upper()
    cost_psf = config.COST_PER_SQFT_BY_STATE.get(
        state_key, config.COST_PER_SQFT_BY_STATE["default"]
    )

    constr = (parsed.get("construction") or "").lower()
    constr_factor = config.CONSTRUCTION_FACTOR.get(
        constr, config.CONSTRUCTION_FACTOR["default"]
    )

    stories = parsed.get("stories") or 1.0
    s_factor = config.story_factor(stories)

    est = sqft * cost_psf * constr_factor * s_factor
    return int(round(est))


def enrich(payload: dict, state: Optional[str]) -> dict:
    """Full pipeline: parse -> score -> cost. Returns flat dict for HubSpot."""
    parsed = parse_nfd(payload)
    parsed["flood_risk_score"] = flood_risk_score(parsed)
    parsed["replacement_cost_est"] = replacement_cost(parsed, state)
    return parsed
