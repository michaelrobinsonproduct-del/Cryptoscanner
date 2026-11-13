# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T23:25:41.374855+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43526978480
**Source SHA:** bd8cc49493424e088d54e2300244a55aae5ce78d
**Previous ledger commit:** c4e6cf10831be43aa2fffcb34ad5cfd1ca245b92 (atomic ledger/results publication)
**Ledger generation:** 370 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 12.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.992 | 111.682 | 96.244 | +7.13% | +0.09% | 5.01x | 7.5 | 2026-11-13T23:25:37.252544+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TAO/USD | 213.2237 | 71.490 | 54.331 | +0.62% | +0.76% | 2.34x | 10.0 | 2026-11-13T23:25:37.252544+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | UAI/USD | 0.0387 | 70.578 | 71.975 | +7.29% | +0.26% | 0.73x | 10.4 | 2026-11-13T23:25:37.252544+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04649 | 65.610 | 57.080 | +1.31% | -0.24% | 1.97x | 4.3 | 2026-11-13T23:25:37.252544+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ZBCN/USD | 0.001809 | 52.895 | 54.153 | +5.91% | +0.00% | 0.87x | 38.8 | 2026-11-13T23:25:37.252544+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 370; predictions: 3418; observations: 222545.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9893. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
