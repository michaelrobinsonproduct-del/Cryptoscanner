# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T07:51:52.206697+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45350985626
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d141520c04ad4c0a0a31933cf3bba579e226273a (atomic ledger/results publication)
**Ledger generation:** 1546 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BABY/USD | 0.00911 | 79.475 | 71.380 | +7.18% | +1.90% | 0.86x | 11.0 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | XMR/USD | 499.82 | 74.343 | 71.272 | +2.84% | +0.01% | 1.30x | 7.2 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LINK/USD | 9.04798 | 71.113 | 57.125 | +0.48% | -0.20% | 4.75x | 2.4 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 41.57 | 70.612 | 56.332 | +0.36% | -0.14% | 4.77x | 2.4 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04904 | 70.600 | 59.337 | +1.85% | -0.75% | 4.03x | 6.1 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | VVV/USD | 25.284 | 69.942 | 75.180 | +3.42% | +0.20% | 0.38x | 7.5 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.3297 | 64.903 | 66.824 | +6.66% | -0.09% | 0.85x | 21.2 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | WEAK 27/100 | EXTREME 85/100 | Do nothing | WATCH |
| 8 | NEAR/USD | 2.9998 | 60.248 | 58.201 | +0.62% | -0.19% | 1.30x | 2.3 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | WEAK 40/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.527e-06 | 59.632 | 70.650 | +3.07% | -0.45% | 0.12x | 2.8 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94394 | 54.202 | 57.967 | +0.48% | +0.07% | 0.59x | 0.8 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | WLD/USD | 0.2411 | 53.201 | 41.494 | +1.18% | -0.66% | 2.73x | 4.1 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 12 | 2Z/USD | 0.01627 | 52.120 | 55.384 | +3.96% | -0.24% | 0.80x | 6.1 | 2026-11-24T07:51:43.779288+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 75.180 | 25.284 | +0.20% | 0.38x |
| 2 | BABY/USD | 71.380 | 0.00911 | +1.90% | 0.86x |
| 3 | XMR/USD | 71.272 | 499.82 | +0.01% | 1.30x |
| 4 | PEPE/USD | 70.650 | 3.527e-06 | -0.45% | 0.12x |
| 5 | ICNT/USD | 66.824 | 0.3297 | -0.09% | 0.85x |
| 6 | NIGHT/USD | 59.337 | 0.04904 | -0.75% | 4.03x |
| 7 | NEAR/USD | 58.201 | 2.9998 | -0.19% | 1.30x |
| 8 | XRP/USD | 57.967 | 0.94394 | +0.07% | 0.59x |
| 9 | LINK/USD | 57.125 | 9.04798 | -0.20% | 4.75x |
| 10 | LTC/USD | 56.332 | 41.57 | -0.14% | 4.77x |
| 11 | 2Z/USD | 55.384 | 0.01627 | -0.24% | 0.80x |
| 12 | WLD/USD | 41.494 | 0.2411 | -0.66% | 2.73x |

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

- Persisted scans: 1546; predictions: 13285; observations: 936612.
- Matured sampled outcomes across 1/6/24/48h: 25049; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
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

**Writer:** 45350985626 · **Generation:** 1546 · **Legacy run:** 45350985626
**Main quote time:** 2026-11-24T07:51:52.206697+00:00 · **Legacy report time:** 2026-11-24T07:52:44.076086+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD | 0.00911 | 79.48 | +1.90% | 0.86x | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |
| 2 | XMR/USD | 499.82 | 74.34 | +0.01% | 1.30x | STRONG 72/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD | 9.04798 | 71.11 | -0.20% | 4.75x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 41.57 | 70.61 | -0.14% | 4.77x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04904 | 70.60 | -0.75% | 4.03x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | VVV/USD | 25.284 | 69.94 | +0.20% | 0.38x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 7 | ICNT/USD | 0.3297 | 64.90 | -0.09% | 0.85x | WEAK 27/100 | EXTREME 85/100 | Do nothing |
| 8 | NEAR/USD | 2.9998 | 60.25 | -0.19% | 1.30x | WEAK 40/100 | HIGH 61/100 | Watch |
| 9 | PEPE/USD | 3.527e-06 | 59.63 | -0.45% | 0.12x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.94394 | 54.20 | +0.07% | 0.59x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | WLD/USD | 0.2411 | 53.20 | -0.66% | 2.73x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 12 | 2Z/USD | 0.01627 | 52.12 | -0.24% | 0.80x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |

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
