# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:10:18.073370+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44418261754
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 469be42f1192299f3e4acf5d2fbde52fb9d32350 (atomic ledger/results publication)
**Ledger generation:** 691 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05554 | 87.316 | 65.380 | +7.55% | +1.39% | 5.01x | 21.6 | 2026-11-18T23:10:13.162058+00:00 | Not calibrated | STRONG 89/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04528 | 43.740 | 44.916 | +0.87% | +1.14% | 0.31x | 11.1 | 2026-11-18T23:10:13.162058+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | AKE/USD | 0.01011786 | 43.081 | 31.392 | +1.34% | -0.66% | 3.27x | 24.9 | 2026-11-18T23:10:13.162058+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.235e-05 | 28.294 | 29.486 | +1.68% | -0.56% | 1.16x | 28.1 | 2026-11-18T23:10:13.162058+00:00 | Not calibrated | WEAK 14/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 65.380 | 0.05554 | +1.39% | 5.01x |
| 2 | NIGHT/USD | 44.916 | 0.04528 | +1.14% | 0.31x |
| 3 | AKE/USD | 31.392 | 0.01011786 | -0.66% | 3.27x |
| 4 | LUNA/USD | 29.486 | 4.235e-05 | -0.56% | 1.16x |

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

- Persisted scans: 691; predictions: 5609; observations: 417826.
- Matured sampled outcomes across 1/6/24/48h: 5446; gap abstentions: 13194. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44418261754 · **Generation:** 691 · **Legacy run:** 44418261754
**Main quote time:** 2026-11-18T23:10:18.073370+00:00 · **Legacy report time:** 2026-11-18T23:10:59.649985+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05554 | 87.32 | +1.39% | 5.01x | STRONG 99/100 | VERY_HIGH 79/100 | Watch |
| 2 | NIGHT/USD | 0.04528 | 43.74 | +1.14% | 0.31x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 3 | AKE/USD | 0.01011786 | 43.08 | -0.66% | 3.27x | WEAK 42/100 | VERY_HIGH 78/100 | Watch |
| 4 | LUNA/USD | 4.235e-05 | 28.29 | -0.56% | 1.16x | WEAK 14/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05554 | 71.50 | +1.39% | 5.01x | 1275 | STRONG 96/100 | VERY_HIGH 73/100 | Watch |
| 2 | AKT/USD | 0.5104 | 36.56 | +0.97% | 15.71x | 4088 | MODERATE 68/100 | HIGH 66/100 | Watch |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
