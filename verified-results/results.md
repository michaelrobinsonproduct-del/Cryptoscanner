# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:55:35.637884+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44613414448
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 90516d9e03134ef29dcf320fd1806902891a3d27 (atomic ledger/results publication)
**Ledger generation:** 858 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.259 | 69.317 | 73.094 | +2.71% | +0.19% | 0.53x | 1.8 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5482 | 65.529 | 67.577 | +5.83% | -0.11% | 0.85x | 11.0 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 3 | HYPE/USD | 67.71 | 63.123 | 60.731 | +1.24% | +1.06% | 0.71x | 5.9 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.09888 | 62.527 | 50.936 | +3.47% | +1.14% | 1.59x | 23.3 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 66/100 | HIGH 67/100 | Watch | WATCH |
| 5 | INJ/USD | 7.027 | 61.935 | 47.433 | +0.66% | -0.10% | 2.79x | 4.3 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010138 | 58.629 | 59.945 | +5.24% | +0.27% | 0.73x | 15.8 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | PUMP/USD | 0.002641 | 55.181 | 49.088 | +1.73% | +0.65% | 1.29x | 11.4 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.151875 | 53.018 | 55.799 | +0.41% | +0.27% | 0.59x | 4.2 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TAO/USD | 192.8399 | 46.165 | 50.396 | +0.46% | +0.44% | 0.36x | 10.0 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SENT/USD | 0.021147 | 45.531 | 48.718 | +2.63% | +0.29% | 0.53x | 8.0 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | TRX/USD | 0.310081 | 41.248 | 42.545 | +0.26% | +0.06% | 0.84x | 1.1 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PYTH/USD | 0.05327 | 37.119 | 34.589 | +0.97% | +0.11% | 1.20x | 9.4 | 2026-11-19T20:55:27.067664+00:00 | Not calibrated | WEAK 44/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.094 | 22.259 | +0.19% | 0.53x |
| 2 | AKT/USD | 67.577 | 0.5482 | -0.11% | 0.85x |
| 3 | HYPE/USD | 60.731 | 67.71 | +1.06% | 0.71x |
| 4 | SKR/USD | 59.945 | 0.010138 | +0.27% | 0.73x |
| 5 | ADA/USD | 55.799 | 0.151875 | +0.27% | 0.59x |
| 6 | USELESS/USD | 50.936 | 0.09888 | +1.14% | 1.59x |
| 7 | TAO/USD | 50.396 | 192.8399 | +0.44% | 0.36x |
| 8 | PUMP/USD | 49.088 | 0.002641 | +0.65% | 1.29x |
| 9 | SENT/USD | 48.718 | 0.021147 | +0.29% | 0.53x |
| 10 | INJ/USD | 47.433 | 7.027 | -0.10% | 2.79x |
| 11 | TRX/USD | 42.545 | 0.310081 | +0.06% | 0.84x |
| 12 | PYTH/USD | 34.589 | 0.05327 | +0.11% | 1.20x |

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

- Persisted scans: 858; predictions: 7435; observations: 518525.
- Matured sampled outcomes across 1/6/24/48h: 7607; gap abstentions: 15676. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44613414448 · **Generation:** 858 · **Legacy run:** 44613414448
**Main quote time:** 2026-11-19T20:55:35.637884+00:00 · **Legacy report time:** 2026-11-19T20:56:28.070883+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.259 | 69.32 | +0.19% | 0.53x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 2 | AKT/USD | 0.5482 | 65.53 | -0.11% | 0.85x | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing |
| 3 | HYPE/USD | 67.71 | 63.12 | +1.06% | 0.71x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 4 | USELESS/USD ⭐ | 0.09888 | 62.53 | +1.14% | 1.59x | STRONG 76/100 | HIGH 67/100 | Consider small entry |
| 5 | INJ/USD | 7.027 | 61.94 | -0.10% | 2.79x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 6 | SKR/USD | 0.010138 | 58.63 | +0.27% | 0.73x | MODERATE 54/100 | EXTREME 88/100 | Do nothing |
| 7 | PUMP/USD | 0.002641 | 55.18 | +0.65% | 1.29x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.151875 | 53.02 | +0.27% | 0.59x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | TAO/USD | 192.8399 | 46.16 | +0.44% | 0.36x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 10 | SENT/USD | 0.021147 | 45.53 | +0.29% | 0.53x | MODERATE 53/100 | VERY_HIGH 75/100 | Watch |
| 11 | TRX/USD | 0.310081 | 41.25 | +0.06% | 0.84x | WEAK 41/100 | HIGH 62/100 | Watch |
| 12 | PYTH/USD | 0.05327 | 37.12 | +0.11% | 1.20x | WEAK 44/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.0987 | 72.17 | +1.14% | 1.59x | 3723 | STRONG 81/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
