# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:00:19.048020+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44425332365
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 49c3676adfe5c91966c20a7a8c3e3085824d847a (atomic ledger/results publication)
**Ledger generation:** 701 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05598 | 63.960 | 65.434 | +8.40% | +0.63% | 0.54x | 21.5 | 2026-11-19T00:00:13.564922+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 94/100 | Do nothing | WATCH |
| 2 | TRX/USD | 0.309315 | 57.078 | 42.491 | +0.46% | -0.08% | 4.75x | 1.2 | 2026-11-19T00:00:13.564922+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.378e-05 | 46.231 | 48.318 | +5.11% | -0.43% | 1.01x | 39.0 | 2026-11-19T00:00:13.564922+00:00 | Not calibrated | WEAK 18/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04548 | 44.162 | 48.764 | +1.31% | +0.26% | 0.41x | 8.8 | 2026-11-19T00:00:13.564922+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | MON/USD | 0.0143 | 23.948 | 16.342 | +0.28% | +0.42% | 1.55x | 35.1 | 2026-11-19T00:00:13.564922+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 65.434 | 0.05598 | +0.63% | 0.54x |
| 2 | NIGHT/USD | 48.764 | 0.04548 | +0.26% | 0.41x |
| 3 | LUNA/USD | 48.318 | 4.378e-05 | -0.43% | 1.01x |
| 4 | TRX/USD | 42.491 | 0.309315 | -0.08% | 4.75x |
| 5 | MON/USD | 16.342 | 0.0143 | +0.42% | 1.55x |

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

- Persisted scans: 701; predictions: 5663; observations: 423916.
- Matured sampled outcomes across 1/6/24/48h: 5533; gap abstentions: 13314. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44425332365 · **Generation:** 701 · **Legacy run:** 44425332365
**Main quote time:** 2026-11-19T00:00:19.048020+00:00 · **Legacy report time:** 2026-11-19T00:00:54.169573+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05598 | 63.96 | +0.63% | 0.54x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 2 | TRX/USD | 0.309315 | 57.08 | -0.08% | 4.75x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 3 | LUNA/USD | 4.378e-05 | 46.23 | -0.43% | 1.01x | WEAK 18/100 | EXTREME 85/100 | Do nothing |
| 4 | NIGHT/USD | 0.04548 | 44.16 | +0.26% | 0.41x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 5 | MON/USD ⭐ | 0.0143 | 23.95 | +0.42% | 1.55x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01428 | 20.01 | +0.42% | 1.55x | 1642 | MODERATE 60/100 | HIGH 66/100 | Watch |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
