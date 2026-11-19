# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:15:21.392690+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44575032520
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 13de5ac6d994475086d6a011df0fa473c037b10e (atomic ledger/results publication)
**Ledger generation:** 822 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.32 | 86.332 | 72.383 | +2.99% | -0.21% | 3.06x | 7.2 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.05496 | 67.139 | 68.999 | +11.71% | -0.45% | 1.04x | 14.5 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |
| 3 | SKR/USD | 0.010168 | 66.514 | 66.007 | +5.55% | -1.24% | 1.67x | 7.9 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 4 | PYTH/USD | 0.05513 | 61.273 | 55.447 | +4.49% | -0.92% | 2.04x | 16.3 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002636 | 59.439 | 49.323 | +1.54% | -0.98% | 3.69x | 7.6 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SENT/USD | 0.021574 | 59.331 | 63.386 | +4.70% | -1.39% | 1.29x | 7.9 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 7 | HYPE/USD | 67.12 | 57.406 | 56.767 | +0.36% | -0.70% | 1.41x | 1.5 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ALEO/USD | 0.031 | 53.067 | 54.957 | +3.40% | +0.52% | 0.55x | 3.2 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | DRV/USD | 0.26787 | 43.823 | 40.736 | +1.20% | -0.86% | 1.74x | 0.4 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |
| 10 | INJ/USD | 7.031 | 41.800 | 45.450 | +0.72% | -0.52% | 0.90x | 5.7 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | PEPE/USD | 3.762e-06 | 40.966 | 39.720 | +0.43% | -0.74% | 1.49x | 8.0 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | WEAK 40/100 | HIGH 61/100 | Watch | WATCH |
| 12 | MEGA/USD | 0.05724 | 32.577 | 39.646 | +2.21% | +0.09% | 0.25x | 15.7 | 2026-11-19T17:15:14.952668+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.383 | 22.32 | -0.21% | 3.06x |
| 2 | TRUST/USD | 68.999 | 0.05496 | -0.45% | 1.04x |
| 3 | SKR/USD | 66.007 | 0.010168 | -1.24% | 1.67x |
| 4 | SENT/USD | 63.386 | 0.021574 | -1.39% | 1.29x |
| 5 | HYPE/USD | 56.767 | 67.12 | -0.70% | 1.41x |
| 6 | PYTH/USD | 55.447 | 0.05513 | -0.92% | 2.04x |
| 7 | ALEO/USD | 54.957 | 0.031 | +0.52% | 0.55x |
| 8 | PUMP/USD | 49.323 | 0.002636 | -0.98% | 3.69x |
| 9 | INJ/USD | 45.450 | 7.031 | -0.52% | 0.90x |
| 10 | DRV/USD | 40.736 | 0.26787 | -0.86% | 1.74x |
| 11 | PEPE/USD | 39.720 | 3.762e-06 | -0.74% | 1.49x |
| 12 | MEGA/USD | 39.646 | 0.05724 | +0.09% | 0.25x |

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

- Persisted scans: 822; predictions: 7008; observations: 496967.
- Matured sampled outcomes across 1/6/24/48h: 6971; gap abstentions: 15424. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44575032520 · **Generation:** 822 · **Legacy run:** 44575032520
**Main quote time:** 2026-11-19T17:15:21.392690+00:00 · **Legacy report time:** 2026-11-19T17:16:17.097225+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.32 | 86.33 | -0.21% | 3.06x | STRONG 73/100 | HIGH 61/100 | Watch |
| 2 | TRUST/USD | 0.05496 | 67.14 | -0.45% | 1.04x | WEAK 39/100 | EXTREME 86/100 | Do nothing |
| 3 | SKR/USD | 0.010168 | 66.51 | -1.24% | 1.67x | MODERATE 53/100 | VERY_HIGH 77/100 | Do nothing |
| 4 | PYTH/USD | 0.05513 | 61.27 | -0.92% | 2.04x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 5 | PUMP/USD | 0.002636 | 59.44 | -0.98% | 3.69x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | SENT/USD | 0.021574 | 59.33 | -1.39% | 1.29x | WEAK 40/100 | VERY_HIGH 70/100 | Do nothing |
| 7 | HYPE/USD | 67.12 | 57.41 | -0.70% | 1.41x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 8 | ALEO/USD | 0.031 | 53.07 | +0.52% | 0.55x | MODERATE 57/100 | VERY_HIGH 75/100 | Watch |
| 9 | DRV/USD | 0.26787 | 43.82 | -0.86% | 1.74x | WEAK 42/100 | HIGH 66/100 | Watch |
| 10 | INJ/USD | 7.031 | 41.80 | -0.52% | 0.90x | WEAK 26/100 | HIGH 68/100 | Do nothing |
| 11 | PEPE/USD | 3.762e-06 | 40.97 | -0.74% | 1.49x | WEAK 40/100 | HIGH 61/100 | Watch |
| 12 | MEGA/USD | 0.05724 | 32.58 | +0.09% | 0.25x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CSPR/USD | 0.00178 | 80.88 | +3.95% | 1.51x | 3796 | STRONG 75/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
