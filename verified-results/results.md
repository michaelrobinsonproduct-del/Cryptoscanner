# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T23:54:50.758651+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43530503636
**Source SHA:** bf3e28495fb4b8b85be31ec2c9d59b97bca01388
**Previous ledger commit:** 8692ccd71ec3be9207247b2759c6e06c8cdf2cda (atomic ledger/results publication)
**Ledger generation:** 371 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 19.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.072 | 93.752 | 97.522 | +8.20% | +0.41% | 0.42x | 5.0 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.4362 | 69.706 | 56.735 | +0.48% | +0.18% | 2.21x | 3.2 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZBCN/USD | 0.001809 | 64.932 | 54.201 | +5.91% | +0.00% | 2.07x | 38.7 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04681 | 63.153 | 61.375 | +2.00% | +0.28% | 1.04x | 6.4 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.03868 | 62.959 | 70.695 | +7.24% | -0.21% | 0.33x | 12.9 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TAO/USD | 214.2244 | 58.382 | 59.519 | +1.09% | -0.10% | 0.94x | 6.2 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LIGHTER/USD | 3.235 | 50.631 | 41.108 | +0.28% | +0.31% | 1.80x | 6.2 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | RENDER/USD | 1.529 | 47.758 | 31.445 | +0.46% | +0.26% | 3.98x | 13.1 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PROMPT/USD | 0.01343 | 32.989 | 38.238 | +2.68% | -2.39% | 1.67x | 22.4 | 2026-11-13T23:54:43.647992+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 371; predictions: 3427; observations: 223152.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9914. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
