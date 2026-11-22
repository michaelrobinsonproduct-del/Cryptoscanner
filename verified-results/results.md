# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T15:51:22.593905+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45040426183
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 88ab8d0ed69cb94b900b65ddce6616ef4b28098b (atomic ledger/results publication)
**Ledger generation:** 1303 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ETH/USD | 1716.85 | 82.406 | 69.356 | +2.05% | +0.16% | 2.23x | 0.1 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002546 | 81.983 | 78.077 | +8.62% | +0.91% | 0.94x | 15.7 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 66/100 | HIGH 68/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04823 | 78.555 | 85.108 | +8.92% | -0.68% | 0.68x | 14.5 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | DRV/USD | 0.36571 | 77.210 | 80.776 | +9.10% | +0.41% | 0.44x | 16.1 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6565 | 77.126 | 63.425 | +1.42% | +0.18% | 2.28x | 3.0 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0001 | 76.925 | 81.099 | +3.94% | +0.02% | 0.57x | 3.0 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LINK/USD | 8.80163 | 76.419 | 60.567 | +2.41% | +0.17% | 7.41x | 3.0 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 8 | VVV/USD | 25.464 | 74.979 | 66.930 | +2.27% | -0.29% | 1.95x | 7.9 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.8 | 69.253 | 71.239 | +2.55% | +0.29% | 0.66x | 3.2 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | TAO/USD | 190.7863 | 67.968 | 64.292 | +2.72% | +0.21% | 1.26x | 6.9 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XBT/USD | 60850.3 | 63.635 | 63.850 | +1.27% | +0.12% | 0.92x | 0.0 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 12 | STBL/USD | 0.017093 | 63.602 | 67.329 | +6.80% | +0.29% | 0.48x | 17.0 | 2026-11-22T15:51:14.418032+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 85.108 | 0.04823 | -0.68% | 0.68x |
| 2 | NEAR/USD | 81.099 | 3.0001 | +0.02% | 0.57x |
| 3 | DRV/USD | 80.776 | 0.36571 | +0.41% | 0.44x |
| 4 | PUMP/USD | 78.077 | 0.002546 | +0.91% | 0.94x |
| 5 | HYPE/USD | 71.239 | 62.8 | +0.29% | 0.66x |
| 6 | ETH/USD | 69.356 | 1716.85 | +0.16% | 2.23x |
| 7 | STBL/USD | 67.329 | 0.017093 | +0.29% | 0.48x |
| 8 | VVV/USD | 66.930 | 25.464 | -0.29% | 1.95x |
| 9 | TAO/USD | 64.292 | 190.7863 | +0.21% | 1.26x |
| 10 | XBT/USD | 63.850 | 60850.3 | +0.12% | 0.92x |
| 11 | SUI/USD | 63.425 | 0.6565 | +0.18% | 2.28x |
| 12 | LINK/USD | 60.567 | 8.80163 | +0.17% | 7.41x |

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

- Persisted scans: 1303; predictions: 10555; observations: 788635.
- Matured sampled outcomes across 1/6/24/48h: 15518; gap abstentions: 22316. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45040426183 · **Generation:** 1303 · **Legacy run:** 45040426183
**Main quote time:** 2026-11-22T15:51:22.593905+00:00 · **Legacy report time:** 2026-11-22T15:52:19.770925+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1716.85 | 82.41 | +0.16% | 2.23x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD | 0.002546 | 81.98 | +0.91% | 0.94x | MODERATE 66/100 | HIGH 68/100 | Watch |
| 3 | NIGHT/USD | 0.04823 | 78.56 | -0.68% | 0.68x | WEAK 39/100 | VERY_HIGH 82/100 | Watch |
| 4 | DRV/USD | 0.36571 | 77.21 | +0.41% | 0.44x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 5 | SUI/USD | 0.6565 | 77.13 | +0.18% | 2.28x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | NEAR/USD | 3.0001 | 76.92 | +0.02% | 0.57x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | LINK/USD ⭐ | 8.80163 | 76.42 | +0.17% | 7.41x | STRONG 93/100 | HIGH 55/100 | Watch |
| 8 | VVV/USD | 25.464 | 74.98 | -0.29% | 1.95x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 9 | HYPE/USD | 62.8 | 69.25 | +0.29% | 0.66x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 10 | TAO/USD ⭐ | 190.7863 | 67.97 | +0.21% | 1.26x | STRONG 79/100 | HIGH 55/100 | Watch |
| 11 | XBT/USD | 60850.3 | 63.64 | +0.12% | 0.92x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 12 | STBL/USD | 0.017093 | 63.60 | +0.29% | 0.48x | MODERATE 57/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1716.59 | 81.73 | +0.16% | 2.23x | 39324 | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 8.8029 | 79.43 | +0.17% | 7.41x | 4882 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | ZBCN/USD | 0.001956 | 75.28 | +1.03% | 1.01x | 4840 | MODERATE 63/100 | VERY_HIGH 79/100 | Watch |
| 4 | TAO/USD ⭐ | 190.4803 | 73.34 | +0.21% | 1.26x | 5668 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ETH/USD, LINK/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
