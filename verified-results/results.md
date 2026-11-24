# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T18:27:16.967535+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45459218165
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9b7d2a954a8431d7a9d18b821608a02e18311392 (atomic ledger/results publication)
**Ledger generation:** 1610 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 504.08 | 76.607 | 77.542 | +3.72% | +0.01% | 0.90x | 6.9 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31145 | 54.591 | 59.214 | +0.63% | -0.03% | 0.55x | 0.4 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | VVV/USD | 24.976 | 54.276 | 65.712 | +2.16% | -0.96% | 0.34x | 8.8 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.0483 | 53.442 | 40.090 | +0.31% | -0.33% | 2.69x | 6.2 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.435e-06 | 51.983 | 45.233 | +0.38% | -0.41% | 1.88x | 2.9 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66455 | 38.236 | 44.195 | +0.30% | -0.02% | 0.41x | 1.7 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.01623 | 37.627 | 47.492 | +3.71% | -0.55% | 0.29x | 18.5 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | DBR/USD | 0.01346 | 22.007 | 22.599 | +0.30% | -0.66% | 1.27x | 22.3 | 2026-11-24T18:27:13.453837+00:00 | Not calibrated | WEAK 11/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 77.542 | 504.08 | +0.01% | 0.90x |
| 2 | VVV/USD | 65.712 | 24.976 | -0.96% | 0.34x |
| 3 | GBP/USD | 59.214 | 1.31145 | -0.03% | 0.55x |
| 4 | 2Z/USD | 47.492 | 0.01623 | -0.55% | 0.29x |
| 5 | PEPE/USD | 45.233 | 3.435e-06 | -0.41% | 1.88x |
| 6 | AUD/USD | 44.195 | 0.66455 | -0.02% | 0.41x |
| 7 | NIGHT/USD | 40.090 | 0.0483 | -0.33% | 2.69x |
| 8 | DBR/USD | 22.599 | 0.01346 | -0.66% | 1.27x |

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

- Persisted scans: 1610; predictions: 13830; observations: 975582.
- Matured sampled outcomes across 1/6/24/48h: 27901; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45459218165 · **Generation:** 1610 · **Legacy run:** 45459218165
**Main quote time:** 2026-11-24T18:27:16.967535+00:00 · **Legacy report time:** 2026-11-24T18:28:27.767097+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 504.08 | 76.61 | +0.01% | 0.90x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 2 | GBP/USD | 1.31145 | 54.59 | -0.03% | 0.55x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | VVV/USD | 24.976 | 54.28 | -0.96% | 0.34x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | NIGHT/USD | 0.0483 | 53.44 | -0.33% | 2.69x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | PEPE/USD | 3.435e-06 | 51.98 | -0.41% | 1.88x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 6 | AUD/USD | 0.66455 | 38.24 | -0.02% | 0.41x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | 2Z/USD | 0.01623 | 37.63 | -0.55% | 0.29x | WEAK 19/100 | EXTREME 94/100 | Do nothing |
| 8 | DBR/USD | 0.01346 | 22.01 | -0.66% | 1.27x | WEAK 11/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
