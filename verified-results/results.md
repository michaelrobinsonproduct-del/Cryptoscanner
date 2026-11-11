# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T02:02:54.747863+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42942991866
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** d92b210e14abc8077c0faab89001277986cfbc2a
**Ledger generation:** 259 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 601; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.448e-06 | 71.978 | 62.802 | +1.38% | -1.16% | 3.85x | 3.7 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TAO/USD | 220.038 | 71.892 | 58.707 | +0.86% | -0.36% | 2.51x | 4.6 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDG/USD | 0.0681917 | 70.131 | 57.589 | +0.37% | -0.49% | 3.88x | 0.0 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ADA/USD | 0.175123 | 69.539 | 57.785 | +0.76% | -0.65% | 4.98x | 5.0 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | INJ/USD | 8.222 | 68.858 | 56.938 | +2.71% | -0.62% | 3.52x | 8.5 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UNI/USD | 6.7027 | 65.677 | 56.836 | +0.57% | -1.23% | 4.49x | 4.3 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LINK/USD | 10.35013 | 62.407 | 50.630 | +0.64% | -0.64% | 2.96x | 5.7 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | NEAR/USD | 3.6468 | 61.930 | 65.250 | +1.76% | -0.79% | 1.06x | 4.1 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ONDO/USD | 0.37012 | 57.574 | 47.467 | +0.93% | -0.98% | 15.98x | 2.4 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | AAVE/USD | 123.7 | 57.025 | 50.725 | +0.26% | -0.71% | 1.98x | 4.0 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | AVAX/USD | 8.442 | 52.620 | 60.175 | +0.91% | -0.40% | 0.45x | 2.4 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SUI/USD | 0.8292 | 50.019 | 59.841 | +0.78% | -0.52% | 0.28x | 1.2 | 2026-11-11T02:02:48.210996+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 259; predictions: 2385; observations: 155361.
- Matured sampled outcomes across 1/6/24/48h: 1580; gap abstentions: 6531. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
