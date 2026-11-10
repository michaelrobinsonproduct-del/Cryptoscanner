# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T12:06:26.893454+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42812672260
**Source SHA:** 104a4347a7ce126d5801730cff397c5a215a9b38
**Ledger commit:** 09fb9ef22bbb5c299321cc9de87d1cdbaf52a237
**Ledger generation:** 231 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 579; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.286e-06 | 69.907 | 75.521 | +3.20% | -0.60% | 0.74x | 3.8 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04188 | 67.745 | 58.533 | +3.46% | -1.16% | 4.05x | 9.6 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | CAP/USD | 0.101953 | 58.141 | 51.038 | +3.13% | +0.25% | 1.58x | 6.1 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XDC/USD | 0.03089 | 57.913 | 66.370 | +4.82% | -0.58% | 0.44x | 12.9 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.04166 | 51.619 | 61.609 | +8.04% | -1.19% | 0.60x | 33.6 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ADA/USD | 0.177893 | 50.533 | 49.661 | +0.36% | -0.05% | 1.11x | 5.4 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TRX/USD | 0.318529 | 48.594 | 39.974 | +0.37% | -0.10% | 1.91x | 0.8 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TON/USD | 1.076 | 44.813 | 44.569 | +3.46% | -0.83% | 1.44x | 27.9 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ATOM/USD | 1.3802 | 44.396 | 32.062 | +0.69% | -0.53% | 3.82x | 8.0 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | FET/USD | 0.1455 | 33.294 | 33.178 | +1.18% | +0.21% | 0.91x | 13.8 | 2026-11-10T12:06:18.600664+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 231; predictions: 2111; observations: 138671.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5971. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
