# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T13:02:18.870346+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45398860822
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 31563c9ce406a6e7c089ed1dfa634f9826acc75e (atomic ledger/results publication)
**Ledger generation:** 1577 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.022 | 98.174 | 94.618 | +6.44% | +0.71% | 1.00x | 10.8 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | STRONG 74/100 | HIGH 68/100 | Watch | WATCH |
| 2 | XMR/USD | 499.28 | 78.046 | 69.485 | +2.73% | -0.24% | 1.98x | 9.2 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 3 | MON/USD | 0.01225 | 76.879 | 82.265 | +6.34% | -0.49% | 0.71x | 8.2 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | GBP/USD | 1.30959 | 73.264 | 58.138 | +0.49% | +0.03% | 5.03x | 0.5 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04909 | 58.931 | 60.044 | +1.95% | -0.04% | 0.91x | 4.1 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | AUD/USD | 0.66448 | 40.460 | 49.219 | +0.29% | +0.01% | 0.12x | 0.9 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.435e-06 | 38.149 | 50.252 | +0.38% | -0.55% | 0.06x | 8.7 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | 2Z/USD | 0.01595 | 37.135 | 41.020 | +1.92% | -0.25% | 0.74x | 6.3 | 2026-11-24T13:02:12.785174+00:00 | Not calibrated | WEAK 24/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.618 | 26.022 | +0.71% | 1.00x |
| 2 | MON/USD | 82.265 | 0.01225 | -0.49% | 0.71x |
| 3 | XMR/USD | 69.485 | 499.28 | -0.24% | 1.98x |
| 4 | NIGHT/USD | 60.044 | 0.04909 | -0.04% | 0.91x |
| 5 | GBP/USD | 58.138 | 1.30959 | +0.03% | 5.03x |
| 6 | PEPE/USD | 50.252 | 3.435e-06 | -0.55% | 0.06x |
| 7 | AUD/USD | 49.219 | 0.66448 | +0.01% | 0.12x |
| 8 | 2Z/USD | 41.020 | 0.01595 | -0.25% | 0.74x |

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

- Persisted scans: 1577; predictions: 13606; observations: 955491.
- Matured sampled outcomes across 1/6/24/48h: 26488; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45398860822 · **Generation:** 1577 · **Legacy run:** 45398860822
**Main quote time:** 2026-11-24T13:02:18.870346+00:00 · **Legacy report time:** 2026-11-24T13:03:30.611453+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.022 | 98.17 | +0.71% | 1.00x | STRONG 74/100 | HIGH 68/100 | Watch |
| 2 | XMR/USD | 499.28 | 78.05 | -0.24% | 1.98x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 3 | MON/USD | 0.01225 | 76.88 | -0.49% | 0.71x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 4 | GBP/USD | 1.30959 | 73.26 | +0.03% | 5.03x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.04909 | 58.93 | -0.04% | 0.91x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 6 | AUD/USD | 0.66448 | 40.46 | +0.01% | 0.12x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 7 | PEPE/USD | 3.435e-06 | 38.15 | -0.55% | 0.06x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | 2Z/USD | 0.01595 | 37.13 | -0.25% | 0.74x | WEAK 24/100 | EXTREME 88/100 | Do nothing |

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
