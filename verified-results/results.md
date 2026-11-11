# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T16:04:26.421812+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43054282320
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 1f1b0259ff5dbe90f7210ba46ceaf2fd2ac53b53
**Ledger generation:** 288 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.7477 | 98.619 | 85.145 | +4.57% | +0.06% | 2.32x | 3.7 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04663 | 92.042 | 81.543 | +11.24% | +0.32% | 1.89x | 12.8 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XLM/USD | 0.152203 | 88.364 | 86.006 | +5.27% | +0.40% | 1.04x | 0.3 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.604 | 87.874 | 72.001 | +2.84% | +0.17% | 18.25x | 5.8 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SUI/USD | 0.8438 | 86.213 | 72.273 | +2.55% | -0.04% | 2.41x | 1.2 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ADA/USD | 0.178437 | 82.041 | 67.919 | +2.66% | -0.18% | 4.06x | 4.3 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDG/USD | 0.0690727 | 81.099 | 65.325 | +1.67% | +0.15% | 3.35x | 0.0 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TAO/USD | 224.3513 | 76.574 | 72.530 | +2.83% | +0.01% | 1.40x | 4.6 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XRP/USD | 1.0695 | 74.492 | 64.500 | +1.36% | +0.11% | 1.94x | 0.1 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XMR/USD | 586.69 | 73.778 | 82.279 | +4.27% | -0.56% | 0.43x | 5.3 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TON/USD | 1.183 | 69.310 | 68.277 | +3.86% | -0.75% | 1.48x | 8.5 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ETH/USD | 2072.99 | 66.320 | 62.457 | +1.09% | +0.09% | 1.34x | 0.3 | 2026-11-11T16:04:19.359773+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 288; predictions: 2724; observations: 172853.
- Matured sampled outcomes across 1/6/24/48h: 2016; gap abstentions: 7143. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
