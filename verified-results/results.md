# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T13:21:08.355527+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45026875304
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 88370e4bc2e03d3acb81d5c8c60ba986720a5c09 (atomic ledger/results publication)
**Ledger generation:** 1288 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002495 | 87.555 | 81.889 | +6.44% | -0.04% | 1.59x | 12.0 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 2 | TAO/USD | 191.3349 | 84.099 | 69.844 | +3.02% | -0.15% | 2.56x | 7.4 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | DRV/USD | 0.36088 | 78.019 | 80.796 | +7.66% | +0.52% | 0.46x | 12.2 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | INJ/USD | 6.29 | 77.387 | 76.755 | +5.31% | +0.82% | 0.66x | 6.4 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04704 | 77.318 | 79.496 | +6.23% | +0.28% | 0.64x | 19.2 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9972 | 75.017 | 80.394 | +3.84% | +0.26% | 0.33x | 3.0 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.75 | 66.211 | 70.667 | +2.47% | -0.02% | 0.56x | 3.2 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ZEC/USD | 792.8 | 58.175 | 66.646 | +1.88% | +0.13% | 0.09x | 3.0 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1701.9 | 57.634 | 63.135 | +1.17% | +0.07% | 0.41x | 0.1 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6578 | 56.547 | 65.594 | +1.62% | -0.11% | 0.15x | 1.5 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XBT/USD | 60668.4 | 55.451 | 61.731 | +0.96% | +0.07% | 0.34x | 0.0 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 8.75589 | 50.609 | 59.070 | +1.87% | -0.18% | 0.24x | 3.0 | 2026-11-22T13:21:00.031670+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 81.889 | 0.002495 | -0.04% | 1.59x |
| 2 | DRV/USD | 80.796 | 0.36088 | +0.52% | 0.46x |
| 3 | NEAR/USD | 80.394 | 2.9972 | +0.26% | 0.33x |
| 4 | NIGHT/USD | 79.496 | 0.04704 | +0.28% | 0.64x |
| 5 | INJ/USD | 76.755 | 6.29 | +0.82% | 0.66x |
| 6 | HYPE/USD | 70.667 | 62.75 | -0.02% | 0.56x |
| 7 | TAO/USD | 69.844 | 191.3349 | -0.15% | 2.56x |
| 8 | ZEC/USD | 66.646 | 792.8 | +0.13% | 0.09x |
| 9 | SUI/USD | 65.594 | 0.6578 | -0.11% | 0.15x |
| 10 | ETH/USD | 63.135 | 1701.9 | +0.07% | 0.41x |
| 11 | XBT/USD | 61.731 | 60668.4 | +0.07% | 0.34x |
| 12 | LINK/USD | 59.070 | 8.75589 | -0.18% | 0.24x |

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

- Persisted scans: 1288; predictions: 10376; observations: 779501.
- Matured sampled outcomes across 1/6/24/48h: 15032; gap abstentions: 22255. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45026875304 · **Generation:** 1288 · **Legacy run:** 45026875304
**Main quote time:** 2026-11-22T13:21:08.355527+00:00 · **Legacy report time:** 2026-11-22T13:22:01.278173+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002495 | 87.55 | -0.04% | 1.59x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 2 | TAO/USD | 191.3349 | 84.10 | -0.15% | 2.56x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | DRV/USD | 0.36088 | 78.02 | +0.52% | 0.46x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 4 | INJ/USD | 6.29 | 77.39 | +0.82% | 0.66x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 5 | NIGHT/USD | 0.04704 | 77.32 | +0.28% | 0.64x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 6 | NEAR/USD | 2.9972 | 75.02 | +0.26% | 0.33x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD | 62.75 | 66.21 | -0.02% | 0.56x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | ZEC/USD | 792.8 | 58.18 | +0.13% | 0.09x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1701.9 | 57.63 | +0.07% | 0.41x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | SUI/USD | 0.6578 | 56.55 | -0.11% | 0.15x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XBT/USD | 60668.4 | 55.45 | +0.07% | 0.34x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 8.75589 | 50.61 | -0.18% | 0.24x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.009 | 71.94 | +1.19% | 1.31x | 7970 | STRONG 76/100 | HIGH 61/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
