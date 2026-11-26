# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T05:46:23.921125+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45763559798
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 41c0b525f288de369aa6b56c257c80cc61ca712e (atomic ledger/results publication)
**Ledger generation:** 1820 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07044 | 86.447 | 66.225 | +6.29% | +1.04% | 2.73x | 19.9 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.95868 | 85.496 | 71.116 | +2.36% | -0.12% | 3.67x | 0.8 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ADA/USD | 0.14913 | 84.621 | 70.297 | +2.31% | -0.14% | 7.03x | 1.7 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 43.53 | 81.260 | 67.291 | +1.92% | -0.21% | 4.63x | 2.3 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 9.21495 | 78.151 | 63.899 | +1.88% | -0.15% | 3.88x | 4.0 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0734 | 75.590 | 59.743 | +0.77% | +0.17% | 4.13x | 1.3 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 71 | 69.118 | 60.362 | +0.87% | -0.20% | 1.97x | 1.4 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0567104 | 67.216 | 59.475 | +1.34% | -0.09% | 1.82x | 0.5 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 9 | TAO/USD | 183.8386 | 65.904 | 59.786 | +1.24% | -0.01% | 1.62x | 7.7 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | DRV/USD | 0.36503 | 61.384 | 51.035 | +2.02% | -0.93% | 8.31x | 0.3 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XBT/USD | 60732.6 | 58.336 | 59.212 | +0.60% | -0.19% | 1.01x | 0.0 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XMR/USD | 520 | 57.053 | 59.034 | +0.59% | +0.24% | 0.68x | 0.2 | 2026-11-26T05:46:15.659271+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 71.116 | 0.95868 | -0.12% | 3.67x |
| 2 | ADA/USD | 70.297 | 0.14913 | -0.14% | 7.03x |
| 3 | LTC/USD | 67.291 | 43.53 | -0.21% | 4.63x |
| 4 | SYRUP/USD | 66.225 | 0.07044 | +1.04% | 2.73x |
| 5 | LINK/USD | 63.899 | 9.21495 | -0.15% | 3.88x |
| 6 | SOL/USD | 60.362 | 71 | -0.20% | 1.97x |
| 7 | TAO/USD | 59.786 | 183.8386 | -0.01% | 1.62x |
| 8 | NEAR/USD | 59.743 | 3.0734 | +0.17% | 4.13x |
| 9 | XDG/USD | 59.475 | 0.0567104 | -0.09% | 1.82x |
| 10 | XBT/USD | 59.212 | 60732.6 | -0.19% | 1.01x |
| 11 | XMR/USD | 59.034 | 520 | +0.24% | 0.68x |
| 12 | DRV/USD | 51.035 | 0.36503 | -0.93% | 8.31x |

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

- Persisted scans: 1820; predictions: 15575; observations: 1103424.
- Matured sampled outcomes across 1/6/24/48h: 33791; gap abstentions: 23992. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45763559798 · **Generation:** 1820 · **Legacy run:** 45763559798
**Main quote time:** 2026-11-26T05:46:23.921125+00:00 · **Legacy report time:** 2026-11-26T05:47:21.816093+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07044 | 86.45 | +1.04% | 2.73x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | XRP/USD | 0.95868 | 85.50 | -0.12% | 3.67x | STRONG 73/100 | HIGH 61/100 | Watch |
| 3 | ADA/USD | 0.14913 | 84.62 | -0.14% | 7.03x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 43.53 | 81.26 | -0.21% | 4.63x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 9.21495 | 78.15 | -0.15% | 3.88x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD | 3.0734 | 75.59 | +0.17% | 4.13x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 71 | 69.12 | -0.20% | 1.97x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | XDG/USD | 0.0567104 | 67.22 | -0.09% | 1.82x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 9 | TAO/USD | 183.8386 | 65.90 | -0.01% | 1.62x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | DRV/USD | 0.36503 | 61.38 | -0.93% | 8.31x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 11 | XBT/USD | 60732.6 | 58.34 | -0.19% | 1.01x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | XMR/USD | 520 | 57.05 | +0.24% | 0.68x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.902 | 86.02 | +1.65% | 6.47x | 2488 | STRONG 83/100 | HIGH 67/100 | Consider small entry |
| 2 | SYRUP/USD ⭐ | 0.07044 | 81.35 | +1.04% | 2.73x | 3659 | STRONG 100/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
