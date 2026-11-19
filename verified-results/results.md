# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:30:31.175403+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44566691215
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 957c078f8795d5730408b2e499c717279a17e673 (atomic ledger/results publication)
**Ledger generation:** 813 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKR/USD | 0.010332 | 80.725 | 71.219 | +7.26% | -0.06% | 1.98x | 9.7 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 22.593 | 78.428 | 81.909 | +4.25% | +0.35% | 0.48x | 5.7 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | BILL/USD | 0.00438 | 69.295 | 64.405 | +10.89% | +0.92% | 1.03x | 22.8 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | PYTH/USD | 0.05616 | 67.520 | 70.977 | +6.44% | -0.37% | 0.84x | 12.4 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | BMT/USD | 0.02026 | 65.689 | 73.704 | +7.31% | +0.00% | 0.20x | 4.9 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | TRUST/USD | 0.05414 | 64.031 | 73.415 | +10.04% | -1.06% | 0.59x | 5.5 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | WEAK 37/100 | EXTREME 92/100 | Do nothing | WATCH |
| 7 | HYPE/USD | 67.83 | 59.935 | 64.206 | +1.42% | +0.15% | 0.50x | 1.5 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SENT/USD | 0.021602 | 58.630 | 65.216 | +4.84% | +0.24% | 0.22x | 6.0 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | ADA/USD | 0.152788 | 55.341 | 60.529 | +1.01% | +0.21% | 0.38x | 3.1 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.10096 | 54.456 | 65.869 | +5.65% | -0.54% | 0.13x | 21.8 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | WEAK 22/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.9735 | 52.946 | 59.805 | +0.74% | -0.02% | 0.32x | 0.7 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TAO/USD | 193.2902 | 51.435 | 56.535 | +0.69% | +0.07% | 0.46x | 6.6 | 2026-11-19T16:30:21.994146+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.909 | 22.593 | +0.35% | 0.48x |
| 2 | BMT/USD | 73.704 | 0.02026 | +0.00% | 0.20x |
| 3 | TRUST/USD | 73.415 | 0.05414 | -1.06% | 0.59x |
| 4 | SKR/USD | 71.219 | 0.010332 | -0.06% | 1.98x |
| 5 | PYTH/USD | 70.977 | 0.05616 | -0.37% | 0.84x |
| 6 | USELESS/USD | 65.869 | 0.10096 | -0.54% | 0.13x |
| 7 | SENT/USD | 65.216 | 0.021602 | +0.24% | 0.22x |
| 8 | BILL/USD | 64.405 | 0.00438 | +0.92% | 1.03x |
| 9 | HYPE/USD | 64.206 | 67.83 | +0.15% | 0.50x |
| 10 | ADA/USD | 60.529 | 0.152788 | +0.21% | 0.38x |
| 11 | XRP/USD | 59.805 | 0.9735 | -0.02% | 0.32x |
| 12 | TAO/USD | 56.535 | 193.2902 | +0.07% | 0.46x |

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

- Persisted scans: 813; predictions: 6900; observations: 491587.
- Matured sampled outcomes across 1/6/24/48h: 6887; gap abstentions: 15351. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44566691215 · **Generation:** 813 · **Legacy run:** 44566691215
**Main quote time:** 2026-11-19T16:30:31.175403+00:00 · **Legacy report time:** 2026-11-19T16:31:16.654909+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKR/USD | 0.010332 | 80.72 | -0.06% | 1.98x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD | 22.593 | 78.43 | +0.35% | 0.48x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 3 | BILL/USD | 0.00438 | 69.29 | +0.92% | 1.03x | MODERATE 60/100 | EXTREME 86/100 | Do nothing |
| 4 | PYTH/USD | 0.05616 | 67.52 | -0.37% | 0.84x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | BMT/USD | 0.02026 | 65.69 | +0.00% | 0.20x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |
| 6 | TRUST/USD | 0.05414 | 64.03 | -1.06% | 0.59x | WEAK 37/100 | EXTREME 92/100 | Do nothing |
| 7 | HYPE/USD | 67.83 | 59.94 | +0.15% | 0.50x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | SENT/USD | 0.021602 | 58.63 | +0.24% | 0.22x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 9 | ADA/USD | 0.152788 | 55.34 | +0.21% | 0.38x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 10 | USELESS/USD | 0.10096 | 54.46 | -0.54% | 0.13x | WEAK 22/100 | EXTREME 88/100 | Do nothing |
| 11 | XRP/USD | 0.9735 | 52.95 | -0.02% | 0.32x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TAO/USD | 193.2902 | 51.43 | +0.07% | 0.46x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002671 | 66.44 | +0.41% | 1.28x | 4138 | MODERATE 63/100 | HIGH 61/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
