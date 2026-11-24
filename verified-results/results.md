# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:31:34.566782+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45340839080
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d652851c5683229a128a2ae6bb3bfa123748ca25 (atomic ledger/results publication)
**Ledger generation:** 1538 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.497 | 95.432 | 81.108 | +4.29% | +0.19% | 2.34x | 7.9 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.539e-06 | 71.641 | 73.064 | +3.42% | -0.65% | 1.18x | 2.8 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.02 | 69.710 | 57.617 | +0.60% | -0.19% | 2.30x | 3.1 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XMR/USD | 496 | 67.334 | 65.033 | +2.05% | +0.44% | 1.01x | 8.7 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LTC/USD | 41.73 | 60.960 | 59.040 | +0.75% | -0.24% | 1.31x | 2.4 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94912 | 56.867 | 62.198 | +1.04% | -0.39% | 0.66x | 0.1 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | DOT/USD | 0.6843 | 53.869 | 41.774 | +1.30% | -0.58% | 3.47x | 4.4 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.022 | 52.911 | 61.432 | +1.37% | -0.70% | 0.50x | 6.3 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | LINK/USD | 9.07734 | 51.851 | 58.755 | +0.80% | -0.21% | 0.42x | 3.7 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | NIGHT/USD | 0.0492 | 50.953 | 59.934 | +2.18% | -0.49% | 0.34x | 10.2 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | TIA/USD | 0.3415 | 49.171 | 42.395 | +1.70% | -0.61% | 1.98x | 2.9 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | MODERATE 45/100 | HIGH 66/100 | Watch | WATCH |
| 12 | WLD/USD | 0.2428 | 35.980 | 46.371 | +1.89% | -0.86% | 0.39x | 4.1 | 2026-11-24T06:31:28.236757+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.108 | 25.497 | +0.19% | 2.34x |
| 2 | PEPE/USD | 73.064 | 3.539e-06 | -0.65% | 1.18x |
| 3 | XMR/USD | 65.033 | 496 | +0.44% | 1.01x |
| 4 | XRP/USD | 62.198 | 0.94912 | -0.39% | 0.66x |
| 5 | NEAR/USD | 61.432 | 3.022 | -0.70% | 0.50x |
| 6 | NIGHT/USD | 59.934 | 0.0492 | -0.49% | 0.34x |
| 7 | LTC/USD | 59.040 | 41.73 | -0.24% | 1.31x |
| 8 | LINK/USD | 58.755 | 9.07734 | -0.21% | 0.42x |
| 9 | HYPE/USD | 57.617 | 64.02 | -0.19% | 2.30x |
| 10 | WLD/USD | 46.371 | 0.2428 | -0.86% | 0.39x |
| 11 | TIA/USD | 42.395 | 0.3415 | -0.61% | 1.98x |
| 12 | DOT/USD | 41.774 | 0.6843 | -0.58% | 3.47x |

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

- Persisted scans: 1538; predictions: 13189; observations: 931740.
- Matured sampled outcomes across 1/6/24/48h: 24754; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 138 (sampled only; not a success-rate estimate).
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

**Writer:** 45340839080 · **Generation:** 1538 · **Legacy run:** 45340839080
**Main quote time:** 2026-11-24T06:31:34.566782+00:00 · **Legacy report time:** 2026-11-24T06:32:45.540360+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.497 | 95.43 | +0.19% | 2.34x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | PEPE/USD | 3.539e-06 | 71.64 | -0.65% | 1.18x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 3 | HYPE/USD | 64.02 | 69.71 | -0.19% | 2.30x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD ⭐ | 496 | 67.33 | +0.44% | 1.01x | STRONG 79/100 | HIGH 62/100 | Watch |
| 5 | LTC/USD | 41.73 | 60.96 | -0.24% | 1.31x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.94912 | 56.87 | -0.39% | 0.66x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | DOT/USD | 0.6843 | 53.87 | -0.58% | 3.47x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 8 | NEAR/USD | 3.022 | 52.91 | -0.70% | 0.50x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | LINK/USD | 9.07734 | 51.85 | -0.21% | 0.42x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | NIGHT/USD | 0.0492 | 50.95 | -0.49% | 0.34x | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | TIA/USD | 0.3415 | 49.17 | -0.61% | 1.98x | MODERATE 45/100 | HIGH 66/100 | Watch |
| 12 | WLD/USD | 0.2428 | 35.98 | -0.86% | 0.39x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.444 | 90.92 | +0.19% | 2.34x | 12449 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | BABY/USD | 0.00886 | 84.06 | +1.71% | 4.65x | 3106 | STRONG 92/100 | VERY_HIGH 73/100 | Watch |
| 3 | INX/USD | 0.00407 | 73.05 | +0.66% | 1.03x | 3600 | MODERATE 62/100 | EXTREME 86/100 | Do nothing |
| 4 | XMR/USD ⭐ | 496.28 | 63.70 | +0.44% | 1.01x | 11700 | STRONG 72/100 | HIGH 68/100 | Watch |

**Same-run overlap:** VVV/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
