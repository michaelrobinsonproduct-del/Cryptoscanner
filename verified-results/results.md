# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:15:22.316747+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44427412122
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 8c21ea27d5209b9c5cd9eb3af48855694795a38b (atomic ledger/results publication)
**Ledger generation:** 704 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ATOM/USD | 1.305 | 51.223 | 34.030 | +0.49% | +0.44% | 3.11x | 6.1 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5198 | 49.537 | 33.187 | +0.35% | +0.27% | 2.55x | 1.9 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 3 | INJ/USD | 7.018 | 47.741 | 42.737 | +0.53% | +0.43% | 1.29x | 4.3 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | MODERATE 59/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04568 | 47.655 | 43.639 | +0.57% | +0.44% | 1.18x | 8.8 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | BAT/USD | 0.09349 | 43.997 | 31.862 | +0.51% | +0.25% | 2.09x | 5.3 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | STRONG 77/100 | HIGH 67/100 | Watch | WATCH |
| 6 | UAI/USD | 0.03322 | 39.827 | 25.642 | +0.33% | +0.21% | 2.31x | 15.1 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | W/USD | 0.00895 | 32.804 | 28.648 | +0.45% | +0.22% | 1.30x | 11.2 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | CAP/USD | 0.096402 | 32.364 | 24.347 | +0.40% | +0.40% | 1.60x | 19.9 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.09591 | 23.087 | 31.085 | +0.37% | +0.11% | 0.14x | 19.7 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ICP/USD | 2.184 | 23.073 | 31.873 | +0.28% | -0.18% | 0.21x | 13.7 | 2026-11-19T00:15:17.327842+00:00 | Not calibrated | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 43.639 | 0.04568 | +0.44% | 1.18x |
| 2 | INJ/USD | 42.737 | 7.018 | +0.43% | 1.29x |
| 3 | ATOM/USD | 34.030 | 1.305 | +0.44% | 3.11x |
| 4 | AKT/USD | 33.187 | 0.5198 | +0.27% | 2.55x |
| 5 | ICP/USD | 31.873 | 2.184 | -0.18% | 0.21x |
| 6 | BAT/USD | 31.862 | 0.09349 | +0.25% | 2.09x |
| 7 | USELESS/USD | 31.085 | 0.09591 | +0.11% | 0.14x |
| 8 | W/USD | 28.648 | 0.00895 | +0.22% | 1.30x |
| 9 | UAI/USD | 25.642 | 0.03322 | +0.21% | 2.31x |
| 10 | CAP/USD | 24.347 | 0.096402 | +0.40% | 1.60x |

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

- Persisted scans: 704; predictions: 5685; observations: 425743.
- Matured sampled outcomes across 1/6/24/48h: 5567; gap abstentions: 13350. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44427412122 · **Generation:** 704 · **Legacy run:** 44427412122
**Main quote time:** 2026-11-19T00:15:22.316747+00:00 · **Legacy report time:** 2026-11-19T00:16:04.338471+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ATOM/USD ⭐ | 1.305 | 51.22 | +0.44% | 3.11x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 2 | AKT/USD | 0.5198 | 49.54 | +0.27% | 2.55x | STRONG 80/100 | HIGH 60/100 | Watch |
| 3 | INJ/USD ⭐ | 7.018 | 47.74 | +0.43% | 1.29x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04568 | 47.65 | +0.44% | 1.18x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 5 | BAT/USD | 0.09349 | 44.00 | +0.25% | 2.09x | STRONG 77/100 | HIGH 67/100 | Watch |
| 6 | UAI/USD | 0.03322 | 39.83 | +0.21% | 2.31x | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 7 | W/USD | 0.00895 | 32.80 | +0.22% | 1.30x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 8 | CAP/USD ⭐ | 0.096402 | 32.36 | +0.40% | 1.60x | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |
| 9 | USELESS/USD | 0.09591 | 23.09 | +0.11% | 0.14x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ICP/USD | 2.184 | 23.07 | -0.18% | 0.21x | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ATOM/USD ⭐ | 1.305 | 49.82 | +0.44% | 3.11x | 2736 | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04571 | 40.12 | +0.44% | 1.18x | 10946 | MODERATE 65/100 | HIGH 62/100 | Watch |
| 3 | INJ/USD ⭐ | 7.026 | 38.87 | +0.43% | 1.29x | 5141 | MODERATE 64/100 | HIGH 55/100 | Watch |
| 4 | CAP/USD ⭐ | 0.096821 | 36.55 | +0.40% | 1.60x | 2715 | MODERATE 63/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** ATOM/USD, INJ/USD, NIGHT/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
