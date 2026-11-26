# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T04:36:54.644867+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45756082919
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7ab21536a7150ab62e57aeaead1bc5b0fdd09d5d (atomic ledger/results publication)
**Ledger generation:** 1813 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.95619 | 83.086 | 69.620 | +2.10% | -0.23% | 2.46x | 0.1 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ADA/USD | 0.14924 | 81.672 | 70.223 | +2.38% | +0.31% | 1.99x | 2.9 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 184.3033 | 77.822 | 62.003 | +1.49% | +0.16% | 3.65x | 6.9 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0568888 | 77.253 | 62.091 | +1.66% | +0.03% | 8.79x | 0.0 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LTC/USD | 43.89 | 76.054 | 73.200 | +2.76% | +0.00% | 1.29x | 2.3 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 6 | BABY/USD | 0.00945 | 71.350 | 70.744 | +8.50% | +0.95% | 0.59x | 10.6 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | XBT/USD | 60928.6 | 70.892 | 61.485 | +0.93% | +0.11% | 1.88x | 0.0 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SYRUP/USD | 0.07218 | 68.595 | 69.506 | +8.92% | +1.16% | 0.33x | 15.3 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | SEI/USD | 0.03513 | 63.623 | 67.256 | +5.46% | +0.00% | 0.64x | 5.7 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | LINK/USD | 9.23599 | 62.628 | 65.747 | +2.12% | +0.18% | 0.60x | 3.9 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6731 | 60.722 | 61.400 | +1.02% | +0.09% | 0.89x | 1.5 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.579e-06 | 59.595 | 63.143 | +2.73% | +0.28% | 0.50x | 2.8 | 2026-11-26T04:36:46.245504+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 73.200 | 43.89 | +0.00% | 1.29x |
| 2 | BABY/USD | 70.744 | 0.00945 | +0.95% | 0.59x |
| 3 | ADA/USD | 70.223 | 0.14924 | +0.31% | 1.99x |
| 4 | XRP/USD | 69.620 | 0.95619 | -0.23% | 2.46x |
| 5 | SYRUP/USD | 69.506 | 0.07218 | +1.16% | 0.33x |
| 6 | SEI/USD | 67.256 | 0.03513 | +0.00% | 0.64x |
| 7 | LINK/USD | 65.747 | 9.23599 | +0.18% | 0.60x |
| 8 | PEPE/USD | 63.143 | 3.579e-06 | +0.28% | 0.50x |
| 9 | XDG/USD | 62.091 | 0.0568888 | +0.03% | 8.79x |
| 10 | TAO/USD | 62.003 | 184.3033 | +0.16% | 3.65x |
| 11 | XBT/USD | 61.485 | 60928.6 | +0.11% | 1.88x |
| 12 | SUI/USD | 61.400 | 0.6731 | +0.09% | 0.89x |

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

- Persisted scans: 1813; predictions: 15491; observations: 1099161.
- Matured sampled outcomes across 1/6/24/48h: 33623; gap abstentions: 23872. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45756082919 · **Generation:** 1813 · **Legacy run:** 45756082919
**Main quote time:** 2026-11-26T04:36:54.644867+00:00 · **Legacy report time:** 2026-11-26T04:38:14.049119+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.95619 | 83.09 | -0.23% | 2.46x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | ADA/USD ⭐ | 0.14924 | 81.67 | +0.31% | 1.99x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD | 184.3033 | 77.82 | +0.16% | 3.65x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | XDG/USD | 0.0568888 | 77.25 | +0.03% | 8.79x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | LTC/USD | 43.89 | 76.05 | +0.00% | 1.29x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 6 | BABY/USD | 0.00945 | 71.35 | +0.95% | 0.59x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 7 | XBT/USD ⭐ | 60928.6 | 70.89 | +0.11% | 1.88x | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | SYRUP/USD | 0.07218 | 68.59 | +1.16% | 0.33x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 9 | SEI/USD | 0.03513 | 63.62 | +0.00% | 0.64x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 10 | LINK/USD | 9.23599 | 62.63 | +0.18% | 0.60x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | SUI/USD | 0.6731 | 60.72 | +0.09% | 0.89x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 12 | PEPE/USD | 3.579e-06 | 59.59 | +0.28% | 0.50x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.14924 | 78.35 | +0.31% | 1.99x | 11486 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 60909.5 | 66.60 | +0.11% | 1.88x | 229274 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
