# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T20:50:49.656520+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45483938384
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e2bcf764241e51e8bd3ef92f9f89d9e8633eafd6 (atomic ledger/results publication)
**Ledger generation:** 1624 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.59e-05 | 81.144 | 67.720 | +5.59% | +1.17% | 1.76x | 6.5 | 2026-11-24T20:50:45.634925+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 499.17 | 66.931 | 71.035 | +2.71% | -0.07% | 0.62x | 5.8 | 2026-11-24T20:50:45.634925+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31072 | 55.451 | 58.974 | +0.57% | -0.03% | 0.66x | 0.1 | 2026-11-24T20:50:45.634925+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.467e-06 | 53.632 | 50.558 | +1.31% | +0.76% | 0.93x | 5.8 | 2026-11-24T20:50:45.634925+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04871 | 47.963 | 45.649 | +1.16% | +0.31% | 1.08x | 6.2 | 2026-11-24T20:50:45.634925+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.01625 | 47.790 | 48.434 | +3.83% | +0.62% | 0.63x | 18.5 | 2026-11-24T20:50:45.634925+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 71.035 | 499.17 | -0.07% | 0.62x |
| 2 | LUNA/USD | 67.720 | 4.59e-05 | +1.17% | 1.76x |
| 3 | GBP/USD | 58.974 | 1.31072 | -0.03% | 0.66x |
| 4 | PEPE/USD | 50.558 | 3.467e-06 | +0.76% | 0.93x |
| 5 | 2Z/USD | 48.434 | 0.01625 | +0.62% | 0.63x |
| 6 | NIGHT/USD | 45.649 | 0.04871 | +0.31% | 1.08x |

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

- Persisted scans: 1624; predictions: 13930; observations: 984108.
- Matured sampled outcomes across 1/6/24/48h: 28468; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45483938384 · **Generation:** 1624 · **Legacy run:** 45483938384
**Main quote time:** 2026-11-24T20:50:49.656520+00:00 · **Legacy report time:** 2026-11-24T20:51:40.995455+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.59e-05 | 81.14 | +1.17% | 1.76x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 2 | XMR/USD | 499.17 | 66.93 | -0.07% | 0.62x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 3 | GBP/USD | 1.31072 | 55.45 | -0.03% | 0.66x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | PEPE/USD | 3.467e-06 | 53.63 | +0.76% | 0.93x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.04871 | 47.96 | +0.31% | 1.08x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 6 | 2Z/USD | 0.01625 | 47.79 | +0.62% | 0.63x | MODERATE 49/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.59e-05 | 73.30 | +1.17% | 1.76x | 1886 | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04883 | 53.36 | +0.31% | 1.08x | 9295 | STRONG 72/100 | HIGH 62/100 | Watch |
| 3 | SKY/USD | 0.04057 | 33.85 | +0.75% | 1.46x | 4337 | MODERATE 62/100 | HIGH 60/100 | Watch |

**Same-run overlap:** LUNA/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
