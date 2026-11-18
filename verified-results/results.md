# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:50:02.993902+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44239984895
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** f0a2dcb0026d8e41c566ed56e4bcf27181e6bbc6 (atomic ledger/results publication)
**Ledger generation:** 535 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2896 | 71.558 | 59.651 | +4.89% | -0.62% | 5.71x | 13.8 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | XDC/USD | 0.03088 | 62.277 | 49.051 | +1.85% | -0.35% | 3.94x | 3.2 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 3 | UP/USD | 0.05547 | 55.833 | 61.165 | +4.68% | -0.25% | 0.59x | 7.2 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 4 | UAI/USD | 0.03363 | 44.697 | 30.291 | +0.75% | -0.12% | 5.31x | 11.9 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | SENT/USD | 0.019309 | 44.247 | 50.789 | +3.43% | +0.15% | 0.27x | 8.3 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5112 | 38.642 | 26.172 | +0.37% | -0.51% | 6.34x | 17.6 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | CC/USD | 0.08323 | 38.235 | 41.359 | +1.34% | -0.08% | 0.73x | 7.2 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | PEARL/USD | 1.8433 | 32.225 | 38.170 | +1.81% | +0.21% | 0.30x | 19.0 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | MELANIA/USD | 0.0503 | 28.581 | 43.777 | +3.29% | -1.97% | 0.46x | 20.0 | 2026-11-18T04:49:57.342221+00:00 | Not calibrated | WEAK 14/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 61.165 | 0.05547 | -0.25% | 0.59x |
| 2 | ICNT/USD | 59.651 | 0.2896 | -0.62% | 5.71x |
| 3 | SENT/USD | 50.789 | 0.019309 | +0.15% | 0.27x |
| 4 | XDC/USD | 49.051 | 0.03088 | -0.35% | 3.94x |
| 5 | MELANIA/USD | 43.777 | 0.0503 | -1.97% | 0.46x |
| 6 | CC/USD | 41.359 | 0.08323 | -0.08% | 0.73x |
| 7 | PEARL/USD | 38.170 | 1.8433 | +0.21% | 0.30x |
| 8 | UAI/USD | 30.291 | 0.03363 | -0.12% | 5.31x |
| 9 | AKT/USD | 26.172 | 0.5112 | -0.51% | 6.34x |

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

- Persisted scans: 535; predictions: 4521; observations: 322822.
- Matured sampled outcomes across 1/6/24/48h: 3593; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44239984895 · **Generation:** 535 · **Legacy run:** 44239984895
**Main quote time:** 2026-11-18T04:50:02.993902+00:00 · **Legacy report time:** 2026-11-18T04:50:18.917682+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2896 | 71.56 | -0.62% | 5.71x | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |
| 2 | XDC/USD | 0.03088 | 62.28 | -0.35% | 3.94x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 3 | UP/USD | 0.05547 | 55.83 | -0.25% | 0.59x | WEAK 33/100 | VERY_HIGH 81/100 | Do nothing |
| 4 | UAI/USD | 0.03363 | 44.70 | -0.12% | 5.31x | MODERATE 47/100 | VERY_HIGH 79/100 | Watch |
| 5 | SENT/USD | 0.019309 | 44.25 | +0.15% | 0.27x | WEAK 42/100 | VERY_HIGH 82/100 | Watch |
| 6 | AKT/USD | 0.5112 | 38.64 | -0.51% | 6.34x | WEAK 44/100 | VERY_HIGH 72/100 | Watch |
| 7 | CC/USD | 0.08323 | 38.23 | -0.08% | 0.73x | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | PEARL/USD | 1.8433 | 32.23 | +0.21% | 0.30x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 9 | MELANIA/USD | 0.0503 | 28.58 | -1.97% | 0.46x | WEAK 14/100 | EXTREME 98/100 | Do nothing |

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
