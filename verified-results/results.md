# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:35:34.243936+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44610064731
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** a18710748e70aa2711d963167a46cda9775ca24e (atomic ledger/results publication)
**Ledger generation:** 856 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 600; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.215 | 72.270 | 71.446 | +2.51% | -0.46% | 1.31x | 2.3 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SENT/USD | 0.020991 | 61.000 | 44.544 | +1.87% | +0.29% | 3.18x | 5.7 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 3 | INJ/USD | 7.042 | 58.545 | 48.719 | +0.87% | -0.27% | 2.12x | 4.3 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CSPR/USD | 0.0017614 | 57.717 | 59.299 | +7.86% | -0.84% | 1.26x | 35.2 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 5 | SKR/USD | 0.010092 | 53.849 | 57.548 | +4.76% | -0.42% | 0.84x | 13.9 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 27/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5486 | 53.679 | 67.213 | +5.91% | -1.08% | 0.19x | 12.8 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 27/100 | EXTREME 91/100 | Do nothing | WATCH |
| 7 | USELESS/USD | 0.09773 | 39.649 | 45.557 | +2.27% | -0.44% | 0.63x | 16.4 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | PYTH/USD | 0.05325 | 33.953 | 33.319 | +0.93% | -0.78% | 1.45x | 11.3 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 9 | PUMP/USD | 0.002625 | 32.533 | 45.071 | +1.12% | -0.79% | 0.14x | 11.4 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | ICP/USD | 2.189 | 28.788 | 34.145 | +0.51% | +0.05% | 0.44x | 9.2 | 2026-11-19T20:35:27.353052+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 71.446 | 22.215 | -0.46% | 1.31x |
| 2 | AKT/USD | 67.213 | 0.5486 | -1.08% | 0.19x |
| 3 | CSPR/USD | 59.299 | 0.0017614 | -0.84% | 1.26x |
| 4 | SKR/USD | 57.548 | 0.010092 | -0.42% | 0.84x |
| 5 | INJ/USD | 48.719 | 7.042 | -0.27% | 2.12x |
| 6 | USELESS/USD | 45.557 | 0.09773 | -0.44% | 0.63x |
| 7 | PUMP/USD | 45.071 | 0.002625 | -0.79% | 0.14x |
| 8 | SENT/USD | 44.544 | 0.020991 | +0.29% | 3.18x |
| 9 | ICP/USD | 34.145 | 2.189 | +0.05% | 0.44x |
| 10 | PYTH/USD | 33.319 | 0.05325 | -0.78% | 1.45x |

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

- Persisted scans: 856; predictions: 7411; observations: 517323.
- Matured sampled outcomes across 1/6/24/48h: 7535; gap abstentions: 15653. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44610064731 · **Generation:** 856 · **Legacy run:** 44610064731
**Main quote time:** 2026-11-19T20:35:34.243936+00:00 · **Legacy report time:** 2026-11-19T20:36:30.997780+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.215 | 72.27 | -0.46% | 1.31x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 2 | SENT/USD ⭐ | 0.020991 | 61.00 | +0.29% | 3.18x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 3 | INJ/USD | 7.042 | 58.55 | -0.27% | 2.12x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 4 | CSPR/USD | 0.0017614 | 57.72 | -0.84% | 1.26x | WEAK 24/100 | VERY_HIGH 78/100 | Do nothing |
| 5 | SKR/USD | 0.010092 | 53.85 | -0.42% | 0.84x | WEAK 27/100 | EXTREME 86/100 | Do nothing |
| 6 | AKT/USD | 0.5486 | 53.68 | -1.08% | 0.19x | WEAK 27/100 | EXTREME 91/100 | Do nothing |
| 7 | USELESS/USD | 0.09773 | 39.65 | -0.44% | 0.63x | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | PYTH/USD | 0.05325 | 33.95 | -0.78% | 1.45x | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing |
| 9 | PUMP/USD | 0.002625 | 32.53 | -0.79% | 0.14x | WEAK 16/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | ICP/USD | 2.189 | 28.79 | +0.05% | 0.44x | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021007 | 56.86 | +0.29% | 3.18x | 14730 | STRONG 93/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
