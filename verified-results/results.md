# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:15:27.823644+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44435393307
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e13f16120aaf0e2afb79d8e703c92f3302e069eb (atomic ledger/results publication)
**Ledger generation:** 716 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 192.4548 | 67.430 | 54.005 | +0.26% | -0.31% | 2.81x | 5.6 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.486e-05 | 59.105 | 50.036 | +3.03% | +0.42% | 1.69x | 6.7 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021335 | 58.564 | 55.981 | +3.54% | +0.04% | 1.24x | 0.5 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.3067 | 57.081 | 54.855 | +0.28% | -0.46% | 1.45x | 4.2 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1781.57 | 55.415 | 57.658 | +0.38% | +0.07% | 0.74x | 0.1 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | BNB/USD | 583.51 | 55.383 | 40.306 | +0.38% | +0.02% | 2.82x | 1.5 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | AAVE/USD | 109.74 | 52.951 | 39.269 | +0.46% | -0.26% | 5.99x | 4.6 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LTC/USD | 44.22 | 49.961 | 48.317 | +0.48% | +0.02% | 1.15x | 2.3 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PAXG/USD | 3742.44 | 49.926 | 44.074 | +0.30% | -0.07% | 1.62x | 0.9 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ENA/USD | 0.112 | 47.309 | 34.458 | +0.27% | +0.09% | 2.24x | 17.9 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SHIB/USD | 3.81e-06 | 35.827 | 31.128 | +0.42% | -0.13% | 1.54x | 7.9 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | WEAK 38/100 | HIGH 66/100 | Watch | WATCH |
| 12 | TRX/USD | 0.310448 | 35.307 | 41.093 | +0.38% | -0.05% | 0.45x | 0.0 | 2026-11-19T01:15:19.694056+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ETH/USD | 57.658 | 1781.57 | +0.07% | 0.74x |
| 2 | SENT/USD | 55.981 | 0.021335 | +0.04% | 1.24x |
| 3 | NEAR/USD | 54.855 | 3.3067 | -0.46% | 1.45x |
| 4 | TAO/USD | 54.005 | 192.4548 | -0.31% | 2.81x |
| 5 | LUNA/USD | 50.036 | 4.486e-05 | +0.42% | 1.69x |
| 6 | LTC/USD | 48.317 | 44.22 | +0.02% | 1.15x |
| 7 | PAXG/USD | 44.074 | 3742.44 | -0.07% | 1.62x |
| 8 | TRX/USD | 41.093 | 0.310448 | -0.05% | 0.45x |
| 9 | BNB/USD | 40.306 | 583.51 | +0.02% | 2.82x |
| 10 | AAVE/USD | 39.269 | 109.74 | -0.26% | 5.99x |
| 11 | ENA/USD | 34.458 | 0.112 | +0.09% | 2.24x |
| 12 | SHIB/USD | 31.128 | 3.81e-06 | -0.13% | 1.54x |

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

- Persisted scans: 716; predictions: 5817; observations: 433051.
- Matured sampled outcomes across 1/6/24/48h: 5694; gap abstentions: 13438. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44435393307 · **Generation:** 716 · **Legacy run:** 44435393307
**Main quote time:** 2026-11-19T01:15:27.823644+00:00 · **Legacy report time:** 2026-11-19T01:16:12.366750+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 192.4548 | 67.43 | -0.31% | 2.81x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.486e-05 | 59.10 | +0.42% | 1.69x | STRONG 85/100 | HIGH 60/100 | Consider small entry |
| 3 | SENT/USD | 0.021335 | 58.56 | +0.04% | 1.24x | MODERATE 54/100 | VERY_HIGH 74/100 | Watch |
| 4 | NEAR/USD | 3.3067 | 57.08 | -0.46% | 1.45x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1781.57 | 55.41 | +0.07% | 0.74x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 6 | BNB/USD | 583.51 | 55.38 | +0.02% | 2.82x | STRONG 73/100 | HIGH 55/100 | Watch |
| 7 | AAVE/USD | 109.74 | 52.95 | -0.26% | 5.99x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 8 | LTC/USD | 44.22 | 49.96 | +0.02% | 1.15x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | PAXG/USD | 3742.44 | 49.93 | -0.07% | 1.62x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 10 | ENA/USD | 0.112 | 47.31 | +0.09% | 2.24x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 11 | SHIB/USD | 3.81e-06 | 35.83 | -0.13% | 1.54x | WEAK 38/100 | HIGH 66/100 | Watch |
| 12 | TRX/USD | 0.310448 | 35.31 | -0.05% | 0.45x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD | 0.687 | 65.95 | +2.09% | 3.07x | 2392 | STRONG 73/100 | VERY_HIGH 79/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.486e-05 | 57.55 | +0.42% | 1.69x | 1899 | STRONG 74/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
