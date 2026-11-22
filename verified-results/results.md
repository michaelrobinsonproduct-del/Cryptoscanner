# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T12:50:58.215660+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45024276424
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 68f7fb7a76fe7ced081f6c9ee1472c1166ac84cc (atomic ledger/results publication)
**Ledger generation:** 1285 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04707 | 97.956 | 79.969 | +6.30% | +1.07% | 2.26x | 19.1 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 99/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0031 | 82.274 | 81.326 | +4.05% | +1.04% | 0.57x | 4.0 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 62.81 | 79.745 | 72.150 | +2.56% | +1.06% | 1.23x | 1.6 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 4 | TAO/USD | 191.073 | 78.583 | 68.717 | +2.88% | +0.47% | 1.75x | 6.9 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | INJ/USD | 6.229 | 76.601 | 69.353 | +4.29% | +0.73% | 1.36x | 6.4 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002489 | 76.585 | 82.067 | +6.19% | +0.69% | 0.11x | 8.0 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LINK/USD | 8.79261 | 74.374 | 63.399 | +2.30% | +0.23% | 1.98x | 0.6 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | DRV/USD | 0.3647 | 70.309 | 73.418 | +8.80% | +0.01% | 0.68x | 27.2 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6586 | 69.004 | 66.461 | +1.75% | +0.46% | 1.03x | 1.5 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XBT/USD | 60720.6 | 64.479 | 62.339 | +1.05% | +0.29% | 1.07x | 0.0 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 11 | ETH/USD | 1704.81 | 62.647 | 64.345 | +1.34% | +0.29% | 0.69x | 0.1 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PENGU/USD | 0.004311 | 53.409 | 36.547 | +0.75% | +0.37% | 3.75x | 2.3 | 2026-11-22T12:50:51.357119+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 82.067 | 0.002489 | +0.69% | 0.11x |
| 2 | NEAR/USD | 81.326 | 3.0031 | +1.04% | 0.57x |
| 3 | NIGHT/USD | 79.969 | 0.04707 | +1.07% | 2.26x |
| 4 | DRV/USD | 73.418 | 0.3647 | +0.01% | 0.68x |
| 5 | HYPE/USD | 72.150 | 62.81 | +1.06% | 1.23x |
| 6 | INJ/USD | 69.353 | 6.229 | +0.73% | 1.36x |
| 7 | TAO/USD | 68.717 | 191.073 | +0.47% | 1.75x |
| 8 | SUI/USD | 66.461 | 0.6586 | +0.46% | 1.03x |
| 9 | ETH/USD | 64.345 | 1704.81 | +0.29% | 0.69x |
| 10 | LINK/USD | 63.399 | 8.79261 | +0.23% | 1.98x |
| 11 | XBT/USD | 62.339 | 60720.6 | +0.29% | 1.07x |
| 12 | PENGU/USD | 36.547 | 0.004311 | +0.37% | 3.75x |

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

- Persisted scans: 1285; predictions: 10340; observations: 777674.
- Matured sampled outcomes across 1/6/24/48h: 14952; gap abstentions: 22249. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45024276424 · **Generation:** 1285 · **Legacy run:** 45024276424
**Main quote time:** 2026-11-22T12:50:58.215660+00:00 · **Legacy report time:** 2026-11-22T12:51:39.545949+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04707 | 97.96 | +1.07% | 2.26x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NEAR/USD | 3.0031 | 82.27 | +1.04% | 0.57x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.81 | 79.75 | +1.06% | 1.23x | STRONG 85/100 | HIGH 62/100 | Watch |
| 4 | TAO/USD ⭐ | 191.073 | 78.58 | +0.47% | 1.75x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 5 | INJ/USD ⭐ | 6.229 | 76.60 | +0.73% | 1.36x | STRONG 93/100 | HIGH 55/100 | Watch |
| 6 | PUMP/USD | 0.002489 | 76.58 | +0.69% | 0.11x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 7 | LINK/USD ⭐ | 8.79261 | 74.37 | +0.23% | 1.98x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 8 | DRV/USD | 0.3647 | 70.31 | +0.01% | 0.68x | MODERATE 45/100 | VERY_HIGH 82/100 | Watch |
| 9 | SUI/USD ⭐ | 0.6586 | 69.00 | +0.46% | 1.03x | STRONG 80/100 | HIGH 62/100 | Watch |
| 10 | XBT/USD ⭐ | 60720.6 | 64.48 | +0.29% | 1.07x | STRONG 77/100 | HIGH 62/100 | Watch |
| 11 | ETH/USD | 1704.81 | 62.65 | +0.29% | 0.69x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | PENGU/USD | 0.004311 | 53.41 | +0.37% | 3.75x | STRONG 82/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04689 | 87.50 | +1.07% | 2.26x | 9390 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.229 | 86.54 | +0.73% | 1.36x | 7070 | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.78 | 83.09 | +1.06% | 1.23x | 13066 | STRONG 87/100 | HIGH 62/100 | Watch |
| 4 | TAO/USD ⭐ | 191.073 | 76.40 | +0.47% | 1.75x | 6694 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD | 790.32 | 72.62 | +0.58% | 9.76x | 26657 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6587 | 68.53 | +0.46% | 1.03x | 7447 | STRONG 79/100 | HIGH 62/100 | Watch |
| 7 | LINK/USD ⭐ | 8.78794 | 68.44 | +0.23% | 1.98x | 5877 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 8 | XBT/USD ⭐ | 60668.6 | 64.67 | +0.29% | 1.07x | 146112 | STRONG 77/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD, HYPE/USD, TAO/USD, INJ/USD, LINK/USD, SUI/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
