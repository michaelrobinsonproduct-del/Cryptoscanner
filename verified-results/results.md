# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:00:28.527284+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44455196752
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 224ace2591178497ffa82c22109bcc6bf6395473 (atomic ledger/results publication)
**Ledger generation:** 749 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022558 | 89.683 | 70.137 | +9.48% | +1.28% | 2.31x | 13.3 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.27 | 82.748 | 66.961 | +2.76% | +0.16% | 8.39x | 6.7 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ETH/USD | 1791.76 | 80.133 | 61.677 | +0.96% | +0.69% | 2.68x | 0.1 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.7245 | 76.981 | 59.763 | +0.78% | +0.44% | 7.45x | 1.4 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NEAR/USD | 3.3814 | 75.933 | 70.318 | +2.55% | +0.53% | 1.30x | 5.0 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LINK/USD | 9.10743 | 74.362 | 56.645 | +0.38% | +0.54% | 3.34x | 2.1 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | KNTQ/USD | 0.23979 | 73.812 | 73.919 | +11.30% | +1.48% | 0.25x | 5.4 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | ZEC/USD | 918.95 | 72.841 | 58.522 | +0.77% | +0.90% | 1.98x | 3.7 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | SOL/USD | 74.17 | 70.088 | 60.322 | +0.86% | +0.57% | 1.69x | 1.3 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | HYPE/USD | 67.28 | 63.761 | 58.443 | +0.60% | +0.55% | 1.26x | 1.5 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 11 | TAO/USD | 194.4636 | 63.464 | 60.952 | +1.30% | +0.88% | 0.81x | 6.4 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 12 | LTC/USD | 44.42 | 61.118 | 51.880 | +0.93% | +0.36% | 1.74x | 2.3 | 2026-11-19T04:00:20.109174+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | KNTQ/USD | 73.919 | 0.23979 | +1.48% | 0.25x |
| 2 | NEAR/USD | 70.318 | 3.3814 | +0.53% | 1.30x |
| 3 | SENT/USD | 70.137 | 0.022558 | +1.28% | 2.31x |
| 4 | VVV/USD | 66.961 | 22.27 | +0.16% | 8.39x |
| 5 | ETH/USD | 61.677 | 1791.76 | +0.69% | 2.68x |
| 6 | TAO/USD | 60.952 | 194.4636 | +0.88% | 0.81x |
| 7 | SOL/USD | 60.322 | 74.17 | +0.57% | 1.69x |
| 8 | SUI/USD | 59.763 | 0.7245 | +0.44% | 7.45x |
| 9 | ZEC/USD | 58.522 | 918.95 | +0.90% | 1.98x |
| 10 | HYPE/USD | 58.443 | 67.28 | +0.55% | 1.26x |
| 11 | LINK/USD | 56.645 | 9.10743 | +0.54% | 3.34x |
| 12 | LTC/USD | 51.880 | 44.42 | +0.36% | 1.74x |

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

- Persisted scans: 749; predictions: 6132; observations: 453148.
- Matured sampled outcomes across 1/6/24/48h: 6102; gap abstentions: 13596. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44455196752 · **Generation:** 749 · **Legacy run:** 44455196752
**Main quote time:** 2026-11-19T04:00:28.527284+00:00 · **Legacy report time:** 2026-11-19T04:01:05.998473+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.022558 | 89.68 | +1.28% | 2.31x | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.27 | 82.75 | +0.16% | 8.39x | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD ⭐ | 1791.76 | 80.13 | +0.69% | 2.68x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.7245 | 76.98 | +0.44% | 7.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.3814 | 75.93 | +0.53% | 1.30x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | LINK/USD | 9.10743 | 74.36 | +0.54% | 3.34x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 7 | KNTQ/USD | 0.23979 | 73.81 | +1.48% | 0.25x | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |
| 8 | ZEC/USD | 918.95 | 72.84 | +0.90% | 1.98x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 9 | SOL/USD ⭐ | 74.17 | 70.09 | +0.57% | 1.69x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 10 | HYPE/USD ⭐ | 67.28 | 63.76 | +0.55% | 1.26x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | TAO/USD | 194.4636 | 63.46 | +0.88% | 0.81x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 12 | LTC/USD | 44.42 | 61.12 | +0.36% | 1.74x | STRONG 76/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.335 | 84.12 | +0.16% | 8.39x | 8721 | STRONG 97/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.3852 | 79.64 | +0.53% | 1.30x | 13862 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD ⭐ | 1794.65 | 73.22 | +0.69% | 2.68x | 58275 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.7259 | 70.26 | +0.44% | 7.45x | 6757 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | TIA/USD | 0.3536 | 68.45 | +0.83% | 2.63x | 2182 | STRONG 89/100 | HIGH 67/100 | Watch |
| 6 | SOL/USD ⭐ | 74.24 | 65.20 | +0.57% | 1.69x | 35165 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD | 0.96928 | 65.02 | +0.54% | 5.70x | 35847 | STRONG 88/100 | HIGH 55/100 | Watch |
| 8 | HYPE/USD ⭐ | 67.32 | 59.60 | +0.55% | 1.26x | 14462 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, ETH/USD, SUI/USD, NEAR/USD, SOL/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
