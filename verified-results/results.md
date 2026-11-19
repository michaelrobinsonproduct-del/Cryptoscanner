# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:40:28.136233+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44438552201
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 2bd69dd9ed68d8e8918a04e89765dbe9a8ec472d (atomic ledger/results publication)
**Ledger generation:** 721 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021542 | 66.609 | 59.119 | +4.55% | +1.36% | 1.07x | 8.4 | 2026-11-19T01:40:22.162943+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.0574 | 47.793 | 40.863 | +2.50% | +0.16% | 1.61x | 15.7 | 2026-11-19T01:40:22.162943+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | DRV/USD | 0.266 | 44.395 | 31.473 | +0.49% | -0.42% | 4.22x | 10.5 | 2026-11-19T01:40:22.162943+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | TRX/USD | 0.310213 | 37.775 | 39.894 | +0.30% | -0.01% | 0.80x | 1.5 | 2026-11-19T01:40:22.162943+00:00 | Not calibrated | WEAK 24/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | PYTH/USD | 0.05337 | 22.993 | 31.377 | +1.16% | +0.13% | 0.10x | 16.8 | 2026-11-19T01:40:22.162943+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 6 | BAT/USD | 0.09327 | 21.397 | 20.556 | +0.27% | +0.20% | 0.98x | 24.7 | 2026-11-19T01:40:22.162943+00:00 | Not calibrated | WEAK 31/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 59.119 | 0.021542 | +1.36% | 1.07x |
| 2 | MEGA/USD | 40.863 | 0.0574 | +0.16% | 1.61x |
| 3 | TRX/USD | 39.894 | 0.310213 | -0.01% | 0.80x |
| 4 | DRV/USD | 31.473 | 0.266 | -0.42% | 4.22x |
| 5 | PYTH/USD | 31.377 | 0.05337 | +0.13% | 0.10x |
| 6 | BAT/USD | 20.556 | 0.09327 | +0.20% | 0.98x |

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

- Persisted scans: 721; predictions: 5846; observations: 436096.
- Matured sampled outcomes across 1/6/24/48h: 5762; gap abstentions: 13458. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44438552201 · **Generation:** 721 · **Legacy run:** 44438552201
**Main quote time:** 2026-11-19T01:40:28.136233+00:00 · **Legacy report time:** 2026-11-19T01:41:02.562935+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021542 | 66.61 | +1.36% | 1.07x | STRONG 78/100 | VERY_HIGH 74/100 | Watch |
| 2 | MEGA/USD ⭐ | 0.0574 | 47.79 | +0.16% | 1.61x | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |
| 3 | DRV/USD | 0.266 | 44.39 | -0.42% | 4.22x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |
| 4 | TRX/USD | 0.310213 | 37.78 | -0.01% | 0.80x | WEAK 24/100 | HIGH 68/100 | Do nothing |
| 5 | PYTH/USD | 0.05337 | 22.99 | +0.13% | 0.10x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 6 | BAT/USD | 0.09327 | 21.40 | +0.20% | 0.98x | WEAK 31/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021538 | 75.38 | +1.36% | 1.07x | 7453 | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 2 | MEGA/USD ⭐ | 0.0574 | 44.83 | +0.16% | 1.61x | 1341 | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
