# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T05:38:02.781715+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42966770543
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 605207c0dbc59f0fadbdf94d9aa07c9644a3b326
**Ledger generation:** 266 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD | 2065.7 | 60.613 | 60.113 | +0.73% | +0.21% | 0.95x | 0.0 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 124.03 | 59.521 | 52.062 | +0.53% | +0.14% | 1.68x | 3.2 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ENA/USD | 0.1521 | 58.668 | 60.945 | +1.67% | -0.07% | 0.81x | 6.6 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.6437 | 57.669 | 64.369 | +1.67% | -0.06% | 0.36x | 4.7 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.427 | 55.946 | 58.324 | +0.73% | -0.15% | 0.84x | 3.6 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LTC/USD | 50.94 | 53.897 | 49.518 | +0.47% | +0.00% | 1.44x | 2.0 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TAO/USD | 220.0328 | 53.075 | 59.344 | +0.85% | +0.03% | 0.36x | 3.3 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | INJ/USD | 8.238 | 51.102 | 59.395 | +2.91% | -0.41% | 0.38x | 7.3 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ADA/USD | 0.174945 | 50.928 | 57.525 | +0.65% | +0.11% | 0.28x | 4.1 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8261 | 50.682 | 57.202 | +0.40% | +0.06% | 0.32x | 1.2 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PENGU/USD | 0.006218 | 47.660 | 33.301 | +0.32% | -0.13% | 3.37x | 3.2 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | POL/USD | 0.0888 | 28.038 | 34.041 | +0.53% | -0.11% | 0.46x | 3.4 | 2026-11-11T05:37:54.527614+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 266; predictions: 2469; observations: 159575.
- Matured sampled outcomes across 1/6/24/48h: 1727; gap abstentions: 6654. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
