# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T13:21:55.554449+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46006129283
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f21dcfd40b76658eefaf057356795faa4f5f296a (atomic ledger/results publication)
**Ledger generation:** 2013 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.93 | 93.013 | 95.981 | +5.96% | -0.09% | 0.75x | 1.5 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ZEC/USD | 756.24 | 85.593 | 97.224 | +10.94% | -0.96% | 0.31x | 5.6 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SOL/USD | 73.16 | 75.549 | 76.222 | +3.13% | -0.01% | 0.94x | 1.4 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 4 | VVV/USD | 27.279 | 74.599 | 76.519 | +4.19% | -0.73% | 1.17x | 9.5 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0585637 | 73.314 | 72.613 | +3.88% | +0.01% | 1.06x | 2.4 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6862 | 72.561 | 73.666 | +2.77% | -0.04% | 0.91x | 1.5 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ETH/USD | 1718.31 | 70.086 | 67.675 | +1.81% | -0.19% | 1.34x | 0.1 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.96937 | 69.892 | 74.301 | +2.82% | -0.33% | 0.73x | 0.9 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.0491 | 67.481 | 59.296 | +1.30% | +1.12% | 1.26x | 2.0 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 10 | FET/USD | 0.1297 | 66.950 | 72.301 | +7.72% | -0.69% | 0.81x | 15.4 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | XBT/USD | 61379.8 | 59.951 | 65.195 | +1.46% | -0.24% | 0.60x | 0.0 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | PAXG/USD | 3631.19 | 58.238 | 55.799 | +2.09% | -0.55% | 1.52x | 0.2 | 2026-11-27T13:21:48.692008+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.224 | 756.24 | -0.96% | 0.31x |
| 2 | HYPE/USD | 95.981 | 65.93 | -0.09% | 0.75x |
| 3 | VVV/USD | 76.519 | 27.279 | -0.73% | 1.17x |
| 4 | SOL/USD | 76.222 | 73.16 | -0.01% | 0.94x |
| 5 | XRP/USD | 74.301 | 0.96937 | -0.33% | 0.73x |
| 6 | SUI/USD | 73.666 | 0.6862 | -0.04% | 0.91x |
| 7 | XDG/USD | 72.613 | 0.0585637 | +0.01% | 1.06x |
| 8 | FET/USD | 72.301 | 0.1297 | -0.69% | 0.81x |
| 9 | ETH/USD | 67.675 | 1718.31 | -0.19% | 1.34x |
| 10 | XBT/USD | 65.195 | 61379.8 | -0.24% | 0.60x |
| 11 | NIGHT/USD | 59.296 | 0.0491 | +1.12% | 1.26x |
| 12 | PAXG/USD | 55.799 | 3631.19 | -0.55% | 1.52x |

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

- Persisted scans: 2013; predictions: 17858; observations: 1218988.
- Matured sampled outcomes across 1/6/24/48h: 39785; gap abstentions: 25858. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46006129283 · **Generation:** 2013 · **Legacy run:** 46006129283
**Main quote time:** 2026-11-27T13:21:55.554449+00:00 · **Legacy report time:** 2026-11-27T13:22:37.581092+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.93 | 93.01 | -0.09% | 0.75x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 2 | ZEC/USD | 756.24 | 85.59 | -0.96% | 0.31x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | SOL/USD | 73.16 | 75.55 | -0.01% | 0.94x | WEAK 43/100 | HIGH 68/100 | Watch |
| 4 | VVV/USD | 27.279 | 74.60 | -0.73% | 1.17x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 5 | XDG/USD | 0.0585637 | 73.31 | +0.01% | 1.06x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 6 | SUI/USD | 0.6862 | 72.56 | -0.04% | 0.91x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | ETH/USD | 1718.31 | 70.09 | -0.19% | 1.34x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.96937 | 69.89 | -0.33% | 0.73x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | NIGHT/USD | 0.0491 | 67.48 | +1.12% | 1.26x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 10 | FET/USD | 0.1297 | 66.95 | -0.69% | 0.81x | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | XBT/USD | 61379.8 | 59.95 | -0.24% | 0.60x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | PAXG/USD | 3631.19 | 58.24 | -0.55% | 1.52x | MODERATE 49/100 | HIGH 61/100 | Watch |

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
