# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T22:00:23.853105+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42910124409
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 6b26ecb1482fa9cda40b11c840cc0dea006ede44
**Ledger generation:** 251 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 19.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.152 | 99.613 | 77.031 | +10.77% | +3.03% | 1.74x | 8.7 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | LIGHTER/USD | 3.478 | 90.089 | 74.079 | +7.58% | +0.20% | 2.51x | 11.5 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | UAI/USD | 0.04176 | 69.632 | 61.081 | +8.30% | -0.36% | 2.03x | 33.6 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.258e-06 | 62.014 | 63.126 | +2.66% | +0.40% | 0.69x | 20.9 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.0418 | 57.792 | 60.347 | +3.26% | -0.19% | 0.84x | 12.0 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ZRO/USD | 1.511 | 53.022 | 47.477 | +2.37% | +1.21% | 0.95x | 26.5 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SYRUP/USD | 0.13804 | 52.725 | 33.745 | +1.88% | +0.80% | 45.14x | 21.8 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | FET/USD | 0.1442 | 41.550 | 23.760 | +0.28% | +0.56% | 3.68x | 20.8 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | RENDER/USD | 1.596 | 36.328 | 26.215 | +0.31% | +1.01% | 1.50x | 18.8 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ATOM/USD | 1.3907 | 29.306 | 31.962 | +1.45% | +0.01% | 0.73x | 20.1 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | MEGA/USD | 0.0508 | 25.484 | 27.180 | +2.03% | -0.61% | 1.13x | 39.5 | 2026-11-10T22:00:17.128418+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 251; predictions: 2307; observations: 150560.
- Matured sampled outcomes across 1/6/24/48h: 1427; gap abstentions: 6348. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
