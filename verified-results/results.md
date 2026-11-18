# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:15:14.250570+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44311718922
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 06b315a27b25b6f2e2b68767fe3bb709adb534d1 (atomic ledger/results publication)
**Ledger generation:** 574 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04653 | 86.819 | 69.877 | +3.65% | +0.39% | 5.84x | 8.6 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.98575 | 73.777 | 57.243 | +0.33% | +0.41% | 2.45x | 0.1 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | MNT/USD | 0.386 | 66.647 | 53.005 | +3.40% | +0.16% | 2.29x | 7.8 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 4 | AKT/USD | 0.522 | 61.021 | 41.381 | +2.49% | +0.93% | 3.16x | 17.2 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.10079 | 59.761 | 54.067 | +3.29% | +0.78% | 1.18x | 21.9 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | STABLE/USD | 0.02333 | 55.491 | 60.962 | +10.83% | +0.30% | 0.30x | 30.0 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.08329 | 52.419 | 43.758 | +1.41% | +0.02% | 1.85x | 3.6 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | MODERATE 61/100 | HIGH 60/100 | Watch | WATCH |
| 8 | SENT/USD | 0.019396 | 46.064 | 54.429 | +3.89% | -0.85% | 0.59x | 7.7 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | ME/USD | 0.04 | 43.511 | 44.386 | +3.63% | -0.50% | 1.16x | 25.0 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | WEAK 22/100 | EXTREME 92/100 | Do nothing | WATCH |
| 10 | VVV/USD | 21.223 | 43.405 | 46.007 | +0.94% | +0.58% | 0.45x | 17.4 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | TRX/USD | 0.309272 | 36.834 | 44.110 | +0.44% | -0.04% | 0.29x | 0.9 | 2026-11-18T13:15:06.398213+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 69.877 | 0.04653 | +0.39% | 5.84x |
| 2 | STABLE/USD | 60.962 | 0.02333 | +0.30% | 0.30x |
| 3 | XRP/USD | 57.243 | 0.98575 | +0.41% | 2.45x |
| 4 | SENT/USD | 54.429 | 0.019396 | -0.85% | 0.59x |
| 5 | USELESS/USD | 54.067 | 0.10079 | +0.78% | 1.18x |
| 6 | MNT/USD | 53.005 | 0.386 | +0.16% | 2.29x |
| 7 | VVV/USD | 46.007 | 21.223 | +0.58% | 0.45x |
| 8 | ME/USD | 44.386 | 0.04 | -0.50% | 1.16x |
| 9 | TRX/USD | 44.110 | 0.309272 | -0.04% | 0.29x |
| 10 | CC/USD | 43.758 | 0.08329 | +0.02% | 1.85x |
| 11 | AKT/USD | 41.381 | 0.522 | +0.93% | 3.16x |

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

- Persisted scans: 574; predictions: 4853; observations: 346573.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13027. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44311718922 · **Generation:** 574 · **Legacy run:** 44311718922
**Main quote time:** 2026-11-18T13:15:14.250570+00:00 · **Legacy report time:** 2026-11-18T13:15:40.756982+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04653 | 86.82 | +0.39% | 5.84x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.98575 | 73.78 | +0.41% | 2.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | MNT/USD ⭐ | 0.386 | 66.65 | +0.16% | 2.29x | STRONG 88/100 | HIGH 60/100 | Watch |
| 4 | AKT/USD ⭐ | 0.522 | 61.02 | +0.93% | 3.16x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 5 | USELESS/USD ⭐ | 0.10079 | 59.76 | +0.78% | 1.18x | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |
| 6 | STABLE/USD | 0.02333 | 55.49 | +0.30% | 0.30x | MODERATE 48/100 | EXTREME 94/100 | Do nothing |
| 7 | CC/USD | 0.08329 | 52.42 | +0.02% | 1.85x | MODERATE 61/100 | HIGH 60/100 | Watch |
| 8 | SENT/USD | 0.019396 | 46.06 | -0.85% | 0.59x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 9 | ME/USD | 0.04 | 43.51 | -0.50% | 1.16x | WEAK 22/100 | EXTREME 92/100 | Do nothing |
| 10 | VVV/USD | 21.223 | 43.41 | +0.58% | 0.45x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 11 | TRX/USD | 0.309272 | 36.83 | -0.04% | 0.29x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04653 | 86.17 | +0.39% | 5.84x | 15939 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | USELESS/USD ⭐ | 0.10079 | 71.71 | +0.78% | 1.18x | 5301 | STRONG 71/100 | VERY_HIGH 74/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5228 | 66.12 | +0.93% | 3.16x | 4551 | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 4 | MNT/USD ⭐ | 0.386 | 65.28 | +0.16% | 2.29x | 2040 | STRONG 88/100 | HIGH 60/100 | Watch |
| 5 | XRP/USD ⭐ | 0.98559 | 60.12 | +0.41% | 2.45x | 35838 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD, XRP/USD, MNT/USD, AKT/USD, USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
