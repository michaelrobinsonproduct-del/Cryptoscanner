# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T23:01:11.820000+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42919475210
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 3564698c2df9683faad6064e2f96b36cef708011
**Ledger generation:** 253 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICP/USD | 2.511 | 87.977 | 63.350 | +4.71% | +1.93% | 7.70x | 8.0 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TON/USD | 1.137 | 80.462 | 73.039 | +9.33% | -0.26% | 1.87x | 17.6 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.267e-06 | 71.999 | 71.970 | +2.83% | -0.17% | 1.09x | 5.7 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ZRO/USD | 1.527 | 71.247 | 62.130 | +3.46% | +0.07% | 1.88x | 13.1 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.04167 | 51.672 | 60.227 | +2.94% | +0.05% | 0.12x | 7.2 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.102108 | 50.537 | 54.109 | +3.29% | -1.91% | 1.60x | 16.3 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | RENDER/USD | 1.605 | 32.789 | 33.139 | +0.88% | +0.06% | 0.93x | 12.5 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | MEGA/USD | 0.05055 | 30.054 | 28.524 | +1.53% | -0.06% | 1.18x | 29.8 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SYRUP/USD | 0.13781 | 28.432 | 36.217 | +1.71% | -0.10% | 0.27x | 14.5 | 2026-11-10T23:01:03.085533+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 253; predictions: 2328; observations: 151760.
- Matured sampled outcomes across 1/6/24/48h: 1468; gap abstentions: 6389. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
