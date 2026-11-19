# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:45:24.966422+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44569510683
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 72804910c5db6205584c3e7c1673b33e5fba08a5 (atomic ledger/results publication)
**Ledger generation:** 816 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.05461 | 89.252 | 68.885 | +11.00% | +1.07% | 2.87x | 14.7 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 22.537 | 72.044 | 80.088 | +4.00% | -0.16% | 0.28x | 5.8 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ADA/USD | 0.152819 | 67.355 | 60.247 | +1.03% | +0.28% | 1.57x | 4.0 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5466 | 66.385 | 65.542 | +5.52% | +0.70% | 0.73x | 9.2 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010357 | 66.067 | 71.698 | +7.52% | +0.24% | 0.32x | 8.7 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97475 | 64.878 | 61.019 | +0.87% | +0.32% | 1.23x | 0.1 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SENT/USD | 0.021661 | 63.999 | 66.554 | +5.12% | +0.45% | 0.52x | 7.4 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | ALEO/USD | 0.03106 | 63.996 | 56.027 | +3.60% | +0.36% | 1.62x | 3.2 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 9 | PYTH/USD | 0.05612 | 63.834 | 71.417 | +6.37% | -0.07% | 0.28x | 10.7 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | BMT/USD | 0.02037 | 62.570 | 68.801 | +7.89% | +0.69% | 0.03x | 14.8 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | USELESS/USD | 0.1005 | 60.340 | 66.415 | +5.17% | +0.10% | 0.34x | 13.9 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | HYPE/USD | 67.87 | 59.608 | 63.888 | +1.48% | +0.22% | 0.46x | 2.9 | 2026-11-19T16:45:16.606208+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.088 | 22.537 | -0.16% | 0.28x |
| 2 | SKR/USD | 71.698 | 0.010357 | +0.24% | 0.32x |
| 3 | PYTH/USD | 71.417 | 0.05612 | -0.07% | 0.28x |
| 4 | TRUST/USD | 68.885 | 0.05461 | +1.07% | 2.87x |
| 5 | BMT/USD | 68.801 | 0.02037 | +0.69% | 0.03x |
| 6 | SENT/USD | 66.554 | 0.021661 | +0.45% | 0.52x |
| 7 | USELESS/USD | 66.415 | 0.1005 | +0.10% | 0.34x |
| 8 | AKT/USD | 65.542 | 0.5466 | +0.70% | 0.73x |
| 9 | HYPE/USD | 63.888 | 67.87 | +0.22% | 0.46x |
| 10 | XRP/USD | 61.019 | 0.97475 | +0.32% | 1.23x |
| 11 | ADA/USD | 60.247 | 0.152819 | +0.28% | 1.57x |
| 12 | ALEO/USD | 56.027 | 0.03106 | +0.36% | 1.62x |

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

- Persisted scans: 816; predictions: 6936; observations: 493379.
- Matured sampled outcomes across 1/6/24/48h: 6911; gap abstentions: 15379. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44569510683 · **Generation:** 816 · **Legacy run:** 44569510683
**Main quote time:** 2026-11-19T16:45:24.966422+00:00 · **Legacy report time:** 2026-11-19T16:46:04.435118+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.05461 | 89.25 | +1.07% | 2.87x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD | 22.537 | 72.04 | -0.16% | 0.28x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 3 | ADA/USD | 0.152819 | 67.36 | +0.28% | 1.57x | STRONG 79/100 | HIGH 55/100 | Watch |
| 4 | AKT/USD | 0.5466 | 66.38 | +0.70% | 0.73x | MODERATE 63/100 | VERY_HIGH 82/100 | Watch |
| 5 | SKR/USD | 0.010357 | 66.07 | +0.24% | 0.32x | MODERATE 63/100 | VERY_HIGH 82/100 | Watch |
| 6 | XRP/USD | 0.97475 | 64.88 | +0.32% | 1.23x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | SENT/USD | 0.021661 | 64.00 | +0.45% | 0.52x | MODERATE 62/100 | VERY_HIGH 75/100 | Watch |
| 8 | ALEO/USD | 0.03106 | 64.00 | +0.36% | 1.62x | STRONG 77/100 | HIGH 60/100 | Watch |
| 9 | PYTH/USD | 0.05612 | 63.83 | -0.07% | 0.28x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 10 | BMT/USD | 0.02037 | 62.57 | +0.69% | 0.03x | MODERATE 56/100 | EXTREME 88/100 | Do nothing |
| 11 | USELESS/USD | 0.1005 | 60.34 | +0.10% | 0.34x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 12 | HYPE/USD | 67.87 | 59.61 | +0.22% | 0.46x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.100036 | 87.75 | +3.26% | 2.77x | 7885 | STRONG 89/100 | VERY_HIGH 82/100 | Watch |
| 2 | TRUST/USD ⭐ | 0.05463 | 76.39 | +1.07% | 2.87x | 2035 | STRONG 93/100 | VERY_HIGH 79/100 | Watch |
| 3 | INJ/USD | 7.143 | 69.46 | +0.24% | 2.10x | 6789 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** TRUST/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
