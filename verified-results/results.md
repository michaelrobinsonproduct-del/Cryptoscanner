# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:20:25.880311+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44586589485
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** da3046a2feb1b61ada17a835e9ac63037c2a8c20 (atomic ledger/results publication)
**Ledger generation:** 833 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 69.49 | 83.845 | 81.598 | +3.90% | -0.07% | 1.26x | 1.4 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.00269 | 76.832 | 63.869 | +3.62% | -0.41% | 2.75x | 7.4 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.97115 | 70.984 | 58.411 | +0.49% | +0.06% | 2.23x | 0.1 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.153292 | 65.824 | 63.356 | +1.35% | +0.12% | 1.19x | 2.2 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 5 | VVV/USD | 22.458 | 64.535 | 75.743 | +3.63% | -0.78% | 0.27x | 9.4 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 74.06 | 64.266 | 59.275 | +0.71% | +0.05% | 1.47x | 1.3 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010203 | 61.642 | 61.265 | +5.92% | -0.05% | 1.06x | 22.5 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | WEAK 31/100 | EXTREME 92/100 | Do nothing | WATCH |
| 8 | TAO/USD | 195.1097 | 60.857 | 61.105 | +1.64% | -0.02% | 0.99x | 8.6 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | CT/USD | 0.1276 | 60.762 | 65.051 | +7.95% | +0.08% | 0.53x | 23.5 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | WEAK 40/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | CSPR/USD | 0.0017974 | 59.186 | 65.177 | +10.06% | -0.90% | 0.85x | 22.8 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | WEAK 25/100 | EXTREME 92/100 | Do nothing | WATCH |
| 11 | INJ/USD | 7.138 | 59.149 | 56.956 | +2.25% | +0.18% | 1.13x | 4.2 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 12 | AKT/USD | 0.5501 | 56.094 | 69.990 | +6.20% | -0.99% | 0.11x | 10.9 | 2026-11-19T18:20:19.345788+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 81.598 | 69.49 | -0.07% | 1.26x |
| 2 | VVV/USD | 75.743 | 22.458 | -0.78% | 0.27x |
| 3 | AKT/USD | 69.990 | 0.5501 | -0.99% | 0.11x |
| 4 | CSPR/USD | 65.177 | 0.0017974 | -0.90% | 0.85x |
| 5 | CT/USD | 65.051 | 0.1276 | +0.08% | 0.53x |
| 6 | PUMP/USD | 63.869 | 0.00269 | -0.41% | 2.75x |
| 7 | ADA/USD | 63.356 | 0.153292 | +0.12% | 1.19x |
| 8 | SKR/USD | 61.265 | 0.010203 | -0.05% | 1.06x |
| 9 | TAO/USD | 61.105 | 195.1097 | -0.02% | 0.99x |
| 10 | SOL/USD | 59.275 | 74.06 | +0.05% | 1.47x |
| 11 | XRP/USD | 58.411 | 0.97115 | +0.06% | 2.23x |
| 12 | INJ/USD | 56.956 | 7.138 | +0.18% | 1.13x |

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

- Persisted scans: 833; predictions: 7140; observations: 503545.
- Matured sampled outcomes across 1/6/24/48h: 7115; gap abstentions: 15506. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44586589485 · **Generation:** 833 · **Legacy run:** 44586589485
**Main quote time:** 2026-11-19T18:20:25.880311+00:00 · **Legacy report time:** 2026-11-19T18:21:04.042348+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 69.49 | 83.85 | -0.07% | 1.26x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 2 | PUMP/USD | 0.00269 | 76.83 | -0.41% | 2.75x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.97115 | 70.98 | +0.06% | 2.23x | STRONG 80/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD | 0.153292 | 65.82 | +0.12% | 1.19x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 5 | VVV/USD | 22.458 | 64.53 | -0.78% | 0.27x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 74.06 | 64.27 | +0.05% | 1.47x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 7 | SKR/USD | 0.010203 | 61.64 | -0.05% | 1.06x | WEAK 31/100 | EXTREME 92/100 | Do nothing |
| 8 | TAO/USD | 195.1097 | 60.86 | -0.02% | 0.99x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | CT/USD | 0.1276 | 60.76 | +0.08% | 0.53x | WEAK 40/100 | EXTREME 87/100 | Do nothing |
| 10 | CSPR/USD | 0.0017974 | 59.19 | -0.90% | 0.85x | WEAK 25/100 | EXTREME 92/100 | Do nothing |
| 11 | INJ/USD ⭐ | 7.138 | 59.15 | +0.18% | 1.13x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 12 | AKT/USD | 0.5501 | 56.09 | -0.99% | 0.11x | WEAK 28/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.02122 | 71.41 | +0.77% | 1.55x | 14718 | STRONG 81/100 | HIGH 60/100 | Consider small entry |
| 2 | SYRUP/USD | 0.09963 | 71.05 | +0.24% | 2.66x | 1776 | STRONG 86/100 | VERY_HIGH 73/100 | Watch |
| 3 | INJ/USD ⭐ | 7.156 | 64.98 | +0.18% | 1.13x | 6914 | MODERATE 67/100 | HIGH 62/100 | Watch |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
