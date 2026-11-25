# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T06:37:24.446500+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45561621026
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4da14cc8400e696a16ceed4d215488aea4684d2e (atomic ledger/results publication)
**Ledger generation:** 1682 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01039 | 114.305 | 84.365 | +9.71% | +2.99% | 2.51x | 19.2 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.33711 | 89.727 | 74.190 | +7.26% | +1.66% | 1.72x | 16.3 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | BABY/USD | 0.00893 | 75.123 | 71.705 | +8.11% | +0.11% | 1.29x | 11.2 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.522e-06 | 66.865 | 53.709 | +2.00% | -0.37% | 3.20x | 8.5 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PENGU/USD | 0.004264 | 55.743 | 40.508 | +1.14% | +0.05% | 5.47x | 2.3 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.07217 | 55.017 | 50.647 | +3.59% | +0.66% | 1.11x | 12.5 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | VVV/USD | 24.954 | 52.421 | 61.881 | +1.70% | -1.09% | 0.60x | 10.0 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.4663 | 50.869 | 32.734 | +0.30% | +0.63% | 2.50x | 2.1 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 9 | TRX/USD | 0.308626 | 35.621 | 42.742 | +0.29% | +0.05% | 0.26x | 0.9 | 2026-11-25T06:37:16.810102+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 84.365 | 0.01039 | +2.99% | 2.51x |
| 2 | DRV/USD | 74.190 | 0.33711 | +1.66% | 1.72x |
| 3 | BABY/USD | 71.705 | 0.00893 | +0.11% | 1.29x |
| 4 | VVV/USD | 61.881 | 24.954 | -1.09% | 0.60x |
| 5 | PEPE/USD | 53.709 | 3.522e-06 | -0.37% | 3.20x |
| 6 | SYRUP/USD | 50.647 | 0.07217 | +0.66% | 1.11x |
| 7 | TRX/USD | 42.742 | 0.308626 | +0.05% | 0.26x |
| 8 | PENGU/USD | 40.508 | 0.004264 | +0.05% | 5.47x |
| 9 | AKT/USD | 32.734 | 0.4663 | +0.63% | 2.50x |

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

- Persisted scans: 1682; predictions: 14282; observations: 1019429.
- Matured sampled outcomes across 1/6/24/48h: 30452; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45561621026 · **Generation:** 1682 · **Legacy run:** 45561621026
**Main quote time:** 2026-11-25T06:37:24.446500+00:00 · **Legacy report time:** 2026-11-25T06:38:17.806730+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01039 | 114.31 | +2.99% | 2.51x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33711 | 89.73 | +1.66% | 1.72x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 3 | BABY/USD ⭐ | 0.00893 | 75.12 | +0.11% | 1.29x | MODERATE 68/100 | HIGH 66/100 | Watch |
| 4 | PEPE/USD | 3.522e-06 | 66.86 | -0.37% | 3.20x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | PENGU/USD | 0.004264 | 55.74 | +0.05% | 5.47x | STRONG 73/100 | HIGH 60/100 | Watch |
| 6 | SYRUP/USD ⭐ | 0.07217 | 55.02 | +0.66% | 1.11x | MODERATE 68/100 | VERY_HIGH 73/100 | Watch |
| 7 | VVV/USD | 24.954 | 52.42 | -1.09% | 0.60x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | AKT/USD | 0.4663 | 50.87 | +0.63% | 2.50x | STRONG 80/100 | HIGH 60/100 | Watch |
| 9 | TRX/USD | 0.308626 | 35.62 | +0.05% | 0.26x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01043 | 95.47 | +2.99% | 2.51x | 18500 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.3377 | 82.30 | +1.66% | 1.72x | 9046 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 3 | BABY/USD ⭐ | 0.00893 | 72.87 | +0.11% | 1.29x | 4003 | MODERATE 66/100 | HIGH 66/100 | Watch |
| 4 | SYRUP/USD ⭐ | 0.07223 | 69.56 | +0.66% | 1.11x | 3463 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** MON/USD, DRV/USD, BABY/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
