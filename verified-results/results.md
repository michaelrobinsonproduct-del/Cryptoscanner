# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T21:28:58.609516+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42905211201
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 13a5048ca0051efdc19da6ab53d7049c31ffd6da
**Ledger generation:** 250 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.254e-06 | 70.413 | 71.136 | +2.58% | -0.93% | 1.39x | 3.8 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | USELESS/USD | 0.13969 | 66.706 | 51.310 | +2.49% | +0.08% | 8.81x | 12.2 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.128 | 66.423 | 71.806 | +8.46% | -0.09% | 0.51x | 17.8 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04179 | 64.739 | 64.992 | +3.24% | -0.07% | 1.01x | 2.4 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.10042 | 52.780 | 39.419 | +1.58% | -0.33% | 11.42x | 21.0 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ATOM/USD | 1.3958 | 50.234 | 38.476 | +1.82% | -0.65% | 3.02x | 12.2 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TRUMP/USD | 1.134 | 40.751 | 37.763 | +1.25% | -0.35% | 1.47x | 8.8 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XCN/USD | 0.00327 | 37.611 | 38.838 | +2.83% | -0.30% | 1.03x | 30.7 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | MEGA/USD | 0.05095 | 37.475 | 36.241 | +2.33% | -0.12% | 1.18x | 25.6 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SYRUP/USD | 0.13587 | 19.506 | 26.087 | +0.28% | -0.79% | 0.74x | 14.0 | 2026-11-10T21:28:52.049886+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 250; predictions: 2296; observations: 149960.
- Matured sampled outcomes across 1/6/24/48h: 1409; gap abstentions: 6330. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
