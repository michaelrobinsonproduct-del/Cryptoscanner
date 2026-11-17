# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:50:04.108887+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44193763875
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** bb0d109dbe432db08ad61cffd36482b2908166ed (atomic ledger/results publication)
**Ledger generation:** 463 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.242 | 105.095 | 87.039 | +4.97% | +0.61% | 6.32x | 5.5 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 945.56 | 100.716 | 85.590 | +4.62% | +0.57% | 2.23x | 3.5 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3126 | 93.045 | 88.258 | +4.90% | +0.01% | 1.47x | 2.1 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 20.815 | 83.144 | 67.207 | +3.31% | +0.19% | 6.30x | 6.3 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 73.83 | 70.408 | 76.254 | +3.23% | +0.22% | 0.31x | 2.7 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XMR/USD | 506.24 | 68.895 | 67.420 | +2.56% | +0.42% | 0.94x | 11.1 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 7 | TRUST/USD | 0.04731 | 66.895 | 76.916 | +10.00% | -0.23% | 0.11x | 2.1 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | AVAX/USD | 7.205 | 66.505 | 52.531 | +1.32% | +0.13% | 2.33x | 1.4 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5034 | 63.759 | 67.640 | +5.23% | +0.06% | 0.58x | 2.0 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | JUP/USD | 0.25796 | 63.585 | 71.119 | +7.23% | +0.17% | 0.16x | 14.0 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | SUI/USD | 0.7312 | 59.940 | 65.798 | +1.64% | +0.21% | 0.31x | 1.4 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.97071 | 59.392 | 66.179 | +1.67% | +0.06% | 0.29x | 1.0 | 2026-11-17T22:49:55.453127+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 88.258 | 3.3126 | +0.01% | 1.47x |
| 2 | INJ/USD | 87.039 | 7.242 | +0.61% | 6.32x |
| 3 | ZEC/USD | 85.590 | 945.56 | +0.57% | 2.23x |
| 4 | TRUST/USD | 76.916 | 0.04731 | -0.23% | 0.11x |
| 5 | SOL/USD | 76.254 | 73.83 | +0.22% | 0.31x |
| 6 | JUP/USD | 71.119 | 0.25796 | +0.17% | 0.16x |
| 7 | AKT/USD | 67.640 | 0.5034 | +0.06% | 0.58x |
| 8 | XMR/USD | 67.420 | 506.24 | +0.42% | 0.94x |
| 9 | VVV/USD | 67.207 | 20.815 | +0.19% | 6.30x |
| 10 | XRP/USD | 66.179 | 0.97071 | +0.06% | 0.29x |
| 11 | SUI/USD | 65.798 | 0.7312 | +0.21% | 0.31x |
| 12 | AVAX/USD | 52.531 | 7.205 | +0.13% | 2.33x |

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

- Persisted scans: 463; predictions: 4037; observations: 278974.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44193763875 · **Generation:** 463 · **Legacy run:** 44193763875
**Main quote time:** 2026-11-17T22:50:04.108887+00:00 · **Legacy report time:** 2026-11-17T22:50:13.516840+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.242 | 105.09 | +0.61% | 6.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 945.56 | 100.72 | +0.57% | 2.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD | 3.3126 | 93.05 | +0.01% | 1.47x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD | 20.815 | 83.14 | +0.19% | 6.30x | STRONG 87/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 73.83 | 70.41 | +0.22% | 0.31x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 6 | XMR/USD | 506.24 | 68.90 | +0.42% | 0.94x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 7 | TRUST/USD | 0.04731 | 66.90 | -0.23% | 0.11x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 8 | AVAX/USD | 7.205 | 66.51 | +0.13% | 2.33x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | AKT/USD | 0.5034 | 63.76 | +0.06% | 0.58x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 10 | JUP/USD | 0.25796 | 63.58 | +0.17% | 0.16x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 11 | SUI/USD | 0.7312 | 59.94 | +0.21% | 0.31x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.97071 | 59.39 | +0.06% | 0.29x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 945.56 | 99.52 | +0.06% | 3.67x | 25935 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | WINGS/USD | 0.001927 | 72.15 | +0.47% | 1.00x | 3908 | MODERATE 56/100 | EXTREME 96/100 | Do nothing |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
