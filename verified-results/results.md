# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T06:16:38.717723+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42571946618
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** ceb9f5d596360af5501c554cb77aaca29833df6f
**Ledger generation:** 184 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD | 4103.89 | 59.672 | 45.241 | +1.41% | -0.11% | 3.66x | 0.9 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5e-06 | 52.985 | 57.498 | +1.07% | +0.04% | 0.53x | 10.0 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | CAP/USD | 0.101507 | 49.078 | 40.753 | +1.59% | +1.42% | 1.12x | 5.1 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1493 | 46.545 | 55.410 | +0.54% | -0.40% | 0.31x | 6.7 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | WLD/USD | 0.3183 | 44.023 | 48.126 | +2.08% | -0.03% | 0.61x | 9.4 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LTC/USD | 50.39 | 42.119 | 47.124 | +0.64% | +0.04% | 0.48x | 6.0 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | RSR/USD | 0.001722 | 38.936 | 48.593 | +4.11% | -0.63% | 0.35x | 23.3 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AUD/USD | 0.68912 | 38.626 | 41.192 | +0.34% | +0.01% | 0.74x | 1.2 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BAT/USD | 0.12127 | 37.512 | 43.417 | +2.71% | -0.01% | 0.41x | 14.0 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HBAR/USD | 0.06592 | 33.402 | 41.877 | +0.50% | +0.06% | 0.12x | 1.5 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XAUT/USD | 4099.3 | 31.147 | 39.996 | +1.22% | -0.14% | 0.18x | 0.2 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | PENGU/USD | 0.006152 | 24.137 | 33.691 | +0.44% | -0.19% | 0.14x | 4.9 | 2026-11-09T06:16:30.976713+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 184; predictions: 1616; observations: 111212.
- Matured sampled outcomes across 1/6/24/48h: 915; gap abstentions: 4482. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
