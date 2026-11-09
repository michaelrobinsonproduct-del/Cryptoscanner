# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T19:24:45.801505+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42682907680
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** de7edaa75f82bdd6004b3d622d640a6225470f95
**Ledger generation:** 206 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD | 0.37393 | 92.912 | 94.948 | +6.36% | -0.40% | 0.99x | 9.1 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.508 | 92.462 | 96.471 | +7.30% | -0.48% | 0.84x | 7.1 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01688 | 91.142 | 79.378 | +7.52% | -0.65% | 30.01x | 5.9 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1553 | 82.047 | 83.830 | +4.58% | -0.19% | 0.92x | 6.4 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 224.5764 | 81.961 | 77.307 | +3.61% | -0.08% | 1.51x | 5.9 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.85 | 80.183 | 79.667 | +3.61% | -0.07% | 1.09x | 1.2 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PEPE/USD | 5.122e-06 | 76.611 | 74.877 | +3.54% | -0.54% | 1.45x | 9.8 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | JUP/USD | 0.25542 | 76.268 | 83.590 | +10.18% | -0.72% | 0.63x | 11.8 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ARB/USD | 0.178 | 75.966 | 82.348 | +7.29% | +0.00% | 0.36x | 11.3 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | UNI/USD | 7.0274 | 73.209 | 75.708 | +3.59% | -0.24% | 0.87x | 8.8 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LINK/USD | 10.6713 | 73.091 | 73.124 | +2.60% | -0.02% | 1.01x | 0.1 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XLM/USD | 0.146806 | 53.282 | 56.791 | +0.43% | -0.19% | 0.74x | 2.4 | 2026-11-09T19:24:37.383236+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 206; predictions: 1875; observations: 124543.
- Matured sampled outcomes across 1/6/24/48h: 1081; gap abstentions: 5061. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
