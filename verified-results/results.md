# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:55:30.651629+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44571354021
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** bc046dbb7a929d54c32a7443fbd7be84c1d80efd (atomic ledger/results publication)
**Ledger generation:** 818 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.779e-05 | 85.005 | 77.424 | +9.76% | -1.48% | 8.95x | 8.3 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.021916 | 81.854 | 75.109 | +6.36% | +2.19% | 0.58x | 7.8 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | TRUST/USD | 0.05503 | 73.213 | 64.405 | +11.85% | +0.75% | 1.50x | 23.6 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97052 | 68.959 | 56.512 | +0.43% | -0.51% | 3.44x | 3.0 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 5 | BMT/USD | 0.02051 | 68.188 | 71.297 | +8.63% | +1.13% | 0.12x | 9.8 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | VVV/USD | 22.505 | 66.963 | 77.716 | +3.85% | -0.64% | 0.24x | 8.4 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ADA/USD | 0.15228 | 64.002 | 57.515 | +0.68% | -0.77% | 2.03x | 4.5 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SKR/USD | 0.010337 | 62.413 | 70.727 | +7.31% | -0.28% | 0.31x | 10.7 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | INJ/USD | 7.122 | 59.890 | 53.950 | +2.02% | -0.15% | 1.67x | 7.0 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 10 | HYPE/USD | 67.62 | 56.611 | 62.006 | +1.11% | -0.54% | 0.73x | 1.5 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | AKT/USD | 0.5432 | 53.446 | 61.838 | +4.86% | -0.64% | 0.48x | 7.4 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | WEAK 32/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | PYTH/USD | 0.05572 | 52.065 | 62.428 | +5.61% | -1.10% | 0.51x | 17.9 | 2026-11-19T16:55:22.912298+00:00 | Not calibrated | WEAK 26/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.716 | 22.505 | -0.64% | 0.24x |
| 2 | LUNA/USD | 77.424 | 4.779e-05 | -1.48% | 8.95x |
| 3 | SENT/USD | 75.109 | 0.021916 | +2.19% | 0.58x |
| 4 | BMT/USD | 71.297 | 0.02051 | +1.13% | 0.12x |
| 5 | SKR/USD | 70.727 | 0.010337 | -0.28% | 0.31x |
| 6 | TRUST/USD | 64.405 | 0.05503 | +0.75% | 1.50x |
| 7 | PYTH/USD | 62.428 | 0.05572 | -1.10% | 0.51x |
| 8 | HYPE/USD | 62.006 | 67.62 | -0.54% | 0.73x |
| 9 | AKT/USD | 61.838 | 0.5432 | -0.64% | 0.48x |
| 10 | ADA/USD | 57.515 | 0.15228 | -0.77% | 2.03x |
| 11 | XRP/USD | 56.512 | 0.97052 | -0.51% | 3.44x |
| 12 | INJ/USD | 53.950 | 7.122 | -0.15% | 1.67x |

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

- Persisted scans: 818; predictions: 6960; observations: 494575.
- Matured sampled outcomes across 1/6/24/48h: 6935; gap abstentions: 15399. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44571354021 · **Generation:** 818 · **Legacy run:** 44571354021
**Main quote time:** 2026-11-19T16:55:30.651629+00:00 · **Legacy report time:** 2026-11-19T16:56:16.394048+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.779e-05 | 85.00 | -1.48% | 8.95x | STRONG 73/100 | VERY_HIGH 70/100 | Do nothing |
| 2 | SENT/USD | 0.021916 | 81.85 | +2.19% | 0.58x | STRONG 71/100 | VERY_HIGH 75/100 | Watch |
| 3 | TRUST/USD ⭐ | 0.05503 | 73.21 | +0.75% | 1.50x | STRONG 82/100 | VERY_HIGH 79/100 | Watch |
| 4 | XRP/USD | 0.97052 | 68.96 | -0.51% | 3.44x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 5 | BMT/USD | 0.02051 | 68.19 | +1.13% | 0.12x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 6 | VVV/USD | 22.505 | 66.96 | -0.64% | 0.24x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 7 | ADA/USD | 0.15228 | 64.00 | -0.77% | 2.03x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | SKR/USD | 0.010337 | 62.41 | -0.28% | 0.31x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 9 | INJ/USD | 7.122 | 59.89 | -0.15% | 1.67x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 10 | HYPE/USD | 67.62 | 56.61 | -0.54% | 0.73x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | AKT/USD | 0.5432 | 53.45 | -0.64% | 0.48x | WEAK 32/100 | EXTREME 88/100 | Do nothing |
| 12 | PYTH/USD | 0.05572 | 52.06 | -1.10% | 0.51x | WEAK 26/100 | EXTREME 91/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.05512 | 70.02 | +0.75% | 1.50x | 2041 | STRONG 80/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** TRUST/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
