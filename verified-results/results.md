# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T12:31:43.502043+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45174810735
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 62891a1f6700cb5ee024ef2a649c8acfd5c9afcd (atomic ledger/results publication)
**Ledger generation:** 1430 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.35 | 102.877 | 87.558 | +9.00% | +0.62% | 2.22x | 9.6 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UAI/USD | 0.03153 | 90.858 | 69.464 | +6.63% | +1.28% | 15.73x | 12.7 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | KAS/USD | 0.02722 | 83.553 | 68.736 | +5.46% | -0.04% | 5.94x | 7.4 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6701 | 82.094 | 68.878 | +2.20% | -0.36% | 6.56x | 3.0 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.08307 | 73.289 | 76.374 | +10.13% | -0.94% | 1.16x | 8.4 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | XLM/USD | 0.128312 | 70.905 | 57.038 | +0.61% | -0.18% | 2.48x | 2.3 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93789 | 69.309 | 62.651 | +1.12% | -0.03% | 1.68x | 0.3 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SOL/USD | 72.17 | 66.384 | 69.570 | +2.18% | -0.14% | 0.75x | 1.4 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | BLUR/USD | 0.00802 | 65.319 | 63.503 | +8.53% | +1.13% | 0.61x | 24.9 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | NEAR/USD | 2.9896 | 60.918 | 53.677 | +0.26% | -0.20% | 1.82x | 6.4 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XMR/USD | 502.63 | 57.177 | 65.059 | +1.81% | -0.07% | 0.25x | 5.2 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | INJ/USD | 6.407 | 55.032 | 59.701 | +2.87% | -0.47% | 0.77x | 1.6 | 2026-11-23T12:31:36.804646+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 87.558 | 156.35 | +0.62% | 2.22x |
| 2 | ALGO/USD | 76.374 | 0.08307 | -0.94% | 1.16x |
| 3 | SOL/USD | 69.570 | 72.17 | -0.14% | 0.75x |
| 4 | UAI/USD | 69.464 | 0.03153 | +1.28% | 15.73x |
| 5 | SUI/USD | 68.878 | 0.6701 | -0.36% | 6.56x |
| 6 | KAS/USD | 68.736 | 0.02722 | -0.04% | 5.94x |
| 7 | XMR/USD | 65.059 | 502.63 | -0.07% | 0.25x |
| 8 | BLUR/USD | 63.503 | 0.00802 | +1.13% | 0.61x |
| 9 | XRP/USD | 62.651 | 0.93789 | -0.03% | 1.68x |
| 10 | INJ/USD | 59.701 | 6.407 | -0.47% | 0.77x |
| 11 | XLM/USD | 57.038 | 0.128312 | -0.18% | 2.48x |
| 12 | NEAR/USD | 53.677 | 2.9896 | -0.20% | 1.82x |

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

- Persisted scans: 1430; predictions: 11927; observations: 865973.
- Matured sampled outcomes across 1/6/24/48h: 19931; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45174810735 · **Generation:** 1430 · **Legacy run:** 45174810735
**Main quote time:** 2026-11-23T12:31:43.502043+00:00 · **Legacy report time:** 2026-11-23T12:32:49.998258+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.35 | 102.88 | +0.62% | 2.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UAI/USD ⭐ | 0.03153 | 90.86 | +1.28% | 15.73x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 3 | KAS/USD | 0.02722 | 83.55 | -0.04% | 5.94x | STRONG 72/100 | HIGH 66/100 | Watch |
| 4 | SUI/USD | 0.6701 | 82.09 | -0.36% | 6.56x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | ALGO/USD | 0.08307 | 73.29 | -0.94% | 1.16x | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |
| 6 | XLM/USD | 0.128312 | 70.90 | -0.18% | 2.48x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.93789 | 69.31 | -0.03% | 1.68x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | SOL/USD | 72.17 | 66.38 | -0.14% | 0.75x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | BLUR/USD | 0.00802 | 65.32 | +1.13% | 0.61x | MODERATE 53/100 | EXTREME 94/100 | Do nothing |
| 10 | NEAR/USD | 2.9896 | 60.92 | -0.20% | 1.82x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 11 | XMR/USD | 502.63 | 57.18 | -0.07% | 0.25x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | INJ/USD | 6.407 | 55.03 | -0.47% | 0.77x | WEAK 33/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.38 | 88.01 | +0.62% | 2.22x | 5852 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UAI/USD ⭐ | 0.0315 | 75.96 | +1.28% | 15.73x | 1877 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | ONDO/USD | 0.29229 | 75.16 | +0.24% | 11.90x | 3926 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 4 | XPL/USD | 0.0467 | 62.80 | +0.22% | 1.10x | 1439 | MODERATE 56/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** QNT/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
