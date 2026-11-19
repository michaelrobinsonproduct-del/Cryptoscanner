# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:35:27.258853+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44599744836
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 89a233fd928dee00b471fefac8dab3ff4d471aae (atomic ledger/results publication)
**Ledger generation:** 845 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1301 | 76.942 | 65.330 | +10.07% | +2.20% | 1.06x | 23.2 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | VVV/USD | 22.542 | 75.940 | 78.253 | +4.02% | +0.30% | 0.62x | 9.8 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SKR/USD | 0.010167 | 74.825 | 62.095 | +5.54% | -0.16% | 2.35x | 15.7 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5507 | 73.522 | 69.932 | +6.31% | +0.40% | 1.16x | 12.7 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.75 | 58.056 | 63.368 | +1.30% | +0.13% | 0.40x | 1.5 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ADA/USD | 0.153136 | 56.715 | 61.553 | +1.24% | +0.32% | 0.35x | 4.3 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ONDO/USD | 0.29942 | 54.775 | 38.671 | +0.59% | +0.22% | 12.42x | 3.0 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 8 | SHIB/USD | 3.83e-06 | 54.257 | 36.896 | +0.95% | +0.47% | 5.63x | 5.2 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 9 | MEGA/USD | 0.059 | 51.901 | 58.633 | +5.36% | +0.29% | 0.18x | 22.0 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | SENT/USD | 0.021418 | 51.236 | 57.957 | +3.95% | +0.00% | 0.33x | 7.9 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | PEPE/USD | 3.76e-06 | 50.435 | 42.417 | +0.37% | +0.80% | 1.40x | 2.7 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BNB/USD | 584.95 | 48.049 | 44.759 | +0.63% | -0.00% | 1.33x | 1.5 | 2026-11-19T19:35:18.481711+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 78.253 | 22.542 | +0.30% | 0.62x |
| 2 | AKT/USD | 69.932 | 0.5507 | +0.40% | 1.16x |
| 3 | CT/USD | 65.330 | 0.1301 | +2.20% | 1.06x |
| 4 | HYPE/USD | 63.368 | 67.75 | +0.13% | 0.40x |
| 5 | SKR/USD | 62.095 | 0.010167 | -0.16% | 2.35x |
| 6 | ADA/USD | 61.553 | 0.153136 | +0.32% | 0.35x |
| 7 | MEGA/USD | 58.633 | 0.059 | +0.29% | 0.18x |
| 8 | SENT/USD | 57.957 | 0.021418 | +0.00% | 0.33x |
| 9 | BNB/USD | 44.759 | 584.95 | -0.00% | 1.33x |
| 10 | PEPE/USD | 42.417 | 3.76e-06 | +0.80% | 1.40x |
| 11 | ONDO/USD | 38.671 | 0.29942 | +0.22% | 12.42x |
| 12 | SHIB/USD | 36.896 | 3.83e-06 | +0.47% | 5.63x |

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

- Persisted scans: 845; predictions: 7284; observations: 510732.
- Matured sampled outcomes across 1/6/24/48h: 7295; gap abstentions: 15604. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44599744836 · **Generation:** 845 · **Legacy run:** 44599744836
**Main quote time:** 2026-11-19T19:35:27.258853+00:00 · **Legacy report time:** 2026-11-19T19:36:17.047401+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1301 | 76.94 | +2.20% | 1.06x | STRONG 73/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD | 22.542 | 75.94 | +0.30% | 0.62x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 3 | SKR/USD | 0.010167 | 74.83 | -0.16% | 2.35x | MODERATE 62/100 | VERY_HIGH 79/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5507 | 73.52 | +0.40% | 1.16x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 5 | HYPE/USD | 67.75 | 58.06 | +0.13% | 0.40x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 6 | ADA/USD | 0.153136 | 56.72 | +0.32% | 0.35x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | ONDO/USD | 0.29942 | 54.78 | +0.22% | 12.42x | STRONG 82/100 | HIGH 60/100 | Watch |
| 8 | SHIB/USD | 3.83e-06 | 54.26 | +0.47% | 5.63x | STRONG 82/100 | HIGH 60/100 | Watch |
| 9 | MEGA/USD | 0.059 | 51.90 | +0.29% | 0.18x | MODERATE 46/100 | EXTREME 87/100 | Do nothing |
| 10 | SENT/USD | 0.021418 | 51.24 | +0.00% | 0.33x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |
| 11 | PEPE/USD | 3.76e-06 | 50.43 | +0.80% | 1.40x | STRONG 70/100 | HIGH 55/100 | Watch |
| 12 | BNB/USD | 584.95 | 48.05 | -0.00% | 1.33x | WEAK 44/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.09926 | 75.73 | +0.91% | 1.04x | 3151 | MODERATE 68/100 | HIGH 68/100 | Watch |
| 2 | CT/USD ⭐ | 0.1296 | 74.87 | +2.20% | 1.06x | 2266 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5504 | 73.09 | +0.40% | 1.16x | 3350 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** CT/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
