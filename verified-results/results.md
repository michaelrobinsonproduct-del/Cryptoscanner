# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T22:06:09.221706+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45710055341
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d4b9e86b2d1bfe0a8e5553e32da2a9132554a8ee (atomic ledger/results publication)
**Ledger generation:** 1773 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.47 | 95.174 | 81.583 | +3.97% | -0.28% | 2.93x | 2.4 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0253 | 81.808 | 87.020 | +4.88% | -0.25% | 0.61x | 4.3 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XMR/USD | 519.75 | 75.273 | 62.971 | +1.99% | -0.54% | 7.64x | 11.9 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.56 | 73.806 | 73.947 | +2.82% | -0.29% | 1.13x | 1.6 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6619 | 68.476 | 69.812 | +2.22% | -0.38% | 1.05x | 1.5 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XBT/USD | 60092.7 | 63.846 | 59.109 | +0.59% | -0.29% | 1.62x | 0.0 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ZEC/USD | 758 | 62.159 | 71.192 | +2.59% | -0.77% | 0.48x | 3.8 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | PUMP/USD | 0.00253 | 61.437 | 64.866 | +3.73% | -0.12% | 0.72x | 7.9 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XAUT/USD | 3578.7 | 60.409 | 46.761 | +1.16% | +0.14% | 2.29x | 0.6 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 10 | LINK/USD | 9.04227 | 60.059 | 63.259 | +2.27% | -0.31% | 0.84x | 1.9 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SOL/USD | 70.51 | 59.004 | 63.443 | +1.31% | -0.35% | 0.73x | 1.4 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XRP/USD | 0.93925 | 57.660 | 66.747 | +1.69% | -0.33% | 0.26x | 0.2 | 2026-11-25T22:06:00.642443+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.020 | 3.0253 | -0.25% | 0.61x |
| 2 | LTC/USD | 81.583 | 42.47 | -0.28% | 2.93x |
| 3 | HYPE/USD | 73.947 | 61.56 | -0.29% | 1.13x |
| 4 | ZEC/USD | 71.192 | 758 | -0.77% | 0.48x |
| 5 | SUI/USD | 69.812 | 0.6619 | -0.38% | 1.05x |
| 6 | XRP/USD | 66.747 | 0.93925 | -0.33% | 0.26x |
| 7 | PUMP/USD | 64.866 | 0.00253 | -0.12% | 0.72x |
| 8 | SOL/USD | 63.443 | 70.51 | -0.35% | 0.73x |
| 9 | LINK/USD | 63.259 | 9.04227 | -0.31% | 0.84x |
| 10 | XMR/USD | 62.971 | 519.75 | -0.54% | 7.64x |
| 11 | XBT/USD | 59.109 | 60092.7 | -0.29% | 1.62x |
| 12 | XAUT/USD | 46.761 | 3578.7 | +0.14% | 2.29x |

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

- Persisted scans: 1773; predictions: 15020; observations: 1074801.
- Matured sampled outcomes across 1/6/24/48h: 32774; gap abstentions: 23210. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45710055341 · **Generation:** 1773 · **Legacy run:** 45710055341
**Main quote time:** 2026-11-25T22:06:09.221706+00:00 · **Legacy report time:** 2026-11-25T22:07:17.420416+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.47 | 95.17 | -0.28% | 2.93x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 3.0253 | 81.81 | -0.25% | 0.61x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 3 | XMR/USD | 519.75 | 75.27 | -0.54% | 7.64x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 4 | HYPE/USD | 61.56 | 73.81 | -0.29% | 1.13x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 5 | SUI/USD | 0.6619 | 68.48 | -0.38% | 1.05x | WEAK 44/100 | HIGH 68/100 | Watch |
| 6 | XBT/USD | 60092.7 | 63.85 | -0.29% | 1.62x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | ZEC/USD | 758 | 62.16 | -0.77% | 0.48x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | PUMP/USD | 0.00253 | 61.44 | -0.12% | 0.72x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | XAUT/USD | 3578.7 | 60.41 | +0.14% | 2.29x | STRONG 75/100 | HIGH 55/100 | Watch |
| 10 | LINK/USD | 9.04227 | 60.06 | -0.31% | 0.84x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | SOL/USD | 70.51 | 59.00 | -0.35% | 0.73x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XRP/USD | 0.93925 | 57.66 | -0.33% | 0.26x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

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
