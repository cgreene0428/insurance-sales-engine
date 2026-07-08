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


def _ci_get(d, key: str):
    """Case-insensitive single-key lookup in a dict. None if absent/not a dict."""
    if not isinstance(d, dict):
        return None
    if key in d:
        return d[key]
    lk = key.lower()
    for k, v in d.items():
        if isinstance(k, str) and k.lower() == lk:
            return v
    return None


def _dig(obj, path):
    """Resolve a logical key-path against an NFD payload whose nesting may be
    expressed EITHER as real sub-objects (result["elevation"]["propertyelevation"])
    OR as dotted, flattened keys (result["elevation.propertyElevation"]), in any
    letter case. `path` is a list of segments, e.g. ["elevation", "propertyelevation"].

    NOTE: this tolerance is best-effort. NFD's exact response shape/casing should
    still be confirmed against one real response before production use.
    """
    if obj is None or not path:
        return obj
    # Consume the first `take` segments as a single (possibly dotted) key, then
    # recurse on the remainder. Prefer longer joins so a fully-flattened dotted
    # key is matched before falling back to per-level nesting.
    for take in range(len(path), 0, -1):
        if not isinstance(obj, dict):
            break
        val = _ci_get(obj, ".".join(path[:take]))
        if val is not None:
            sub = _dig(val, path[take:])
            if sub is not None:
                return sub
    return None


def parse_nfd(payload: dict) -> dict:
    """Flatten the parts of the NFD response we care about into a flat dict.

    Field lookups go through _dig(), so they resolve whether NFD returns nested
    sub-objects or dotted top-level keys. All fields degrade to None on absence.
    """
    result = payload.get("result", {}) or {}

    # Flood zone: first hazard-area record's fld_zone.
    # Floodway status lives in zone_subty (e.g. "FLOODWAY") on the same record.
    haz = _dig(result, ["flood", "s_fld_haz_ar"]) or []
    fld_zone = haz[0].get("fld_zone") if haz else None
    zone_subty = (haz[0].get("zone_subty") or "") if haz else ""
    in_floodway = "FLOODWAY" in zone_subty.upper()

    prop_elev = _safe_float(_dig(result, ["elevation", "propertyelevation"]))
    if prop_elev == config.NFD_DATA_INVALID_ELEVATION:
        prop_elev = None

    # BFE: take the first base flood elevation value if present.
    bfe_list = _dig(result, ["elevation", "flood", "basefloodelevation"]) or []
    bfe = _safe_float(bfe_list[0].get("elevation")) if bfe_list else None

    # Nearest body of water distance. Prefer km; fall back to miles -> km.
    water = _dig(result, ["elevation", "waterbody"]) or []
    dist_water = None
    if water:
        rec = water[0]
        dist_water = _safe_float(rec.get("distkm"))
        if dist_water is None:
            miles = _safe_float(rec.get("distmiles"))
            dist_water = miles * 1.60934 if miles is not None else None

    # Storm surge: dict of {category: value-or-null}. Lowest category that
    # has a non-null value is the most-exposed category for the site.
    surge = _dig(result, ["elevation", "stormsurge"]) or {}
    surge_cat = None
    if isinstance(surge, dict):
        for cat in (1, 2, 3, 4, 5):
            if surge.get(str(cat), surge.get(cat)) is not None:  # str or int keys
                surge_cat = cat
                break

    # Property data.
    sqft = _safe_float(_dig(result, ["property", "sqft"]))
    year_built = _dig(result, ["property", "yearbuilt"])
    construction = _dig(result, ["property", "constructiondesc"])
    stories = _safe_float(_dig(result, ["property", "storiescount"])) or 1.0

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

    # Tolerant of text labels ("Frame") and numeric codes (5) alike; a raw
    # (parsed_construction).lower() would crash on an int constructiondesc.
    constr_factor = config.construction_factor(parsed.get("construction"))

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
