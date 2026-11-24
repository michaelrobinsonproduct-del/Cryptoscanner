# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T23:41:59.179603+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45511823880
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 82af9f384798c004096461f8a48b28ac19462bc7 (atomic ledger/results publication)
**Ledger generation:** 1641 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 507.91 | 76.308 | 80.614 | +4.50% | -0.01% | 0.58x | 11.8 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.59e-05 | 74.851 | 60.938 | +5.59% | -0.22% | 2.57x | 19.8 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | WINGS/USD | 0.002214 | 59.402 | 69.727 | +6.85% | -0.94% | 0.44x | 13.6 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | GBP/USD | 1.31082 | 57.044 | 58.913 | +0.58% | +0.01% | 0.81x | 0.3 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 5 | VVV/USD | 24.65 | 47.642 | 57.740 | +0.83% | -0.44% | 0.21x | 6.1 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04887 | 45.351 | 48.515 | +1.50% | -0.35% | 0.86x | 2.0 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | SKY/USD | 0.04108 | 42.462 | 42.149 | +1.71% | -0.07% | 1.07x | 7.3 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 8 | PEPE/USD | 3.45e-06 | 40.091 | 48.373 | +0.82% | -0.32% | 0.33x | 5.8 | 2026-11-24T23:41:55.740547+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 80.614 | 507.91 | -0.01% | 0.58x |
| 2 | WINGS/USD | 69.727 | 0.002214 | -0.94% | 0.44x |
| 3 | LUNA/USD | 60.938 | 4.59e-05 | -0.22% | 2.57x |
| 4 | GBP/USD | 58.913 | 1.31082 | +0.01% | 0.81x |
| 5 | VVV/USD | 57.740 | 24.65 | -0.44% | 0.21x |
| 6 | NIGHT/USD | 48.515 | 0.04887 | -0.35% | 0.86x |
| 7 | PEPE/USD | 48.373 | 3.45e-06 | -0.32% | 0.33x |
| 8 | SKY/USD | 42.149 | 0.04108 | -0.07% | 1.07x |

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

- Persisted scans: 1641; predictions: 14051; observations: 994460.
- Matured sampled outcomes across 1/6/24/48h: 29106; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45511823880 · **Generation:** 1641 · **Legacy run:** 45511823880
**Main quote time:** 2026-11-24T23:41:59.179603+00:00 · **Legacy report time:** 2026-11-24T23:42:51.100315+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 507.91 | 76.31 | -0.01% | 0.58x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |
| 2 | LUNA/USD | 4.59e-05 | 74.85 | -0.22% | 2.57x | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |
| 3 | WINGS/USD | 0.002214 | 59.40 | -0.94% | 0.44x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 4 | GBP/USD | 1.31082 | 57.04 | +0.01% | 0.81x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 5 | VVV/USD | 24.65 | 47.64 | -0.44% | 0.21x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | NIGHT/USD | 0.04887 | 45.35 | -0.35% | 0.86x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 7 | SKY/USD | 0.04108 | 42.46 | -0.07% | 1.07x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 8 | PEPE/USD | 3.45e-06 | 40.09 | -0.32% | 0.33x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
