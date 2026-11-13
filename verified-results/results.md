# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T19:45:36.733593+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43495130916
**Source SHA:** a575e7d515240220856513017d2a0e19a4aa88a7
**Previous ledger commit:** 31c1ab1d2b29e0f22b2a9d013e62178733cb7bfe (atomic ledger/results publication)
**Ledger generation:** 365 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.296 | 114.550 | 95.781 | +11.21% | +0.75% | 3.90x | 8.4 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.5444 | 95.449 | 78.507 | +3.64% | +0.39% | 3.27x | 4.0 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TAO/USD | 218.7679 | 82.258 | 74.291 | +3.23% | -0.04% | 1.82x | 6.7 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | QNT/USD | 167.23 | 76.809 | 60.207 | +2.21% | +1.34% | 1.99x | 6.6 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.433 | 74.174 | 60.263 | +1.01% | +0.12% | 2.33x | 3.6 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.109421 | 72.368 | 62.707 | +5.65% | -0.93% | 2.43x | 29.5 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SUI/USD | 0.8121 | 70.232 | 60.206 | +0.92% | +0.35% | 1.83x | 2.5 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PUMP/USD | 0.003537 | 63.262 | 61.356 | +1.55% | +0.63% | 0.88x | 8.5 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BCH/USD | 226.4 | 60.467 | 45.467 | +0.60% | +0.00% | 5.67x | 0.4 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | UAI/USD | 0.03881 | 58.881 | 69.410 | +7.60% | -0.94% | 0.42x | 15.5 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ZBCN/USD | 0.001849 | 55.407 | 63.489 | +8.26% | -0.80% | 0.59x | 27.0 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | VVV/USD | 19.59 | 55.114 | 57.584 | +3.15% | +0.63% | 0.44x | 11.2 | 2026-11-13T19:45:29.872193+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 365; predictions: 3382; observations: 219510.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9672. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
