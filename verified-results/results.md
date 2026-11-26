# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T04:56:03.303354+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45758151083
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f522c45612f5d44536b56520326bf7467d67f8bb (atomic ledger/results publication)
**Ledger generation:** 1815 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PAXG/USD | 3585.36 | 71.765 | 57.250 | +0.44% | -0.10% | 13.76x | 1.6 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.56e-06 | 71.717 | 59.451 | +2.18% | -0.17% | 2.31x | 2.8 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SEI/USD | 0.03518 | 67.447 | 66.896 | +5.61% | -0.09% | 1.10x | 8.6 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | LTC/USD | 43.75 | 66.139 | 70.902 | +2.44% | -0.09% | 0.57x | 2.3 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | PIEVERSE/USD | 3.7372 | 64.738 | 60.533 | +5.54% | +1.97% | 0.44x | 27.3 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | ADA/USD | 0.148843 | 64.685 | 68.614 | +2.11% | -0.14% | 0.68x | 2.3 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95695 | 62.639 | 69.978 | +2.18% | +0.26% | 0.14x | 0.5 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SOL/USD | 71.01 | 61.597 | 60.461 | +0.88% | -0.08% | 1.16x | 1.4 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 9 | LINK/USD | 9.22251 | 59.923 | 65.083 | +1.97% | -0.08% | 0.52x | 3.0 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | TAO/USD | 183.5435 | 58.420 | 59.307 | +1.07% | -0.25% | 1.04x | 6.4 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XAUT/USD | 3587.2 | 56.837 | 44.449 | +0.51% | -0.04% | 2.26x | 0.3 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SYRUP/USD | 0.07158 | 55.068 | 62.436 | +8.01% | -0.92% | 0.72x | 29.4 | 2026-11-26T04:55:57.437868+00:00 | Not calibrated | WEAK 23/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 70.902 | 43.75 | -0.09% | 0.57x |
| 2 | XRP/USD | 69.978 | 0.95695 | +0.26% | 0.14x |
| 3 | ADA/USD | 68.614 | 0.148843 | -0.14% | 0.68x |
| 4 | SEI/USD | 66.896 | 0.03518 | -0.09% | 1.10x |
| 5 | LINK/USD | 65.083 | 9.22251 | -0.08% | 0.52x |
| 6 | SYRUP/USD | 62.436 | 0.07158 | -0.92% | 0.72x |
| 7 | PIEVERSE/USD | 60.533 | 3.7372 | +1.97% | 0.44x |
| 8 | SOL/USD | 60.461 | 71.01 | -0.08% | 1.16x |
| 9 | PEPE/USD | 59.451 | 3.56e-06 | -0.17% | 2.31x |
| 10 | TAO/USD | 59.307 | 183.5435 | -0.25% | 1.04x |
| 11 | PAXG/USD | 57.250 | 3585.36 | -0.10% | 13.76x |
| 12 | XAUT/USD | 44.449 | 3587.2 | -0.04% | 2.26x |

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

- Persisted scans: 1815; predictions: 15515; observations: 1100379.
- Matured sampled outcomes across 1/6/24/48h: 33671; gap abstentions: 23904. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45758151083 · **Generation:** 1815 · **Legacy run:** 45758151083
**Main quote time:** 2026-11-26T04:56:03.303354+00:00 · **Legacy report time:** 2026-11-26T04:56:59.051123+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD | 3585.36 | 71.77 | -0.10% | 13.76x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | PEPE/USD | 3.56e-06 | 71.72 | -0.17% | 2.31x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | SEI/USD | 0.03518 | 67.45 | -0.09% | 1.10x | WEAK 44/100 | VERY_HIGH 73/100 | Watch |
| 4 | LTC/USD | 43.75 | 66.14 | -0.09% | 0.57x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 5 | PIEVERSE/USD | 3.7372 | 64.74 | +1.97% | 0.44x | MODERATE 52/100 | EXTREME 87/100 | Do nothing |
| 6 | ADA/USD | 0.148843 | 64.68 | -0.14% | 0.68x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 7 | XRP/USD | 0.95695 | 62.64 | +0.26% | 0.14x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 8 | SOL/USD | 71.01 | 61.60 | -0.08% | 1.16x | WEAK 41/100 | HIGH 68/100 | Watch |
| 9 | LINK/USD | 9.22251 | 59.92 | -0.08% | 0.52x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | TAO/USD | 183.5435 | 58.42 | -0.25% | 1.04x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | XAUT/USD | 3587.2 | 56.84 | -0.04% | 2.26x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 12 | SYRUP/USD | 0.07158 | 55.07 | -0.92% | 0.72x | WEAK 23/100 | EXTREME 93/100 | Do nothing |

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
