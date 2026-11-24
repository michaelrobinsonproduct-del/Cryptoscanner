# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T11:11:49.249794+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45381581090
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3628fc24f62977a1169ab0158fea8fe939ccf177 (atomic ledger/results publication)
**Ledger generation:** 1566 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.416 | 95.575 | 76.217 | +3.96% | +0.87% | 7.16x | 13.0 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01257 | 74.741 | 78.474 | +9.11% | +0.32% | 0.47x | 15.9 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | GBP/USD | 1.30703 | 72.095 | 56.954 | +0.29% | +0.03% | 3.21x | 0.2 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XMR/USD | 498.2 | 64.931 | 68.718 | +2.51% | +0.59% | 0.33x | 7.6 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.477e-06 | 64.180 | 56.737 | +1.61% | +0.99% | 1.25x | 11.5 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 6 | BAT/USD | 0.07796 | 53.724 | 37.055 | +1.02% | +0.33% | 3.08x | 5.1 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 7 | ARB/USD | 0.1134 | 52.343 | 33.130 | +0.71% | +0.89% | 2.48x | 17.7 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 8 | 2Z/USD | 0.01608 | 51.463 | 46.821 | +2.75% | -0.25% | 1.59x | 6.2 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | BABY/USD | 0.0087 | 49.481 | 43.391 | +2.35% | +0.70% | 1.26x | 11.5 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 10 | XDC/USD | 0.02624 | 39.303 | 34.538 | +1.00% | -0.04% | 1.50x | 15.3 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | LUNA/USD | 4.564e-05 | 32.337 | 45.039 | +4.99% | -1.18% | 0.32x | 43.7 | 2026-11-24T11:11:44.425917+00:00 | Not calibrated | WEAK 6/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.474 | 0.01257 | +0.32% | 0.47x |
| 2 | VVV/USD | 76.217 | 25.416 | +0.87% | 7.16x |
| 3 | XMR/USD | 68.718 | 498.2 | +0.59% | 0.33x |
| 4 | GBP/USD | 56.954 | 1.30703 | +0.03% | 3.21x |
| 5 | PEPE/USD | 56.737 | 3.477e-06 | +0.99% | 1.25x |
| 6 | 2Z/USD | 46.821 | 0.01608 | -0.25% | 1.59x |
| 7 | LUNA/USD | 45.039 | 4.564e-05 | -1.18% | 0.32x |
| 8 | BABY/USD | 43.391 | 0.0087 | +0.70% | 1.26x |
| 9 | BAT/USD | 37.055 | 0.07796 | +0.33% | 3.08x |
| 10 | XDC/USD | 34.538 | 0.02624 | -0.04% | 1.50x |
| 11 | ARB/USD | 33.130 | 0.1134 | +0.89% | 2.48x |

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

- Persisted scans: 1566; predictions: 13498; observations: 948792.
- Matured sampled outcomes across 1/6/24/48h: 25944; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45381581090 · **Generation:** 1566 · **Legacy run:** 45381581090
**Main quote time:** 2026-11-24T11:11:49.249794+00:00 · **Legacy report time:** 2026-11-24T11:12:57.127009+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.416 | 95.58 | +0.87% | 7.16x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | MON/USD | 0.01257 | 74.74 | +0.32% | 0.47x | MODERATE 62/100 | VERY_HIGH 76/100 | Watch |
| 3 | GBP/USD | 1.30703 | 72.10 | +0.03% | 3.21x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | XMR/USD | 498.2 | 64.93 | +0.59% | 0.33x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 5 | PEPE/USD ⭐ | 3.477e-06 | 64.18 | +0.99% | 1.25x | STRONG 72/100 | HIGH 61/100 | Watch |
| 6 | BAT/USD ⭐ | 0.07796 | 53.72 | +0.33% | 3.08x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 7 | ARB/USD ⭐ | 0.1134 | 52.34 | +0.89% | 2.48x | STRONG 86/100 | HIGH 61/100 | Consider small entry |
| 8 | 2Z/USD | 0.01608 | 51.46 | -0.25% | 1.59x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 9 | BABY/USD ⭐ | 0.0087 | 49.48 | +0.70% | 1.26x | MODERATE 65/100 | HIGH 66/100 | Watch |
| 10 | XDC/USD | 0.02624 | 39.30 | -0.04% | 1.50x | WEAK 35/100 | VERY_HIGH 72/100 | Watch |
| 11 | LUNA/USD | 4.564e-05 | 32.34 | -1.18% | 0.32x | WEAK 6/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.318 | 90.32 | +0.87% | 7.16x | 13741 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEPE/USD ⭐ | 3.473e-06 | 56.58 | +0.99% | 1.25x | 9350 | STRONG 73/100 | HIGH 55/100 | Watch |
| 3 | BABY/USD ⭐ | 0.00869 | 53.56 | +0.70% | 1.26x | 5153 | MODERATE 67/100 | HIGH 66/100 | Watch |
| 4 | BAT/USD ⭐ | 0.07797 | 44.91 | +0.33% | 3.08x | 3811 | STRONG 82/100 | HIGH 66/100 | Consider small entry |
| 5 | ARB/USD ⭐ | 0.1134 | 43.28 | +0.89% | 2.48x | 2639 | STRONG 87/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, PEPE/USD, BAT/USD, ARB/USD, BABY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
