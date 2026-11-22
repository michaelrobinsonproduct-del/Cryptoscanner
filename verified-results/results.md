# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:01:21.549524+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45041301783
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 6fe3454c2b0efe7e94fb3320f7003b4c2d50f382 (atomic ledger/results publication)
**Ledger generation:** 1304 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04821 | 85.011 | 86.087 | +8.88% | +0.12% | 0.83x | 12.4 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | DRV/USD | 0.36525 | 82.953 | 88.725 | +8.96% | +0.10% | 0.37x | 0.3 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002542 | 81.591 | 80.114 | +8.45% | +0.79% | 0.75x | 11.8 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 66/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ETH/USD | 1716.61 | 73.523 | 69.256 | +2.04% | +0.13% | 1.36x | 0.1 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9929 | 73.208 | 78.515 | +3.69% | -0.18% | 0.56x | 4.7 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | HYPE/USD | 62.73 | 68.204 | 70.438 | +2.43% | -0.16% | 0.86x | 3.2 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XBT/USD | 60827.6 | 65.457 | 63.585 | +1.23% | +0.22% | 1.08x | 0.0 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 8.80126 | 60.205 | 60.688 | +2.40% | +0.11% | 0.90x | 2.6 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ZEC/USD | 793.68 | 59.904 | 65.674 | +1.99% | -0.14% | 0.49x | 6.6 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6566 | 56.884 | 64.296 | +1.44% | +0.09% | 0.21x | 1.5 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.144683 | 53.422 | 42.422 | +0.38% | +0.08% | 2.06x | 4.6 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BNB/USD | 555.99 | 52.261 | 47.209 | +1.57% | +0.06% | 1.48x | 1.8 | 2026-11-22T16:01:14.227337+00:00 | Not calibrated | MODERATE 61/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 88.725 | 0.36525 | +0.10% | 0.37x |
| 2 | NIGHT/USD | 86.087 | 0.04821 | +0.12% | 0.83x |
| 3 | PUMP/USD | 80.114 | 0.002542 | +0.79% | 0.75x |
| 4 | NEAR/USD | 78.515 | 2.9929 | -0.18% | 0.56x |
| 5 | HYPE/USD | 70.438 | 62.73 | -0.16% | 0.86x |
| 6 | ETH/USD | 69.256 | 1716.61 | +0.13% | 1.36x |
| 7 | ZEC/USD | 65.674 | 793.68 | -0.14% | 0.49x |
| 8 | SUI/USD | 64.296 | 0.6566 | +0.09% | 0.21x |
| 9 | XBT/USD | 63.585 | 60827.6 | +0.22% | 1.08x |
| 10 | LINK/USD | 60.688 | 8.80126 | +0.11% | 0.90x |
| 11 | BNB/USD | 47.209 | 555.99 | +0.06% | 1.48x |
| 12 | ADA/USD | 42.422 | 0.144683 | +0.08% | 2.06x |

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

- Persisted scans: 1304; predictions: 10567; observations: 789244.
- Matured sampled outcomes across 1/6/24/48h: 15552; gap abstentions: 22317. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45041301783 · **Generation:** 1304 · **Legacy run:** 45041301783
**Main quote time:** 2026-11-22T16:01:21.549524+00:00 · **Legacy report time:** 2026-11-22T16:02:21.068678+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04821 | 85.01 | +0.12% | 0.83x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | DRV/USD | 0.36525 | 82.95 | +0.10% | 0.37x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 3 | PUMP/USD | 0.002542 | 81.59 | +0.79% | 0.75x | MODERATE 66/100 | HIGH 68/100 | Watch |
| 4 | ETH/USD ⭐ | 1716.61 | 73.52 | +0.13% | 1.36x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD | 2.9929 | 73.21 | -0.18% | 0.56x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | HYPE/USD | 62.73 | 68.20 | -0.16% | 0.86x | WEAK 39/100 | HIGH 68/100 | Watch |
| 7 | XBT/USD | 60827.6 | 65.46 | +0.22% | 1.08x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD | 8.80126 | 60.21 | +0.11% | 0.90x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | ZEC/USD | 793.68 | 59.90 | -0.14% | 0.49x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.6566 | 56.88 | +0.09% | 0.21x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.144683 | 53.42 | +0.08% | 2.06x | STRONG 72/100 | HIGH 55/100 | Watch |
| 12 | BNB/USD | 555.99 | 52.26 | +0.06% | 1.48x | MODERATE 61/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD | 0.001922 | 79.43 | +0.36% | 2.55x | 4970 | STRONG 80/100 | VERY_HIGH 82/100 | Watch |
| 2 | ETH/USD ⭐ | 1716.83 | 77.09 | +0.13% | 1.36x | 39154 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
