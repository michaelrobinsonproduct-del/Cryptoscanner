# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T04:16:10.013996+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45753951812
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cf009d1fcb47924459913410181971bf745aa99b (atomic ledger/results publication)
**Ledger generation:** 1811 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.96 | 89.460 | 72.467 | +2.50% | +0.40% | 2.81x | 0.1 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XBT/USD | 60886.1 | 77.868 | 60.992 | +0.86% | +0.38% | 4.46x | 0.0 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 183.943 | 77.099 | 61.447 | +1.29% | +0.13% | 4.56x | 5.2 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0568405 | 76.315 | 61.370 | +1.58% | -0.01% | 6.15x | 0.2 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LTC/USD | 43.92 | 76.228 | 73.693 | +2.83% | +0.39% | 1.06x | 2.3 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LINK/USD | 9.2102 | 75.510 | 64.633 | +1.83% | +0.09% | 2.04x | 2.2 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07185 | 74.233 | 68.046 | +8.42% | +0.91% | 1.16x | 18.2 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6727 | 71.995 | 60.980 | +0.96% | +0.01% | 2.09x | 1.5 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ADA/USD | 0.148741 | 68.924 | 67.922 | +2.04% | +0.10% | 1.05x | 2.7 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 71.11 | 63.546 | 61.457 | +1.02% | +0.32% | 1.05x | 1.4 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128842 | 60.695 | 48.799 | +0.80% | +0.29% | 2.05x | 3.0 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 12 | HYPE/USD | 61.9 | 58.563 | 56.564 | +0.45% | +0.24% | 1.08x | 3.2 | 2026-11-26T04:16:03.321771+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 73.693 | 43.92 | +0.39% | 1.06x |
| 2 | XRP/USD | 72.467 | 0.96 | +0.40% | 2.81x |
| 3 | SYRUP/USD | 68.046 | 0.07185 | +0.91% | 1.16x |
| 4 | ADA/USD | 67.922 | 0.148741 | +0.10% | 1.05x |
| 5 | LINK/USD | 64.633 | 9.2102 | +0.09% | 2.04x |
| 6 | SOL/USD | 61.457 | 71.11 | +0.32% | 1.05x |
| 7 | TAO/USD | 61.447 | 183.943 | +0.13% | 4.56x |
| 8 | XDG/USD | 61.370 | 0.0568405 | -0.01% | 6.15x |
| 9 | XBT/USD | 60.992 | 60886.1 | +0.38% | 4.46x |
| 10 | SUI/USD | 60.980 | 0.6727 | +0.01% | 2.09x |
| 11 | HYPE/USD | 56.564 | 61.9 | +0.24% | 1.08x |
| 12 | XLM/USD | 48.799 | 0.128842 | +0.29% | 2.05x |

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

- Persisted scans: 1811; predictions: 15467; observations: 1097943.
- Matured sampled outcomes across 1/6/24/48h: 33563; gap abstentions: 23837. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45753951812 · **Generation:** 1811 · **Legacy run:** 45753951812
**Main quote time:** 2026-11-26T04:16:10.013996+00:00 · **Legacy report time:** 2026-11-26T04:17:27.858972+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96 | 89.46 | +0.40% | 2.81x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 60886.1 | 77.87 | +0.38% | 4.46x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD | 183.943 | 77.10 | +0.13% | 4.56x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | XDG/USD | 0.0568405 | 76.31 | -0.01% | 6.15x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | LTC/USD ⭐ | 43.92 | 76.23 | +0.39% | 1.06x | STRONG 83/100 | HIGH 62/100 | Watch |
| 6 | LINK/USD ⭐ | 9.2102 | 75.51 | +0.09% | 2.04x | STRONG 93/100 | HIGH 55/100 | Watch |
| 7 | SYRUP/USD ⭐ | 0.07185 | 74.23 | +0.91% | 1.16x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 8 | SUI/USD | 0.6727 | 72.00 | +0.01% | 2.09x | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | ADA/USD ⭐ | 0.148741 | 68.92 | +0.10% | 1.05x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD ⭐ | 71.11 | 63.55 | +0.32% | 1.05x | STRONG 77/100 | HIGH 62/100 | Watch |
| 11 | XLM/USD | 0.128842 | 60.70 | +0.29% | 2.05x | STRONG 85/100 | HIGH 55/100 | Watch |
| 12 | HYPE/USD | 61.9 | 58.56 | +0.24% | 1.08x | MODERATE 64/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95982 | 86.49 | +0.40% | 2.81x | 42246 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BABY/USD | 0.00949 | 83.80 | +1.74% | 3.70x | 2807 | STRONG 87/100 | VERY_HIGH 79/100 | Watch |
| 3 | LTC/USD ⭐ | 43.92 | 78.29 | +0.39% | 1.06x | 14904 | STRONG 84/100 | HIGH 62/100 | Watch |
| 4 | SYRUP/USD ⭐ | 0.0718 | 74.66 | +0.91% | 1.16x | 3565 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 5 | LINK/USD ⭐ | 9.21458 | 72.58 | +0.09% | 2.04x | 9025 | STRONG 91/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD ⭐ | 0.148743 | 71.47 | +0.10% | 1.05x | 11430 | STRONG 71/100 | HIGH 62/100 | Watch |
| 7 | XBT/USD ⭐ | 60879.4 | 71.25 | +0.38% | 4.46x | 230203 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 71.12 | 62.79 | +0.32% | 1.05x | 47102 | STRONG 76/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD, XBT/USD, LTC/USD, LINK/USD, SYRUP/USD, ADA/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
