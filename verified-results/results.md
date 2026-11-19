# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:05:30.458084+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44625062317
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b9bb99d7a8d2afa5581b11c0b2926d843a27aca4 (atomic ledger/results publication)
**Ledger generation:** 866 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021339 | 72.591 | 57.223 | +3.56% | +0.71% | 2.18x | 4.2 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | STRONG 91/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | MEGA/USD | 0.05997 | 69.177 | 69.700 | +7.09% | +0.25% | 0.82x | 15.0 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ALEO/USD | 0.03106 | 56.975 | 61.328 | +3.60% | -0.54% | 0.84x | 6.4 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | SYRUP/USD | 0.0963 | 56.940 | 36.799 | +1.41% | +1.03% | 2.66x | 9.4 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Watch | WATCH |
| 5 | LUNA/USD | 4.789e-05 | 51.412 | 62.370 | +9.99% | -0.29% | 0.05x | 39.8 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | WEAK 16/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | CSPR/USD | 0.0017049 | 50.338 | 52.089 | +4.40% | +0.71% | 0.47x | 21.1 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | VVV/USD | 21.851 | 49.596 | 56.688 | +0.83% | -0.06% | 0.32x | 8.3 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SKR/USD | 0.010005 | 48.657 | 47.663 | +3.86% | +0.15% | 1.02x | 21.0 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | USELESS/USD | 0.09791 | 48.467 | 49.739 | +2.46% | +0.13% | 0.81x | 13.3 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 10 | AKT/USD | 0.5362 | 43.953 | 51.314 | +3.51% | +0.21% | 0.16x | 11.2 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | XPL/USD | 0.0466 | 19.657 | 21.286 | +1.30% | +0.22% | 0.73x | 42.9 | 2026-11-19T22:05:24.225473+00:00 | Not calibrated | WEAK 25/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 69.700 | 0.05997 | +0.25% | 0.82x |
| 2 | LUNA/USD | 62.370 | 4.789e-05 | -0.29% | 0.05x |
| 3 | ALEO/USD | 61.328 | 0.03106 | -0.54% | 0.84x |
| 4 | SENT/USD | 57.223 | 0.021339 | +0.71% | 2.18x |
| 5 | VVV/USD | 56.688 | 21.851 | -0.06% | 0.32x |
| 6 | CSPR/USD | 52.089 | 0.0017049 | +0.71% | 0.47x |
| 7 | AKT/USD | 51.314 | 0.5362 | +0.21% | 0.16x |
| 8 | USELESS/USD | 49.739 | 0.09791 | +0.13% | 0.81x |
| 9 | SKR/USD | 47.663 | 0.010005 | +0.15% | 1.02x |
| 10 | SYRUP/USD | 36.799 | 0.0963 | +1.03% | 2.66x |
| 11 | XPL/USD | 21.286 | 0.0466 | +0.22% | 0.73x |

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

- Persisted scans: 866; predictions: 7523; observations: 523334.
- Matured sampled outcomes across 1/6/24/48h: 7882; gap abstentions: 15724. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44625062317 · **Generation:** 866 · **Legacy run:** 44625062317
**Main quote time:** 2026-11-19T22:05:30.458084+00:00 · **Legacy report time:** 2026-11-19T22:06:20.727019+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021339 | 72.59 | +0.71% | 2.18x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | MEGA/USD | 0.05997 | 69.18 | +0.25% | 0.82x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 3 | ALEO/USD | 0.03106 | 56.98 | -0.54% | 0.84x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 4 | SYRUP/USD | 0.0963 | 56.94 | +1.03% | 2.66x | STRONG 83/100 | HIGH 67/100 | Watch |
| 5 | LUNA/USD | 4.789e-05 | 51.41 | -0.29% | 0.05x | WEAK 16/100 | EXTREME 88/100 | Do nothing |
| 6 | CSPR/USD | 0.0017049 | 50.34 | +0.71% | 0.47x | MODERATE 45/100 | EXTREME 87/100 | Do nothing |
| 7 | VVV/USD | 21.851 | 49.60 | -0.06% | 0.32x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SKR/USD ⭐ | 0.010005 | 48.66 | +0.15% | 1.02x | MODERATE 49/100 | EXTREME 86/100 | Do nothing |
| 9 | USELESS/USD | 0.09791 | 48.47 | +0.13% | 0.81x | WEAK 39/100 | HIGH 68/100 | Watch |
| 10 | AKT/USD | 0.5362 | 43.95 | +0.21% | 0.16x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 11 | XPL/USD | 0.0466 | 19.66 | +0.22% | 0.73x | WEAK 25/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021287 | 71.21 | +0.71% | 2.18x | 14838 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.010005 | 58.98 | +0.15% | 1.02x | 1370 | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** SENT/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
