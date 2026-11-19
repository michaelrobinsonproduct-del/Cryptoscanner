# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T17:05:04.176196+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44573127494
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 1e86d3382db75882ccc6444af790654b7a3042fb (atomic ledger/results publication)
**Ledger generation:** 820 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.05482 | 77.920 | 68.038 | +11.42% | +1.10% | 1.44x | 16.4 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021651 | 71.819 | 68.095 | +5.08% | +1.32% | 0.71x | 3.7 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | BMT/USD | 0.02037 | 62.358 | 68.814 | +7.89% | +0.44% | 0.13x | 14.7 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | VVV/USD | 22.138 | 54.582 | 66.031 | +2.15% | -0.84% | 0.27x | 8.1 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 67.18 | 54.227 | 56.651 | +0.45% | -0.41% | 0.96x | 3.0 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | PYTH/USD | 0.05556 | 53.480 | 61.169 | +5.31% | -0.86% | 0.66x | 16.2 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 27/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | CSPR/USD | 0.0017103 | 52.736 | 56.771 | +4.73% | -0.06% | 0.63x | 15.2 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 26/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | SKR/USD | 0.010136 | 49.699 | 60.220 | +5.22% | -0.65% | 0.27x | 14.8 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 25/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | ALEO/USD | 0.03107 | 49.301 | 54.937 | +3.64% | -0.55% | 0.71x | 6.4 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | PUMP/USD | 0.002635 | 44.985 | 48.984 | +1.50% | -1.50% | 1.35x | 7.6 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 42/100 | HIGH 65/100 | Do nothing | WATCH |
| 11 | CAP/USD | 0.098142 | 38.053 | 46.848 | +2.21% | -2.01% | 1.12x | 6.1 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 12 | PEPE/USD | 3.77e-06 | 35.869 | 42.505 | +0.64% | -1.26% | 0.96x | 5.3 | 2026-11-19T17:04:56.299718+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BMT/USD | 68.814 | 0.02037 | +0.44% | 0.13x |
| 2 | SENT/USD | 68.095 | 0.021651 | +1.32% | 0.71x |
| 3 | TRUST/USD | 68.038 | 0.05482 | +1.10% | 1.44x |
| 4 | VVV/USD | 66.031 | 22.138 | -0.84% | 0.27x |
| 5 | PYTH/USD | 61.169 | 0.05556 | -0.86% | 0.66x |
| 6 | SKR/USD | 60.220 | 0.010136 | -0.65% | 0.27x |
| 7 | CSPR/USD | 56.771 | 0.0017103 | -0.06% | 0.63x |
| 8 | HYPE/USD | 56.651 | 67.18 | -0.41% | 0.96x |
| 9 | ALEO/USD | 54.937 | 0.03107 | -0.55% | 0.71x |
| 10 | PUMP/USD | 48.984 | 0.002635 | -1.50% | 1.35x |
| 11 | CAP/USD | 46.848 | 0.098142 | -2.01% | 1.12x |
| 12 | PEPE/USD | 42.505 | 3.77e-06 | -1.26% | 0.96x |

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

- Persisted scans: 820; predictions: 6984; observations: 495771.
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

**Writer:** 44573127494 · **Generation:** 820 · **Legacy run:** 44573127494
**Main quote time:** 2026-11-19T17:05:04.176196+00:00 · **Legacy report time:** 2026-11-19T17:05:42.343497+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.05482 | 77.92 | +1.10% | 1.44x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.021651 | 71.82 | +1.32% | 0.71x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 3 | BMT/USD | 0.02037 | 62.36 | +0.44% | 0.13x | MODERATE 56/100 | EXTREME 88/100 | Do nothing |
| 4 | VVV/USD | 22.138 | 54.58 | -0.84% | 0.27x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | HYPE/USD | 67.18 | 54.23 | -0.41% | 0.96x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 6 | PYTH/USD | 0.05556 | 53.48 | -0.86% | 0.66x | WEAK 27/100 | EXTREME 87/100 | Do nothing |
| 7 | CSPR/USD | 0.0017103 | 52.74 | -0.06% | 0.63x | WEAK 26/100 | EXTREME 94/100 | Do nothing |
| 8 | SKR/USD | 0.010136 | 49.70 | -0.65% | 0.27x | WEAK 25/100 | EXTREME 94/100 | Do nothing |
| 9 | ALEO/USD | 0.03107 | 49.30 | -0.55% | 0.71x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | PUMP/USD | 0.002635 | 44.98 | -1.50% | 1.35x | WEAK 42/100 | HIGH 65/100 | Do nothing |
| 11 | CAP/USD | 0.098142 | 38.05 | -2.01% | 1.12x | WEAK 29/100 | VERY_HIGH 77/100 | Do nothing |
| 12 | PEPE/USD | 3.77e-06 | 35.87 | -1.26% | 0.96x | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.05492 | 80.23 | +0.53% | 1.32x | 2072 | STRONG 95/100 | HIGH 67/100 | Watch |

**Same-run overlap:** TRUST/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
