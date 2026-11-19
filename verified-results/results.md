# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:20:24.316175+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44553506943
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 5ed613d3ae6236eb77b2352d5221882f0e064f48 (atomic ledger/results publication)
**Ledger generation:** 800 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.977 | 87.336 | 91.742 | +6.03% | -1.87% | 1.49x | 10.9 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | AKT/USD | 0.55 | 84.310 | 73.814 | +6.18% | -0.90% | 3.56x | 1.8 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021943 | 83.098 | 76.083 | +6.49% | -0.12% | 1.76x | 5.5 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 4 | PYTH/USD | 0.05637 | 70.415 | 69.999 | +6.84% | -0.46% | 1.27x | 14.3 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | LIGHTER/USD | 2.923 | 68.968 | 70.576 | +7.70% | -1.42% | 1.55x | 20.5 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | PEARL/USD | 2.3495 | 62.363 | 57.386 | +0.40% | +1.06% | 0.97x | 0.9 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ZEC/USD | 932.57 | 61.277 | 68.897 | +2.26% | -1.11% | 0.79x | 3.9 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | ETH/USD | 1786.05 | 59.599 | 58.585 | +0.64% | -1.27% | 1.74x | 1.7 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | MODERATE 50/100 | HIGH 65/100 | Do nothing | WATCH |
| 9 | GRASS/USD | 0.4453 | 55.722 | 70.936 | +9.90% | -2.17% | 0.57x | 15.8 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 28/100 | EXTREME 91/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.98022 | 55.073 | 64.420 | +1.43% | -1.05% | 0.59x | 1.2 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | XBT/USD | 63160.4 | 54.530 | 56.234 | +0.28% | -0.92% | 1.29x | 1.4 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 37/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SOL/USD | 74.42 | 51.491 | 62.705 | +1.20% | -1.12% | 0.44x | 1.3 | 2026-11-19T15:20:15.658842+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.742 | 22.977 | -1.87% | 1.49x |
| 2 | SENT/USD | 76.083 | 0.021943 | -0.12% | 1.76x |
| 3 | AKT/USD | 73.814 | 0.55 | -0.90% | 3.56x |
| 4 | GRASS/USD | 70.936 | 0.4453 | -2.17% | 0.57x |
| 5 | LIGHTER/USD | 70.576 | 2.923 | -1.42% | 1.55x |
| 6 | PYTH/USD | 69.999 | 0.05637 | -0.46% | 1.27x |
| 7 | ZEC/USD | 68.897 | 932.57 | -1.11% | 0.79x |
| 8 | XRP/USD | 64.420 | 0.98022 | -1.05% | 0.59x |
| 9 | SOL/USD | 62.705 | 74.42 | -1.12% | 0.44x |
| 10 | ETH/USD | 58.585 | 1786.05 | -1.27% | 1.74x |
| 11 | PEARL/USD | 57.386 | 2.3495 | +1.06% | 0.97x |
| 12 | XBT/USD | 56.234 | 63160.4 | -0.92% | 1.29x |

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

- Persisted scans: 800; predictions: 6744; observations: 483836.
- Matured sampled outcomes across 1/6/24/48h: 6755; gap abstentions: 15198. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44553506943 · **Generation:** 800 · **Legacy run:** 44553506943
**Main quote time:** 2026-11-19T15:20:24.316175+00:00 · **Legacy report time:** 2026-11-19T15:21:09.470655+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.977 | 87.34 | -1.87% | 1.49x | MODERATE 59/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | AKT/USD | 0.55 | 84.31 | -0.90% | 3.56x | STRONG 72/100 | VERY_HIGH 73/100 | Watch |
| 3 | SENT/USD | 0.021943 | 83.10 | -0.12% | 1.76x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 4 | PYTH/USD | 0.05637 | 70.42 | -0.46% | 1.27x | WEAK 40/100 | VERY_HIGH 72/100 | Watch |
| 5 | LIGHTER/USD | 2.923 | 68.97 | -1.42% | 1.55x | WEAK 44/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | PEARL/USD | 2.3495 | 62.36 | +1.06% | 0.97x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 7 | ZEC/USD | 932.57 | 61.28 | -1.11% | 0.79x | WEAK 36/100 | VERY_HIGH 72/100 | Watch |
| 8 | ETH/USD | 1786.05 | 59.60 | -1.27% | 1.74x | MODERATE 50/100 | HIGH 65/100 | Do nothing |
| 9 | GRASS/USD | 0.4453 | 55.72 | -2.17% | 0.57x | WEAK 28/100 | EXTREME 91/100 | Do nothing |
| 10 | XRP/USD | 0.98022 | 55.07 | -1.05% | 0.59x | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | XBT/USD | 63160.4 | 54.53 | -0.92% | 1.29x | WEAK 37/100 | HIGH 61/100 | Watch |
| 12 | SOL/USD | 74.42 | 51.49 | -1.12% | 0.44x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |

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
