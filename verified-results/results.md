# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:15:28.118498+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44596268285
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** a5ede750abe0bd06a9db43cb359ff5b7937e7f14 (atomic ledger/results publication)
**Ledger generation:** 842 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1281 | 77.160 | 69.019 | +8.38% | -0.54% | 2.09x | 15.7 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | VVV/USD | 22.529 | 71.745 | 79.157 | +3.96% | -0.23% | 0.37x | 7.1 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021377 | 69.808 | 57.287 | +3.75% | +0.15% | 2.18x | 6.5 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010193 | 66.765 | 66.901 | +5.81% | +0.44% | 0.76x | 9.8 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5479 | 62.156 | 66.106 | +5.77% | -0.51% | 0.86x | 12.8 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 6 | MEGA/USD | 0.05874 | 60.881 | 58.742 | +4.89% | +0.29% | 1.07x | 15.3 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97055 | 57.757 | 57.976 | +0.43% | -0.24% | 1.10x | 0.1 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 73.73 | 56.883 | 56.130 | +0.26% | -0.24% | 1.20x | 1.4 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ADA/USD | 0.1529 | 53.327 | 61.178 | +1.09% | -0.21% | 0.32x | 2.9 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HYPE/USD | 67.69 | 49.833 | 62.739 | +1.21% | -1.21% | 0.31x | 1.5 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | AVAX/USD | 7.044 | 49.195 | 46.542 | +0.33% | +0.00% | 1.27x | 4.3 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | MODERATE 50/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BNB/USD | 585.12 | 48.438 | 45.488 | +0.66% | -0.15% | 1.37x | 0.7 | 2026-11-19T19:15:19.333017+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.157 | 22.529 | -0.23% | 0.37x |
| 2 | CT/USD | 69.019 | 0.1281 | -0.54% | 2.09x |
| 3 | SKR/USD | 66.901 | 0.010193 | +0.44% | 0.76x |
| 4 | AKT/USD | 66.106 | 0.5479 | -0.51% | 0.86x |
| 5 | HYPE/USD | 62.739 | 67.69 | -1.21% | 0.31x |
| 6 | ADA/USD | 61.178 | 0.1529 | -0.21% | 0.32x |
| 7 | MEGA/USD | 58.742 | 0.05874 | +0.29% | 1.07x |
| 8 | XRP/USD | 57.976 | 0.97055 | -0.24% | 1.10x |
| 9 | SENT/USD | 57.287 | 0.021377 | +0.15% | 2.18x |
| 10 | SOL/USD | 56.130 | 73.73 | -0.24% | 1.20x |
| 11 | AVAX/USD | 46.542 | 7.044 | +0.00% | 1.27x |
| 12 | BNB/USD | 45.488 | 585.12 | -0.15% | 1.37x |

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

- Persisted scans: 842; predictions: 7248; observations: 508935.
- Matured sampled outcomes across 1/6/24/48h: 7247; gap abstentions: 15574. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44596268285 · **Generation:** 842 · **Legacy run:** 44596268285
**Main quote time:** 2026-11-19T19:15:28.118498+00:00 · **Legacy report time:** 2026-11-19T19:16:07.031589+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD | 0.1281 | 77.16 | -0.54% | 2.09x | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD | 22.529 | 71.75 | -0.23% | 0.37x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 3 | SENT/USD ⭐ | 0.021377 | 69.81 | +0.15% | 2.18x | STRONG 90/100 | HIGH 60/100 | Watch |
| 4 | SKR/USD | 0.010193 | 66.77 | +0.44% | 0.76x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 5 | AKT/USD | 0.5479 | 62.16 | -0.51% | 0.86x | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing |
| 6 | MEGA/USD ⭐ | 0.05874 | 60.88 | +0.29% | 1.07x | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 7 | XRP/USD | 0.97055 | 57.76 | -0.24% | 1.10x | WEAK 39/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 73.73 | 56.88 | -0.24% | 1.20x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | ADA/USD | 0.1529 | 53.33 | -0.21% | 0.32x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HYPE/USD | 67.69 | 49.83 | -1.21% | 0.31x | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | AVAX/USD | 7.044 | 49.19 | +0.00% | 1.27x | MODERATE 50/100 | HIGH 55/100 | Watch |
| 12 | BNB/USD | 585.12 | 48.44 | -0.15% | 1.37x | WEAK 44/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.02143 | 77.76 | +0.15% | 2.18x | 14641 | STRONG 94/100 | HIGH 60/100 | Watch |
| 2 | CSPR/USD | 0.0018634 | 73.10 | +0.27% | 1.31x | 4982 | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |
| 3 | MEGA/USD ⭐ | 0.05883 | 68.33 | +0.29% | 1.07x | 2147 | STRONG 74/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
