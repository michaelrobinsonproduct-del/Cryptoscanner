# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:50:28.428992+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44570449550
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** af9acde8848a5011d29c6cd98f7591b23b095337 (atomic ledger/results publication)
**Ledger generation:** 817 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.572 | 77.685 | 80.777 | +4.16% | +0.56% | 0.41x | 6.7 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | INJ/USD | 7.162 | 74.121 | 60.036 | +2.59% | +0.94% | 1.94x | 2.8 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.021816 | 71.164 | 70.292 | +5.88% | +1.28% | 0.45x | 10.5 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97438 | 70.643 | 60.494 | +0.83% | +0.41% | 1.81x | 0.6 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ADA/USD | 0.152808 | 70.039 | 60.031 | +1.03% | +0.21% | 1.89x | 4.3 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | PYTH/USD | 0.05624 | 66.754 | 70.882 | +6.60% | +0.23% | 0.47x | 12.5 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | BILL/USD | 0.00437 | 66.558 | 64.406 | +10.63% | -0.91% | 1.67x | 22.9 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | WEAK 43/100 | EXTREME 85/100 | Do nothing | WATCH |
| 8 | BMT/USD | 0.02051 | 65.632 | 68.878 | +8.63% | +1.28% | 0.03x | 14.6 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | SKR/USD | 0.010367 | 65.000 | 71.224 | +7.62% | +0.14% | 0.31x | 9.7 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | HYPE/USD | 67.9 | 61.384 | 64.939 | +1.53% | +0.43% | 0.43x | 1.5 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AKT/USD | 0.5461 | 59.281 | 65.765 | +5.42% | +0.17% | 0.27x | 7.3 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.811e-06 | 51.668 | 50.168 | +1.74% | +0.53% | 0.89x | 5.3 | 2026-11-19T16:50:22.113056+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.777 | 22.572 | +0.56% | 0.41x |
| 2 | SKR/USD | 71.224 | 0.010367 | +0.14% | 0.31x |
| 3 | PYTH/USD | 70.882 | 0.05624 | +0.23% | 0.47x |
| 4 | SENT/USD | 70.292 | 0.021816 | +1.28% | 0.45x |
| 5 | BMT/USD | 68.878 | 0.02051 | +1.28% | 0.03x |
| 6 | AKT/USD | 65.765 | 0.5461 | +0.17% | 0.27x |
| 7 | HYPE/USD | 64.939 | 67.9 | +0.43% | 0.43x |
| 8 | BILL/USD | 64.406 | 0.00437 | -0.91% | 1.67x |
| 9 | XRP/USD | 60.494 | 0.97438 | +0.41% | 1.81x |
| 10 | INJ/USD | 60.036 | 7.162 | +0.94% | 1.94x |
| 11 | ADA/USD | 60.031 | 0.152808 | +0.21% | 1.89x |
| 12 | PEPE/USD | 50.168 | 3.811e-06 | +0.53% | 0.89x |

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

- Persisted scans: 817; predictions: 6948; observations: 493977.
- Matured sampled outcomes across 1/6/24/48h: 6923; gap abstentions: 15389. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44570449550 · **Generation:** 817 · **Legacy run:** 44570449550
**Main quote time:** 2026-11-19T16:50:28.428992+00:00 · **Legacy report time:** 2026-11-19T16:51:24.648378+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.572 | 77.68 | +0.56% | 0.41x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 2 | INJ/USD ⭐ | 7.162 | 74.12 | +0.94% | 1.94x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD | 0.021816 | 71.16 | +1.28% | 0.45x | MODERATE 61/100 | VERY_HIGH 81/100 | Watch |
| 4 | XRP/USD | 0.97438 | 70.64 | +0.41% | 1.81x | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 5 | ADA/USD | 0.152808 | 70.04 | +0.21% | 1.89x | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 6 | PYTH/USD | 0.05624 | 66.75 | +0.23% | 0.47x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 7 | BILL/USD | 0.00437 | 66.56 | -0.91% | 1.67x | WEAK 43/100 | EXTREME 85/100 | Do nothing |
| 8 | BMT/USD | 0.02051 | 65.63 | +1.28% | 0.03x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 9 | SKR/USD | 0.010367 | 65.00 | +0.14% | 0.31x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |
| 10 | HYPE/USD | 67.9 | 61.38 | +0.43% | 0.43x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | AKT/USD | 0.5461 | 59.28 | +0.17% | 0.27x | MODERATE 50/100 | VERY_HIGH 82/100 | Watch |
| 12 | PEPE/USD | 3.811e-06 | 51.67 | +0.53% | 0.89x | MODERATE 56/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.099908 | 82.21 | +1.79% | 2.04x | 7908 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 2 | TRUST/USD | 0.05437 | 75.17 | +0.78% | 2.78x | 2039 | STRONG 88/100 | VERY_HIGH 73/100 | Watch |
| 3 | INJ/USD ⭐ | 7.142 | 70.78 | +0.94% | 1.94x | 6780 | STRONG 90/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
