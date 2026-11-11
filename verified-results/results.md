# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T05:00:08.876917+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42962598670
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 88120f42d6faf5851e25ea5c45de4fa83f12c0cb
**Ledger generation:** 265 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ENA/USD | 0.1528 | 73.721 | 61.001 | +2.14% | -0.46% | 7.71x | 13.1 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ETH/USD | 2061.77 | 72.811 | 58.772 | +0.54% | -0.19% | 2.77x | 0.0 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TAO/USD | 219.7504 | 71.944 | 58.376 | +0.72% | -0.29% | 6.30x | 3.4 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8266 | 69.615 | 57.023 | +0.46% | -0.48% | 8.49x | 2.4 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | LINK/USD | 10.35346 | 64.573 | 51.985 | +0.68% | -0.35% | 2.43x | 2.9 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NEAR/USD | 3.6642 | 64.539 | 68.793 | +2.24% | -0.40% | 0.78x | 3.8 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AAVE/USD | 123.72 | 63.877 | 50.729 | +0.28% | -0.37% | 3.95x | 2.4 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | INJ/USD | 8.28 | 59.188 | 63.882 | +3.44% | -0.20% | 0.63x | 6.0 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PYTH/USD | 0.06946 | 54.302 | 66.605 | +6.11% | -0.77% | 0.16x | 17.3 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | NIGHT/USD | 0.04306 | 52.846 | 60.720 | +2.72% | -0.14% | 0.28x | 4.7 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SPX/USD | 0.3726 | 51.631 | 56.832 | +3.10% | -0.21% | 0.59x | 2.7 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LTC/USD | 50.98 | 51.514 | 50.066 | +0.55% | -0.22% | 1.25x | 2.0 | 2026-11-11T05:00:00.685366+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 265; predictions: 2457; observations: 158973.
- Matured sampled outcomes across 1/6/24/48h: 1703; gap abstentions: 6635. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
