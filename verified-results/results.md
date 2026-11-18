# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:25:09.266962+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44369390960
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 74d59d473c30f94e502a55e7b0f25348d8fb11bf (atomic ledger/results publication)
**Ledger generation:** 635 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020051 | 70.990 | 72.865 | +7.40% | +0.58% | 0.52x | 6.5 | 2026-11-18T18:25:05.073384+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | MNT/USD | 0.3851 | 53.001 | 51.400 | +3.16% | +0.47% | 0.93x | 5.2 | 2026-11-18T18:25:05.073384+00:00 | Not calibrated | MODERATE 57/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05344 | 46.630 | 46.136 | +3.49% | +1.08% | 0.51x | 18.8 | 2026-11-18T18:25:05.073384+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04529 | 42.605 | 53.615 | +0.89% | -0.53% | 0.16x | 2.2 | 2026-11-18T18:25:05.073384+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.08239 | 28.060 | 34.418 | +0.32% | +0.21% | 0.26x | 6.1 | 2026-11-18T18:25:05.073384+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.865 | 0.020051 | +0.58% | 0.52x |
| 2 | NIGHT/USD | 53.615 | 0.04529 | -0.53% | 0.16x |
| 3 | MNT/USD | 51.400 | 0.3851 | +0.47% | 0.93x |
| 4 | MEGA/USD | 46.136 | 0.05344 | +1.08% | 0.51x |
| 5 | CC/USD | 34.418 | 0.08239 | +0.21% | 0.26x |

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

- Persisted scans: 635; predictions: 5400; observations: 383722.
- Matured sampled outcomes across 1/6/24/48h: 4705; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44369390960 · **Generation:** 635 · **Legacy run:** 44369390960
**Main quote time:** 2026-11-18T18:25:09.266962+00:00 · **Legacy report time:** 2026-11-18T18:25:32.267726+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020051 | 70.99 | +0.58% | 0.52x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 2 | MNT/USD | 0.3851 | 53.00 | +0.47% | 0.93x | MODERATE 57/100 | HIGH 67/100 | Watch |
| 3 | MEGA/USD | 0.05344 | 46.63 | +1.08% | 0.51x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 4 | NIGHT/USD | 0.04529 | 42.60 | -0.53% | 0.16x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | CC/USD | 0.08239 | 28.06 | +0.21% | 0.26x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

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
