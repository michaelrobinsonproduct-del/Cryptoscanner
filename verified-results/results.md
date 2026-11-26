# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T23:40:57.256357+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45912227122
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 524354a51df57223a3fcd7b3a2f0636a24973073 (atomic ledger/results publication)
**Ledger generation:** 1929 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.25065 | 73.531 | 69.818 | +2.28% | -0.03% | 1.39x | 2.3 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZRO/USD | 1.128 | 71.835 | 76.162 | +10.16% | +0.53% | 0.30x | 8.8 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | LTC/USD | 43.83 | 66.619 | 72.215 | +2.62% | +0.00% | 0.44x | 2.3 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.18 | 65.307 | 59.752 | +0.91% | +0.24% | 1.43x | 3.2 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ADA/USD | 0.148383 | 65.053 | 65.546 | +1.79% | +0.17% | 0.87x | 3.0 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 6 | INJ/USD | 6.179 | 60.417 | 63.234 | +3.78% | +0.59% | 0.43x | 3.2 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05383 | 56.843 | 56.217 | +3.32% | +0.24% | 0.94x | 3.7 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 8 | SOL/USD | 70.91 | 54.939 | 59.466 | +0.74% | -0.01% | 0.55x | 1.4 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XRP/USD | 0.94119 | 52.268 | 58.407 | +0.49% | -0.12% | 0.44x | 0.1 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ONDO/USD | 0.28638 | 47.277 | 41.309 | +1.37% | -0.02% | 1.61x | 1.4 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | WEAK 44/100 | HIGH 66/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0563267 | 40.751 | 47.286 | +0.66% | -0.02% | 0.36x | 0.0 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | KAS/USD | 0.02665 | 20.149 | 29.172 | +0.38% | -0.11% | 0.15x | 11.3 | 2026-11-26T23:40:49.667493+00:00 | Not calibrated | WEAK 10/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 76.162 | 1.128 | +0.53% | 0.30x |
| 2 | LTC/USD | 72.215 | 43.83 | +0.00% | 0.44x |
| 3 | LINK/USD | 69.818 | 9.25065 | -0.03% | 1.39x |
| 4 | ADA/USD | 65.546 | 0.148383 | +0.17% | 0.87x |
| 5 | INJ/USD | 63.234 | 6.179 | +0.59% | 0.43x |
| 6 | HYPE/USD | 59.752 | 62.18 | +0.24% | 1.43x |
| 7 | SOL/USD | 59.466 | 70.91 | -0.01% | 0.55x |
| 8 | XRP/USD | 58.407 | 0.94119 | -0.12% | 0.44x |
| 9 | HBAR/USD | 56.217 | 0.05383 | +0.24% | 0.94x |
| 10 | XDG/USD | 47.286 | 0.0563267 | -0.02% | 0.36x |
| 11 | ONDO/USD | 41.309 | 0.28638 | -0.02% | 1.61x |
| 12 | KAS/USD | 29.172 | 0.02665 | -0.11% | 0.15x |

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

- Persisted scans: 1929; predictions: 16878; observations: 1168414.
- Matured sampled outcomes across 1/6/24/48h: 36848; gap abstentions: 25361. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
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

**Writer:** 45912227122 · **Generation:** 1929 · **Legacy run:** 45912227122
**Main quote time:** 2026-11-26T23:40:57.256357+00:00 · **Legacy report time:** 2026-11-26T23:41:32.174386+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.25065 | 73.53 | -0.03% | 1.39x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 2 | ZRO/USD | 1.128 | 71.83 | +0.53% | 0.30x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 3 | LTC/USD | 43.83 | 66.62 | +0.00% | 0.44x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 4 | HYPE/USD | 62.18 | 65.31 | +0.24% | 1.43x | STRONG 78/100 | HIGH 55/100 | Watch |
| 5 | ADA/USD | 0.148383 | 65.05 | +0.17% | 0.87x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 6 | INJ/USD | 6.179 | 60.42 | +0.59% | 0.43x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 7 | HBAR/USD | 0.05383 | 56.84 | +0.24% | 0.94x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 8 | SOL/USD | 70.91 | 54.94 | -0.01% | 0.55x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XRP/USD | 0.94119 | 52.27 | -0.12% | 0.44x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ONDO/USD | 0.28638 | 47.28 | -0.02% | 1.61x | WEAK 44/100 | HIGH 66/100 | Watch |
| 11 | XDG/USD | 0.0563267 | 40.75 | -0.02% | 0.36x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | KAS/USD | 0.02665 | 20.15 | -0.11% | 0.15x | WEAK 10/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ME/USD | 0.0421 | 74.78 | +0.48% | 1.46x | 4820 | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
