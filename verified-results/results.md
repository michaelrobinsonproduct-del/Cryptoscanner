# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:25:25.700465+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44444095832
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 3c2962368cf261b47f08f48ff364934f71d5fd33 (atomic ledger/results publication)
**Ledger generation:** 730 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021995 | 84.776 | 72.447 | +6.75% | +1.19% | 1.64x | 8.2 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.032 | 80.335 | 58.059 | +1.67% | +1.46% | 2.66x | 4.1 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UAI/USD | 0.03397 | 63.118 | 41.708 | +2.60% | +1.28% | 2.55x | 14.7 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.3272 | 61.915 | 61.176 | +0.90% | +0.81% | 0.67x | 0.3 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ICP/USD | 2.247 | 58.179 | 57.856 | +3.17% | +0.99% | 0.54x | 4.5 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | BMT/USD | 0.01974 | 54.188 | 57.559 | +4.56% | +0.05% | 0.64x | 10.1 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | WEAK 42/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | TRX/USD | 0.310133 | 41.843 | 42.000 | +0.28% | +0.01% | 0.98x | 0.0 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 8 | MEGA/USD | 0.0575 | 40.448 | 36.995 | +2.68% | -0.57% | 1.63x | 26.1 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | WEAK 30/100 | EXTREME 85/100 | Do nothing | WATCH |
| 9 | TON/USD | 1.025 | 38.472 | 31.995 | +0.39% | +0.59% | 1.35x | 9.8 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | MODERATE 64/100 | HIGH 60/100 | Watch | WATCH |
| 10 | DRV/USD | 0.26629 | 25.930 | 33.766 | +0.60% | -0.06% | 0.25x | 7.5 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | FIL/USD | 0.569 | 22.417 | 25.668 | +0.35% | +0.18% | 0.59x | 17.6 | 2026-11-19T02:25:16.620182+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.447 | 0.021995 | +1.19% | 1.64x |
| 2 | NEAR/USD | 61.176 | 3.3272 | +0.81% | 0.67x |
| 3 | VVV/USD | 58.059 | 22.032 | +1.46% | 2.66x |
| 4 | ICP/USD | 57.856 | 2.247 | +0.99% | 0.54x |
| 5 | BMT/USD | 57.559 | 0.01974 | +0.05% | 0.64x |
| 6 | TRX/USD | 42.000 | 0.310133 | +0.01% | 0.98x |
| 7 | UAI/USD | 41.708 | 0.03397 | +1.28% | 2.55x |
| 8 | MEGA/USD | 36.995 | 0.0575 | -0.57% | 1.63x |
| 9 | DRV/USD | 33.766 | 0.26629 | -0.06% | 0.25x |
| 10 | TON/USD | 31.995 | 1.025 | +0.59% | 1.35x |
| 11 | FIL/USD | 25.668 | 0.569 | +0.18% | 0.59x |

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

- Persisted scans: 730; predictions: 5935; observations: 441577.
- Matured sampled outcomes across 1/6/24/48h: 5872; gap abstentions: 13491. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44444095832 · **Generation:** 730 · **Legacy run:** 44444095832
**Main quote time:** 2026-11-19T02:25:25.700465+00:00 · **Legacy report time:** 2026-11-19T02:26:04.059630+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021995 | 84.78 | +1.19% | 1.64x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.032 | 80.33 | +1.46% | 2.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UAI/USD ⭐ | 0.03397 | 63.12 | +1.28% | 2.55x | STRONG 92/100 | VERY_HIGH 73/100 | Watch |
| 4 | NEAR/USD | 3.3272 | 61.92 | +0.81% | 0.67x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 5 | ICP/USD | 2.247 | 58.18 | +0.99% | 0.54x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | BMT/USD | 0.01974 | 54.19 | +0.05% | 0.64x | WEAK 42/100 | EXTREME 88/100 | Do nothing |
| 7 | TRX/USD | 0.310133 | 41.84 | +0.01% | 0.98x | WEAK 41/100 | HIGH 62/100 | Watch |
| 8 | MEGA/USD | 0.0575 | 40.45 | -0.57% | 1.63x | WEAK 30/100 | EXTREME 85/100 | Do nothing |
| 9 | TON/USD | 1.025 | 38.47 | +0.59% | 1.35x | MODERATE 64/100 | HIGH 60/100 | Watch |
| 10 | DRV/USD | 0.26629 | 25.93 | -0.06% | 0.25x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | FIL/USD | 0.569 | 22.42 | +0.18% | 0.59x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022015 | 77.04 | +1.19% | 1.64x | 7766 | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.02 | 63.50 | +1.46% | 2.66x | 7974 | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 3 | UAI/USD ⭐ | 0.03402 | 60.56 | +1.28% | 2.55x | 2038 | STRONG 90/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, VVV/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
