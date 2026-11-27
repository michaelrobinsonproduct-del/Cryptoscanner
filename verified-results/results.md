# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T22:02:34.021049+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46073797099
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 938bb9f362945de4a05190b98be689bdc4fa557e (atomic ledger/results publication)
**Ledger generation:** 2066 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 733.41 | 93.626 | 96.794 | +7.59% | -0.00% | 0.68x | 6.4 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | PAXG/USD | 3642.47 | 75.428 | 60.415 | +2.41% | +0.00% | 4.55x | 0.2 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04997 | 75.273 | 71.656 | +3.09% | -0.20% | 1.46x | 10.0 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.85 | 70.053 | 72.555 | +2.62% | +0.06% | 0.72x | 1.6 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | LINK/USD | 9.3095 | 69.773 | 55.274 | +0.44% | -0.10% | 4.46x | 5.7 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | RENDER/USD | 1.404 | 68.946 | 66.752 | +5.33% | -0.28% | 1.36x | 7.1 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0575047 | 68.355 | 69.025 | +2.00% | -0.14% | 1.00x | 0.0 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 71.74 | 66.473 | 62.197 | +1.13% | -0.01% | 1.43x | 1.4 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XAUT/USD | 3645.3 | 63.146 | 54.455 | +2.40% | -0.02% | 1.88x | 0.3 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6727 | 58.425 | 59.498 | +0.75% | -0.15% | 0.97x | 1.5 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | LTC/USD | 44.27 | 57.716 | 62.352 | +1.21% | +0.05% | 0.51x | 2.3 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TAO/USD | 187.1401 | 54.186 | 62.961 | +1.83% | -0.17% | 0.21x | 9.6 | 2026-11-27T22:02:27.809152+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.794 | 733.41 | -0.00% | 0.68x |
| 2 | HYPE/USD | 72.555 | 63.85 | +0.06% | 0.72x |
| 3 | NIGHT/USD | 71.656 | 0.04997 | -0.20% | 1.46x |
| 4 | XDG/USD | 69.025 | 0.0575047 | -0.14% | 1.00x |
| 5 | RENDER/USD | 66.752 | 1.404 | -0.28% | 1.36x |
| 6 | TAO/USD | 62.961 | 187.1401 | -0.17% | 0.21x |
| 7 | LTC/USD | 62.352 | 44.27 | +0.05% | 0.51x |
| 8 | SOL/USD | 62.197 | 71.74 | -0.01% | 1.43x |
| 9 | PAXG/USD | 60.415 | 3642.47 | +0.00% | 4.55x |
| 10 | SUI/USD | 59.498 | 0.6727 | -0.15% | 0.97x |
| 11 | LINK/USD | 55.274 | 9.3095 | -0.10% | 4.46x |
| 12 | XAUT/USD | 54.455 | 3645.3 | -0.02% | 1.88x |

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

- Persisted scans: 2066; predictions: 18494; observations: 1251044.
- Matured sampled outcomes across 1/6/24/48h: 42035; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46073797099 · **Generation:** 2066 · **Legacy run:** 46073797099
**Main quote time:** 2026-11-27T22:02:34.021049+00:00 · **Legacy report time:** 2026-11-27T22:03:29.214917+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 733.41 | 93.63 | -0.00% | 0.68x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 2 | PAXG/USD | 3642.47 | 75.43 | +0.00% | 4.55x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD | 0.04997 | 75.27 | -0.20% | 1.46x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 4 | HYPE/USD | 63.85 | 70.05 | +0.06% | 0.72x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 5 | LINK/USD | 9.3095 | 69.77 | -0.10% | 4.46x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | RENDER/USD | 1.404 | 68.95 | -0.28% | 1.36x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 7 | XDG/USD | 0.0575047 | 68.35 | -0.14% | 1.00x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 71.74 | 66.47 | -0.01% | 1.43x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | XAUT/USD | 3645.3 | 63.15 | -0.02% | 1.88x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | SUI/USD | 0.6727 | 58.43 | -0.15% | 0.97x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 11 | LTC/USD | 44.27 | 57.72 | +0.05% | 0.51x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | TAO/USD | 187.1401 | 54.19 | -0.17% | 0.21x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

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
