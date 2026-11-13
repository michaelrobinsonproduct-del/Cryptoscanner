# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T15:02:31.715359+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43448480904
**Source SHA:** 724af27bedfcc5e759528bd81b2c6f20541964a7
**Previous ledger commit:** c9bdb4fad8e50ade2992ee74044e69568d8ed08c (atomic ledger/results publication)
**Ledger generation:** 360 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.108 | 90.987 | 96.300 | +8.69% | -0.64% | 0.79x | 7.4 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.5314 | 77.588 | 74.423 | +3.26% | -0.15% | 1.39x | 6.8 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SUI/USD | 0.8154 | 67.734 | 62.467 | +1.33% | -0.02% | 1.54x | 3.7 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HYPE/USD | 73.42 | 66.077 | 61.543 | +1.03% | -0.38% | 1.64x | 1.4 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 215.0263 | 64.037 | 62.013 | +1.47% | +0.46% | 0.97x | 6.5 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AVAX/USD | 8.47 | 59.300 | 62.187 | +1.45% | +0.16% | 0.63x | 5.9 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ICP/USD | 2.631 | 56.827 | 48.190 | +2.21% | -0.19% | 1.96x | 7.6 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XLM/USD | 0.149335 | 54.755 | 55.849 | +0.70% | -0.23% | 1.01x | 4.2 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BCH/USD | 225.75 | 53.638 | 41.208 | +0.31% | -0.51% | 19.14x | 4.9 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | VVV/USD | 19.103 | 49.755 | 39.105 | +0.58% | -0.51% | 2.32x | 11.5 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LIGHTER/USD | 3.312 | 48.669 | 47.609 | +2.67% | -0.27% | 1.24x | 24.1 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | BABY/USD | 0.00984 | 42.122 | 44.952 | +2.61% | +0.81% | 0.31x | 10.2 | 2026-11-13T15:02:24.581596+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 360; predictions: 3326; observations: 216477.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9395. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
