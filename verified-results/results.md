# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T16:18:40.987255+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42653221585
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** ce6ad442f74c6967e27f5d5c7c3259d15ba691cc
**Ledger generation:** 201 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.276e-06 | 109.906 | 97.161 | +6.65% | -0.45% | 3.26x | 5.7 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.868 | 89.002 | 97.181 | +11.84% | -0.99% | 0.68x | 5.6 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ONDO/USD | 0.38738 | 87.027 | 92.677 | +10.18% | -0.43% | 0.65x | 9.0 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | BAT/USD | 0.13144 | 85.726 | 75.032 | +11.32% | -0.86% | 4.49x | 5.3 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AAVE/USD | 132.9 | 83.111 | 85.892 | +5.52% | -0.18% | 0.81x | 5.3 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | JUP/USD | 0.25 | 82.383 | 81.272 | +7.84% | -0.44% | 1.33x | 4.0 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MON/USD | 0.01674 | 80.716 | 75.921 | +6.62% | -2.04% | 66.54x | 12.0 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ARB/USD | 0.1823 | 79.516 | 85.169 | +9.89% | -0.54% | 0.71x | 5.5 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8554 | 75.984 | 84.279 | +4.27% | -1.29% | 0.82x | 1.2 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ENA/USD | 0.1552 | 73.210 | 83.357 | +4.51% | -1.14% | 0.56x | 6.5 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | UNI/USD | 6.9131 | 67.404 | 68.259 | +1.90% | -0.63% | 1.23x | 0.1 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XDG/USD | 0.0701704 | 65.514 | 68.143 | +1.88% | -0.71% | 1.09x | 0.0 | 2026-11-09T16:18:34.461542+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 201; predictions: 1815; observations: 121513.
- Matured sampled outcomes across 1/6/24/48h: 1033; gap abstentions: 4888. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
