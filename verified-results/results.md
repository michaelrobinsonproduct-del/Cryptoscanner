# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T14:10:29.630231+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44540729739
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** e748b6219947c29e2b8d606f828daa06b4b5d152 (atomic ledger/results publication)
**Ledger generation:** 789 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.115 | 109.937 | 98.054 | +6.66% | -0.62% | 6.73x | 3.9 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.00274 | 92.898 | 78.263 | +5.55% | -0.07% | 2.82x | 11.0 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.941e-06 | 86.024 | 75.742 | +5.21% | -0.76% | 2.41x | 2.5 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TAO/USD | 199.2294 | 84.034 | 78.322 | +3.79% | -0.12% | 1.63x | 6.4 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0595885 | 76.389 | 61.922 | +1.50% | -0.11% | 3.71x | 0.1 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ZEC/USD | 944.59 | 74.494 | 78.413 | +3.58% | -0.15% | 0.68x | 3.3 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ADA/USD | 0.155294 | 71.627 | 72.345 | +2.67% | -0.13% | 0.99x | 2.7 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.99065 | 70.621 | 72.284 | +2.51% | -0.06% | 0.86x | 0.6 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | QNT/USD | 155.6 | 70.159 | 61.875 | +2.33% | +0.15% | 1.75x | 0.6 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ONDO/USD | 0.30569 | 67.365 | 53.478 | +2.70% | -0.05% | 2.41x | 0.3 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 11 | AKT/USD | 0.5529 | 66.957 | 73.824 | +6.74% | +0.00% | 0.31x | 5.4 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | XBT/USD | 63869 | 66.793 | 64.822 | +1.40% | +0.04% | 1.18x | 0.0 | 2026-11-19T14:10:23.909625+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 98.054 | 23.115 | -0.62% | 6.73x |
| 2 | ZEC/USD | 78.413 | 944.59 | -0.15% | 0.68x |
| 3 | TAO/USD | 78.322 | 199.2294 | -0.12% | 1.63x |
| 4 | PUMP/USD | 78.263 | 0.00274 | -0.07% | 2.82x |
| 5 | PEPE/USD | 75.742 | 3.941e-06 | -0.76% | 2.41x |
| 6 | AKT/USD | 73.824 | 0.5529 | +0.00% | 0.31x |
| 7 | ADA/USD | 72.345 | 0.155294 | -0.13% | 0.99x |
| 8 | XRP/USD | 72.284 | 0.99065 | -0.06% | 0.86x |
| 9 | XBT/USD | 64.822 | 63869 | +0.04% | 1.18x |
| 10 | XDG/USD | 61.922 | 0.0595885 | -0.11% | 3.71x |
| 11 | QNT/USD | 61.875 | 155.6 | +0.15% | 1.75x |
| 12 | ONDO/USD | 53.478 | 0.30569 | -0.05% | 2.41x |

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

- Persisted scans: 789; predictions: 6612; observations: 477295.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 15041. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44540729739 · **Generation:** 789 · **Legacy run:** 44540729739
**Main quote time:** 2026-11-19T14:10:29.630231+00:00 · **Legacy report time:** 2026-11-19T14:11:07.386861+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.115 | 109.94 | -0.62% | 6.73x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | PUMP/USD | 0.00274 | 92.90 | -0.07% | 2.82x | STRONG 71/100 | HIGH 67/100 | Watch |
| 3 | PEPE/USD | 3.941e-06 | 86.02 | -0.76% | 2.41x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | TAO/USD | 199.2294 | 84.03 | -0.12% | 1.63x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 5 | XDG/USD | 0.0595885 | 76.39 | -0.11% | 3.71x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | ZEC/USD | 944.59 | 74.49 | -0.15% | 0.68x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 7 | ADA/USD | 0.155294 | 71.63 | -0.13% | 0.99x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.99065 | 70.62 | -0.06% | 0.86x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | QNT/USD | 155.6 | 70.16 | +0.15% | 1.75x | STRONG 70/100 | HIGH 55/100 | Watch |
| 10 | ONDO/USD | 0.30569 | 67.37 | -0.05% | 2.41x | MODERATE 64/100 | HIGH 66/100 | Watch |
| 11 | AKT/USD | 0.5529 | 66.96 | +0.00% | 0.31x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |
| 12 | XBT/USD | 63869 | 66.79 | +0.04% | 1.18x | MODERATE 58/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021739 | 85.75 | +0.58% | 3.25x | 13568 | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 2 | CAP/USD | 0.101371 | 82.68 | +0.91% | 1.52x | 6524 | STRONG 86/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
