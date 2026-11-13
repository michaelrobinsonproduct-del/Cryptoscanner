# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T23:13:27.849525+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43525430238
**Source SHA:** 4ba1e881181af600d22f8244a9e8f0c02f579e51
**Previous ledger commit:** aeec49e7f8926d150fab3e0e39a0d06d5eb4f8e0 (atomic ledger/results publication)
**Ledger generation:** 369 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 13.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.973 | 107.732 | 94.353 | +6.88% | -0.32% | 4.02x | 11.3 | 2026-11-13T23:13:24.234430+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UAI/USD | 0.03858 | 67.716 | 71.935 | +6.96% | -0.77% | 0.96x | 10.4 | 2026-11-13T23:13:24.234430+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04658 | 53.800 | 58.479 | +1.50% | -0.09% | 0.57x | 4.3 | 2026-11-13T23:13:24.234430+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ZBCN/USD | 0.001814 | 42.739 | 53.509 | +6.21% | -1.09% | 0.47x | 44.2 | 2026-11-13T23:13:24.234430+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 369; predictions: 3413; observations: 221938.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9893. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
