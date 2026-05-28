# Flood Insurance Guru — Property & Flood Enrichment Service

Replaces the HazardHub integration. On a HubSpot contact address change, this
service pulls flood + property data from **National Flood Data (NFD)**, computes
a **flood risk score** and a **replacement cost estimate**, and writes both back
to the contact — all from a single NFD API call.

## Why this is cheaper than HazardHub (~$6k/yr)

One NFD `addressparcel` call with the `property` and `elevation` add-ons returns
flood zone, BFE, property elevation, distance to water, storm-surge category,
**and** property attributes (sqft, year built, construction, stories). That one
feed powers both your risk score and your cost estimator — no separate property
data vendor needed.

-----

## 1. Prerequisites

- **National Flood Data** account with an API key. Confirm your plan includes the
  `property` and `elevation` add-ons (the docs flag them “special key required”).
- **HubSpot Private App** token (legacy API keys are deprecated). Scopes needed:
  - `crm.objects.contacts.read`
  - `crm.objects.contacts.write`
  - Copy the app’s **Client secret** too — used to validate webhook signatures.

## 2. Create the HubSpot custom properties (one-time)

On the **Contact** object, create these properties (Settings → Properties).
Internal names must match `OUT_PROPS` in `app/config.py`:

|Internal name          |Field type               |
|-----------------------|-------------------------|
|`flood_zone`           |Single-line text         |
|`in_floodway`          |Single checkbox (boolean)|
|`base_flood_elevation` |Number                   |
|`property_elevation`   |Number                   |
|`dist_to_water_km`     |Number                   |
|`storm_surge_cat`      |Number                   |
|`flood_risk_score`     |Number                   |
|`replacement_cost_est` |Number                   |
|`flood_data_updated_at`|Date picker (datetime)   |

## 3. Configure & run

```bash
cp .env.example .env      # fill in your three secrets
pip install -r requirements.txt
python -m app.server      # dev server on :8000
```

Production:

```bash
gunicorn -w 2 -b 0.0.0.0:8000 app.server:app
```

Deploy behind HTTPS (Render, Fly.io, Cloud Run, etc.).

## 4. Wire up the HubSpot webhook

Easiest path — a **Workflow**:

1. Create a contact-based workflow, enrollment trigger = “Address is known / has
   changed”.
1. Add action **Send a webhook** → POST to `https://YOUR_HOST/webhook/hubspot`.

The handler reads `objectId` from the payload, so the default contact webhook
body works. Signature validation uses `X-HubSpot-Signature-V3` + your client
secret.

## 5. Tune the models

Everything lives in `app/config.py`:

- `ZONE_BASE_SCORE`, `SURGE_BONUS`, proximity + elevation weights → risk score.
- `FLOODWAY_MULTIPLIER` (default 1.35) → applied last, scales the summed score by +35% when the parcel is in a regulatory floodway, then clamps to 100.
- `COST_PER_SQFT_BY_STATE`, `CONSTRUCTION_FACTOR`, `story_factor()` → cost model.

Inspect a few real NFD responses first, then refine `CONSTRUCTION_FACTOR` (the
`constructiondesc` field is a code you’ll want to map) and your $/sqft by region.

## Files

- `app/config.py` — all tunable knobs + property mapping
- `app/nfd_client.py` — National Flood Data call (rate-limited)
- `app/scoring.py` — parse + risk score + cost (pure, unit-testable)
- `app/hubspot_client.py` — read address / write enriched props
- `app/server.py` — webhook receiver + signature validation

## Notes / next steps

- High volume? Move `process_contact` onto a queue (Redis/RQ, SQS) and return 200
  immediately so HubSpot never retries.
- Want a nightly safety-net batch for contacts that slipped through? The NFD
  `/v3/databatch` endpoint takes up to 20k addresses — easy to add later.
- Replacement cost here is directional. For carrier-grade numbers you’d layer in
  Verisk 360Value or CoreLogic RCT, but this is defensible for triage/quoting.
