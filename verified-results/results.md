# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T17:51:06.119449+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45870963098
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b30034a359c2366dee46fa77b90b891b40b704a6 (atomic ledger/results publication)
**Ledger generation:** 1893 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04582 | 85.626 | 75.498 | +9.41% | -0.97% | 8.24x | 8.7 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0698 | 70.683 | 58.101 | +0.65% | -0.23% | 2.37x | 2.9 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.27 | 70.390 | 63.022 | +1.31% | -0.07% | 1.77x | 2.3 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 4 | FET/USD | 0.1158 | 66.387 | 69.719 | +6.73% | -0.09% | 0.71x | 17.2 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | WIF/USD | 0.1369 | 65.172 | 72.846 | +7.54% | -0.07% | 0.27x | 7.3 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01747 | 65.026 | 66.230 | +5.75% | -0.57% | 1.16x | 11.5 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | ADA/USD | 0.148836 | 64.990 | 67.037 | +2.10% | -0.13% | 0.86x | 5.4 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 8 | STBL/USD | 0.020145 | 63.892 | 64.556 | +6.67% | -0.06% | 0.96x | 22.9 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 27/100 | EXTREME 92/100 | Do nothing | WATCH |
| 9 | XRP/USD | 0.94922 | 63.526 | 64.146 | +1.35% | -0.03% | 0.95x | 0.6 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SOL/USD | 70.99 | 61.001 | 60.262 | +0.85% | -0.03% | 1.09x | 1.4 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | LINK/USD | 9.19018 | 58.560 | 64.772 | +1.61% | -0.18% | 0.47x | 3.0 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ZRO/USD | 1.071 | 58.291 | 64.388 | +4.59% | -0.46% | 0.62x | 9.3 | 2026-11-26T17:50:58.124179+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.498 | 0.04582 | -0.97% | 8.24x |
| 2 | WIF/USD | 72.846 | 0.1369 | -0.07% | 0.27x |
| 3 | FET/USD | 69.719 | 0.1158 | -0.09% | 0.71x |
| 4 | ADA/USD | 67.037 | 0.148836 | -0.13% | 0.86x |
| 5 | 2Z/USD | 66.230 | 0.01747 | -0.57% | 1.16x |
| 6 | LINK/USD | 64.772 | 9.19018 | -0.18% | 0.47x |
| 7 | STBL/USD | 64.556 | 0.020145 | -0.06% | 0.96x |
| 8 | ZRO/USD | 64.388 | 1.071 | -0.46% | 0.62x |
| 9 | XRP/USD | 64.146 | 0.94922 | -0.03% | 0.95x |
| 10 | LTC/USD | 63.022 | 43.27 | -0.07% | 1.77x |
| 11 | SOL/USD | 60.262 | 70.99 | -0.03% | 1.09x |
| 12 | NEAR/USD | 58.101 | 3.0698 | -0.23% | 2.37x |

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

- Persisted scans: 1893; predictions: 16451; observations: 1146869.
- Matured sampled outcomes across 1/6/24/48h: 35568; gap abstentions: 25112. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45870963098 · **Generation:** 1893 · **Legacy run:** 45870963098
**Main quote time:** 2026-11-26T17:51:06.119449+00:00 · **Legacy report time:** 2026-11-26T17:51:39.350650+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.04582 | 85.63 | -0.97% | 8.24x | STRONG 73/100 | HIGH 66/100 | Watch |
| 2 | NEAR/USD | 3.0698 | 70.68 | -0.23% | 2.37x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.27 | 70.39 | -0.07% | 1.77x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 4 | FET/USD | 0.1158 | 66.39 | -0.09% | 0.71x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 5 | WIF/USD | 0.1369 | 65.17 | -0.07% | 0.27x | WEAK 38/100 | EXTREME 88/100 | Do nothing |
| 6 | 2Z/USD | 0.01747 | 65.03 | -0.57% | 1.16x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |
| 7 | ADA/USD | 0.148836 | 64.99 | -0.13% | 0.86x | WEAK 37/100 | HIGH 68/100 | Watch |
| 8 | STBL/USD | 0.020145 | 63.89 | -0.06% | 0.96x | WEAK 27/100 | EXTREME 92/100 | Do nothing |
| 9 | XRP/USD | 0.94922 | 63.53 | -0.03% | 0.95x | WEAK 37/100 | HIGH 68/100 | Watch |
| 10 | SOL/USD | 70.99 | 61.00 | -0.03% | 1.09x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | LINK/USD | 9.19018 | 58.56 | -0.18% | 0.47x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ZRO/USD | 1.071 | 58.29 | -0.46% | 0.62x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

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
