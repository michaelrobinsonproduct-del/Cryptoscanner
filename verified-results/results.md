# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T23:39:53.984365+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42924923995
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 56f78474c8a15c8d6d0747c9fae848d6da4e924a
**Ledger generation:** 254 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.315e-06 | 96.004 | 79.494 | +3.77% | +0.30% | 2.88x | 3.8 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TON/USD | 1.143 | 72.170 | 77.569 | +9.90% | -0.61% | 0.77x | 8.8 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.0415 | 70.284 | 57.443 | +2.52% | -0.43% | 17.06x | 7.2 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ICP/USD | 2.529 | 59.239 | 68.899 | +5.46% | -0.04% | 0.05x | 7.9 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SYRUP/USD | 0.13837 | 48.527 | 35.888 | +2.13% | +0.01% | 2.26x | 21.0 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.101949 | 46.376 | 58.069 | +3.13% | -0.76% | 0.21x | 6.1 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MEGA/USD | 0.05029 | 31.799 | 28.785 | +1.00% | -0.22% | 1.41x | 21.9 | 2026-11-10T23:39:45.562618+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 254; predictions: 2335; observations: 152360.
- Matured sampled outcomes across 1/6/24/48h: 1489; gap abstentions: 6427. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
