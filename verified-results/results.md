# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T05:11:29.957072+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45116012628
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ce5a8a94c57de01093f0559e9e34b12e48bc80e2 (atomic ledger/results publication)
**Ledger generation:** 1385 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.07553 | 60.444 | 55.377 | +3.08% | -0.40% | 1.70x | 2.6 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | MODERATE 50/100 | HIGH 66/100 | Watch | WATCH |
| 2 | XMR/USD | 500.8 | 59.788 | 62.456 | +1.44% | -0.20% | 0.83x | 5.2 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 3 | LINK/USD | 8.87792 | 59.281 | 46.766 | +0.76% | -0.04% | 2.27x | 4.2 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | JUP/USD | 0.23135 | 59.086 | 49.105 | +3.02% | -0.13% | 2.06x | 11.7 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.0025 | 58.211 | 57.720 | +0.70% | +0.24% | 0.93x | 4.3 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.408e-06 | 57.961 | 41.191 | +0.56% | +0.35% | 3.87x | 2.9 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LTC/USD | 40.39 | 57.806 | 46.111 | +0.57% | +0.07% | 2.13x | 2.5 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | AI/USD | 0.01573 | 57.310 | 66.513 | +7.59% | -1.01% | 0.58x | 19.1 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | WEAK 29/100 | EXTREME 98/100 | Do nothing | WATCH |
| 9 | NIGHT/USD | 0.04994 | 54.593 | 58.511 | +1.57% | +0.30% | 0.46x | 6.0 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 71.17 | 54.536 | 59.650 | +0.76% | -0.15% | 0.57x | 1.4 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.6574 | 54.536 | 56.055 | +0.26% | -0.11% | 0.90x | 1.5 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.9315 | 50.174 | 57.344 | +0.43% | -0.13% | 0.35x | 1.3 | 2026-11-23T05:11:22.317826+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 66.513 | 0.01573 | -1.01% | 0.58x |
| 2 | XMR/USD | 62.456 | 500.8 | -0.20% | 0.83x |
| 3 | SOL/USD | 59.650 | 71.17 | -0.15% | 0.57x |
| 4 | NIGHT/USD | 58.511 | 0.04994 | +0.30% | 0.46x |
| 5 | NEAR/USD | 57.720 | 3.0025 | +0.24% | 0.93x |
| 6 | XRP/USD | 57.344 | 0.9315 | -0.13% | 0.35x |
| 7 | SUI/USD | 56.055 | 0.6574 | -0.11% | 0.90x |
| 8 | CC/USD | 55.377 | 0.07553 | -0.40% | 1.70x |
| 9 | JUP/USD | 49.105 | 0.23135 | -0.13% | 2.06x |
| 10 | LINK/USD | 46.766 | 8.87792 | -0.04% | 2.27x |
| 11 | LTC/USD | 46.111 | 40.39 | +0.07% | 2.13x |
| 12 | PEPE/USD | 41.191 | 3.408e-06 | +0.35% | 3.87x |

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

- Persisted scans: 1385; predictions: 11387; observations: 838570.
- Matured sampled outcomes across 1/6/24/48h: 18425; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 106 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45116012628 · **Generation:** 1385 · **Legacy run:** 45116012628
**Main quote time:** 2026-11-23T05:11:29.957072+00:00 · **Legacy report time:** 2026-11-23T05:12:21.589093+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD | 0.07553 | 60.44 | -0.40% | 1.70x | MODERATE 50/100 | HIGH 66/100 | Watch |
| 2 | XMR/USD | 500.8 | 59.79 | -0.20% | 0.83x | WEAK 35/100 | HIGH 68/100 | Watch |
| 3 | LINK/USD | 8.87792 | 59.28 | -0.04% | 2.27x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | JUP/USD | 0.23135 | 59.09 | -0.13% | 2.06x | MODERATE 55/100 | VERY_HIGH 72/100 | Watch |
| 5 | NEAR/USD | 3.0025 | 58.21 | +0.24% | 0.93x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 6 | PEPE/USD | 3.408e-06 | 57.96 | +0.35% | 3.87x | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | LTC/USD | 40.39 | 57.81 | +0.07% | 2.13x | STRONG 74/100 | HIGH 55/100 | Watch |
| 8 | AI/USD | 0.01573 | 57.31 | -1.01% | 0.58x | WEAK 29/100 | EXTREME 98/100 | Do nothing |
| 9 | NIGHT/USD | 0.04994 | 54.59 | +0.30% | 0.46x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 71.17 | 54.54 | -0.15% | 0.57x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SUI/USD | 0.6574 | 54.54 | -0.11% | 0.90x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 12 | XRP/USD | 0.9315 | 50.17 | -0.13% | 0.35x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

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
