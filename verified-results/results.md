# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T19:36:58.738348+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45471661410
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 65f47e0da631204b90739d72c7abc2d10366435e (atomic ledger/results publication)
**Ledger generation:** 1617 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 2Z/USD | 0.01649 | 68.504 | 59.318 | +5.37% | +0.30% | 1.77x | 18.1 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | XMR/USD | 500.56 | 65.916 | 74.343 | +2.99% | -0.23% | 0.27x | 3.2 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | VVV/USD | 24.821 | 63.961 | 61.441 | +1.53% | -0.48% | 1.49x | 8.5 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.621e-05 | 59.556 | 66.260 | +6.30% | +0.02% | 0.32x | 19.5 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | ZEUS/USD | 0.0047 | 55.855 | 55.199 | +7.31% | -2.87% | 6.38x | 42.7 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | WEAK 43/100 | EXTREME 99/100 | Do nothing | WATCH |
| 6 | GBP/USD | 1.3111 | 52.984 | 59.102 | +0.60% | -0.02% | 0.40x | 0.2 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | PEPE/USD | 3.436e-06 | 50.468 | 43.438 | +0.41% | -0.52% | 1.96x | 5.8 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04868 | 37.197 | 47.376 | +1.10% | -0.29% | 0.13x | 2.1 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | AUD/USD | 0.66459 | 36.961 | 44.378 | +0.30% | -0.05% | 0.29x | 1.4 | 2026-11-24T19:36:54.355097+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.343 | 500.56 | -0.23% | 0.27x |
| 2 | LUNA/USD | 66.260 | 4.621e-05 | +0.02% | 0.32x |
| 3 | VVV/USD | 61.441 | 24.821 | -0.48% | 1.49x |
| 4 | 2Z/USD | 59.318 | 0.01649 | +0.30% | 1.77x |
| 5 | GBP/USD | 59.102 | 1.3111 | -0.02% | 0.40x |
| 6 | ZEUS/USD | 55.199 | 0.0047 | -2.87% | 6.38x |
| 7 | NIGHT/USD | 47.376 | 0.04868 | -0.29% | 0.13x |
| 8 | AUD/USD | 44.378 | 0.66459 | -0.05% | 0.29x |
| 9 | PEPE/USD | 43.438 | 3.436e-06 | -0.52% | 1.96x |

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

- Persisted scans: 1617; predictions: 13882; observations: 979845.
- Matured sampled outcomes across 1/6/24/48h: 28168; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45471661410 · **Generation:** 1617 · **Legacy run:** 45471661410
**Main quote time:** 2026-11-24T19:36:58.738348+00:00 · **Legacy report time:** 2026-11-24T19:38:12.006361+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD ⭐ | 0.01649 | 68.50 | +0.30% | 1.77x | STRONG 84/100 | VERY_HIGH 73/100 | Watch |
| 2 | XMR/USD | 500.56 | 65.92 | -0.23% | 0.27x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 3 | VVV/USD | 24.821 | 63.96 | -0.48% | 1.49x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 4 | LUNA/USD | 4.621e-05 | 59.56 | +0.02% | 0.32x | MODERATE 45/100 | VERY_HIGH 81/100 | Watch |
| 5 | ZEUS/USD | 0.0047 | 55.85 | -2.87% | 6.38x | WEAK 43/100 | EXTREME 99/100 | Do nothing |
| 6 | GBP/USD | 1.3111 | 52.98 | -0.02% | 0.40x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | PEPE/USD | 3.436e-06 | 50.47 | -0.52% | 1.96x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 8 | NIGHT/USD | 0.04868 | 37.20 | -0.29% | 0.13x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | AUD/USD | 0.66459 | 36.96 | -0.05% | 0.29x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD ⭐ | 0.01649 | 64.67 | +0.30% | 1.77x | 1464 | STRONG 77/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
