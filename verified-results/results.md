# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:35:29.741360+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44567640430
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** bfe2f3fc5f042e416140ad55aefc358adf510b24 (atomic ledger/results publication)
**Ledger generation:** 814 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BILL/USD | 0.00441 | 84.998 | 64.450 | +11.65% | +1.38% | 2.37x | 22.8 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | STRONG 87/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010353 | 77.529 | 71.228 | +7.47% | -0.23% | 1.75x | 9.7 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 22.546 | 74.300 | 79.716 | +4.04% | -0.15% | 0.53x | 7.1 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5452 | 66.533 | 65.483 | +5.25% | +0.11% | 1.05x | 5.5 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | TRUST/USD | 0.05411 | 64.541 | 73.412 | +9.98% | -1.26% | 0.74x | 5.6 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | WEAK 37/100 | EXTREME 92/100 | Do nothing | WATCH |
| 6 | BMT/USD | 0.02025 | 63.931 | 71.231 | +7.26% | +0.30% | 0.12x | 9.9 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | PYTH/USD | 0.05611 | 61.426 | 69.523 | +6.35% | -0.32% | 0.35x | 14.2 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 67.67 | 58.334 | 62.530 | +1.18% | +0.12% | 0.52x | 1.5 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.10057 | 53.990 | 65.939 | +5.24% | -0.63% | 0.12x | 15.9 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | TAO/USD | 193.3764 | 53.840 | 56.987 | +0.74% | +0.10% | 0.64x | 6.4 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.152666 | 52.699 | 59.767 | +0.93% | +0.11% | 0.24x | 3.5 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.97133 | 52.513 | 57.975 | +0.51% | -0.10% | 0.50x | 1.2 | 2026-11-19T16:35:21.094794+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.716 | 22.546 | -0.15% | 0.53x |
| 2 | TRUST/USD | 73.412 | 0.05411 | -1.26% | 0.74x |
| 3 | BMT/USD | 71.231 | 0.02025 | +0.30% | 0.12x |
| 4 | SKR/USD | 71.228 | 0.010353 | -0.23% | 1.75x |
| 5 | PYTH/USD | 69.523 | 0.05611 | -0.32% | 0.35x |
| 6 | USELESS/USD | 65.939 | 0.10057 | -0.63% | 0.12x |
| 7 | AKT/USD | 65.483 | 0.5452 | +0.11% | 1.05x |
| 8 | BILL/USD | 64.450 | 0.00441 | +1.38% | 2.37x |
| 9 | HYPE/USD | 62.530 | 67.67 | +0.12% | 0.52x |
| 10 | ADA/USD | 59.767 | 0.152666 | +0.11% | 0.24x |
| 11 | XRP/USD | 57.975 | 0.97133 | -0.10% | 0.50x |
| 12 | TAO/USD | 56.987 | 193.3764 | +0.10% | 0.64x |

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

- Persisted scans: 814; predictions: 6912; observations: 492183.
- Matured sampled outcomes across 1/6/24/48h: 6899; gap abstentions: 15360. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44567640430 · **Generation:** 814 · **Legacy run:** 44567640430
**Main quote time:** 2026-11-19T16:35:29.741360+00:00 · **Legacy report time:** 2026-11-19T16:36:16.625774+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BILL/USD | 0.00441 | 85.00 | +1.38% | 2.37x | STRONG 87/100 | VERY_HIGH 79/100 | Watch |
| 2 | SKR/USD | 0.010353 | 77.53 | -0.23% | 1.75x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 22.546 | 74.30 | -0.15% | 0.53x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5452 | 66.53 | +0.11% | 1.05x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 5 | TRUST/USD | 0.05411 | 64.54 | -1.26% | 0.74x | WEAK 37/100 | EXTREME 92/100 | Do nothing |
| 6 | BMT/USD | 0.02025 | 63.93 | +0.30% | 0.12x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 7 | PYTH/USD | 0.05611 | 61.43 | -0.32% | 0.35x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 8 | HYPE/USD | 67.67 | 58.33 | +0.12% | 0.52x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | USELESS/USD | 0.10057 | 53.99 | -0.63% | 0.12x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | TAO/USD | 193.3764 | 53.84 | +0.10% | 0.64x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.152666 | 52.70 | +0.11% | 0.24x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.97133 | 52.51 | -0.10% | 0.50x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5458 | 71.42 | +0.11% | 1.05x | 3138 | MODERATE 66/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
