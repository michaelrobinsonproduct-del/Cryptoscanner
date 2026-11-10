# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T21:04:30.245199+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42901184793
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 67cd5825a0794f326951e9fe4a82ea6edeac38f6
**Ledger generation:** 249 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.133 | 83.094 | 71.627 | +8.94% | -0.71% | 7.57x | 17.7 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.27e-06 | 74.767 | 73.328 | +2.89% | +0.73% | 0.78x | 3.8 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04173 | 58.614 | 61.597 | +3.09% | +0.12% | 0.64x | 7.2 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | USELESS/USD | 0.13734 | 55.297 | 35.209 | +0.77% | +1.02% | 2.91x | 19.7 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TRUMP/USD | 1.134 | 52.298 | 37.739 | +1.25% | -0.09% | 2.55x | 8.8 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MEGA/USD | 0.05093 | 40.127 | 34.959 | +2.29% | +0.58% | 1.23x | 27.6 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ICP/USD | 2.435 | 35.240 | 39.353 | +1.54% | +0.04% | 0.57x | 8.2 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SYRUP/USD | 0.1364 | 20.700 | 27.756 | +0.67% | +0.09% | 0.25x | 16.1 | 2026-11-10T21:04:22.579739+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 249; predictions: 2286; observations: 149360.
- Matured sampled outcomes across 1/6/24/48h: 1390; gap abstentions: 6318. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
