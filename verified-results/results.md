# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:30:05.765445+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44237685414
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** f83e4c9b4abd0c3f14905f3a6c9677cc1f7dfe7b (atomic ledger/results publication)
**Ledger generation:** 531 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.291 | 75.429 | 49.364 | +5.40% | +2.21% | 5.80x | 41.5 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019155 | 55.708 | 44.429 | +2.60% | +0.44% | 1.91x | 9.4 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 3 | XDC/USD | 0.031 | 47.490 | 49.951 | +2.24% | +0.71% | 0.40x | 6.5 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.8339 | 42.479 | 36.377 | +1.29% | -0.11% | 1.66x | 15.3 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | CC/USD | 0.08333 | 41.157 | 43.952 | +1.46% | -0.94% | 1.19x | 3.6 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | MELANIA/USD | 0.0508 | 33.688 | 41.196 | +4.31% | -0.39% | 0.45x | 39.4 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | ZAMA/USD | 0.06081 | 31.945 | 36.980 | +1.47% | -0.62% | 0.81x | 13.2 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5166 | 27.987 | 35.613 | +1.43% | +0.14% | 0.17x | 13.6 | 2026-11-18T04:30:00.457663+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XDC/USD | 49.951 | 0.031 | +0.71% | 0.40x |
| 2 | ICNT/USD | 49.364 | 0.291 | +2.21% | 5.80x |
| 3 | SENT/USD | 44.429 | 0.019155 | +0.44% | 1.91x |
| 4 | CC/USD | 43.952 | 0.08333 | -0.94% | 1.19x |
| 5 | MELANIA/USD | 41.196 | 0.0508 | -0.39% | 0.45x |
| 6 | ZAMA/USD | 36.980 | 0.06081 | -0.62% | 0.81x |
| 7 | PEARL/USD | 36.377 | 1.8339 | -0.11% | 1.66x |
| 8 | AKT/USD | 35.613 | 0.5166 | +0.14% | 0.17x |

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

- Persisted scans: 531; predictions: 4488; observations: 320386.
- Matured sampled outcomes across 1/6/24/48h: 3572; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44237685414 · **Generation:** 531 · **Legacy run:** 44237685414
**Main quote time:** 2026-11-18T04:30:05.765445+00:00 · **Legacy report time:** 2026-11-18T04:30:23.232633+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.291 | 75.43 | +2.21% | 5.80x | STRONG 88/100 | VERY_HIGH 82/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019155 | 55.71 | +0.44% | 1.91x | STRONG 83/100 | HIGH 67/100 | Consider small entry |
| 3 | XDC/USD | 0.031 | 47.49 | +0.71% | 0.40x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 4 | PEARL/USD | 1.8339 | 42.48 | -0.11% | 1.66x | WEAK 36/100 | VERY_HIGH 72/100 | Watch |
| 5 | CC/USD | 0.08333 | 41.16 | -0.94% | 1.19x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | MELANIA/USD | 0.0508 | 33.69 | -0.39% | 0.45x | WEAK 7/100 | EXTREME 100/100 | Do nothing |
| 7 | ZAMA/USD | 0.06081 | 31.94 | -0.62% | 0.81x | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing |
| 8 | AKT/USD | 0.5166 | 27.99 | +0.14% | 0.17x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2873 | 86.03 | +2.21% | 5.80x | 3786 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.01919 | 67.63 | +0.44% | 1.91x | 4002 | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 3 | UAI/USD | 0.03345 | 23.44 | +0.45% | 1.35x | 2107 | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ICNT/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
