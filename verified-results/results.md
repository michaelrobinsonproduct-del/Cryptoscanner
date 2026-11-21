# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T11:21:02.234831+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44898558013
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 9b147e452d95ab89c4d5d87762ccea23bbee4630 (atomic ledger/results publication)
**Ledger generation:** 1126 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.839 | 84.427 | 88.922 | +5.30% | -0.12% | 0.61x | 6.4 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 467.76 | 69.923 | 68.532 | +2.51% | +0.36% | 0.96x | 8.1 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TRX/USD | 0.302894 | 65.191 | 57.435 | +0.46% | -0.02% | 1.79x | 1.6 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ETH/USD | 1638.61 | 62.332 | 63.308 | +1.19% | -0.02% | 0.91x | 0.1 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.07681 | 59.469 | 55.522 | +3.10% | +0.27% | 1.26x | 11.7 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04453 | 42.593 | 41.004 | +1.57% | +0.07% | 1.13x | 9.0 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |
| 7 | SENT/USD | 0.020884 | 31.477 | 36.761 | +1.40% | -0.29% | 0.62x | 8.1 | 2026-11-21T11:20:54.982815+00:00 | Not calibrated | WEAK 21/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 88.922 | 21.839 | -0.12% | 0.61x |
| 2 | XMR/USD | 68.532 | 467.76 | +0.36% | 0.96x |
| 3 | ETH/USD | 63.308 | 1638.61 | -0.02% | 0.91x |
| 4 | TRX/USD | 57.435 | 0.302894 | -0.02% | 1.79x |
| 5 | USELESS/USD | 55.522 | 0.07681 | +0.27% | 1.26x |
| 6 | SKY/USD | 41.004 | 0.04453 | +0.07% | 1.13x |
| 7 | SENT/USD | 36.761 | 0.020884 | -0.29% | 0.62x |

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

- Persisted scans: 1126; predictions: 8833; observations: 680967.
- Matured sampled outcomes across 1/6/24/48h: 11624; gap abstentions: 20335. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44898558013 · **Generation:** 1126 · **Legacy run:** 44898558013
**Main quote time:** 2026-11-21T11:21:02.234831+00:00 · **Legacy report time:** 2026-11-21T11:21:49.619255+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.839 | 84.43 | -0.12% | 0.61x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 467.76 | 69.92 | +0.36% | 0.96x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 3 | TRX/USD | 0.302894 | 65.19 | -0.02% | 1.79x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | ETH/USD | 1638.61 | 62.33 | -0.02% | 0.91x | WEAK 36/100 | HIGH 68/100 | Watch |
| 5 | USELESS/USD ⭐ | 0.07681 | 59.47 | +0.27% | 1.26x | STRONG 70/100 | HIGH 61/100 | Watch |
| 6 | SKY/USD ⭐ | 0.04453 | 42.59 | +0.07% | 1.13x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 7 | SENT/USD | 0.020884 | 31.48 | -0.29% | 0.62x | WEAK 21/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.07736 | 75.76 | +0.27% | 1.26x | 4941 | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04453 | 50.29 | +0.07% | 1.13x | 4509 | MODERATE 60/100 | HIGH 67/100 | Watch |
| 3 | AAVE/USD | 98.01 | 40.34 | +0.41% | 1.37x | 8177 | MODERATE 65/100 | HIGH 55/100 | Watch |

**Same-run overlap:** USELESS/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
