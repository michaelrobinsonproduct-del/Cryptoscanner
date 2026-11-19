# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:40:20.636406+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44557285399
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 27a4d3f93157d24031ad26caab94683add785fef (atomic ledger/results publication)
**Ledger generation:** 804 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.527 | 75.219 | 77.326 | +3.95% | -1.59% | 1.58x | 10.6 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | ZEC/USD | 919.44 | 67.631 | 60.043 | +0.82% | -1.48% | 3.91x | 1.4 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | MODERATE 64/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | HYPE/USD | 67.89 | 63.941 | 64.099 | +1.51% | -1.12% | 1.54x | 2.9 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | MODERATE 52/100 | HIGH 65/100 | Watch | WATCH |
| 4 | PYTH/USD | 0.05606 | 61.981 | 66.097 | +6.25% | -0.28% | 0.73x | 19.6 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | SKR/USD | 0.01032 | 60.079 | 69.210 | +7.13% | -1.18% | 0.68x | 13.6 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 30/100 | EXTREME 98/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5463 | 59.289 | 62.400 | +5.46% | -0.82% | 1.10x | 14.6 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 35/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | BILL/USD | 0.00428 | 59.043 | 64.052 | +8.35% | -2.06% | 1.53x | 23.4 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 40/100 | EXTREME 89/100 | Do nothing | WATCH |
| 8 | INJ/USD | 7.07 | 54.623 | 49.871 | +1.27% | -2.05% | 3.39x | 5.7 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | MODERATE 57/100 | HIGH 65/100 | Do nothing | WATCH |
| 9 | PEPE/USD | 3.78e-06 | 53.127 | 45.826 | +0.91% | -1.54% | 4.01x | 2.6 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | MODERATE 57/100 | HIGH 65/100 | Do nothing | WATCH |
| 10 | USELESS/USD | 0.1013 | 49.754 | 68.668 | +6.01% | -3.12% | 0.67x | 21.7 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 20/100 | EXTREME 92/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.96915 | 49.226 | 54.693 | +0.29% | -1.35% | 1.13x | 4.6 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 12 | SOL/USD | 73.78 | 47.403 | 56.607 | +0.33% | -1.19% | 0.68x | 1.4 | 2026-11-19T15:40:12.717048+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.326 | 22.527 | -1.59% | 1.58x |
| 2 | SKR/USD | 69.210 | 0.01032 | -1.18% | 0.68x |
| 3 | USELESS/USD | 68.668 | 0.1013 | -3.12% | 0.67x |
| 4 | PYTH/USD | 66.097 | 0.05606 | -0.28% | 0.73x |
| 5 | HYPE/USD | 64.099 | 67.89 | -1.12% | 1.54x |
| 6 | BILL/USD | 64.052 | 0.00428 | -2.06% | 1.53x |
| 7 | AKT/USD | 62.400 | 0.5463 | -0.82% | 1.10x |
| 8 | ZEC/USD | 60.043 | 919.44 | -1.48% | 3.91x |
| 9 | SOL/USD | 56.607 | 73.78 | -1.19% | 0.68x |
| 10 | XRP/USD | 54.693 | 0.96915 | -1.35% | 1.13x |
| 11 | INJ/USD | 49.871 | 7.07 | -2.05% | 3.39x |
| 12 | PEPE/USD | 45.826 | 3.78e-06 | -1.54% | 4.01x |

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

- Persisted scans: 804; predictions: 6792; observations: 486219.
- Matured sampled outcomes across 1/6/24/48h: 6791; gap abstentions: 15235. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44557285399 · **Generation:** 804 · **Legacy run:** 44557285399
**Main quote time:** 2026-11-19T15:40:20.636406+00:00 · **Legacy report time:** 2026-11-19T15:41:01.432778+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.527 | 75.22 | -1.59% | 1.58x | MODERATE 53/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | ZEC/USD | 919.44 | 67.63 | -1.48% | 3.91x | MODERATE 64/100 | HIGH 65/100 | Do nothing |
| 3 | HYPE/USD | 67.89 | 63.94 | -1.12% | 1.54x | MODERATE 52/100 | HIGH 65/100 | Watch |
| 4 | PYTH/USD | 0.05606 | 61.98 | -0.28% | 0.73x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 5 | SKR/USD | 0.01032 | 60.08 | -1.18% | 0.68x | WEAK 30/100 | EXTREME 98/100 | Do nothing |
| 6 | AKT/USD | 0.5463 | 59.29 | -0.82% | 1.10x | WEAK 35/100 | EXTREME 86/100 | Do nothing |
| 7 | BILL/USD | 0.00428 | 59.04 | -2.06% | 1.53x | WEAK 40/100 | EXTREME 89/100 | Do nothing |
| 8 | INJ/USD | 7.07 | 54.62 | -2.05% | 3.39x | MODERATE 57/100 | HIGH 65/100 | Do nothing |
| 9 | PEPE/USD | 3.78e-06 | 53.13 | -1.54% | 4.01x | MODERATE 57/100 | HIGH 65/100 | Do nothing |
| 10 | USELESS/USD | 0.1013 | 49.75 | -3.12% | 0.67x | WEAK 20/100 | EXTREME 92/100 | Do nothing |
| 11 | XRP/USD | 0.96915 | 49.23 | -1.35% | 1.13x | WEAK 35/100 | VERY_HIGH 72/100 | Do nothing |
| 12 | SOL/USD | 73.78 | 47.40 | -1.19% | 0.68x | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.058 | 63.15 | +0.66% | 1.10x | 2019 | MODERATE 57/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
