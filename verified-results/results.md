# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T04:12:42.683340+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45324421917
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 40e84798a779794455461b0764d5ded74c5c79c2 (atomic ledger/results publication)
**Ledger generation:** 1523 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01634 | 83.404 | 66.957 | +7.29% | +2.06% | 1.61x | 18.4 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 24.885 | 81.763 | 62.483 | +1.79% | +0.86% | 8.53x | 10.1 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | STRONG 91/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 2.992 | 71.306 | 56.365 | +0.36% | +1.28% | 1.85x | 2.3 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | MON/USD | 0.01235 | 67.265 | 76.500 | +7.20% | -0.56% | 0.36x | 16.2 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.491e-06 | 62.397 | 59.653 | +2.02% | +1.16% | 0.69x | 8.6 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XMR/USD | 489.99 | 57.165 | 59.595 | +0.82% | +0.43% | 0.54x | 2.2 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95058 | 56.408 | 62.970 | +1.19% | +0.37% | 0.16x | 0.7 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | AAVE/USD | 98.21 | 54.191 | 55.267 | +1.20% | +0.60% | 0.59x | 3.1 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 9.05766 | 50.886 | 57.603 | +0.59% | +0.28% | 0.19x | 3.0 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | DOT/USD | 0.6779 | 50.193 | 32.366 | +0.36% | +0.57% | 5.25x | 10.3 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 11 | UNI/USD | 4.8531 | 47.622 | 50.342 | +0.31% | +0.53% | 0.47x | 4.7 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | WLD/USD | 0.2411 | 40.572 | 39.219 | +1.18% | +0.97% | 0.65x | 8.3 | 2026-11-24T04:12:34.800522+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.500 | 0.01235 | -0.56% | 0.36x |
| 2 | AI/USD | 66.957 | 0.01634 | +2.06% | 1.61x |
| 3 | XRP/USD | 62.970 | 0.95058 | +0.37% | 0.16x |
| 4 | VVV/USD | 62.483 | 24.885 | +0.86% | 8.53x |
| 5 | PEPE/USD | 59.653 | 3.491e-06 | +1.16% | 0.69x |
| 6 | XMR/USD | 59.595 | 489.99 | +0.43% | 0.54x |
| 7 | LINK/USD | 57.603 | 9.05766 | +0.28% | 0.19x |
| 8 | NEAR/USD | 56.365 | 2.992 | +1.28% | 1.85x |
| 9 | AAVE/USD | 55.267 | 98.21 | +0.60% | 0.59x |
| 10 | UNI/USD | 50.342 | 4.8531 | +0.53% | 0.47x |
| 11 | WLD/USD | 39.219 | 0.2411 | +0.97% | 0.65x |
| 12 | DOT/USD | 32.366 | 0.6779 | +0.57% | 5.25x |

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

- Persisted scans: 1523; predictions: 13009; observations: 922605.
- Matured sampled outcomes across 1/6/24/48h: 24234; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45324421917 · **Generation:** 1523 · **Legacy run:** 45324421917
**Main quote time:** 2026-11-24T04:12:42.683340+00:00 · **Legacy report time:** 2026-11-24T04:13:42.801144+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01634 | 83.40 | +2.06% | 1.61x | STRONG 92/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 24.885 | 81.76 | +0.86% | 8.53x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 2.992 | 71.31 | +1.28% | 1.85x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | MON/USD | 0.01235 | 67.27 | -0.56% | 0.36x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | PEPE/USD | 3.491e-06 | 62.40 | +1.16% | 0.69x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 6 | XMR/USD | 489.99 | 57.16 | +0.43% | 0.54x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.95058 | 56.41 | +0.37% | 0.16x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 8 | AAVE/USD | 98.21 | 54.19 | +0.60% | 0.59x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 9.05766 | 50.89 | +0.28% | 0.19x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 10 | DOT/USD | 0.6779 | 50.19 | +0.57% | 5.25x | STRONG 75/100 | HIGH 66/100 | Watch |
| 11 | UNI/USD | 4.8531 | 47.62 | +0.53% | 0.47x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | WLD/USD | 0.2411 | 40.57 | +0.97% | 0.65x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01632 | 79.35 | +2.06% | 1.61x | 2880 | STRONG 90/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 24.864 | 67.99 | +0.86% | 8.53x | 13633 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 2.9898 | 60.71 | +1.28% | 1.85x | 23173 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 4 | XLM/USD | 0.130192 | 53.01 | +0.18% | 1.54x | 18104 | MODERATE 62/100 | HIGH 55/100 | Watch |

**Same-run overlap:** AI/USD, VVV/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
