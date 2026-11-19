# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:05:29.270653+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44604891431
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 25902f5fcc771885968d3c7aec2d19eeca375ea8 (atomic ledger/results publication)
**Ledger generation:** 851 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.456 | 90.482 | 77.235 | +3.62% | -0.35% | 9.86x | 6.2 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5516 | 79.874 | 69.098 | +6.49% | -0.84% | 6.09x | 16.3 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | ADA/USD | 0.152352 | 67.669 | 58.932 | +0.73% | -0.72% | 2.23x | 2.3 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ALEO/USD | 0.03115 | 60.758 | 62.030 | +3.90% | -0.54% | 1.14x | 3.2 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010119 | 56.994 | 62.013 | +5.05% | +0.11% | 0.44x | 8.9 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | HYPE/USD | 67.34 | 54.538 | 57.586 | +0.69% | -0.61% | 1.00x | 4.5 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | SENT/USD | 0.021101 | 47.620 | 49.208 | +2.41% | -1.08% | 1.38x | 3.8 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.05357 | 46.355 | 39.433 | +1.54% | -0.78% | 2.08x | 7.5 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 9 | INJ/USD | 7.063 | 43.424 | 50.177 | +1.17% | -0.27% | 0.46x | 5.7 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | CSPR/USD | 0.0018234 | 40.080 | 60.574 | +11.65% | -2.85% | 0.37x | 32.6 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 15/100 | EXTREME 97/100 | Do nothing | WATCH |
| 11 | ONDO/USD | 0.29865 | 27.950 | 37.091 | +0.34% | -0.26% | 0.22x | 2.7 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | SHIB/USD | 3.811e-06 | 23.387 | 34.687 | +0.45% | -0.55% | 0.14x | 2.6 | 2026-11-19T20:05:23.084823+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.235 | 22.456 | -0.35% | 9.86x |
| 2 | AKT/USD | 69.098 | 0.5516 | -0.84% | 6.09x |
| 3 | ALEO/USD | 62.030 | 0.03115 | -0.54% | 1.14x |
| 4 | SKR/USD | 62.013 | 0.010119 | +0.11% | 0.44x |
| 5 | CSPR/USD | 60.574 | 0.0018234 | -2.85% | 0.37x |
| 6 | ADA/USD | 58.932 | 0.152352 | -0.72% | 2.23x |
| 7 | HYPE/USD | 57.586 | 67.34 | -0.61% | 1.00x |
| 8 | INJ/USD | 50.177 | 7.063 | -0.27% | 0.46x |
| 9 | SENT/USD | 49.208 | 0.021101 | -1.08% | 1.38x |
| 10 | PYTH/USD | 39.433 | 0.05357 | -0.78% | 2.08x |
| 11 | ONDO/USD | 37.091 | 0.29865 | -0.26% | 0.22x |
| 12 | SHIB/USD | 34.687 | 3.811e-06 | -0.55% | 0.14x |

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

- Persisted scans: 851; predictions: 7356; observations: 514326.
- Matured sampled outcomes across 1/6/24/48h: 7415; gap abstentions: 15634. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44604891431 · **Generation:** 851 · **Legacy run:** 44604891431
**Main quote time:** 2026-11-19T20:05:29.270653+00:00 · **Legacy report time:** 2026-11-19T20:06:13.492907+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.456 | 90.48 | -0.35% | 9.86x | STRONG 75/100 | HIGH 61/100 | Watch |
| 2 | AKT/USD | 0.5516 | 79.87 | -0.84% | 6.09x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 3 | ADA/USD | 0.152352 | 67.67 | -0.72% | 2.23x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 4 | ALEO/USD | 0.03115 | 60.76 | -0.54% | 1.14x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 5 | SKR/USD | 0.010119 | 56.99 | +0.11% | 0.44x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 6 | HYPE/USD | 67.34 | 54.54 | -0.61% | 1.00x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 7 | SENT/USD | 0.021101 | 47.62 | -1.08% | 1.38x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 8 | PYTH/USD | 0.05357 | 46.36 | -0.78% | 2.08x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 9 | INJ/USD | 7.063 | 43.42 | -0.27% | 0.46x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | CSPR/USD | 0.0018234 | 40.08 | -2.85% | 0.37x | WEAK 15/100 | EXTREME 97/100 | Do nothing |
| 11 | ONDO/USD | 0.29865 | 27.95 | -0.26% | 0.22x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | SHIB/USD | 3.811e-06 | 23.39 | -0.55% | 0.14x | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
