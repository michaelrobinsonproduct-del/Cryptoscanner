# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T02:47:58.093468+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45744424145
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d4483c23f31a1f70740cedf457c06f1e67e57a64 (atomic ledger/results publication)
**Ledger generation:** 1802 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.6772 | 77.560 | 65.712 | +1.64% | +0.37% | 2.00x | 1.5 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.17951 | 77.557 | 63.344 | +1.49% | -0.16% | 74.28x | 0.0 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INJ/USD | 6.242 | 70.404 | 66.500 | +4.84% | +1.32% | 0.73x | 19.3 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | TIA/USD | 0.356 | 69.323 | 69.323 | +5.79% | +1.59% | 0.21x | 5.6 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SOL/USD | 71.34 | 69.020 | 63.746 | +1.35% | +0.07% | 1.49x | 1.4 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.07068 | 68.027 | 67.187 | +6.65% | +0.83% | 0.67x | 19.8 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | ETH/USD | 1702.85 | 67.376 | 59.564 | +0.74% | +0.06% | 1.75x | 1.2 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95766 | 67.020 | 70.353 | +2.25% | +0.28% | 0.52x | 0.8 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ZEC/USD | 780.97 | 64.706 | 62.664 | +1.40% | +0.31% | 1.05x | 4.2 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 10 | LTC/USD | 43.62 | 64.469 | 68.767 | +2.13% | +0.05% | 0.55x | 2.3 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XAUT/USD | 3595 | 62.608 | 45.093 | +0.73% | +0.50% | 8.07x | 0.3 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 12 | TAO/USD | 185.3961 | 61.141 | 65.776 | +2.09% | +0.08% | 0.50x | 7.8 | 2026-11-26T02:47:51.336707+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 70.353 | 0.95766 | +0.28% | 0.52x |
| 2 | TIA/USD | 69.323 | 0.356 | +1.59% | 0.21x |
| 3 | LTC/USD | 68.767 | 43.62 | +0.05% | 0.55x |
| 4 | SYRUP/USD | 67.187 | 0.07068 | +0.83% | 0.67x |
| 5 | INJ/USD | 66.500 | 6.242 | +1.32% | 0.73x |
| 6 | TAO/USD | 65.776 | 185.3961 | +0.08% | 0.50x |
| 7 | SUI/USD | 65.712 | 0.6772 | +0.37% | 2.00x |
| 8 | SOL/USD | 63.746 | 71.34 | +0.07% | 1.49x |
| 9 | LINK/USD | 63.344 | 9.17951 | -0.16% | 74.28x |
| 10 | ZEC/USD | 62.664 | 780.97 | +0.31% | 1.05x |
| 11 | ETH/USD | 59.564 | 1702.85 | +0.06% | 1.75x |
| 12 | XAUT/USD | 45.093 | 3595 | +0.50% | 8.07x |

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

- Persisted scans: 1802; predictions: 15359; observations: 1092462.
- Matured sampled outcomes across 1/6/24/48h: 33347; gap abstentions: 23725. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45744424145 · **Generation:** 1802 · **Legacy run:** 45744424145
**Main quote time:** 2026-11-26T02:47:58.093468+00:00 · **Legacy report time:** 2026-11-26T02:48:49.219583+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.6772 | 77.56 | +0.37% | 2.00x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD | 9.17951 | 77.56 | -0.16% | 74.28x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | INJ/USD | 6.242 | 70.40 | +1.32% | 0.73x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 4 | TIA/USD | 0.356 | 69.32 | +1.59% | 0.21x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 5 | SOL/USD ⭐ | 71.34 | 69.02 | +0.07% | 1.49x | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | SYRUP/USD | 0.07068 | 68.03 | +0.83% | 0.67x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 7 | ETH/USD | 1702.85 | 67.38 | +0.06% | 1.75x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD | 0.95766 | 67.02 | +0.28% | 0.52x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | ZEC/USD | 780.97 | 64.71 | +0.31% | 1.05x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 10 | LTC/USD | 43.62 | 64.47 | +0.05% | 0.55x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | XAUT/USD | 3595 | 62.61 | +0.50% | 8.07x | STRONG 86/100 | HIGH 55/100 | Watch |
| 12 | TAO/USD | 185.3961 | 61.14 | +0.08% | 0.50x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.677 | 70.47 | +0.37% | 2.00x | 8470 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 71.32 | 67.23 | +0.07% | 1.49x | 46985 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SUI/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
