# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T04:33:59.347033+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42959895957
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** a9df23b2f4185ff97aa54a4bffdda071dc1d4ef6
**Ledger generation:** 264 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PYTH/USD | 0.06922 | 76.777 | 66.151 | +5.74% | -0.87% | 7.11x | 13.0 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ADA/USD | 0.175153 | 75.199 | 59.822 | +0.77% | +0.08% | 4.34x | 1.2 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04318 | 75.135 | 59.322 | +3.01% | +0.16% | 2.96x | 11.6 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | INJ/USD | 8.289 | 73.669 | 63.992 | +3.55% | -0.38% | 2.16x | 7.2 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.686 | 73.003 | 72.791 | +2.85% | +0.23% | 0.91x | 4.3 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8299 | 62.661 | 60.438 | +0.86% | -0.14% | 1.29x | 1.2 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDG/USD | 0.0682987 | 59.519 | 58.523 | +0.53% | -0.07% | 1.13x | 0.4 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ETH/USD | 2064.71 | 58.334 | 59.775 | +0.69% | +0.02% | 0.84x | 0.0 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | AVAX/USD | 8.457 | 58.299 | 60.247 | +1.09% | -0.07% | 0.84x | 4.7 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TAO/USD | 219.8872 | 50.068 | 58.619 | +0.79% | +0.07% | 0.11x | 3.8 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LTC/USD | 51.1 | 49.364 | 51.846 | +0.79% | -0.18% | 0.84x | 2.0 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AAVE/USD | 124.18 | 46.802 | 53.677 | +0.65% | -0.31% | 0.47x | 2.4 | 2026-11-11T04:33:50.837461+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 264; predictions: 2445; observations: 158371.
- Matured sampled outcomes across 1/6/24/48h: 1680; gap abstentions: 6623. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
