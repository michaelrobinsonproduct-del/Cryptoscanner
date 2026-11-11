# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T15:01:33.882065+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43043855228
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 52910c7aa760298584410fc0e3ced371ebcb827d
**Ledger generation:** 285 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.209 | 86.184 | 79.913 | +6.15% | -0.41% | 1.83x | 16.6 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.7136 | 81.336 | 76.852 | +3.62% | -0.35% | 1.63x | 7.0 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04515 | 81.020 | 81.915 | +7.71% | -0.46% | 1.14x | 13.3 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ADA/USD | 0.176778 | 80.003 | 64.960 | +1.71% | +0.06% | 2.47x | 4.0 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 221.8459 | 78.453 | 64.347 | +1.68% | -0.18% | 4.68x | 4.9 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ZRO/USD | 1.583 | 78.019 | 61.117 | +3.19% | +0.38% | 3.30x | 12.7 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.528 | 75.143 | 66.796 | +1.94% | +0.21% | 1.73x | 3.5 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XMR/USD | 583.81 | 71.975 | 71.824 | +3.76% | -0.05% | 1.04x | 19.0 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8308 | 69.794 | 60.602 | +0.97% | -0.23% | 2.03x | 2.4 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.149442 | 63.269 | 70.431 | +3.36% | +0.13% | 0.22x | 3.2 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SOL/USD | 83.79 | 59.765 | 58.431 | +0.66% | -0.23% | 1.25x | 2.4 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LINK/USD | 10.32623 | 59.406 | 44.549 | +0.41% | -0.03% | 2.93x | 7.9 | 2026-11-11T15:01:25.387252+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 285; predictions: 2688; observations: 171038.
- Matured sampled outcomes across 1/6/24/48h: 1968; gap abstentions: 7107. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
