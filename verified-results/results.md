# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:20:34.406248+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44636673197
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 009e755d76186efad12e329aa5eb4033a0582fc2 (atomic ledger/results publication)
**Ledger generation:** 878 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021384 | 72.274 | 56.853 | +3.78% | +0.08% | 2.54x | 8.0 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05959 | 62.852 | 71.901 | +6.41% | -0.43% | 0.31x | 10.1 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | USELESS/USD | 0.09925 | 57.727 | 59.402 | +3.86% | +0.31% | 0.68x | 16.2 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | INJ/USD | 7.094 | 52.983 | 54.755 | +1.62% | +0.00% | 0.82x | 4.2 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 5 | VVV/USD | 21.887 | 51.950 | 58.546 | +1.00% | +0.39% | 0.15x | 6.9 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AKT/USD | 0.529 | 50.493 | 38.760 | +2.12% | -0.65% | 16.03x | 17.0 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ADA/USD | 0.151827 | 49.957 | 56.003 | +0.38% | +0.40% | 0.20x | 3.3 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CAP/USD | 0.097146 | 41.791 | 39.833 | +1.18% | +0.71% | 0.84x | 6.1 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 9 | CSPR/USD | 0.0016755 | 40.126 | 46.774 | +2.60% | -0.05% | 0.36x | 6.6 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | LIGHTER/USD | 2.77 | 38.945 | 42.100 | +2.06% | -0.86% | 1.11x | 14.5 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | PYTH/USD | 0.0531 | 36.719 | 33.977 | +0.64% | +0.28% | 1.13x | 7.5 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 12 | BABY/USD | 0.00844 | 31.169 | 33.263 | +1.20% | +0.72% | 0.43x | 11.9 | 2026-11-19T23:20:27.741124+00:00 | Not calibrated | WEAK 41/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 71.901 | 0.05959 | -0.43% | 0.31x |
| 2 | USELESS/USD | 59.402 | 0.09925 | +0.31% | 0.68x |
| 3 | VVV/USD | 58.546 | 21.887 | +0.39% | 0.15x |
| 4 | SENT/USD | 56.853 | 0.021384 | +0.08% | 2.54x |
| 5 | ADA/USD | 56.003 | 0.151827 | +0.40% | 0.20x |
| 6 | INJ/USD | 54.755 | 7.094 | +0.00% | 0.82x |
| 7 | CSPR/USD | 46.774 | 0.0016755 | -0.05% | 0.36x |
| 8 | LIGHTER/USD | 42.100 | 2.77 | -0.86% | 1.11x |
| 9 | CAP/USD | 39.833 | 0.097146 | +0.71% | 0.84x |
| 10 | AKT/USD | 38.760 | 0.529 | -0.65% | 16.03x |
| 11 | PYTH/USD | 33.977 | 0.0531 | +0.28% | 1.13x |
| 12 | BABY/USD | 33.263 | 0.00844 | +0.72% | 0.43x |

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

- Persisted scans: 878; predictions: 7647; observations: 530559.
- Matured sampled outcomes across 1/6/24/48h: 8151; gap abstentions: 15829. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44636673197 · **Generation:** 878 · **Legacy run:** 44636673197
**Main quote time:** 2026-11-19T23:20:34.406248+00:00 · **Legacy report time:** 2026-11-19T23:21:25.752495+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021384 | 72.27 | +0.08% | 2.54x | STRONG 91/100 | HIGH 60/100 | Watch |
| 2 | MEGA/USD | 0.05959 | 62.85 | -0.43% | 0.31x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 3 | USELESS/USD | 0.09925 | 57.73 | +0.31% | 0.68x | MODERATE 54/100 | VERY_HIGH 76/100 | Watch |
| 4 | INJ/USD | 7.094 | 52.98 | +0.00% | 0.82x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 5 | VVV/USD | 21.887 | 51.95 | +0.39% | 0.15x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 6 | AKT/USD | 0.529 | 50.49 | -0.65% | 16.03x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 7 | ADA/USD | 0.151827 | 49.96 | +0.40% | 0.20x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 8 | CAP/USD | 0.097146 | 41.79 | +0.71% | 0.84x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 9 | CSPR/USD | 0.0016755 | 40.13 | -0.05% | 0.36x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | LIGHTER/USD | 2.77 | 38.95 | -0.86% | 1.11x | WEAK 24/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | PYTH/USD | 0.0531 | 36.72 | +0.28% | 1.13x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 12 | BABY/USD | 0.00844 | 31.17 | +0.72% | 0.43x | WEAK 41/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021338 | 73.73 | +0.08% | 2.54x | 14752 | STRONG 92/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
