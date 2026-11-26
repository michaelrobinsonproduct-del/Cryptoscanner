# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T19:51:09.503916+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45886502519
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fcb663ea1e02d3cd93470db36cf195dfc16b00c9 (atomic ledger/results publication)
**Ledger generation:** 1905 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.3842 | 84.343 | 74.744 | +7.38% | -1.08% | 2.51x | 15.6 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | ADA/USD | 0.150419 | 81.037 | 75.196 | +3.19% | -0.21% | 1.69x | 4.3 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 3 | AKT/USD | 0.509 | 73.283 | 76.977 | +7.59% | +0.32% | 0.47x | 2.0 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04551 | 71.477 | 76.382 | +8.67% | -0.13% | 0.58x | 6.6 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | INJ/USD | 6.26 | 69.192 | 74.160 | +5.14% | +0.13% | 0.44x | 3.2 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ZRO/USD | 1.108 | 66.041 | 72.335 | +8.20% | +0.18% | 0.28x | 18.1 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | SOL/USD | 71.29 | 64.434 | 63.249 | +1.28% | -0.20% | 1.22x | 1.4 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LINK/USD | 9.27664 | 64.313 | 69.688 | +2.57% | +0.03% | 0.45x | 3.6 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1704.45 | 61.988 | 60.785 | +0.83% | +0.13% | 1.06x | 0.1 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 10 | WIF/USD | 0.1398 | 61.955 | 69.668 | +9.82% | -0.57% | 0.51x | 14.3 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.95338 | 60.357 | 67.519 | +1.80% | -0.10% | 0.33x | 0.1 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XBT/USD | 60638.9 | 58.463 | 58.126 | +0.45% | +0.17% | 0.95x | 0.0 | 2026-11-26T19:51:00.559692+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 76.977 | 0.509 | +0.32% | 0.47x |
| 2 | SKY/USD | 76.382 | 0.04551 | -0.13% | 0.58x |
| 3 | ADA/USD | 75.196 | 0.150419 | -0.21% | 1.69x |
| 4 | DRV/USD | 74.744 | 0.3842 | -1.08% | 2.51x |
| 5 | INJ/USD | 74.160 | 6.26 | +0.13% | 0.44x |
| 6 | ZRO/USD | 72.335 | 1.108 | +0.18% | 0.28x |
| 7 | LINK/USD | 69.688 | 9.27664 | +0.03% | 0.45x |
| 8 | WIF/USD | 69.668 | 0.1398 | -0.57% | 0.51x |
| 9 | XRP/USD | 67.519 | 0.95338 | -0.10% | 0.33x |
| 10 | SOL/USD | 63.249 | 71.29 | -0.20% | 1.22x |
| 11 | ETH/USD | 60.785 | 1704.45 | +0.13% | 1.06x |
| 12 | XBT/USD | 58.126 | 60638.9 | +0.17% | 0.95x |

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

- Persisted scans: 1905; predictions: 16595; observations: 1154029.
- Matured sampled outcomes across 1/6/24/48h: 36008; gap abstentions: 25201. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45886502519 · **Generation:** 1905 · **Legacy run:** 45886502519
**Main quote time:** 2026-11-26T19:51:09.503916+00:00 · **Legacy report time:** 2026-11-26T19:51:57.823738+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.3842 | 84.34 | -1.08% | 2.51x | MODERATE 67/100 | VERY_HIGH 71/100 | Watch |
| 2 | ADA/USD | 0.150419 | 81.04 | -0.21% | 1.69x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 3 | AKT/USD | 0.509 | 73.28 | +0.32% | 0.47x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 4 | SKY/USD | 0.04551 | 71.48 | -0.13% | 0.58x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 5 | INJ/USD | 6.26 | 69.19 | +0.13% | 0.44x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 6 | ZRO/USD | 1.108 | 66.04 | +0.18% | 0.28x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 7 | SOL/USD | 71.29 | 64.43 | -0.20% | 1.22x | WEAK 42/100 | HIGH 68/100 | Watch |
| 8 | LINK/USD | 9.27664 | 64.31 | +0.03% | 0.45x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1704.45 | 61.99 | +0.13% | 1.06x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 10 | WIF/USD | 0.1398 | 61.95 | -0.57% | 0.51x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 11 | XRP/USD | 0.95338 | 60.36 | -0.10% | 0.33x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XBT/USD | 60638.9 | 58.46 | +0.17% | 0.95x | MODERATE 49/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TREAD/USD | 1.232 | 76.20 | +0.98% | 1.59x | 3007 | MODERATE 68/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
