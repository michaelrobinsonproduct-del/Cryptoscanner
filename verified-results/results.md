# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T12:31:57.091604+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45394017811
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 53adf431a958bc345610578aeace76e3b3be0da8 (atomic ledger/results publication)
**Ledger generation:** 1574 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.799 | 89.329 | 90.386 | +5.53% | -0.05% | 0.92x | 6.6 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 2 | MON/USD | 0.01253 | 82.868 | 79.040 | +8.77% | +0.08% | 1.34x | 16.0 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 499.53 | 78.512 | 69.352 | +2.78% | +0.00% | 1.92x | 10.2 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04871 | 73.021 | 55.845 | +1.16% | +0.44% | 2.52x | 2.1 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PEPE/USD | 3.455e-06 | 69.983 | 54.548 | +0.96% | +0.09% | 5.27x | 8.7 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 6 | GBP/USD | 1.30835 | 50.368 | 57.701 | +0.39% | +0.04% | 0.25x | 0.1 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ARB/USD | 0.113 | 35.558 | 30.654 | +0.36% | +0.09% | 1.45x | 17.7 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 8 | BAT/USD | 0.0776 | 33.891 | 33.749 | +0.56% | -0.32% | 1.17x | 5.2 | 2026-11-24T12:31:50.318182+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.386 | 25.799 | -0.05% | 0.92x |
| 2 | MON/USD | 79.040 | 0.01253 | +0.08% | 1.34x |
| 3 | XMR/USD | 69.352 | 499.53 | +0.00% | 1.92x |
| 4 | GBP/USD | 57.701 | 1.30835 | +0.04% | 0.25x |
| 5 | NIGHT/USD | 55.845 | 0.04871 | +0.44% | 2.52x |
| 6 | PEPE/USD | 54.548 | 3.455e-06 | +0.09% | 5.27x |
| 7 | BAT/USD | 33.749 | 0.0776 | -0.32% | 1.17x |
| 8 | ARB/USD | 30.654 | 0.113 | +0.09% | 1.45x |

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

- Persisted scans: 1574; predictions: 13578; observations: 953664.
- Matured sampled outcomes across 1/6/24/48h: 26323; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45394017811 · **Generation:** 1574 · **Legacy run:** 45394017811
**Main quote time:** 2026-11-24T12:31:57.091604+00:00 · **Legacy report time:** 2026-11-24T12:32:51.296134+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.799 | 89.33 | -0.05% | 0.92x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 2 | MON/USD ⭐ | 0.01253 | 82.87 | +0.08% | 1.34x | STRONG 81/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 499.53 | 78.51 | +0.00% | 1.92x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04871 | 73.02 | +0.44% | 2.52x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PEPE/USD ⭐ | 3.455e-06 | 69.98 | +0.09% | 5.27x | STRONG 90/100 | HIGH 55/100 | Watch |
| 6 | GBP/USD | 1.30835 | 50.37 | +0.04% | 0.25x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | ARB/USD ⭐ | 0.113 | 35.56 | +0.09% | 1.45x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | BAT/USD | 0.0776 | 33.89 | -0.32% | 1.17x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01241 | 78.77 | +0.08% | 1.34x | 10648 | STRONG 79/100 | HIGH 61/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.45e-06 | 62.55 | +0.09% | 5.27x | 9560 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04871 | 57.26 | +0.44% | 2.52x | 12348 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | ARB/USD ⭐ | 0.113 | 32.53 | +0.09% | 1.45x | 2653 | MODERATE 61/100 | HIGH 55/100 | Watch |

**Same-run overlap:** MON/USD, NIGHT/USD, PEPE/USD, ARB/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
