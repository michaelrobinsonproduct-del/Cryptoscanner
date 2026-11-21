# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T07:10:37.072881+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44878918205
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** d3ef3667768520e70948a2560c6167f769543de2 (atomic ledger/results publication)
**Ledger generation:** 1100 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.828 | 102.031 | 84.197 | +5.25% | +0.57% | 8.57x | 15.1 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | ETH/USD | 1642.19 | 74.566 | 63.546 | +1.41% | -0.14% | 2.17x | 2.7 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TRX/USD | 0.302672 | 74.149 | 57.450 | +0.39% | +0.34% | 2.79x | 0.0 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | DRV/USD | 0.26661 | 72.869 | 73.575 | +8.58% | +0.74% | 0.56x | 19.2 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | RARE/USD | 0.01398 | 65.111 | 56.996 | +5.11% | +1.01% | 1.31x | 21.5 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04474 | 56.075 | 42.967 | +2.05% | -0.38% | 7.92x | 13.4 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | CAP/USD | 0.094481 | 55.014 | 51.213 | +3.21% | +1.25% | 0.76x | 10.1 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | CT/USD | 0.1233 | 41.210 | 32.258 | +1.82% | +1.15% | 1.32x | 24.4 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | RAY/USD | 1.287 | 39.061 | 24.061 | +0.31% | +0.00% | 4.74x | 23.3 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | BLUR/USD | 0.00736 | 35.388 | 24.058 | +0.82% | +1.52% | 1.37x | 27.3 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | ZAMA/USD | 0.05783 | 33.128 | 34.351 | +1.44% | +0.35% | 0.70x | 13.9 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | WEAK 42/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | STBL/USD | 0.015966 | 32.123 | 26.574 | +0.57% | +0.36% | 1.38x | 16.9 | 2026-11-21T07:10:30.206682+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 84.197 | 21.828 | +0.57% | 8.57x |
| 2 | DRV/USD | 73.575 | 0.26661 | +0.74% | 0.56x |
| 3 | ETH/USD | 63.546 | 1642.19 | -0.14% | 2.17x |
| 4 | TRX/USD | 57.450 | 0.302672 | +0.34% | 2.79x |
| 5 | RARE/USD | 56.996 | 0.01398 | +1.01% | 1.31x |
| 6 | CAP/USD | 51.213 | 0.094481 | +1.25% | 0.76x |
| 7 | SKY/USD | 42.967 | 0.04474 | -0.38% | 7.92x |
| 8 | ZAMA/USD | 34.351 | 0.05783 | +0.35% | 0.70x |
| 9 | CT/USD | 32.258 | 0.1233 | +1.15% | 1.32x |
| 10 | STBL/USD | 26.574 | 0.015966 | +0.36% | 1.38x |
| 11 | RAY/USD | 24.061 | 1.287 | +0.00% | 4.74x |
| 12 | BLUR/USD | 24.058 | 0.00736 | +1.52% | 1.37x |

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

- Persisted scans: 1100; predictions: 8669; observations: 665159.
- Matured sampled outcomes across 1/6/24/48h: 11249; gap abstentions: 20159. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44878918205 · **Generation:** 1100 · **Legacy run:** 44878918205
**Main quote time:** 2026-11-21T07:10:37.072881+00:00 · **Legacy report time:** 2026-11-21T07:11:26.751446+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.828 | 102.03 | +0.57% | 8.57x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | ETH/USD | 1642.19 | 74.57 | -0.14% | 2.17x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | TRX/USD ⭐ | 0.302672 | 74.15 | +0.34% | 2.79x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | DRV/USD | 0.26661 | 72.87 | +0.74% | 0.56x | MODERATE 61/100 | VERY_HIGH 76/100 | Watch |
| 5 | RARE/USD ⭐ | 0.01398 | 65.11 | +1.01% | 1.31x | STRONG 78/100 | VERY_HIGH 72/100 | Watch |
| 6 | SKY/USD | 0.04474 | 56.07 | -0.38% | 7.92x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 7 | CAP/USD | 0.094481 | 55.01 | +1.25% | 0.76x | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |
| 8 | CT/USD ⭐ | 0.1233 | 41.21 | +1.15% | 1.32x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 9 | RAY/USD | 1.287 | 39.06 | +0.00% | 4.74x | MODERATE 55/100 | VERY_HIGH 72/100 | Watch |
| 10 | BLUR/USD ⭐ | 0.00736 | 35.39 | +1.52% | 1.37x | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |
| 11 | ZAMA/USD | 0.05783 | 33.13 | +0.35% | 0.70x | WEAK 42/100 | EXTREME 88/100 | Do nothing |
| 12 | STBL/USD | 0.015966 | 32.12 | +0.36% | 1.38x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.799 | 98.66 | +0.57% | 8.57x | 14335 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | RARE/USD ⭐ | 0.01404 | 75.43 | +1.01% | 1.31x | 7248 | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 3 | TRX/USD ⭐ | 0.302651 | 62.48 | +0.34% | 2.79x | 6870 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | CT/USD ⭐ | 0.1233 | 47.58 | +1.15% | 1.32x | 2400 | MODERATE 69/100 | VERY_HIGH 72/100 | Watch |
| 5 | BLUR/USD ⭐ | 0.00736 | 34.81 | +1.52% | 1.37x | 2128 | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, TRX/USD, RARE/USD, CT/USD, BLUR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
