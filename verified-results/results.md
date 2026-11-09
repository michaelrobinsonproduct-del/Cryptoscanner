# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T17:45:24.835296+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42667468910
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 9642cb130fb2bdebc3ac82ddc642ec18fc0d3869
**Ledger generation:** 204 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.64 | 94.919 | 96.529 | +8.97% | -0.48% | 1.08x | 6.9 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | JUP/USD | 0.25124 | 92.215 | 78.594 | +8.38% | +0.00% | 2.36x | 19.9 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.24e-06 | 90.389 | 94.552 | +5.92% | +0.13% | 0.52x | 3.8 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ONDO/USD | 0.3741 | 89.730 | 96.530 | +6.41% | -0.30% | 0.47x | 5.6 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SUI/USD | 0.8453 | 79.344 | 75.655 | +3.04% | -0.34% | 1.54x | 1.2 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PYTH/USD | 0.06445 | 78.637 | 71.148 | +7.18% | +0.66% | 1.42x | 13.9 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AAVE/USD | 132.76 | 77.799 | 86.509 | +5.41% | -0.26% | 0.26x | 5.3 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XDG/USD | 0.0697216 | 77.753 | 63.582 | +1.23% | -0.17% | 2.82x | 0.0 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ARB/USD | 0.1779 | 77.556 | 84.899 | +7.23% | -0.78% | 0.66x | 5.6 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | LIGHTER/USD | 3.269 | 74.246 | 72.471 | +6.90% | -0.94% | 1.65x | 18.4 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | USELESS/USD | 0.13313 | 71.788 | 72.215 | +8.12% | -0.07% | 0.99x | 25.5 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34179 | 63.261 | 58.026 | +0.46% | -0.03% | 1.54x | 0.4 | 2026-11-09T17:45:17.406828+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 204; predictions: 1851; observations: 123331.
- Matured sampled outcomes across 1/6/24/48h: 1057; gap abstentions: 4981. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
