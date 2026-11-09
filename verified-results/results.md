# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T10:48:47.115902+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42603790100
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 0df4692c735f311480002aae21fd93770c4a3ec7
**Ledger generation:** 191 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ARB/USD | 0.1764 | 82.722 | 78.016 | +6.33% | -0.62% | 1.78x | 11.3 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | HBAR/USD | 0.06688 | 65.922 | 51.817 | +1.97% | -0.18% | 5.93x | 3.0 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AAVE/USD | 130.97 | 63.316 | 72.109 | +3.99% | -0.55% | 0.39x | 5.4 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | GBP/USD | 1.342 | 59.748 | 58.062 | +0.48% | +0.01% | 1.16x | 0.6 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AUD/USD | 0.69022 | 55.518 | 44.013 | +0.50% | -0.03% | 2.17x | 1.2 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LTC/USD | 50.52 | 50.623 | 52.216 | +0.90% | -0.86% | 1.27x | 2.0 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PEPE/USD | 5.02e-06 | 50.007 | 58.367 | +1.48% | -0.55% | 0.44x | 13.9 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 7.978 | 41.879 | 43.137 | +0.62% | -0.37% | 1.06x | 6.3 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PAXG/USD | 4081.69 | 37.635 | 43.711 | +0.86% | -0.00% | 0.39x | 0.1 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | WLD/USD | 0.3145 | 35.222 | 41.878 | +0.87% | -0.66% | 0.67x | 6.4 | 2026-11-09T10:48:38.110176+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 191; predictions: 1695; observations: 115454.
- Matured sampled outcomes across 1/6/24/48h: 963; gap abstentions: 4661. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
