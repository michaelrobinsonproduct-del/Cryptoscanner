# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:20:10.876432+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44236536402
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 7cc3c54317e1127b38acc08503d497905821c7b3 (atomic ledger/results publication)
**Ledger generation:** 529 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.285 | 66.305 | 46.165 | +3.22% | +1.03% | 4.01x | 17.6 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019162 | 61.781 | 47.843 | +2.64% | +0.38% | 2.20x | 3.1 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | STRONG 86/100 | HIGH 67/100 | Watch | WATCH |
| 3 | CC/USD | 0.08378 | 50.780 | 47.799 | +2.01% | -0.81% | 1.70x | 3.6 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | MODERATE 45/100 | HIGH 66/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04515 | 47.938 | 49.576 | +0.58% | -0.46% | 1.07x | 2.2 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | MELANIA/USD | 0.051 | 39.938 | 44.216 | +4.72% | +0.20% | 0.47x | 39.1 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | WEAK 25/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | PEARL/USD | 1.8317 | 34.393 | 36.947 | +1.17% | -0.30% | 0.90x | 12.5 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.518 | 33.206 | 41.419 | +1.71% | +0.14% | 0.11x | 5.8 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | ZAMA/USD | 0.06095 | 31.960 | 38.683 | +1.70% | -0.34% | 0.50x | 13.2 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | WEAK 16/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | XDC/USD | 0.03076 | 31.953 | 39.381 | +1.45% | +0.16% | 0.18x | 16.2 | 2026-11-18T04:20:04.679877+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 49.576 | 0.04515 | -0.46% | 1.07x |
| 2 | SENT/USD | 47.843 | 0.019162 | +0.38% | 2.20x |
| 3 | CC/USD | 47.799 | 0.08378 | -0.81% | 1.70x |
| 4 | ICNT/USD | 46.165 | 0.285 | +1.03% | 4.01x |
| 5 | MELANIA/USD | 44.216 | 0.051 | +0.20% | 0.47x |
| 6 | AKT/USD | 41.419 | 0.518 | +0.14% | 0.11x |
| 7 | XDC/USD | 39.381 | 0.03076 | +0.16% | 0.18x |
| 8 | ZAMA/USD | 38.683 | 0.06095 | -0.34% | 0.50x |
| 9 | PEARL/USD | 36.947 | 1.8317 | -0.30% | 0.90x |

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

- Persisted scans: 529; predictions: 4473; observations: 319168.
- Matured sampled outcomes across 1/6/24/48h: 3563; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44236536402 · **Generation:** 529 · **Legacy run:** 44236536402
**Main quote time:** 2026-11-18T04:20:10.876432+00:00 · **Legacy report time:** 2026-11-18T04:20:30.812195+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.285 | 66.30 | +1.03% | 4.01x | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.019162 | 61.78 | +0.38% | 2.20x | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 3 | CC/USD | 0.08378 | 50.78 | -0.81% | 1.70x | MODERATE 45/100 | HIGH 66/100 | Watch |
| 4 | NIGHT/USD | 0.04515 | 47.94 | -0.46% | 1.07x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 5 | MELANIA/USD | 0.051 | 39.94 | +0.20% | 0.47x | WEAK 25/100 | EXTREME 94/100 | Do nothing |
| 6 | PEARL/USD | 1.8317 | 34.39 | -0.30% | 0.90x | WEAK 17/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | AKT/USD | 0.518 | 33.21 | +0.14% | 0.11x | WEAK 37/100 | VERY_HIGH 75/100 | Watch |
| 8 | ZAMA/USD | 0.06095 | 31.96 | -0.34% | 0.50x | WEAK 16/100 | EXTREME 87/100 | Do nothing |
| 9 | XDC/USD | 0.03076 | 31.95 | +0.16% | 0.18x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.285 | 73.20 | +1.03% | 4.01x | 3822 | STRONG 97/100 | HIGH 66/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.019189 | 61.94 | +0.38% | 2.20x | 4003 | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 3 | NEAR/USD | 3.4034 | 54.89 | +0.37% | 19.13x | 15750 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ICNT/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
