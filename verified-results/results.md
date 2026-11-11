# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T02:30:55.021530+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42946365455
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** e14a316c99765e7d60aff6b5b77f2ea1bb40cdbc
**Ledger generation:** 260 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ARB/USD | 0.1662 | 86.969 | 65.879 | +3.62% | +1.22% | 3.39x | 12.0 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ICNT/USD | 0.3004 | 66.136 | 52.945 | +3.94% | +1.55% | 1.54x | 13.3 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | LINK/USD | 10.33151 | 61.670 | 49.939 | +0.46% | +0.26% | 2.04x | 5.8 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.6356 | 58.063 | 62.091 | +1.45% | +0.49% | 0.35x | 6.1 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AVAX/USD | 8.448 | 55.784 | 59.493 | +0.98% | +0.33% | 0.46x | 4.7 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NIGHT/USD | 0.04244 | 54.831 | 48.079 | +1.24% | +0.09% | 1.63x | 9.4 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | CAP/USD | 0.102823 | 52.811 | 35.761 | +0.61% | +0.41% | 31.80x | 15.7 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PEPE/USD | 5.404e-06 | 52.324 | 57.056 | +0.56% | -0.28% | 0.67x | 3.7 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ADA/USD | 0.174346 | 49.126 | 54.417 | +0.31% | +0.07% | 0.44x | 5.5 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PENGU/USD | 0.00622 | 49.095 | 33.693 | +0.35% | +0.08% | 3.99x | 3.2 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | INJ/USD | 8.193 | 42.227 | 52.465 | +2.35% | -0.44% | 0.19x | 12.2 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HBAR/USD | 0.06584 | 32.696 | 41.184 | +0.47% | +0.05% | 0.13x | 4.6 | 2026-11-11T02:30:46.483810+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 260; predictions: 2397; observations: 155963.
- Matured sampled outcomes across 1/6/24/48h: 1599; gap abstentions: 6565. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
