# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T09:11:45.596016+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45362518952
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f8e1aed2d5be4aea48e51ce9b413b4398d2be0b4 (atomic ledger/results publication)
**Ledger generation:** 1554 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01278 | 66.346 | 78.906 | +10.94% | -1.16% | 0.32x | 15.6 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | WEAK 33/100 | EXTREME 86/100 | Do nothing | WATCH |
| 2 | VVV/USD | 24.847 | 66.285 | 60.581 | +1.63% | -1.14% | 2.14x | 11.7 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.604e-05 | 59.991 | 63.667 | +5.91% | +0.35% | 0.46x | 19.5 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.48e-06 | 58.611 | 59.413 | +1.69% | -1.61% | 1.73x | 5.8 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | MODERATE 49/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | BABY/USD | 0.00898 | 58.389 | 66.585 | +5.65% | -0.22% | 0.29x | 11.2 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | WEAK 29/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | XMR/USD | 494.98 | 53.066 | 64.067 | +1.84% | -0.57% | 0.18x | 7.7 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | BAT/USD | 0.07917 | 37.383 | 47.985 | +2.59% | -0.62% | 0.25x | 5.1 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | ATOM/USD | 1.29 | 22.087 | 32.446 | +0.61% | -0.90% | 0.41x | 10.1 | 2026-11-24T09:11:39.370912+00:00 | Not calibrated | WEAK 11/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.906 | 0.01278 | -1.16% | 0.32x |
| 2 | BABY/USD | 66.585 | 0.00898 | -0.22% | 0.29x |
| 3 | XMR/USD | 64.067 | 494.98 | -0.57% | 0.18x |
| 4 | LUNA/USD | 63.667 | 4.604e-05 | +0.35% | 0.46x |
| 5 | VVV/USD | 60.581 | 24.847 | -1.14% | 2.14x |
| 6 | PEPE/USD | 59.413 | 3.48e-06 | -1.61% | 1.73x |
| 7 | BAT/USD | 47.985 | 0.07917 | -0.62% | 0.25x |
| 8 | ATOM/USD | 32.446 | 1.29 | -0.90% | 0.41x |

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

- Persisted scans: 1554; predictions: 13375; observations: 941484.
- Matured sampled outcomes across 1/6/24/48h: 25396; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45362518952 · **Generation:** 1554 · **Legacy run:** 45362518952
**Main quote time:** 2026-11-24T09:11:45.596016+00:00 · **Legacy report time:** 2026-11-24T09:12:57.506476+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01278 | 66.35 | -1.16% | 0.32x | WEAK 33/100 | EXTREME 86/100 | Do nothing |
| 2 | VVV/USD | 24.847 | 66.28 | -1.14% | 2.14x | MODERATE 58/100 | VERY_HIGH 71/100 | Watch |
| 3 | LUNA/USD | 4.604e-05 | 59.99 | +0.35% | 0.46x | MODERATE 55/100 | VERY_HIGH 81/100 | Watch |
| 4 | PEPE/USD | 3.48e-06 | 58.61 | -1.61% | 1.73x | MODERATE 49/100 | HIGH 65/100 | Do nothing |
| 5 | BABY/USD | 0.00898 | 58.39 | -0.22% | 0.29x | WEAK 29/100 | EXTREME 87/100 | Do nothing |
| 6 | XMR/USD | 494.98 | 53.07 | -0.57% | 0.18x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | BAT/USD | 0.07917 | 37.38 | -0.62% | 0.25x | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | ATOM/USD | 1.29 | 22.09 | -0.90% | 0.41x | WEAK 11/100 | EXTREME 87/100 | Do nothing |

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
