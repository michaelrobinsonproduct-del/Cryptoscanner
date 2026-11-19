# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:30:24.107151+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44555376487
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 52fafb2da3055d713ca78d9ee31366358143731c (atomic ledger/results publication)
**Ledger generation:** 802 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 595; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.809 | 80.928 | 86.717 | +5.25% | -1.51% | 1.18x | 10.1 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 2 | LIGHTER/USD | 2.922 | 78.874 | 70.626 | +7.66% | -1.35% | 5.24x | 20.6 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | AKT/USD | 0.5515 | 73.787 | 72.848 | +6.47% | -0.47% | 1.33x | 7.3 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | SENT/USD | 0.021404 | 67.157 | 60.947 | +3.88% | -1.76% | 3.50x | 0.5 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 5 | ETH/USD | 1786.26 | 67.102 | 59.508 | +0.65% | -0.49% | 2.01x | 0.1 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HYPE/USD | 68.42 | 65.890 | 70.388 | +2.30% | -0.44% | 0.77x | 1.5 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | GRASS/USD | 0.4431 | 65.650 | 66.475 | +9.35% | -0.98% | 1.41x | 24.9 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 8 | ZEC/USD | 930.72 | 62.524 | 67.100 | +2.06% | -0.65% | 0.87x | 4.6 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SKR/USD | 0.010352 | 61.481 | 65.347 | +7.46% | -1.21% | 1.22x | 21.3 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 31/100 | EXTREME 96/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.97985 | 59.967 | 64.713 | +1.39% | -0.29% | 0.67x | 0.1 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 63295.1 | 58.283 | 58.444 | +0.49% | -0.26% | 1.11x | 0.0 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | USELESS/USD | 0.10422 | 56.432 | 69.267 | +9.06% | -1.15% | 0.29x | 26.1 | 2026-11-19T15:30:15.417661+00:00 | Not calibrated | WEAK 23/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 86.717 | 22.809 | -1.51% | 1.18x |
| 2 | AKT/USD | 72.848 | 0.5515 | -0.47% | 1.33x |
| 3 | LIGHTER/USD | 70.626 | 2.922 | -1.35% | 5.24x |
| 4 | HYPE/USD | 70.388 | 68.42 | -0.44% | 0.77x |
| 5 | USELESS/USD | 69.267 | 0.10422 | -1.15% | 0.29x |
| 6 | ZEC/USD | 67.100 | 930.72 | -0.65% | 0.87x |
| 7 | GRASS/USD | 66.475 | 0.4431 | -0.98% | 1.41x |
| 8 | SKR/USD | 65.347 | 0.010352 | -1.21% | 1.22x |
| 9 | XRP/USD | 64.713 | 0.97985 | -0.29% | 0.67x |
| 10 | SENT/USD | 60.947 | 0.021404 | -1.76% | 3.50x |
| 11 | ETH/USD | 59.508 | 1786.26 | -0.49% | 2.01x |
| 12 | XBT/USD | 58.444 | 63295.1 | -0.26% | 1.11x |

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

- Persisted scans: 802; predictions: 6768; observations: 485027.
- Matured sampled outcomes across 1/6/24/48h: 6767; gap abstentions: 15216. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44555376487 · **Generation:** 802 · **Legacy run:** 44555376487
**Main quote time:** 2026-11-19T15:30:24.107151+00:00 · **Legacy report time:** 2026-11-19T15:31:19.341740+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.809 | 80.93 | -1.51% | 1.18x | MODERATE 45/100 | VERY_HIGH 78/100 | Do nothing |
| 2 | LIGHTER/USD | 2.922 | 78.87 | -1.35% | 5.24x | MODERATE 59/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | AKT/USD | 0.5515 | 73.79 | -0.47% | 1.33x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 4 | SENT/USD | 0.021404 | 67.16 | -1.76% | 3.50x | MODERATE 64/100 | VERY_HIGH 70/100 | Do nothing |
| 5 | ETH/USD | 1786.26 | 67.10 | -0.49% | 2.01x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | HYPE/USD | 68.42 | 65.89 | -0.44% | 0.77x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | GRASS/USD | 0.4431 | 65.65 | -0.98% | 1.41x | WEAK 43/100 | VERY_HIGH 78/100 | Watch |
| 8 | ZEC/USD | 930.72 | 62.52 | -0.65% | 0.87x | WEAK 36/100 | HIGH 68/100 | Watch |
| 9 | SKR/USD | 0.010352 | 61.48 | -1.21% | 1.22x | WEAK 31/100 | EXTREME 96/100 | Do nothing |
| 10 | XRP/USD | 0.97985 | 59.97 | -0.29% | 0.67x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 63295.1 | 58.28 | -0.26% | 1.11x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | USELESS/USD | 0.10422 | 56.43 | -1.15% | 0.29x | WEAK 23/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
