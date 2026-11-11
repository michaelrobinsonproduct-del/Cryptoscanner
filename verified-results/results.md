# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T12:35:58.879612+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43021376788
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 6e903742a19a9e7a47aa1980ca131f1bef50329b
**Ledger generation:** 280 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.226 | 110.055 | 79.456 | +7.64% | +3.12% | 2.66x | 16.3 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XMR/USD | 575.07 | 66.517 | 66.552 | +2.21% | -0.41% | 1.20x | 7.8 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SOL/USD | 83.66 | 65.925 | 57.934 | +0.50% | -0.27% | 1.94x | 1.2 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.7187 | 65.868 | 79.468 | +3.76% | -1.39% | 0.34x | 3.8 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.488 | 61.976 | 62.853 | +1.46% | -0.88% | 1.35x | 4.7 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TAO/USD | 219.1465 | 56.491 | 56.306 | +0.45% | -0.19% | 1.11x | 3.6 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | NIGHT/USD | 0.04383 | 55.165 | 70.804 | +4.56% | -1.62% | 0.24x | 11.4 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PENGU/USD | 0.0063 | 54.391 | 40.498 | +1.65% | -0.22% | 4.45x | 7.9 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | CC/USD | 0.09178 | 54.288 | 54.648 | +2.57% | -1.21% | 1.57x | 5.4 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.146643 | 51.673 | 57.394 | +1.42% | -0.74% | 0.80x | 3.9 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ADA/USD | 0.175458 | 51.598 | 59.656 | +0.95% | -0.68% | 0.53x | 4.0 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SUI/USD | 0.8268 | 50.312 | 57.799 | +0.49% | -0.54% | 0.52x | 1.2 | 2026-11-11T12:35:50.059293+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 280; predictions: 2628; observations: 168013.
- Matured sampled outcomes across 1/6/24/48h: 1908; gap abstentions: 6961. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
