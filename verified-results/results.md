# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:30:32.819509+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44609211413
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 3a6c7eed69b22a63f3913a4c573ce9d26a6d5061 (atomic ledger/results publication)
**Ledger generation:** 855 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 600; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.167 | 69.140 | 65.834 | +2.29% | -0.31% | 1.49x | 10.4 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5493 | 58.969 | 69.067 | +6.04% | -0.58% | 0.28x | 11.0 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | WEAK 29/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | SKR/USD | 0.010076 | 55.734 | 60.847 | +4.60% | +0.26% | 0.36x | 5.0 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | SENT/USD | 0.020886 | 51.598 | 39.741 | +1.36% | -0.63% | 3.32x | 8.1 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 5 | INJ/USD | 7.012 | 48.261 | 45.641 | +0.44% | -0.76% | 1.64x | 4.3 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.05305 | 41.498 | 28.745 | +0.55% | -0.45% | 2.79x | 15.1 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | PUMP/USD | 0.00263 | 40.641 | 46.539 | +1.31% | +0.65% | 0.08x | 11.5 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | USELESS/USD | 0.0976 | 36.182 | 40.412 | +2.13% | -0.05% | 0.60x | 24.7 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | WEAK 13/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | ICP/USD | 2.188 | 28.623 | 31.508 | +0.46% | +0.69% | 0.37x | 13.8 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | ALEO/USD | 0.03041 | 12.844 | 33.333 | +1.43% | -3.34% | 0.62x | 26.5 | 2026-11-19T20:30:24.506064+00:00 | Not calibrated | WEAK 1/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 69.067 | 0.5493 | -0.58% | 0.28x |
| 2 | VVV/USD | 65.834 | 22.167 | -0.31% | 1.49x |
| 3 | SKR/USD | 60.847 | 0.010076 | +0.26% | 0.36x |
| 4 | PUMP/USD | 46.539 | 0.00263 | +0.65% | 0.08x |
| 5 | INJ/USD | 45.641 | 7.012 | -0.76% | 1.64x |
| 6 | USELESS/USD | 40.412 | 0.0976 | -0.05% | 0.60x |
| 7 | SENT/USD | 39.741 | 0.020886 | -0.63% | 3.32x |
| 8 | ALEO/USD | 33.333 | 0.03041 | -3.34% | 0.62x |
| 9 | ICP/USD | 31.508 | 2.188 | +0.69% | 0.37x |
| 10 | PYTH/USD | 28.745 | 0.05305 | -0.45% | 2.79x |

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

- Persisted scans: 855; predictions: 7401; observations: 516723.
- Matured sampled outcomes across 1/6/24/48h: 7511; gap abstentions: 15650. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44609211413 · **Generation:** 855 · **Legacy run:** 44609211413
**Main quote time:** 2026-11-19T20:30:32.819509+00:00 · **Legacy report time:** 2026-11-19T20:31:22.342422+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.167 | 69.14 | -0.31% | 1.49x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 2 | AKT/USD | 0.5493 | 58.97 | -0.58% | 0.28x | WEAK 29/100 | EXTREME 87/100 | Do nothing |
| 3 | SKR/USD | 0.010076 | 55.73 | +0.26% | 0.36x | MODERATE 58/100 | VERY_HIGH 82/100 | Watch |
| 4 | SENT/USD | 0.020886 | 51.60 | -0.63% | 3.32x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 5 | INJ/USD | 7.012 | 48.26 | -0.76% | 1.64x | WEAK 44/100 | HIGH 61/100 | Watch |
| 6 | PYTH/USD | 0.05305 | 41.50 | -0.45% | 2.79x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 7 | PUMP/USD | 0.00263 | 40.64 | +0.65% | 0.08x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 8 | USELESS/USD | 0.0976 | 36.18 | -0.05% | 0.60x | WEAK 13/100 | EXTREME 88/100 | Do nothing |
| 9 | ICP/USD | 2.188 | 28.62 | +0.69% | 0.37x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 10 | ALEO/USD | 0.03041 | 12.84 | -3.34% | 0.62x | WEAK 1/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
