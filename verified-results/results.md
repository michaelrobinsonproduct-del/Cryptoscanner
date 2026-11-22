# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T22:41:13.341083+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45078950038
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 17fbd9e4100e8ec9a0a4aaa82684a17b51741565 (atomic ledger/results publication)
**Ledger generation:** 1346 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002557 | 101.244 | 84.676 | +9.09% | +0.31% | 4.11x | 3.9 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.36705 | 93.346 | 85.211 | +9.50% | -1.37% | 4.93x | 7.4 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | STRONG 77/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | VVV/USD | 25.886 | 90.147 | 79.240 | +3.96% | -0.12% | 2.15x | 7.0 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9572 | 86.350 | 70.843 | +2.46% | +0.10% | 5.26x | 2.7 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04912 | 86.087 | 88.049 | +10.93% | -0.24% | 0.93x | 12.2 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | STBL/USD | 0.01712 | 79.069 | 67.564 | +6.97% | -0.41% | 2.35x | 17.0 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.08 | 78.394 | 63.796 | +1.37% | -0.08% | 4.47x | 1.6 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 8 | PIEVERSE/USD | 3.6853 | 73.171 | 63.195 | +8.29% | -1.00% | 6.10x | 45.0 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | ETH/USD | 1710.36 | 67.500 | 66.655 | +1.67% | -0.03% | 1.10x | 0.1 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XBT/USD | 60733.5 | 63.185 | 62.489 | +1.07% | -0.01% | 1.07x | 0.0 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6503 | 62.125 | 56.634 | +0.46% | -0.09% | 1.60x | 3.1 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 12 | ZEC/USD | 787.26 | 61.737 | 62.224 | +1.17% | +0.10% | 0.90x | 1.9 | 2026-11-22T22:41:06.637712+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.049 | 0.04912 | -0.24% | 0.93x |
| 2 | DRV/USD | 85.211 | 0.36705 | -1.37% | 4.93x |
| 3 | PUMP/USD | 84.676 | 0.002557 | +0.31% | 4.11x |
| 4 | VVV/USD | 79.240 | 25.886 | -0.12% | 2.15x |
| 5 | NEAR/USD | 70.843 | 2.9572 | +0.10% | 5.26x |
| 6 | STBL/USD | 67.564 | 0.01712 | -0.41% | 2.35x |
| 7 | ETH/USD | 66.655 | 1710.36 | -0.03% | 1.10x |
| 8 | HYPE/USD | 63.796 | 62.08 | -0.08% | 4.47x |
| 9 | PIEVERSE/USD | 63.195 | 3.6853 | -1.00% | 6.10x |
| 10 | XBT/USD | 62.489 | 60733.5 | -0.01% | 1.07x |
| 11 | ZEC/USD | 62.224 | 787.26 | +0.10% | 0.90x |
| 12 | SUI/USD | 56.634 | 0.6503 | -0.09% | 1.60x |

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

- Persisted scans: 1346; predictions: 11071; observations: 814821.
- Matured sampled outcomes across 1/6/24/48h: 17037; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45078950038 · **Generation:** 1346 · **Legacy run:** 45078950038
**Main quote time:** 2026-11-22T22:41:13.341083+00:00 · **Legacy report time:** 2026-11-22T22:42:06.882203+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002557 | 101.24 | +0.31% | 4.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD | 0.36705 | 93.35 | -1.37% | 4.93x | STRONG 77/100 | HIGH 65/100 | Do nothing |
| 3 | VVV/USD | 25.886 | 90.15 | -0.12% | 2.15x | STRONG 75/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD ⭐ | 2.9572 | 86.35 | +0.10% | 5.26x | STRONG 98/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.04912 | 86.09 | -0.24% | 0.93x | WEAK 43/100 | VERY_HIGH 74/100 | Watch |
| 6 | STBL/USD | 0.01712 | 79.07 | -0.41% | 2.35x | MODERATE 65/100 | VERY_HIGH 79/100 | Watch |
| 7 | HYPE/USD | 62.08 | 78.39 | -0.08% | 4.47x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 8 | PIEVERSE/USD | 3.6853 | 73.17 | -1.00% | 6.10x | MODERATE 52/100 | EXTREME 87/100 | Do nothing |
| 9 | ETH/USD | 1710.36 | 67.50 | -0.03% | 1.10x | WEAK 44/100 | HIGH 68/100 | Watch |
| 10 | XBT/USD | 60733.5 | 63.18 | -0.01% | 1.07x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | SUI/USD | 0.6503 | 62.13 | -0.09% | 1.60x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 12 | ZEC/USD | 787.26 | 61.74 | +0.10% | 0.90x | MODERATE 51/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002559 | 93.10 | +0.31% | 4.11x | 4306 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 2.9605 | 85.07 | +0.10% | 5.26x | 12918 | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | ZBCN/USD | 0.001843 | 82.29 | +0.93% | 2.64x | 6341 | STRONG 81/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** PUMP/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
