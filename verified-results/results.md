# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T10:01:33.411128+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45151979799
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9a3c9988e0ac10c2b5c1ccf856fb198e68ad87d8 (atomic ledger/results publication)
**Ledger generation:** 1414 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 152.98 | 105.988 | 90.067 | +6.65% | +0.18% | 9.79x | 3.3 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08066 | 94.209 | 75.141 | +6.93% | +0.81% | 5.29x | 7.5 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | XLM/USD | 0.12853 | 71.181 | 59.498 | +0.79% | +0.29% | 2.02x | 1.2 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | JUP/USD | 0.2441 | 70.208 | 73.115 | +8.70% | +0.13% | 0.64x | 14.3 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6698 | 67.064 | 69.306 | +2.15% | -0.09% | 0.82x | 1.5 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93901 | 66.942 | 63.603 | +1.24% | +0.09% | 1.29x | 0.1 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | MODERATE 58/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 72.44 | 66.473 | 72.248 | +2.56% | +0.24% | 0.30x | 1.4 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XMR/USD | 504.69 | 60.433 | 67.099 | +2.22% | +0.07% | 0.30x | 6.9 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HYPE/USD | 63.94 | 60.299 | 63.986 | +1.40% | +0.13% | 0.57x | 1.6 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 61401.3 | 56.006 | 57.638 | +0.38% | -0.09% | 0.88x | 0.0 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | LTC/USD | 40.72 | 49.842 | 50.824 | +1.39% | +0.05% | 0.88x | 2.5 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | MODERATE 45/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PAXG/USD | 3603.68 | 46.256 | 50.747 | +0.88% | -0.08% | 0.59x | 0.6 | 2026-11-23T10:01:24.870187+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 90.067 | 152.98 | +0.18% | 9.79x |
| 2 | ALGO/USD | 75.141 | 0.08066 | +0.81% | 5.29x |
| 3 | JUP/USD | 73.115 | 0.2441 | +0.13% | 0.64x |
| 4 | SOL/USD | 72.248 | 72.44 | +0.24% | 0.30x |
| 5 | SUI/USD | 69.306 | 0.6698 | -0.09% | 0.82x |
| 6 | XMR/USD | 67.099 | 504.69 | +0.07% | 0.30x |
| 7 | HYPE/USD | 63.986 | 63.94 | +0.13% | 0.57x |
| 8 | XRP/USD | 63.603 | 0.93901 | +0.09% | 1.29x |
| 9 | XLM/USD | 59.498 | 0.12853 | +0.29% | 2.02x |
| 10 | XBT/USD | 57.638 | 61401.3 | -0.09% | 0.88x |
| 11 | LTC/USD | 50.824 | 40.72 | +0.05% | 0.88x |
| 12 | PAXG/USD | 50.747 | 3603.68 | -0.08% | 0.59x |

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

- Persisted scans: 1414; predictions: 11735; observations: 856229.
- Matured sampled outcomes across 1/6/24/48h: 19281; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45151979799 · **Generation:** 1414 · **Legacy run:** 45151979799
**Main quote time:** 2026-11-23T10:01:33.411128+00:00 · **Legacy report time:** 2026-11-23T10:02:29.562447+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 152.98 | 105.99 | +0.18% | 9.79x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ALGO/USD ⭐ | 0.08066 | 94.21 | +0.81% | 5.29x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | XLM/USD | 0.12853 | 71.18 | +0.29% | 2.02x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | JUP/USD | 0.2441 | 70.21 | +0.13% | 0.64x | MODERATE 50/100 | VERY_HIGH 81/100 | Watch |
| 5 | SUI/USD | 0.6698 | 67.06 | -0.09% | 0.82x | WEAK 39/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.93901 | 66.94 | +0.09% | 1.29x | MODERATE 58/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 72.44 | 66.47 | +0.24% | 0.30x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | XMR/USD | 504.69 | 60.43 | +0.07% | 0.30x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | HYPE/USD | 63.94 | 60.30 | +0.13% | 0.57x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 61401.3 | 56.01 | -0.09% | 0.88x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 11 | LTC/USD | 40.72 | 49.84 | +0.05% | 0.88x | MODERATE 45/100 | HIGH 62/100 | Watch |
| 12 | PAXG/USD | 3603.68 | 46.26 | -0.08% | 0.59x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 153 | 91.76 | +0.18% | 9.79x | 5043 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ALGO/USD ⭐ | 0.0802 | 82.75 | +0.81% | 5.29x | 2727 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | INJ/USD | 6.42 | 72.51 | +0.33% | 2.47x | 4739 | STRONG 86/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** QNT/USD, ALGO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
