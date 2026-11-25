# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T17:37:49.747509+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45666210315
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4a036acb502a9669eefe531dc715741904121333 (atomic ledger/results publication)
**Ledger generation:** 1745 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.443 | 115.410 | 95.648 | +7.76% | +0.95% | 4.31x | 8.7 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.33905 | 95.311 | 79.038 | +7.88% | +0.25% | 2.57x | 8.9 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 41.62 | 80.790 | 66.993 | +1.88% | -0.24% | 4.11x | 2.4 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XPL/USD | 0.0474 | 75.628 | 70.822 | +7.73% | +0.64% | 1.16x | 21.1 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | INJ/USD | 5.907 | 56.895 | 42.915 | +1.01% | -0.20% | 12.64x | 5.1 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HBAR/USD | 0.05067 | 53.728 | 39.618 | +0.82% | -0.18% | 3.88x | 3.9 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 7 | STRK/USD | 0.03025 | 51.074 | 38.223 | +1.41% | -0.43% | 8.50x | 6.6 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 8 | CC/USD | 0.07542 | 49.683 | 35.148 | +0.49% | -0.09% | 2.56x | 5.3 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 9 | ASTER/USD | 0.49087 | 45.413 | 44.254 | +2.09% | -0.09% | 1.16x | 6.1 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | W/USD | 0.00812 | 45.199 | 30.199 | +0.74% | +0.00% | 3.73x | 12.3 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | XLM/USD | 0.124829 | 45.037 | 44.024 | +0.62% | -0.23% | 1.21x | 7.1 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | APT/USD | 0.3666 | 44.642 | 30.460 | +0.71% | -0.16% | 26.36x | 10.9 | 2026-11-25T17:37:43.178936+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.648 | 26.443 | +0.95% | 4.31x |
| 2 | DRV/USD | 79.038 | 0.33905 | +0.25% | 2.57x |
| 3 | XPL/USD | 70.822 | 0.0474 | +0.64% | 1.16x |
| 4 | LTC/USD | 66.993 | 41.62 | -0.24% | 4.11x |
| 5 | ASTER/USD | 44.254 | 0.49087 | -0.09% | 1.16x |
| 6 | XLM/USD | 44.024 | 0.124829 | -0.23% | 1.21x |
| 7 | INJ/USD | 42.915 | 5.907 | -0.20% | 12.64x |
| 8 | HBAR/USD | 39.618 | 0.05067 | -0.18% | 3.88x |
| 9 | STRK/USD | 38.223 | 0.03025 | -0.43% | 8.50x |
| 10 | CC/USD | 35.148 | 0.07542 | -0.09% | 2.56x |
| 11 | APT/USD | 30.460 | 0.3666 | -0.16% | 26.36x |
| 12 | W/USD | 30.199 | 0.00812 | +0.00% | 3.73x |

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

- Persisted scans: 1745; predictions: 14684; observations: 1057749.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22569. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45666210315 · **Generation:** 1745 · **Legacy run:** 45666210315
**Main quote time:** 2026-11-25T17:37:49.747509+00:00 · **Legacy report time:** 2026-11-25T17:39:06.226958+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.443 | 115.41 | +0.95% | 4.31x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33905 | 95.31 | +0.25% | 2.57x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD | 41.62 | 80.79 | -0.24% | 4.11x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | XPL/USD ⭐ | 0.0474 | 75.63 | +0.64% | 1.16x | STRONG 73/100 | VERY_HIGH 79/100 | Watch |
| 5 | INJ/USD | 5.907 | 56.90 | -0.20% | 12.64x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 6 | HBAR/USD | 0.05067 | 53.73 | -0.18% | 3.88x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 7 | STRK/USD | 0.03025 | 51.07 | -0.43% | 8.50x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 8 | CC/USD | 0.07542 | 49.68 | -0.09% | 2.56x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 9 | ASTER/USD | 0.49087 | 45.41 | -0.09% | 1.16x | WEAK 33/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | W/USD | 0.00812 | 45.20 | +0.00% | 3.73x | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |
| 11 | XLM/USD | 0.124829 | 45.04 | -0.23% | 1.21x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | APT/USD | 0.3666 | 44.64 | -0.16% | 26.36x | MODERATE 47/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.495 | 95.86 | +0.95% | 4.31x | 9970 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33894 | 82.14 | +0.25% | 2.57x | 10867 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0472 | 70.97 | +0.64% | 1.16x | 1989 | MODERATE 65/100 | EXTREME 89/100 | Do nothing |
| 4 | KAS/USD | 0.02671 | 56.23 | +0.15% | 2.41x | 2507 | MODERATE 68/100 | HIGH 66/100 | Watch |

**Same-run overlap:** VVV/USD, DRV/USD, XPL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
