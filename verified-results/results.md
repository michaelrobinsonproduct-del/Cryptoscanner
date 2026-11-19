# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T21:15:32.163967+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44616776401
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** a968c87eca7bbe5153de45e67a09374d0e42dd1d (atomic ledger/results publication)
**Ledger generation:** 860 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALEO/USD | 0.03104 | 85.240 | 59.882 | +3.54% | +2.07% | 2.84x | 6.5 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.5452 | 81.034 | 67.222 | +5.25% | -0.24% | 2.88x | 3.7 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | STRONG 71/100 | HIGH 66/100 | Watch | WATCH |
| 3 | VVV/USD | 22.091 | 71.179 | 65.170 | +1.94% | -0.33% | 1.77x | 6.8 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002612 | 57.030 | 45.074 | +0.62% | -0.61% | 2.70x | 3.8 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.09869 | 56.736 | 52.313 | +3.28% | -0.01% | 1.45x | 18.3 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.0973 | 56.055 | 32.217 | +2.46% | +1.77% | 9.58x | 33.0 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.05926 | 55.797 | 62.781 | +5.82% | -0.27% | 0.44x | 20.3 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | WEAK 23/100 | EXTREME 93/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021314 | 51.992 | 54.927 | +3.44% | +0.92% | 0.25x | 7.0 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | CSPR/USD | 0.0017157 | 51.614 | 58.791 | +5.06% | -1.70% | 1.13x | 17.0 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 10 | SKR/USD | 0.010044 | 47.903 | 49.529 | +4.27% | -0.70% | 1.19x | 22.9 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | WEAK 24/100 | EXTREME 92/100 | Do nothing | WATCH |
| 11 | HYPE/USD | 67.28 | 47.833 | 57.700 | +0.60% | -0.62% | 0.32x | 3.0 | 2026-11-19T21:15:27.194564+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 67.222 | 0.5452 | -0.24% | 2.88x |
| 2 | VVV/USD | 65.170 | 22.091 | -0.33% | 1.77x |
| 3 | MEGA/USD | 62.781 | 0.05926 | -0.27% | 0.44x |
| 4 | ALEO/USD | 59.882 | 0.03104 | +2.07% | 2.84x |
| 5 | CSPR/USD | 58.791 | 0.0017157 | -1.70% | 1.13x |
| 6 | HYPE/USD | 57.700 | 67.28 | -0.62% | 0.32x |
| 7 | SENT/USD | 54.927 | 0.021314 | +0.92% | 0.25x |
| 8 | USELESS/USD | 52.313 | 0.09869 | -0.01% | 1.45x |
| 9 | SKR/USD | 49.529 | 0.010044 | -0.70% | 1.19x |
| 10 | PUMP/USD | 45.074 | 0.002612 | -0.61% | 2.70x |
| 11 | SYRUP/USD | 32.217 | 0.0973 | +1.77% | 9.58x |

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

- Persisted scans: 860; predictions: 7458; observations: 519727.
- Matured sampled outcomes across 1/6/24/48h: 7679; gap abstentions: 15685. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44616776401 · **Generation:** 860 · **Legacy run:** 44616776401
**Main quote time:** 2026-11-19T21:15:32.163967+00:00 · **Legacy report time:** 2026-11-19T21:16:16.920107+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALEO/USD ⭐ | 0.03104 | 85.24 | +2.07% | 2.84x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD | 0.5452 | 81.03 | -0.24% | 2.88x | STRONG 71/100 | HIGH 66/100 | Watch |
| 3 | VVV/USD | 22.091 | 71.18 | -0.33% | 1.77x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 4 | PUMP/USD | 0.002612 | 57.03 | -0.61% | 2.70x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 5 | USELESS/USD | 0.09869 | 56.74 | -0.01% | 1.45x | WEAK 43/100 | HIGH 67/100 | Watch |
| 6 | SYRUP/USD | 0.0973 | 56.06 | +1.77% | 9.58x | STRONG 73/100 | VERY_HIGH 79/100 | Watch |
| 7 | MEGA/USD | 0.05926 | 55.80 | -0.27% | 0.44x | WEAK 23/100 | EXTREME 93/100 | Do nothing |
| 8 | SENT/USD | 0.021314 | 51.99 | +0.92% | 0.25x | MODERATE 56/100 | VERY_HIGH 75/100 | Watch |
| 9 | CSPR/USD | 0.0017157 | 51.61 | -1.70% | 1.13x | WEAK 31/100 | VERY_HIGH 83/100 | Do nothing |
| 10 | SKR/USD | 0.010044 | 47.90 | -0.70% | 1.19x | WEAK 24/100 | EXTREME 92/100 | Do nothing |
| 11 | HYPE/USD | 67.28 | 47.83 | -0.62% | 0.32x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALEO/USD ⭐ | 0.03104 | 83.02 | +2.07% | 2.84x | 10589 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** ALEO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
