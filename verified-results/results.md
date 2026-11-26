# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T08:06:11.917164+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45780120027
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 23286b9c64a01f5905e55cd72b6a6fc5f749803d (atomic ledger/results publication)
**Ledger generation:** 1834 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07217 | 67.371 | 70.388 | +8.90% | -0.15% | 0.77x | 13.8 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 2 | HBAR/USD | 0.0534 | 65.761 | 52.719 | +2.50% | -0.39% | 2.93x | 3.7 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.42 | 62.985 | 63.180 | +1.66% | -0.18% | 1.07x | 6.9 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ADA/USD | 0.147709 | 60.949 | 62.313 | +1.33% | -0.04% | 0.88x | 4.0 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 5 | INJ/USD | 6.159 | 60.028 | 59.276 | +3.44% | +0.31% | 0.92x | 14.6 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95238 | 56.776 | 64.566 | +1.69% | +0.03% | 0.21x | 4.5 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LINK/USD | 9.15168 | 55.889 | 60.870 | +1.18% | -0.08% | 0.54x | 3.5 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SOL/USD | 70.91 | 52.889 | 59.466 | +0.74% | -0.06% | 0.37x | 1.4 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XBT/USD | 60549.1 | 50.976 | 57.085 | +0.30% | +0.02% | 0.38x | 0.0 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.497e-06 | 49.256 | 42.434 | +0.37% | +0.09% | 1.64x | 8.6 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | MODERATE 60/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0565084 | 48.125 | 53.667 | +0.98% | +0.01% | 0.44x | 6.6 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.128517 | 41.276 | 47.391 | +0.54% | +0.02% | 0.38x | 1.7 | 2026-11-26T08:06:04.434032+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 70.388 | 0.07217 | -0.15% | 0.77x |
| 2 | XRP/USD | 64.566 | 0.95238 | +0.03% | 0.21x |
| 3 | LTC/USD | 63.180 | 43.42 | -0.18% | 1.07x |
| 4 | ADA/USD | 62.313 | 0.147709 | -0.04% | 0.88x |
| 5 | LINK/USD | 60.870 | 9.15168 | -0.08% | 0.54x |
| 6 | SOL/USD | 59.466 | 70.91 | -0.06% | 0.37x |
| 7 | INJ/USD | 59.276 | 6.159 | +0.31% | 0.92x |
| 8 | XBT/USD | 57.085 | 60549.1 | +0.02% | 0.38x |
| 9 | XDG/USD | 53.667 | 0.0565084 | +0.01% | 0.44x |
| 10 | HBAR/USD | 52.719 | 0.0534 | -0.39% | 2.93x |
| 11 | XLM/USD | 47.391 | 0.128517 | +0.02% | 0.38x |
| 12 | PEPE/USD | 42.434 | 3.497e-06 | +0.09% | 1.64x |

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

- Persisted scans: 1834; predictions: 15743; observations: 1111948.
- Matured sampled outcomes across 1/6/24/48h: 34118; gap abstentions: 24285. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45780120027 · **Generation:** 1834 · **Legacy run:** 45780120027
**Main quote time:** 2026-11-26T08:06:11.917164+00:00 · **Legacy report time:** 2026-11-26T08:07:17.654760+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.07217 | 67.37 | -0.15% | 0.77x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 2 | HBAR/USD | 0.0534 | 65.76 | -0.39% | 2.93x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.42 | 62.99 | -0.18% | 1.07x | WEAK 41/100 | HIGH 68/100 | Watch |
| 4 | ADA/USD | 0.147709 | 60.95 | -0.04% | 0.88x | WEAK 35/100 | HIGH 68/100 | Watch |
| 5 | INJ/USD | 6.159 | 60.03 | +0.31% | 0.92x | MODERATE 55/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.95238 | 56.78 | +0.03% | 0.21x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 7 | LINK/USD | 9.15168 | 55.89 | -0.08% | 0.54x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SOL/USD | 70.91 | 52.89 | -0.06% | 0.37x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XBT/USD | 60549.1 | 50.98 | +0.02% | 0.38x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 10 | PEPE/USD | 3.497e-06 | 49.26 | +0.09% | 1.64x | MODERATE 60/100 | HIGH 55/100 | Watch |
| 11 | XDG/USD | 0.0565084 | 48.13 | +0.01% | 0.44x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD | 0.128517 | 41.28 | +0.02% | 0.38x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |

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
