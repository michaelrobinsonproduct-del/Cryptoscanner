# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:45:34.504793+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44611752570
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 2ef9fc0554cca15fa4143568cadfbb0ed2693826 (atomic ledger/results publication)
**Ledger generation:** 857 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WINGS/USD | 0.00196 | 74.808 | 47.908 | +3.05% | +2.51% | 2.43x | 10.2 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | STRONG 87/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | TAO/USD | 192.803 | 68.952 | 51.561 | +0.44% | +0.48% | 4.97x | 7.9 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021092 | 67.476 | 46.828 | +2.36% | +1.14% | 2.49x | 8.1 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | STRONG 89/100 | HIGH 60/100 | Watch | WATCH |
| 4 | INJ/USD | 7.041 | 65.635 | 48.710 | +0.86% | +0.38% | 2.78x | 4.3 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 22.227 | 61.755 | 68.236 | +2.57% | +0.16% | 0.27x | 9.4 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.09854 | 58.773 | 57.354 | +3.12% | +0.87% | 0.71x | 5.1 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5487 | 57.508 | 66.450 | +5.93% | -0.09% | 0.15x | 14.6 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | WEAK 29/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | SKR/USD | 0.010123 | 56.906 | 57.852 | +5.09% | +0.35% | 0.73x | 17.8 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | ADA/USD | 0.151956 | 52.294 | 56.076 | +0.46% | +0.39% | 0.43x | 4.3 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PUMP/USD | 0.002637 | 42.428 | 48.348 | +1.58% | +0.27% | 0.28x | 11.4 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ALEO/USD | 0.03018 | 41.963 | 38.060 | +0.67% | +0.66% | 1.06x | 6.6 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PYTH/USD | 0.05331 | 37.587 | 32.262 | +1.04% | +0.24% | 1.41x | 15.0 | 2026-11-19T20:45:25.531212+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 68.236 | 22.227 | +0.16% | 0.27x |
| 2 | AKT/USD | 66.450 | 0.5487 | -0.09% | 0.15x |
| 3 | SKR/USD | 57.852 | 0.010123 | +0.35% | 0.73x |
| 4 | USELESS/USD | 57.354 | 0.09854 | +0.87% | 0.71x |
| 5 | ADA/USD | 56.076 | 0.151956 | +0.39% | 0.43x |
| 6 | TAO/USD | 51.561 | 192.803 | +0.48% | 4.97x |
| 7 | INJ/USD | 48.710 | 7.041 | +0.38% | 2.78x |
| 8 | PUMP/USD | 48.348 | 0.002637 | +0.27% | 0.28x |
| 9 | WINGS/USD | 47.908 | 0.00196 | +2.51% | 2.43x |
| 10 | SENT/USD | 46.828 | 0.021092 | +1.14% | 2.49x |
| 11 | ALEO/USD | 38.060 | 0.03018 | +0.66% | 1.06x |
| 12 | PYTH/USD | 32.262 | 0.05331 | +0.24% | 1.41x |

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

- Persisted scans: 857; predictions: 7423; observations: 517924.
- Matured sampled outcomes across 1/6/24/48h: 7559; gap abstentions: 15659. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44611752570 · **Generation:** 857 · **Legacy run:** 44611752570
**Main quote time:** 2026-11-19T20:45:34.504793+00:00 · **Legacy report time:** 2026-11-19T20:46:39.043351+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.00196 | 74.81 | +2.51% | 2.43x | STRONG 97/100 | VERY_HIGH 73/100 | Watch |
| 2 | TAO/USD | 192.803 | 68.95 | +0.48% | 4.97x | STRONG 89/100 | HIGH 55/100 | Watch |
| 3 | SENT/USD ⭐ | 0.021092 | 67.48 | +1.14% | 2.49x | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 4 | INJ/USD | 7.041 | 65.63 | +0.38% | 2.78x | STRONG 88/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD | 22.227 | 61.75 | +0.16% | 0.27x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 6 | USELESS/USD | 0.09854 | 58.77 | +0.87% | 0.71x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | AKT/USD | 0.5487 | 57.51 | -0.09% | 0.15x | WEAK 29/100 | EXTREME 87/100 | Do nothing |
| 8 | SKR/USD | 0.010123 | 56.91 | +0.35% | 0.73x | MODERATE 53/100 | EXTREME 88/100 | Do nothing |
| 9 | ADA/USD | 0.151956 | 52.29 | +0.39% | 0.43x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 10 | PUMP/USD | 0.002637 | 42.43 | +0.27% | 0.28x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 11 | ALEO/USD ⭐ | 0.03018 | 41.96 | +0.66% | 1.06x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 12 | PYTH/USD | 0.05331 | 37.59 | +0.24% | 1.41x | MODERATE 59/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.00196 | 72.85 | +2.51% | 2.43x | 5820 | STRONG 96/100 | VERY_HIGH 73/100 | Watch |
| 2 | ALEO/USD ⭐ | 0.03095 | 67.23 | +0.66% | 1.06x | 9271 | MODERATE 69/100 | VERY_HIGH 74/100 | Watch |
| 3 | SENT/USD ⭐ | 0.02107 | 61.07 | +1.14% | 2.49x | 14740 | STRONG 96/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** WINGS/USD, SENT/USD, ALEO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
