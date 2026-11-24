# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T04:22:26.514766+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45325595868
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bb9f2c00f2298e7c2a834173def61759ba3a154f (atomic ledger/results publication)
**Ledger generation:** 1524 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01634 | 95.520 | 73.118 | +7.29% | +1.48% | 4.51x | 6.1 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 24.926 | 87.736 | 65.676 | +1.96% | +1.41% | 9.95x | 6.0 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | MON/USD | 0.0126 | 87.438 | 77.009 | +9.38% | +2.35% | 0.87x | 15.9 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | MODERATE 69/100 | HIGH 68/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9924 | 75.304 | 57.129 | +0.38% | +0.64% | 2.62x | 1.0 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | AAVE/USD | 98.03 | 70.194 | 52.936 | +1.01% | +0.45% | 10.59x | 5.1 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | UNI/USD | 4.8603 | 68.951 | 51.354 | +0.46% | +0.52% | 9.28x | 4.7 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.491e-06 | 65.423 | 59.664 | +2.02% | +0.63% | 1.26x | 8.6 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LINK/USD | 9.05762 | 60.369 | 57.469 | +0.59% | +0.30% | 1.14x | 3.3 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6809 | 59.601 | 39.926 | +0.80% | +0.94% | 5.02x | 1.5 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 10 | WLD/USD | 0.2421 | 59.209 | 44.265 | +1.59% | +0.83% | 2.08x | 4.1 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 11 | XRP/USD | 0.95145 | 58.683 | 63.619 | +1.28% | +0.39% | 0.31x | 0.7 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XMR/USD | 490.46 | 57.537 | 58.234 | +0.91% | +0.38% | 0.74x | 6.3 | 2026-11-24T04:22:17.844894+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 77.009 | 0.0126 | +2.35% | 0.87x |
| 2 | AI/USD | 73.118 | 0.01634 | +1.48% | 4.51x |
| 3 | VVV/USD | 65.676 | 24.926 | +1.41% | 9.95x |
| 4 | XRP/USD | 63.619 | 0.95145 | +0.39% | 0.31x |
| 5 | PEPE/USD | 59.664 | 3.491e-06 | +0.63% | 1.26x |
| 6 | XMR/USD | 58.234 | 490.46 | +0.38% | 0.74x |
| 7 | LINK/USD | 57.469 | 9.05762 | +0.30% | 1.14x |
| 8 | NEAR/USD | 57.129 | 2.9924 | +0.64% | 2.62x |
| 9 | AAVE/USD | 52.936 | 98.03 | +0.45% | 10.59x |
| 10 | UNI/USD | 51.354 | 4.8603 | +0.52% | 9.28x |
| 11 | WLD/USD | 44.265 | 0.2421 | +0.83% | 2.08x |
| 12 | DOT/USD | 39.926 | 0.6809 | +0.94% | 5.02x |

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

- Persisted scans: 1524; predictions: 13021; observations: 923214.
- Matured sampled outcomes across 1/6/24/48h: 24273; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45325595868 · **Generation:** 1524 · **Legacy run:** 45325595868
**Main quote time:** 2026-11-24T04:22:26.514766+00:00 · **Legacy report time:** 2026-11-24T04:23:38.120476+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01634 | 95.52 | +1.48% | 4.51x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.926 | 87.74 | +1.41% | 9.95x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | MON/USD | 0.0126 | 87.44 | +2.35% | 0.87x | MODERATE 69/100 | HIGH 68/100 | Watch |
| 4 | NEAR/USD ⭐ | 2.9924 | 75.30 | +0.64% | 2.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | AAVE/USD | 98.03 | 70.19 | +0.45% | 10.59x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 6 | UNI/USD | 4.8603 | 68.95 | +0.52% | 9.28x | STRONG 89/100 | HIGH 55/100 | Watch |
| 7 | PEPE/USD ⭐ | 3.491e-06 | 65.42 | +0.63% | 1.26x | STRONG 78/100 | HIGH 55/100 | Watch |
| 8 | LINK/USD ⭐ | 9.05762 | 60.37 | +0.30% | 1.14x | STRONG 75/100 | HIGH 62/100 | Watch |
| 9 | DOT/USD | 0.6809 | 59.60 | +0.94% | 5.02x | STRONG 85/100 | HIGH 60/100 | Watch |
| 10 | WLD/USD | 0.2421 | 59.21 | +0.83% | 2.08x | STRONG 85/100 | HIGH 60/100 | Watch |
| 11 | XRP/USD | 0.95145 | 58.68 | +0.39% | 0.31x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | XMR/USD | 490.46 | 57.54 | +0.38% | 0.74x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01633 | 83.15 | +1.48% | 4.51x | 2916 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 24.924 | 76.36 | +1.41% | 9.95x | 13602 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEPE/USD ⭐ | 3.501e-06 | 64.59 | +0.63% | 1.26x | 9375 | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 2.9917 | 61.26 | +0.64% | 2.62x | 23203 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.06503 | 58.23 | +0.30% | 1.14x | 8845 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** AI/USD, VVV/USD, NEAR/USD, PEPE/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
