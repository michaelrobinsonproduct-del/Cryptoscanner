# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T19:21:41.291028+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45882792902
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c4bf453bd4945d6e8907d76363d816c42e33e1f0 (atomic ledger/results publication)
**Ledger generation:** 1902 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | FET/USD | 0.1214 | 94.189 | 70.417 | +11.89% | +1.75% | 4.06x | 16.5 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | STRONG 97/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.508 | 91.696 | 76.005 | +7.38% | +0.14% | 2.58x | 3.9 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | STRONG 91/100 | HIGH 60/100 | Watch | WATCH |
| 3 | ZRO/USD | 1.112 | 85.481 | 72.715 | +8.59% | -0.45% | 3.39x | 18.0 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 4 | INJ/USD | 6.254 | 81.328 | 72.846 | +5.04% | +0.32% | 1.69x | 4.8 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | LINK/USD | 9.29123 | 78.004 | 70.855 | +2.73% | +0.32% | 1.56x | 4.0 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ADA/USD | 0.150819 | 73.434 | 76.692 | +3.46% | +0.27% | 0.54x | 5.1 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1409 | 72.066 | 73.264 | +10.68% | -0.78% | 1.27x | 7.1 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | MODERATE 46/100 | HIGH 66/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04535 | 67.996 | 75.367 | +8.29% | -0.75% | 0.64x | 8.8 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | JUP/USD | 0.23991 | 66.225 | 69.329 | +5.87% | +0.62% | 0.38x | 10.4 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | XRP/USD | 0.95455 | 65.663 | 68.132 | +1.92% | +0.28% | 0.62x | 0.6 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ONDO/USD | 0.28856 | 63.990 | 47.687 | +2.15% | +0.26% | 3.66x | 0.3 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 12 | SOL/USD | 71.32 | 63.717 | 63.547 | +1.32% | +0.18% | 0.93x | 1.4 | 2026-11-26T19:21:33.315886+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ADA/USD | 76.692 | 0.150819 | +0.27% | 0.54x |
| 2 | AKT/USD | 76.005 | 0.508 | +0.14% | 2.58x |
| 3 | SKY/USD | 75.367 | 0.04535 | -0.75% | 0.64x |
| 4 | WIF/USD | 73.264 | 0.1409 | -0.78% | 1.27x |
| 5 | INJ/USD | 72.846 | 6.254 | +0.32% | 1.69x |
| 6 | ZRO/USD | 72.715 | 1.112 | -0.45% | 3.39x |
| 7 | LINK/USD | 70.855 | 9.29123 | +0.32% | 1.56x |
| 8 | FET/USD | 70.417 | 0.1214 | +1.75% | 4.06x |
| 9 | JUP/USD | 69.329 | 0.23991 | +0.62% | 0.38x |
| 10 | XRP/USD | 68.132 | 0.95455 | +0.28% | 0.62x |
| 11 | SOL/USD | 63.547 | 71.32 | +0.18% | 0.93x |
| 12 | ONDO/USD | 47.687 | 0.28856 | +0.26% | 3.66x |

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

- Persisted scans: 1902; predictions: 16559; observations: 1152235.
- Matured sampled outcomes across 1/6/24/48h: 35900; gap abstentions: 25180. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45882792902 · **Generation:** 1902 · **Legacy run:** 45882792902
**Main quote time:** 2026-11-26T19:21:41.291028+00:00 · **Legacy report time:** 2026-11-26T19:22:18.626074+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD | 0.1214 | 94.19 | +1.75% | 4.06x | STRONG 97/100 | HIGH 66/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.508 | 91.70 | +0.14% | 2.58x | STRONG 100/100 | HIGH 60/100 | Watch |
| 3 | ZRO/USD | 1.112 | 85.48 | -0.45% | 3.39x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 4 | INJ/USD ⭐ | 6.254 | 81.33 | +0.32% | 1.69x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.29123 | 78.00 | +0.32% | 1.56x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | ADA/USD | 0.150819 | 73.43 | +0.27% | 0.54x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 7 | WIF/USD | 0.1409 | 72.07 | -0.78% | 1.27x | MODERATE 46/100 | HIGH 66/100 | Watch |
| 8 | SKY/USD | 0.04535 | 68.00 | -0.75% | 0.64x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 9 | JUP/USD | 0.23991 | 66.23 | +0.62% | 0.38x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 10 | XRP/USD | 0.95455 | 65.66 | +0.28% | 0.62x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 11 | ONDO/USD | 0.28856 | 63.99 | +0.26% | 3.66x | STRONG 87/100 | HIGH 60/100 | Watch |
| 12 | SOL/USD | 71.32 | 63.72 | +0.18% | 0.93x | MODERATE 52/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.2859 | 82.04 | +0.32% | 1.56x | 6970 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.254 | 81.89 | +0.32% | 1.69x | 5580 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.508 | 78.40 | +0.14% | 2.58x | 2626 | STRONG 94/100 | HIGH 60/100 | Watch |
| 4 | DRV/USD | 0.39049 | 76.07 | +0.30% | 1.15x | 8190 | MODERATE 58/100 | VERY_HIGH 84/100 | Watch |

**Same-run overlap:** AKT/USD, INJ/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
