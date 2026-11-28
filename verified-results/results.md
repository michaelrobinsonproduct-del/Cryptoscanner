# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T18:52:47.048066+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46177933494
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2f032c7eb5c7ff293fc60e520b6b85eeae404432 (atomic ledger/results publication)
**Ledger generation:** 2193 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 607; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05226 | 76.487 | 77.060 | +4.02% | -0.68% | 1.29x | 9.6 | 2026-11-28T18:52:42.279664+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SENT/USD | 0.024421 | 59.750 | 48.322 | +2.98% | +1.82% | 1.23x | 7.8 | 2026-11-28T18:52:42.279664+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | BCH/USD | 209.24 | 56.996 | 38.230 | +1.08% | +0.75% | 66.11x | 4.8 | 2026-11-28T18:52:42.279664+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 4 | VVV/USD | 26.375 | 53.553 | 54.435 | +2.43% | +0.05% | 0.89x | 8.7 | 2026-11-28T18:52:42.279664+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 77.060 | 0.05226 | -0.68% | 1.29x |
| 2 | VVV/USD | 54.435 | 26.375 | +0.05% | 0.89x |
| 3 | SENT/USD | 48.322 | 0.024421 | +1.82% | 1.23x |
| 4 | BCH/USD | 38.230 | 209.24 | +0.75% | 66.11x |

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

- Persisted scans: 2193; predictions: 19371; observations: 1328012.
- Matured sampled outcomes across 1/6/24/48h: 47198; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 158 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46177933494 · **Generation:** 2193 · **Legacy run:** 46177933494
**Main quote time:** 2026-11-28T18:52:47.048066+00:00 · **Legacy report time:** 2026-11-28T18:53:36.453606+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05226 | 76.49 | -0.68% | 1.29x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 2 | SENT/USD ⭐ | 0.024421 | 59.75 | +1.82% | 1.23x | STRONG 75/100 | VERY_HIGH 74/100 | Watch |
| 3 | BCH/USD ⭐ | 209.24 | 57.00 | +0.75% | 66.11x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 4 | VVV/USD | 26.375 | 53.55 | +0.05% | 0.89x | MODERATE 47/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.024344 | 61.08 | +1.82% | 1.23x | 6456 | STRONG 76/100 | VERY_HIGH 74/100 | Watch |
| 2 | BCH/USD ⭐ | 208.75 | 44.73 | +0.75% | 66.11x | 1821 | STRONG 87/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SENT/USD, BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
