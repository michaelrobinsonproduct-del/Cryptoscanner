# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:55:24.657848+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44560094021
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 6b925cf6002d7f789927841ac7c966dd673ccfe0 (atomic ledger/results publication)
**Ledger generation:** 807 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | USELESS/USD | 0.10115 | 87.688 | 71.996 | +5.85% | +0.14% | 3.00x | 12.9 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PYTH/USD | 0.05638 | 84.059 | 73.630 | +6.86% | +0.16% | 1.96x | 7.1 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 3 | TRUST/USD | 0.05412 | 76.287 | 65.046 | +10.00% | -0.75% | 4.69x | 22.2 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | SKR/USD | 0.010481 | 74.650 | 70.279 | +8.80% | +1.56% | 0.66x | 11.5 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | MODERATE 62/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | VVV/USD | 22.475 | 73.001 | 77.407 | +3.71% | -0.23% | 0.67x | 7.1 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SENT/USD | 0.021307 | 69.898 | 56.683 | +3.41% | +0.56% | 2.04x | 2.8 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.10242 | 69.286 | 63.761 | +7.86% | -0.25% | 1.68x | 25.4 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 85/100 | Do nothing | WATCH |
| 8 | BILL/USD | 0.00427 | 63.968 | 64.029 | +8.10% | -0.23% | 1.11x | 23.5 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | WEAK 32/100 | EXTREME 92/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5474 | 63.389 | 63.919 | +5.68% | +0.20% | 0.85x | 14.6 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 10 | ADA/USD | 0.152171 | 62.011 | 56.975 | +0.61% | +0.26% | 1.37x | 4.5 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 11 | INJ/USD | 7.076 | 55.970 | 50.914 | +1.36% | +0.11% | 1.45x | 4.2 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BNB/USD | 585.28 | 48.307 | 46.078 | +0.69% | +0.18% | 1.13x | 0.9 | 2026-11-19T15:55:15.803701+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.407 | 22.475 | -0.23% | 0.67x |
| 2 | PYTH/USD | 73.630 | 0.05638 | +0.16% | 1.96x |
| 3 | USELESS/USD | 71.996 | 0.10115 | +0.14% | 3.00x |
| 4 | SKR/USD | 70.279 | 0.010481 | +1.56% | 0.66x |
| 5 | TRUST/USD | 65.046 | 0.05412 | -0.75% | 4.69x |
| 6 | BILL/USD | 64.029 | 0.00427 | -0.23% | 1.11x |
| 7 | AKT/USD | 63.919 | 0.5474 | +0.20% | 0.85x |
| 8 | SYRUP/USD | 63.761 | 0.10242 | -0.25% | 1.68x |
| 9 | ADA/USD | 56.975 | 0.152171 | +0.26% | 1.37x |
| 10 | SENT/USD | 56.683 | 0.021307 | +0.56% | 2.04x |
| 11 | INJ/USD | 50.914 | 7.076 | +0.11% | 1.45x |
| 12 | BNB/USD | 46.078 | 585.28 | +0.18% | 1.13x |

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

- Persisted scans: 807; predictions: 6828; observations: 488007.
- Matured sampled outcomes across 1/6/24/48h: 6815; gap abstentions: 15270. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44560094021 · **Generation:** 807 · **Legacy run:** 44560094021
**Main quote time:** 2026-11-19T15:55:24.657848+00:00 · **Legacy report time:** 2026-11-19T15:56:09.959087+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.10115 | 87.69 | +0.14% | 3.00x | STRONG 94/100 | HIGH 61/100 | Watch |
| 2 | PYTH/USD ⭐ | 0.05638 | 84.06 | +0.16% | 1.96x | STRONG 87/100 | HIGH 60/100 | Watch |
| 3 | TRUST/USD | 0.05412 | 76.29 | -0.75% | 4.69x | MODERATE 58/100 | EXTREME 85/100 | Do nothing |
| 4 | SKR/USD | 0.010481 | 74.65 | +1.56% | 0.66x | MODERATE 62/100 | EXTREME 88/100 | Do nothing |
| 5 | VVV/USD | 22.475 | 73.00 | -0.23% | 0.67x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | SENT/USD ⭐ | 0.021307 | 69.90 | +0.56% | 2.04x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 7 | SYRUP/USD | 0.10242 | 69.29 | -0.25% | 1.68x | MODERATE 45/100 | EXTREME 85/100 | Do nothing |
| 8 | BILL/USD | 0.00427 | 63.97 | -0.23% | 1.11x | WEAK 32/100 | EXTREME 92/100 | Do nothing |
| 9 | AKT/USD | 0.5474 | 63.39 | +0.20% | 0.85x | MODERATE 57/100 | VERY_HIGH 80/100 | Watch |
| 10 | ADA/USD | 0.152171 | 62.01 | +0.26% | 1.37x | STRONG 76/100 | HIGH 55/100 | Watch |
| 11 | INJ/USD | 7.076 | 55.97 | +0.11% | 1.45x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 12 | BNB/USD | 585.28 | 48.31 | +0.18% | 1.13x | MODERATE 49/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021317 | 84.06 | +0.56% | 2.04x | 14422 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | USELESS/USD ⭐ | 0.10115 | 82.91 | +0.14% | 3.00x | 3309 | STRONG 91/100 | HIGH 61/100 | Watch |
| 3 | PYTH/USD ⭐ | 0.0563 | 75.64 | +0.16% | 1.96x | 2680 | STRONG 78/100 | HIGH 66/100 | Watch |
| 4 | PUMP/USD | 0.002664 | 70.15 | +0.45% | 3.42x | 4146 | STRONG 85/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** USELESS/USD, PYTH/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
