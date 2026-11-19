# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:10:52.040140+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44584802940
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 68649f77b1c520238bb0352a3a376481c41e910a (atomic ledger/results publication)
**Ledger generation:** 832 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 69.18 | 83.002 | 77.627 | +3.44% | +0.70% | 1.19x | 2.9 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010173 | 71.251 | 66.414 | +5.61% | -0.10% | 1.53x | 7.9 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 22.573 | 68.387 | 80.813 | +4.16% | -1.00% | 0.26x | 6.6 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.09955 | 67.963 | 59.279 | +4.83% | -0.16% | 1.95x | 12.1 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | CT/USD | 0.1276 | 64.334 | 69.027 | +7.95% | -1.01% | 1.04x | 15.7 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 6 | LIGHTER/USD | 2.861 | 63.747 | 65.663 | +5.42% | -0.03% | 0.83x | 14.1 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | SOL/USD | 73.75 | 62.550 | 56.321 | +0.29% | -0.14% | 1.69x | 1.4 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | PUMP/USD | 0.002679 | 62.094 | 58.930 | +3.20% | -0.67% | 1.65x | 11.2 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |
| 9 | ADA/USD | 0.152744 | 60.284 | 60.357 | +0.99% | -0.15% | 1.07x | 3.1 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | AKT/USD | 0.55 | 56.737 | 70.759 | +6.18% | -1.13% | 0.16x | 9.1 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 33/100 | EXTREME 85/100 | Do nothing | WATCH |
| 11 | INJ/USD | 7.082 | 45.546 | 50.625 | +1.45% | -0.88% | 0.93x | 5.6 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | BNB/USD | 584.87 | 38.780 | 44.582 | +0.62% | -0.26% | 0.55x | 1.7 | 2026-11-19T18:10:43.742795+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.813 | 22.573 | -1.00% | 0.26x |
| 2 | HYPE/USD | 77.627 | 69.18 | +0.70% | 1.19x |
| 3 | AKT/USD | 70.759 | 0.55 | -1.13% | 0.16x |
| 4 | CT/USD | 69.027 | 0.1276 | -1.01% | 1.04x |
| 5 | SKR/USD | 66.414 | 0.010173 | -0.10% | 1.53x |
| 6 | LIGHTER/USD | 65.663 | 2.861 | -0.03% | 0.83x |
| 7 | ADA/USD | 60.357 | 0.152744 | -0.15% | 1.07x |
| 8 | SYRUP/USD | 59.279 | 0.09955 | -0.16% | 1.95x |
| 9 | PUMP/USD | 58.930 | 0.002679 | -0.67% | 1.65x |
| 10 | SOL/USD | 56.321 | 73.75 | -0.14% | 1.69x |
| 11 | INJ/USD | 50.625 | 7.082 | -0.88% | 0.93x |
| 12 | BNB/USD | 44.582 | 584.87 | -0.26% | 0.55x |

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

- Persisted scans: 832; predictions: 7128; observations: 502947.
- Matured sampled outcomes across 1/6/24/48h: 7103; gap abstentions: 15483. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44584802940 · **Generation:** 832 · **Legacy run:** 44584802940
**Main quote time:** 2026-11-19T18:10:52.040140+00:00 · **Legacy report time:** 2026-11-19T18:11:34.823184+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.18 | 83.00 | +0.70% | 1.19x | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | SKR/USD | 0.010173 | 71.25 | -0.10% | 1.53x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 22.573 | 68.39 | -1.00% | 0.26x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 4 | SYRUP/USD | 0.09955 | 67.96 | -0.16% | 1.95x | MODERATE 49/100 | VERY_HIGH 79/100 | Watch |
| 5 | CT/USD | 0.1276 | 64.33 | -1.01% | 1.04x | WEAK 37/100 | VERY_HIGH 83/100 | Watch |
| 6 | LIGHTER/USD | 2.861 | 63.75 | -0.03% | 0.83x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | SOL/USD | 73.75 | 62.55 | -0.14% | 1.69x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | PUMP/USD | 0.002679 | 62.09 | -0.67% | 1.65x | MODERATE 46/100 | HIGH 67/100 | Watch |
| 9 | ADA/USD | 0.152744 | 60.28 | -0.15% | 1.07x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | AKT/USD | 0.55 | 56.74 | -1.13% | 0.16x | WEAK 33/100 | EXTREME 85/100 | Do nothing |
| 11 | INJ/USD | 7.082 | 45.55 | -0.88% | 0.93x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 12 | BNB/USD | 584.87 | 38.78 | -0.26% | 0.55x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.13 | 86.52 | +0.70% | 1.19x | 13322 | STRONG 88/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
