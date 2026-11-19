# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:10:28.741579+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44625883337
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 1a49e0b4ef494e10342b124745be3671bb4b78b1 (atomic ledger/results publication)
**Ledger generation:** 867 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.06009 | 73.298 | 72.219 | +7.30% | +0.89% | 0.66x | 10.0 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021345 | 71.796 | 55.556 | +3.59% | +0.70% | 2.27x | 8.0 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | STRONG 91/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | ALEO/USD | 0.03108 | 62.808 | 63.518 | +3.67% | +0.06% | 0.90x | 3.2 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SKR/USD | 0.009984 | 56.840 | 52.125 | +3.64% | +0.07% | 1.44x | 9.0 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.09597 | 55.113 | 36.440 | +1.06% | +0.73% | 2.99x | 5.2 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.09804 | 45.626 | 48.782 | +2.60% | -0.44% | 0.90x | 17.4 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 7 | VVV/USD | 21.766 | 45.164 | 54.161 | +0.44% | -0.49% | 0.35x | 7.8 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.535 | 37.861 | 48.742 | +3.28% | -0.58% | 0.20x | 13.1 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | WEAK 19/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | BLUR/USD | 0.00668 | 35.624 | 26.953 | +1.52% | +0.30% | 1.72x | 29.9 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | XPL/USD | 0.0467 | 31.691 | 22.837 | +1.52% | -0.21% | 1.99x | 42.9 | 2026-11-19T22:10:22.481923+00:00 | Not calibrated | WEAK 21/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 72.219 | 0.06009 | +0.89% | 0.66x |
| 2 | ALEO/USD | 63.518 | 0.03108 | +0.06% | 0.90x |
| 3 | SENT/USD | 55.556 | 0.021345 | +0.70% | 2.27x |
| 4 | VVV/USD | 54.161 | 21.766 | -0.49% | 0.35x |
| 5 | SKR/USD | 52.125 | 0.009984 | +0.07% | 1.44x |
| 6 | USELESS/USD | 48.782 | 0.09804 | -0.44% | 0.90x |
| 7 | AKT/USD | 48.742 | 0.535 | -0.58% | 0.20x |
| 8 | SYRUP/USD | 36.440 | 0.09597 | +0.73% | 2.99x |
| 9 | BLUR/USD | 26.953 | 0.00668 | +0.30% | 1.72x |
| 10 | XPL/USD | 22.837 | 0.0467 | -0.21% | 1.99x |

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

- Persisted scans: 867; predictions: 7533; observations: 523936.
- Matured sampled outcomes across 1/6/24/48h: 7906; gap abstentions: 15728. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44625883337 · **Generation:** 867 · **Legacy run:** 44625883337
**Main quote time:** 2026-11-19T22:10:28.741579+00:00 · **Legacy report time:** 2026-11-19T22:11:11.630500+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.06009 | 73.30 | +0.89% | 0.66x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 2 | SENT/USD ⭐ | 0.021345 | 71.80 | +0.70% | 2.27x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | ALEO/USD | 0.03108 | 62.81 | +0.06% | 0.90x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 4 | SKR/USD ⭐ | 0.009984 | 56.84 | +0.07% | 1.44x | STRONG 73/100 | HIGH 67/100 | Watch |
| 5 | SYRUP/USD | 0.09597 | 55.11 | +0.73% | 2.99x | STRONG 83/100 | HIGH 67/100 | Watch |
| 6 | USELESS/USD | 0.09804 | 45.63 | -0.44% | 0.90x | WEAK 23/100 | VERY_HIGH 74/100 | Do nothing |
| 7 | VVV/USD | 21.766 | 45.16 | -0.49% | 0.35x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKT/USD | 0.535 | 37.86 | -0.58% | 0.20x | WEAK 19/100 | EXTREME 87/100 | Do nothing |
| 9 | BLUR/USD | 0.00668 | 35.62 | +0.30% | 1.72x | MODERATE 53/100 | VERY_HIGH 79/100 | Watch |
| 10 | XPL/USD | 0.0467 | 31.69 | -0.21% | 1.99x | WEAK 21/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021352 | 79.10 | +0.70% | 2.27x | 14837 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.009974 | 56.56 | +0.07% | 1.44x | 1374 | MODERATE 68/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
