# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:00:39.354698+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44583031705
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 3ac2373e005e6870cc99e9ef6f52014df99b8988 (atomic ledger/results publication)
**Ledger generation:** 831 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 68.85 | 76.400 | 74.893 | +2.95% | +0.67% | 0.81x | 1.5 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 2 | VVV/USD | 22.589 | 76.106 | 81.776 | +4.24% | +0.13% | 0.37x | 5.8 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002691 | 71.318 | 66.057 | +3.66% | +0.22% | 1.41x | 3.7 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | CT/USD | 0.1286 | 67.698 | 65.139 | +8.80% | +1.34% | 0.59x | 23.5 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | ADA/USD | 0.152448 | 62.989 | 59.575 | +0.79% | -0.33% | 1.51x | 1.9 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5528 | 62.572 | 72.544 | +6.72% | -0.41% | 0.21x | 9.1 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010161 | 61.024 | 64.052 | +5.48% | -0.45% | 0.92x | 10.8 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 31/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | TAO/USD | 194.05 | 56.852 | 58.594 | +1.09% | -0.14% | 0.90x | 6.5 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | LIGHTER/USD | 2.855 | 52.698 | 64.146 | +5.20% | -0.70% | 0.20x | 14.1 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 26/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | INJ/USD | 7.077 | 49.724 | 50.779 | +1.38% | -0.46% | 1.13x | 4.2 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ZEC/USD | 914.52 | 49.542 | 55.387 | +0.28% | -0.05% | 0.44x | 3.2 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | BNB/USD | 584.36 | 44.773 | 43.808 | +0.53% | -0.22% | 1.20x | 2.1 | 2026-11-19T18:00:30.446674+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.776 | 22.589 | +0.13% | 0.37x |
| 2 | HYPE/USD | 74.893 | 68.85 | +0.67% | 0.81x |
| 3 | AKT/USD | 72.544 | 0.5528 | -0.41% | 0.21x |
| 4 | PUMP/USD | 66.057 | 0.002691 | +0.22% | 1.41x |
| 5 | CT/USD | 65.139 | 0.1286 | +1.34% | 0.59x |
| 6 | LIGHTER/USD | 64.146 | 2.855 | -0.70% | 0.20x |
| 7 | SKR/USD | 64.052 | 0.010161 | -0.45% | 0.92x |
| 8 | ADA/USD | 59.575 | 0.152448 | -0.33% | 1.51x |
| 9 | TAO/USD | 58.594 | 194.05 | -0.14% | 0.90x |
| 10 | ZEC/USD | 55.387 | 914.52 | -0.05% | 0.44x |
| 11 | INJ/USD | 50.779 | 7.077 | -0.46% | 1.13x |
| 12 | BNB/USD | 43.808 | 584.36 | -0.22% | 1.20x |

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

- Persisted scans: 831; predictions: 7116; observations: 502349.
- Matured sampled outcomes across 1/6/24/48h: 7079; gap abstentions: 15468. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44583031705 · **Generation:** 831 · **Legacy run:** 44583031705
**Main quote time:** 2026-11-19T18:00:39.354698+00:00 · **Legacy report time:** 2026-11-19T18:01:22.489954+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 68.85 | 76.40 | +0.67% | 0.81x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD | 22.589 | 76.11 | +0.13% | 0.37x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 3 | PUMP/USD ⭐ | 0.002691 | 71.32 | +0.22% | 1.41x | STRONG 91/100 | HIGH 55/100 | Watch |
| 4 | CT/USD | 0.1286 | 67.70 | +1.34% | 0.59x | MODERATE 54/100 | EXTREME 87/100 | Do nothing |
| 5 | ADA/USD | 0.152448 | 62.99 | -0.33% | 1.51x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 6 | AKT/USD | 0.5528 | 62.57 | -0.41% | 0.21x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 7 | SKR/USD | 0.010161 | 61.02 | -0.45% | 0.92x | WEAK 31/100 | EXTREME 86/100 | Do nothing |
| 8 | TAO/USD | 194.05 | 56.85 | -0.14% | 0.90x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 9 | LIGHTER/USD | 2.855 | 52.70 | -0.70% | 0.20x | WEAK 26/100 | EXTREME 87/100 | Do nothing |
| 10 | INJ/USD | 7.077 | 49.72 | -0.46% | 1.13x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | ZEC/USD | 914.52 | 49.54 | -0.05% | 0.44x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | BNB/USD | 584.36 | 44.77 | -0.22% | 1.20x | WEAK 32/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002678 | 69.67 | +0.22% | 1.41x | 4050 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
