# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T01:36:10.952851+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45736677968
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 663b7456fdb31f09ae16154694bee11014a27c25 (atomic ledger/results publication)
**Ledger generation:** 1794 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 30.167 | 68.807 | 76.482 | +3.33% | -0.13% | 0.30x | 3.6 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XRP/USD | 0.94319 | 61.446 | 59.478 | +0.71% | +0.01% | 1.19x | 1.0 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 3 | ADA/USD | 0.147054 | 59.547 | 59.704 | +0.88% | -0.04% | 1.00x | 2.9 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XBT/USD | 60607.3 | 59.474 | 57.760 | +0.40% | -0.01% | 1.17x | 0.0 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LTC/USD | 43.23 | 58.346 | 61.208 | +1.22% | +0.26% | 0.59x | 4.6 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AKT/USD | 0.4923 | 55.782 | 56.599 | +4.06% | +0.26% | 0.79x | 10.2 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6728 | 55.498 | 61.085 | +0.98% | -0.06% | 0.47x | 1.5 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ETH/USD | 1696.02 | 54.413 | 57.294 | +0.33% | -0.19% | 0.81x | 0.1 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | NEAR/USD | 3.0835 | 54.076 | 59.632 | +1.10% | -0.18% | 0.53x | 6.2 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | CC/USD | 0.07859 | 53.957 | 45.138 | +1.47% | +0.85% | 1.46x | 1.3 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 11 | TAO/USD | 183.3081 | 53.905 | 58.219 | +0.94% | +0.19% | 0.47x | 6.8 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 70.76 | 53.800 | 57.973 | +0.53% | -0.13% | 0.65x | 1.4 | 2026-11-26T01:36:02.406174+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 76.482 | 30.167 | -0.13% | 0.30x |
| 2 | LTC/USD | 61.208 | 43.23 | +0.26% | 0.59x |
| 3 | SUI/USD | 61.085 | 0.6728 | -0.06% | 0.47x |
| 4 | ADA/USD | 59.704 | 0.147054 | -0.04% | 1.00x |
| 5 | NEAR/USD | 59.632 | 3.0835 | -0.18% | 0.53x |
| 6 | XRP/USD | 59.478 | 0.94319 | +0.01% | 1.19x |
| 7 | TAO/USD | 58.219 | 183.3081 | +0.19% | 0.47x |
| 8 | SOL/USD | 57.973 | 70.76 | -0.13% | 0.65x |
| 9 | XBT/USD | 57.760 | 60607.3 | -0.01% | 1.17x |
| 10 | ETH/USD | 57.294 | 1696.02 | -0.19% | 0.81x |
| 11 | AKT/USD | 56.599 | 0.4923 | +0.26% | 0.79x |
| 12 | CC/USD | 45.138 | 0.07859 | +0.85% | 1.46x |

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

- Persisted scans: 1794; predictions: 15263; observations: 1087590.
- Matured sampled outcomes across 1/6/24/48h: 33176; gap abstentions: 23594. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45736677968 · **Generation:** 1794 · **Legacy run:** 45736677968
**Main quote time:** 2026-11-26T01:36:10.952851+00:00 · **Legacy report time:** 2026-11-26T01:37:07.867828+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 30.167 | 68.81 | -0.13% | 0.30x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 2 | XRP/USD | 0.94319 | 61.45 | +0.01% | 1.19x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 3 | ADA/USD | 0.147054 | 59.55 | -0.04% | 1.00x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | XBT/USD | 60607.3 | 59.47 | -0.01% | 1.17x | WEAK 40/100 | HIGH 68/100 | Watch |
| 5 | LTC/USD | 43.23 | 58.35 | +0.26% | 0.59x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | AKT/USD | 0.4923 | 55.78 | +0.26% | 0.79x | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |
| 7 | SUI/USD | 0.6728 | 55.50 | -0.06% | 0.47x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ETH/USD | 1696.02 | 54.41 | -0.19% | 0.81x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 9 | NEAR/USD | 3.0835 | 54.08 | -0.18% | 0.53x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | CC/USD | 0.07859 | 53.96 | +0.85% | 1.46x | STRONG 72/100 | HIGH 60/100 | Watch |
| 11 | TAO/USD | 183.3081 | 53.91 | +0.19% | 0.47x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 70.76 | 53.80 | -0.13% | 0.65x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD | 0.01712 | 59.84 | +0.18% | 1.04x | 1417 | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
