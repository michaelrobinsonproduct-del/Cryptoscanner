# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:55:12.733613+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44318539434
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 277bee41ee4effecc598dbc597568ef3f18a7e2b (atomic ledger/results publication)
**Ledger generation:** 582 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04675 | 74.602 | 75.380 | +4.14% | +0.67% | 0.59x | 4.3 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019337 | 69.729 | 51.947 | +3.58% | +0.56% | 3.07x | 8.3 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | STRONG 90/100 | HIGH 67/100 | Watch | WATCH |
| 3 | VVV/USD | 21.254 | 65.399 | 52.157 | +1.08% | -0.35% | 2.64x | 7.5 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TRX/USD | 0.309681 | 60.451 | 45.348 | +0.58% | +0.02% | 2.71x | 1.1 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05481 | 53.108 | 54.930 | +6.14% | +0.51% | 0.56x | 38.4 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 42/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | XRP/USD | 0.98564 | 48.082 | 57.165 | +0.32% | -0.11% | 0.15x | 0.1 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | CAP/USD | 0.102374 | 46.840 | 29.159 | +1.39% | +0.54% | 6.37x | 23.7 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5216 | 40.981 | 48.453 | +2.42% | -0.61% | 0.56x | 1.9 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | W/USD | 0.00904 | 39.445 | 34.790 | +1.23% | -0.66% | 1.80x | 11.1 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.09971 | 38.286 | 46.552 | +2.18% | -0.59% | 0.47x | 21.0 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 14/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | CC/USD | 0.08304 | 34.075 | 41.381 | +1.11% | -0.22% | 0.38x | 3.6 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | PEARL/USD | 1.8277 | 28.797 | 24.653 | +0.95% | +1.20% | 0.81x | 40.5 | 2026-11-18T13:55:04.362534+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 84/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 75.380 | 0.04675 | +0.67% | 0.59x |
| 2 | XRP/USD | 57.165 | 0.98564 | -0.11% | 0.15x |
| 3 | MEGA/USD | 54.930 | 0.05481 | +0.51% | 0.56x |
| 4 | VVV/USD | 52.157 | 21.254 | -0.35% | 2.64x |
| 5 | SENT/USD | 51.947 | 0.019337 | +0.56% | 3.07x |
| 6 | AKT/USD | 48.453 | 0.5216 | -0.61% | 0.56x |
| 7 | USELESS/USD | 46.552 | 0.09971 | -0.59% | 0.47x |
| 8 | TRX/USD | 45.348 | 0.309681 | +0.02% | 2.71x |
| 9 | CC/USD | 41.381 | 0.08304 | -0.22% | 0.38x |
| 10 | W/USD | 34.790 | 0.00904 | -0.66% | 1.80x |
| 11 | CAP/USD | 29.159 | 0.102374 | +0.54% | 6.37x |
| 12 | PEARL/USD | 24.653 | 1.8277 | +1.20% | 0.81x |

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

- Persisted scans: 582; predictions: 4939; observations: 351445.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13081. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44318539434 · **Generation:** 582 · **Legacy run:** 44318539434
**Main quote time:** 2026-11-18T13:55:12.733613+00:00 · **Legacy report time:** 2026-11-18T13:55:34.541221+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04675 | 74.60 | +0.67% | 0.59x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019337 | 69.73 | +0.56% | 3.07x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | VVV/USD | 21.254 | 65.40 | -0.35% | 2.64x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 4 | TRX/USD | 0.309681 | 60.45 | +0.02% | 2.71x | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | MEGA/USD | 0.05481 | 53.11 | +0.51% | 0.56x | WEAK 42/100 | EXTREME 94/100 | Do nothing |
| 6 | XRP/USD | 0.98564 | 48.08 | -0.11% | 0.15x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | CAP/USD | 0.102374 | 46.84 | +0.54% | 6.37x | MODERATE 68/100 | VERY_HIGH 79/100 | Watch |
| 8 | AKT/USD | 0.5216 | 40.98 | -0.61% | 0.56x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | W/USD | 0.00904 | 39.44 | -0.66% | 1.80x | WEAK 35/100 | VERY_HIGH 72/100 | Watch |
| 10 | USELESS/USD | 0.09971 | 38.29 | -0.59% | 0.47x | WEAK 14/100 | EXTREME 88/100 | Do nothing |
| 11 | CC/USD | 0.08304 | 34.08 | -0.22% | 0.38x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | PEARL/USD | 1.8277 | 28.80 | +1.20% | 0.81x | WEAK 29/100 | VERY_HIGH 84/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019337 | 75.24 | +0.56% | 3.07x | 5668 | STRONG 100/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
