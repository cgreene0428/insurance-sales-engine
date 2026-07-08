"""
Unit tests for the pure scoring/parsing pipeline. No network, no I/O.

The two payloads below encode the SAME property two ways:
  - NESTED: sub-objects, e.g. result["elevation"]["propertyelevation"]
  - DOTTED: flattened top-level keys, e.g. result["elevation.propertyElevation"]
parse_nfd() must extract identical values from both, since NFD's exact
encoding hasn't been confirmed against a live response.

Run:  python -m pytest flood-enrichment  (or)  python flood-enrichment/app/test_scoring.py
"""

from . import config
from .scoring import parse_nfd, enrich


NESTED = {
    "result": {
        "flood.s_fld_haz_ar": [{"fld_zone": "AE", "zone_subty": "FLOODWAY"}],
        "elevation": {
            "propertyelevation": 8.0,
            "flood.basefloodelevation": [{"elevation": 11.0}],
            "waterbody": [{"distkm": 0.4}],
            "stormsurge": {"1": None, "2": 12.3, "3": 15.0},
        },
        "property": {
            "sqft": 2200,
            "yearbuilt": 1998,
            "constructiondesc": "Wood Frame",
            "storiescount": 2,
        },
    }
}

# Same data, expressed as dotted/flattened keys with different casing.
DOTTED = {
    "result": {
        "flood.s_fld_haz_ar": [{"fld_zone": "AE", "zone_subty": "FLOODWAY"}],
        "elevation.propertyElevation": 8.0,
        "elevation.flood.basefloodelevation": [{"elevation": 11.0}],
        "elevation.waterbody": [{"distkm": 0.4}],
        "elevation.stormsurge": {"1": None, "2": 12.3, "3": 15.0},
        "property.sqft": 2200,
        "property.yearbuilt": 1998,
        "property.constructiondesc": "Wood Frame",
        "property.storiescount": 2,
    }
}


def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)


def test_both_shapes_parse_identically():
    a = parse_nfd(NESTED)
    b = parse_nfd(DOTTED)
    _assert(a == b, f"nested vs dotted differ:\n{a}\n{b}")
    _assert(a["flood_zone"] == "AE", a)
    _assert(a["in_floodway"] is True, a)
    _assert(a["property_elevation"] == 8.0, a)
    _assert(a["bfe"] == 11.0, a)
    _assert(abs(a["dist_to_water_km"] - 0.4) < 1e-9, a)
    _assert(a["storm_surge_cat"] == 2, a)
    _assert(a["sqft"] == 2200.0, a)
    _assert(a["construction"] == "Wood Frame", a)
    _assert(a["stories"] == 2.0, a)


def test_miles_fallback_for_water_distance():
    payload = {"result": {"elevation": {"waterbody": [{"distmiles": 1.0}]}}}
    parsed = parse_nfd(payload)
    _assert(abs(parsed["dist_to_water_km"] - 1.60934) < 1e-6, parsed)


def test_invalid_elevation_sentinel_becomes_none():
    payload = {"result": {"elevation": {"propertyelevation": config.NFD_DATA_INVALID_ELEVATION}}}
    _assert(parse_nfd(payload)["property_elevation"] is None, "sentinel not nulled")


def test_construction_factor_label_and_code():
    # text label -> keyword-substring match
    _assert(config.construction_factor("Wood Frame") == 1.00, "frame label")
    _assert(config.construction_factor("Masonry/Brick") == 1.10, "masonry label")
    # numeric code must not crash (previously .lower() on an int did)
    _assert(config.construction_factor(5) == config.CONSTRUCTION_FACTOR["default"], "int code")
    _assert(config.construction_factor(None) == config.CONSTRUCTION_FACTOR["default"], "None")


def test_enrich_end_to_end():
    out = enrich(NESTED, "FL")
    # AE(70) + surge cat2(15) + prox(<2km) + below-BFE(10), *floodway 1.35, clamp 100
    _assert(out["flood_risk_score"] == 100, out)
    # 2200 sqft * $165 (FL) * 1.00 (frame) * 1.05 (2-story)
    _assert(out["replacement_cost_est"] == 381150, out)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
        print(f"ok  {fn.__name__}")
    print(f"\n{len(fns)} passed")
