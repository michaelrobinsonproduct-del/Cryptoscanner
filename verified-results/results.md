# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:10:20.859148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44434740355
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ab931ba18bb4bbec7df877104935c874ec2275d3 (atomic ledger/results publication)
**Ledger generation:** 715 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 192.5279 | 63.033 | 53.128 | +0.30% | +0.10% | 1.94x | 7.9 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ETH/USD | 1784.45 | 60.964 | 58.794 | +0.55% | +0.03% | 1.20x | 0.1 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PAXG/USD | 3744.89 | 59.696 | 44.920 | +0.37% | -0.04% | 5.53x | 0.1 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AAVE/USD | 109.67 | 56.099 | 40.185 | +0.39% | +0.18% | 4.38x | 1.8 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.3126 | 55.384 | 55.356 | +0.46% | -0.34% | 1.17x | 5.7 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 6 | UP/USD | 0.05196 | 54.212 | 57.012 | +4.07% | -0.31% | 0.87x | 7.7 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 7 | HYPE/USD | 67.06 | 51.637 | 55.394 | +0.27% | +0.16% | 0.54x | 3.0 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SENT/USD | 0.021287 | 49.861 | 52.923 | +3.31% | -0.82% | 1.10x | 3.3 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 9 | LTC/USD | 44.22 | 46.404 | 48.306 | +0.48% | -0.02% | 0.82x | 2.3 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | TRUST/USD | 0.05108 | 45.975 | 46.542 | +3.82% | +0.20% | 0.85x | 23.5 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | WEAK 33/100 | EXTREME 86/100 | Do nothing | WATCH |
| 11 | TRX/USD | 0.310409 | 45.733 | 40.919 | +0.36% | -0.10% | 1.53x | 0.0 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 12 | BNB/USD | 584.05 | 42.608 | 40.752 | +0.47% | +0.04% | 1.16x | 1.9 | 2026-11-19T01:10:11.828104+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ETH/USD | 58.794 | 1784.45 | +0.03% | 1.20x |
| 2 | UP/USD | 57.012 | 0.05196 | -0.31% | 0.87x |
| 3 | HYPE/USD | 55.394 | 67.06 | +0.16% | 0.54x |
| 4 | NEAR/USD | 55.356 | 3.3126 | -0.34% | 1.17x |
| 5 | TAO/USD | 53.128 | 192.5279 | +0.10% | 1.94x |
| 6 | SENT/USD | 52.923 | 0.021287 | -0.82% | 1.10x |
| 7 | LTC/USD | 48.306 | 44.22 | -0.02% | 0.82x |
| 8 | TRUST/USD | 46.542 | 0.05108 | +0.20% | 0.85x |
| 9 | PAXG/USD | 44.920 | 3744.89 | -0.04% | 5.53x |
| 10 | TRX/USD | 40.919 | 0.310409 | -0.10% | 1.53x |
| 11 | BNB/USD | 40.752 | 584.05 | +0.04% | 1.16x |
| 12 | AAVE/USD | 40.185 | 109.67 | +0.18% | 4.38x |

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

- Persisted scans: 715; predictions: 5805; observations: 432442.
- Matured sampled outcomes across 1/6/24/48h: 5678; gap abstentions: 13432. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44434740355 · **Generation:** 715 · **Legacy run:** 44434740355
**Main quote time:** 2026-11-19T01:10:20.859148+00:00 · **Legacy report time:** 2026-11-19T01:10:54.334755+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 192.5279 | 63.03 | +0.10% | 1.94x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 2 | ETH/USD | 1784.45 | 60.96 | +0.03% | 1.20x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 3 | PAXG/USD | 3744.89 | 59.70 | -0.04% | 5.53x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | AAVE/USD | 109.67 | 56.10 | +0.18% | 4.38x | STRONG 73/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD | 3.3126 | 55.38 | -0.34% | 1.17x | WEAK 38/100 | HIGH 68/100 | Watch |
| 6 | UP/USD | 0.05196 | 54.21 | -0.31% | 0.87x | WEAK 32/100 | VERY_HIGH 73/100 | Do nothing |
| 7 | HYPE/USD | 67.06 | 51.64 | +0.16% | 0.54x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 8 | SENT/USD | 0.021287 | 49.86 | -0.82% | 1.10x | WEAK 35/100 | VERY_HIGH 80/100 | Watch |
| 9 | LTC/USD | 44.22 | 46.40 | -0.02% | 0.82x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 10 | TRUST/USD | 0.05108 | 45.97 | +0.20% | 0.85x | WEAK 33/100 | EXTREME 86/100 | Do nothing |
| 11 | TRX/USD | 0.310409 | 45.73 | -0.10% | 1.53x | WEAK 43/100 | HIGH 61/100 | Watch |
| 12 | BNB/USD | 584.05 | 42.61 | +0.04% | 1.16x | MODERATE 46/100 | HIGH 62/100 | Watch |

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
