# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T08:39:26.773994+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43394873917
**Source SHA:** 27b2c2d1e9b6fd360c5aca4124a6f6977c9777a5
**Previous ledger commit:** 60da5cfb50ef12fb37348c37499c90781e1b6e23 (atomic ledger/results publication)
**Ledger generation:** 354 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.5279 | 78.660 | 75.689 | +3.16% | +0.72% | 0.94x | 2.8 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UAI/USD | 0.03802 | 76.464 | 61.398 | +5.41% | +0.42% | 2.30x | 15.8 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ICP/USD | 2.633 | 71.861 | 49.928 | +2.29% | +1.39% | 3.19x | 3.8 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PONS/USD | 0.1594 | 59.958 | 62.382 | +5.42% | +0.32% | 0.60x | 12.6 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | USELESS/USD | 0.1351 | 58.473 | 50.884 | +2.35% | +0.35% | 1.59x | 11.1 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ICNT/USD | 0.287 | 52.014 | 52.882 | +4.10% | +0.67% | 0.58x | 14.0 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | INJ/USD | 7.526 | 51.004 | 48.676 | +0.88% | +0.70% | 0.88x | 5.3 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | KAS/USD | 0.02907 | 29.762 | 34.869 | +0.97% | -0.03% | 0.51x | 13.8 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | CAP/USD | 0.105017 | 24.209 | 31.543 | +1.40% | -0.11% | 0.32x | 21.0 | 2026-11-13T08:39:21.272642+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 354; predictions: 3260; observations: 212840.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9087. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
