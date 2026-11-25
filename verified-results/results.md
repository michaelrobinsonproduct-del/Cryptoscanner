# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T01:12:27.610576+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45523631173
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** abd0aeb6482cd981e2f6e65e6b16071123f05032 (atomic ledger/results publication)
**Ledger generation:** 1650 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.1992 | 61.569 | 49.987 | +2.76% | +1.40% | 1.46x | 16.4 | 2026-11-25T01:12:24.117627+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04905 | 53.647 | 37.927 | +0.47% | +0.14% | 13.88x | 8.2 | 2026-11-25T01:12:24.117627+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 3 | DRV/USD | 0.31937 | 37.227 | 37.704 | +1.62% | +0.98% | 0.46x | 16.0 | 2026-11-25T01:12:24.117627+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04141 | 35.806 | 35.236 | +1.05% | -0.86% | 1.49x | 12.0 | 2026-11-25T01:12:24.117627+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07013 | 33.719 | 26.253 | +0.66% | -0.19% | 1.84x | 19.9 | 2026-11-25T01:12:24.117627+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 6 | PROS/USD | 0.6885 | 25.475 | 32.597 | +2.65% | +0.28% | 0.15x | 34.6 | 2026-11-25T01:12:24.117627+00:00 | Not calibrated | WEAK 33/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 49.987 | 2.1992 | +1.40% | 1.46x |
| 2 | NIGHT/USD | 37.927 | 0.04905 | +0.14% | 13.88x |
| 3 | DRV/USD | 37.704 | 0.31937 | +0.98% | 0.46x |
| 4 | SKY/USD | 35.236 | 0.04141 | -0.86% | 1.49x |
| 5 | PROS/USD | 32.597 | 0.6885 | +0.28% | 0.15x |
| 6 | SYRUP/USD | 26.253 | 0.07013 | -0.19% | 1.84x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 1650; predictions: 14099; observations: 999941.
- Matured sampled outcomes across 1/6/24/48h: 29401; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45523631173 · **Generation:** 1650 · **Legacy run:** 45523631173
**Main quote time:** 2026-11-25T01:12:27.610576+00:00 · **Legacy report time:** 2026-11-25T01:13:40.135739+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.1992 | 61.57 | +1.40% | 1.46x | STRONG 81/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04905 | 53.65 | +0.14% | 13.88x | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD | 0.31937 | 37.23 | +0.98% | 0.46x | WEAK 44/100 | VERY_HIGH 81/100 | Watch |
| 4 | SKY/USD | 0.04141 | 35.81 | -0.86% | 1.49x | WEAK 33/100 | VERY_HIGH 72/100 | Do nothing |
| 5 | SYRUP/USD | 0.07013 | 33.72 | -0.19% | 1.84x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |
| 6 | PROS/USD | 0.6885 | 25.47 | +0.28% | 0.15x | WEAK 33/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.1931 | 65.29 | +1.40% | 1.46x | 7559 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.049 | 42.83 | +0.14% | 13.88x | 8766 | STRONG 76/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PEARL/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
