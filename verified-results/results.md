# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T17:04:13.750230+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43064090579
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 1c9294cb8f9d5079df0680c2487ebeb30db21420
**Ledger generation:** 290 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 593.06 | 101.906 | 83.579 | +5.41% | +0.67% | 6.13x | 18.5 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.788 | 94.711 | 93.037 | +5.70% | +0.71% | 0.81x | 3.7 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | VVV/USD | 20.538 | 88.860 | 81.934 | +6.40% | +1.24% | 1.07x | 5.8 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 223.73 | 87.812 | 69.864 | +2.55% | +0.71% | 2.44x | 5.9 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XLM/USD | 0.150876 | 75.776 | 79.018 | +4.35% | -0.19% | 0.77x | 3.0 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AVAX/USD | 8.638 | 75.568 | 76.600 | +3.25% | +0.49% | 0.65x | 2.3 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HYPE/USD | 74.04 | 74.654 | 71.290 | +2.52% | +0.62% | 1.02x | 2.7 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | CC/USD | 0.09372 | 72.664 | 68.276 | +4.74% | +0.79% | 1.05x | 7.5 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SOL/USD | 84.87 | 72.045 | 68.118 | +1.96% | +0.37% | 1.21x | 1.2 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ADA/USD | 0.179067 | 71.598 | 72.728 | +3.03% | +0.36% | 0.71x | 4.2 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XRP/USD | 1.07106 | 66.778 | 65.535 | +1.51% | +0.29% | 0.98x | 0.1 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SUI/USD | 0.844 | 65.447 | 71.853 | +2.58% | +0.38% | 0.17x | 2.4 | 2026-11-11T17:04:06.493649+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 290; predictions: 2748; observations: 174063.
- Matured sampled outcomes across 1/6/24/48h: 2063; gap abstentions: 7203. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
