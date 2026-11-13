# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T20:29:17.836783+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43501917710
**Source SHA:** 08c6443b5e44e9625fffa893e3b1c6858a776208
**Previous ledger commit:** 780b5279cea61b88ce1628b0017c24f22d89ff04 (atomic ledger/results publication)
**Ledger generation:** 366 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.132 | 83.987 | 96.309 | +9.01% | -1.55% | 0.54x | 7.4 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04646 | 75.511 | 58.678 | +1.24% | +0.37% | 3.36x | 2.2 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.5285 | 73.102 | 75.386 | +3.18% | -0.30% | 0.92x | 3.7 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | UAI/USD | 0.03918 | 65.618 | 69.474 | +8.62% | +0.26% | 0.49x | 15.3 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 216.3298 | 56.202 | 66.465 | +2.08% | -0.42% | 0.18x | 6.2 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | VVV/USD | 19.603 | 54.032 | 59.049 | +3.22% | +0.39% | 0.30x | 9.2 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PUMP/USD | 0.003527 | 53.843 | 58.145 | +1.26% | -0.17% | 0.65x | 11.4 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 8.376 | 51.103 | 56.667 | +0.32% | -0.37% | 0.63x | 1.2 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZEC/USD | 961.65 | 48.368 | 55.091 | +0.60% | +0.01% | 0.32x | 8.2 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | QNT/USD | 164.61 | 40.908 | 47.827 | +0.61% | -0.39% | 0.50x | 8.5 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | DASH/USD | 41.494 | 35.521 | 32.744 | +0.30% | +0.15% | 1.20x | 4.8 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | BCH/USD | 226.16 | 33.353 | 41.945 | +0.49% | +0.08% | 0.10x | 5.8 | 2026-11-13T20:29:09.025608+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 366; predictions: 3394; observations: 220117.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9739. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
