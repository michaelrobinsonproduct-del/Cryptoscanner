# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:50:26.425168+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44559159832
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 97dff866633ee387d622fb5ab0eee2e6840f3086 (atomic ledger/results publication)
**Ledger generation:** 806 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.369 | 81.665 | 75.310 | +3.22% | -1.18% | 2.23x | 4.5 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | STRONG 71/100 | HIGH 65/100 | Watch | WATCH |
| 2 | PYTH/USD | 0.05582 | 73.561 | 66.494 | +5.80% | -1.10% | 2.26x | 12.5 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | TRUST/USD | 0.05396 | 73.328 | 65.902 | +9.67% | -1.51% | 3.46x | 20.5 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | ZEC/USD | 918.97 | 69.493 | 57.774 | +0.77% | -0.66% | 3.89x | 5.2 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | BILL/USD | 0.00426 | 66.449 | 64.020 | +7.85% | -1.16% | 1.82x | 23.5 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | WEAK 43/100 | EXTREME 89/100 | Do nothing | WATCH |
| 6 | SYRUP/USD | 0.10216 | 65.581 | 68.615 | +7.58% | -1.39% | 1.39x | 15.6 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 7 | TAO/USD | 192.6359 | 65.304 | 54.246 | +0.35% | -0.79% | 2.64x | 6.4 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.151716 | 63.435 | 54.928 | +0.31% | -0.78% | 2.24x | 4.4 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5484 | 62.500 | 66.165 | +5.87% | +0.04% | 0.62x | 12.8 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | SKR/USD | 0.010388 | 60.671 | 62.503 | +7.84% | +0.47% | 0.58x | 27.0 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | HYPE/USD | 67.5 | 55.133 | 60.748 | +0.93% | -0.93% | 0.90x | 1.5 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | USELESS/USD | 0.10061 | 54.102 | 66.000 | +5.28% | -2.09% | 0.85x | 16.9 | 2026-11-19T15:50:17.505512+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 78/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 75.310 | 22.369 | -1.18% | 2.23x |
| 2 | SYRUP/USD | 68.615 | 0.10216 | -1.39% | 1.39x |
| 3 | PYTH/USD | 66.494 | 0.05582 | -1.10% | 2.26x |
| 4 | AKT/USD | 66.165 | 0.5484 | +0.04% | 0.62x |
| 5 | USELESS/USD | 66.000 | 0.10061 | -2.09% | 0.85x |
| 6 | TRUST/USD | 65.902 | 0.05396 | -1.51% | 3.46x |
| 7 | BILL/USD | 64.020 | 0.00426 | -1.16% | 1.82x |
| 8 | SKR/USD | 62.503 | 0.010388 | +0.47% | 0.58x |
| 9 | HYPE/USD | 60.748 | 67.5 | -0.93% | 0.90x |
| 10 | ZEC/USD | 57.774 | 918.97 | -0.66% | 3.89x |
| 11 | ADA/USD | 54.928 | 0.151716 | -0.78% | 2.24x |
| 12 | TAO/USD | 54.246 | 192.6359 | -0.79% | 2.64x |

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

- Persisted scans: 806; predictions: 6816; observations: 487411.
- Matured sampled outcomes across 1/6/24/48h: 6803; gap abstentions: 15258. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44559159832 · **Generation:** 806 · **Legacy run:** 44559159832
**Main quote time:** 2026-11-19T15:50:26.425168+00:00 · **Legacy report time:** 2026-11-19T15:51:11.647112+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.369 | 81.66 | -1.18% | 2.23x | STRONG 71/100 | HIGH 65/100 | Watch |
| 2 | PYTH/USD | 0.05582 | 73.56 | -1.10% | 2.26x | MODERATE 62/100 | VERY_HIGH 76/100 | Watch |
| 3 | TRUST/USD | 0.05396 | 73.33 | -1.51% | 3.46x | MODERATE 57/100 | EXTREME 89/100 | Do nothing |
| 4 | ZEC/USD | 918.97 | 69.49 | -0.66% | 3.89x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | BILL/USD | 0.00426 | 66.45 | -1.16% | 1.82x | WEAK 43/100 | EXTREME 89/100 | Do nothing |
| 6 | SYRUP/USD | 0.10216 | 65.58 | -1.39% | 1.39x | MODERATE 48/100 | VERY_HIGH 83/100 | Do nothing |
| 7 | TAO/USD | 192.6359 | 65.30 | -0.79% | 2.64x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.151716 | 63.44 | -0.78% | 2.24x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 9 | AKT/USD | 0.5484 | 62.50 | +0.04% | 0.62x | MODERATE 46/100 | EXTREME 88/100 | Do nothing |
| 10 | SKR/USD | 0.010388 | 60.67 | +0.47% | 0.58x | MODERATE 50/100 | EXTREME 94/100 | Do nothing |
| 11 | HYPE/USD | 67.5 | 55.13 | -0.93% | 0.90x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | USELESS/USD | 0.10061 | 54.10 | -2.09% | 0.85x | WEAK 27/100 | VERY_HIGH 78/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021224 | 65.72 | +0.14% | 2.18x | 14415 | STRONG 78/100 | HIGH 60/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
