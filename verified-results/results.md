# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T07:30:36.243575+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44880484022
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 2d4043cd5cf4496d05f3703c446e8aabf04c093e (atomic ledger/results publication)
**Ledger generation:** 1102 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.473 | 62.261 | 74.189 | +3.54% | -0.91% | 0.26x | 11.2 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 2 | ETH/USD | 1633 | 58.454 | 60.883 | +0.84% | +0.04% | 0.74x | 0.1 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | TRX/USD | 0.302332 | 50.723 | 56.527 | +0.27% | -0.08% | 0.46x | 0.3 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.093452 | 44.392 | 40.780 | +2.09% | -0.67% | 1.70x | 15.2 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | SENT/USD | 0.020684 | 35.172 | 29.848 | +0.43% | +1.20% | 0.93x | 8.2 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | MORPHO/USD | 1.54605 | 23.972 | 31.405 | +0.95% | -0.13% | 0.32x | 19.5 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | PEAQ/USD | 0.01997 | 22.206 | 28.637 | +0.40% | +0.45% | 0.13x | 10.0 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | A/USD | 0.0638 | 16.634 | 17.650 | +0.31% | -0.31% | 1.05x | 31.4 | 2026-11-21T07:30:30.659672+00:00 | Not calibrated | WEAK 8/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 74.189 | 21.473 | -0.91% | 0.26x |
| 2 | ETH/USD | 60.883 | 1633 | +0.04% | 0.74x |
| 3 | TRX/USD | 56.527 | 0.302332 | -0.08% | 0.46x |
| 4 | CAP/USD | 40.780 | 0.093452 | -0.67% | 1.70x |
| 5 | MORPHO/USD | 31.405 | 1.54605 | -0.13% | 0.32x |
| 6 | SENT/USD | 29.848 | 0.020684 | +1.20% | 0.93x |
| 7 | PEAQ/USD | 28.637 | 0.01997 | +0.45% | 0.13x |
| 8 | A/USD | 17.650 | 0.0638 | -0.31% | 1.05x |

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

- Persisted scans: 1102; predictions: 8687; observations: 666375.
- Matured sampled outcomes across 1/6/24/48h: 11285; gap abstentions: 20174. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44880484022 · **Generation:** 1102 · **Legacy run:** 44880484022
**Main quote time:** 2026-11-21T07:30:36.243575+00:00 · **Legacy report time:** 2026-11-21T07:31:25.235601+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.473 | 62.26 | -0.91% | 0.26x | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing |
| 2 | ETH/USD | 1633 | 58.45 | +0.04% | 0.74x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 3 | TRX/USD | 0.302332 | 50.72 | -0.08% | 0.46x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | CAP/USD | 0.093452 | 44.39 | -0.67% | 1.70x | WEAK 37/100 | VERY_HIGH 72/100 | Watch |
| 5 | SENT/USD | 0.020684 | 35.17 | +1.20% | 0.93x | MODERATE 48/100 | VERY_HIGH 74/100 | Watch |
| 6 | MORPHO/USD | 1.54605 | 23.97 | -0.13% | 0.32x | WEAK 12/100 | EXTREME 87/100 | Do nothing |
| 7 | PEAQ/USD | 0.01997 | 22.21 | +0.45% | 0.13x | WEAK 36/100 | EXTREME 88/100 | Do nothing |
| 8 | A/USD | 0.0638 | 16.63 | -0.31% | 1.05x | WEAK 8/100 | EXTREME 92/100 | Do nothing |

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
