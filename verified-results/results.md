# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:50:28.673879+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44581303928
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 96f4cc20f0f622bcac382e07b03df6515a0de08b (atomic ledger/results publication)
**Ledger generation:** 829 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1273 | 78.926 | 61.161 | +7.70% | +0.55% | 4.34x | 31.4 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | VVV/USD | 22.592 | 74.591 | 79.879 | +4.25% | -1.62% | 1.28x | 9.7 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | MODERATE 47/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | AKT/USD | 0.5565 | 74.448 | 69.885 | +7.43% | +0.61% | 1.15x | 14.4 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | HYPE/USD | 68.45 | 73.404 | 69.972 | +2.35% | -0.28% | 1.48x | 2.9 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | BMT/USD | 0.02045 | 58.566 | 71.435 | +8.32% | -1.16% | 0.29x | 9.8 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 34/100 | EXTREME 92/100 | Do nothing | WATCH |
| 6 | ADA/USD | 0.152948 | 55.170 | 59.766 | +1.12% | -0.46% | 0.77x | 6.1 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | LIGHTER/USD | 2.858 | 55.017 | 66.928 | +5.31% | -0.66% | 0.14x | 10.5 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | SKR/USD | 0.010192 | 54.865 | 62.865 | +5.80% | -1.37% | 0.88x | 17.7 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 27/100 | EXTREME 90/100 | Do nothing | WATCH |
| 9 | SOL/USD | 73.85 | 54.685 | 56.596 | +0.42% | -0.28% | 0.95x | 2.7 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | PUMP/USD | 0.00268 | 50.434 | 59.233 | +3.24% | -0.56% | 0.40x | 11.2 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | RENDER/USD | 1.401 | 49.347 | 35.060 | +0.79% | -0.14% | 2.81x | 7.1 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 12 | XRP/USD | 0.9721 | 49.154 | 58.070 | +0.59% | -0.38% | 0.30x | 2.2 | 2026-11-19T17:50:20.755309+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.879 | 22.592 | -1.62% | 1.28x |
| 2 | BMT/USD | 71.435 | 0.02045 | -1.16% | 0.29x |
| 3 | HYPE/USD | 69.972 | 68.45 | -0.28% | 1.48x |
| 4 | AKT/USD | 69.885 | 0.5565 | +0.61% | 1.15x |
| 5 | LIGHTER/USD | 66.928 | 2.858 | -0.66% | 0.14x |
| 6 | SKR/USD | 62.865 | 0.010192 | -1.37% | 0.88x |
| 7 | CT/USD | 61.161 | 0.1273 | +0.55% | 4.34x |
| 8 | ADA/USD | 59.766 | 0.152948 | -0.46% | 0.77x |
| 9 | PUMP/USD | 59.233 | 0.00268 | -0.56% | 0.40x |
| 10 | XRP/USD | 58.070 | 0.9721 | -0.38% | 0.30x |
| 11 | SOL/USD | 56.596 | 73.85 | -0.28% | 0.95x |
| 12 | RENDER/USD | 35.060 | 1.401 | -0.14% | 2.81x |

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

- Persisted scans: 829; predictions: 7092; observations: 501153.
- Matured sampled outcomes across 1/6/24/48h: 7055; gap abstentions: 15456. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44581303928 · **Generation:** 829 · **Legacy run:** 44581303928
**Main quote time:** 2026-11-19T17:50:28.673879+00:00 · **Legacy report time:** 2026-11-19T17:51:23.018273+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1273 | 78.93 | +0.55% | 4.34x | STRONG 94/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD | 22.592 | 74.59 | -1.62% | 1.28x | MODERATE 47/100 | HIGH 65/100 | Do nothing |
| 3 | AKT/USD ⭐ | 0.5565 | 74.45 | +0.61% | 1.15x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 4 | HYPE/USD | 68.45 | 73.40 | -0.28% | 1.48x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | BMT/USD | 0.02045 | 58.57 | -1.16% | 0.29x | WEAK 34/100 | EXTREME 92/100 | Do nothing |
| 6 | ADA/USD | 0.152948 | 55.17 | -0.46% | 0.77x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 7 | LIGHTER/USD | 2.858 | 55.02 | -0.66% | 0.14x | WEAK 28/100 | EXTREME 87/100 | Do nothing |
| 8 | SKR/USD | 0.010192 | 54.86 | -1.37% | 0.88x | WEAK 27/100 | EXTREME 90/100 | Do nothing |
| 9 | SOL/USD | 73.85 | 54.69 | -0.28% | 0.95x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 10 | PUMP/USD | 0.00268 | 50.43 | -0.56% | 0.40x | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | RENDER/USD | 1.401 | 49.35 | -0.14% | 2.81x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 12 | XRP/USD | 0.9721 | 49.15 | -0.38% | 0.30x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1273 | 76.78 | +0.55% | 4.34x | 2161 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5562 | 73.69 | +0.61% | 1.15x | 3313 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 3 | MEGA/USD | 0.05836 | 68.06 | +0.40% | 1.01x | 2111 | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** CT/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
