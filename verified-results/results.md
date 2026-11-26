# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T13:41:22.429811+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45831288283
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e50896614a99e679f915fa3ee47a42595d8486f8 (atomic ledger/results publication)
**Ledger generation:** 1868 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 43.61 | 83.604 | 68.604 | +2.11% | +0.00% | 6.22x | 2.3 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LINK/USD | 9.23502 | 82.951 | 68.130 | +2.11% | -0.04% | 3.09x | 2.8 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.95003 | 80.410 | 65.015 | +1.44% | +0.08% | 3.25x | 0.1 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | INJ/USD | 6.172 | 73.160 | 67.416 | +3.66% | +0.08% | 1.53x | 3.2 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1701.28 | 70.870 | 59.472 | +0.64% | -0.20% | 2.24x | 0.1 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | QNT/USD | 151.11 | 70.866 | 74.972 | +4.36% | +0.59% | 0.29x | 6.6 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03619 | 68.097 | 73.949 | +8.65% | +0.19% | 0.32x | 8.3 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | ZRO/USD | 1.107 | 67.459 | 75.942 | +8.11% | -0.54% | 0.42x | 18.0 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | BABY/USD | 0.00916 | 65.828 | 62.098 | +5.17% | -0.22% | 1.48x | 10.9 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | ADA/USD | 0.148805 | 64.298 | 68.297 | +2.08% | -0.06% | 0.63x | 2.6 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 60773.8 | 56.261 | 59.690 | +0.67% | -0.01% | 0.66x | 0.0 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | FET/USD | 0.115 | 54.446 | 66.705 | +5.99% | -0.69% | 0.12x | 17.4 | 2026-11-26T13:41:13.985952+00:00 | Not calibrated | WEAK 27/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 75.942 | 1.107 | -0.54% | 0.42x |
| 2 | QNT/USD | 74.972 | 151.11 | +0.59% | 0.29x |
| 3 | SEI/USD | 73.949 | 0.03619 | +0.19% | 0.32x |
| 4 | LTC/USD | 68.604 | 43.61 | +0.00% | 6.22x |
| 5 | ADA/USD | 68.297 | 0.148805 | -0.06% | 0.63x |
| 6 | LINK/USD | 68.130 | 9.23502 | -0.04% | 3.09x |
| 7 | INJ/USD | 67.416 | 6.172 | +0.08% | 1.53x |
| 8 | FET/USD | 66.705 | 0.115 | -0.69% | 0.12x |
| 9 | XRP/USD | 65.015 | 0.95003 | +0.08% | 3.25x |
| 10 | BABY/USD | 62.098 | 0.00916 | -0.22% | 1.48x |
| 11 | XBT/USD | 59.690 | 60773.8 | -0.01% | 0.66x |
| 12 | ETH/USD | 59.472 | 1701.28 | -0.20% | 2.24x |

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

- Persisted scans: 1868; predictions: 16151; observations: 1132065.
- Matured sampled outcomes across 1/6/24/48h: 34934; gap abstentions: 24852. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45831288283 · **Generation:** 1868 · **Legacy run:** 45831288283
**Main quote time:** 2026-11-26T13:41:22.429811+00:00 · **Legacy report time:** 2026-11-26T13:42:38.273296+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 43.61 | 83.60 | +0.00% | 6.22x | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD | 9.23502 | 82.95 | -0.04% | 3.09x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD ⭐ | 0.95003 | 80.41 | +0.08% | 3.25x | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | INJ/USD ⭐ | 6.172 | 73.16 | +0.08% | 1.53x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1701.28 | 70.87 | -0.20% | 2.24x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | QNT/USD | 151.11 | 70.87 | +0.59% | 0.29x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 7 | SEI/USD | 0.03619 | 68.10 | +0.19% | 0.32x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 8 | ZRO/USD | 1.107 | 67.46 | -0.54% | 0.42x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | BABY/USD | 0.00916 | 65.83 | -0.22% | 1.48x | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |
| 10 | ADA/USD | 0.148805 | 64.30 | -0.06% | 0.63x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 60773.8 | 56.26 | -0.01% | 0.66x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | FET/USD | 0.115 | 54.45 | -0.69% | 0.12x | WEAK 27/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.173 | 81.84 | +0.08% | 1.53x | 7258 | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | USELESS/USD | 0.07472 | 78.76 | +0.90% | 2.64x | 3680 | STRONG 84/100 | HIGH 67/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95053 | 77.93 | +0.08% | 3.25x | 36982 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
