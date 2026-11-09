# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T22:42:06.261827+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42713981935
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** 6e210c9265daa9559a9f495ecff8405238de55d1
**Ledger generation:** 214 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD | 0.37681 | 104.903 | 98.184 | +7.18% | +1.10% | 1.12x | 0.5 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.653 | 101.074 | 96.531 | +9.13% | +0.41% | 1.25x | 6.9 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | VVV/USD | 22.026 | 93.092 | 78.433 | +9.80% | -0.07% | 3.95x | 6.8 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | UNI/USD | 7.063 | 88.672 | 82.100 | +4.11% | +0.86% | 1.23x | 3.4 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 223.3969 | 86.154 | 76.143 | +3.06% | +0.63% | 1.69x | 0.6 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 5.147e-06 | 84.389 | 81.355 | +4.04% | +1.54% | 0.54x | 3.9 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDG/USD | 0.0700163 | 84.151 | 66.577 | +1.65% | +0.51% | 3.29x | 0.0 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.1549 | 81.445 | 78.257 | +4.31% | +0.91% | 0.86x | 6.5 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XBT/USD | 75208.9 | 76.091 | 59.362 | +0.62% | +0.35% | 2.54x | 0.0 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8472 | 73.702 | 77.276 | +3.27% | +0.42% | 0.43x | 1.2 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | NEAR/USD | 3.643 | 69.684 | 67.624 | +1.86% | +0.24% | 1.09x | 0.8 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LINK/USD | 10.68186 | 68.364 | 73.263 | +2.70% | +0.44% | 0.29x | 1.2 | 2026-11-09T22:41:59.213696+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 214; predictions: 1971; observations: 129371.
- Matured sampled outcomes across 1/6/24/48h: 1105; gap abstentions: 5253. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
