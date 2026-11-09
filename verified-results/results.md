# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T16:43:19.525790+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42657412395
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 58f75f786a59a40becb2e31a89a5aeb94d3eca7f
**Ledger generation:** 202 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.271e-06 | 93.507 | 98.103 | +6.55% | -0.08% | 0.58x | 3.8 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.779 | 92.821 | 98.861 | +10.72% | -0.26% | 0.53x | 2.3 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AAVE/USD | 131.71 | 91.600 | 78.105 | +4.57% | -0.30% | 2.67x | 7.6 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8499 | 90.819 | 79.582 | +3.60% | -0.48% | 2.36x | 1.2 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ONDO/USD | 0.37885 | 86.166 | 94.778 | +7.76% | -1.89% | 1.08x | 7.4 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | STRK/USD | 0.03952 | 81.516 | 75.535 | +6.52% | +0.28% | 1.46x | 7.6 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ARB/USD | 0.1806 | 80.890 | 82.504 | +8.86% | -0.93% | 1.30x | 11.1 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | JUP/USD | 0.25001 | 74.385 | 79.403 | +7.85% | +0.08% | 0.46x | 8.8 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ENA/USD | 0.1535 | 65.963 | 75.312 | +3.37% | -0.26% | 0.19x | 6.5 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PYTH/USD | 0.06469 | 65.462 | 72.695 | +7.58% | +0.43% | 0.06x | 10.8 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LTC/USD | 51.69 | 64.798 | 71.246 | +3.24% | -0.19% | 0.45x | 1.9 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | MON/USD | 0.01671 | 64.162 | 75.907 | +6.43% | -0.42% | 0.03x | 12.0 | 2026-11-09T16:43:10.722804+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 202; predictions: 1827; observations: 122119.
- Matured sampled outcomes across 1/6/24/48h: 1033; gap abstentions: 4931. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
