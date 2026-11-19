# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:50:25.139281+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44447097072
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** c9e4e836c434627be65026a202fa3bb5d220cc4a (atomic ledger/results publication)
**Ledger generation:** 735 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3159 | 70.958 | 56.816 | +0.56% | -0.17% | 3.96x | 4.2 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021975 | 70.569 | 68.380 | +6.65% | +0.37% | 1.03x | 16.4 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | VVV/USD | 21.972 | 54.866 | 56.889 | +1.39% | +0.16% | 0.72x | 3.6 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ICP/USD | 2.244 | 49.923 | 54.772 | +3.03% | -0.09% | 0.56x | 8.9 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | BMT/USD | 0.01952 | 45.852 | 46.781 | +3.39% | -0.51% | 1.16x | 15.4 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | WEAK 28/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | TRUMP/USD | 0.95 | 43.397 | 33.341 | +0.53% | -0.11% | 2.06x | 10.5 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | UAI/USD | 0.03349 | 42.608 | 32.926 | +1.15% | -1.06% | 8.24x | 12.0 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 8 | AKE/USD | 0.01043795 | 39.174 | 30.887 | +0.45% | -0.62% | 2.14x | 13.7 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | DRV/USD | 0.26626 | 35.987 | 34.630 | +0.59% | +0.06% | 1.11x | 5.6 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |
| 10 | MEGA/USD | 0.05704 | 29.890 | 35.512 | +1.86% | -0.37% | 0.62x | 17.6 | 2026-11-19T02:50:18.790859+00:00 | Not calibrated | WEAK 15/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 68.380 | 0.021975 | +0.37% | 1.03x |
| 2 | VVV/USD | 56.889 | 21.972 | +0.16% | 0.72x |
| 3 | NEAR/USD | 56.816 | 3.3159 | -0.17% | 3.96x |
| 4 | ICP/USD | 54.772 | 2.244 | -0.09% | 0.56x |
| 5 | BMT/USD | 46.781 | 0.01952 | -0.51% | 1.16x |
| 6 | MEGA/USD | 35.512 | 0.05704 | -0.37% | 0.62x |
| 7 | DRV/USD | 34.630 | 0.26626 | +0.06% | 1.11x |
| 8 | TRUMP/USD | 33.341 | 0.95 | -0.11% | 2.06x |
| 9 | UAI/USD | 32.926 | 0.03349 | -1.06% | 8.24x |
| 10 | AKE/USD | 30.887 | 0.01043795 | -0.62% | 2.14x |

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

- Persisted scans: 735; predictions: 5987; observations: 444622.
- Matured sampled outcomes across 1/6/24/48h: 5947; gap abstentions: 13506. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44447097072 · **Generation:** 735 · **Legacy run:** 44447097072
**Main quote time:** 2026-11-19T02:50:25.139281+00:00 · **Legacy report time:** 2026-11-19T02:50:58.216695+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.3159 | 70.96 | -0.17% | 3.96x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | SENT/USD ⭐ | 0.021975 | 70.57 | +0.37% | 1.03x | STRONG 75/100 | VERY_HIGH 80/100 | Watch |
| 3 | VVV/USD | 21.972 | 54.87 | +0.16% | 0.72x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 4 | ICP/USD | 2.244 | 49.92 | -0.09% | 0.56x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | BMT/USD | 0.01952 | 45.85 | -0.51% | 1.16x | WEAK 28/100 | EXTREME 86/100 | Do nothing |
| 6 | TRUMP/USD | 0.95 | 43.40 | -0.11% | 2.06x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |
| 7 | UAI/USD | 0.03349 | 42.61 | -1.06% | 8.24x | MODERATE 46/100 | VERY_HIGH 83/100 | Watch |
| 8 | AKE/USD | 0.01043795 | 39.17 | -0.62% | 2.14x | MODERATE 45/100 | VERY_HIGH 72/100 | Watch |
| 9 | DRV/USD ⭐ | 0.26626 | 35.99 | +0.06% | 1.11x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 10 | MEGA/USD | 0.05704 | 29.89 | -0.37% | 0.62x | WEAK 15/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022 | 72.19 | +0.37% | 1.03x | 7910 | STRONG 81/100 | VERY_HIGH 74/100 | Watch |
| 2 | TON/USD | 1.028 | 37.17 | +0.10% | 2.04x | 2751 | MODERATE 64/100 | HIGH 60/100 | Watch |
| 3 | DRV/USD ⭐ | 0.26626 | 35.28 | +0.06% | 1.11x | 2624 | MODERATE 53/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
