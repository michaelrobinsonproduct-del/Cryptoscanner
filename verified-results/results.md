# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T21:22:27.642200+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45489944959
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 78ac699229aa0f76e3489f3cdf5b126186990932 (atomic ledger/results publication)
**Ledger generation:** 1627 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 499.93 | 70.270 | 70.527 | +2.86% | +0.05% | 0.95x | 9.0 | 2026-11-24T21:22:23.244995+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31104 | 61.538 | 59.070 | +0.60% | +0.02% | 1.24x | 0.2 | 2026-11-24T21:22:23.244995+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.476e-06 | 48.489 | 52.486 | +1.58% | +0.43% | 0.38x | 5.8 | 2026-11-24T21:22:23.244995+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AUD/USD | 0.66425 | 42.949 | 44.090 | +0.25% | -0.04% | 0.91x | 2.3 | 2026-11-24T21:22:23.244995+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.04831 | 37.157 | 40.690 | +0.33% | -0.21% | 0.75x | 4.1 | 2026-11-24T21:22:23.244995+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 70.527 | 499.93 | +0.05% | 0.95x |
| 2 | GBP/USD | 59.070 | 1.31104 | +0.02% | 1.24x |
| 3 | PEPE/USD | 52.486 | 3.476e-06 | +0.43% | 0.38x |
| 4 | AUD/USD | 44.090 | 0.66425 | -0.04% | 0.91x |
| 5 | NIGHT/USD | 40.690 | 0.04831 | -0.21% | 0.75x |

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

- Persisted scans: 1627; predictions: 13949; observations: 985935.
- Matured sampled outcomes across 1/6/24/48h: 28593; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45489944959 · **Generation:** 1627 · **Legacy run:** 45489944959
**Main quote time:** 2026-11-24T21:22:27.642200+00:00 · **Legacy report time:** 2026-11-24T21:23:40.766748+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 499.93 | 70.27 | +0.05% | 0.95x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 2 | GBP/USD | 1.31104 | 61.54 | +0.02% | 1.24x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 3 | PEPE/USD | 3.476e-06 | 48.49 | +0.43% | 0.38x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 4 | AUD/USD | 0.66425 | 42.95 | -0.04% | 0.91x | WEAK 26/100 | HIGH 68/100 | Do nothing |
| 5 | NIGHT/USD | 0.04831 | 37.16 | -0.21% | 0.75x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

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
