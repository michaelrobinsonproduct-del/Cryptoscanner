# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T04:47:35.342279+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46108936122
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8fec39ee396c12d6eed1d78e3350ff06ac4d6de7 (atomic ledger/results publication)
**Ledger generation:** 2107 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 421.39 | 71.731 | 74.162 | +3.47% | -0.13% | 0.82x | 10.2 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | SENT/USD | 0.02448 | 66.030 | 51.091 | +3.23% | -0.01% | 5.10x | 4.9 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ZEC/USD | 750.39 | 63.120 | 67.609 | +2.15% | +0.23% | 0.44x | 4.9 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | VVV/USD | 26.327 | 59.630 | 57.700 | +2.24% | +0.83% | 0.78x | 8.7 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HYPE/USD | 64.24 | 58.934 | 62.490 | +1.18% | +0.06% | 0.61x | 1.6 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0412 | 57.868 | 58.197 | +0.76% | -0.20% | 1.07x | 4.3 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03875 | 44.467 | 33.837 | +0.89% | -0.87% | 39.16x | 10.3 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | BCH/USD | 208.5 | 33.163 | 39.794 | +0.72% | -0.14% | 0.41x | 3.4 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2742 | 21.870 | 25.595 | +0.66% | -0.25% | 0.76x | 21.9 | 2026-11-28T04:47:29.420658+00:00 | Not calibrated | WEAK 6/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.162 | 421.39 | -0.13% | 0.82x |
| 2 | ZEC/USD | 67.609 | 750.39 | +0.23% | 0.44x |
| 3 | HYPE/USD | 62.490 | 64.24 | +0.06% | 0.61x |
| 4 | NEAR/USD | 58.197 | 3.0412 | -0.20% | 1.07x |
| 5 | VVV/USD | 57.700 | 26.327 | +0.83% | 0.78x |
| 6 | SENT/USD | 51.091 | 0.02448 | -0.01% | 5.10x |
| 7 | BCH/USD | 39.794 | 208.5 | -0.14% | 0.41x |
| 8 | SEI/USD | 33.837 | 0.03875 | -0.87% | 39.16x |
| 9 | SPX/USD | 25.595 | 0.2742 | -0.25% | 0.76x |

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

- Persisted scans: 2107; predictions: 18922; observations: 1275888.
- Matured sampled outcomes across 1/6/24/48h: 43954; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46108936122 · **Generation:** 2107 · **Legacy run:** 46108936122
**Main quote time:** 2026-11-28T04:47:35.342279+00:00 · **Legacy report time:** 2026-11-28T04:48:21.140048+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 421.39 | 71.73 | -0.13% | 0.82x | WEAK 36/100 | VERY_HIGH 74/100 | Watch |
| 2 | SENT/USD | 0.02448 | 66.03 | -0.01% | 5.10x | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |
| 3 | ZEC/USD | 750.39 | 63.12 | +0.23% | 0.44x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 4 | VVV/USD | 26.327 | 59.63 | +0.83% | 0.78x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | HYPE/USD | 64.24 | 58.93 | +0.06% | 0.61x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 6 | NEAR/USD | 3.0412 | 57.87 | -0.20% | 1.07x | WEAK 39/100 | HIGH 68/100 | Watch |
| 7 | SEI/USD | 0.03875 | 44.47 | -0.87% | 39.16x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |
| 8 | BCH/USD | 208.5 | 33.16 | -0.14% | 0.41x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | SPX/USD | 0.2742 | 21.87 | -0.25% | 0.76x | WEAK 6/100 | EXTREME 85/100 | Do nothing |

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
