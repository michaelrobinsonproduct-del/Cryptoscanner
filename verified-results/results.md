# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T07:40:45.396839+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44881258506
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 63c9123eed2c16c01f8ae2cc8164c08c649aa1a3 (atomic ledger/results publication)
**Ledger generation:** 1103 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.404 | 61.417 | 73.488 | +3.21% | -0.77% | 0.18x | 7.9 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ETH/USD | 1634.45 | 53.743 | 61.510 | +0.93% | -0.08% | 0.27x | 0.1 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.094325 | 50.495 | 49.029 | +3.04% | -0.01% | 1.15x | 12.1 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | TRX/USD | 0.302633 | 49.027 | 56.804 | +0.37% | +0.06% | 0.19x | 1.1 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SENT/USD | 0.020936 | 41.202 | 38.230 | +1.66% | +1.14% | 0.73x | 8.6 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | A/USD | 0.0639 | 29.931 | 26.641 | +0.47% | +0.16% | 1.25x | 15.6 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.0572 | 26.691 | 26.574 | +0.33% | -0.38% | 1.20x | 14.0 | 2026-11-21T07:40:39.373451+00:00 | Not calibrated | WEAK 18/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.488 | 21.404 | -0.77% | 0.18x |
| 2 | ETH/USD | 61.510 | 1634.45 | -0.08% | 0.27x |
| 3 | TRX/USD | 56.804 | 0.302633 | +0.06% | 0.19x |
| 4 | CAP/USD | 49.029 | 0.094325 | -0.01% | 1.15x |
| 5 | SENT/USD | 38.230 | 0.020936 | +1.14% | 0.73x |
| 6 | A/USD | 26.641 | 0.0639 | +0.16% | 1.25x |
| 7 | ZAMA/USD | 26.574 | 0.0572 | -0.38% | 1.20x |

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

- Persisted scans: 1103; predictions: 8694; observations: 666983.
- Matured sampled outcomes across 1/6/24/48h: 11310; gap abstentions: 20190. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44881258506 · **Generation:** 1103 · **Legacy run:** 44881258506
**Main quote time:** 2026-11-21T07:40:45.396839+00:00 · **Legacy report time:** 2026-11-21T07:41:31.731479+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.404 | 61.42 | -0.77% | 0.18x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 2 | ETH/USD | 1634.45 | 53.74 | -0.08% | 0.27x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | CAP/USD | 0.094325 | 50.49 | -0.01% | 1.15x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | TRX/USD | 0.302633 | 49.03 | +0.06% | 0.19x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 5 | SENT/USD | 0.020936 | 41.20 | +1.14% | 0.73x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 6 | A/USD | 0.0639 | 29.93 | +0.16% | 1.25x | WEAK 35/100 | VERY_HIGH 73/100 | Watch |
| 7 | ZAMA/USD | 0.0572 | 26.69 | -0.38% | 1.20x | WEAK 18/100 | EXTREME 86/100 | Do nothing |

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
