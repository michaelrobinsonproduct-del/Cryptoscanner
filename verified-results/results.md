# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T13:11:01.531552+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45826420740
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6a0f574910f20c566f04d8bb20825d357169460e (atomic ledger/results publication)
**Ledger generation:** 1865 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 151.4 | 88.328 | 72.664 | +4.56% | +0.13% | 2.83x | 16.5 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07261 | 80.680 | 68.337 | +9.57% | +0.40% | 2.03x | 17.9 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | STRONG 90/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.0568018 | 76.292 | 61.253 | +1.51% | +0.01% | 3.13x | 0.5 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 4 | INJ/USD | 6.178 | 65.901 | 67.309 | +3.76% | -0.02% | 0.87x | 4.9 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ETH/USD | 1704.64 | 63.077 | 60.863 | +0.84% | -0.02% | 1.23x | 0.1 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SEI/USD | 0.03648 | 62.839 | 72.704 | +9.52% | -1.54% | 0.78x | 11.0 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 7 | ADA/USD | 0.148778 | 61.383 | 68.167 | +2.06% | -0.18% | 0.41x | 2.6 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LINK/USD | 9.23961 | 60.527 | 68.854 | +2.16% | +0.09% | 0.12x | 2.5 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 43.6 | 59.865 | 68.439 | +2.08% | +0.09% | 0.10x | 2.3 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 60752.1 | 59.168 | 59.439 | +0.64% | -0.16% | 1.05x | 0.0 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94872 | 54.977 | 64.036 | +1.30% | -0.13% | 0.16x | 0.1 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SOL/USD | 70.89 | 51.428 | 59.267 | +0.71% | -0.06% | 0.24x | 1.4 | 2026-11-26T13:10:53.689409+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 72.704 | 0.03648 | -1.54% | 0.78x |
| 2 | QNT/USD | 72.664 | 151.4 | +0.13% | 2.83x |
| 3 | LINK/USD | 68.854 | 9.23961 | +0.09% | 0.12x |
| 4 | LTC/USD | 68.439 | 43.6 | +0.09% | 0.10x |
| 5 | SYRUP/USD | 68.337 | 0.07261 | +0.40% | 2.03x |
| 6 | ADA/USD | 68.167 | 0.148778 | -0.18% | 0.41x |
| 7 | INJ/USD | 67.309 | 6.178 | -0.02% | 0.87x |
| 8 | XRP/USD | 64.036 | 0.94872 | -0.13% | 0.16x |
| 9 | XDG/USD | 61.253 | 0.0568018 | +0.01% | 3.13x |
| 10 | ETH/USD | 60.863 | 1704.64 | -0.02% | 1.23x |
| 11 | XBT/USD | 59.439 | 60752.1 | -0.16% | 1.05x |
| 12 | SOL/USD | 59.267 | 70.89 | -0.06% | 0.24x |

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

- Persisted scans: 1865; predictions: 16115; observations: 1130301.
- Matured sampled outcomes across 1/6/24/48h: 34850; gap abstentions: 24805. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45826420740 · **Generation:** 1865 · **Legacy run:** 45826420740
**Main quote time:** 2026-11-26T13:11:01.531552+00:00 · **Legacy report time:** 2026-11-26T13:11:54.559722+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 151.4 | 88.33 | +0.13% | 2.83x | STRONG 94/100 | HIGH 61/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07261 | 80.68 | +0.40% | 2.03x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | XDG/USD | 0.0568018 | 76.29 | +0.01% | 3.13x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | INJ/USD | 6.178 | 65.90 | -0.02% | 0.87x | WEAK 38/100 | HIGH 68/100 | Watch |
| 5 | ETH/USD | 1704.64 | 63.08 | -0.02% | 1.23x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | SEI/USD | 0.03648 | 62.84 | -1.54% | 0.78x | WEAK 31/100 | VERY_HIGH 83/100 | Do nothing |
| 7 | ADA/USD | 0.148778 | 61.38 | -0.18% | 0.41x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | LINK/USD | 9.23961 | 60.53 | +0.09% | 0.12x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 43.6 | 59.86 | +0.09% | 0.10x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 60752.1 | 59.17 | -0.16% | 1.05x | WEAK 40/100 | HIGH 68/100 | Watch |
| 11 | XRP/USD | 0.94872 | 54.98 | -0.13% | 0.16x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SOL/USD | 70.89 | 51.43 | -0.06% | 0.24x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 151.38 | 90.94 | +0.13% | 2.83x | 9168 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07261 | 76.72 | +0.40% | 2.03x | 3857 | STRONG 98/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** QNT/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
