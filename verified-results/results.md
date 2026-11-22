# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T21:31:16.548718+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45072384898
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 6708c516b2798606e284300270c0584d534638b5 (atomic ledger/results publication)
**Ledger generation:** 1338 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04863 | 99.593 | 86.941 | +9.82% | -0.47% | 3.14x | 12.3 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9995 | 96.299 | 80.787 | +3.92% | +0.58% | 2.26x | 3.3 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 62.66 | 84.555 | 69.635 | +2.32% | -0.02% | 2.75x | 3.2 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 26.015 | 84.401 | 83.461 | +4.48% | -0.28% | 1.24x | 5.8 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002578 | 80.181 | 82.764 | +9.98% | +0.58% | 0.45x | 7.8 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6566 | 79.576 | 64.195 | +1.44% | +0.08% | 10.31x | 1.5 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1722.26 | 74.194 | 71.607 | +2.38% | +0.08% | 1.22x | 0.1 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ZEC/USD | 792.81 | 67.219 | 66.403 | +1.88% | -0.08% | 1.12x | 3.5 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XBT/USD | 60896.6 | 65.890 | 64.389 | +1.34% | +0.02% | 1.14x | 0.0 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 10 | STBL/USD | 0.017205 | 64.417 | 66.992 | +7.50% | +0.57% | 0.46x | 18.0 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | BNB/USD | 557.11 | 63.671 | 48.635 | +1.77% | +0.01% | 2.67x | 1.3 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XMR/USD | 494.14 | 53.092 | 55.192 | +0.48% | +0.06% | 0.76x | 6.3 | 2026-11-22T21:31:07.824426+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 86.941 | 0.04863 | -0.47% | 3.14x |
| 2 | VVV/USD | 83.461 | 26.015 | -0.28% | 1.24x |
| 3 | PUMP/USD | 82.764 | 0.002578 | +0.58% | 0.45x |
| 4 | NEAR/USD | 80.787 | 2.9995 | +0.58% | 2.26x |
| 5 | ETH/USD | 71.607 | 1722.26 | +0.08% | 1.22x |
| 6 | HYPE/USD | 69.635 | 62.66 | -0.02% | 2.75x |
| 7 | STBL/USD | 66.992 | 0.017205 | +0.57% | 0.46x |
| 8 | ZEC/USD | 66.403 | 792.81 | -0.08% | 1.12x |
| 9 | XBT/USD | 64.389 | 60896.6 | +0.02% | 1.14x |
| 10 | SUI/USD | 64.195 | 0.6566 | +0.08% | 10.31x |
| 11 | XMR/USD | 55.192 | 494.14 | +0.06% | 0.76x |
| 12 | BNB/USD | 48.635 | 557.11 | +0.01% | 2.67x |

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

- Persisted scans: 1338; predictions: 10975; observations: 809950.
- Matured sampled outcomes across 1/6/24/48h: 16773; gap abstentions: 22365. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45072384898 · **Generation:** 1338 · **Legacy run:** 45072384898
**Main quote time:** 2026-11-22T21:31:16.548718+00:00 · **Legacy report time:** 2026-11-22T21:32:02.278844+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04863 | 99.59 | -0.47% | 3.14x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.9995 | 96.30 | +0.58% | 2.26x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD | 62.66 | 84.56 | -0.02% | 2.75x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 26.015 | 84.40 | -0.28% | 1.24x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 5 | PUMP/USD | 0.002578 | 80.18 | +0.58% | 0.45x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 6 | SUI/USD | 0.6566 | 79.58 | +0.08% | 10.31x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD ⭐ | 1722.26 | 74.19 | +0.08% | 1.22x | STRONG 72/100 | HIGH 62/100 | Watch |
| 8 | ZEC/USD | 792.81 | 67.22 | -0.08% | 1.12x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | XBT/USD | 60896.6 | 65.89 | +0.02% | 1.14x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 10 | STBL/USD | 0.017205 | 64.42 | +0.57% | 0.46x | MODERATE 57/100 | EXTREME 88/100 | Do nothing |
| 11 | BNB/USD | 557.11 | 63.67 | +0.01% | 2.67x | STRONG 77/100 | HIGH 55/100 | Watch |
| 12 | XMR/USD | 494.14 | 53.09 | +0.06% | 0.76x | MODERATE 47/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9938 | 97.47 | +0.58% | 2.26x | 12717 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1721.62 | 81.06 | +0.08% | 1.22x | 38845 | STRONG 76/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD | 190.8182 | 80.70 | +0.26% | 3.35x | 5052 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD | 8.81261 | 70.64 | +0.09% | 1.44x | 4489 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
