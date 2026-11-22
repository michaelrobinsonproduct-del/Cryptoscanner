# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T12:31:04.140181+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45022541358
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 59f7dac8a2a87fed9d5cc682568e1a366d6f10e6 (atomic ledger/results publication)
**Ledger generation:** 1283 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002469 | 86.827 | 76.246 | +5.33% | -0.88% | 6.40x | 8.1 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9813 | 84.817 | 74.014 | +3.29% | -0.84% | 4.49x | 8.1 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TAO/USD | 190.4437 | 78.093 | 64.746 | +2.54% | -0.33% | 2.74x | 10.2 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ETH/USD | 1703.82 | 75.533 | 63.728 | +1.28% | -0.64% | 5.95x | 0.5 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6568 | 74.142 | 63.751 | +1.47% | -0.92% | 2.95x | 3.0 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HYPE/USD | 62.17 | 72.461 | 64.826 | +1.52% | -1.30% | 2.42x | 1.6 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 66/100 | HIGH 65/100 | Do nothing | WATCH |
| 7 | XBT/USD | 60646.4 | 70.504 | 60.271 | +0.93% | -0.95% | 6.06x | 2.4 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 8 | INJ/USD | 6.197 | 67.232 | 63.834 | +3.75% | -1.17% | 1.92x | 9.7 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 54/100 | HIGH 65/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04652 | 60.001 | 72.032 | +5.06% | -1.27% | 0.43x | 17.2 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | WEAK 30/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | BNB/USD | 552.7 | 57.515 | 44.266 | +0.97% | -0.35% | 4.27x | 2.9 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 11 | AAVE/USD | 98.48 | 56.589 | 44.851 | +1.18% | -0.50% | 2.42x | 5.1 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 12 | DRV/USD | 0.36861 | 55.605 | 77.114 | +9.97% | -6.61% | 1.35x | 19.6 | 2026-11-22T12:30:56.495318+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 71/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 77.114 | 0.36861 | -6.61% | 1.35x |
| 2 | PUMP/USD | 76.246 | 0.002469 | -0.88% | 6.40x |
| 3 | NEAR/USD | 74.014 | 2.9813 | -0.84% | 4.49x |
| 4 | NIGHT/USD | 72.032 | 0.04652 | -1.27% | 0.43x |
| 5 | HYPE/USD | 64.826 | 62.17 | -1.30% | 2.42x |
| 6 | TAO/USD | 64.746 | 190.4437 | -0.33% | 2.74x |
| 7 | INJ/USD | 63.834 | 6.197 | -1.17% | 1.92x |
| 8 | SUI/USD | 63.751 | 0.6568 | -0.92% | 2.95x |
| 9 | ETH/USD | 63.728 | 1703.82 | -0.64% | 5.95x |
| 10 | XBT/USD | 60.271 | 60646.4 | -0.95% | 6.06x |
| 11 | AAVE/USD | 44.851 | 98.48 | -0.50% | 2.42x |
| 12 | BNB/USD | 44.266 | 552.7 | -0.35% | 4.27x |

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

- Persisted scans: 1283; predictions: 10316; observations: 776456.
- Matured sampled outcomes across 1/6/24/48h: 14902; gap abstentions: 22243. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45022541358 · **Generation:** 1283 · **Legacy run:** 45022541358
**Main quote time:** 2026-11-22T12:31:04.140181+00:00 · **Legacy report time:** 2026-11-22T12:31:55.645885+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002469 | 86.83 | -0.88% | 6.40x | STRONG 73/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 2.9813 | 84.82 | -0.84% | 4.49x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | TAO/USD | 190.4437 | 78.09 | -0.33% | 2.74x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 4 | ETH/USD | 1703.82 | 75.53 | -0.64% | 5.95x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | SUI/USD | 0.6568 | 74.14 | -0.92% | 2.95x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 6 | HYPE/USD | 62.17 | 72.46 | -1.30% | 2.42x | MODERATE 66/100 | HIGH 65/100 | Do nothing |
| 7 | XBT/USD | 60646.4 | 70.50 | -0.95% | 6.06x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 8 | INJ/USD | 6.197 | 67.23 | -1.17% | 1.92x | MODERATE 54/100 | HIGH 65/100 | Watch |
| 9 | NIGHT/USD | 0.04652 | 60.00 | -1.27% | 0.43x | WEAK 30/100 | EXTREME 86/100 | Do nothing |
| 10 | BNB/USD | 552.7 | 57.52 | -0.35% | 4.27x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 11 | AAVE/USD | 98.48 | 56.59 | -0.50% | 2.42x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 12 | DRV/USD | 0.36861 | 55.61 | -6.61% | 1.35x | WEAK 43/100 | VERY_HIGH 71/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001978 | 75.00 | +0.90% | 1.06x | 4342 | MODERATE 58/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
