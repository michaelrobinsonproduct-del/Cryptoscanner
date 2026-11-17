# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:30:01.760732+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44190570384
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** d08d5631d538a58bc7f8d1cce2fb22aae98fb6f2 (atomic ledger/results publication)
**Ledger generation:** 459 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3254 | 89.855 | 89.594 | +5.31% | +0.93% | 0.56x | 5.1 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 943.1 | 87.302 | 85.377 | +4.35% | +1.02% | 0.68x | 0.1 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.109e-05 | 83.441 | 70.619 | +10.16% | -0.44% | 4.78x | 14.6 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | INJ/USD | 7.199 | 77.872 | 82.666 | +4.35% | +0.45% | 0.30x | 5.5 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | JUP/USD | 0.25758 | 77.467 | 72.694 | +7.08% | +0.82% | 1.07x | 10.9 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | TRUST/USD | 0.0474 | 75.009 | 76.949 | +10.21% | +0.72% | 0.44x | 2.1 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | SOL/USD | 73.78 | 74.403 | 76.442 | +3.16% | +0.45% | 0.57x | 1.4 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97093 | 73.282 | 66.546 | +1.69% | +0.20% | 1.57x | 0.6 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | AKT/USD | 0.503 | 68.130 | 67.042 | +5.14% | +1.13% | 0.54x | 2.0 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | XMR/USD | 505.34 | 65.088 | 68.213 | +2.38% | +0.33% | 0.52x | 6.9 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | VVV/USD | 20.815 | 63.055 | 65.847 | +3.31% | +1.31% | 0.07x | 7.7 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 9.20261 | 62.372 | 56.830 | +0.74% | +0.12% | 1.50x | 3.9 | 2026-11-17T22:29:55.664585+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 89.594 | 3.3254 | +0.93% | 0.56x |
| 2 | ZEC/USD | 85.377 | 943.1 | +1.02% | 0.68x |
| 3 | INJ/USD | 82.666 | 7.199 | +0.45% | 0.30x |
| 4 | TRUST/USD | 76.949 | 0.0474 | +0.72% | 0.44x |
| 5 | SOL/USD | 76.442 | 73.78 | +0.45% | 0.57x |
| 6 | JUP/USD | 72.694 | 0.25758 | +0.82% | 1.07x |
| 7 | LUNA/USD | 70.619 | 4.109e-05 | -0.44% | 4.78x |
| 8 | XMR/USD | 68.213 | 505.34 | +0.33% | 0.52x |
| 9 | AKT/USD | 67.042 | 0.503 | +1.13% | 0.54x |
| 10 | XRP/USD | 66.546 | 0.97093 | +0.20% | 1.57x |
| 11 | VVV/USD | 65.847 | 20.815 | +1.31% | 0.07x |
| 12 | LINK/USD | 56.830 | 9.20261 | +0.12% | 1.50x |

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

- Persisted scans: 459; predictions: 3989; observations: 276538.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44190570384 · **Generation:** 459 · **Legacy run:** 44190570384
**Main quote time:** 2026-11-17T22:30:01.760732+00:00 · **Legacy report time:** 2026-11-17T22:30:10.883046+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.3254 | 89.86 | +0.93% | 0.56x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD ⭐ | 943.1 | 87.30 | +1.02% | 0.68x | STRONG 84/100 | VERY_HIGH 70/100 | Watch |
| 3 | LUNA/USD ⭐ | 4.109e-05 | 83.44 | -0.44% | 4.78x | STRONG 77/100 | VERY_HIGH 72/100 | Watch |
| 4 | INJ/USD | 7.199 | 77.87 | +0.45% | 0.30x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 5 | JUP/USD | 0.25758 | 77.47 | +0.82% | 1.07x | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 6 | TRUST/USD | 0.0474 | 75.01 | +0.72% | 0.44x | MODERATE 68/100 | VERY_HIGH 75/100 | Watch |
| 7 | SOL/USD | 73.78 | 74.40 | +0.45% | 0.57x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD ⭐ | 0.97093 | 73.28 | +0.20% | 1.57x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 9 | AKT/USD ⭐ | 0.503 | 68.13 | +1.13% | 0.54x | STRONG 74/100 | VERY_HIGH 75/100 | Watch |
| 10 | XMR/USD | 505.34 | 65.09 | +0.33% | 0.52x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 11 | VVV/USD | 20.815 | 63.05 | +1.31% | 0.07x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 9.20261 | 62.37 | +0.12% | 1.50x | MODERATE 66/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 943.59 | 93.99 | +0.74% | 1.59x | 25813 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LUNA/USD ⭐ | 4.109e-05 | 82.11 | +0.78% | 4.78x | 3237 | STRONG 96/100 | VERY_HIGH 72/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5031 | 80.69 | +1.31% | 1.62x | 2932 | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 4 | RENDER/USD | 1.443 | 79.67 | +0.49% | 5.10x | 2395 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.97106 | 73.79 | +0.10% | 1.81x | 29741 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, LUNA/USD, XRP/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
