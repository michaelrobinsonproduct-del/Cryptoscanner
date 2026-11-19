# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T14:15:29.749254+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44541619001
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 0dacbf96313d8dd28b026b15c48566e09f5ab648 (atomic ledger/results publication)
**Ledger generation:** 790 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.14 | 109.693 | 96.759 | +6.78% | -0.41% | 5.46x | 6.5 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002749 | 95.555 | 80.919 | +5.89% | -0.07% | 4.85x | 10.9 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 3 | HYPE/USD | 68.6 | 86.328 | 72.273 | +2.57% | -0.19% | 4.57x | 1.5 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TAO/USD | 199.2274 | 84.948 | 78.948 | +3.79% | -0.43% | 1.82x | 5.1 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010343 | 84.497 | 71.150 | +7.37% | +0.86% | 1.91x | 9.7 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Consider small entry | WATCH |
| 6 | XBT/USD | 63867.1 | 77.944 | 64.801 | +1.40% | -0.16% | 2.39x | 0.0 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.059567 | 75.654 | 61.672 | +1.47% | -0.20% | 4.06x | 0.1 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZEC/USD | 944.79 | 73.420 | 78.725 | +3.60% | -0.17% | 0.55x | 3.0 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ADA/USD | 0.155189 | 71.080 | 71.664 | +2.60% | -0.26% | 1.07x | 3.1 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.935e-06 | 70.460 | 73.366 | +5.05% | -0.86% | 1.14x | 5.1 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XRP/USD | 0.9899 | 67.638 | 71.994 | +2.43% | -0.21% | 0.67x | 0.1 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | LINK/USD | 9.24094 | 64.901 | 67.389 | +1.85% | +0.04% | 0.73x | 1.2 | 2026-11-19T14:15:21.649363+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.759 | 23.14 | -0.41% | 5.46x |
| 2 | PUMP/USD | 80.919 | 0.002749 | -0.07% | 4.85x |
| 3 | TAO/USD | 78.948 | 199.2274 | -0.43% | 1.82x |
| 4 | ZEC/USD | 78.725 | 944.79 | -0.17% | 0.55x |
| 5 | PEPE/USD | 73.366 | 3.935e-06 | -0.86% | 1.14x |
| 6 | HYPE/USD | 72.273 | 68.6 | -0.19% | 4.57x |
| 7 | XRP/USD | 71.994 | 0.9899 | -0.21% | 0.67x |
| 8 | ADA/USD | 71.664 | 0.155189 | -0.26% | 1.07x |
| 9 | SKR/USD | 71.150 | 0.010343 | +0.86% | 1.91x |
| 10 | LINK/USD | 67.389 | 9.24094 | +0.04% | 0.73x |
| 11 | XBT/USD | 64.801 | 63867.1 | -0.16% | 2.39x |
| 12 | XDG/USD | 61.672 | 0.059567 | -0.20% | 4.06x |

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

- Persisted scans: 790; predictions: 6624; observations: 477888.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 15052. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44541619001 · **Generation:** 790 · **Legacy run:** 44541619001
**Main quote time:** 2026-11-19T14:15:29.749254+00:00 · **Legacy report time:** 2026-11-19T14:16:09.429413+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.14 | 109.69 | -0.41% | 5.46x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | PUMP/USD | 0.002749 | 95.56 | -0.07% | 4.85x | STRONG 73/100 | HIGH 67/100 | Watch |
| 3 | HYPE/USD | 68.6 | 86.33 | -0.19% | 4.57x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | TAO/USD | 199.2274 | 84.95 | -0.43% | 1.82x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 5 | SKR/USD | 0.010343 | 84.50 | +0.86% | 1.91x | STRONG 87/100 | HIGH 67/100 | Consider small entry |
| 6 | XBT/USD | 63867.1 | 77.94 | -0.16% | 2.39x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.059567 | 75.65 | -0.20% | 4.06x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | ZEC/USD | 944.79 | 73.42 | -0.17% | 0.55x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 9 | ADA/USD | 0.155189 | 71.08 | -0.26% | 1.07x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 10 | PEPE/USD | 3.935e-06 | 70.46 | -0.86% | 1.14x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 11 | XRP/USD | 0.9899 | 67.64 | -0.21% | 0.67x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 12 | LINK/USD | 9.24094 | 64.90 | +0.04% | 0.73x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.100883 | 78.47 | +0.54% | 1.44x | 6562 | STRONG 84/100 | HIGH 60/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
