# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T22:35:16.524136+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42915553317
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 9d582d34de7d337f7e264bf00a23eb13a8adf483
**Ledger generation:** 252 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 23.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.104072 | 72.164 | 73.272 | +5.27% | +1.54% | 0.12x | 6.1 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.281e-06 | 71.084 | 75.784 | +3.10% | -0.08% | 0.57x | 1.9 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZRO/USD | 1.511 | 67.986 | 54.306 | +2.37% | -0.26% | 2.60x | 13.3 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.139 | 67.939 | 77.307 | +9.52% | -1.72% | 0.93x | 8.8 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | LIGHTER/USD | 3.464 | 65.888 | 72.584 | +7.15% | -0.49% | 0.57x | 14.5 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDC/USD | 0.03018 | 65.283 | 51.275 | +2.41% | -0.20% | 3.19x | 9.9 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ICP/USD | 2.466 | 63.685 | 50.705 | +2.84% | -0.40% | 2.67x | 4.1 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | NIGHT/USD | 0.04167 | 61.243 | 61.424 | +2.94% | -0.90% | 1.43x | 4.8 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | AKE/USD | 0.00300437 | 53.958 | 47.112 | +3.74% | -1.63% | 6.57x | 35.3 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | UAI/USD | 0.04116 | 45.783 | 60.784 | +6.74% | -1.91% | 0.45x | 34.0 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | BEAM/USD | 0.004399 | 32.415 | 35.041 | +2.18% | -0.39% | 0.93x | 22.8 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SYRUP/USD | 0.13768 | 25.528 | 36.609 | +1.62% | -0.33% | 0.05x | 12.4 | 2026-11-10T22:35:07.951209+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 252; predictions: 2319; observations: 151160.
- Matured sampled outcomes across 1/6/24/48h: 1448; gap abstentions: 6363. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
