# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T13:03:17.094574+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43025254746
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 2b8a48a19d0e5c595f6813a59056cb85806714a0
**Ledger generation:** 281 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.23 | 97.247 | 80.692 | +7.99% | +0.89% | 2.21x | 16.2 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.7269 | 74.533 | 80.534 | +3.99% | -0.09% | 0.45x | 4.8 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ADA/USD | 0.175867 | 71.225 | 60.627 | +1.19% | +0.29% | 1.92x | 5.3 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.148491 | 68.694 | 66.766 | +2.70% | +0.80% | 0.79x | 3.6 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 218.9169 | 68.188 | 54.081 | +0.34% | -0.18% | 4.57x | 6.6 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NIGHT/USD | 0.04402 | 66.281 | 72.919 | +5.01% | +0.39% | 0.14x | 13.7 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | DOT/USD | 0.8558 | 66.192 | 48.844 | +1.58% | +0.47% | 10.43x | 1.2 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 8.532 | 65.591 | 68.303 | +1.98% | -0.14% | 0.80x | 1.2 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XMR/USD | 577.25 | 64.113 | 69.106 | +2.60% | +0.11% | 0.45x | 8.1 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SUI/USD | 0.8281 | 63.257 | 58.906 | +0.64% | +0.16% | 1.36x | 1.2 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TIA/USD | 0.4362 | 61.343 | 44.510 | +2.23% | +0.37% | 2.52x | 4.6 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ONDO/USD | 0.36892 | 60.576 | 41.881 | +0.60% | +0.74% | 9.14x | 2.4 | 2026-11-11T13:03:08.062575+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 281; predictions: 2640; observations: 168618.
- Matured sampled outcomes across 1/6/24/48h: 1920; gap abstentions: 6995. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
