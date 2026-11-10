# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T02:57:36.903906+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42746096486
**Source SHA:** 54cbedb0b79308fa50f17420a7e93d57841d3dd2
**Ledger commit:** d318337722b3c14519ea9e7eb9539a1fad9b309d
**Ledger generation:** 224 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 493; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.093 | 72.528 | 61.615 | +5.10% | -0.82% | 6.70x | 18.3 | 2026-11-10T02:57:32.191455+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ONDO/USD | 0.37455 | 69.918 | 51.887 | +0.27% | +0.61% | 8.41x | 0.3 | 2026-11-10T02:57:32.191455+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | CAP/USD | 0.0998 | 45.518 | 35.877 | +0.95% | -0.05% | 1.99x | 6.1 | 2026-11-10T02:57:32.191455+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SHX/USD | 0.004214 | 25.545 | 21.851 | +0.74% | -0.26% | 1.50x | 28.5 | 2026-11-10T02:57:32.191455+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 224; predictions: 2054; observations: 134835.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5506. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
