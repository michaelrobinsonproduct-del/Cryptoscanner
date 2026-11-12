# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T03:39:02.481368+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43149433226
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b1e4a91941b7e70673bf180d3d3b1c6083ea211d
**Ledger generation:** 311 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 20.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 984.02 | 82.234 | 69.533 | +2.29% | -0.46% | 9.09x | 2.9 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.596e-06 | 65.437 | 66.488 | +1.95% | +0.04% | 0.87x | 4.4 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.02939 | 60.984 | 42.030 | +1.14% | +0.79% | 14.77x | 6.8 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.584 | 51.977 | 58.590 | +0.85% | -0.17% | 0.43x | 4.7 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CC/USD | 0.0909 | 44.095 | 36.237 | +0.32% | -0.44% | 2.00x | 6.6 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PUMP/USD | 0.003478 | 37.318 | 40.845 | +0.49% | +0.09% | 0.60x | 8.6 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | DOT/USD | 0.8438 | 35.175 | 38.990 | +0.62% | -0.19% | 0.71x | 2.4 | 2026-11-12T03:38:55.210432+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 311; predictions: 2976; observations: 186783.
- Matured sampled outcomes across 1/6/24/48h: 2357; gap abstentions: 7844. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
