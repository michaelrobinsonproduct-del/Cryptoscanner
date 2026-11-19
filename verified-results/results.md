# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:00:32.910028+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44572251379
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** c82cd5b0b54a38096b1a1fec3a68ea2b33efaab3 (atomic ledger/results publication)
**Ledger generation:** 819 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021869 | 76.763 | 73.039 | +6.13% | +1.32% | 0.71x | 8.7 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 2 | BMT/USD | 0.02046 | 64.821 | 71.277 | +8.37% | +0.44% | 0.13x | 9.8 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | ADA/USD | 0.15196 | 63.034 | 55.669 | +0.47% | -0.65% | 2.06x | 5.2 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 22.336 | 60.111 | 71.560 | +3.07% | -0.84% | 0.27x | 9.8 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.58 | 58.421 | 60.846 | +1.05% | -0.41% | 0.96x | 3.0 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | SKR/USD | 0.010265 | 57.230 | 67.751 | +6.56% | -0.65% | 0.27x | 16.6 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 29/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | BILL/USD | 0.00433 | 55.010 | 64.288 | +9.62% | -1.81% | 0.98x | 23.1 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 23/100 | EXTREME 96/100 | Do nothing | WATCH |
| 8 | PYTH/USD | 0.05564 | 52.746 | 60.434 | +5.46% | -0.86% | 0.66x | 19.8 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 26/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | TAO/USD | 192.5719 | 48.082 | 51.962 | +0.32% | -0.31% | 0.77x | 10.5 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 10 | INJ/USD | 7.068 | 44.700 | 49.106 | +1.25% | -0.97% | 1.04x | 5.7 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | SHIB/USD | 3.812e-06 | 43.034 | 31.724 | +0.47% | -0.47% | 2.37x | 7.9 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | MODERATE 52/100 | HIGH 66/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.785e-06 | 39.362 | 46.572 | +1.04% | -0.58% | 0.57x | 2.6 | 2026-11-19T17:00:25.774815+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.039 | 0.021869 | +1.32% | 0.71x |
| 2 | VVV/USD | 71.560 | 22.336 | -0.84% | 0.27x |
| 3 | BMT/USD | 71.277 | 0.02046 | +0.44% | 0.13x |
| 4 | SKR/USD | 67.751 | 0.010265 | -0.65% | 0.27x |
| 5 | BILL/USD | 64.288 | 0.00433 | -1.81% | 0.98x |
| 6 | HYPE/USD | 60.846 | 67.58 | -0.41% | 0.96x |
| 7 | PYTH/USD | 60.434 | 0.05564 | -0.86% | 0.66x |
| 8 | ADA/USD | 55.669 | 0.15196 | -0.65% | 2.06x |
| 9 | TAO/USD | 51.962 | 192.5719 | -0.31% | 0.77x |
| 10 | INJ/USD | 49.106 | 7.068 | -0.97% | 1.04x |
| 11 | PEPE/USD | 46.572 | 3.785e-06 | -0.58% | 0.57x |
| 12 | SHIB/USD | 31.724 | 3.812e-06 | -0.47% | 2.37x |

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

- Persisted scans: 819; predictions: 6972; observations: 495173.
- Matured sampled outcomes across 1/6/24/48h: 6947; gap abstentions: 15408. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44572251379 · **Generation:** 819 · **Legacy run:** 44572251379
**Main quote time:** 2026-11-19T17:00:32.910028+00:00 · **Legacy report time:** 2026-11-19T17:01:23.200605+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021869 | 76.76 | +1.32% | 0.71x | MODERATE 68/100 | VERY_HIGH 75/100 | Watch |
| 2 | BMT/USD | 0.02046 | 64.82 | +0.44% | 0.13x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 3 | ADA/USD | 0.15196 | 63.03 | -0.65% | 2.06x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 22.336 | 60.11 | -0.84% | 0.27x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 5 | HYPE/USD | 67.58 | 58.42 | -0.41% | 0.96x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 6 | SKR/USD | 0.010265 | 57.23 | -0.65% | 0.27x | WEAK 29/100 | EXTREME 94/100 | Do nothing |
| 7 | BILL/USD | 0.00433 | 55.01 | -1.81% | 0.98x | WEAK 23/100 | EXTREME 96/100 | Do nothing |
| 8 | PYTH/USD | 0.05564 | 52.75 | -0.86% | 0.66x | WEAK 26/100 | EXTREME 87/100 | Do nothing |
| 9 | TAO/USD | 192.5719 | 48.08 | -0.31% | 0.77x | WEAK 24/100 | VERY_HIGH 74/100 | Do nothing |
| 10 | INJ/USD | 7.068 | 44.70 | -0.97% | 1.04x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 11 | SHIB/USD | 3.812e-06 | 43.03 | -0.47% | 2.37x | MODERATE 52/100 | HIGH 66/100 | Watch |
| 12 | PEPE/USD | 3.785e-06 | 39.36 | -0.58% | 0.57x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.05532 | 70.86 | +1.10% | 1.44x | 2048 | STRONG 70/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
