# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:35:22.989840+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44445319796
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 735ae09387af8d0431f7a7fed166dd373555bf4a (atomic ledger/results publication)
**Ledger generation:** 732 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022007 | 82.707 | 72.691 | +6.80% | +0.60% | 1.70x | 7.7 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.3207 | 76.346 | 59.796 | +0.71% | +0.44% | 2.43x | 0.3 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 21.961 | 70.010 | 54.439 | +1.34% | +0.11% | 4.58x | 7.7 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03389 | 59.140 | 41.467 | +2.36% | +0.53% | 2.76x | 11.8 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | ICP/USD | 2.246 | 54.684 | 53.133 | +3.12% | +0.18% | 1.07x | 13.4 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 6 | TON/USD | 1.027 | 50.342 | 33.387 | +0.59% | +0.39% | 3.13x | 9.7 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.05725 | 45.776 | 38.211 | +2.23% | -0.33% | 1.92x | 17.4 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | BMT/USD | 0.01962 | 41.121 | 53.076 | +3.92% | -0.91% | 0.26x | 10.2 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | WEAK 21/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | LIGHTER/USD | 2.732 | 30.064 | 34.914 | +0.66% | +0.33% | 0.35x | 11.0 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | DRV/USD | 0.26611 | 25.566 | 33.279 | +0.54% | -0.08% | 0.27x | 7.5 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | W/USD | 0.00894 | 17.649 | 22.249 | +0.34% | +0.00% | 0.54x | 22.4 | 2026-11-19T02:35:16.233822+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.691 | 0.022007 | +0.60% | 1.70x |
| 2 | NEAR/USD | 59.796 | 3.3207 | +0.44% | 2.43x |
| 3 | VVV/USD | 54.439 | 21.961 | +0.11% | 4.58x |
| 4 | ICP/USD | 53.133 | 2.246 | +0.18% | 1.07x |
| 5 | BMT/USD | 53.076 | 0.01962 | -0.91% | 0.26x |
| 6 | UAI/USD | 41.467 | 0.03389 | +0.53% | 2.76x |
| 7 | MEGA/USD | 38.211 | 0.05725 | -0.33% | 1.92x |
| 8 | LIGHTER/USD | 34.914 | 2.732 | +0.33% | 0.35x |
| 9 | TON/USD | 33.387 | 1.027 | +0.39% | 3.13x |
| 10 | DRV/USD | 33.279 | 0.26611 | -0.08% | 0.27x |
| 11 | W/USD | 22.249 | 0.00894 | +0.00% | 0.54x |

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

- Persisted scans: 732; predictions: 5957; observations: 442795.
- Matured sampled outcomes across 1/6/24/48h: 5902; gap abstentions: 13495. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44445319796 · **Generation:** 732 · **Legacy run:** 44445319796
**Main quote time:** 2026-11-19T02:35:22.989840+00:00 · **Legacy report time:** 2026-11-19T02:36:00.068100+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022007 | 82.71 | +0.60% | 1.70x | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3207 | 76.35 | +0.44% | 2.43x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 21.961 | 70.01 | +0.11% | 4.58x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03389 | 59.14 | +0.53% | 2.76x | STRONG 90/100 | VERY_HIGH 73/100 | Watch |
| 5 | ICP/USD ⭐ | 2.246 | 54.68 | +0.18% | 1.07x | MODERATE 57/100 | HIGH 68/100 | Watch |
| 6 | TON/USD | 1.027 | 50.34 | +0.39% | 3.13x | STRONG 80/100 | HIGH 60/100 | Watch |
| 7 | MEGA/USD | 0.05725 | 45.78 | -0.33% | 1.92x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |
| 8 | BMT/USD | 0.01962 | 41.12 | -0.91% | 0.26x | WEAK 21/100 | EXTREME 94/100 | Do nothing |
| 9 | LIGHTER/USD | 2.732 | 30.06 | +0.33% | 0.35x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 10 | DRV/USD | 0.26611 | 25.57 | -0.08% | 0.27x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | W/USD | 0.00894 | 17.65 | +0.00% | 0.54x | WEAK 19/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022021 | 82.37 | +0.60% | 1.70x | 7823 | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 2 | ICP/USD ⭐ | 2.251 | 67.80 | +0.18% | 1.07x | 3231 | MODERATE 59/100 | VERY_HIGH 74/100 | Watch |
| 3 | VVV/USD ⭐ | 21.999 | 59.89 | +0.11% | 4.58x | 8162 | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 3.3193 | 56.78 | +0.44% | 2.43x | 13316 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 5 | UAI/USD ⭐ | 0.03389 | 54.57 | +0.53% | 2.76x | 2054 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |
| 6 | LTC/USD | 44.07 | 45.67 | +0.07% | 1.41x | 11695 | MODERATE 58/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SENT/USD, NEAR/USD, VVV/USD, UAI/USD, ICP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
