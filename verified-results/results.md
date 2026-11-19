# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T21:50:34.192205+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44622629897
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** c8fb6989fa223da62605869db4d28f5bb1558df6 (atomic ledger/results publication)
**Ledger generation:** 864 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05952 | 73.881 | 70.297 | +6.29% | +0.54% | 1.09x | 11.8 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | BMT/USD | 0.02003 | 59.506 | 66.513 | +6.09% | +0.35% | 0.12x | 15.0 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | LUNA/USD | 4.777e-05 | 58.904 | 63.627 | +9.72% | +0.25% | 0.40x | 37.9 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | ALEO/USD | 0.03115 | 53.484 | 55.208 | +3.90% | +0.71% | 0.47x | 22.4 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | VVV/USD | 21.871 | 51.905 | 59.402 | +0.92% | -0.16% | 0.33x | 4.1 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.021186 | 51.578 | 50.069 | +2.82% | +0.47% | 0.92x | 8.0 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5355 | 50.151 | 49.419 | +3.38% | +0.02% | 1.06x | 13.1 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | USELESS/USD | 0.09783 | 45.199 | 40.727 | +2.38% | +0.61% | 1.14x | 29.7 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | SKR/USD | 0.009986 | 44.969 | 51.266 | +3.66% | -0.12% | 0.43x | 11.0 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | WEAK 22/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | CSPR/USD | 0.0016928 | 41.779 | 53.316 | +3.66% | -1.05% | 0.37x | 8.3 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | WEAK 26/100 | EXTREME 85/100 | Do nothing | WATCH |
| 11 | XPL/USD | 0.0465 | 27.040 | 30.428 | +1.09% | +0.22% | 0.55x | 21.5 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | SYRUP/USD | 0.09532 | 24.692 | 28.924 | +0.38% | -0.52% | 0.84x | 10.5 | 2026-11-19T21:50:27.119992+00:00 | Not calibrated | WEAK 12/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 70.297 | 0.05952 | +0.54% | 1.09x |
| 2 | BMT/USD | 66.513 | 0.02003 | +0.35% | 0.12x |
| 3 | LUNA/USD | 63.627 | 4.777e-05 | +0.25% | 0.40x |
| 4 | VVV/USD | 59.402 | 21.871 | -0.16% | 0.33x |
| 5 | ALEO/USD | 55.208 | 0.03115 | +0.71% | 0.47x |
| 6 | CSPR/USD | 53.316 | 0.0016928 | -1.05% | 0.37x |
| 7 | SKR/USD | 51.266 | 0.009986 | -0.12% | 0.43x |
| 8 | SENT/USD | 50.069 | 0.021186 | +0.47% | 0.92x |
| 9 | AKT/USD | 49.419 | 0.5355 | +0.02% | 1.06x |
| 10 | USELESS/USD | 40.727 | 0.09783 | +0.61% | 1.14x |
| 11 | XPL/USD | 30.428 | 0.0465 | +0.22% | 0.55x |
| 12 | SYRUP/USD | 28.924 | 0.09532 | -0.52% | 0.84x |

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

- Persisted scans: 864; predictions: 7503; observations: 522131.
- Matured sampled outcomes across 1/6/24/48h: 7823; gap abstentions: 15707. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44622629897 · **Generation:** 864 · **Legacy run:** 44622629897
**Main quote time:** 2026-11-19T21:50:34.192205+00:00 · **Legacy report time:** 2026-11-19T21:51:31.610527+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05952 | 73.88 | +0.54% | 1.09x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 2 | BMT/USD | 0.02003 | 59.51 | +0.35% | 0.12x | MODERATE 55/100 | EXTREME 88/100 | Do nothing |
| 3 | LUNA/USD | 4.777e-05 | 58.90 | +0.25% | 0.40x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |
| 4 | ALEO/USD | 0.03115 | 53.48 | +0.71% | 0.47x | MODERATE 47/100 | VERY_HIGH 82/100 | Watch |
| 5 | VVV/USD | 21.871 | 51.91 | -0.16% | 0.33x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | SENT/USD | 0.021186 | 51.58 | +0.47% | 0.92x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 7 | AKT/USD | 0.5355 | 50.15 | +0.02% | 1.06x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 8 | USELESS/USD ⭐ | 0.09783 | 45.20 | +0.61% | 1.14x | MODERATE 58/100 | VERY_HIGH 74/100 | Watch |
| 9 | SKR/USD | 0.009986 | 44.97 | -0.12% | 0.43x | WEAK 22/100 | EXTREME 94/100 | Do nothing |
| 10 | CSPR/USD | 0.0016928 | 41.78 | -1.05% | 0.37x | WEAK 26/100 | EXTREME 85/100 | Do nothing |
| 11 | XPL/USD | 0.0465 | 27.04 | +0.22% | 0.55x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 12 | SYRUP/USD | 0.09532 | 24.69 | -0.52% | 0.84x | WEAK 12/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05952 | 69.43 | +0.54% | 1.09x | 2178 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.09804 | 60.93 | +0.61% | 1.14x | 4382 | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** MEGA/USD, USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
