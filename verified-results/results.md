# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T22:31:01.441490+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45905115234
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bdcd3b4483bca06755e65cadaf25bcfa6d174315 (atomic ledger/results publication)
**Ledger generation:** 1922 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 10s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.131 | 90.173 | 76.496 | +10.45% | -0.26% | 7.78x | 8.9 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 2 | LTC/USD | 44.04 | 90.075 | 75.663 | +3.11% | +0.16% | 2.36x | 2.3 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 3 | DRV/USD | 0.38577 | 83.005 | 73.233 | +7.82% | -1.05% | 2.57x | 19.7 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5041 | 79.792 | 73.961 | +6.55% | +0.14% | 1.51x | 7.9 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 5 | LINK/USD | 9.31963 | 75.191 | 75.004 | +3.04% | +0.04% | 1.00x | 2.6 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6689 | 68.916 | 53.916 | +0.39% | +0.00% | 8.39x | 1.5 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ADA/USD | 0.149519 | 64.381 | 70.524 | +2.57% | +0.13% | 0.32x | 3.6 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0565147 | 64.297 | 48.998 | +0.99% | +0.06% | 3.33x | 1.8 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 9 | W/USD | 0.00882 | 64.294 | 70.440 | +6.27% | -0.11% | 0.44x | 11.4 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | PIEVERSE/USD | 3.8251 | 63.803 | 75.394 | +8.03% | -0.91% | 0.30x | 19.3 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | SOL/USD | 71.14 | 58.174 | 61.755 | +1.07% | +0.14% | 0.57x | 1.4 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1694.82 | 57.345 | 56.797 | +0.26% | +0.04% | 1.04x | 0.1 | 2026-11-26T22:30:51.940935+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 76.496 | 1.131 | -0.26% | 7.78x |
| 2 | LTC/USD | 75.663 | 44.04 | +0.16% | 2.36x |
| 3 | PIEVERSE/USD | 75.394 | 3.8251 | -0.91% | 0.30x |
| 4 | LINK/USD | 75.004 | 9.31963 | +0.04% | 1.00x |
| 5 | AKT/USD | 73.961 | 0.5041 | +0.14% | 1.51x |
| 6 | DRV/USD | 73.233 | 0.38577 | -1.05% | 2.57x |
| 7 | ADA/USD | 70.524 | 0.149519 | +0.13% | 0.32x |
| 8 | W/USD | 70.440 | 0.00882 | -0.11% | 0.44x |
| 9 | SOL/USD | 61.755 | 71.14 | +0.14% | 0.57x |
| 10 | ETH/USD | 56.797 | 1694.82 | +0.04% | 1.04x |
| 11 | SUI/USD | 53.916 | 0.6689 | +0.00% | 8.39x |
| 12 | XDG/USD | 48.998 | 0.0565147 | +0.06% | 3.33x |

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

- Persisted scans: 1922; predictions: 16799; observations: 1164212.
- Matured sampled outcomes across 1/6/24/48h: 36608; gap abstentions: 25312. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45905115234 · **Generation:** 1922 · **Legacy run:** 45905115234
**Main quote time:** 2026-11-26T22:31:01.441490+00:00 · **Legacy report time:** 2026-11-26T22:31:36.008340+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD | 1.131 | 90.17 | -0.26% | 7.78x | STRONG 75/100 | HIGH 66/100 | Watch |
| 2 | LTC/USD ⭐ | 44.04 | 90.08 | +0.16% | 2.36x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD | 0.38577 | 83.01 | -1.05% | 2.57x | MODERATE 67/100 | VERY_HIGH 71/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5041 | 79.79 | +0.14% | 1.51x | STRONG 85/100 | HIGH 60/100 | Watch |
| 5 | LINK/USD | 9.31963 | 75.19 | +0.04% | 1.00x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 6 | SUI/USD | 0.6689 | 68.92 | +0.00% | 8.39x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | ADA/USD | 0.149519 | 64.38 | +0.13% | 0.32x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD | 0.0565147 | 64.30 | +0.06% | 3.33x | STRONG 77/100 | HIGH 55/100 | Watch |
| 9 | W/USD | 0.00882 | 64.29 | -0.11% | 0.44x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 10 | PIEVERSE/USD | 3.8251 | 63.80 | -0.91% | 0.30x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | SOL/USD | 71.14 | 58.17 | +0.14% | 0.57x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1694.82 | 57.35 | +0.04% | 1.04x | MODERATE 54/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 44.07 | 91.60 | +0.16% | 2.36x | 14386 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5041 | 74.23 | +0.14% | 1.51x | 2753 | STRONG 77/100 | HIGH 66/100 | Watch |

**Same-run overlap:** LTC/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
