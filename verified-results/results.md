# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T20:00:50.749664+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45887703048
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7ff235715142028404fe6ee975e51111361aaa75 (atomic ledger/results publication)
**Ledger generation:** 1906 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5087 | 91.885 | 73.026 | +7.52% | +0.77% | 4.15x | 9.8 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.38686 | 73.867 | 77.527 | +8.12% | +0.93% | 0.17x | 10.1 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04554 | 73.416 | 75.295 | +8.74% | +0.46% | 0.58x | 8.8 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | FET/USD | 0.1208 | 71.016 | 70.356 | +11.34% | -0.25% | 1.19x | 16.6 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | ADA/USD | 0.150479 | 70.497 | 75.751 | +3.23% | -0.05% | 0.50x | 3.7 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 71.17 | 64.702 | 62.054 | +1.11% | -0.13% | 1.33x | 1.4 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1393 | 62.359 | 73.225 | +9.43% | -0.92% | 0.38x | 7.2 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | ZRO/USD | 1.108 | 61.831 | 72.269 | +8.20% | -0.63% | 0.27x | 18.1 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | LINK/USD | 9.26021 | 61.767 | 68.271 | +2.38% | -0.07% | 0.39x | 3.4 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | INJ/USD | 6.232 | 58.019 | 69.192 | +4.67% | -0.75% | 0.26x | 6.4 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1701.52 | 57.910 | 59.571 | +0.66% | -0.09% | 0.88x | 0.1 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.95087 | 57.742 | 65.643 | +1.53% | -0.12% | 0.27x | 0.1 | 2026-11-26T20:00:43.387803+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 77.527 | 0.38686 | +0.93% | 0.17x |
| 2 | ADA/USD | 75.751 | 0.150479 | -0.05% | 0.50x |
| 3 | SKY/USD | 75.295 | 0.04554 | +0.46% | 0.58x |
| 4 | WIF/USD | 73.225 | 0.1393 | -0.92% | 0.38x |
| 5 | AKT/USD | 73.026 | 0.5087 | +0.77% | 4.15x |
| 6 | ZRO/USD | 72.269 | 1.108 | -0.63% | 0.27x |
| 7 | FET/USD | 70.356 | 0.1208 | -0.25% | 1.19x |
| 8 | INJ/USD | 69.192 | 6.232 | -0.75% | 0.26x |
| 9 | LINK/USD | 68.271 | 9.26021 | -0.07% | 0.39x |
| 10 | XRP/USD | 65.643 | 0.95087 | -0.12% | 0.27x |
| 11 | SOL/USD | 62.054 | 71.17 | -0.13% | 1.33x |
| 12 | ETH/USD | 59.571 | 1701.52 | -0.09% | 0.88x |

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

- Persisted scans: 1906; predictions: 16607; observations: 1154628.
- Matured sampled outcomes across 1/6/24/48h: 36044; gap abstentions: 25209. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45887703048 · **Generation:** 1906 · **Legacy run:** 45887703048
**Main quote time:** 2026-11-26T20:00:50.749664+00:00 · **Legacy report time:** 2026-11-26T20:01:24.355321+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5087 | 91.88 | +0.77% | 4.15x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | DRV/USD | 0.38686 | 73.87 | +0.93% | 0.17x | MODERATE 62/100 | VERY_HIGH 76/100 | Watch |
| 3 | SKY/USD | 0.04554 | 73.42 | +0.46% | 0.58x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 4 | FET/USD | 0.1208 | 71.02 | -0.25% | 1.19x | WEAK 41/100 | VERY_HIGH 79/100 | Watch |
| 5 | ADA/USD | 0.150479 | 70.50 | -0.05% | 0.50x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 71.17 | 64.70 | -0.13% | 1.33x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | WIF/USD | 0.1393 | 62.36 | -0.92% | 0.38x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 8 | ZRO/USD | 1.108 | 61.83 | -0.63% | 0.27x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 9 | LINK/USD | 9.26021 | 61.77 | -0.07% | 0.39x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | INJ/USD | 6.232 | 58.02 | -0.75% | 0.26x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1701.52 | 57.91 | -0.09% | 0.88x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | XRP/USD | 0.95087 | 57.74 | -0.12% | 0.27x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD | 0.05478 | 85.80 | +0.38% | 2.00x | 4863 | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5086 | 82.02 | +0.77% | 4.15x | 2632 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | TREAD/USD | 1.23 | 73.42 | +0.44% | 1.31x | 3037 | MODERATE 67/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
