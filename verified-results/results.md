# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:20:39.557113+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44607505409
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 17618844f655c756a1be9375dcd78ba32c39acc5 (atomic ledger/results publication)
**Ledger generation:** 854 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.331 | 85.618 | 73.401 | +3.05% | -0.56% | 27.09x | 5.8 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ALEO/USD | 0.03168 | 80.028 | 74.685 | +5.67% | +1.67% | 0.70x | 3.2 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | HYPE/USD | 67.24 | 71.612 | 57.280 | +0.54% | -0.13% | 4.61x | 3.0 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5546 | 70.831 | 73.657 | +7.07% | +0.54% | 0.45x | 7.2 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | ADA/USD | 0.152252 | 62.307 | 57.512 | +0.66% | +0.08% | 1.44x | 4.2 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 6 | TAO/USD | 193.9216 | 60.916 | 55.145 | +1.02% | -0.19% | 1.67x | 8.8 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010135 | 58.463 | 62.671 | +5.21% | +0.16% | 0.50x | 9.9 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | CSPR/USD | 0.0017764 | 53.185 | 70.978 | +8.77% | -2.58% | 0.51x | 11.8 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | WEAK 27/100 | EXTREME 91/100 | Do nothing | WATCH |
| 9 | PYTH/USD | 0.05349 | 53.011 | 37.452 | +1.38% | +0.11% | 4.50x | 9.4 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 10 | INJ/USD | 7.061 | 47.610 | 50.008 | +1.15% | -0.03% | 0.77x | 5.7 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | ICP/USD | 2.188 | 42.216 | 31.507 | +0.46% | +0.55% | 1.80x | 13.7 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 12 | SENT/USD | 0.02093 | 38.515 | 43.353 | +1.58% | -0.88% | 0.96x | 3.8 | 2026-11-19T20:20:30.441341+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ALEO/USD | 74.685 | 0.03168 | +1.67% | 0.70x |
| 2 | AKT/USD | 73.657 | 0.5546 | +0.54% | 0.45x |
| 3 | VVV/USD | 73.401 | 22.331 | -0.56% | 27.09x |
| 4 | CSPR/USD | 70.978 | 0.0017764 | -2.58% | 0.51x |
| 5 | SKR/USD | 62.671 | 0.010135 | +0.16% | 0.50x |
| 6 | ADA/USD | 57.512 | 0.152252 | +0.08% | 1.44x |
| 7 | HYPE/USD | 57.280 | 67.24 | -0.13% | 4.61x |
| 8 | TAO/USD | 55.145 | 193.9216 | -0.19% | 1.67x |
| 9 | INJ/USD | 50.008 | 7.061 | -0.03% | 0.77x |
| 10 | SENT/USD | 43.353 | 0.02093 | -0.88% | 0.96x |
| 11 | PYTH/USD | 37.452 | 0.05349 | +0.11% | 4.50x |
| 12 | ICP/USD | 31.507 | 2.188 | +0.55% | 1.80x |

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

- Persisted scans: 854; predictions: 7391; observations: 516123.
- Matured sampled outcomes across 1/6/24/48h: 7463; gap abstentions: 15644. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44607505409 · **Generation:** 854 · **Legacy run:** 44607505409
**Main quote time:** 2026-11-19T20:20:39.557113+00:00 · **Legacy report time:** 2026-11-19T20:21:40.893960+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.331 | 85.62 | -0.56% | 27.09x | STRONG 73/100 | HIGH 61/100 | Watch |
| 2 | ALEO/USD | 0.03168 | 80.03 | +1.67% | 0.70x | STRONG 70/100 | VERY_HIGH 75/100 | Watch |
| 3 | HYPE/USD | 67.24 | 71.61 | -0.13% | 4.61x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | AKT/USD | 0.5546 | 70.83 | +0.54% | 0.45x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 5 | ADA/USD | 0.152252 | 62.31 | +0.08% | 1.44x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 6 | TAO/USD | 193.9216 | 60.92 | -0.19% | 1.67x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 7 | SKR/USD | 0.010135 | 58.46 | +0.16% | 0.50x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 8 | CSPR/USD | 0.0017764 | 53.19 | -2.58% | 0.51x | WEAK 27/100 | EXTREME 91/100 | Do nothing |
| 9 | PYTH/USD | 0.05349 | 53.01 | +0.11% | 4.50x | STRONG 72/100 | HIGH 60/100 | Watch |
| 10 | INJ/USD | 7.061 | 47.61 | -0.03% | 0.77x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 11 | ICP/USD | 2.188 | 42.22 | +0.55% | 1.80x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 12 | SENT/USD | 0.02093 | 38.52 | -0.88% | 0.96x | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.09806 | 66.49 | +0.30% | 2.89x | 3358 | STRONG 83/100 | HIGH 61/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
