"""
Unit tests for the CRC Group quote-input mapping (pure, no browser/network).
These lock in the SOP-derived logic so it can't silently drift.

Run:  python -m app.test_crc
"""

from . import crc_client as crc


def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)


def test_risk_type():
    _assert(crc.risk_type_for_occupancy("primary") == "Owner Occupied Residential", "primary")
    _assert(crc.risk_type_for_occupancy("Seasonal") == "Seasonal Occupied Residential", "seasonal")
    _assert(crc.risk_type_for_occupancy("rental") == "Tenant/Rental", "rental")
    _assert(crc.risk_type_for_occupancy("") is None, "empty")
    _assert(crc.risk_type_for_occupancy("warehouse") is None, "unknown")


def test_construction():
    # veneer must win over the bare "brick" substring
    _assert(crc.crc_construction("Frame with Brick Veneer") == "Brick Veneer", "veneer")
    _assert(crc.crc_construction("Brick") == "Brick", "brick")
    _assert(crc.crc_construction("Wood Frame") == "Frame", "frame")
    _assert(crc.crc_construction("Steel") is None, "unknown -> None")
    _assert(crc.crc_construction(None) is None, "None")


def test_foundation():
    _assert(crc.crc_foundation("Concrete Slab") == "Slab on Grade", "slab")
    _assert(crc.crc_foundation("Full Basement") == "Foundation Wall", "basement")
    _assert(crc.crc_foundation("Crawlspace") == "Foundation Wall", "crawl")
    _assert(crc.crc_foundation(None) is None, "None")


def test_ale():
    _assert(crc.ale_from_building_limit(625000) == 62500, "10% of 625k")
    _assert(crc.ale_from_building_limit(0) is None, "zero")
    _assert(crc.ale_from_building_limit(None) is None, "None")


def test_pick_cheapest():
    quotes = [
        {"carrier": "A", "premium": 900, "total": 1000},
        {"carrier": "B", "premium": 750, "total": 880},
        {"carrier": "C", "premium": None, "total": None},
    ]
    _assert(crc.pick_cheapest(quotes)["carrier"] == "B", "cheapest is B")
    _assert(crc.pick_cheapest([]) is None, "empty")


def test_build_quote_inputs():
    contact = {"name": "Jane Doe", "street": "1 Main St", "zip": "33101", "state": "FL"}
    enriched = {
        "flood_zone": "AE", "year_built": 1998, "construction": "Wood Frame",
        "stories": 2.0, "sqft": 2200.0, "replacement_cost_est": 625000,
    }
    out = crc.build_quote_inputs(
        contact=contact, enriched=enriched, occupancy="primary",
        contents_limit=100000, prior_flood_losses=False,
        foundation_desc="Concrete Slab",
    )
    _assert(out["risk_type"] == "Owner Occupied Residential", out)
    _assert(out["over_water"] == "No", out)
    _assert(out["prior_flood_losses"] == "No", out)
    _assert(out["primary_construction"] == "Frame", out)
    _assert(out["foundation"] == "Slab on Grade", out)
    _assert(out["building_limit"] == 625000, out)
    _assert(out["additional_living_expense"] == 62500, out)
    _assert(out["deductible"] == 1000, out)
    _assert(out["flood_zone"] == "AE" and out["construction_year"] == 1998, out)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
        print(f"ok  {fn.__name__}")
    print(f"\n{len(fns)} passed")
