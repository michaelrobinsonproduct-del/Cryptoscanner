# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T18:19:05.316595+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45456445299
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8df5cb227784e41e2a5c6806bc32d0b948bfef44 (atomic ledger/results publication)
**Ledger generation:** 1609 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 503.79 | 80.050 | 79.601 | +3.66% | +0.24% | 0.93x | 2.0 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31146 | 70.850 | 59.372 | +0.63% | -0.02% | 2.16x | 0.1 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 25.084 | 63.527 | 69.406 | +2.60% | -0.50% | 0.66x | 7.6 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.433e-06 | 52.368 | 43.373 | +0.32% | +0.29% | 1.75x | 5.8 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LUNA/USD | 4.75e-05 | 52.218 | 72.650 | +9.27% | -2.57% | 0.24x | 8.4 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | WEAK 31/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04833 | 50.626 | 37.483 | +0.37% | -0.37% | 5.70x | 12.4 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 7 | ZEUS/USD | 0.00467 | 49.046 | 54.966 | +6.62% | +0.21% | 0.30x | 42.8 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | WEAK 40/100 | EXTREME 100/100 | Do nothing | WATCH |
| 8 | 2Z/USD | 0.01628 | 38.736 | 49.732 | +4.03% | -0.49% | 0.14x | 18.5 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | AUD/USD | 0.66453 | 35.651 | 44.064 | +0.29% | +0.07% | 0.12x | 1.8 | 2026-11-24T18:18:59.756999+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 79.601 | 503.79 | +0.24% | 0.93x |
| 2 | LUNA/USD | 72.650 | 4.75e-05 | -2.57% | 0.24x |
| 3 | VVV/USD | 69.406 | 25.084 | -0.50% | 0.66x |
| 4 | GBP/USD | 59.372 | 1.31146 | -0.02% | 2.16x |
| 5 | ZEUS/USD | 54.966 | 0.00467 | +0.21% | 0.30x |
| 6 | 2Z/USD | 49.732 | 0.01628 | -0.49% | 0.14x |
| 7 | AUD/USD | 44.064 | 0.66453 | +0.07% | 0.12x |
| 8 | PEPE/USD | 43.373 | 3.433e-06 | +0.29% | 1.75x |
| 9 | NIGHT/USD | 37.483 | 0.04833 | -0.37% | 5.70x |

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

- Persisted scans: 1609; predictions: 13822; observations: 974973.
- Matured sampled outcomes across 1/6/24/48h: 27866; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45456445299 · **Generation:** 1609 · **Legacy run:** 45456445299
**Main quote time:** 2026-11-24T18:19:05.316595+00:00 · **Legacy report time:** 2026-11-24T18:20:03.354602+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 503.79 | 80.05 | +0.24% | 0.93x | STRONG 70/100 | HIGH 62/100 | Watch |
| 2 | GBP/USD | 1.31146 | 70.85 | -0.02% | 2.16x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 25.084 | 63.53 | -0.50% | 0.66x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 4 | PEPE/USD | 3.433e-06 | 52.37 | +0.29% | 1.75x | STRONG 71/100 | HIGH 55/100 | Watch |
| 5 | LUNA/USD | 4.75e-05 | 52.22 | -2.57% | 0.24x | WEAK 31/100 | EXTREME 85/100 | Do nothing |
| 6 | NIGHT/USD ⭐ | 0.04833 | 50.63 | -0.37% | 5.70x | MODERATE 60/100 | HIGH 67/100 | Watch |
| 7 | ZEUS/USD | 0.00467 | 49.05 | +0.21% | 0.30x | WEAK 40/100 | EXTREME 100/100 | Do nothing |
| 8 | 2Z/USD | 0.01628 | 38.74 | -0.49% | 0.14x | WEAK 19/100 | EXTREME 94/100 | Do nothing |
| 9 | AUD/USD | 0.66453 | 35.65 | +0.07% | 0.12x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04839 | 43.76 | +0.37% | 8.18x | 9337 | STRONG 82/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
