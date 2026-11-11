# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T13:41:40.084978+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43031053902
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** e9e32cfe50fc4d626439cca0f46ab00dc9689013
**Ledger generation:** 282 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04452 | 99.853 | 84.289 | +6.20% | +0.11% | 2.93x | 6.7 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XMR/USD | 582.29 | 93.559 | 76.871 | +3.49% | +0.34% | 4.49x | 5.2 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.7384 | 88.367 | 82.789 | +4.31% | -0.81% | 1.96x | 4.8 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.25 | 83.643 | 81.878 | +9.75% | +0.08% | 1.14x | 16.1 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SOL/USD | 84.19 | 75.617 | 62.395 | +1.14% | -0.36% | 7.56x | 1.2 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AVAX/USD | 8.555 | 67.780 | 69.060 | +2.26% | -0.47% | 1.11x | 3.5 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.148402 | 64.972 | 65.657 | +2.64% | -0.34% | 1.10x | 3.7 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ADA/USD | 0.176452 | 60.879 | 63.186 | +1.52% | -0.32% | 0.93x | 4.9 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 220.7601 | 56.002 | 61.160 | +1.19% | -0.06% | 0.51x | 4.3 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8304 | 52.288 | 60.261 | +0.92% | -0.32% | 0.36x | 2.4 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HYPE/USD | 72.58 | 48.577 | 57.111 | +0.50% | -0.53% | 0.41x | 2.8 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TIA/USD | 0.4339 | 47.845 | 40.681 | +1.69% | -0.39% | 1.91x | 4.6 | 2026-11-11T13:41:33.042935+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 282; predictions: 2652; observations: 169223.
- Matured sampled outcomes across 1/6/24/48h: 1932; gap abstentions: 7025. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
