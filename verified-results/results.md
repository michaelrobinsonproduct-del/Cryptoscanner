# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:45:33.210916+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44601463173
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** fc9a44c7bdf71c1dc808f45cbe8f8cac4d546f0a (atomic ledger/results publication)
**Ledger generation:** 847 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.555 | 74.767 | 80.223 | +4.08% | -0.27% | 0.59x | 6.7 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010131 | 70.189 | 62.890 | +5.17% | -0.38% | 1.92x | 8.9 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ALEO/USD | 0.03129 | 68.037 | 64.939 | +4.37% | +0.45% | 1.08x | 3.2 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5514 | 66.203 | 70.740 | +6.45% | +0.04% | 0.53x | 12.7 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | ADA/USD | 0.153045 | 63.622 | 61.294 | +1.18% | -0.20% | 1.33x | 4.0 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HYPE/USD | 67.87 | 60.027 | 63.887 | +1.48% | +0.04% | 0.59x | 3.0 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | CT/USD | 0.1296 | 57.701 | 65.343 | +9.64% | -0.69% | 0.58x | 23.1 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | WEAK 24/100 | EXTREME 93/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.310446 | 55.472 | 42.323 | +0.38% | -0.03% | 2.33x | 2.5 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ONDO/USD | 0.29945 | 52.345 | 39.044 | +0.60% | -0.34% | 13.09x | 2.3 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 10 | SHIB/USD | 3.831e-06 | 50.791 | 35.791 | +0.98% | +0.00% | 6.49x | 7.8 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 11 | INJ/USD | 7.092 | 45.607 | 54.082 | +1.59% | -0.17% | 0.24x | 4.2 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SENT/USD | 0.021313 | 41.547 | 54.117 | +3.44% | -1.13% | 0.31x | 8.5 | 2026-11-19T19:45:24.103224+00:00 | Not calibrated | WEAK 26/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.223 | 22.555 | -0.27% | 0.59x |
| 2 | AKT/USD | 70.740 | 0.5514 | +0.04% | 0.53x |
| 3 | CT/USD | 65.343 | 0.1296 | -0.69% | 0.58x |
| 4 | ALEO/USD | 64.939 | 0.03129 | +0.45% | 1.08x |
| 5 | HYPE/USD | 63.887 | 67.87 | +0.04% | 0.59x |
| 6 | SKR/USD | 62.890 | 0.010131 | -0.38% | 1.92x |
| 7 | ADA/USD | 61.294 | 0.153045 | -0.20% | 1.33x |
| 8 | SENT/USD | 54.117 | 0.021313 | -1.13% | 0.31x |
| 9 | INJ/USD | 54.082 | 7.092 | -0.17% | 0.24x |
| 10 | TRX/USD | 42.323 | 0.310446 | -0.03% | 2.33x |
| 11 | ONDO/USD | 39.044 | 0.29945 | -0.34% | 13.09x |
| 12 | SHIB/USD | 35.791 | 3.831e-06 | +0.00% | 6.49x |

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

- Persisted scans: 847; predictions: 7308; observations: 511930.
- Matured sampled outcomes across 1/6/24/48h: 7331; gap abstentions: 15620. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44601463173 · **Generation:** 847 · **Legacy run:** 44601463173
**Main quote time:** 2026-11-19T19:45:33.210916+00:00 · **Legacy report time:** 2026-11-19T19:46:18.419047+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.555 | 74.77 | -0.27% | 0.59x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 2 | SKR/USD | 0.010131 | 70.19 | -0.38% | 1.92x | MODERATE 55/100 | VERY_HIGH 73/100 | Watch |
| 3 | ALEO/USD ⭐ | 0.03129 | 68.04 | +0.45% | 1.08x | STRONG 79/100 | HIGH 67/100 | Watch |
| 4 | AKT/USD | 0.5514 | 66.20 | +0.04% | 0.53x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 5 | ADA/USD | 0.153045 | 63.62 | -0.20% | 1.33x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 6 | HYPE/USD | 67.87 | 60.03 | +0.04% | 0.59x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 7 | CT/USD | 0.1296 | 57.70 | -0.69% | 0.58x | WEAK 24/100 | EXTREME 93/100 | Do nothing |
| 8 | TRX/USD | 0.310446 | 55.47 | -0.03% | 2.33x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 9 | ONDO/USD | 0.29945 | 52.35 | -0.34% | 13.09x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 10 | SHIB/USD | 3.831e-06 | 50.79 | +0.00% | 6.49x | STRONG 70/100 | HIGH 60/100 | Watch |
| 11 | INJ/USD | 7.092 | 45.61 | -0.17% | 0.24x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SENT/USD | 0.021313 | 41.55 | -1.13% | 0.31x | WEAK 26/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALEO/USD ⭐ | 0.03132 | 83.88 | +0.45% | 1.08x | 6706 | STRONG 87/100 | HIGH 67/100 | Watch |

**Same-run overlap:** ALEO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
