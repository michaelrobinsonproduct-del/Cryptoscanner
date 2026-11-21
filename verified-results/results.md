# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:35:34.026637+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44850978235
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** ccf167f14883166285ba44d7a469130b84c5af1c (atomic ledger/results publication)
**Ledger generation:** 1056 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.327 | 92.233 | 71.093 | +2.84% | +1.23% | 4.48x | 7.5 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PIEVERSE/USD | 3.0497 | 42.514 | 42.852 | +1.70% | -0.08% | 1.01x | 7.9 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 3 | BLESS/USD | 0.014073 | 37.723 | 36.059 | +2.19% | +1.42% | 0.46x | 29.7 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 39/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | SKY/USD | 0.04416 | 34.224 | 36.372 | +0.73% | +0.00% | 0.79x | 9.1 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 37/100 | HIGH 67/100 | Watch | WATCH |
| 5 | CT/USD | 0.1227 | 33.709 | 28.992 | +1.32% | -0.24% | 1.59x | 24.4 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 6 | AB/USD | 0.000531 | 31.261 | 22.813 | +1.14% | +2.91% | 0.39x | 37.7 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | MEGA/USD | 0.04806 | 30.672 | 24.026 | +0.46% | +0.63% | 1.35x | 23.0 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | DCR/USD | 10.166 | 28.823 | 30.522 | +0.60% | +0.25% | 0.71x | 8.9 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | BLUR/USD | 0.00735 | 21.333 | 23.193 | +0.68% | -0.68% | 1.15x | 27.2 | 2026-11-21T01:35:25.446116+00:00 | Not calibrated | WEAK 11/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 71.093 | 21.327 | +1.23% | 4.48x |
| 2 | PIEVERSE/USD | 42.852 | 3.0497 | -0.08% | 1.01x |
| 3 | SKY/USD | 36.372 | 0.04416 | +0.00% | 0.79x |
| 4 | BLESS/USD | 36.059 | 0.014073 | +1.42% | 0.46x |
| 5 | DCR/USD | 30.522 | 10.166 | +0.25% | 0.71x |
| 6 | CT/USD | 28.992 | 0.1227 | -0.24% | 1.59x |
| 7 | MEGA/USD | 24.026 | 0.04806 | +0.63% | 1.35x |
| 8 | BLUR/USD | 23.193 | 0.00735 | -0.68% | 1.15x |
| 9 | AB/USD | 22.813 | 0.000531 | +2.91% | 0.39x |

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

- Persisted scans: 1056; predictions: 8467; observations: 638408.
- Matured sampled outcomes across 1/6/24/48h: 10939; gap abstentions: 19215. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44850978235 · **Generation:** 1056 · **Legacy run:** 44850978235
**Main quote time:** 2026-11-21T01:35:34.026637+00:00 · **Legacy report time:** 2026-11-21T01:36:20.868182+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.327 | 92.23 | +1.23% | 4.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PIEVERSE/USD | 3.0497 | 42.51 | -0.08% | 1.01x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 3 | BLESS/USD | 0.014073 | 37.72 | +1.42% | 0.46x | WEAK 39/100 | EXTREME 87/100 | Do nothing |
| 4 | SKY/USD | 0.04416 | 34.22 | +0.00% | 0.79x | WEAK 37/100 | HIGH 67/100 | Watch |
| 5 | CT/USD | 0.1227 | 33.71 | -0.24% | 1.59x | WEAK 27/100 | VERY_HIGH 78/100 | Do nothing |
| 6 | AB/USD | 0.000531 | 31.26 | +2.91% | 0.39x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 7 | MEGA/USD | 0.04806 | 30.67 | +0.63% | 1.35x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 8 | DCR/USD | 10.166 | 28.82 | +0.25% | 0.71x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |
| 9 | BLUR/USD | 0.00735 | 21.33 | -0.68% | 1.15x | WEAK 11/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.314 | 81.95 | +1.23% | 4.48x | 11772 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
