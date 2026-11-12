# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T21:32:32.105922+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43310828210
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** f0167d3db56c39b9ed4e3d0b0545e643447f3c4e
**Ledger generation:** 348 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.149837 | 71.358 | 64.415 | +1.94% | +0.99% | 1.20x | 0.9 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AKE/USD | 0.00274588 | 69.464 | 63.279 | +10.84% | -1.76% | 3.49x | 32.3 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01764 | 68.195 | 66.407 | +5.88% | +1.20% | 0.58x | 17.0 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 4.555e-06 | 67.229 | 60.104 | +1.04% | +0.09% | 1.67x | 4.4 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ATOM/USD | 1.4254 | 53.234 | 43.976 | +2.29% | +0.76% | 1.54x | 9.1 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | JUP/USD | 0.26528 | 52.183 | 55.360 | +3.96% | +0.23% | 0.57x | 12.4 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | BAT/USD | 0.12242 | 51.862 | 53.656 | +3.98% | +0.14% | 0.75x | 13.1 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | POL/USD | 0.08862 | 41.194 | 41.087 | +1.63% | +0.75% | 0.64x | 6.8 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | CAP/USD | 0.104503 | 38.798 | 48.084 | +4.01% | -0.30% | 0.22x | 23.5 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | USELESS/USD | 0.1291 | 37.660 | 39.630 | +1.42% | -0.09% | 0.85x | 17.8 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | FET/USD | 0.149 | 33.755 | 33.103 | +0.34% | +1.08% | 0.52x | 6.7 | 2026-11-12T21:32:24.301011+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 348; predictions: 3222; observations: 209204.
- Matured sampled outcomes across 1/6/24/48h: 2901; gap abstentions: 8495. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
