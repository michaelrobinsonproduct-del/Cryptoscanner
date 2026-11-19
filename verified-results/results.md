# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:35:30.415199+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44629912335
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** bfe42bfbcb92e165e584a5bd10786a0d27da3f62 (atomic ledger/results publication)
**Ledger generation:** 871 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | USELESS/USD | 0.10003 | 80.885 | 64.292 | +4.68% | +1.78% | 1.77x | 17.0 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | MEGA/USD | 0.06058 | 77.164 | 69.778 | +8.18% | +1.22% | 1.13x | 14.9 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 21.995 | 65.162 | 62.965 | +1.50% | +0.61% | 0.91x | 5.0 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ADA/USD | 0.151996 | 64.967 | 56.723 | +0.49% | +0.67% | 1.49x | 3.4 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5376 | 60.809 | 52.331 | +3.78% | +0.52% | 1.59x | 13.0 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | STRONG 70/100 | HIGH 66/100 | Watch | WATCH |
| 6 | TRX/USD | 0.310341 | 59.842 | 43.924 | +0.34% | +0.18% | 4.19x | 1.4 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010037 | 59.673 | 55.032 | +4.19% | +0.56% | 1.18x | 10.9 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | SENT/USD | 0.021499 | 58.742 | 61.776 | +4.34% | +0.90% | 0.25x | 6.0 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | HYPE/USD | 67.07 | 58.732 | 55.497 | +0.28% | +0.42% | 1.11x | 3.0 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 10 | INJ/USD | 7.09 | 56.881 | 54.367 | +1.56% | +1.41% | 0.55x | 4.2 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PYTH/USD | 0.05322 | 30.667 | 33.711 | +0.87% | +0.82% | 0.29x | 11.3 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | TIA/USD | 0.3456 | 28.032 | 29.146 | +0.29% | +1.05% | 0.36x | 8.7 | 2026-11-19T22:35:24.220326+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 69.778 | 0.06058 | +1.22% | 1.13x |
| 2 | USELESS/USD | 64.292 | 0.10003 | +1.78% | 1.77x |
| 3 | VVV/USD | 62.965 | 21.995 | +0.61% | 0.91x |
| 4 | SENT/USD | 61.776 | 0.021499 | +0.90% | 0.25x |
| 5 | ADA/USD | 56.723 | 0.151996 | +0.67% | 1.49x |
| 6 | HYPE/USD | 55.497 | 67.07 | +0.42% | 1.11x |
| 7 | SKR/USD | 55.032 | 0.010037 | +0.56% | 1.18x |
| 8 | INJ/USD | 54.367 | 7.09 | +1.41% | 0.55x |
| 9 | AKT/USD | 52.331 | 0.5376 | +0.52% | 1.59x |
| 10 | TRX/USD | 43.924 | 0.310341 | +0.18% | 4.19x |
| 11 | PYTH/USD | 33.711 | 0.05322 | +0.82% | 0.29x |
| 12 | TIA/USD | 29.146 | 0.3456 | +1.05% | 0.36x |

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

- Persisted scans: 871; predictions: 7573; observations: 526344.
- Matured sampled outcomes across 1/6/24/48h: 7998; gap abstentions: 15750. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44629912335 · **Generation:** 871 · **Legacy run:** 44629912335
**Main quote time:** 2026-11-19T22:35:30.415199+00:00 · **Legacy report time:** 2026-11-19T22:36:16.818367+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.10003 | 80.88 | +1.78% | 1.77x | STRONG 90/100 | HIGH 61/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.06058 | 77.16 | +1.22% | 1.13x | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 21.995 | 65.16 | +0.61% | 0.91x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD | 0.151996 | 64.97 | +0.67% | 1.49x | STRONG 77/100 | HIGH 55/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5376 | 60.81 | +0.52% | 1.59x | STRONG 80/100 | HIGH 66/100 | Consider small entry |
| 6 | TRX/USD | 0.310341 | 59.84 | +0.18% | 4.19x | STRONG 75/100 | HIGH 55/100 | Watch |
| 7 | SKR/USD ⭐ | 0.010037 | 59.67 | +0.56% | 1.18x | STRONG 70/100 | VERY_HIGH 80/100 | Watch |
| 8 | SENT/USD | 0.021499 | 58.74 | +0.90% | 0.25x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 9 | HYPE/USD | 67.07 | 58.73 | +0.42% | 1.11x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 10 | INJ/USD | 7.09 | 56.88 | +1.41% | 0.55x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | PYTH/USD | 0.05322 | 30.67 | +0.82% | 0.29x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 12 | TIA/USD | 0.3456 | 28.03 | +1.05% | 0.36x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.877e-05 | 87.82 | +1.79% | 5.47x | 6805 | STRONG 84/100 | VERY_HIGH 77/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.10017 | 84.48 | +1.78% | 1.77x | 5201 | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.5387 | 75.28 | +0.52% | 1.59x | 3490 | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 4 | MEGA/USD ⭐ | 0.06058 | 71.48 | +1.22% | 1.13x | 2157 | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 5 | SKR/USD ⭐ | 0.010037 | 62.64 | +0.56% | 1.18x | 1385 | STRONG 76/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** USELESS/USD, MEGA/USD, AKT/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
