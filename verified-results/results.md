# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:15:21.787943+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44563849929
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 1baf0a22ebfe8bd010bd8995e466a2bb3c7dac7e (atomic ledger/results publication)
**Ledger generation:** 810 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BMT/USD | 0.02023 | 85.974 | 68.740 | +7.15% | +0.45% | 4.54x | 14.9 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | STRONG 93/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | PYTH/USD | 0.05637 | 82.024 | 68.351 | +6.84% | -0.27% | 3.36x | 17.8 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.10221 | 75.262 | 72.059 | +7.63% | -0.64% | 1.64x | 8.8 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | VVV/USD | 22.514 | 73.475 | 78.892 | +3.89% | -0.10% | 0.51x | 6.7 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | TRUST/USD | 0.05463 | 66.355 | 67.929 | +11.04% | +1.09% | 0.30x | 16.5 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | HYPE/USD | 67.62 | 61.706 | 61.264 | +1.11% | -0.37% | 1.23x | 3.0 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5461 | 61.363 | 64.868 | +5.42% | -0.38% | 0.84x | 9.2 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97202 | 58.163 | 59.041 | +0.58% | +0.37% | 0.73x | 0.1 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.10094 | 56.258 | 64.269 | +5.63% | -0.20% | 0.30x | 24.8 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | SENT/USD | 0.021514 | 55.634 | 62.406 | +4.41% | +0.31% | 0.17x | 5.6 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | ADA/USD | 0.152313 | 50.742 | 57.930 | +0.70% | -0.04% | 0.30x | 3.9 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ZEC/USD | 920.2 | 49.395 | 58.995 | +0.90% | -0.16% | 0.12x | 4.7 | 2026-11-19T16:15:14.216009+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 78.892 | 22.514 | -0.10% | 0.51x |
| 2 | SYRUP/USD | 72.059 | 0.10221 | -0.64% | 1.64x |
| 3 | BMT/USD | 68.740 | 0.02023 | +0.45% | 4.54x |
| 4 | PYTH/USD | 68.351 | 0.05637 | -0.27% | 3.36x |
| 5 | TRUST/USD | 67.929 | 0.05463 | +1.09% | 0.30x |
| 6 | AKT/USD | 64.868 | 0.5461 | -0.38% | 0.84x |
| 7 | USELESS/USD | 64.269 | 0.10094 | -0.20% | 0.30x |
| 8 | SENT/USD | 62.406 | 0.021514 | +0.31% | 0.17x |
| 9 | HYPE/USD | 61.264 | 67.62 | -0.37% | 1.23x |
| 10 | XRP/USD | 59.041 | 0.97202 | +0.37% | 0.73x |
| 11 | ZEC/USD | 58.995 | 920.2 | -0.16% | 0.12x |
| 12 | ADA/USD | 57.930 | 0.152313 | -0.04% | 0.30x |

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

- Persisted scans: 810; predictions: 6864; observations: 489797.
- Matured sampled outcomes across 1/6/24/48h: 6863; gap abstentions: 15318. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44563849929 · **Generation:** 810 · **Legacy run:** 44563849929
**Main quote time:** 2026-11-19T16:15:21.787943+00:00 · **Legacy report time:** 2026-11-19T16:16:05.694505+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.02023 | 85.97 | +0.45% | 4.54x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | PYTH/USD | 0.05637 | 82.02 | -0.27% | 3.36x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 3 | SYRUP/USD | 0.10221 | 75.26 | -0.64% | 1.64x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |
| 4 | VVV/USD | 22.514 | 73.47 | -0.10% | 0.51x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 5 | TRUST/USD | 0.05463 | 66.36 | +1.09% | 0.30x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 6 | HYPE/USD | 67.62 | 61.71 | -0.37% | 1.23x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | AKT/USD | 0.5461 | 61.36 | -0.38% | 0.84x | WEAK 36/100 | VERY_HIGH 80/100 | Watch |
| 8 | XRP/USD | 0.97202 | 58.16 | +0.37% | 0.73x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 9 | USELESS/USD | 0.10094 | 56.26 | -0.20% | 0.30x | WEAK 23/100 | EXTREME 88/100 | Do nothing |
| 10 | SENT/USD | 0.021514 | 55.63 | +0.31% | 0.17x | MODERATE 58/100 | VERY_HIGH 75/100 | Watch |
| 11 | ADA/USD | 0.152313 | 50.74 | -0.04% | 0.30x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ZEC/USD | 920.2 | 49.40 | -0.16% | 0.12x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.02023 | 80.05 | +0.45% | 4.54x | 2949 | STRONG 95/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** BMT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
