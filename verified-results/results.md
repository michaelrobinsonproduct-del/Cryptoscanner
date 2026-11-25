# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T07:27:34.195780+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45567900381
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3796a23b0bb471005c1747e9926e177479a0bb4b (atomic ledger/results publication)
**Ledger generation:** 1687 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01042 | 102.210 | 89.480 | +10.03% | +2.45% | 1.05x | 9.6 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | BABY/USD | 0.0088 | 66.770 | 71.572 | +6.54% | -3.96% | 6.28x | 11.4 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | DRV/USD | 0.3345 | 65.484 | 73.067 | +6.43% | -0.34% | 0.41x | 18.6 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.481e-06 | 44.026 | 45.719 | +0.81% | -0.71% | 1.19x | 8.6 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07181 | 39.363 | 44.907 | +3.07% | -0.32% | 0.60x | 16.7 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 20/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | CAP/USD | 0.093324 | 36.059 | 36.044 | +0.98% | +0.33% | 0.84x | 6.1 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 7 | PENGU/USD | 0.004231 | 27.355 | 33.790 | +0.36% | -0.40% | 0.56x | 4.7 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | 2Z/USD | 0.01644 | 26.946 | 29.999 | +0.31% | +0.12% | 0.63x | 6.1 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | KAS/USD | 0.0262 | 26.640 | 26.183 | +0.31% | -0.38% | 1.24x | 19.1 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | SKY/USD | 0.04111 | 22.108 | 31.106 | +0.32% | -0.07% | 0.14x | 9.8 | 2026-11-25T07:27:27.416877+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 89.480 | 0.01042 | +2.45% | 1.05x |
| 2 | DRV/USD | 73.067 | 0.3345 | -0.34% | 0.41x |
| 3 | BABY/USD | 71.572 | 0.0088 | -3.96% | 6.28x |
| 4 | PEPE/USD | 45.719 | 3.481e-06 | -0.71% | 1.19x |
| 5 | SYRUP/USD | 44.907 | 0.07181 | -0.32% | 0.60x |
| 6 | CAP/USD | 36.044 | 0.093324 | +0.33% | 0.84x |
| 7 | PENGU/USD | 33.790 | 0.004231 | -0.40% | 0.56x |
| 8 | SKY/USD | 31.106 | 0.04111 | -0.07% | 0.14x |
| 9 | 2Z/USD | 29.999 | 0.01644 | +0.12% | 0.63x |
| 10 | KAS/USD | 26.183 | 0.0262 | -0.38% | 1.24x |

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

- Persisted scans: 1687; predictions: 14326; observations: 1022474.
- Matured sampled outcomes across 1/6/24/48h: 30629; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45567900381 · **Generation:** 1687 · **Legacy run:** 45567900381
**Main quote time:** 2026-11-25T07:27:34.195780+00:00 · **Legacy report time:** 2026-11-25T07:28:48.362364+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01042 | 102.21 | +2.45% | 1.05x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | BABY/USD | 0.0088 | 66.77 | -3.96% | 6.28x | MODERATE 58/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | DRV/USD | 0.3345 | 65.48 | -0.34% | 0.41x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | PEPE/USD | 3.481e-06 | 44.03 | -0.71% | 1.19x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 5 | SYRUP/USD | 0.07181 | 39.36 | -0.32% | 0.60x | WEAK 20/100 | EXTREME 87/100 | Do nothing |
| 6 | CAP/USD | 0.093324 | 36.06 | +0.33% | 0.84x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 7 | PENGU/USD | 0.004231 | 27.36 | -0.40% | 0.56x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | 2Z/USD | 0.01644 | 26.95 | +0.12% | 0.63x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | KAS/USD | 0.0262 | 26.64 | -0.38% | 1.24x | WEAK 18/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | SKY/USD | 0.04111 | 22.11 | -0.07% | 0.14x | WEAK 16/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01044 | 89.14 | +2.45% | 1.05x | 18801 | STRONG 90/100 | HIGH 62/100 | Watch |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
