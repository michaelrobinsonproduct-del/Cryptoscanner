# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T18:51:24.070559+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45878966570
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6e16d2959dde8713836487215aa9ff04a05dbd5d (atomic ledger/results publication)
**Ledger generation:** 1899 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.095 | 91.361 | 77.037 | +6.93% | +0.64% | 2.11x | 9.1 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.150327 | 90.634 | 74.987 | +3.13% | +0.13% | 4.23x | 3.8 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SKY/USD | 0.0458 | 90.605 | 76.588 | +9.36% | -0.20% | 2.81x | 6.6 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5056 | 86.636 | 71.043 | +6.87% | +0.12% | 14.55x | 13.8 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 5 | WIF/USD | 0.1408 | 77.303 | 69.594 | +10.60% | +0.64% | 1.45x | 14.2 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 79/100 | HIGH 66/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0996 | 75.033 | 65.276 | +1.63% | +0.19% | 1.88x | 2.3 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1699.53 | 74.130 | 58.747 | +0.54% | +0.08% | 3.59x | 0.1 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95495 | 70.290 | 68.693 | +1.96% | +0.10% | 1.11x | 0.1 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 9 | DRV/USD | 0.39199 | 69.973 | 67.462 | +9.56% | +0.84% | 0.83x | 28.1 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | LINK/USD | 9.26471 | 67.677 | 70.297 | +2.43% | +0.13% | 0.67x | 2.9 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SOL/USD | 71.26 | 67.397 | 62.950 | +1.24% | +0.01% | 1.44x | 1.4 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 12 | LTC/USD | 43.36 | 62.697 | 64.500 | +1.52% | -0.02% | 0.83x | 2.3 | 2026-11-26T18:51:17.870062+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 77.037 | 1.095 | +0.64% | 2.11x |
| 2 | SKY/USD | 76.588 | 0.0458 | -0.20% | 2.81x |
| 3 | ADA/USD | 74.987 | 0.150327 | +0.13% | 4.23x |
| 4 | AKT/USD | 71.043 | 0.5056 | +0.12% | 14.55x |
| 5 | LINK/USD | 70.297 | 9.26471 | +0.13% | 0.67x |
| 6 | WIF/USD | 69.594 | 0.1408 | +0.64% | 1.45x |
| 7 | XRP/USD | 68.693 | 0.95495 | +0.10% | 1.11x |
| 8 | DRV/USD | 67.462 | 0.39199 | +0.84% | 0.83x |
| 9 | NEAR/USD | 65.276 | 3.0996 | +0.19% | 1.88x |
| 10 | LTC/USD | 64.500 | 43.36 | -0.02% | 0.83x |
| 11 | SOL/USD | 62.950 | 71.26 | +0.01% | 1.44x |
| 12 | ETH/USD | 58.747 | 1699.53 | +0.08% | 3.59x |

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

- Persisted scans: 1899; predictions: 16523; observations: 1150445.
- Matured sampled outcomes across 1/6/24/48h: 35780; gap abstentions: 25163. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45878966570 · **Generation:** 1899 · **Legacy run:** 45878966570
**Main quote time:** 2026-11-26T18:51:24.070559+00:00 · **Legacy report time:** 2026-11-26T18:52:14.085466+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.095 | 91.36 | +0.64% | 2.11x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.150327 | 90.63 | +0.13% | 4.23x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD | 0.0458 | 90.61 | -0.20% | 2.81x | STRONG 75/100 | HIGH 66/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5056 | 86.64 | +0.12% | 14.55x | STRONG 93/100 | HIGH 66/100 | Watch |
| 5 | WIF/USD | 0.1408 | 77.30 | +0.64% | 1.45x | STRONG 79/100 | HIGH 66/100 | Watch |
| 6 | NEAR/USD | 3.0996 | 75.03 | +0.19% | 1.88x | STRONG 73/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD | 1699.53 | 74.13 | +0.08% | 3.59x | STRONG 82/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD ⭐ | 0.95495 | 70.29 | +0.10% | 1.11x | STRONG 70/100 | HIGH 62/100 | Watch |
| 9 | DRV/USD | 0.39199 | 69.97 | +0.84% | 0.83x | MODERATE 55/100 | VERY_HIGH 79/100 | Watch |
| 10 | LINK/USD | 9.26471 | 67.68 | +0.13% | 0.67x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 11 | SOL/USD | 71.26 | 67.40 | +0.01% | 1.44x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 12 | LTC/USD | 43.36 | 62.70 | -0.02% | 0.83x | WEAK 36/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.150239 | 88.52 | +0.13% | 4.23x | 10548 | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5046 | 80.24 | +0.12% | 14.55x | 2746 | STRONG 90/100 | HIGH 66/100 | Watch |
| 3 | ZRO/USD ⭐ | 1.095 | 76.96 | +0.64% | 2.11x | 2235 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 4 | XRP/USD ⭐ | 0.95397 | 72.74 | +0.10% | 1.11x | 29422 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZRO/USD, ADA/USD, AKT/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
