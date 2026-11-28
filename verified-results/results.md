# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T14:33:18.655002+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46154919527
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 994e297cf0bf455fca294277c61c3512e9c556d0 (atomic ledger/results publication)
**Ledger generation:** 2166 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05379 | 88.255 | 93.497 | +7.07% | -0.74% | 0.84x | 13.0 | 2026-11-28T14:33:15.430556+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | XMR/USD | 429.58 | 88.228 | 87.869 | +5.48% | -0.19% | 1.13x | 11.0 | 2026-11-28T14:33:15.430556+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | VVV/USD | 26.775 | 62.829 | 66.358 | +3.98% | +0.60% | 0.35x | 9.7 | 2026-11-28T14:33:15.430556+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.751e-05 | 59.148 | 59.732 | +4.21% | +1.01% | 0.44x | 2.1 | 2026-11-28T14:33:15.430556+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024507 | 39.089 | 36.341 | +3.34% | +0.75% | 0.90x | 37.2 | 2026-11-28T14:33:15.430556+00:00 | Not calibrated | WEAK 35/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 93.497 | 0.05379 | -0.74% | 0.84x |
| 2 | XMR/USD | 87.869 | 429.58 | -0.19% | 1.13x |
| 3 | VVV/USD | 66.358 | 26.775 | +0.60% | 0.35x |
| 4 | LUNA/USD | 59.732 | 4.751e-05 | +1.01% | 0.44x |
| 5 | SENT/USD | 36.341 | 0.024507 | +0.75% | 0.90x |

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

- Persisted scans: 2166; predictions: 19258; observations: 1311642.
- Matured sampled outcomes across 1/6/24/48h: 46309; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46154919527 · **Generation:** 2166 · **Legacy run:** 46154919527
**Main quote time:** 2026-11-28T14:33:18.655002+00:00 · **Legacy report time:** 2026-11-28T14:34:16.413496+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05379 | 88.25 | -0.74% | 0.84x | WEAK 44/100 | VERY_HIGH 74/100 | Watch |
| 2 | XMR/USD | 429.58 | 88.23 | -0.19% | 1.13x | MODERATE 49/100 | VERY_HIGH 74/100 | Watch |
| 3 | VVV/USD | 26.775 | 62.83 | +0.60% | 0.35x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 4 | LUNA/USD | 4.751e-05 | 59.15 | +1.01% | 0.44x | MODERATE 60/100 | VERY_HIGH 82/100 | Watch |
| 5 | SENT/USD | 0.024507 | 39.09 | +0.75% | 0.90x | WEAK 35/100 | EXTREME 86/100 | Do nothing |

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
