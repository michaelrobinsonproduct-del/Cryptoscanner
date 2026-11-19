# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:30:23.459488+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44638065282
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 1c27737526f9ff8492f958ca0e6b8d4c391ec3a0 (atomic ledger/results publication)
**Ledger generation:** 879 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021353 | 68.907 | 53.205 | +3.63% | +0.14% | 8.87x | 13.1 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05945 | 64.282 | 69.313 | +6.16% | -0.47% | 0.73x | 11.8 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | AKT/USD | 0.5311 | 61.870 | 44.509 | +2.53% | +0.47% | 33.58x | 11.3 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.0989 | 59.261 | 58.800 | +3.50% | +0.06% | 1.02x | 12.2 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ADA/USD | 0.151654 | 58.125 | 54.509 | +0.26% | +0.38% | 1.17x | 4.7 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 6 | VVV/USD | 21.949 | 56.229 | 61.928 | +1.28% | +0.53% | 0.17x | 4.1 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | INJ/USD | 7.08 | 54.658 | 53.376 | +1.42% | +0.44% | 0.91x | 4.2 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 8 | TRX/USD | 0.310139 | 44.632 | 43.937 | +0.28% | +0.12% | 1.01x | 0.6 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PYTH/USD | 0.0531 | 38.918 | 33.035 | +0.64% | +0.66% | 1.26x | 9.4 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | MODERATE 54/100 | HIGH 60/100 | Watch | WATCH |
| 10 | CAP/USD | 0.096462 | 37.165 | 31.945 | +0.46% | -0.14% | 1.59x | 11.8 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 11 | BABY/USD | 0.00845 | 35.633 | 34.119 | +1.32% | +1.08% | 0.61x | 11.8 | 2026-11-19T23:30:15.064229+00:00 | Not calibrated | WEAK 43/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 69.313 | 0.05945 | -0.47% | 0.73x |
| 2 | VVV/USD | 61.928 | 21.949 | +0.53% | 0.17x |
| 3 | USELESS/USD | 58.800 | 0.0989 | +0.06% | 1.02x |
| 4 | ADA/USD | 54.509 | 0.151654 | +0.38% | 1.17x |
| 5 | INJ/USD | 53.376 | 7.08 | +0.44% | 0.91x |
| 6 | SENT/USD | 53.205 | 0.021353 | +0.14% | 8.87x |
| 7 | AKT/USD | 44.509 | 0.5311 | +0.47% | 33.58x |
| 8 | TRX/USD | 43.937 | 0.310139 | +0.12% | 1.01x |
| 9 | BABY/USD | 34.119 | 0.00845 | +1.08% | 0.61x |
| 10 | PYTH/USD | 33.035 | 0.0531 | +0.66% | 1.26x |
| 11 | CAP/USD | 31.945 | 0.096462 | -0.14% | 1.59x |

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

- Persisted scans: 879; predictions: 7658; observations: 531162.
- Matured sampled outcomes across 1/6/24/48h: 8174; gap abstentions: 15862. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44638065282 · **Generation:** 879 · **Legacy run:** 44638065282
**Main quote time:** 2026-11-19T23:30:23.459488+00:00 · **Legacy report time:** 2026-11-19T23:31:17.380047+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021353 | 68.91 | +0.14% | 8.87x | STRONG 84/100 | HIGH 66/100 | Watch |
| 2 | MEGA/USD | 0.05945 | 64.28 | -0.47% | 0.73x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 3 | AKT/USD ⭐ | 0.5311 | 61.87 | +0.47% | 33.58x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 4 | USELESS/USD ⭐ | 0.0989 | 59.26 | +0.06% | 1.02x | MODERATE 60/100 | HIGH 68/100 | Watch |
| 5 | ADA/USD | 0.151654 | 58.12 | +0.38% | 1.17x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 6 | VVV/USD | 21.949 | 56.23 | +0.53% | 0.17x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | INJ/USD | 7.08 | 54.66 | +0.44% | 0.91x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 8 | TRX/USD | 0.310139 | 44.63 | +0.12% | 1.01x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 9 | PYTH/USD | 0.0531 | 38.92 | +0.66% | 1.26x | MODERATE 54/100 | HIGH 60/100 | Watch |
| 10 | CAP/USD | 0.096462 | 37.17 | -0.14% | 1.59x | WEAK 34/100 | VERY_HIGH 72/100 | Do nothing |
| 11 | BABY/USD | 0.00845 | 35.63 | +1.08% | 0.61x | WEAK 43/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021254 | 79.23 | +0.14% | 8.87x | 14713 | STRONG 95/100 | HIGH 60/100 | Watch |
| 2 | AKT/USD ⭐ | 0.53 | 71.92 | +0.47% | 33.58x | 3561 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | USELESS/USD ⭐ | 0.09831 | 62.99 | +0.06% | 1.02x | 6071 | MODERATE 61/100 | HIGH 68/100 | Watch |

**Same-run overlap:** SENT/USD, AKT/USD, USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
