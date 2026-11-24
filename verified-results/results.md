# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T11:41:54.088148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45386194125
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6402d13af7905fb66852543d499f93ae26430f7a (atomic ledger/results publication)
**Ledger generation:** 1569 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.727 | 100.434 | 89.483 | +5.23% | +0.72% | 1.74x | 4.3 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01274 | 95.109 | 78.925 | +10.59% | +0.24% | 5.14x | 15.7 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04873 | 75.225 | 55.146 | +1.20% | +1.02% | 5.19x | 4.1 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ICNT/USD | 0.3288 | 68.367 | 65.223 | +6.37% | -0.24% | 1.44x | 24.4 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 5 | GBP/USD | 1.30776 | 66.100 | 57.308 | +0.35% | +0.00% | 1.88x | 0.2 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 496.8 | 61.578 | 65.695 | +2.22% | +0.16% | 0.51x | 9.7 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | DBR/USD | 0.01421 | 59.635 | 54.728 | +5.89% | +1.21% | 0.89x | 35.3 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | PEPE/USD | 3.452e-06 | 45.069 | 54.320 | +0.88% | +0.00% | 0.07x | 5.8 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LUNA/USD | 4.547e-05 | 41.679 | 45.247 | +4.60% | +0.53% | 0.38x | 37.6 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | WEAK 36/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | BABY/USD | 0.00861 | 38.092 | 35.932 | +1.29% | +0.00% | 1.22x | 11.6 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | BAT/USD | 0.07779 | 25.119 | 32.955 | +0.80% | -0.56% | 0.50x | 10.3 | 2026-11-24T11:41:47.579741+00:00 | Not calibrated | WEAK 13/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 89.483 | 25.727 | +0.72% | 1.74x |
| 2 | MON/USD | 78.925 | 0.01274 | +0.24% | 5.14x |
| 3 | XMR/USD | 65.695 | 496.8 | +0.16% | 0.51x |
| 4 | ICNT/USD | 65.223 | 0.3288 | -0.24% | 1.44x |
| 5 | GBP/USD | 57.308 | 1.30776 | +0.00% | 1.88x |
| 6 | NIGHT/USD | 55.146 | 0.04873 | +1.02% | 5.19x |
| 7 | DBR/USD | 54.728 | 0.01421 | +1.21% | 0.89x |
| 8 | PEPE/USD | 54.320 | 3.452e-06 | +0.00% | 0.07x |
| 9 | LUNA/USD | 45.247 | 4.547e-05 | +0.53% | 0.38x |
| 10 | BABY/USD | 35.932 | 0.00861 | +0.00% | 1.22x |
| 11 | BAT/USD | 32.955 | 0.07779 | -0.56% | 0.50x |

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

- Persisted scans: 1569; predictions: 13530; observations: 950619.
- Matured sampled outcomes across 1/6/24/48h: 26085; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45386194125 · **Generation:** 1569 · **Legacy run:** 45386194125
**Main quote time:** 2026-11-24T11:41:54.088148+00:00 · **Legacy report time:** 2026-11-24T11:42:54.960754+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.727 | 100.43 | +0.72% | 1.74x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01274 | 95.11 | +0.24% | 5.14x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04873 | 75.23 | +1.02% | 5.19x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ICNT/USD | 0.3288 | 68.37 | -0.24% | 1.44x | WEAK 44/100 | VERY_HIGH 78/100 | Watch |
| 5 | GBP/USD | 1.30776 | 66.10 | +0.00% | 1.88x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 6 | XMR/USD | 496.8 | 61.58 | +0.16% | 0.51x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | DBR/USD | 0.01421 | 59.64 | +1.21% | 0.89x | MODERATE 45/100 | EXTREME 86/100 | Do nothing |
| 8 | PEPE/USD | 3.452e-06 | 45.07 | +0.00% | 0.07x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 9 | LUNA/USD | 4.547e-05 | 41.68 | +0.53% | 0.38x | WEAK 36/100 | EXTREME 87/100 | Do nothing |
| 10 | BABY/USD | 0.00861 | 38.09 | +0.00% | 1.22x | WEAK 39/100 | VERY_HIGH 73/100 | Watch |
| 11 | BAT/USD | 0.07779 | 25.12 | -0.56% | 0.50x | WEAK 13/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.724 | 90.10 | +0.72% | 1.74x | 14112 | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01272 | 85.84 | +0.24% | 5.14x | 10481 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04864 | 63.26 | +1.02% | 5.19x | 12281 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, MON/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
