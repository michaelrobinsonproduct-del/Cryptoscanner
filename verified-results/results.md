# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:01:05.247181+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45000693407
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 0d37583390b03611dfdc323fa89eb171fe8e9d2c (atomic ledger/results publication)
**Ledger generation:** 1254 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.013545 | 69.606 | 65.365 | +9.81% | +2.21% | 0.32x | 39.9 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | ZEC/USD | 784.27 | 67.629 | 59.276 | +0.78% | +0.25% | 1.71x | 2.4 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | TAO/USD | 186.455 | 59.338 | 54.516 | +0.39% | +0.23% | 1.37x | 6.2 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 24.968 | 52.660 | 53.111 | +0.27% | -0.36% | 1.14x | 7.6 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.0448 | 44.243 | 47.526 | +1.17% | +0.31% | 0.51x | 11.2 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ORCA/USD | 1.228 | 43.407 | 39.697 | +2.25% | -0.16% | 1.45x | 16.3 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.9715 | 40.753 | 37.301 | +1.19% | +0.51% | 1.09x | 25.9 | 2026-11-22T08:01:01.081565+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 65.365 | 0.013545 | +2.21% | 0.32x |
| 2 | ZEC/USD | 59.276 | 784.27 | +0.25% | 1.71x |
| 3 | TAO/USD | 54.516 | 186.455 | +0.23% | 1.37x |
| 4 | VVV/USD | 53.111 | 24.968 | -0.36% | 1.14x |
| 5 | NIGHT/USD | 47.526 | 0.0448 | +0.31% | 0.51x |
| 6 | ORCA/USD | 39.697 | 1.228 | -0.16% | 1.45x |
| 7 | PEARL/USD | 37.301 | 1.9715 | +0.51% | 1.09x |

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

- Persisted scans: 1254; predictions: 9981; observations: 758796.
- Matured sampled outcomes across 1/6/24/48h: 14359; gap abstentions: 22077. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45000693407 · **Generation:** 1254 · **Legacy run:** 45000693407
**Main quote time:** 2026-11-22T08:01:05.247181+00:00 · **Legacy report time:** 2026-11-22T08:01:51.141175+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.013545 | 69.61 | +2.21% | 0.32x | MODERATE 50/100 | VERY_HIGH 82/100 | Watch |
| 2 | ZEC/USD ⭐ | 784.27 | 67.63 | +0.25% | 1.71x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 186.455 | 59.34 | +0.23% | 1.37x | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD | 24.968 | 52.66 | -0.36% | 1.14x | WEAK 36/100 | HIGH 68/100 | Watch |
| 5 | NIGHT/USD | 0.0448 | 44.24 | +0.31% | 0.51x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 6 | ORCA/USD | 1.228 | 43.41 | -0.16% | 1.45x | WEAK 37/100 | VERY_HIGH 72/100 | Watch |
| 7 | PEARL/USD ⭐ | 1.9715 | 40.75 | +0.51% | 1.09x | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.8871 | 84.87 | +2.76% | 2.04x | 2637 | STRONG 82/100 | VERY_HIGH 82/100 | Watch |
| 2 | ZEC/USD ⭐ | 784.16 | 56.92 | +0.25% | 1.71x | 29035 | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 3 | PEARL/USD ⭐ | 1.9717 | 45.46 | +0.51% | 1.09x | 8364 | MODERATE 58/100 | VERY_HIGH 74/100 | Watch |
| 4 | TAO/USD ⭐ | 186.4514 | 45.36 | +0.23% | 1.37x | 7007 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, TAO/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
