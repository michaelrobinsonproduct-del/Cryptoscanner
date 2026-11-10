# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T20:31:35.338737+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42895795285
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** fab5ba51905a43a7895e3ad78cae1d5ee523437e
**Ledger generation:** 248 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.102 | 78.888 | 72.016 | +5.96% | -0.36% | 1.87x | 9.1 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.232e-06 | 71.619 | 68.118 | +2.15% | -0.10% | 1.40x | 3.8 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04161 | 68.992 | 59.496 | +2.79% | +0.31% | 1.79x | 7.2 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | CAP/USD | 0.100118 | 52.471 | 35.990 | +1.27% | +0.30% | 5.07x | 23.2 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XCN/USD | 0.0033 | 34.479 | 45.470 | +3.77% | -1.19% | 0.50x | 30.4 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ICP/USD | 2.423 | 30.045 | 35.882 | +1.04% | -0.62% | 0.72x | 8.3 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TRUMP/USD | 1.135 | 29.474 | 38.321 | +1.34% | -0.18% | 0.20x | 8.9 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | MEGA/USD | 0.05067 | 29.140 | 32.210 | +1.77% | +0.32% | 0.53x | 25.7 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | KAS/USD | 0.03004 | 27.853 | 33.996 | +1.01% | +0.27% | 0.25x | 13.4 | 2026-11-10T20:31:28.854265+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 248; predictions: 2278; observations: 148760.
- Matured sampled outcomes across 1/6/24/48h: 1366; gap abstentions: 6313. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
