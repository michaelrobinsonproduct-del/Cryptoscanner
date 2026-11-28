# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T04:27:19.529005+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46107394173
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f8024292315501f78acaf3f68c356d3b67e6ace7 (atomic ledger/results publication)
**Ledger generation:** 2105 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.29 | 78.666 | 63.043 | +1.26% | +0.12% | 5.26x | 1.6 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0491 | 61.678 | 61.019 | +1.02% | -0.04% | 1.09x | 2.3 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SEI/USD | 0.03898 | 61.423 | 38.061 | +1.48% | +1.67% | 19.04x | 10.3 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 4 | ZEC/USD | 749.18 | 60.702 | 67.588 | +1.99% | -0.01% | 0.31x | 2.7 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | VVV/USD | 26.134 | 55.762 | 51.571 | +1.50% | +1.07% | 0.88x | 10.3 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SENT/USD | 0.024588 | 52.901 | 54.851 | +3.69% | +0.10% | 0.76x | 3.7 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | BCH/USD | 209.49 | 36.278 | 43.173 | +1.20% | +0.15% | 0.23x | 3.8 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | SYRUP/USD | 0.0698 | 22.720 | 24.476 | +0.34% | +0.13% | 0.76x | 18.6 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2749 | 21.268 | 29.243 | +0.92% | +0.26% | 0.07x | 18.2 | 2026-11-28T04:27:12.844248+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 67.588 | 749.18 | -0.01% | 0.31x |
| 2 | HYPE/USD | 63.043 | 64.29 | +0.12% | 5.26x |
| 3 | NEAR/USD | 61.019 | 3.0491 | -0.04% | 1.09x |
| 4 | SENT/USD | 54.851 | 0.024588 | +0.10% | 0.76x |
| 5 | VVV/USD | 51.571 | 26.134 | +1.07% | 0.88x |
| 6 | BCH/USD | 43.173 | 209.49 | +0.15% | 0.23x |
| 7 | SEI/USD | 38.061 | 0.03898 | +1.67% | 19.04x |
| 8 | SPX/USD | 29.243 | 0.2749 | +0.26% | 0.07x |
| 9 | SYRUP/USD | 24.476 | 0.0698 | +0.13% | 0.76x |

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

- Persisted scans: 2105; predictions: 18904; observations: 1274676.
- Matured sampled outcomes across 1/6/24/48h: 43838; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46107394173 · **Generation:** 2105 · **Legacy run:** 46107394173
**Main quote time:** 2026-11-28T04:27:19.529005+00:00 · **Legacy report time:** 2026-11-28T04:27:56.267254+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.29 | 78.67 | +0.12% | 5.26x | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 3.0491 | 61.68 | -0.04% | 1.09x | WEAK 41/100 | HIGH 68/100 | Watch |
| 3 | SEI/USD ⭐ | 0.03898 | 61.42 | +1.67% | 19.04x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 4 | ZEC/USD | 749.18 | 60.70 | -0.01% | 0.31x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 5 | VVV/USD | 26.134 | 55.76 | +1.07% | 0.88x | MODERATE 53/100 | HIGH 68/100 | Watch |
| 6 | SENT/USD | 0.024588 | 52.90 | +0.10% | 0.76x | MODERATE 46/100 | VERY_HIGH 74/100 | Watch |
| 7 | BCH/USD | 209.49 | 36.28 | +0.15% | 0.23x | WEAK 38/100 | VERY_HIGH 75/100 | Watch |
| 8 | SYRUP/USD | 0.0698 | 22.72 | +0.13% | 0.76x | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | SPX/USD | 0.2749 | 21.27 | +0.26% | 0.07x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.29 | 72.38 | +0.12% | 5.26x | 17096 | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | SEI/USD ⭐ | 0.03895 | 53.57 | +1.67% | 19.04x | 4101 | STRONG 92/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** HYPE/USD, SEI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
