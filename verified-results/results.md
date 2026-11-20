# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T09:20:49.456258+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44709752638
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** d59e16a4d18d74e8bc36d986668712d6f82e34ba (atomic ledger/results publication)
**Ledger generation:** 959 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01398 | 110.267 | 70.267 | +6.15% | +5.04% | 35.41x | 7.1 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | HBAR/USD | 0.05401 | 55.829 | 41.847 | +0.47% | -0.20% | 3.16x | 3.7 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TON/USD | 1.02 | 44.280 | 30.259 | +0.29% | -0.20% | 4.72x | 9.8 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | MODERATE 52/100 | HIGH 66/100 | Watch | WATCH |
| 4 | BMT/USD | 0.02239 | 41.738 | 56.564 | +11.50% | -1.15% | 0.09x | 40.2 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | WEAK 11/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | CT/USD | 0.1294 | 33.705 | 24.990 | +0.70% | +1.09% | 1.32x | 23.3 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010251 | 30.064 | 40.356 | +2.04% | -0.63% | 0.29x | 10.7 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | WEAK 15/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | SAPIEN/USD | 0.04055 | 20.414 | 27.937 | +0.97% | -1.77% | 1.13x | 19.8 | 2026-11-20T09:20:44.540001+00:00 | Not calibrated | WEAK 15/100 | EXTREME 90/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 70.267 | 0.01398 | +5.04% | 35.41x |
| 2 | BMT/USD | 56.564 | 0.02239 | -1.15% | 0.09x |
| 3 | HBAR/USD | 41.847 | 0.05401 | -0.20% | 3.16x |
| 4 | SKR/USD | 40.356 | 0.010251 | -0.63% | 0.29x |
| 5 | TON/USD | 30.259 | 1.02 | -0.20% | 4.72x |
| 6 | SAPIEN/USD | 27.937 | 0.04055 | -1.77% | 1.13x |
| 7 | CT/USD | 24.990 | 0.1294 | +1.09% | 1.32x |

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

- Persisted scans: 959; predictions: 8137; observations: 579473.
- Matured sampled outcomes across 1/6/24/48h: 9687; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44709752638 · **Generation:** 959 · **Legacy run:** 44709752638
**Main quote time:** 2026-11-20T09:20:49.456258+00:00 · **Legacy report time:** 2026-11-20T09:21:36.777878+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01398 | 110.27 | +5.04% | 35.41x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | HBAR/USD | 0.05401 | 55.83 | -0.20% | 3.16x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | TON/USD | 1.02 | 44.28 | -0.20% | 4.72x | MODERATE 52/100 | HIGH 66/100 | Watch |
| 4 | BMT/USD | 0.02239 | 41.74 | -1.15% | 0.09x | WEAK 11/100 | EXTREME 100/100 | Do nothing |
| 5 | CT/USD ⭐ | 0.1294 | 33.71 | +1.09% | 1.32x | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |
| 6 | SKR/USD | 0.010251 | 30.06 | -0.63% | 0.29x | WEAK 15/100 | EXTREME 94/100 | Do nothing |
| 7 | SAPIEN/USD | 0.04055 | 20.41 | -1.77% | 1.13x | WEAK 15/100 | EXTREME 90/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01381 | 86.99 | +5.04% | 35.41x | 2930 | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | XRP/USD | 0.96121 | 60.43 | +0.09% | 3.16x | 32283 | STRONG 75/100 | HIGH 55/100 | Watch |
| 3 | CT/USD ⭐ | 0.1294 | 33.87 | +1.09% | 1.32x | 2383 | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** AI/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
