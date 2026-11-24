# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T04:03:01.691911+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45323246319
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 534420fae6d473db9de2b1cefc4dc153d92d765d (atomic ledger/results publication)
**Ledger generation:** 1522 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.736 | 75.441 | 59.200 | +1.18% | +1.20% | 2.02x | 8.1 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01234 | 74.330 | 76.450 | +7.12% | +0.89% | 0.34x | 16.2 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | AI/USD | 0.01621 | 65.310 | 69.997 | +6.43% | +0.13% | 0.47x | 12.3 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.469e-06 | 59.816 | 57.596 | +1.37% | +0.52% | 0.96x | 2.9 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94763 | 59.448 | 61.087 | +0.88% | +0.39% | 0.64x | 0.1 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | BABY/USD | 0.00878 | 58.581 | 48.451 | +3.29% | +0.34% | 1.84x | 11.4 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XMR/USD | 488.34 | 51.306 | 54.856 | +0.48% | +0.44% | 0.42x | 7.0 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | LINK/USD | 9.03528 | 48.918 | 56.008 | +0.34% | +0.48% | 0.05x | 2.7 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | AAVE/USD | 97.47 | 43.613 | 49.180 | +0.43% | +0.85% | 0.02x | 4.1 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | WLD/USD | 0.2401 | 33.649 | 36.221 | +0.76% | +0.97% | 0.26x | 8.3 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | XTZ/USD | 0.21496 | 32.170 | 31.276 | +0.99% | +0.59% | 0.79x | 13.0 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 12 | XDC/USD | 0.02612 | 23.252 | 31.462 | +0.54% | +0.04% | 0.16x | 15.3 | 2026-11-24T04:02:53.506853+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.450 | 0.01234 | +0.89% | 0.34x |
| 2 | AI/USD | 69.997 | 0.01621 | +0.13% | 0.47x |
| 3 | XRP/USD | 61.087 | 0.94763 | +0.39% | 0.64x |
| 4 | VVV/USD | 59.200 | 24.736 | +1.20% | 2.02x |
| 5 | PEPE/USD | 57.596 | 3.469e-06 | +0.52% | 0.96x |
| 6 | LINK/USD | 56.008 | 9.03528 | +0.48% | 0.05x |
| 7 | XMR/USD | 54.856 | 488.34 | +0.44% | 0.42x |
| 8 | AAVE/USD | 49.180 | 97.47 | +0.85% | 0.02x |
| 9 | BABY/USD | 48.451 | 0.00878 | +0.34% | 1.84x |
| 10 | WLD/USD | 36.221 | 0.2401 | +0.97% | 0.26x |
| 11 | XDC/USD | 31.462 | 0.02612 | +0.04% | 0.16x |
| 12 | XTZ/USD | 31.276 | 0.21496 | +0.59% | 0.79x |

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

- Persisted scans: 1522; predictions: 12997; observations: 921996.
- Matured sampled outcomes across 1/6/24/48h: 24195; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45323246319 · **Generation:** 1522 · **Legacy run:** 45323246319
**Main quote time:** 2026-11-24T04:03:01.691911+00:00 · **Legacy report time:** 2026-11-24T04:04:14.774447+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.736 | 75.44 | +1.20% | 2.02x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD | 0.01234 | 74.33 | +0.89% | 0.34x | MODERATE 62/100 | VERY_HIGH 76/100 | Watch |
| 3 | AI/USD | 0.01621 | 65.31 | +0.13% | 0.47x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 4 | PEPE/USD | 3.469e-06 | 59.82 | +0.52% | 0.96x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | XRP/USD | 0.94763 | 59.45 | +0.39% | 0.64x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 6 | BABY/USD ⭐ | 0.00878 | 58.58 | +0.34% | 1.84x | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 7 | XMR/USD | 488.34 | 51.31 | +0.44% | 0.42x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | LINK/USD | 9.03528 | 48.92 | +0.48% | 0.05x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | AAVE/USD | 97.47 | 43.61 | +0.85% | 0.02x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 10 | WLD/USD | 0.2401 | 33.65 | +0.97% | 0.26x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 11 | XTZ/USD | 0.21496 | 32.17 | +0.59% | 0.79x | WEAK 41/100 | VERY_HIGH 80/100 | Watch |
| 12 | XDC/USD | 0.02612 | 23.25 | +0.04% | 0.16x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00878 | 65.37 | +0.34% | 1.84x | 2495 | STRONG 83/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 24.674 | 65.12 | +1.20% | 2.02x | 13655 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | BAT/USD | 0.07841 | 44.87 | +0.50% | 1.24x | 3045 | MODERATE 47/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** VVV/USD, BABY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
