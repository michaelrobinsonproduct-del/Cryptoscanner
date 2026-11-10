# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T14:34:22.800745+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42835113631
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** 8f5bc8518b644f997142ad2dd2e790faecb2fe55
**Ledger generation:** 236 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 589; OHLC screened: 22.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.343e-06 | 73.097 | 82.395 | +4.31% | -0.37% | 0.26x | 5.6 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PLAY/USD | 0.00869 | 62.173 | 57.882 | +5.81% | -0.21% | 1.53x | 27.7 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.0422 | 58.929 | 68.578 | +4.25% | +0.00% | 0.04x | 2.4 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XDC/USD | 0.03074 | 56.012 | 58.373 | +4.31% | -1.06% | 1.29x | 22.7 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.096 | 52.081 | 53.548 | +5.38% | -0.73% | 1.22x | 36.6 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PYTH/USD | 0.06554 | 50.297 | 33.612 | +1.03% | +0.34% | 9.90x | 13.7 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZEC/USD | 1170.26 | 47.295 | 56.147 | +0.67% | -0.39% | 0.31x | 7.1 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | LIGHTER/USD | 3.307 | 43.963 | 34.422 | +2.29% | -0.54% | 2.23x | 30.3 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TRX/USD | 0.31891 | 36.907 | 42.384 | +0.49% | -0.06% | 0.48x | 1.0 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PIEVERSE/USD | 2.0541 | 32.027 | 18.205 | +0.82% | -0.24% | 11.04x | 39.4 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | JUP/USD | 0.25368 | 30.001 | 41.451 | +0.40% | -0.34% | 0.03x | 13.8 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TRUMP/USD | 1.128 | 23.155 | 33.716 | +0.71% | -0.44% | 0.16x | 8.9 | 2026-11-10T14:34:15.973615+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 236; predictions: 2159; observations: 141599.
- Matured sampled outcomes across 1/6/24/48h: 1209; gap abstentions: 6089. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
