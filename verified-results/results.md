# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T07:47:45.741324+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45570512744
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7f92446b180a8e155a8c3c3ea7cb5e68b8e8117d (atomic ledger/results publication)
**Ledger generation:** 1689 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01041 | 79.390 | 84.795 | +9.93% | -2.46% | 1.69x | 19.3 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | DRV/USD | 0.33365 | 69.896 | 74.055 | +6.16% | -1.00% | 1.08x | 12.9 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00891 | 68.004 | 71.674 | +7.87% | +0.11% | 0.58x | 11.2 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.469e-06 | 37.219 | 42.034 | +0.46% | -0.55% | 0.79x | 11.5 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 5 | CT/USD | 0.1267 | 31.496 | 21.278 | +0.32% | -0.55% | 2.30x | 23.6 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | WEAK 36/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | CAP/USD | 0.092981 | 29.025 | 33.434 | +0.61% | -0.43% | 0.78x | 6.1 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 7 | XPL/USD | 0.0447 | 24.904 | 24.038 | +1.59% | -0.45% | 1.31x | 44.7 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | WEAK 17/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | SYRUP/USD | 0.07132 | 23.430 | 34.268 | +2.37% | -0.89% | 0.36x | 28.1 | 2026-11-25T07:47:38.694909+00:00 | Not calibrated | WEAK 7/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 84.795 | 0.01041 | -2.46% | 1.69x |
| 2 | DRV/USD | 74.055 | 0.33365 | -1.00% | 1.08x |
| 3 | BABY/USD | 71.674 | 0.00891 | +0.11% | 0.58x |
| 4 | PEPE/USD | 42.034 | 3.469e-06 | -0.55% | 0.79x |
| 5 | SYRUP/USD | 34.268 | 0.07132 | -0.89% | 0.36x |
| 6 | CAP/USD | 33.434 | 0.092981 | -0.43% | 0.78x |
| 7 | XPL/USD | 24.038 | 0.0447 | -0.45% | 1.31x |
| 8 | CT/USD | 21.278 | 0.1267 | -0.55% | 2.30x |

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

- Persisted scans: 1689; predictions: 14339; observations: 1023692.
- Matured sampled outcomes across 1/6/24/48h: 30709; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45570512744 · **Generation:** 1689 · **Legacy run:** 45570512744
**Main quote time:** 2026-11-25T07:47:45.741324+00:00 · **Legacy report time:** 2026-11-25T07:48:54.403138+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01041 | 79.39 | -2.46% | 1.69x | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | DRV/USD | 0.33365 | 69.90 | -1.00% | 1.08x | WEAK 40/100 | VERY_HIGH 74/100 | Watch |
| 3 | BABY/USD | 0.00891 | 68.00 | +0.11% | 0.58x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 4 | PEPE/USD | 3.469e-06 | 37.22 | -0.55% | 0.79x | WEAK 19/100 | VERY_HIGH 74/100 | Do nothing |
| 5 | CT/USD | 0.1267 | 31.50 | -0.55% | 2.30x | WEAK 36/100 | EXTREME 85/100 | Do nothing |
| 6 | CAP/USD | 0.092981 | 29.02 | -0.43% | 0.78x | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing |
| 7 | XPL/USD | 0.0447 | 24.90 | -0.45% | 1.31x | WEAK 17/100 | EXTREME 88/100 | Do nothing |
| 8 | SYRUP/USD | 0.07132 | 23.43 | -0.89% | 0.36x | WEAK 7/100 | EXTREME 93/100 | Do nothing |

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
