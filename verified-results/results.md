# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T21:20:48.543882+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44617610921
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 2b3a67ca063f8507358a6ba3463b737f5c011efb (atomic ledger/results publication)
**Ledger generation:** 861 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.996 | 75.295 | 61.406 | +1.50% | -0.22% | 2.68x | 8.2 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5414 | 67.346 | 54.645 | +4.52% | -0.46% | 3.84x | 18.5 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | BMT/USD | 0.01999 | 62.796 | 67.519 | +5.88% | -0.74% | 0.90x | 10.0 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | WEAK 31/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | ALEO/USD | 0.03096 | 59.889 | 59.760 | +3.27% | -0.61% | 1.32x | 3.2 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05914 | 56.351 | 63.802 | +5.61% | -0.52% | 0.52x | 15.2 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | PUMP/USD | 0.00261 | 54.160 | 40.688 | +0.54% | -0.31% | 3.40x | 11.5 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010019 | 53.261 | 48.692 | +4.01% | -0.32% | 1.62x | 21.0 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | WEAK 37/100 | EXTREME 85/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021299 | 49.656 | 54.651 | +3.37% | +0.49% | 0.26x | 6.6 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.09808 | 43.179 | 43.129 | +2.64% | -0.36% | 1.18x | 27.7 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 10 | SYRUP/USD | 0.09674 | 33.786 | 29.567 | +1.87% | +0.95% | 0.95x | 30.0 | 2026-11-19T21:20:42.183480+00:00 | Not calibrated | WEAK 37/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BMT/USD | 67.519 | 0.01999 | -0.74% | 0.90x |
| 2 | MEGA/USD | 63.802 | 0.05914 | -0.52% | 0.52x |
| 3 | VVV/USD | 61.406 | 21.996 | -0.22% | 2.68x |
| 4 | ALEO/USD | 59.760 | 0.03096 | -0.61% | 1.32x |
| 5 | SENT/USD | 54.651 | 0.021299 | +0.49% | 0.26x |
| 6 | AKT/USD | 54.645 | 0.5414 | -0.46% | 3.84x |
| 7 | SKR/USD | 48.692 | 0.010019 | -0.32% | 1.62x |
| 8 | USELESS/USD | 43.129 | 0.09808 | -0.36% | 1.18x |
| 9 | PUMP/USD | 40.688 | 0.00261 | -0.31% | 3.40x |
| 10 | SYRUP/USD | 29.567 | 0.09674 | +0.95% | 0.95x |

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

- Persisted scans: 861; predictions: 7468; observations: 520328.
- Matured sampled outcomes across 1/6/24/48h: 7703; gap abstentions: 15688. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44617610921 · **Generation:** 861 · **Legacy run:** 44617610921
**Main quote time:** 2026-11-19T21:20:48.543882+00:00 · **Legacy report time:** 2026-11-19T21:21:39.639852+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.996 | 75.30 | -0.22% | 2.68x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | AKT/USD | 0.5414 | 67.35 | -0.46% | 3.84x | MODERATE 59/100 | VERY_HIGH 72/100 | Watch |
| 3 | BMT/USD | 0.01999 | 62.80 | -0.74% | 0.90x | WEAK 31/100 | EXTREME 86/100 | Do nothing |
| 4 | ALEO/USD | 0.03096 | 59.89 | -0.61% | 1.32x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 5 | MEGA/USD | 0.05914 | 56.35 | -0.52% | 0.52x | WEAK 28/100 | EXTREME 87/100 | Do nothing |
| 6 | PUMP/USD | 0.00261 | 54.16 | -0.31% | 3.40x | MODERATE 52/100 | HIGH 67/100 | Watch |
| 7 | SKR/USD | 0.010019 | 53.26 | -0.32% | 1.62x | WEAK 37/100 | EXTREME 85/100 | Do nothing |
| 8 | SENT/USD | 0.021299 | 49.66 | +0.49% | 0.26x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 9 | USELESS/USD | 0.09808 | 43.18 | -0.36% | 1.18x | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing |
| 10 | SYRUP/USD | 0.09674 | 33.79 | +0.95% | 0.95x | WEAK 37/100 | EXTREME 86/100 | Do nothing |

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
