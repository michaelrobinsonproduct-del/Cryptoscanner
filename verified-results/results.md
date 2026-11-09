# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T15:21:01.013734+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42643589965
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** 4c2b720f4399069bada5db0371e955ade284106b
**Ledger generation:** 199 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD | 133.25 | 106.112 | 89.377 | +5.80% | +0.35% | 6.82x | 0.8 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ENA/USD | 0.1571 | 101.023 | 89.169 | +5.79% | +0.77% | 1.80x | 12.7 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ARB/USD | 0.1807 | 98.589 | 81.922 | +8.92% | +0.33% | 7.25x | 11.1 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.282e-06 | 93.419 | 94.312 | +6.77% | +0.88% | 0.47x | 11.4 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.181478 | 93.174 | 77.257 | +3.69% | +0.18% | 2.75x | 5.0 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MON/USD | 0.01709 | 89.149 | 75.018 | +8.85% | +0.59% | 2.12x | 11.7 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LTC/USD | 52.18 | 85.525 | 76.882 | +4.21% | +0.23% | 1.75x | 3.8 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SUI/USD | 0.8605 | 84.782 | 88.052 | +4.89% | +0.06% | 0.64x | 2.3 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ATOM/USD | 1.392 | 82.675 | 74.194 | +6.58% | +0.30% | 1.70x | 11.5 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TAO/USD | 224.8661 | 80.772 | 79.272 | +3.74% | +0.03% | 1.13x | 3.8 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PUMP/USD | 0.003697 | 77.648 | 80.138 | +5.30% | +0.68% | 0.41x | 8.1 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | USELESS/USD | 0.13787 | 75.348 | 77.396 | +11.97% | +0.77% | 0.41x | 16.0 | 2026-11-09T15:20:51.755363+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 199; predictions: 1791; observations: 120301.
- Matured sampled outcomes across 1/6/24/48h: 1033; gap abstentions: 4835. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
