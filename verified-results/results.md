# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T04:51:36.438351+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45329046662
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b5f3b1e6ee1906c5171f4b5f1638097ac8f1ed8c (atomic ledger/results publication)
**Ledger generation:** 1527 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0129 | 90.083 | 77.861 | +11.98% | +1.09% | 1.68x | 15.5 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.9513 | 78.005 | 63.822 | +1.27% | -0.16% | 4.68x | 0.1 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00888 | 68.489 | 56.856 | +4.47% | -0.67% | 5.59x | 11.3 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.521e-06 | 66.855 | 68.995 | +2.89% | +0.69% | 0.44x | 2.9 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | VVV/USD | 25.086 | 62.791 | 71.073 | +2.61% | +0.03% | 0.16x | 4.4 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | LINK/USD | 9.06948 | 62.638 | 57.203 | +0.72% | -0.01% | 1.55x | 5.6 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.797 | 60.227 | 44.859 | +0.30% | +0.07% | 2.58x | 5.9 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.0073 | 59.728 | 58.633 | +0.88% | -0.00% | 1.11x | 5.0 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | LTC/USD | 41.54 | 58.356 | 54.618 | +0.29% | +0.07% | 1.34x | 4.8 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XMR/USD | 491.94 | 55.015 | 59.149 | +1.22% | +0.00% | 0.58x | 8.8 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AI/USD | 0.016 | 48.475 | 63.435 | +5.06% | -2.14% | 0.57x | 6.2 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | WEAK 29/100 | EXTREME 92/100 | Do nothing | WATCH |
| 12 | AAVE/USD | 98.09 | 46.047 | 53.306 | +1.07% | -0.05% | 0.30x | 5.1 | 2026-11-24T04:51:27.856728+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 77.861 | 0.0129 | +1.09% | 1.68x |
| 2 | VVV/USD | 71.073 | 25.086 | +0.03% | 0.16x |
| 3 | PEPE/USD | 68.995 | 3.521e-06 | +0.69% | 0.44x |
| 4 | XRP/USD | 63.822 | 0.9513 | -0.16% | 4.68x |
| 5 | AI/USD | 63.435 | 0.016 | -2.14% | 0.57x |
| 6 | XMR/USD | 59.149 | 491.94 | +0.00% | 0.58x |
| 7 | NEAR/USD | 58.633 | 3.0073 | -0.00% | 1.11x |
| 8 | LINK/USD | 57.203 | 9.06948 | -0.01% | 1.55x |
| 9 | BABY/USD | 56.856 | 0.00888 | -0.67% | 5.59x |
| 10 | LTC/USD | 54.618 | 41.54 | +0.07% | 1.34x |
| 11 | AAVE/USD | 53.306 | 98.09 | -0.05% | 0.30x |
| 12 | AVAX/USD | 44.859 | 6.797 | +0.07% | 2.58x |

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

- Persisted scans: 1527; predictions: 13057; observations: 925041.
- Matured sampled outcomes across 1/6/24/48h: 24371; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45329046662 · **Generation:** 1527 · **Legacy run:** 45329046662
**Main quote time:** 2026-11-24T04:51:36.438351+00:00 · **Legacy report time:** 2026-11-24T04:52:47.624873+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.0129 | 90.08 | +1.09% | 1.68x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 2 | XRP/USD | 0.9513 | 78.01 | -0.16% | 4.68x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | BABY/USD | 0.00888 | 68.49 | -0.67% | 5.59x | MODERATE 59/100 | VERY_HIGH 79/100 | Watch |
| 4 | PEPE/USD | 3.521e-06 | 66.86 | +0.69% | 0.44x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 5 | VVV/USD | 25.086 | 62.79 | +0.03% | 0.16x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 6 | LINK/USD | 9.06948 | 62.64 | -0.01% | 1.55x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 7 | AVAX/USD | 6.797 | 60.23 | +0.07% | 2.58x | STRONG 75/100 | HIGH 55/100 | Watch |
| 8 | NEAR/USD | 3.0073 | 59.73 | -0.00% | 1.11x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | LTC/USD ⭐ | 41.54 | 58.36 | +0.07% | 1.34x | STRONG 74/100 | HIGH 55/100 | Watch |
| 10 | XMR/USD | 491.94 | 55.01 | +0.00% | 0.58x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | AI/USD | 0.016 | 48.48 | -2.14% | 0.57x | WEAK 29/100 | EXTREME 92/100 | Do nothing |
| 12 | AAVE/USD | 98.09 | 46.05 | -0.05% | 0.30x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01293 | 82.36 | +1.09% | 1.68x | 9059 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 2 | INX/USD | 0.004071 | 74.05 | +0.87% | 1.14x | 3054 | MODERATE 62/100 | EXTREME 86/100 | Do nothing |
| 3 | LTC/USD ⭐ | 41.5 | 51.07 | +0.07% | 1.34x | 13038 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** MON/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
