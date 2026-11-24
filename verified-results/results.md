# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:31:53.267598+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45449155537
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ab5b2e7e55803f41843cf1be2fa49d86e791d26e (atomic ledger/results publication)
**Ledger generation:** 1604 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.215 | 74.662 | 72.393 | +3.14% | +0.64% | 0.91x | 9.1 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XMR/USD | 499.91 | 71.647 | 70.205 | +2.86% | +0.43% | 0.93x | 9.6 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.705e-05 | 70.255 | 56.315 | +8.24% | -0.21% | 6.28x | 40.4 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 95/100 | Do nothing | WATCH |
| 4 | GBP/USD | 1.31138 | 51.762 | 59.214 | +0.62% | +0.03% | 0.24x | 0.3 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.0162 | 48.878 | 52.258 | +3.51% | -0.37% | 0.85x | 6.2 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | BAT/USD | 0.07746 | 41.455 | 33.896 | +0.38% | +0.17% | 1.67x | 2.6 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | MODERATE 56/100 | HIGH 60/100 | Watch | WATCH |
| 7 | DBR/USD | 0.01369 | 34.846 | 27.323 | +2.01% | -0.80% | 2.15x | 36.6 | 2026-11-24T17:31:49.566457+00:00 | Not calibrated | WEAK 32/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.393 | 25.215 | +0.64% | 0.91x |
| 2 | XMR/USD | 70.205 | 499.91 | +0.43% | 0.93x |
| 3 | GBP/USD | 59.214 | 1.31138 | +0.03% | 0.24x |
| 4 | LUNA/USD | 56.315 | 4.705e-05 | -0.21% | 6.28x |
| 5 | 2Z/USD | 52.258 | 0.0162 | -0.37% | 0.85x |
| 6 | BAT/USD | 33.896 | 0.07746 | +0.17% | 1.67x |
| 7 | DBR/USD | 27.323 | 0.01369 | -0.80% | 2.15x |

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

- Persisted scans: 1604; predictions: 13782; observations: 971928.
- Matured sampled outcomes across 1/6/24/48h: 27668; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45449155537 · **Generation:** 1604 · **Legacy run:** 45449155537
**Main quote time:** 2026-11-24T17:31:53.267598+00:00 · **Legacy report time:** 2026-11-24T17:33:06.696626+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.215 | 74.66 | +0.64% | 0.91x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD | 499.91 | 71.65 | +0.43% | 0.93x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 3 | LUNA/USD | 4.705e-05 | 70.25 | -0.21% | 6.28x | MODERATE 50/100 | EXTREME 95/100 | Do nothing |
| 4 | GBP/USD | 1.31138 | 51.76 | +0.03% | 0.24x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 5 | 2Z/USD | 0.0162 | 48.88 | -0.37% | 0.85x | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | BAT/USD ⭐ | 0.07746 | 41.45 | +0.17% | 1.67x | MODERATE 66/100 | HIGH 60/100 | Watch |
| 7 | DBR/USD | 0.01369 | 34.85 | -0.80% | 2.15x | WEAK 32/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEUS/USD | 0.00473 | 75.62 | +0.43% | 1.88x | 2685 | MODERATE 68/100 | EXTREME 89/100 | Do nothing |
| 2 | BAT/USD ⭐ | 0.07744 | 30.92 | +0.17% | 1.67x | 4112 | MODERATE 55/100 | HIGH 66/100 | Watch |

**Same-run overlap:** BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
