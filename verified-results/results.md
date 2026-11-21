# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T10:50:42.178777+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44896160499
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 8bee36f39fa93dd47ce264667f6be1803b006201 (atomic ledger/results publication)
**Ledger generation:** 1123 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.073 | 95.342 | 95.691 | +6.43% | +1.19% | 0.37x | 8.6 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XMR/USD | 469.33 | 86.322 | 69.673 | +2.86% | +0.68% | 2.33x | 10.7 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | STRONG 93/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | SKY/USD | 0.04481 | 65.234 | 45.500 | +2.21% | +0.95% | 4.77x | 8.9 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ETH/USD | 1640.92 | 62.544 | 64.307 | +1.33% | +0.24% | 0.71x | 0.1 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SENT/USD | 0.021076 | 59.010 | 43.795 | +2.34% | +0.04% | 5.02x | 7.1 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.07712 | 55.970 | 58.477 | +3.52% | +0.95% | 0.28x | 11.7 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | TRX/USD | 0.302769 | 54.037 | 57.706 | +0.42% | +0.03% | 0.62x | 0.5 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ZAMA/USD | 0.0582 | 31.528 | 40.082 | +2.09% | -0.05% | 0.17x | 12.0 | 2026-11-21T10:50:36.794406+00:00 | Not calibrated | WEAK 16/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.691 | 22.073 | +1.19% | 0.37x |
| 2 | XMR/USD | 69.673 | 469.33 | +0.68% | 2.33x |
| 3 | ETH/USD | 64.307 | 1640.92 | +0.24% | 0.71x |
| 4 | USELESS/USD | 58.477 | 0.07712 | +0.95% | 0.28x |
| 5 | TRX/USD | 57.706 | 0.302769 | +0.03% | 0.62x |
| 6 | SKY/USD | 45.500 | 0.04481 | +0.95% | 4.77x |
| 7 | SENT/USD | 43.795 | 0.021076 | +0.04% | 5.02x |
| 8 | ZAMA/USD | 40.082 | 0.0582 | -0.05% | 0.17x |

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

- Persisted scans: 1123; predictions: 8811; observations: 679143.
- Matured sampled outcomes across 1/6/24/48h: 11595; gap abstentions: 20329. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44896160499 · **Generation:** 1123 · **Legacy run:** 44896160499
**Main quote time:** 2026-11-21T10:50:42.178777+00:00 · **Legacy report time:** 2026-11-21T10:51:27.179581+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.073 | 95.34 | +1.19% | 0.37x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | XMR/USD ⭐ | 469.33 | 86.32 | +0.68% | 2.33x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.04481 | 65.23 | +0.95% | 4.77x | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 4 | ETH/USD | 1640.92 | 62.54 | +0.24% | 0.71x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 5 | SENT/USD | 0.021076 | 59.01 | +0.04% | 5.02x | STRONG 75/100 | HIGH 67/100 | Watch |
| 6 | USELESS/USD | 0.07712 | 55.97 | +0.95% | 0.28x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 7 | TRX/USD | 0.302769 | 54.04 | +0.03% | 0.62x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 8 | ZAMA/USD | 0.0582 | 31.53 | -0.05% | 0.17x | WEAK 16/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 469.16 | 78.18 | +0.68% | 2.33x | 11754 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04488 | 64.00 | +0.95% | 4.77x | 4495 | STRONG 87/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** XMR/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
