# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:35:15.841372+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44371210163
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** f1278582184c86be0cff8fe1cf4502e09bb5cbe5 (atomic ledger/results publication)
**Ledger generation:** 637 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019935 | 66.059 | 73.337 | +6.78% | -0.29% | 0.42x | 5.5 | 2026-11-18T18:35:12.075014+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | NIGHT/USD | 0.04515 | 49.601 | 47.727 | +0.58% | +0.07% | 1.15x | 8.9 | 2026-11-18T18:35:12.075014+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3854 | 45.847 | 49.364 | +3.24% | +0.36% | 0.47x | 10.4 | 2026-11-18T18:35:12.075014+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05338 | 45.761 | 47.225 | +3.37% | +0.26% | 0.72x | 15.0 | 2026-11-18T18:35:12.075014+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | SPACE/USD | 0.003356 | 31.628 | 29.007 | +0.39% | +1.67% | 0.43x | 8.9 | 2026-11-18T18:35:12.075014+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.337 | 0.019935 | -0.29% | 0.42x |
| 2 | MNT/USD | 49.364 | 0.3854 | +0.36% | 0.47x |
| 3 | NIGHT/USD | 47.727 | 0.04515 | +0.07% | 1.15x |
| 4 | MEGA/USD | 47.225 | 0.05338 | +0.26% | 0.72x |
| 5 | SPACE/USD | 29.007 | 0.003356 | +1.67% | 0.43x |

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

- Persisted scans: 637; predictions: 5409; observations: 384940.
- Matured sampled outcomes across 1/6/24/48h: 4718; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44371210163 · **Generation:** 637 · **Legacy run:** 44371210163
**Main quote time:** 2026-11-18T18:35:15.841372+00:00 · **Legacy report time:** 2026-11-18T18:35:40.505729+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019935 | 66.06 | -0.29% | 0.42x | WEAK 38/100 | EXTREME 88/100 | Do nothing |
| 2 | NIGHT/USD ⭐ | 0.04515 | 49.60 | +0.07% | 1.15x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 3 | MNT/USD | 0.3854 | 45.85 | +0.36% | 0.47x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 4 | MEGA/USD | 0.05338 | 45.76 | +0.26% | 0.72x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 5 | SPACE/USD | 0.003356 | 31.63 | +1.67% | 0.43x | MODERATE 46/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04515 | 42.33 | +0.07% | 1.15x | 15859 | MODERATE 56/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
