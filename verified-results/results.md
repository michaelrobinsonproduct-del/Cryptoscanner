# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:55:25.705647+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44603171565
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 8caf31978198f03525990a5a49e70d751c8ebdfe (atomic ledger/results publication)
**Ledger generation:** 849 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.492 | 94.007 | 79.295 | +3.79% | -0.06% | 7.69x | 4.4 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5564 | 92.133 | 70.955 | +7.41% | +1.24% | 6.08x | 12.6 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | STRONG 96/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | SKR/USD | 0.0101 | 72.316 | 61.605 | +4.85% | -0.28% | 2.21x | 6.9 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152889 | 67.547 | 61.357 | +1.08% | +0.08% | 1.58x | 2.4 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.71 | 58.949 | 61.471 | +1.24% | +0.33% | 0.58x | 4.4 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | TRX/USD | 0.310259 | 57.591 | 42.639 | +0.32% | -0.01% | 3.25x | 1.2 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 7 | CT/USD | 0.1299 | 55.221 | 65.339 | +9.90% | -0.46% | 0.22x | 23.1 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | WEAK 23/100 | EXTREME 93/100 | Do nothing | WATCH |
| 8 | ALEO/USD | 0.03084 | 54.996 | 54.538 | +2.87% | +0.19% | 0.95x | 3.2 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 47/100 | HIGH 67/100 | Watch | WATCH |
| 9 | INJ/USD | 7.088 | 46.851 | 53.464 | +1.53% | +0.18% | 0.25x | 4.2 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.761e-06 | 41.960 | 41.376 | +0.40% | +0.35% | 0.89x | 5.3 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 11 | TIA/USD | 0.3462 | 40.557 | 31.683 | +0.46% | +0.26% | 1.76x | 5.8 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 12 | BNB/USD | 582.83 | 40.104 | 42.131 | +0.26% | -0.22% | 0.91x | 1.5 | 2026-11-19T19:55:17.537409+00:00 | Not calibrated | WEAK 25/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.295 | 22.492 | -0.06% | 7.69x |
| 2 | AKT/USD | 70.955 | 0.5564 | +1.24% | 6.08x |
| 3 | CT/USD | 65.339 | 0.1299 | -0.46% | 0.22x |
| 4 | SKR/USD | 61.605 | 0.0101 | -0.28% | 2.21x |
| 5 | HYPE/USD | 61.471 | 67.71 | +0.33% | 0.58x |
| 6 | ADA/USD | 61.357 | 0.152889 | +0.08% | 1.58x |
| 7 | ALEO/USD | 54.538 | 0.03084 | +0.19% | 0.95x |
| 8 | INJ/USD | 53.464 | 7.088 | +0.18% | 0.25x |
| 9 | TRX/USD | 42.639 | 0.310259 | -0.01% | 3.25x |
| 10 | BNB/USD | 42.131 | 582.83 | -0.22% | 0.91x |
| 11 | PEPE/USD | 41.376 | 3.761e-06 | +0.35% | 0.89x |
| 12 | TIA/USD | 31.683 | 0.3462 | +0.26% | 1.76x |

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

- Persisted scans: 849; predictions: 7332; observations: 513128.
- Matured sampled outcomes across 1/6/24/48h: 7355; gap abstentions: 15628. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44603171565 · **Generation:** 849 · **Legacy run:** 44603171565
**Main quote time:** 2026-11-19T19:55:25.705647+00:00 · **Legacy report time:** 2026-11-19T19:56:16.664226+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.492 | 94.01 | -0.06% | 7.69x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5564 | 92.13 | +1.24% | 6.08x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | SKR/USD | 0.0101 | 72.32 | -0.28% | 2.21x | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |
| 4 | ADA/USD ⭐ | 0.152889 | 67.55 | +0.08% | 1.58x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | HYPE/USD | 67.71 | 58.95 | +0.33% | 0.58x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | TRX/USD | 0.310259 | 57.59 | -0.01% | 3.25x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 7 | CT/USD | 0.1299 | 55.22 | -0.46% | 0.22x | WEAK 23/100 | EXTREME 93/100 | Do nothing |
| 8 | ALEO/USD | 0.03084 | 55.00 | +0.19% | 0.95x | MODERATE 47/100 | HIGH 67/100 | Watch |
| 9 | INJ/USD | 7.088 | 46.85 | +0.18% | 0.25x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 10 | PEPE/USD | 3.761e-06 | 41.96 | +0.35% | 0.89x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 11 | TIA/USD | 0.3462 | 40.56 | +0.26% | 1.76x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 12 | BNB/USD | 582.83 | 40.10 | -0.22% | 0.91x | WEAK 25/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5564 | 83.05 | +1.24% | 6.08x | 3375 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.152826 | 59.18 | +0.08% | 1.58x | 11840 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** AKT/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
