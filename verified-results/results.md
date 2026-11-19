# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:10:25.807453+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44442239895
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 0ac1d4ea441e72d12fb7309e54fc42d2e93a3fdc (atomic ledger/results publication)
**Ledger generation:** 727 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 10s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CFG/USD | 0.0706 | 74.730 | 68.694 | +9.63% | +1.29% | 0.96x | 14.2 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.592e-05 | 70.434 | 52.879 | +5.47% | +0.92% | 2.29x | 35.1 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021725 | 64.250 | 66.331 | +5.44% | +0.38% | 0.60x | 6.4 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | PROS/USD | 0.6916 | 60.471 | 38.670 | +3.25% | +3.47% | 1.44x | 31.9 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | TRX/USD | 0.310109 | 56.257 | 41.505 | +0.27% | -0.05% | 9.12x | 0.7 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 6 | MEGA/USD | 0.05783 | 49.087 | 46.320 | +3.27% | +1.01% | 0.77x | 15.6 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 7 | STX/USD | 0.273 | 41.749 | 30.668 | +0.70% | -0.18% | 2.20x | 11.0 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.05337 | 27.500 | 33.260 | +1.16% | -0.47% | 0.66x | 13.1 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | WEAK 14/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | DRV/USD | 0.26626 | 25.336 | 32.924 | +0.59% | +0.01% | 0.24x | 9.0 | 2026-11-19T02:10:15.903882+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CFG/USD | 68.694 | 0.0706 | +1.29% | 0.96x |
| 2 | SENT/USD | 66.331 | 0.021725 | +0.38% | 0.60x |
| 3 | LUNA/USD | 52.879 | 4.592e-05 | +0.92% | 2.29x |
| 4 | MEGA/USD | 46.320 | 0.05783 | +1.01% | 0.77x |
| 5 | TRX/USD | 41.505 | 0.310109 | -0.05% | 9.12x |
| 6 | PROS/USD | 38.670 | 0.6916 | +3.47% | 1.44x |
| 7 | PYTH/USD | 33.260 | 0.05337 | -0.47% | 0.66x |
| 8 | DRV/USD | 32.924 | 0.26626 | +0.01% | 0.24x |
| 9 | STX/USD | 30.668 | 0.273 | -0.18% | 2.20x |

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

- Persisted scans: 727; predictions: 5901; observations: 439750.
- Matured sampled outcomes across 1/6/24/48h: 5826; gap abstentions: 13478. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44442239895 · **Generation:** 727 · **Legacy run:** 44442239895
**Main quote time:** 2026-11-19T02:10:25.807453+00:00 · **Legacy report time:** 2026-11-19T02:11:12.942595+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CFG/USD | 0.0706 | 74.73 | +1.29% | 0.96x | MODERATE 62/100 | VERY_HIGH 80/100 | Watch |
| 2 | LUNA/USD | 4.592e-05 | 70.43 | +0.92% | 2.29x | STRONG 75/100 | VERY_HIGH 72/100 | Watch |
| 3 | SENT/USD | 0.021725 | 64.25 | +0.38% | 0.60x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 4 | PROS/USD ⭐ | 0.6916 | 60.47 | +3.47% | 1.44x | STRONG 75/100 | VERY_HIGH 82/100 | Watch |
| 5 | TRX/USD | 0.310109 | 56.26 | -0.05% | 9.12x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 6 | MEGA/USD | 0.05783 | 49.09 | +1.01% | 0.77x | MODERATE 50/100 | VERY_HIGH 80/100 | Watch |
| 7 | STX/USD | 0.273 | 41.75 | -0.18% | 2.20x | MODERATE 46/100 | VERY_HIGH 79/100 | Watch |
| 8 | PYTH/USD | 0.05337 | 27.50 | -0.47% | 0.66x | WEAK 14/100 | EXTREME 87/100 | Do nothing |
| 9 | DRV/USD | 0.26626 | 25.34 | +0.01% | 0.24x | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD ⭐ | 0.6861 | 62.07 | +3.47% | 1.44x | 2659 | STRONG 76/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** PROS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
