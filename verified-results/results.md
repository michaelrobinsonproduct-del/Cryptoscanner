# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T23:38:16.129336+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42721857557
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** 922a4e390c1e6dd576030fb0488d75c319562e5f
**Ledger generation:** 217 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.644 | 94.500 | 99.422 | +9.02% | -0.07% | 0.54x | 1.2 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ONDO/USD | 0.37166 | 94.026 | 92.566 | +5.71% | -0.41% | 1.35x | 0.3 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.121e-06 | 92.376 | 77.669 | +3.52% | -0.06% | 4.40x | 3.9 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8423 | 68.523 | 73.092 | +2.67% | -0.06% | 0.57x | 1.2 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | VVV/USD | 21.593 | 68.054 | 79.180 | +7.64% | -0.50% | 0.14x | 5.6 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TAO/USD | 222.4439 | 66.312 | 70.824 | +2.62% | -0.23% | 0.67x | 5.1 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AAVE/USD | 131.51 | 63.146 | 72.472 | +4.41% | -0.17% | 0.15x | 5.3 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XBT/USD | 75081.4 | 62.554 | 58.168 | +0.45% | -0.00% | 1.44x | 0.0 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0698998 | 59.576 | 64.271 | +1.49% | -0.12% | 0.59x | 0.0 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HYPE/USD | 75.04 | 57.952 | 59.691 | +0.77% | -0.28% | 0.97x | 1.3 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XLM/USD | 0.147229 | 54.655 | 58.344 | +0.72% | -0.10% | 0.68x | 3.3 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34361 | 52.733 | 59.054 | +0.60% | -0.01% | 0.37x | 0.3 | 2026-11-09T23:38:07.699071+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 217; predictions: 2007; observations: 131177.
- Matured sampled outcomes across 1/6/24/48h: 1129; gap abstentions: 5295. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
