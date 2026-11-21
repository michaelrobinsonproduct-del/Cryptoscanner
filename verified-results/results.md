# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T09:40:46.337119+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44890615694
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** a76e429ada8ad30142fa23b2a59b0863248ca05c (atomic ledger/results publication)
**Ledger generation:** 1116 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.684 | 78.448 | 83.671 | +4.56% | -0.11% | 0.53x | 6.5 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | RARE/USD | 0.01403 | 77.279 | 56.154 | +5.49% | +4.07% | 1.08x | 28.5 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | MODERATE 64/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | ZAMA/USD | 0.05842 | 57.082 | 39.321 | +2.47% | +0.55% | 19.07x | 18.8 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ETH/USD | 1633.31 | 55.987 | 61.017 | +0.86% | -0.03% | 0.51x | 0.1 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.093586 | 55.738 | 42.292 | +2.23% | -0.31% | 2.98x | 14.0 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | TRX/USD | 0.302598 | 48.840 | 57.523 | +0.36% | -0.05% | 0.16x | 0.0 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | MORPHO/USD | 1.5474 | 39.061 | 35.584 | +1.04% | +0.46% | 1.12x | 12.5 | 2026-11-21T09:40:41.176766+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 83.671 | 21.684 | -0.11% | 0.53x |
| 2 | ETH/USD | 61.017 | 1633.31 | -0.03% | 0.51x |
| 3 | TRX/USD | 57.523 | 0.302598 | -0.05% | 0.16x |
| 4 | RARE/USD | 56.154 | 0.01403 | +4.07% | 1.08x |
| 5 | CAP/USD | 42.292 | 0.093586 | -0.31% | 2.98x |
| 6 | ZAMA/USD | 39.321 | 0.05842 | +0.55% | 19.07x |
| 7 | MORPHO/USD | 35.584 | 1.5474 | +0.46% | 1.12x |

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

- Persisted scans: 1116; predictions: 8760; observations: 674887.
- Matured sampled outcomes across 1/6/24/48h: 11538; gap abstentions: 20300. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44890615694 · **Generation:** 1116 · **Legacy run:** 44890615694
**Main quote time:** 2026-11-21T09:40:46.337119+00:00 · **Legacy report time:** 2026-11-21T09:41:47.270257+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.684 | 78.45 | -0.11% | 0.53x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 2 | RARE/USD ⭐ | 0.01403 | 77.28 | +4.07% | 1.08x | STRONG 74/100 | EXTREME 89/100 | Do nothing |
| 3 | ZAMA/USD ⭐ | 0.05842 | 57.08 | +0.55% | 19.07x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 4 | ETH/USD | 1633.31 | 55.99 | -0.03% | 0.51x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | CAP/USD | 0.093586 | 55.74 | -0.31% | 2.98x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 6 | TRX/USD | 0.302598 | 48.84 | -0.05% | 0.16x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | MORPHO/USD ⭐ | 1.5474 | 39.06 | +0.46% | 1.12x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD ⭐ | 0.01401 | 80.21 | +4.07% | 1.08x | 7526 | STRONG 85/100 | VERY_HIGH 77/100 | Watch |
| 2 | ZAMA/USD ⭐ | 0.05859 | 77.36 | +0.55% | 19.07x | 2822 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | MORPHO/USD ⭐ | 1.5474 | 39.06 | +0.46% | 1.12x | 2743 | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** RARE/USD, ZAMA/USD, MORPHO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
