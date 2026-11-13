# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T09:06:18.031834+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43398472471
**Source SHA:** 033d5f24d0d0646676a64aeb13688c6f24766b47
**Previous ledger commit:** 04131aaa446adb659158efecf9ee9f1228673442 (atomic ledger/results publication)
**Ledger generation:** 355 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | UAI/USD | 0.03927 | 76.878 | 68.919 | +8.87% | +1.82% | 0.88x | 15.3 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.5238 | 71.699 | 75.131 | +3.04% | -0.16% | 0.74x | 2.3 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | INJ/USD | 7.623 | 63.566 | 56.942 | +2.19% | +1.14% | 1.09x | 7.9 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | KAS/USD | 0.02926 | 47.172 | 39.600 | +1.63% | +0.55% | 1.48x | 13.7 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | USELESS/USD | 0.136 | 46.804 | 48.389 | +3.03% | +0.99% | 0.35x | 25.9 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PONS/USD | 0.1571 | 41.080 | 51.639 | +3.90% | -0.69% | 0.29x | 12.7 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | W/USD | 0.00995 | 40.469 | 36.846 | +1.53% | -0.20% | 1.46x | 10.1 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ICP/USD | 2.615 | 35.690 | 42.977 | +1.59% | -0.76% | 0.65x | 7.7 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZRO/USD | 1.577 | 35.078 | 40.733 | +1.55% | +0.32% | 0.28x | 19.1 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SEI/USD | 0.04321 | 25.506 | 29.870 | +0.26% | +0.09% | 0.52x | 7.0 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | CAP/USD | 0.104407 | 20.457 | 27.128 | +0.81% | -0.31% | 0.49x | 21.6 | 2026-11-13T09:06:13.582908+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 355; predictions: 3271; observations: 213446.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9094. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
