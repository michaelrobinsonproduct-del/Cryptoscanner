# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T18:21:45.453208+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45237169477
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8fba9ad42d2c40df40e52169ffb0d6280a777124 (atomic ledger/results publication)
**Ledger generation:** 1465 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 160.62 | 104.671 | 91.586 | +11.98% | -0.38% | 3.05x | 16.8 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ICP/USD | 2.089 | 94.658 | 79.897 | +6.26% | -0.05% | 7.74x | 4.8 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CC/USD | 0.07816 | 92.593 | 78.995 | +6.67% | -0.28% | 5.73x | 5.1 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | STRONG 76/100 | HIGH 66/100 | Watch | WATCH |
| 4 | INJ/USD | 6.607 | 85.804 | 92.534 | +6.09% | -0.23% | 0.44x | 6.1 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | LTC/USD | 42.01 | 80.468 | 84.862 | +4.61% | +0.24% | 0.44x | 4.8 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ADA/USD | 0.150736 | 78.389 | 82.533 | +4.24% | +0.26% | 0.45x | 4.3 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | JUP/USD | 0.2463 | 77.493 | 77.904 | +9.68% | -0.29% | 1.10x | 6.9 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | UNI/USD | 4.9129 | 76.581 | 83.305 | +4.95% | -0.06% | 0.36x | 4.5 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6857 | 76.542 | 85.567 | +4.58% | -0.36% | 0.28x | 2.9 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0572604 | 73.378 | 79.154 | +3.58% | +0.10% | 0.37x | 1.7 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XLM/USD | 0.131438 | 72.327 | 74.254 | +3.07% | -0.14% | 0.87x | 4.4 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 12 | SOL/USD | 73.32 | 71.352 | 80.296 | +3.81% | -0.27% | 0.24x | 2.7 | 2026-11-23T18:21:38.965621+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 92.534 | 6.607 | -0.23% | 0.44x |
| 2 | QNT/USD | 91.586 | 160.62 | -0.38% | 3.05x |
| 3 | SUI/USD | 85.567 | 0.6857 | -0.36% | 0.28x |
| 4 | LTC/USD | 84.862 | 42.01 | +0.24% | 0.44x |
| 5 | UNI/USD | 83.305 | 4.9129 | -0.06% | 0.36x |
| 6 | ADA/USD | 82.533 | 0.150736 | +0.26% | 0.45x |
| 7 | SOL/USD | 80.296 | 73.32 | -0.27% | 0.24x |
| 8 | ICP/USD | 79.897 | 2.089 | -0.05% | 7.74x |
| 9 | XDG/USD | 79.154 | 0.0572604 | +0.10% | 0.37x |
| 10 | CC/USD | 78.995 | 0.07816 | -0.28% | 5.73x |
| 11 | JUP/USD | 77.904 | 0.2463 | -0.29% | 1.10x |
| 12 | XLM/USD | 74.254 | 0.131438 | -0.14% | 0.87x |

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

- Persisted scans: 1465; predictions: 12347; observations: 887287.
- Matured sampled outcomes across 1/6/24/48h: 21664; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45237169477 · **Generation:** 1465 · **Legacy run:** 45237169477
**Main quote time:** 2026-11-23T18:21:45.453208+00:00 · **Legacy report time:** 2026-11-23T18:22:55.188140+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 160.62 | 104.67 | -0.38% | 3.05x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | ICP/USD | 2.089 | 94.66 | -0.05% | 7.74x | STRONG 77/100 | HIGH 61/100 | Watch |
| 3 | CC/USD | 0.07816 | 92.59 | -0.28% | 5.73x | STRONG 76/100 | HIGH 66/100 | Watch |
| 4 | INJ/USD | 6.607 | 85.80 | -0.23% | 0.44x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 5 | LTC/USD | 42.01 | 80.47 | +0.24% | 0.44x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 6 | ADA/USD | 0.150736 | 78.39 | +0.26% | 0.45x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 7 | JUP/USD | 0.2463 | 77.49 | -0.29% | 1.10x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 8 | UNI/USD | 4.9129 | 76.58 | -0.06% | 0.36x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 9 | SUI/USD | 0.6857 | 76.54 | -0.36% | 0.28x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 10 | XDG/USD | 0.0572604 | 73.38 | +0.10% | 0.37x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 11 | XLM/USD | 0.131438 | 72.33 | -0.14% | 0.87x | WEAK 41/100 | HIGH 68/100 | Watch |
| 12 | SOL/USD | 73.32 | 71.35 | -0.27% | 0.24x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |

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
