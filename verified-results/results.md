# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T14:32:22.944130+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45839543587
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 01aeb8361a947defa628f91ad2f8af072b4fb15c (atomic ledger/results publication)
**Ledger generation:** 1873 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 589; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WIF/USD | 0.1349 | 84.683 | 69.321 | +5.97% | +0.22% | 2.42x | 7.4 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | STRONG 97/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | FET/USD | 0.1157 | 84.582 | 70.014 | +6.64% | -0.09% | 124.77x | 17.3 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | LINK/USD | 9.25489 | 83.289 | 68.964 | +2.33% | -0.14% | 3.02x | 2.8 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | QNT/USD | 150.44 | 82.071 | 70.970 | +3.90% | -0.68% | 2.45x | 5.3 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.149039 | 81.665 | 67.513 | +2.24% | -0.17% | 3.06x | 6.4 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HBAR/USD | 0.0542 | 77.515 | 63.888 | +4.03% | +0.09% | 2.32x | 1.8 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07094 | 74.912 | 67.302 | +7.05% | -0.32% | 1.92x | 19.8 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | XBT/USD | 60810.3 | 74.251 | 60.114 | +0.73% | -0.17% | 3.19x | 0.0 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 9 | 2Z/USD | 0.0177 | 72.708 | 73.398 | +7.14% | +0.51% | 0.67x | 5.6 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | ZRO/USD | 1.107 | 71.921 | 75.523 | +8.11% | -0.09% | 0.68x | 18.1 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | SOL/USD | 71.32 | 68.895 | 63.548 | +1.32% | -0.18% | 1.63x | 1.4 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 12 | LTC/USD | 43.87 | 66.311 | 71.735 | +2.72% | -0.09% | 0.50x | 4.6 | 2026-11-26T14:32:15.069344+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 75.523 | 1.107 | -0.09% | 0.68x |
| 2 | 2Z/USD | 73.398 | 0.0177 | +0.51% | 0.67x |
| 3 | LTC/USD | 71.735 | 43.87 | -0.09% | 0.50x |
| 4 | QNT/USD | 70.970 | 150.44 | -0.68% | 2.45x |
| 5 | FET/USD | 70.014 | 0.1157 | -0.09% | 124.77x |
| 6 | WIF/USD | 69.321 | 0.1349 | +0.22% | 2.42x |
| 7 | LINK/USD | 68.964 | 9.25489 | -0.14% | 3.02x |
| 8 | ADA/USD | 67.513 | 0.149039 | -0.17% | 3.06x |
| 9 | SYRUP/USD | 67.302 | 0.07094 | -0.32% | 1.92x |
| 10 | HBAR/USD | 63.888 | 0.0542 | +0.09% | 2.32x |
| 11 | SOL/USD | 63.548 | 71.32 | -0.18% | 1.63x |
| 12 | XBT/USD | 60.114 | 60810.3 | -0.17% | 3.19x |

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

- Persisted scans: 1873; predictions: 16211; observations: 1135010.
- Matured sampled outcomes across 1/6/24/48h: 35066; gap abstentions: 24914. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45839543587 · **Generation:** 1873 · **Legacy run:** 45839543587
**Main quote time:** 2026-11-26T14:32:22.944130+00:00 · **Legacy report time:** 2026-11-26T14:33:22.116046+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WIF/USD | 0.1349 | 84.68 | +0.22% | 2.42x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 2 | FET/USD | 0.1157 | 84.58 | -0.09% | 124.77x | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 3 | LINK/USD | 9.25489 | 83.29 | -0.14% | 3.02x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | QNT/USD | 150.44 | 82.07 | -0.68% | 2.45x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD | 0.149039 | 81.67 | -0.17% | 3.06x | STRONG 71/100 | HIGH 61/100 | Watch |
| 6 | HBAR/USD ⭐ | 0.0542 | 77.51 | +0.09% | 2.32x | STRONG 94/100 | HIGH 60/100 | Watch |
| 7 | SYRUP/USD | 0.07094 | 74.91 | -0.32% | 1.92x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 8 | XBT/USD | 60810.3 | 74.25 | -0.17% | 3.19x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 9 | 2Z/USD | 0.0177 | 72.71 | +0.51% | 0.67x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 10 | ZRO/USD | 1.107 | 71.92 | -0.09% | 0.68x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 11 | SOL/USD | 71.32 | 68.89 | -0.18% | 1.63x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 12 | LTC/USD | 43.87 | 66.31 | -0.09% | 0.50x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05422 | 87.13 | +0.09% | 2.32x | 5715 | STRONG 99/100 | HIGH 60/100 | Watch |
| 2 | PIEVERSE/USD | 4.0544 | 84.13 | +0.78% | 2.26x | 3602 | STRONG 87/100 | HIGH 67/100 | Consider small entry |
| 3 | SKY/USD | 0.04774 | 77.76 | +0.86% | 1.56x | 5970 | STRONG 79/100 | HIGH 66/100 | Consider small entry |
| 4 | ZBCN/USD | 0.001747 | 75.29 | +0.34% | 2.16x | 2478 | STRONG 78/100 | EXTREME 89/100 | Do nothing |
| 5 | XDG/USD | 0.0571268 | 72.35 | +0.07% | 1.13x | 7076 | MODERATE 61/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
