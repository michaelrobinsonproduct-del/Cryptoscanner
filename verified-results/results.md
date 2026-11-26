# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T04:25:55.604742+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45755012350
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7c796b6b77475aab8dce57c5dde7e91ac70d932c (atomic ledger/results publication)
**Ledger generation:** 1812 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.9584 | 86.251 | 70.802 | +2.33% | +0.09% | 4.08x | 1.0 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ADA/USD | 0.148981 | 81.956 | 69.178 | +2.20% | +0.15% | 2.20x | 2.5 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 43.89 | 78.147 | 73.201 | +2.76% | +0.07% | 1.46x | 2.3 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6735 | 77.714 | 61.822 | +1.08% | +0.18% | 4.92x | 1.5 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | TAO/USD | 184.3482 | 77.624 | 62.284 | +1.52% | +0.07% | 3.98x | 6.7 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0568289 | 76.262 | 61.176 | +1.55% | +0.02% | 9.57x | 0.3 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 61.94 | 73.475 | 57.828 | +0.52% | +0.13% | 2.77x | 1.6 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XBT/USD | 60959.8 | 73.280 | 61.847 | +0.98% | +0.14% | 2.07x | 0.0 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SYRUP/USD | 0.07188 | 64.083 | 66.008 | +8.47% | +0.46% | 0.58x | 22.2 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.22058 | 61.917 | 64.592 | +1.95% | +0.20% | 0.63x | 3.9 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0638 | 60.697 | 58.027 | +0.46% | +0.55% | 0.99x | 0.3 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PAXG/USD | 3580.82 | 58.487 | 56.987 | +0.31% | +0.25% | 1.03x | 0.4 | 2026-11-26T04:25:46.897784+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 73.201 | 43.89 | +0.07% | 1.46x |
| 2 | XRP/USD | 70.802 | 0.9584 | +0.09% | 4.08x |
| 3 | ADA/USD | 69.178 | 0.148981 | +0.15% | 2.20x |
| 4 | SYRUP/USD | 66.008 | 0.07188 | +0.46% | 0.58x |
| 5 | LINK/USD | 64.592 | 9.22058 | +0.20% | 0.63x |
| 6 | TAO/USD | 62.284 | 184.3482 | +0.07% | 3.98x |
| 7 | XBT/USD | 61.847 | 60959.8 | +0.14% | 2.07x |
| 8 | SUI/USD | 61.822 | 0.6735 | +0.18% | 4.92x |
| 9 | XDG/USD | 61.176 | 0.0568289 | +0.02% | 9.57x |
| 10 | NEAR/USD | 58.027 | 3.0638 | +0.55% | 0.99x |
| 11 | HYPE/USD | 57.828 | 61.94 | +0.13% | 2.77x |
| 12 | PAXG/USD | 56.987 | 3580.82 | +0.25% | 1.03x |

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

- Persisted scans: 1812; predictions: 15479; observations: 1098552.
- Matured sampled outcomes across 1/6/24/48h: 33587; gap abstentions: 23853. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45755012350 · **Generation:** 1812 · **Legacy run:** 45755012350
**Main quote time:** 2026-11-26T04:25:55.604742+00:00 · **Legacy report time:** 2026-11-26T04:26:47.803768+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.9584 | 86.25 | +0.09% | 4.08x | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | ADA/USD ⭐ | 0.148981 | 81.96 | +0.15% | 2.20x | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD ⭐ | 43.89 | 78.15 | +0.07% | 1.46x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD | 0.6735 | 77.71 | +0.18% | 4.92x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | TAO/USD | 184.3482 | 77.62 | +0.07% | 3.98x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD | 0.0568289 | 76.26 | +0.02% | 9.57x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD | 61.94 | 73.47 | +0.13% | 2.77x | STRONG 82/100 | HIGH 55/100 | Watch |
| 8 | XBT/USD ⭐ | 60959.8 | 73.28 | +0.14% | 2.07x | STRONG 92/100 | HIGH 55/100 | Watch |
| 9 | SYRUP/USD | 0.07188 | 64.08 | +0.46% | 0.58x | MODERATE 52/100 | EXTREME 87/100 | Do nothing |
| 10 | LINK/USD | 9.22058 | 61.92 | +0.20% | 0.63x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 3.0638 | 60.70 | +0.55% | 0.99x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 12 | PAXG/USD | 3580.82 | 58.49 | +0.25% | 1.03x | MODERATE 64/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95798 | 85.42 | +0.09% | 4.08x | 42225 | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | LTC/USD ⭐ | 43.91 | 78.65 | +0.07% | 1.46x | 14919 | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149024 | 78.14 | +0.15% | 2.20x | 11463 | STRONG 94/100 | HIGH 55/100 | Watch |
| 4 | TIA/USD | 0.3485 | 75.97 | +0.17% | 1.06x | 4197 | MODERATE 63/100 | HIGH 67/100 | Watch |
| 5 | XBT/USD ⭐ | 60974 | 68.71 | +0.14% | 2.07x | 229807 | STRONG 89/100 | HIGH 55/100 | Watch |
| 6 | PEPE/USD | 3.554e-06 | 68.02 | +0.51% | 1.47x | 7400 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, ADA/USD, LTC/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
