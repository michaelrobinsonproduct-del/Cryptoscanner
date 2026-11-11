# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T07:50:51.018269+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42982229095
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 46dafc6eeebcdc7d2d780d2b7bf902e1a2f76b95
**Ledger generation:** 271 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.186 | 67.426 | 54.676 | +2.26% | -0.45% | 2.79x | 6.1 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ETH/USD | 2061.28 | 61.198 | 58.604 | +0.52% | +0.01% | 1.25x | 0.0 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.52 | 60.987 | 66.125 | +1.84% | +0.04% | 0.47x | 3.5 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04313 | 57.510 | 59.138 | +2.89% | +0.05% | 0.81x | 7.0 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.5939 | 50.466 | 55.303 | +0.28% | -0.16% | 0.59x | 3.3 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ATOM/USD | 1.4078 | 45.968 | 29.650 | +0.46% | +0.49% | 2.39x | 10.7 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TON/USD | 1.162 | 45.157 | 42.568 | +2.02% | +0.96% | 0.78x | 17.3 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PYTH/USD | 0.06824 | 44.017 | 53.499 | +4.25% | -0.44% | 0.27x | 17.6 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZRO/USD | 1.557 | 38.407 | 45.154 | +1.50% | +0.19% | 0.23x | 19.3 | 2026-11-11T07:50:42.109894+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 271; predictions: 2521; observations: 162586.
- Matured sampled outcomes across 1/6/24/48h: 1829; gap abstentions: 6724. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
