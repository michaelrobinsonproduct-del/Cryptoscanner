# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:20:20.576508+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44575946306
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 8122aab66f5dcba919e3561f817586109a5e8a46 (atomic ledger/results publication)
**Ledger generation:** 823 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.399 | 94.708 | 75.169 | +3.36% | +0.91% | 3.84x | 6.7 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | BMT/USD | 0.02046 | 87.876 | 71.403 | +8.37% | +0.29% | 30.85x | 9.8 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | STRONG 99/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | SKR/USD | 0.010136 | 67.814 | 62.197 | +5.22% | +0.00% | 1.56x | 10.8 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5342 | 62.395 | 47.020 | +3.13% | +0.07% | 14.92x | 13.1 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | STRONG 71/100 | HIGH 66/100 | Watch | WATCH |
| 5 | TRUST/USD | 0.05459 | 60.966 | 66.196 | +10.96% | -0.49% | 0.72x | 20.1 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | WEAK 25/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | BILL/USD | 0.00435 | 58.342 | 64.375 | +10.13% | +0.23% | 0.28x | 22.9 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | PYTH/USD | 0.05484 | 55.357 | 51.542 | +3.94% | -1.30% | 2.03x | 16.4 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021466 | 54.316 | 59.677 | +4.18% | -1.06% | 1.00x | 7.9 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 9 | ALEO/USD | 0.0309 | 44.315 | 52.574 | +3.07% | -0.52% | 0.43x | 3.2 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | PUMP/USD | 0.002633 | 43.390 | 46.645 | +1.43% | -0.08% | 0.71x | 11.4 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | INJ/USD | 7.024 | 42.649 | 44.809 | +0.62% | -0.21% | 0.89x | 5.7 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | CAP/USD | 0.09805 | 41.871 | 46.155 | +2.12% | -0.13% | 0.64x | 6.1 | 2026-11-19T17:20:13.534115+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 75.169 | 22.399 | +0.91% | 3.84x |
| 2 | BMT/USD | 71.403 | 0.02046 | +0.29% | 30.85x |
| 3 | TRUST/USD | 66.196 | 0.05459 | -0.49% | 0.72x |
| 4 | BILL/USD | 64.375 | 0.00435 | +0.23% | 0.28x |
| 5 | SKR/USD | 62.197 | 0.010136 | +0.00% | 1.56x |
| 6 | SENT/USD | 59.677 | 0.021466 | -1.06% | 1.00x |
| 7 | ALEO/USD | 52.574 | 0.0309 | -0.52% | 0.43x |
| 8 | PYTH/USD | 51.542 | 0.05484 | -1.30% | 2.03x |
| 9 | AKT/USD | 47.020 | 0.5342 | +0.07% | 14.92x |
| 10 | PUMP/USD | 46.645 | 0.002633 | -0.08% | 0.71x |
| 11 | CAP/USD | 46.155 | 0.09805 | -0.13% | 0.64x |
| 12 | INJ/USD | 44.809 | 7.024 | -0.21% | 0.89x |

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

- Persisted scans: 823; predictions: 7020; observations: 497565.
- Matured sampled outcomes across 1/6/24/48h: 6995; gap abstentions: 15431. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44575946306 · **Generation:** 823 · **Legacy run:** 44575946306
**Main quote time:** 2026-11-19T17:20:20.576508+00:00 · **Legacy report time:** 2026-11-19T17:21:05.901676+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.399 | 94.71 | +0.91% | 3.84x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BMT/USD ⭐ | 0.02046 | 87.88 | +0.29% | 30.85x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | SKR/USD | 0.010136 | 67.81 | +0.00% | 1.56x | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5342 | 62.40 | +0.07% | 14.92x | STRONG 81/100 | HIGH 66/100 | Watch |
| 5 | TRUST/USD | 0.05459 | 60.97 | -0.49% | 0.72x | WEAK 25/100 | EXTREME 100/100 | Do nothing |
| 6 | BILL/USD | 0.00435 | 58.34 | +0.23% | 0.28x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |
| 7 | PYTH/USD | 0.05484 | 55.36 | -1.30% | 2.03x | MODERATE 53/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SENT/USD | 0.021466 | 54.32 | -1.06% | 1.00x | WEAK 32/100 | VERY_HIGH 77/100 | Do nothing |
| 9 | ALEO/USD | 0.0309 | 44.32 | -0.52% | 0.43x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | PUMP/USD | 0.002633 | 43.39 | -0.08% | 0.71x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | INJ/USD | 7.024 | 42.65 | -0.21% | 0.89x | WEAK 26/100 | HIGH 68/100 | Do nothing |
| 12 | CAP/USD | 0.09805 | 41.87 | -0.13% | 0.64x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.442 | 90.42 | +0.91% | 3.84x | 12119 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | BMT/USD ⭐ | 0.02046 | 79.66 | +0.29% | 30.85x | 3168 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | USELESS/USD | 0.0983 | 69.73 | +0.31% | 12.64x | 3236 | STRONG 85/100 | HIGH 61/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5342 | 68.84 | +0.07% | 14.92x | 3195 | STRONG 89/100 | HIGH 60/100 | Watch |

**Same-run overlap:** VVV/USD, BMT/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
