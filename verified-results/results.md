# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T15:41:31.779924+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43050549996
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 434c0b4c5d26407c3aff663f10fcc8e501633d9d
**Ledger generation:** 287 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04643 | 104.503 | 83.690 | +10.76% | +2.66% | 1.75x | 10.8 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.7481 | 99.626 | 85.356 | +4.58% | +1.43% | 1.71x | 3.5 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PUMP/USD | 0.003638 | 97.185 | 72.244 | +3.59% | +1.99% | 3.15x | 8.2 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.150771 | 96.876 | 77.139 | +4.28% | +0.95% | 3.87x | 3.8 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.178674 | 95.405 | 72.056 | +2.80% | +1.67% | 7.57x | 5.1 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.843 | 94.142 | 70.999 | +2.46% | +1.63% | 5.86x | 2.4 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XMR/USD | 590.52 | 92.600 | 82.485 | +4.96% | +1.68% | 1.17x | 14.4 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XRP/USD | 1.06984 | 86.925 | 64.726 | +1.40% | +1.44% | 2.71x | 0.1 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 223.9687 | 84.594 | 70.432 | +2.66% | +1.27% | 1.78x | 6.3 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XDG/USD | 0.0688916 | 82.117 | 64.677 | +1.40% | +1.45% | 2.02x | 0.3 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TON/USD | 1.195 | 77.201 | 71.326 | +4.92% | +0.85% | 1.16x | 16.7 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XBT/USD | 73933.5 | 76.984 | 57.217 | +0.32% | +0.95% | 3.41x | 0.0 | 2026-11-11T15:41:23.281327+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 287; predictions: 2712; observations: 172248.
- Matured sampled outcomes across 1/6/24/48h: 1992; gap abstentions: 7131. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
