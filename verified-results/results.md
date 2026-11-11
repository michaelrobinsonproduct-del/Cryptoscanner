# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T18:04:33.279521+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43073896503
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** e19d13fe74e01c1ed548fe81d5ccf68ed606785b
**Ledger generation:** 292 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 16s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 590.57 | 93.192 | 83.738 | +4.96% | -0.61% | 2.25x | 12.0 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TON/USD | 1.222 | 92.087 | 75.028 | +7.29% | +0.41% | 2.51x | 32.8 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NPC/USD | 0.014495 | 90.556 | 75.556 | +6.46% | +0.00% | 3.03x | 0.7 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.7462 | 80.427 | 84.984 | +4.53% | -0.65% | 0.87x | 3.5 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.17881 | 75.098 | 70.504 | +2.88% | -0.28% | 1.60x | 5.8 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.150781 | 73.540 | 76.375 | +4.28% | -0.46% | 0.94x | 3.6 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SUI/USD | 0.8438 | 67.329 | 72.273 | +2.55% | -0.52% | 0.76x | 1.2 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 8.653 | 66.445 | 76.124 | +3.43% | -0.58% | 0.32x | 5.8 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SOL/USD | 85.31 | 63.157 | 71.821 | +2.49% | -0.35% | 0.31x | 1.2 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ETH/USD | 2088.89 | 60.773 | 67.958 | +1.86% | -0.19% | 0.38x | 0.2 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XRP/USD | 1.06844 | 60.258 | 63.797 | +1.26% | -0.33% | 0.81x | 0.1 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HYPE/USD | 73.89 | 59.963 | 69.156 | +2.31% | -0.28% | 0.22x | 4.1 | 2026-11-11T18:04:17.772762+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 292; predictions: 2772; observations: 175273.
- Matured sampled outcomes across 1/6/24/48h: 2123; gap abstentions: 7245. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
