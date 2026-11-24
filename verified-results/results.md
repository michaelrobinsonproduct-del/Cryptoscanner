# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T13:31:43.156958+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45403972887
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5895304d1278cebadd1287d71a42fa5f73a8280d (atomic ledger/results publication)
**Ledger generation:** 1580 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.515 | 85.602 | 81.037 | +4.36% | +0.33% | 1.29x | 9.0 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MON/USD | 0.01227 | 76.546 | 83.084 | +6.51% | -0.57% | 0.63x | 8.1 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XMR/USD | 496.68 | 70.359 | 64.608 | +2.19% | +0.30% | 1.42x | 11.5 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3304 | 63.676 | 65.781 | +6.89% | +0.30% | 0.64x | 24.3 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | GBP/USD | 1.30946 | 53.412 | 58.259 | +0.48% | -0.02% | 0.53x | 0.2 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04852 | 43.289 | 50.460 | +0.77% | -0.53% | 0.55x | 6.2 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.01592 | 41.027 | 39.686 | +1.73% | +0.38% | 0.94x | 6.3 | 2026-11-24T13:31:38.595506+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 83.084 | 0.01227 | -0.57% | 0.63x |
| 2 | VVV/USD | 81.037 | 25.515 | +0.33% | 1.29x |
| 3 | ICNT/USD | 65.781 | 0.3304 | +0.30% | 0.64x |
| 4 | XMR/USD | 64.608 | 496.68 | +0.30% | 1.42x |
| 5 | GBP/USD | 58.259 | 1.30946 | -0.02% | 0.53x |
| 6 | NIGHT/USD | 50.460 | 0.04852 | -0.53% | 0.55x |
| 7 | 2Z/USD | 39.686 | 0.01592 | +0.38% | 0.94x |

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

- Persisted scans: 1580; predictions: 13625; observations: 957317.
- Matured sampled outcomes across 1/6/24/48h: 26628; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45403972887 · **Generation:** 1580 · **Legacy run:** 45403972887
**Main quote time:** 2026-11-24T13:31:43.156958+00:00 · **Legacy report time:** 2026-11-24T13:32:31.643633+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.515 | 85.60 | +0.33% | 1.29x | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | MON/USD | 0.01227 | 76.55 | -0.57% | 0.63x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 3 | XMR/USD ⭐ | 496.68 | 70.36 | +0.30% | 1.42x | STRONG 85/100 | HIGH 61/100 | Watch |
| 4 | ICNT/USD | 0.3304 | 63.68 | +0.30% | 0.64x | MODERATE 52/100 | EXTREME 87/100 | Do nothing |
| 5 | GBP/USD | 1.30946 | 53.41 | -0.02% | 0.53x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | NIGHT/USD | 0.04852 | 43.29 | -0.53% | 0.55x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | 2Z/USD | 0.01592 | 41.03 | +0.38% | 0.94x | MODERATE 51/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.439 | 87.15 | +0.33% | 1.29x | 14689 | STRONG 89/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 495 | 61.78 | +0.30% | 1.42x | 11127 | STRONG 81/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
