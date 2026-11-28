# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T04:17:31.707107+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46106605197
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c5f6f466eb20ee7e1b86fc5be913bf4a2a40ecd4 (atomic ledger/results publication)
**Ledger generation:** 2104 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 420.13 | 70.814 | 72.227 | +3.16% | +0.23% | 0.74x | 9.8 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0652 | 68.585 | 64.433 | +1.56% | +0.21% | 1.31x | 2.9 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 753 | 66.671 | 71.035 | +2.51% | +0.19% | 0.47x | 3.1 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | HYPE/USD | 64.38 | 59.444 | 63.259 | +1.40% | -0.09% | 0.67x | 3.1 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024654 | 57.879 | 58.225 | +3.96% | +0.84% | 0.55x | 0.8 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | VVV/USD | 26.173 | 57.348 | 54.203 | +1.65% | +0.75% | 0.94x | 7.3 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95121 | 53.481 | 57.281 | +0.33% | +0.06% | 0.59x | 0.1 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.07582 | 44.619 | 47.745 | +2.25% | +0.37% | 0.50x | 5.3 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | BCH/USD | 209.57 | 35.041 | 43.027 | +1.24% | -0.06% | 0.23x | 4.8 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | PONS/USD | 0.1032 | 34.764 | 33.082 | +0.88% | +1.18% | 0.58x | 9.7 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | SEI/USD | 0.03884 | 32.898 | 35.423 | +1.12% | +0.42% | 0.54x | 10.3 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | W/USD | 0.00928 | 30.540 | 27.565 | +0.76% | +0.22% | 1.19x | 21.6 | 2026-11-28T04:17:24.536630+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 72.227 | 420.13 | +0.23% | 0.74x |
| 2 | ZEC/USD | 71.035 | 753 | +0.19% | 0.47x |
| 3 | NEAR/USD | 64.433 | 3.0652 | +0.21% | 1.31x |
| 4 | HYPE/USD | 63.259 | 64.38 | -0.09% | 0.67x |
| 5 | SENT/USD | 58.225 | 0.024654 | +0.84% | 0.55x |
| 6 | XRP/USD | 57.281 | 0.95121 | +0.06% | 0.59x |
| 7 | VVV/USD | 54.203 | 26.173 | +0.75% | 0.94x |
| 8 | CC/USD | 47.745 | 0.07582 | +0.37% | 0.50x |
| 9 | BCH/USD | 43.027 | 209.57 | -0.06% | 0.23x |
| 10 | SEI/USD | 35.423 | 0.03884 | +0.42% | 0.54x |
| 11 | PONS/USD | 33.082 | 0.1032 | +1.18% | 0.58x |
| 12 | W/USD | 27.565 | 0.00928 | +0.22% | 1.19x |

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

- Persisted scans: 2104; predictions: 18895; observations: 1274070.
- Matured sampled outcomes across 1/6/24/48h: 43802; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46106605197 · **Generation:** 2104 · **Legacy run:** 46106605197
**Main quote time:** 2026-11-28T04:17:31.707107+00:00 · **Legacy report time:** 2026-11-28T04:18:16.811260+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 420.13 | 70.81 | +0.23% | 0.74x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0652 | 68.58 | +0.21% | 1.31x | STRONG 89/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD | 753 | 66.67 | +0.19% | 0.47x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 4 | HYPE/USD | 64.38 | 59.44 | -0.09% | 0.67x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 5 | SENT/USD | 0.024654 | 57.88 | +0.84% | 0.55x | MODERATE 59/100 | VERY_HIGH 82/100 | Watch |
| 6 | VVV/USD | 26.173 | 57.35 | +0.75% | 0.94x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.95121 | 53.48 | +0.06% | 0.59x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.07582 | 44.62 | +0.37% | 0.50x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 9 | BCH/USD | 209.57 | 35.04 | -0.06% | 0.23x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | PONS/USD | 0.1032 | 34.76 | +1.18% | 0.58x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 11 | SEI/USD | 0.03884 | 32.90 | +0.42% | 0.54x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 12 | W/USD | 0.00928 | 30.54 | +0.22% | 1.19x | WEAK 40/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0648 | 57.39 | +0.21% | 1.31x | 13036 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
