# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T12:22:23.985030+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45173218659
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b02d31465385133c9e3864ad650819aa65f4a129 (atomic ledger/results publication)
**Ledger generation:** 1429 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.37 | 93.791 | 87.862 | +8.32% | +0.88% | 1.15x | 11.0 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | STRONG 77/100 | HIGH 68/100 | Watch | WATCH |
| 2 | UAI/USD | 0.03146 | 88.970 | 70.765 | +6.39% | +0.64% | 18.46x | 9.5 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | STRONG 99/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | SUI/USD | 0.6709 | 85.854 | 70.481 | +2.32% | +0.07% | 8.88x | 1.5 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ALGO/USD | 0.08325 | 85.446 | 77.015 | +10.37% | +0.10% | 1.79x | 7.2 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 5 | BLUR/USD | 0.00793 | 69.040 | 69.640 | +7.31% | +0.00% | 0.94x | 12.6 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93855 | 67.741 | 62.936 | +1.19% | +0.02% | 1.47x | 0.7 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 7 | CC/USD | 0.07629 | 66.389 | 62.408 | +4.12% | +0.14% | 1.33x | 2.6 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 8 | SOL/USD | 72.28 | 65.828 | 70.661 | +2.34% | -0.19% | 0.61x | 1.4 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XLM/USD | 0.128483 | 65.700 | 58.421 | +0.75% | -0.09% | 1.77x | 1.4 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ADA/USD | 0.145331 | 65.326 | 51.036 | +0.50% | -0.14% | 3.40x | 3.7 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 11 | PAXG/USD | 3603.05 | 64.994 | 50.715 | +0.86% | -0.14% | 4.83x | 0.0 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 12 | NEAR/USD | 2.9897 | 64.967 | 54.538 | +0.27% | -0.41% | 2.25x | 4.7 | 2026-11-23T12:22:16.062011+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 87.862 | 155.37 | +0.88% | 1.15x |
| 2 | ALGO/USD | 77.015 | 0.08325 | +0.10% | 1.79x |
| 3 | UAI/USD | 70.765 | 0.03146 | +0.64% | 18.46x |
| 4 | SOL/USD | 70.661 | 72.28 | -0.19% | 0.61x |
| 5 | SUI/USD | 70.481 | 0.6709 | +0.07% | 8.88x |
| 6 | BLUR/USD | 69.640 | 0.00793 | +0.00% | 0.94x |
| 7 | XRP/USD | 62.936 | 0.93855 | +0.02% | 1.47x |
| 8 | CC/USD | 62.408 | 0.07629 | +0.14% | 1.33x |
| 9 | XLM/USD | 58.421 | 0.128483 | -0.09% | 1.77x |
| 10 | NEAR/USD | 54.538 | 2.9897 | -0.41% | 2.25x |
| 11 | ADA/USD | 51.036 | 0.145331 | -0.14% | 3.40x |
| 12 | PAXG/USD | 50.715 | 3603.05 | -0.14% | 4.83x |

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

- Persisted scans: 1429; predictions: 11915; observations: 865364.
- Matured sampled outcomes across 1/6/24/48h: 19885; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45173218659 · **Generation:** 1429 · **Legacy run:** 45173218659
**Main quote time:** 2026-11-23T12:22:23.985030+00:00 · **Legacy report time:** 2026-11-23T12:23:32.915197+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.37 | 93.79 | +0.88% | 1.15x | STRONG 87/100 | HIGH 68/100 | Watch |
| 2 | UAI/USD ⭐ | 0.03146 | 88.97 | +0.64% | 18.46x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6709 | 85.85 | +0.07% | 8.88x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | ALGO/USD ⭐ | 0.08325 | 85.45 | +0.10% | 1.79x | STRONG 88/100 | HIGH 60/100 | Watch |
| 5 | BLUR/USD | 0.00793 | 69.04 | +0.00% | 0.94x | MODERATE 50/100 | VERY_HIGH 80/100 | Watch |
| 6 | XRP/USD | 0.93855 | 67.74 | +0.02% | 1.47x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 7 | CC/USD ⭐ | 0.07629 | 66.39 | +0.14% | 1.33x | STRONG 78/100 | HIGH 60/100 | Watch |
| 8 | SOL/USD | 72.28 | 65.83 | -0.19% | 0.61x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 9 | XLM/USD | 0.128483 | 65.70 | -0.09% | 1.77x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | ADA/USD | 0.145331 | 65.33 | -0.14% | 3.40x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 11 | PAXG/USD | 3603.05 | 64.99 | -0.14% | 4.83x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 12 | NEAR/USD | 2.9897 | 64.97 | -0.41% | 2.25x | MODERATE 62/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.54 | 84.27 | +0.88% | 1.15x | 5912 | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | SUI/USD ⭐ | 0.6708 | 81.89 | +0.07% | 8.88x | 5636 | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | CC/USD ⭐ | 0.07629 | 81.79 | +0.14% | 1.33x | 3975 | STRONG 86/100 | HIGH 60/100 | Watch |
| 4 | ALGO/USD ⭐ | 0.08302 | 77.39 | +0.10% | 1.79x | 4011 | STRONG 84/100 | HIGH 60/100 | Watch |
| 5 | UAI/USD ⭐ | 0.03161 | 74.01 | +0.64% | 18.46x | 1872 | STRONG 97/100 | VERY_HIGH 73/100 | Watch |
| 6 | ONDO/USD | 0.29247 | 71.09 | +0.19% | 6.49x | 3948 | STRONG 76/100 | HIGH 66/100 | Watch |

**Same-run overlap:** QNT/USD, UAI/USD, SUI/USD, ALGO/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
