# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T03:51:59.485315+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45322151974
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5bd6f836dfdbcbd25cd6b1e411ed6ed279102502 (atomic ledger/results publication)
**Ledger generation:** 1521 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01235 | 79.790 | 76.403 | +7.20% | +1.81% | 0.44x | 16.2 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | BABY/USD | 0.00874 | 55.782 | 45.089 | +2.82% | +0.34% | 1.90x | 11.5 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94473 | 55.194 | 58.662 | +0.57% | +0.17% | 0.57x | 0.6 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.445e-06 | 53.497 | 50.965 | +0.67% | -0.03% | 1.27x | 5.8 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | WEAK 37/100 | HIGH 61/100 | Watch | WATCH |
| 5 | AI/USD | 0.01593 | 49.448 | 60.170 | +4.60% | -0.75% | 0.30x | 6.3 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | WEAK 30/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | BAT/USD | 0.0785 | 43.261 | 32.445 | +1.72% | +0.06% | 2.05x | 23.0 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | INX/USD | 0.003959 | 29.619 | 30.979 | +1.56% | -1.03% | 1.38x | 22.8 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | WEAK 25/100 | EXTREME 89/100 | Do nothing | WATCH |
| 8 | XDC/USD | 0.0261 | 24.245 | 34.744 | +0.46% | -0.46% | 0.18x | 7.7 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | XTZ/USD | 0.21428 | 23.376 | 28.544 | +0.67% | -0.07% | 0.52x | 14.0 | 2026-11-24T03:51:54.573841+00:00 | Not calibrated | WEAK 12/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.403 | 0.01235 | +1.81% | 0.44x |
| 2 | AI/USD | 60.170 | 0.01593 | -0.75% | 0.30x |
| 3 | XRP/USD | 58.662 | 0.94473 | +0.17% | 0.57x |
| 4 | PEPE/USD | 50.965 | 3.445e-06 | -0.03% | 1.27x |
| 5 | BABY/USD | 45.089 | 0.00874 | +0.34% | 1.90x |
| 6 | XDC/USD | 34.744 | 0.0261 | -0.46% | 0.18x |
| 7 | BAT/USD | 32.445 | 0.0785 | +0.06% | 2.05x |
| 8 | INX/USD | 30.979 | 0.003959 | -1.03% | 1.38x |
| 9 | XTZ/USD | 28.544 | 0.21428 | -0.07% | 0.52x |

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

- Persisted scans: 1521; predictions: 12985; observations: 921387.
- Matured sampled outcomes across 1/6/24/48h: 24160; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45322151974 · **Generation:** 1521 · **Legacy run:** 45322151974
**Main quote time:** 2026-11-24T03:51:59.485315+00:00 · **Legacy report time:** 2026-11-24T03:53:09.737995+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01235 | 79.79 | +1.81% | 0.44x | MODERATE 65/100 | VERY_HIGH 76/100 | Watch |
| 2 | BABY/USD ⭐ | 0.00874 | 55.78 | +0.34% | 1.90x | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 3 | XRP/USD | 0.94473 | 55.19 | +0.17% | 0.57x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 4 | PEPE/USD | 3.445e-06 | 53.50 | -0.03% | 1.27x | WEAK 37/100 | HIGH 61/100 | Watch |
| 5 | AI/USD | 0.01593 | 49.45 | -0.75% | 0.30x | WEAK 30/100 | EXTREME 88/100 | Do nothing |
| 6 | BAT/USD ⭐ | 0.0785 | 43.26 | +0.06% | 2.05x | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 7 | INX/USD | 0.003959 | 29.62 | -1.03% | 1.38x | WEAK 25/100 | EXTREME 89/100 | Do nothing |
| 8 | XDC/USD | 0.0261 | 24.24 | -0.46% | 0.18x | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | XTZ/USD | 0.21428 | 23.38 | -0.07% | 0.52x | WEAK 12/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00874 | 59.62 | +0.34% | 1.90x | 2456 | STRONG 80/100 | VERY_HIGH 73/100 | Watch |
| 2 | BAT/USD ⭐ | 0.07848 | 47.88 | +0.06% | 2.05x | 3034 | STRONG 74/100 | HIGH 66/100 | Watch |
| 3 | XMR/USD | 486.94 | 45.45 | +0.57% | 2.06x | 11887 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** BABY/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
