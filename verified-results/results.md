# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T13:30:43.064139+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43434200303
**Source SHA:** 2061f6013845bd8b3eea7a6001418c89a72a99c5
**Previous ledger commit:** ab175a0cc783d25c0f92b0d6adf622b4743e1f55 (atomic ledger/results publication)
**Ledger generation:** 359 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.5728 | 95.982 | 80.686 | +4.47% | +0.06% | 6.70x | 11.2 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | INJ/USD | 7.934 | 92.084 | 86.985 | +6.35% | +0.34% | 1.34x | 21.4 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.486 | 79.849 | 62.952 | +1.64% | +0.38% | 3.34x | 7.1 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HYPE/USD | 74.75 | 76.969 | 73.697 | +2.86% | +0.47% | 1.09x | 2.7 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | LIGHTER/USD | 3.346 | 75.311 | 51.286 | +3.72% | +1.80% | 3.71x | 30.1 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8125 | 58.042 | 58.708 | +0.97% | +0.38% | 0.74x | 6.2 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | STX/USD | 0.2951 | 57.389 | 52.037 | +3.58% | +0.31% | 1.38x | 13.5 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZEC/USD | 978.3 | 56.500 | 60.871 | +2.34% | +0.46% | 0.33x | 21.1 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BABY/USD | 0.00988 | 51.237 | 47.841 | +3.02% | +1.23% | 0.72x | 10.1 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | DOT/USD | 0.8398 | 51.219 | 35.321 | +0.74% | +0.18% | 5.05x | 13.1 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TAO/USD | 213.8166 | 50.330 | 55.309 | +0.90% | -0.13% | 0.57x | 12.0 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | VVV/USD | 19.241 | 43.278 | 41.950 | +1.31% | +0.73% | 0.77x | 14.0 | 2026-11-13T13:30:36.420869+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 359; predictions: 3314; observations: 215870.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9323. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
