# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:40:28.877584+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44579547863
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 7dbf4173132ac856af5b5538546600446f426f42 (atomic ledger/results publication)
**Ledger generation:** 827 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.738 | 90.758 | 85.286 | +4.92% | +0.75% | 1.17x | 8.4 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5545 | 85.823 | 70.703 | +7.05% | +2.74% | 1.14x | 12.7 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | BMT/USD | 0.02044 | 81.293 | 68.968 | +8.26% | -0.54% | 93.50x | 14.7 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | HYPE/USD | 68.62 | 79.719 | 71.754 | +2.60% | +1.07% | 1.26x | 2.9 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ZEC/USD | 919.99 | 72.816 | 59.271 | +0.88% | +0.96% | 1.88x | 3.8 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SKR/USD | 0.010263 | 71.861 | 70.715 | +6.54% | +0.89% | 0.67x | 10.7 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | PUMP/USD | 0.002702 | 66.213 | 65.582 | +4.08% | +1.39% | 0.37x | 11.1 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | TAO/USD | 194.986 | 64.150 | 61.348 | +1.58% | +0.71% | 0.93x | 8.1 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LIGHTER/USD | 2.872 | 61.767 | 65.577 | +5.82% | +0.45% | 0.39x | 20.9 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | USELESS/USD | 0.10035 | 60.994 | 61.303 | +5.01% | +1.25% | 0.34x | 22.0 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | SOL/USD | 73.99 | 60.448 | 58.608 | +0.61% | +0.49% | 0.94x | 1.4 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 12 | AVAX/USD | 7.052 | 58.502 | 47.947 | +0.44% | +0.79% | 1.66x | 4.3 | 2026-11-19T17:40:20.467387+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 85.286 | 22.738 | +0.75% | 1.17x |
| 2 | HYPE/USD | 71.754 | 68.62 | +1.07% | 1.26x |
| 3 | SKR/USD | 70.715 | 0.010263 | +0.89% | 0.67x |
| 4 | AKT/USD | 70.703 | 0.5545 | +2.74% | 1.14x |
| 5 | BMT/USD | 68.968 | 0.02044 | -0.54% | 93.50x |
| 6 | PUMP/USD | 65.582 | 0.002702 | +1.39% | 0.37x |
| 7 | LIGHTER/USD | 65.577 | 2.872 | +0.45% | 0.39x |
| 8 | TAO/USD | 61.348 | 194.986 | +0.71% | 0.93x |
| 9 | USELESS/USD | 61.303 | 0.10035 | +1.25% | 0.34x |
| 10 | ZEC/USD | 59.271 | 919.99 | +0.96% | 1.88x |
| 11 | SOL/USD | 58.608 | 73.99 | +0.49% | 0.94x |
| 12 | AVAX/USD | 47.947 | 7.052 | +0.79% | 1.66x |

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

- Persisted scans: 827; predictions: 7068; observations: 499957.
- Matured sampled outcomes across 1/6/24/48h: 7043; gap abstentions: 15447. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44579547863 · **Generation:** 827 · **Legacy run:** 44579547863
**Main quote time:** 2026-11-19T17:40:28.877584+00:00 · **Legacy report time:** 2026-11-19T17:41:08.754206+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.738 | 90.76 | +0.75% | 1.17x | STRONG 90/100 | HIGH 62/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5545 | 85.82 | +2.74% | 1.14x | STRONG 83/100 | VERY_HIGH 73/100 | Watch |
| 3 | BMT/USD | 0.02044 | 81.29 | -0.54% | 93.50x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 4 | HYPE/USD ⭐ | 68.62 | 79.72 | +1.07% | 1.26x | STRONG 85/100 | HIGH 55/100 | Watch |
| 5 | ZEC/USD | 919.99 | 72.82 | +0.96% | 1.88x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 6 | SKR/USD | 0.010263 | 71.86 | +0.89% | 0.67x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 7 | PUMP/USD | 0.002702 | 66.21 | +1.39% | 0.37x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |
| 8 | TAO/USD | 194.986 | 64.15 | +0.71% | 0.93x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 9 | LIGHTER/USD | 2.872 | 61.77 | +0.45% | 0.39x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 10 | USELESS/USD | 0.10035 | 60.99 | +1.25% | 0.34x | MODERATE 50/100 | VERY_HIGH 82/100 | Watch |
| 11 | SOL/USD | 73.99 | 60.45 | +0.49% | 0.94x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 12 | AVAX/USD | 7.052 | 58.50 | +0.79% | 1.66x | STRONG 74/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.686 | 87.94 | +0.75% | 1.17x | 12372 | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | HYPE/USD ⭐ | 68.53 | 80.03 | +1.07% | 1.26x | 12619 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | AKT/USD ⭐ | 0.553 | 79.78 | +2.74% | 1.14x | 3286 | STRONG 80/100 | VERY_HIGH 73/100 | Watch |
| 4 | INJ/USD | 7.139 | 67.77 | +0.72% | 1.49x | 6883 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, AKT/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
