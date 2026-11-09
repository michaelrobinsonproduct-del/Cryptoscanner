# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T05:17:26.252873+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42566320464
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** ee3bf47a9cacadaa5bd535770f4bc7d4527f5087
**Ledger generation:** 182 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | RSR/USD | 0.001749 | 77.499 | 60.201 | +5.74% | +0.46% | 5.57x | 22.9 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | SUI/USD | 0.8274 | 73.805 | 60.368 | +0.85% | -0.31% | 3.88x | 1.2 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ARB/USD | 0.174 | 73.691 | 65.667 | +4.88% | -0.29% | 1.95x | 11.5 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ETH/USD | 2133.85 | 72.290 | 57.955 | +0.43% | +0.09% | 2.39x | 0.0 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 5.042e-06 | 69.562 | 66.458 | +1.92% | +0.32% | 1.15x | 4.0 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ENA/USD | 0.1514 | 67.652 | 65.363 | +1.95% | -0.39% | 1.43x | 6.6 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | USELESS/USD | 0.12893 | 65.512 | 60.202 | +4.71% | +0.22% | 1.42x | 23.4 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 87.01 | 61.236 | 58.960 | +0.65% | -0.11% | 1.28x | 1.1 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0694045 | 60.040 | 59.515 | +0.77% | -0.11% | 1.11x | 1.7 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ZEC/USD | 1227.36 | 58.154 | 61.919 | +1.23% | -0.08% | 0.66x | 3.4 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LTC/USD | 50.72 | 57.770 | 53.791 | +1.30% | -0.06% | 1.43x | 2.0 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | WLD/USD | 0.3204 | 57.058 | 55.974 | +2.76% | -0.06% | 1.14x | 3.1 | 2026-11-09T05:17:17.458762+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 182; predictions: 1592; observations: 110000.
- Matured sampled outcomes across 1/6/24/48h: 891; gap abstentions: 4477. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
