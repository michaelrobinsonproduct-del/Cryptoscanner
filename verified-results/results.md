# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T13:55:21.104418+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42629587417
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** ac98ec993f4ff194810c93f36b44b962a495bd16
**Ledger generation:** 197 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.798 | 114.530 | 94.881 | +10.96% | +0.93% | 3.56x | 10.2 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | SUI/USD | 0.849 | 95.232 | 78.814 | +3.49% | +0.28% | 2.55x | 1.2 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AAVE/USD | 132.81 | 83.425 | 85.264 | +5.45% | -0.22% | 0.93x | 3.8 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ARB/USD | 0.183 | 76.363 | 81.078 | +10.31% | -0.22% | 0.64x | 10.9 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 222.8898 | 75.849 | 68.087 | +2.83% | +0.38% | 1.59x | 13.4 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | WLD/USD | 0.3229 | 72.982 | 62.871 | +3.56% | +0.56% | 1.73x | 3.1 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ENA/USD | 0.1536 | 71.415 | 72.522 | +3.43% | +0.33% | 0.73x | 13.0 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | LTC/USD | 51.55 | 67.172 | 67.290 | +2.96% | +0.21% | 0.88x | 3.9 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PEPE/USD | 5.099e-06 | 66.057 | 73.567 | +3.07% | +0.22% | 0.14x | 5.9 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ADA/USD | 0.179356 | 63.934 | 67.726 | +2.48% | +0.22% | 0.51x | 5.7 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XLM/USD | 0.146787 | 63.613 | 57.177 | +0.41% | -0.02% | 1.65x | 1.4 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34141 | 60.946 | 57.938 | +0.44% | +0.02% | 1.29x | 0.2 | 2026-11-09T13:55:13.690434+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 197; predictions: 1767; observations: 119089.
- Matured sampled outcomes across 1/6/24/48h: 997; gap abstentions: 4806. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
