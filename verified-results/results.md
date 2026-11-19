# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T21:40:35.142057+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44620976609
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 6414b84d8e8da7179bad3b23359601874d3b494b (atomic ledger/results publication)
**Ledger generation:** 863 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.931 | 70.091 | 61.346 | +1.20% | -0.29% | 2.02x | 4.1 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05969 | 67.832 | 68.818 | +6.59% | +0.62% | 0.59x | 16.8 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | BMT/USD | 0.02003 | 63.621 | 69.014 | +6.09% | +0.25% | 0.34x | 10.0 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | ALEO/USD | 0.03105 | 55.493 | 62.259 | +3.57% | -0.22% | 0.44x | 3.2 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | LUNA/USD | 4.763e-05 | 55.296 | 67.921 | +9.39% | -1.34% | 0.41x | 29.5 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 23/100 | EXTREME 92/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5355 | 51.770 | 47.552 | +3.38% | -0.37% | 1.61x | 16.8 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | SKR/USD | 0.009972 | 45.860 | 50.737 | +3.52% | -0.54% | 0.78x | 10.0 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 23/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021093 | 45.711 | 47.114 | +2.37% | -0.96% | 1.34x | 7.6 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 43/100 | HIGH 66/100 | Watch | WATCH |
| 9 | CSPR/USD | 0.0017096 | 41.937 | 47.337 | +4.68% | -0.84% | 0.88x | 34.7 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 16/100 | EXTREME 85/100 | Do nothing | WATCH |
| 10 | USELESS/USD | 0.09755 | 38.415 | 39.522 | +2.08% | -0.23% | 1.00x | 27.8 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | SYRUP/USD | 0.09603 | 20.717 | 32.577 | +1.13% | -0.94% | 0.28x | 13.6 | 2026-11-19T21:40:27.463714+00:00 | Not calibrated | WEAK 10/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BMT/USD | 69.014 | 0.02003 | +0.25% | 0.34x |
| 2 | MEGA/USD | 68.818 | 0.05969 | +0.62% | 0.59x |
| 3 | LUNA/USD | 67.921 | 4.763e-05 | -1.34% | 0.41x |
| 4 | ALEO/USD | 62.259 | 0.03105 | -0.22% | 0.44x |
| 5 | VVV/USD | 61.346 | 21.931 | -0.29% | 2.02x |
| 6 | SKR/USD | 50.737 | 0.009972 | -0.54% | 0.78x |
| 7 | AKT/USD | 47.552 | 0.5355 | -0.37% | 1.61x |
| 8 | CSPR/USD | 47.337 | 0.0017096 | -0.84% | 0.88x |
| 9 | SENT/USD | 47.114 | 0.021093 | -0.96% | 1.34x |
| 10 | USELESS/USD | 39.522 | 0.09755 | -0.23% | 1.00x |
| 11 | SYRUP/USD | 32.577 | 0.09603 | -0.94% | 0.28x |

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

- Persisted scans: 863; predictions: 7491; observations: 521530.
- Matured sampled outcomes across 1/6/24/48h: 7775; gap abstentions: 15702. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44620976609 · **Generation:** 863 · **Legacy run:** 44620976609
**Main quote time:** 2026-11-19T21:40:35.142057+00:00 · **Legacy report time:** 2026-11-19T21:41:39.251410+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.931 | 70.09 | -0.29% | 2.02x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | MEGA/USD | 0.05969 | 67.83 | +0.62% | 0.59x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 3 | BMT/USD | 0.02003 | 63.62 | +0.25% | 0.34x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 4 | ALEO/USD | 0.03105 | 55.49 | -0.22% | 0.44x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | LUNA/USD | 4.763e-05 | 55.30 | -1.34% | 0.41x | WEAK 23/100 | EXTREME 92/100 | Do nothing |
| 6 | AKT/USD | 0.5355 | 51.77 | -0.37% | 1.61x | WEAK 41/100 | VERY_HIGH 72/100 | Watch |
| 7 | SKR/USD | 0.009972 | 45.86 | -0.54% | 0.78x | WEAK 23/100 | EXTREME 86/100 | Do nothing |
| 8 | SENT/USD | 0.021093 | 45.71 | -0.96% | 1.34x | WEAK 43/100 | HIGH 66/100 | Watch |
| 9 | CSPR/USD | 0.0017096 | 41.94 | -0.84% | 0.88x | WEAK 16/100 | EXTREME 85/100 | Do nothing |
| 10 | USELESS/USD | 0.09755 | 38.42 | -0.23% | 1.00x | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | SYRUP/USD | 0.09603 | 20.72 | -0.94% | 0.28x | WEAK 10/100 | EXTREME 94/100 | Do nothing |

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
