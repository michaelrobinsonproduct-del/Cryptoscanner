# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:01:56.949595+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45443489735
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7ef6d43a50bd3e19f295cadd1c021dec4d90a72d (atomic ledger/results publication)
**Ledger generation:** 1601 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.657e-05 | 74.389 | 64.556 | +7.13% | +0.63% | 1.67x | 23.7 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31087 | 71.727 | 58.940 | +0.58% | +0.02% | 2.27x | 0.3 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 24.54 | 55.793 | 53.967 | +0.38% | -0.21% | 1.29x | 7.3 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | WEAK 38/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XMR/USD | 494.63 | 51.245 | 59.108 | +1.77% | -0.30% | 0.36x | 16.6 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | ICNT/USD | 0.3203 | 48.410 | 50.497 | +3.62% | +0.41% | 0.59x | 15.6 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | ZEUS/USD | 0.00482 | 46.943 | 55.467 | +10.05% | -0.41% | 0.35x | 41.7 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | WEAK 13/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.01601 | 40.322 | 40.596 | +2.30% | -0.56% | 1.25x | 12.5 | 2026-11-24T17:01:54.202656+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 64.556 | 4.657e-05 | +0.63% | 1.67x |
| 2 | XMR/USD | 59.108 | 494.63 | -0.30% | 0.36x |
| 3 | GBP/USD | 58.940 | 1.31087 | +0.02% | 2.27x |
| 4 | ZEUS/USD | 55.467 | 0.00482 | -0.41% | 0.35x |
| 5 | VVV/USD | 53.967 | 24.54 | -0.21% | 1.29x |
| 6 | ICNT/USD | 50.497 | 0.3203 | +0.41% | 0.59x |
| 7 | 2Z/USD | 40.596 | 0.01601 | -0.56% | 1.25x |

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

- Persisted scans: 1601; predictions: 13762; observations: 970101.
- Matured sampled outcomes across 1/6/24/48h: 27541; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45443489735 · **Generation:** 1601 · **Legacy run:** 45443489735
**Main quote time:** 2026-11-24T17:01:56.949595+00:00 · **Legacy report time:** 2026-11-24T17:02:48.392856+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.657e-05 | 74.39 | +0.63% | 1.67x | STRONG 82/100 | VERY_HIGH 79/100 | Watch |
| 2 | GBP/USD | 1.31087 | 71.73 | +0.02% | 2.27x | STRONG 81/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 24.54 | 55.79 | -0.21% | 1.29x | WEAK 38/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD | 494.63 | 51.24 | -0.30% | 0.36x | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | ICNT/USD | 0.3203 | 48.41 | +0.41% | 0.59x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 6 | ZEUS/USD | 0.00482 | 46.94 | -0.41% | 0.35x | WEAK 13/100 | EXTREME 100/100 | Do nothing |
| 7 | 2Z/USD | 0.01601 | 40.32 | -0.56% | 1.25x | WEAK 25/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.652e-05 | 65.49 | +0.63% | 1.67x | 1451 | STRONG 83/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
