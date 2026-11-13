# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T21:40:57.081163+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43512783936
**Source SHA:** 08c6443b5e44e9625fffa893e3b1c6858a776208
**Previous ledger commit:** 59b2f641407ff3cafa495502194fd386e00bf00c (atomic ledger/results publication)
**Ledger generation:** 367 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 22.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.053 | 94.554 | 95.653 | +7.95% | -0.25% | 1.01x | 8.7 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UAI/USD | 0.03857 | 85.563 | 69.355 | +6.93% | +0.36% | 2.44x | 15.5 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TAO/USD | 215.3672 | 81.216 | 63.311 | +1.63% | +0.58% | 5.75x | 6.2 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.4879 | 66.695 | 65.763 | +1.99% | -0.49% | 1.34x | 6.3 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.0468 | 56.827 | 57.834 | +1.98% | +0.39% | 0.71x | 12.8 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | STX/USD | 0.2881 | 49.163 | 36.925 | +1.12% | -0.55% | 3.77x | 6.9 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PEARL/USD | 1.4703 | 48.310 | 52.200 | +3.01% | -0.43% | 0.83x | 0.7 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZBCN/USD | 0.001856 | 47.366 | 55.531 | +8.67% | -0.64% | 0.50x | 43.3 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | VVV/USD | 19.181 | 42.927 | 44.628 | +1.00% | -0.92% | 1.29x | 6.8 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | CAP/USD | 0.106802 | 41.171 | 42.593 | +3.12% | +0.05% | 0.83x | 33.3 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | RENDER/USD | 1.535 | 33.609 | 37.289 | +0.85% | -0.33% | 0.79x | 6.5 | 2026-11-13T21:40:48.785429+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 367; predictions: 3405; observations: 220724.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9778. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
