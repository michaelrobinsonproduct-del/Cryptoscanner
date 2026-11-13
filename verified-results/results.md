# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T15:43:11.081341+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43455344004
**Source SHA:** 724af27bedfcc5e759528bd81b2c6f20541964a7
**Previous ledger commit:** 0d5b5be2480cb1449ee95b57e71816575ce73cd6 (atomic ledger/results publication)
**Ledger generation:** 361 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.006 | 104.558 | 94.912 | +7.32% | -1.04% | 2.49x | 10.0 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.4521 | 67.061 | 55.935 | +0.94% | -0.77% | 2.75x | 11.3 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | CAP/USD | 0.106125 | 44.218 | 40.394 | +2.47% | -0.22% | 1.49x | 26.3 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ICP/USD | 2.59 | 38.107 | 38.867 | +0.62% | -0.27% | 1.06x | 3.9 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | W/USD | 0.00993 | 36.385 | 35.589 | +1.33% | -0.30% | 1.23x | 10.1 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UAI/USD | 0.03649 | 32.009 | 30.136 | +1.16% | -0.27% | 1.32x | 19.2 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PIEVERSE/USD | 1.6841 | 31.154 | 37.819 | +2.58% | -1.06% | 0.86x | 22.6 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PENDLE/USD | 1.537 | 29.070 | 34.196 | +1.39% | -0.84% | 0.91x | 13.0 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BABY/USD | 0.0097 | 20.571 | 24.281 | +1.15% | -0.41% | 0.83x | 31.0 | 2026-11-13T15:43:05.639101+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 361; predictions: 3335; observations: 217084.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9437. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
