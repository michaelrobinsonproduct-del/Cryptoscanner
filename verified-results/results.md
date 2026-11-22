# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T13:31:09.211199+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45027752943
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** b8a432830eeff40385e418ec6d70898d4d42df4b (atomic ledger/results publication)
**Ledger generation:** 1289 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0479 | 86.389 | 77.135 | +8.18% | +2.14% | 0.86x | 27.2 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | INJ/USD | 6.266 | 84.340 | 74.867 | +4.91% | +0.11% | 1.89x | 4.8 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9963 | 81.080 | 81.011 | +3.81% | +0.02% | 1.00x | 1.3 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 4 | DRV/USD | 0.35976 | 67.535 | 76.884 | +7.33% | -0.41% | 0.27x | 19.8 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 62.66 | 66.113 | 70.434 | +2.32% | -0.13% | 0.63x | 1.6 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ETH/USD | 1703.75 | 62.979 | 63.904 | +1.28% | -0.03% | 0.92x | 0.1 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XBT/USD | 60664.1 | 60.526 | 61.681 | +0.96% | -0.11% | 0.94x | 0.0 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ADA/USD | 0.144774 | 59.380 | 45.496 | +0.44% | -0.22% | 3.67x | 2.8 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 9 | TAO/USD | 191.041 | 57.566 | 67.953 | +2.86% | -0.16% | 0.04x | 8.5 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ZEC/USD | 792.03 | 56.331 | 66.522 | +1.78% | -0.36% | 0.16x | 1.9 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.6569 | 54.874 | 63.860 | +1.48% | -0.39% | 0.30x | 3.0 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LINK/USD | 8.75093 | 52.690 | 58.367 | +1.82% | -0.25% | 0.56x | 3.0 | 2026-11-22T13:31:02.837335+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 81.011 | 2.9963 | +0.02% | 1.00x |
| 2 | NIGHT/USD | 77.135 | 0.0479 | +2.14% | 0.86x |
| 3 | DRV/USD | 76.884 | 0.35976 | -0.41% | 0.27x |
| 4 | INJ/USD | 74.867 | 6.266 | +0.11% | 1.89x |
| 5 | HYPE/USD | 70.434 | 62.66 | -0.13% | 0.63x |
| 6 | TAO/USD | 67.953 | 191.041 | -0.16% | 0.04x |
| 7 | ZEC/USD | 66.522 | 792.03 | -0.36% | 0.16x |
| 8 | ETH/USD | 63.904 | 1703.75 | -0.03% | 0.92x |
| 9 | SUI/USD | 63.860 | 0.6569 | -0.39% | 0.30x |
| 10 | XBT/USD | 61.681 | 60664.1 | -0.11% | 0.94x |
| 11 | LINK/USD | 58.367 | 8.75093 | -0.25% | 0.56x |
| 12 | ADA/USD | 45.496 | 0.144774 | -0.22% | 3.67x |

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

- Persisted scans: 1289; predictions: 10388; observations: 780110.
- Matured sampled outcomes across 1/6/24/48h: 15060; gap abstentions: 22258. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45027752943 · **Generation:** 1289 · **Legacy run:** 45027752943
**Main quote time:** 2026-11-22T13:31:09.211199+00:00 · **Legacy report time:** 2026-11-22T13:32:11.352945+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0479 | 86.39 | +2.14% | 0.86x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 2 | INJ/USD ⭐ | 6.266 | 84.34 | +0.11% | 1.89x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD | 2.9963 | 81.08 | +0.02% | 1.00x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 4 | DRV/USD | 0.35976 | 67.53 | -0.41% | 0.27x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | HYPE/USD | 62.66 | 66.11 | -0.13% | 0.63x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 6 | ETH/USD | 1703.75 | 62.98 | -0.03% | 0.92x | WEAK 36/100 | HIGH 68/100 | Watch |
| 7 | XBT/USD | 60664.1 | 60.53 | -0.11% | 0.94x | WEAK 35/100 | HIGH 68/100 | Watch |
| 8 | ADA/USD | 0.144774 | 59.38 | -0.22% | 3.67x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 9 | TAO/USD | 191.041 | 57.57 | -0.16% | 0.04x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ZEC/USD | 792.03 | 56.33 | -0.36% | 0.16x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SUI/USD | 0.6569 | 54.87 | -0.39% | 0.30x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LINK/USD | 8.75093 | 52.69 | -0.25% | 0.56x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.266 | 83.89 | +0.11% | 1.89x | 7049 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
