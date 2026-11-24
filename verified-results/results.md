# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T20:37:23.334347+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45482235473
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c8331cf4bd973dc0957c220c6e56e4f2548b7f62 (atomic ledger/results publication)
**Ledger generation:** 1623 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 499.63 | 67.489 | 69.997 | +2.80% | +0.03% | 0.74x | 9.2 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.432e-06 | 56.301 | 41.737 | +0.29% | -0.09% | 7.32x | 8.7 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31117 | 55.395 | 59.025 | +0.61% | -0.02% | 0.65x | 0.5 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04858 | 42.772 | 45.803 | +0.89% | -0.06% | 0.73x | 2.1 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | AUD/USD | 0.66428 | 39.366 | 43.809 | +0.26% | -0.04% | 0.58x | 3.0 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.54e-05 | 35.824 | 40.783 | +4.44% | +0.31% | 0.35x | 44.2 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | WEAK 33/100 | EXTREME 97/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.0161 | 30.893 | 38.518 | +2.88% | -0.68% | 0.58x | 24.9 | 2026-11-24T20:37:19.440547+00:00 | Not calibrated | WEAK 10/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 69.997 | 499.63 | +0.03% | 0.74x |
| 2 | GBP/USD | 59.025 | 1.31117 | -0.02% | 0.65x |
| 3 | NIGHT/USD | 45.803 | 0.04858 | -0.06% | 0.73x |
| 4 | AUD/USD | 43.809 | 0.66428 | -0.04% | 0.58x |
| 5 | PEPE/USD | 41.737 | 3.432e-06 | -0.09% | 7.32x |
| 6 | LUNA/USD | 40.783 | 4.54e-05 | +0.31% | 0.35x |
| 7 | 2Z/USD | 38.518 | 0.0161 | -0.68% | 0.58x |

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

- Persisted scans: 1623; predictions: 13924; observations: 983499.
- Matured sampled outcomes across 1/6/24/48h: 28418; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45482235473 · **Generation:** 1623 · **Legacy run:** 45482235473
**Main quote time:** 2026-11-24T20:37:23.334347+00:00 · **Legacy report time:** 2026-11-24T20:38:36.517509+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 499.63 | 67.49 | +0.03% | 0.74x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 2 | PEPE/USD | 3.432e-06 | 56.30 | -0.09% | 7.32x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | GBP/USD | 1.31117 | 55.40 | -0.02% | 0.65x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | NIGHT/USD | 0.04858 | 42.77 | -0.06% | 0.73x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | AUD/USD | 0.66428 | 39.37 | -0.04% | 0.58x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | LUNA/USD | 4.54e-05 | 35.82 | +0.31% | 0.35x | WEAK 33/100 | EXTREME 97/100 | Do nothing |
| 7 | 2Z/USD | 0.0161 | 30.89 | -0.68% | 0.58x | WEAK 10/100 | EXTREME 100/100 | Do nothing |

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
