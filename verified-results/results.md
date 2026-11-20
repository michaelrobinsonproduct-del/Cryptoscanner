# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T03:45:28.225232+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44669761593
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** e0a0d0227ce47c6c3ede6ceb7daec279728c09ae (atomic ledger/results publication)
**Ledger generation:** 917 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.96281 | 73.111 | 57.234 | +0.37% | +0.54% | 2.32x | 0.7 | 2026-11-20T03:45:23.782575+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.0456 | 66.537 | 47.547 | +1.88% | +0.80% | 3.88x | 13.2 | 2026-11-20T03:45:23.782575+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CT/USD | 0.1307 | 61.369 | 40.173 | +1.71% | +1.24% | 4.49x | 7.7 | 2026-11-20T03:45:23.782575+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 4 | XBT/USD | 62073.3 | 51.722 | 56.799 | +0.26% | +0.08% | 0.45x | 0.0 | 2026-11-20T03:45:23.782575+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SAPIEN/USD | 0.04114 | 31.953 | 36.917 | +2.44% | -0.07% | 0.54x | 21.9 | 2026-11-20T03:45:23.782575+00:00 | Not calibrated | WEAK 11/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.4303 | 30.002 | 31.694 | +0.99% | -0.14% | 0.90x | 25.8 | 2026-11-20T03:45:23.782575+00:00 | Not calibrated | WEAK 10/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 57.234 | 0.96281 | +0.54% | 2.32x |
| 2 | XBT/USD | 56.799 | 62073.3 | +0.08% | 0.45x |
| 3 | NIGHT/USD | 47.547 | 0.0456 | +0.80% | 3.88x |
| 4 | CT/USD | 40.173 | 0.1307 | +1.24% | 4.49x |
| 5 | SAPIEN/USD | 36.917 | 0.04114 | -0.07% | 0.54x |
| 6 | ICNT/USD | 31.694 | 0.4303 | -0.14% | 0.90x |

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

- Persisted scans: 917; predictions: 7916; observations: 554076.
- Matured sampled outcomes across 1/6/24/48h: 9057; gap abstentions: 16593. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44669761593 · **Generation:** 917 · **Legacy run:** 44669761593
**Main quote time:** 2026-11-20T03:45:28.225232+00:00 · **Legacy report time:** 2026-11-20T03:46:10.706133+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96281 | 73.11 | +0.54% | 2.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.0456 | 66.54 | +0.80% | 3.88x | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 3 | CT/USD ⭐ | 0.1307 | 61.37 | +1.24% | 4.49x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 4 | XBT/USD | 62073.3 | 51.72 | +0.08% | 0.45x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 5 | SAPIEN/USD | 0.04114 | 31.95 | -0.07% | 0.54x | WEAK 11/100 | EXTREME 100/100 | Do nothing |
| 6 | ICNT/USD | 0.4303 | 30.00 | -0.14% | 0.90x | WEAK 10/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.0456 | 72.12 | +0.80% | 3.88x | 8446 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.9632 | 62.38 | +0.54% | 2.32x | 34244 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 3 | CT/USD ⭐ | 0.1308 | 55.36 | +1.24% | 4.49x | 2514 | STRONG 83/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** XRP/USD, NIGHT/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
