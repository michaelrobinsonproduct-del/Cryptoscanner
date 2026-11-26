# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T08:26:17.879628+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45782904405
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5d37925a3f1b20f7d25ebe54df0142aa3aef0641 (atomic ledger/results publication)
**Ledger generation:** 1836 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08032 | 76.733 | 59.102 | +2.86% | +0.53% | 74.39x | 2.5 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.95253 | 72.882 | 66.569 | +1.71% | +0.08% | 1.59x | 0.7 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 43.27 | 61.839 | 63.022 | +1.31% | -0.21% | 0.99x | 2.3 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.07308 | 60.953 | 69.794 | +10.28% | -0.57% | 0.40x | 15.1 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | SOL/USD | 70.82 | 59.452 | 57.864 | +0.61% | -0.08% | 1.20x | 2.8 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | INJ/USD | 6.156 | 57.695 | 62.096 | +3.39% | -0.06% | 0.59x | 8.1 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | LINK/USD | 9.1509 | 57.474 | 62.252 | +1.18% | +0.02% | 0.51x | 0.2 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.147525 | 55.501 | 61.665 | +1.20% | -0.18% | 0.47x | 3.5 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XBT/USD | 60594 | 52.335 | 57.605 | +0.37% | -0.01% | 0.48x | 0.0 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | AAVE/USD | 95.83 | 51.834 | 42.672 | +0.49% | +0.30% | 1.76x | 5.2 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128422 | 49.442 | 46.318 | +0.47% | -0.08% | 1.35x | 2.8 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0564713 | 49.408 | 56.051 | +0.92% | +0.01% | 0.33x | 0.8 | 2026-11-26T08:26:11.674987+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 69.794 | 0.07308 | -0.57% | 0.40x |
| 2 | XRP/USD | 66.569 | 0.95253 | +0.08% | 1.59x |
| 3 | LTC/USD | 63.022 | 43.27 | -0.21% | 0.99x |
| 4 | LINK/USD | 62.252 | 9.1509 | +0.02% | 0.51x |
| 5 | INJ/USD | 62.096 | 6.156 | -0.06% | 0.59x |
| 6 | ADA/USD | 61.665 | 0.147525 | -0.18% | 0.47x |
| 7 | ALGO/USD | 59.102 | 0.08032 | +0.53% | 74.39x |
| 8 | SOL/USD | 57.864 | 70.82 | -0.08% | 1.20x |
| 9 | XBT/USD | 57.605 | 60594 | -0.01% | 0.48x |
| 10 | XDG/USD | 56.051 | 0.0564713 | +0.01% | 0.33x |
| 11 | XLM/USD | 46.318 | 0.128422 | -0.08% | 1.35x |
| 12 | AAVE/USD | 42.672 | 95.83 | +0.30% | 1.76x |

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

- Persisted scans: 1836; predictions: 15767; observations: 1113166.
- Matured sampled outcomes across 1/6/24/48h: 34166; gap abstentions: 24324. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45782904405 · **Generation:** 1836 · **Legacy run:** 45782904405
**Main quote time:** 2026-11-26T08:26:17.879628+00:00 · **Legacy report time:** 2026-11-26T08:27:36.096151+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08032 | 76.73 | +0.53% | 74.39x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95253 | 72.88 | +0.08% | 1.59x | STRONG 81/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD | 43.27 | 61.84 | -0.21% | 0.99x | WEAK 36/100 | HIGH 68/100 | Watch |
| 4 | SYRUP/USD | 0.07308 | 60.95 | -0.57% | 0.40x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 5 | SOL/USD | 70.82 | 59.45 | -0.08% | 1.20x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | INJ/USD | 6.156 | 57.69 | -0.06% | 0.59x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | LINK/USD | 9.1509 | 57.47 | +0.02% | 0.51x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.147525 | 55.50 | -0.18% | 0.47x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XBT/USD | 60594 | 52.34 | -0.01% | 0.48x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | AAVE/USD | 95.83 | 51.83 | +0.30% | 1.76x | STRONG 71/100 | HIGH 55/100 | Watch |
| 11 | XLM/USD | 0.128422 | 49.44 | -0.08% | 1.35x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 12 | XDG/USD | 0.0564713 | 49.41 | +0.01% | 0.33x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08032 | 74.62 | +0.53% | 74.39x | 5391 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95212 | 74.33 | +0.08% | 1.59x | 42100 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ALGO/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
