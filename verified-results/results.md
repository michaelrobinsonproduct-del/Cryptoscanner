# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T07:32:57.376012+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42980093922
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b33b5282be2405bf752c82ecd77396ff192361a8
**Ledger generation:** 270 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.488 | 82.706 | 64.030 | +1.46% | +0.74% | 3.22x | 2.4 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PYTH/USD | 0.0691 | 82.592 | 62.098 | +5.56% | +1.10% | 2.70x | 18.9 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.0431 | 78.363 | 57.738 | +2.81% | +1.12% | 2.52x | 9.3 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | INJ/USD | 8.237 | 76.500 | 56.779 | +2.90% | +0.94% | 6.69x | 10.9 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | DASH/USD | 43.987 | 71.848 | 48.714 | +2.39% | +1.63% | 2.58x | 11.6 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.145058 | 59.024 | 48.743 | +0.32% | +0.70% | 1.68x | 3.9 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2062.34 | 58.768 | 58.966 | +0.57% | +0.50% | 0.73x | 0.0 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XRP/USD | 1.05958 | 57.971 | 57.494 | +0.42% | +0.75% | 0.67x | 0.9 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | NEAR/USD | 3.601 | 54.718 | 55.584 | +0.48% | +0.84% | 0.50x | 5.6 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ADA/USD | 0.174329 | 53.641 | 54.494 | +0.30% | +0.66% | 0.58x | 5.2 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ZRO/USD | 1.558 | 53.096 | 48.782 | +1.56% | +1.17% | 0.85x | 12.8 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | KAS/USD | 0.02982 | 52.776 | 36.097 | +0.81% | +0.34% | 16.36x | 10.1 | 2026-11-11T07:32:49.487939+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 270; predictions: 2512; observations: 161983.
- Matured sampled outcomes across 1/6/24/48h: 1805; gap abstentions: 6712. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
