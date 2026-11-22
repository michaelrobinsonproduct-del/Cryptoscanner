# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T02:01:10.493253+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44973972058
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 34bc50f85fd5fa1896679ff34872cc8b00ff83fb (atomic ledger/results publication)
**Ledger generation:** 1218 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9036 | 58.269 | 57.301 | +0.60% | -0.33% | 1.26x | 3.8 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 39/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 25.021 | 52.340 | 54.205 | +0.49% | +0.09% | 0.77x | 8.4 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TAO/USD | 186.702 | 50.888 | 55.940 | +0.52% | +0.06% | 0.46x | 5.5 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.9912 | 41.792 | 45.012 | +2.20% | +0.09% | 0.63x | 26.7 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | BNB/USD | 548.79 | 41.186 | 44.864 | +0.25% | +0.08% | 0.59x | 2.0 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ENSO/USD | 0.513 | 34.835 | 56.179 | +6.43% | -3.24% | 0.49x | 39.1 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | DRV/USD | 0.33947 | 32.956 | 49.494 | +1.27% | -1.63% | 0.16x | 14.5 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 16/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | PENGU/USD | 0.00429 | 31.764 | 34.238 | +0.26% | -0.09% | 0.80x | 4.7 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 9 | ZRO/USD | 1.187 | 29.249 | 40.069 | +1.19% | -0.34% | 0.09x | 16.9 | 2026-11-22T02:01:02.113974+00:00 | Not calibrated | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 57.301 | 2.9036 | -0.33% | 1.26x |
| 2 | ENSO/USD | 56.179 | 0.513 | -3.24% | 0.49x |
| 3 | TAO/USD | 55.940 | 186.702 | +0.06% | 0.46x |
| 4 | VVV/USD | 54.205 | 25.021 | +0.09% | 0.77x |
| 5 | DRV/USD | 49.494 | 0.33947 | -1.63% | 0.16x |
| 6 | PEARL/USD | 45.012 | 1.9912 | +0.09% | 0.63x |
| 7 | BNB/USD | 44.864 | 548.79 | +0.08% | 0.59x |
| 8 | ZRO/USD | 40.069 | 1.187 | -0.34% | 0.09x |
| 9 | PENGU/USD | 34.238 | 0.00429 | -0.09% | 0.80x |

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

- Persisted scans: 1218; predictions: 9850; observations: 736902.
- Matured sampled outcomes across 1/6/24/48h: 13554; gap abstentions: 21855. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 22 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44973972058 · **Generation:** 1218 · **Legacy run:** 44973972058
**Main quote time:** 2026-11-22T02:01:10.493253+00:00 · **Legacy report time:** 2026-11-22T02:02:13.722303+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 2.9036 | 58.27 | -0.33% | 1.26x | WEAK 39/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 25.021 | 52.34 | +0.09% | 0.77x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD | 186.702 | 50.89 | +0.06% | 0.46x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 4 | PEARL/USD | 1.9912 | 41.79 | +0.09% | 0.63x | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | BNB/USD | 548.79 | 41.19 | +0.08% | 0.59x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 6 | ENSO/USD | 0.513 | 34.84 | -3.24% | 0.49x | WEAK 7/100 | EXTREME 100/100 | Do nothing |
| 7 | DRV/USD | 0.33947 | 32.96 | -1.63% | 0.16x | WEAK 16/100 | EXTREME 86/100 | Do nothing |
| 8 | PENGU/USD | 0.00429 | 31.76 | -0.09% | 0.80x | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing |
| 9 | ZRO/USD | 1.187 | 29.25 | -0.34% | 0.09x | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing |

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
