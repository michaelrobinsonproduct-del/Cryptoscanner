# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T15:30:56.393296+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44919449594
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 81248542c6e4a7cf78d769daaaa7cb88a18857e3 (atomic ledger/results publication)
**Ledger generation:** 1151 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.97 | 93.475 | 95.861 | +10.76% | -1.24% | 1.38x | 8.3 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 67/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | TAO/USD | 186.9282 | 83.939 | 77.544 | +3.56% | -1.15% | 2.21x | 4.7 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | STRONG 72/100 | HIGH 65/100 | Watch | WATCH |
| 3 | ZEC/USD | 782.99 | 83.571 | 74.716 | +3.31% | -1.23% | 2.51x | 6.9 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | STRONG 72/100 | HIGH 65/100 | Do nothing | WATCH |
| 4 | ETH/USD | 1676.77 | 80.328 | 79.268 | +3.55% | -0.64% | 1.43x | 1.1 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XBT/USD | 59803.9 | 76.757 | 66.865 | +1.70% | -0.55% | 2.26x | 0.0 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | BEAM/USD | 0.003555 | 74.594 | 68.353 | +8.45% | +0.74% | 1.26x | 17.0 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 67/100 | HIGH 66/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.625 | 73.513 | 66.290 | +1.83% | -0.44% | 1.94x | 3.0 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 8 | UNI/USD | 4.668 | 71.277 | 82.713 | +4.50% | -1.24% | 0.48x | 7.5 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | XRP/USD | 0.92049 | 66.260 | 63.259 | +1.30% | -0.91% | 1.76x | 1.6 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.08177 | 66.208 | 75.529 | +9.76% | -0.44% | 0.29x | 20.8 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | SOL/USD | 70.09 | 66.132 | 68.346 | +2.01% | -0.85% | 1.20x | 1.4 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XLM/USD | 0.12839 | 66.062 | 61.504 | +0.93% | -0.71% | 1.81x | 0.1 | 2026-11-21T15:30:47.525422+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.861 | 22.97 | -1.24% | 1.38x |
| 2 | UNI/USD | 82.713 | 4.668 | -1.24% | 0.48x |
| 3 | ETH/USD | 79.268 | 1676.77 | -0.64% | 1.43x |
| 4 | TAO/USD | 77.544 | 186.9282 | -1.15% | 2.21x |
| 5 | USELESS/USD | 75.529 | 0.08177 | -0.44% | 0.29x |
| 6 | ZEC/USD | 74.716 | 782.99 | -1.23% | 2.51x |
| 7 | BEAM/USD | 68.353 | 0.003555 | +0.74% | 1.26x |
| 8 | SOL/USD | 68.346 | 70.09 | -0.85% | 1.20x |
| 9 | XBT/USD | 66.865 | 59803.9 | -0.55% | 2.26x |
| 10 | AVAX/USD | 66.290 | 6.625 | -0.44% | 1.94x |
| 11 | XRP/USD | 63.259 | 0.92049 | -0.91% | 1.76x |
| 12 | XLM/USD | 61.504 | 0.12839 | -0.71% | 1.81x |

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

- Persisted scans: 1151; predictions: 9121; observations: 696167.
- Matured sampled outcomes across 1/6/24/48h: 11985; gap abstentions: 20668. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44919449594 · **Generation:** 1151 · **Legacy run:** 44919449594
**Main quote time:** 2026-11-21T15:30:56.393296+00:00 · **Legacy report time:** 2026-11-21T15:32:00.537200+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.97 | 93.48 | -1.24% | 1.38x | MODERATE 67/100 | HIGH 65/100 | Do nothing |
| 2 | TAO/USD | 186.9282 | 83.94 | -1.15% | 2.21x | STRONG 72/100 | HIGH 65/100 | Watch |
| 3 | ZEC/USD | 782.99 | 83.57 | -1.23% | 2.51x | STRONG 72/100 | HIGH 65/100 | Do nothing |
| 4 | ETH/USD | 1676.77 | 80.33 | -0.64% | 1.43x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | XBT/USD | 59803.9 | 76.76 | -0.55% | 2.26x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | BEAM/USD | 0.003555 | 74.59 | +0.74% | 1.26x | MODERATE 67/100 | HIGH 66/100 | Watch |
| 7 | AVAX/USD | 6.625 | 73.51 | -0.44% | 1.94x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 8 | UNI/USD | 4.668 | 71.28 | -1.24% | 0.48x | WEAK 41/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | XRP/USD | 0.92049 | 66.26 | -0.91% | 1.76x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | USELESS/USD | 0.08177 | 66.21 | -0.44% | 0.29x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 11 | SOL/USD | 70.09 | 66.13 | -0.85% | 1.20x | WEAK 43/100 | HIGH 68/100 | Watch |
| 12 | XLM/USD | 0.12839 | 66.06 | -0.71% | 1.81x | MODERATE 53/100 | HIGH 61/100 | Watch |

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
