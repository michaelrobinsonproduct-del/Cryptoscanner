# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T13:23:13.830916+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42624813588
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 923b257a6eec5da7dd4e0bf755b12b559137aa54
**Ledger generation:** 196 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.561 | 92.896 | 90.728 | +7.97% | +1.69% | 0.37x | 7.0 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 132.93 | 77.150 | 87.345 | +5.54% | -0.40% | 0.18x | 0.8 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ARB/USD | 0.1847 | 75.089 | 81.018 | +11.33% | -0.43% | 0.62x | 10.8 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.106e-06 | 71.629 | 70.632 | +3.21% | -0.72% | 1.46x | 13.7 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PUMP/USD | 0.00368 | 66.472 | 76.583 | +4.81% | -0.54% | 0.26x | 8.2 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8417 | 65.289 | 71.391 | +2.60% | -0.26% | 0.52x | 3.6 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06852 | 65.130 | 69.953 | +4.47% | -0.38% | 0.71x | 2.9 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TAO/USD | 222.2271 | 63.129 | 70.908 | +2.52% | +0.16% | 0.14x | 3.5 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | LTC/USD | 51.34 | 62.489 | 64.128 | +2.54% | -0.33% | 1.00x | 3.9 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ENA/USD | 0.1529 | 59.638 | 69.201 | +2.96% | -0.20% | 0.14x | 13.1 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | DOT/USD | 0.8762 | 58.029 | 45.360 | +1.69% | -0.47% | 3.50x | 2.3 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.3416 | 57.222 | 57.815 | +0.45% | +0.01% | 0.93x | 0.7 | 2026-11-09T13:23:05.261014+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 196; predictions: 1755; observations: 118483.
- Matured sampled outcomes across 1/6/24/48h: 985; gap abstentions: 4785. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
