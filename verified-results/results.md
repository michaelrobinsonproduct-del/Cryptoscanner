# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T18:47:05.826743+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45462840951
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e1a16896d42eff742889df9dbc5cb631208e460a (atomic ledger/results publication)
**Ledger generation:** 1612 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 504.2 | 76.660 | 75.433 | +3.74% | +0.24% | 1.00x | 11.5 | 2026-11-24T18:47:00.799530+00:00 | Not calibrated | MODERATE 68/100 | HIGH 68/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31125 | 65.975 | 59.144 | +0.61% | -0.01% | 1.69x | 0.3 | 2026-11-24T18:47:00.799530+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66464 | 59.666 | 44.689 | +0.31% | -0.00% | 6.28x | 0.9 | 2026-11-24T18:47:00.799530+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 24.958 | 57.913 | 67.005 | +2.09% | -0.28% | 0.23x | 5.2 | 2026-11-24T18:47:00.799530+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.04858 | 55.980 | 46.519 | +0.89% | +0.46% | 1.72x | 2.1 | 2026-11-24T18:47:00.799530+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.433e-06 | 38.077 | 39.138 | +0.32% | +0.29% | 0.75x | 14.5 | 2026-11-24T18:47:00.799530+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 75.433 | 504.2 | +0.24% | 1.00x |
| 2 | VVV/USD | 67.005 | 24.958 | -0.28% | 0.23x |
| 3 | GBP/USD | 59.144 | 1.31125 | -0.01% | 1.69x |
| 4 | NIGHT/USD | 46.519 | 0.04858 | +0.46% | 1.72x |
| 5 | AUD/USD | 44.689 | 0.66464 | -0.00% | 6.28x |
| 6 | PEPE/USD | 39.138 | 3.433e-06 | +0.29% | 0.75x |

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

- Persisted scans: 1612; predictions: 13845; observations: 976800.
- Matured sampled outcomes across 1/6/24/48h: 27987; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45462840951 · **Generation:** 1612 · **Legacy run:** 45462840951
**Main quote time:** 2026-11-24T18:47:05.826743+00:00 · **Legacy report time:** 2026-11-24T18:47:53.635777+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 504.2 | 76.66 | +0.24% | 1.00x | STRONG 78/100 | HIGH 68/100 | Watch |
| 2 | GBP/USD | 1.31125 | 65.98 | -0.01% | 1.69x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 3 | AUD/USD | 0.66464 | 59.67 | -0.00% | 6.28x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 24.958 | 57.91 | -0.28% | 0.23x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | NIGHT/USD ⭐ | 0.04858 | 55.98 | +0.46% | 1.72x | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 6 | PEPE/USD | 3.433e-06 | 38.08 | +0.29% | 0.75x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 504.88 | 84.30 | +0.24% | 1.00x | 9018 | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04855 | 49.76 | +0.46% | 1.72x | 9458 | STRONG 80/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
