# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:25:28.158850+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44464959994
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** a42e4509bc2b9404dfc78a3c718fe01dd3e0730e (atomic ledger/results publication)
**Ledger generation:** 765 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.532 | 71.183 | 78.243 | +3.97% | +0.12% | 0.23x | 7.5 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 67.87 | 70.625 | 63.889 | +1.48% | +0.46% | 1.44x | 2.9 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 935.54 | 70.188 | 71.560 | +2.59% | +0.05% | 0.84x | 3.1 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SENT/USD | 0.02291 | 68.965 | 70.512 | +11.19% | -1.29% | 1.49x | 13.5 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | NEAR/USD | 3.3957 | 66.555 | 73.366 | +2.98% | -0.64% | 0.64x | 5.0 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ETH/USD | 1797.84 | 57.821 | 64.075 | +1.30% | -0.07% | 0.41x | 0.1 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | SOL/USD | 74.57 | 57.579 | 64.134 | +1.40% | -0.09% | 0.39x | 1.3 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.152551 | 56.201 | 58.613 | +0.86% | -0.03% | 0.77x | 4.8 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | XBT/USD | 63448.2 | 54.627 | 60.146 | +0.74% | -0.16% | 0.53x | 0.0 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.10804 | 53.192 | 55.004 | +0.39% | -0.13% | 0.89x | 5.4 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0590533 | 52.133 | 53.706 | +0.59% | +0.00% | 0.84x | 0.0 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.97337 | 51.679 | 60.019 | +0.72% | -0.06% | 0.20x | 0.1 | 2026-11-19T05:25:20.014596+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 78.243 | 22.532 | +0.12% | 0.23x |
| 2 | NEAR/USD | 73.366 | 3.3957 | -0.64% | 0.64x |
| 3 | ZEC/USD | 71.560 | 935.54 | +0.05% | 0.84x |
| 4 | SENT/USD | 70.512 | 0.02291 | -1.29% | 1.49x |
| 5 | SOL/USD | 64.134 | 74.57 | -0.09% | 0.39x |
| 6 | ETH/USD | 64.075 | 1797.84 | -0.07% | 0.41x |
| 7 | HYPE/USD | 63.889 | 67.87 | +0.46% | 1.44x |
| 8 | XBT/USD | 60.146 | 63448.2 | -0.16% | 0.53x |
| 9 | XRP/USD | 60.019 | 0.97337 | -0.06% | 0.20x |
| 10 | ADA/USD | 58.613 | 0.152551 | -0.03% | 0.77x |
| 11 | LINK/USD | 55.004 | 9.10804 | -0.13% | 0.89x |
| 12 | XDG/USD | 53.706 | 0.0590533 | +0.00% | 0.84x |

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

- Persisted scans: 765; predictions: 6324; observations: 462891.
- Matured sampled outcomes across 1/6/24/48h: 6338; gap abstentions: 13747. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44464959994 · **Generation:** 765 · **Legacy run:** 44464959994
**Main quote time:** 2026-11-19T05:25:28.158850+00:00 · **Legacy report time:** 2026-11-19T05:26:13.674061+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.532 | 71.18 | +0.12% | 0.23x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD ⭐ | 67.87 | 70.62 | +0.46% | 1.44x | STRONG 90/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD | 935.54 | 70.19 | +0.05% | 0.84x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 4 | SENT/USD | 0.02291 | 68.97 | -1.29% | 1.49x | MODERATE 49/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | NEAR/USD | 3.3957 | 66.56 | -0.64% | 0.64x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 6 | ETH/USD | 1797.84 | 57.82 | -0.07% | 0.41x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | SOL/USD | 74.57 | 57.58 | -0.09% | 0.39x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ADA/USD | 0.152551 | 56.20 | -0.03% | 0.77x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 9 | XBT/USD | 63448.2 | 54.63 | -0.16% | 0.53x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LINK/USD | 9.10804 | 53.19 | -0.13% | 0.89x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 11 | XDG/USD | 0.0590533 | 52.13 | +0.00% | 0.84x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.97337 | 51.68 | -0.06% | 0.20x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 67.97 | 68.82 | +0.46% | 1.44x | 14637 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
