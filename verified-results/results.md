# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T08:42:42.679789+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45358049299
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1c5c636b57087ab64858cd7c814f282584470700 (atomic ledger/results publication)
**Ledger generation:** 1551 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 497.17 | 80.875 | 65.633 | +2.29% | +0.05% | 8.73x | 10.9 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.514e-06 | 76.754 | 67.803 | +2.69% | -1.21% | 9.46x | 2.8 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | VVV/USD | 25.197 | 69.595 | 72.677 | +3.06% | -0.16% | 0.77x | 7.5 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | BAT/USD | 0.07977 | 68.817 | 53.440 | +3.37% | +0.08% | 8.39x | 5.0 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9983 | 66.888 | 57.180 | +0.57% | -0.32% | 2.13x | 3.7 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.584e-05 | 65.700 | 60.389 | +5.45% | +0.70% | 1.18x | 19.6 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94209 | 58.730 | 56.640 | +0.29% | -0.46% | 1.44x | 0.7 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ICNT/USD | 0.3257 | 57.278 | 56.273 | +5.37% | +1.88% | 0.16x | 27.6 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | LINK/USD | 9.06939 | 56.946 | 57.778 | +0.72% | -0.10% | 0.97x | 4.5 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | LTC/USD | 41.53 | 53.029 | 55.655 | +0.27% | -0.12% | 0.80x | 2.4 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | DOT/USD | 0.678 | 48.908 | 35.380 | +0.37% | -0.29% | 5.69x | 2.9 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 12 | NIGHT/USD | 0.04845 | 47.957 | 49.163 | +0.62% | +0.00% | 0.88x | 8.3 | 2026-11-24T08:42:34.780566+00:00 | Not calibrated | WEAK 44/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.677 | 25.197 | -0.16% | 0.77x |
| 2 | PEPE/USD | 67.803 | 3.514e-06 | -1.21% | 9.46x |
| 3 | XMR/USD | 65.633 | 497.17 | +0.05% | 8.73x |
| 4 | LUNA/USD | 60.389 | 4.584e-05 | +0.70% | 1.18x |
| 5 | LINK/USD | 57.778 | 9.06939 | -0.10% | 0.97x |
| 6 | NEAR/USD | 57.180 | 2.9983 | -0.32% | 2.13x |
| 7 | XRP/USD | 56.640 | 0.94209 | -0.46% | 1.44x |
| 8 | ICNT/USD | 56.273 | 0.3257 | +1.88% | 0.16x |
| 9 | LTC/USD | 55.655 | 41.53 | -0.12% | 0.80x |
| 10 | BAT/USD | 53.440 | 0.07977 | +0.08% | 8.39x |
| 11 | NIGHT/USD | 49.163 | 0.04845 | +0.00% | 0.88x |
| 12 | DOT/USD | 35.380 | 0.678 | -0.29% | 5.69x |

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

- Persisted scans: 1551; predictions: 13344; observations: 939657.
- Matured sampled outcomes across 1/6/24/48h: 25261; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 141 (sampled only; not a success-rate estimate).
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

**Writer:** 45358049299 · **Generation:** 1551 · **Legacy run:** 45358049299
**Main quote time:** 2026-11-24T08:42:42.679789+00:00 · **Legacy report time:** 2026-11-24T08:43:55.413629+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 497.17 | 80.87 | +0.05% | 8.73x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | PEPE/USD | 3.514e-06 | 76.75 | -1.21% | 9.46x | MODERATE 68/100 | HIGH 65/100 | Do nothing |
| 3 | VVV/USD | 25.197 | 69.59 | -0.16% | 0.77x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | BAT/USD ⭐ | 0.07977 | 68.82 | +0.08% | 8.39x | STRONG 89/100 | HIGH 60/100 | Watch |
| 5 | NEAR/USD | 2.9983 | 66.89 | -0.32% | 2.13x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 6 | LUNA/USD ⭐ | 4.584e-05 | 65.70 | +0.70% | 1.18x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 7 | XRP/USD | 0.94209 | 58.73 | -0.46% | 1.44x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 8 | ICNT/USD | 0.3257 | 57.28 | +1.88% | 0.16x | MODERATE 49/100 | EXTREME 87/100 | Do nothing |
| 9 | LINK/USD | 9.06939 | 56.95 | -0.10% | 0.97x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 10 | LTC/USD | 41.53 | 53.03 | -0.12% | 0.80x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 11 | DOT/USD | 0.678 | 48.91 | -0.29% | 5.69x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 12 | NIGHT/USD | 0.04845 | 47.96 | +0.00% | 0.88x | WEAK 44/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BAT/USD ⭐ | 0.07997 | 80.17 | +0.08% | 8.39x | 3605 | STRONG 95/100 | HIGH 60/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.591e-05 | 67.59 | +0.70% | 1.18x | 1864 | STRONG 74/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** BAT/USD, LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
