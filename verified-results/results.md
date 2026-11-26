# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T07:46:12.058730+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45777579507
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 979a7ad0143b551426b7079e005e6f345c224edb (atomic ledger/results publication)
**Ledger generation:** 1832 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07171 | 94.791 | 70.273 | +8.21% | +1.90% | 5.54x | 14.0 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | STRONG 97/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | ZRO/USD | 1.075 | 76.939 | 65.774 | +4.98% | +0.75% | 1.74x | 18.6 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | QNT/USD | 147.65 | 76.866 | 60.678 | +1.97% | +0.24% | 4.44x | 6.1 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 43.49 | 64.926 | 66.634 | +1.83% | +0.42% | 0.62x | 2.3 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XBT/USD | 60546.2 | 64.917 | 57.051 | +0.29% | +0.12% | 1.73x | 0.0 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 6 | INJ/USD | 6.111 | 62.112 | 59.173 | +2.64% | +0.21% | 1.19x | 3.3 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95305 | 61.471 | 67.010 | +1.76% | +0.29% | 0.30x | 0.6 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04402 | 60.847 | 65.972 | +5.11% | +0.50% | 0.24x | 6.8 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | ADA/USD | 0.147904 | 60.058 | 63.793 | +1.46% | +0.23% | 0.51x | 2.9 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.495e-06 | 57.023 | 45.178 | +0.32% | +0.11% | 2.13x | 2.9 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6692 | 56.751 | 56.552 | +0.44% | +0.28% | 0.88x | 3.0 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SOL/USD | 70.81 | 55.228 | 58.471 | +0.60% | +0.00% | 0.68x | 1.4 | 2026-11-26T07:46:04.023322+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 70.273 | 0.07171 | +1.90% | 5.54x |
| 2 | XRP/USD | 67.010 | 0.95305 | +0.29% | 0.30x |
| 3 | LTC/USD | 66.634 | 43.49 | +0.42% | 0.62x |
| 4 | SKY/USD | 65.972 | 0.04402 | +0.50% | 0.24x |
| 5 | ZRO/USD | 65.774 | 1.075 | +0.75% | 1.74x |
| 6 | ADA/USD | 63.793 | 0.147904 | +0.23% | 0.51x |
| 7 | QNT/USD | 60.678 | 147.65 | +0.24% | 4.44x |
| 8 | INJ/USD | 59.173 | 6.111 | +0.21% | 1.19x |
| 9 | SOL/USD | 58.471 | 70.81 | +0.00% | 0.68x |
| 10 | XBT/USD | 57.051 | 60546.2 | +0.12% | 1.73x |
| 11 | SUI/USD | 56.552 | 0.6692 | +0.28% | 0.88x |
| 12 | PEPE/USD | 45.178 | 3.495e-06 | +0.11% | 2.13x |

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

- Persisted scans: 1832; predictions: 15719; observations: 1110732.
- Matured sampled outcomes across 1/6/24/48h: 34070; gap abstentions: 24244. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45777579507 · **Generation:** 1832 · **Legacy run:** 45777579507
**Main quote time:** 2026-11-26T07:46:12.058730+00:00 · **Legacy report time:** 2026-11-26T07:47:09.634467+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.07171 | 94.79 | +1.90% | 5.54x | STRONG 97/100 | HIGH 66/100 | Consider small entry |
| 2 | ZRO/USD ⭐ | 1.075 | 76.94 | +0.75% | 1.74x | STRONG 88/100 | HIGH 61/100 | Consider small entry |
| 3 | QNT/USD | 147.65 | 76.87 | +0.24% | 4.44x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD | 43.49 | 64.93 | +0.42% | 0.62x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 5 | XBT/USD | 60546.2 | 64.92 | +0.12% | 1.73x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 6 | INJ/USD ⭐ | 6.111 | 62.11 | +0.21% | 1.19x | STRONG 76/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.95305 | 61.47 | +0.29% | 0.30x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 8 | SKY/USD | 0.04402 | 60.85 | +0.50% | 0.24x | MODERATE 60/100 | VERY_HIGH 75/100 | Watch |
| 9 | ADA/USD | 0.147904 | 60.06 | +0.23% | 0.51x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | PEPE/USD | 3.495e-06 | 57.02 | +0.11% | 2.13x | STRONG 74/100 | HIGH 55/100 | Watch |
| 11 | SUI/USD | 0.6692 | 56.75 | +0.28% | 0.88x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 12 | SOL/USD | 70.81 | 55.23 | +0.00% | 0.68x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.075 | 81.35 | +0.75% | 1.74x | 3515 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.111 | 67.61 | +0.21% | 1.19x | 6690 | STRONG 79/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZRO/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
