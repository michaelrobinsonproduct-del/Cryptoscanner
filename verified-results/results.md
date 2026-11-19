# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:20:28.379891+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44627533668
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 4419e2291ff4a2467dd667807c736103a85913ab (atomic ledger/results publication)
**Ledger generation:** 869 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021308 | 69.208 | 54.279 | +3.41% | -0.01% | 2.60x | 8.0 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | MODERATE 65/100 | HIGH 66/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05978 | 68.393 | 71.322 | +6.75% | -0.32% | 0.87x | 11.7 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 3 | SKR/USD | 0.009981 | 62.523 | 52.409 | +3.61% | -0.20% | 2.11x | 8.0 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.09835 | 56.334 | 52.327 | +2.92% | +0.35% | 1.23x | 15.3 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 5 | VVV/USD | 21.827 | 52.654 | 54.537 | +0.72% | -0.19% | 0.91x | 11.0 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5346 | 45.381 | 53.827 | +3.20% | -0.24% | 0.28x | 1.9 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | SYRUP/USD | 0.09589 | 28.817 | 31.148 | +0.98% | -0.43% | 0.98x | 14.6 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | WEAK 14/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | BLUR/USD | 0.00667 | 28.248 | 25.830 | +1.37% | +0.15% | 1.17x | 30.1 | 2026-11-19T22:20:21.129942+00:00 | Not calibrated | WEAK 29/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 71.322 | 0.05978 | -0.32% | 0.87x |
| 2 | VVV/USD | 54.537 | 21.827 | -0.19% | 0.91x |
| 3 | SENT/USD | 54.279 | 0.021308 | -0.01% | 2.60x |
| 4 | AKT/USD | 53.827 | 0.5346 | -0.24% | 0.28x |
| 5 | SKR/USD | 52.409 | 0.009981 | -0.20% | 2.11x |
| 6 | USELESS/USD | 52.327 | 0.09835 | +0.35% | 1.23x |
| 7 | SYRUP/USD | 31.148 | 0.09589 | -0.43% | 0.98x |
| 8 | BLUR/USD | 25.830 | 0.00667 | +0.15% | 1.17x |

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

- Persisted scans: 869; predictions: 7552; observations: 525140.
- Matured sampled outcomes across 1/6/24/48h: 7940; gap abstentions: 15737. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44627533668 · **Generation:** 869 · **Legacy run:** 44627533668
**Main quote time:** 2026-11-19T22:20:28.379891+00:00 · **Legacy report time:** 2026-11-19T22:21:12.366597+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021308 | 69.21 | -0.01% | 2.60x | MODERATE 65/100 | HIGH 66/100 | Watch |
| 2 | MEGA/USD | 0.05978 | 68.39 | -0.32% | 0.87x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 3 | SKR/USD | 0.009981 | 62.52 | -0.20% | 2.11x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 4 | USELESS/USD ⭐ | 0.09835 | 56.33 | +0.35% | 1.23x | MODERATE 68/100 | HIGH 68/100 | Watch |
| 5 | VVV/USD | 21.827 | 52.65 | -0.19% | 0.91x | WEAK 26/100 | VERY_HIGH 74/100 | Do nothing |
| 6 | AKT/USD | 0.5346 | 45.38 | -0.24% | 0.28x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | SYRUP/USD | 0.09589 | 28.82 | -0.43% | 0.98x | WEAK 14/100 | EXTREME 86/100 | Do nothing |
| 8 | BLUR/USD | 0.00667 | 28.25 | +0.15% | 1.17x | WEAK 29/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.09851 | 66.73 | +0.35% | 1.23x | 4811 | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
