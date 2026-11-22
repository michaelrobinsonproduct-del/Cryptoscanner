# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:43:11.748625+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44972474832
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 24642434c36825755c7a53a26076a0a09579d3c1 (atomic ledger/results publication)
**Ledger generation:** 1216 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9075 | 55.917 | 58.078 | +0.73% | +0.33% | 0.62x | 4.1 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TAO/USD | 186.3897 | 54.339 | 55.026 | +0.36% | +0.04% | 0.91x | 4.9 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.991 | 48.764 | 48.475 | +2.19% | +0.89% | 0.59x | 19.6 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | DRV/USD | 0.3439 | 45.917 | 55.998 | +2.60% | -2.12% | 1.05x | 20.4 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 5 | ENA/USD | 0.0986 | 43.734 | 38.602 | +0.31% | +0.20% | 1.41x | 10.2 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ZRO/USD | 1.195 | 42.406 | 44.931 | +1.88% | +0.84% | 0.33x | 16.8 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | CAP/USD | 0.092343 | 28.813 | 35.062 | +0.42% | -0.39% | 0.57x | 6.1 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | PENGU/USD | 0.004292 | 26.898 | 34.569 | +0.30% | +0.12% | 0.17x | 4.7 | 2026-11-22T01:43:03.799310+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 58.078 | 2.9075 | +0.33% | 0.62x |
| 2 | DRV/USD | 55.998 | 0.3439 | -2.12% | 1.05x |
| 3 | TAO/USD | 55.026 | 186.3897 | +0.04% | 0.91x |
| 4 | PEARL/USD | 48.475 | 1.991 | +0.89% | 0.59x |
| 5 | ZRO/USD | 44.931 | 1.195 | +0.84% | 0.33x |
| 6 | ENA/USD | 38.602 | 0.0986 | +0.20% | 1.41x |
| 7 | CAP/USD | 35.062 | 0.092343 | -0.39% | 0.57x |
| 8 | PENGU/USD | 34.569 | 0.004292 | +0.12% | 0.17x |

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

- Persisted scans: 1216; predictions: 9831; observations: 735686.
- Matured sampled outcomes across 1/6/24/48h: 13491; gap abstentions: 21815. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 22 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44972474832 · **Generation:** 1216 · **Legacy run:** 44972474832
**Main quote time:** 2026-11-22T01:43:11.748625+00:00 · **Legacy report time:** 2026-11-22T01:44:10.457441+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 2.9075 | 55.92 | +0.33% | 0.62x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 2 | TAO/USD | 186.3897 | 54.34 | +0.04% | 0.91x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 3 | PEARL/USD | 1.991 | 48.76 | +0.89% | 0.59x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 4 | DRV/USD | 0.3439 | 45.92 | -2.12% | 1.05x | WEAK 23/100 | VERY_HIGH 84/100 | Do nothing |
| 5 | ENA/USD | 0.0986 | 43.73 | +0.20% | 1.41x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 6 | ZRO/USD | 1.195 | 42.41 | +0.84% | 0.33x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 7 | CAP/USD | 0.092343 | 28.81 | -0.39% | 0.57x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | PENGU/USD | 0.004292 | 26.90 | +0.12% | 0.17x | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing |

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
