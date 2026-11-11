# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T14:07:25.440276+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43035042121
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 03ed2d15481402bbee747b80b7b59119a563d483
**Ledger generation:** 283 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.7685 | 94.569 | 89.218 | +5.15% | +0.69% | 1.19x | 3.7 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TAO/USD | 222.4123 | 86.186 | 67.077 | +1.94% | +0.82% | 2.95x | 3.1 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04512 | 83.763 | 83.564 | +7.63% | +0.98% | 0.53x | 11.1 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8349 | 81.922 | 64.096 | +1.47% | +0.57% | 2.57x | 2.4 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SOL/USD | 84.44 | 81.695 | 64.499 | +1.44% | +0.44% | 5.29x | 1.2 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XMR/USD | 583.79 | 74.893 | 78.401 | +3.76% | +0.29% | 0.50x | 5.8 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.149964 | 73.270 | 74.752 | +3.72% | +0.55% | 0.58x | 1.0 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ADA/USD | 0.177598 | 72.158 | 67.647 | +2.18% | +0.58% | 1.16x | 5.2 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TON/USD | 1.232 | 69.998 | 81.754 | +8.17% | -0.88% | 0.26x | 16.3 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XDG/USD | 0.0682549 | 65.974 | 58.240 | +0.46% | +0.41% | 1.57x | 0.0 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | AAVE/USD | 124.03 | 64.775 | 49.090 | +0.53% | +0.14% | 2.82x | 1.6 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AVAX/USD | 8.553 | 61.690 | 69.478 | +2.24% | +0.32% | 0.06x | 2.3 | 2026-11-11T14:07:17.328869+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 283; predictions: 2664; observations: 169828.
- Matured sampled outcomes across 1/6/24/48h: 1944; gap abstentions: 7045. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
