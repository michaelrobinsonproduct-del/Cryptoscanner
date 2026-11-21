# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:35:33.762728+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44856644175
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 1b0c39abfb599ecbdc96b957f8719415fac73ab3 (atomic ledger/results publication)
**Ledger generation:** 1065 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.26582 | 84.940 | 61.980 | +8.26% | +1.59% | 16.19x | 38.9 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | VVV/USD | 20.951 | 69.395 | 57.385 | +1.02% | -0.60% | 3.08x | 9.5 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CAP/USD | 0.09447 | 50.271 | 53.422 | +3.20% | +0.23% | 0.57x | 4.7 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | STBL/USD | 0.016171 | 42.117 | 43.697 | +1.86% | +0.54% | 0.57x | 0.6 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.07345 | 29.843 | 37.393 | +0.40% | -0.12% | 0.31x | 8.2 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | DCR/USD | 10.191 | 21.250 | 29.843 | +0.85% | -0.39% | 0.34x | 13.7 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | AB/USD | 0.000527 | 12.791 | 17.946 | +0.38% | -0.38% | 0.67x | 38.0 | 2026-11-21T02:35:26.722315+00:00 | Not calibrated | WEAK 0/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 61.980 | 0.26582 | +1.59% | 16.19x |
| 2 | VVV/USD | 57.385 | 20.951 | -0.60% | 3.08x |
| 3 | CAP/USD | 53.422 | 0.09447 | +0.23% | 0.57x |
| 4 | STBL/USD | 43.697 | 0.016171 | +0.54% | 0.57x |
| 5 | ALGO/USD | 37.393 | 0.07345 | -0.12% | 0.31x |
| 6 | DCR/USD | 29.843 | 10.191 | -0.39% | 0.34x |
| 7 | AB/USD | 17.946 | 0.000527 | -0.38% | 0.67x |

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

- Persisted scans: 1065; predictions: 8549; observations: 643880.
- Matured sampled outcomes across 1/6/24/48h: 10998; gap abstentions: 19424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44856644175 · **Generation:** 1065 · **Legacy run:** 44856644175
**Main quote time:** 2026-11-21T02:35:33.762728+00:00 · **Legacy report time:** 2026-11-21T02:36:37.245755+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.26582 | 84.94 | +1.59% | 16.19x | STRONG 92/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD | 20.951 | 69.40 | -0.60% | 3.08x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | CAP/USD | 0.09447 | 50.27 | +0.23% | 0.57x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 4 | STBL/USD | 0.016171 | 42.12 | +0.54% | 0.57x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 5 | ALGO/USD | 0.07345 | 29.84 | -0.12% | 0.31x | WEAK 20/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | DCR/USD | 10.191 | 21.25 | -0.39% | 0.34x | WEAK 11/100 | EXTREME 94/100 | Do nothing |
| 7 | AB/USD | 0.000527 | 12.79 | -0.38% | 0.67x | WEAK 0/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.26323 | 86.61 | +1.59% | 16.19x | 6652 | STRONG 100/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
