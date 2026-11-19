# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:40:32.745697+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44630683051
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b2d2dd9d85c24f5971a1245d8834e22b71960202 (atomic ledger/results publication)
**Ledger generation:** 872 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.0602 | 87.508 | 70.591 | +7.50% | +0.38% | 2.78x | 13.3 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | STRONG 94/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | USELESS/USD | 0.10024 | 76.456 | 63.985 | +4.90% | +1.20% | 1.65x | 21.0 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 3 | ADA/USD | 0.151867 | 71.079 | 55.697 | +0.41% | +0.43% | 2.32x | 4.3 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 22.02 | 68.960 | 62.397 | +1.61% | +0.44% | 1.44x | 7.8 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5386 | 64.722 | 59.264 | +3.98% | +0.47% | 1.31x | 1.9 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010083 | 64.141 | 60.858 | +4.67% | +0.81% | 0.92x | 6.0 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | TRX/USD | 0.310471 | 60.658 | 44.898 | +0.38% | +0.15% | 4.20x | 0.0 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 8 | INJ/USD | 7.104 | 56.810 | 55.848 | +1.76% | +1.17% | 0.51x | 4.2 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SENT/USD | 0.021538 | 56.791 | 62.189 | +4.53% | +0.62% | 0.15x | 7.9 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | HYPE/USD | 67.07 | 52.200 | 55.497 | +0.28% | +0.34% | 0.50x | 3.0 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PYTH/USD | 0.05317 | 31.850 | 33.986 | +0.78% | +0.64% | 0.46x | 9.4 | 2026-11-19T22:40:26.644236+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 70.591 | 0.0602 | +0.38% | 2.78x |
| 2 | USELESS/USD | 63.985 | 0.10024 | +1.20% | 1.65x |
| 3 | VVV/USD | 62.397 | 22.02 | +0.44% | 1.44x |
| 4 | SENT/USD | 62.189 | 0.021538 | +0.62% | 0.15x |
| 5 | SKR/USD | 60.858 | 0.010083 | +0.81% | 0.92x |
| 6 | AKT/USD | 59.264 | 0.5386 | +0.47% | 1.31x |
| 7 | INJ/USD | 55.848 | 7.104 | +1.17% | 0.51x |
| 8 | ADA/USD | 55.697 | 0.151867 | +0.43% | 2.32x |
| 9 | HYPE/USD | 55.497 | 67.07 | +0.34% | 0.50x |
| 10 | TRX/USD | 44.898 | 0.310471 | +0.15% | 4.20x |
| 11 | PYTH/USD | 33.986 | 0.05317 | +0.64% | 0.46x |

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

- Persisted scans: 872; predictions: 7584; observations: 526946.
- Matured sampled outcomes across 1/6/24/48h: 8010; gap abstentions: 15754. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44630683051 · **Generation:** 872 · **Legacy run:** 44630683051
**Main quote time:** 2026-11-19T22:40:32.745697+00:00 · **Legacy report time:** 2026-11-19T22:41:19.250380+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.0602 | 87.51 | +0.38% | 2.78x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | USELESS/USD ⭐ | 0.10024 | 76.46 | +1.20% | 1.65x | STRONG 83/100 | HIGH 67/100 | Consider small entry |
| 3 | ADA/USD | 0.151867 | 71.08 | +0.43% | 2.32x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 22.02 | 68.96 | +0.44% | 1.44x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5386 | 64.72 | +0.47% | 1.31x | STRONG 87/100 | HIGH 60/100 | Watch |
| 6 | SKR/USD | 0.010083 | 64.14 | +0.81% | 0.92x | MODERATE 62/100 | VERY_HIGH 74/100 | Watch |
| 7 | TRX/USD | 0.310471 | 60.66 | +0.15% | 4.20x | STRONG 75/100 | HIGH 55/100 | Watch |
| 8 | INJ/USD | 7.104 | 56.81 | +1.17% | 0.51x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 9 | SENT/USD | 0.021538 | 56.79 | +0.62% | 0.15x | MODERATE 58/100 | VERY_HIGH 75/100 | Watch |
| 10 | HYPE/USD | 67.07 | 52.20 | +0.34% | 0.50x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 11 | PYTH/USD | 0.05317 | 31.85 | +0.64% | 0.46x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5387 | 85.30 | +0.47% | 1.31x | 3481 | STRONG 98/100 | HIGH 60/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.10026 | 82.31 | +1.20% | 1.65x | 5315 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 3 | MEGA/USD ⭐ | 0.0602 | 75.67 | +0.38% | 2.78x | 2170 | STRONG 98/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** MEGA/USD, USELESS/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
