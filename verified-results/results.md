# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T20:46:32.026876+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42695967091
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 1f295fcb8046b216092be178eda547c35e102738
**Ledger generation:** 209 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.656 | 106.900 | 97.109 | +9.17% | -1.04% | 5.00x | 5.8 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ONDO/USD | 0.37424 | 85.075 | 94.522 | +6.45% | -0.63% | 0.37x | 11.0 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PAXG/USD | 4120.51 | 81.487 | 67.280 | +1.82% | -0.16% | 4.00x | 0.9 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AAVE/USD | 132.21 | 76.420 | 81.791 | +4.97% | -0.22% | 0.57x | 6.8 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ENA/USD | 0.1556 | 74.669 | 82.033 | +4.78% | -0.13% | 0.33x | 12.9 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8483 | 72.242 | 78.216 | +3.40% | -0.39% | 0.60x | 1.2 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ARB/USD | 0.1754 | 70.736 | 80.746 | +5.73% | -0.34% | 0.17x | 5.7 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | UNI/USD | 7.0354 | 70.708 | 80.809 | +3.71% | -0.20% | 0.09x | 0.3 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | VVV/USD | 21.64 | 67.205 | 78.772 | +7.88% | -0.42% | 0.05x | 6.0 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | QNT/USD | 195.83 | 66.140 | 51.064 | +0.50% | +0.02% | 2.71x | 2.6 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | USELESS/USD | 0.13761 | 66.033 | 75.058 | +11.76% | -0.79% | 0.49x | 20.3 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | PEPE/USD | 5.108e-06 | 64.250 | 75.826 | +3.25% | -0.89% | 0.29x | 3.9 | 2026-11-09T20:46:23.295570+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 209; predictions: 1911; observations: 126361.
- Matured sampled outcomes across 1/6/24/48h: 1093; gap abstentions: 5134. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
