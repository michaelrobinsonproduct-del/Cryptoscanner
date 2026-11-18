# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:40:16.526541+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44238844822
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 54634acff65323a348fa9ec30ddeb1f77fc238c3 (atomic ledger/results publication)
**Ledger generation:** 533 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2859 | 61.120 | 48.387 | +3.55% | -0.45% | 5.91x | 17.5 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | XDC/USD | 0.03111 | 53.482 | 49.469 | +2.61% | +0.91% | 0.95x | 12.9 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 3 | CC/USD | 0.0835 | 42.381 | 44.826 | +1.67% | +0.14% | 0.68x | 4.8 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03377 | 37.276 | 25.798 | +1.17% | +1.17% | 1.56x | 26.8 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.8448 | 37.046 | 40.374 | +1.89% | +0.67% | 0.33x | 15.8 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | SENT/USD | 0.019094 | 35.037 | 42.918 | +2.28% | -0.15% | 0.29x | 7.9 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5119 | 22.564 | 29.066 | +0.51% | -1.08% | 0.89x | 13.7 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | WEAK 11/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 8 | MELANIA/USD | 0.0499 | 13.421 | 27.896 | +2.46% | -2.16% | 0.63x | 40.2 | 2026-11-18T04:40:10.683084+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XDC/USD | 49.469 | 0.03111 | +0.91% | 0.95x |
| 2 | ICNT/USD | 48.387 | 0.2859 | -0.45% | 5.91x |
| 3 | CC/USD | 44.826 | 0.0835 | +0.14% | 0.68x |
| 4 | SENT/USD | 42.918 | 0.019094 | -0.15% | 0.29x |
| 5 | PEARL/USD | 40.374 | 1.8448 | +0.67% | 0.33x |
| 6 | AKT/USD | 29.066 | 0.5119 | -1.08% | 0.89x |
| 7 | MELANIA/USD | 27.896 | 0.0499 | -2.16% | 0.63x |
| 8 | UAI/USD | 25.798 | 0.03377 | +1.17% | 1.56x |

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

- Persisted scans: 533; predictions: 4504; observations: 321604.
- Matured sampled outcomes across 1/6/24/48h: 3578; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44238844822 · **Generation:** 533 · **Legacy run:** 44238844822
**Main quote time:** 2026-11-18T04:40:16.526541+00:00 · **Legacy report time:** 2026-11-18T04:40:33.082058+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2859 | 61.12 | -0.45% | 5.91x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 2 | XDC/USD | 0.03111 | 53.48 | +0.91% | 0.95x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 3 | CC/USD | 0.0835 | 42.38 | +0.14% | 0.68x | WEAK 41/100 | VERY_HIGH 75/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03377 | 37.28 | +1.17% | 1.56x | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |
| 5 | PEARL/USD | 1.8448 | 37.05 | +0.67% | 0.33x | WEAK 44/100 | VERY_HIGH 81/100 | Watch |
| 6 | SENT/USD | 0.019094 | 35.04 | -0.15% | 0.29x | WEAK 23/100 | EXTREME 88/100 | Do nothing |
| 7 | AKT/USD | 0.5119 | 22.56 | -1.08% | 0.89x | WEAK 11/100 | VERY_HIGH 83/100 | Do nothing |
| 8 | MELANIA/USD | 0.0499 | 13.42 | -2.16% | 0.63x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UAI/USD ⭐ | 0.03377 | 37.84 | +1.17% | 1.56x | 2094 | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
