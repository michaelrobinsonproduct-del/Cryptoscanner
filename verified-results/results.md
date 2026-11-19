# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:10:22.051445+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44562909740
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 4d4c98278ff06f1f74e8c916d38104d5a9738aec (atomic ledger/results publication)
**Ledger generation:** 809 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BMT/USD | 0.02031 | 92.232 | 71.253 | +7.57% | +1.20% | 3.40x | 9.9 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | PYTH/USD | 0.05666 | 86.776 | 69.293 | +7.39% | +0.50% | 3.06x | 15.9 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | SYRUP/USD | 0.10238 | 83.463 | 68.658 | +7.81% | -0.04% | 2.91x | 15.6 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010377 | 75.757 | 67.386 | +7.72% | -1.01% | 2.34x | 17.3 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 5 | VVV/USD | 22.44 | 71.411 | 76.273 | +3.55% | -0.12% | 0.57x | 7.1 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | HYPE/USD | 67.62 | 69.332 | 61.267 | +1.11% | -0.04% | 1.83x | 3.0 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5453 | 65.277 | 67.466 | +5.27% | -0.38% | 0.97x | 1.8 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | ADA/USD | 0.152111 | 64.984 | 57.750 | +0.57% | +0.05% | 1.70x | 2.4 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 9 | BILL/USD | 0.00431 | 63.367 | 64.101 | +9.11% | +0.94% | 0.46x | 23.4 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | USELESS/USD | 0.10108 | 62.645 | 69.268 | +5.78% | -0.16% | 0.42x | 16.9 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.97167 | 58.708 | 58.582 | +0.55% | +0.34% | 0.84x | 0.5 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TAO/USD | 192.983 | 54.377 | 53.721 | +0.53% | -0.11% | 1.12x | 10.0 | 2026-11-19T16:10:13.624321+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 74/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 76.273 | 22.44 | -0.12% | 0.57x |
| 2 | BMT/USD | 71.253 | 0.02031 | +1.20% | 3.40x |
| 3 | PYTH/USD | 69.293 | 0.05666 | +0.50% | 3.06x |
| 4 | USELESS/USD | 69.268 | 0.10108 | -0.16% | 0.42x |
| 5 | SYRUP/USD | 68.658 | 0.10238 | -0.04% | 2.91x |
| 6 | AKT/USD | 67.466 | 0.5453 | -0.38% | 0.97x |
| 7 | SKR/USD | 67.386 | 0.010377 | -1.01% | 2.34x |
| 8 | BILL/USD | 64.101 | 0.00431 | +0.94% | 0.46x |
| 9 | HYPE/USD | 61.267 | 67.62 | -0.04% | 1.83x |
| 10 | XRP/USD | 58.582 | 0.97167 | +0.34% | 0.84x |
| 11 | ADA/USD | 57.750 | 0.152111 | +0.05% | 1.70x |
| 12 | TAO/USD | 53.721 | 192.983 | -0.11% | 1.12x |

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

- Persisted scans: 809; predictions: 6852; observations: 489200.
- Matured sampled outcomes across 1/6/24/48h: 6851; gap abstentions: 15306. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44562909740 · **Generation:** 809 · **Legacy run:** 44562909740
**Main quote time:** 2026-11-19T16:10:22.051445+00:00 · **Legacy report time:** 2026-11-19T16:10:58.515880+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.02031 | 92.23 | +1.20% | 3.40x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | PYTH/USD ⭐ | 0.05666 | 86.78 | +0.50% | 3.06x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | SYRUP/USD | 0.10238 | 83.46 | -0.04% | 2.91x | MODERATE 67/100 | VERY_HIGH 79/100 | Watch |
| 4 | SKR/USD | 0.010377 | 75.76 | -1.01% | 2.34x | MODERATE 63/100 | VERY_HIGH 83/100 | Watch |
| 5 | VVV/USD | 22.44 | 71.41 | -0.12% | 0.57x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 6 | HYPE/USD | 67.62 | 69.33 | -0.04% | 1.83x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | AKT/USD | 0.5453 | 65.28 | -0.38% | 0.97x | WEAK 38/100 | VERY_HIGH 80/100 | Watch |
| 8 | ADA/USD | 0.152111 | 64.98 | +0.05% | 1.70x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 9 | BILL/USD | 0.00431 | 63.37 | +0.94% | 0.46x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 10 | USELESS/USD | 0.10108 | 62.64 | -0.16% | 0.42x | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | XRP/USD | 0.97167 | 58.71 | +0.34% | 0.84x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 12 | TAO/USD | 192.983 | 54.38 | -0.11% | 1.12x | WEAK 32/100 | VERY_HIGH 74/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.02025 | 87.43 | +1.20% | 3.40x | 2939 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | PYTH/USD ⭐ | 0.05666 | 80.83 | +0.50% | 3.06x | 2728 | STRONG 95/100 | VERY_HIGH 72/100 | Watch |
| 3 | TRUST/USD | 0.05444 | 77.78 | +1.39% | 2.26x | 1911 | STRONG 94/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** BMT/USD, PYTH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
