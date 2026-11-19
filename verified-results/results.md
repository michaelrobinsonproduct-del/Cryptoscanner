# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:55:23.761061+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44468376415
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** cd51bf4a0c5d0fdf3eeab7dafca7ebc3edef8b40 (atomic ledger/results publication)
**Ledger generation:** 770 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.692 | 87.386 | 85.332 | +4.71% | +0.47% | 0.97x | 4.8 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ZEC/USD | 937.42 | 83.558 | 72.684 | +2.79% | +0.26% | 1.96x | 3.7 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 194.8394 | 79.936 | 63.232 | +1.50% | +0.34% | 6.55x | 4.5 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.7224 | 73.409 | 57.716 | +0.49% | +0.14% | 19.74x | 1.4 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | TRX/USD | 0.311985 | 63.315 | 47.707 | +0.87% | +0.12% | 27.86x | 0.0 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.3761 | 63.236 | 69.338 | +2.39% | +0.07% | 0.35x | 4.7 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ADA/USD | 0.152752 | 59.715 | 61.049 | +0.99% | +0.23% | 0.75x | 1.8 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 8 | HYPE/USD | 67.91 | 59.172 | 65.044 | +1.54% | +0.10% | 0.36x | 1.5 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1796.48 | 58.645 | 63.539 | +1.22% | +0.01% | 0.51x | 0.1 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 74.53 | 57.539 | 63.752 | +1.35% | +0.05% | 0.35x | 1.3 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 63245.8 | 54.939 | 57.896 | +0.41% | -0.07% | 0.74x | 0.0 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SENT/USD | 0.022054 | 54.440 | 70.415 | +7.03% | -2.35% | 0.58x | 13.6 | 2026-11-19T05:55:16.202307+00:00 | Not calibrated | WEAK 27/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 85.332 | 22.692 | +0.47% | 0.97x |
| 2 | ZEC/USD | 72.684 | 937.42 | +0.26% | 1.96x |
| 3 | SENT/USD | 70.415 | 0.022054 | -2.35% | 0.58x |
| 4 | NEAR/USD | 69.338 | 3.3761 | +0.07% | 0.35x |
| 5 | HYPE/USD | 65.044 | 67.91 | +0.10% | 0.36x |
| 6 | SOL/USD | 63.752 | 74.53 | +0.05% | 0.35x |
| 7 | ETH/USD | 63.539 | 1796.48 | +0.01% | 0.51x |
| 8 | TAO/USD | 63.232 | 194.8394 | +0.34% | 6.55x |
| 9 | ADA/USD | 61.049 | 0.152752 | +0.23% | 0.75x |
| 10 | XBT/USD | 57.896 | 63245.8 | -0.07% | 0.74x |
| 11 | SUI/USD | 57.716 | 0.7224 | +0.14% | 19.74x |
| 12 | TRX/USD | 47.707 | 0.311985 | +0.12% | 27.86x |

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

- Persisted scans: 770; predictions: 6384; observations: 465936.
- Matured sampled outcomes across 1/6/24/48h: 6415; gap abstentions: 13796. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44468376415 · **Generation:** 770 · **Legacy run:** 44468376415
**Main quote time:** 2026-11-19T05:55:23.761061+00:00 · **Legacy report time:** 2026-11-19T05:56:14.359791+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.692 | 87.39 | +0.47% | 0.97x | STRONG 74/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 937.42 | 83.56 | +0.26% | 1.96x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD | 194.8394 | 79.94 | +0.34% | 6.55x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD | 0.7224 | 73.41 | +0.14% | 19.74x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | TRX/USD | 0.311985 | 63.31 | +0.12% | 27.86x | STRONG 77/100 | HIGH 55/100 | Watch |
| 6 | NEAR/USD | 3.3761 | 63.24 | +0.07% | 0.35x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 7 | ADA/USD | 0.152752 | 59.72 | +0.23% | 0.75x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 8 | HYPE/USD | 67.91 | 59.17 | +0.10% | 0.36x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1796.48 | 58.64 | +0.01% | 0.51x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 74.53 | 57.54 | +0.05% | 0.35x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 63245.8 | 54.94 | -0.07% | 0.74x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SENT/USD | 0.022054 | 54.44 | -2.35% | 0.58x | WEAK 27/100 | EXTREME 91/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 937.61 | 83.55 | +0.26% | 1.96x | 22306 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
