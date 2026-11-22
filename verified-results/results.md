# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T17:21:20.649129+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45048796454
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** addbf1b1bbd9faf56589ab95972cb161d1e21e9a (atomic ledger/results publication)
**Ledger generation:** 1313 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.35799 | 90.458 | 84.364 | +6.80% | -0.63% | 1.92x | 8.7 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZBCN/USD | 0.001913 | 88.728 | 71.364 | +10.77% | +0.47% | 3.45x | 15.7 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | STRONG 94/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 2.9954 | 83.591 | 79.791 | +3.78% | +0.45% | 1.16x | 3.3 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ETH/USD | 1710.69 | 81.731 | 66.792 | +1.69% | -0.01% | 3.14x | 0.1 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.00256 | 79.630 | 80.096 | +9.21% | -0.35% | 1.13x | 11.7 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | ZEC/USD | 793.69 | 78.846 | 67.513 | +1.99% | +0.01% | 2.13x | 2.9 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.79 | 77.636 | 71.921 | +2.53% | +0.14% | 1.50x | 1.6 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | PEARL/USD | 2.0448 | 70.530 | 68.821 | +4.95% | +0.23% | 1.06x | 15.7 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | MODERATE 65/100 | HIGH 68/100 | Watch | WATCH |
| 9 | VVV/USD | 25.464 | 65.500 | 66.535 | +2.27% | -0.05% | 0.92x | 8.6 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XBT/USD | 60741.6 | 60.592 | 62.584 | +1.08% | -0.21% | 0.91x | 0.0 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | PAXG/USD | 3557.63 | 56.260 | 40.743 | +0.29% | +0.10% | 19.59x | 0.1 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 12 | ONDO/USD | 0.28447 | 55.850 | 41.535 | +1.02% | -0.14% | 3.03x | 0.4 | 2026-11-22T17:21:12.872160+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 84.364 | 0.35799 | -0.63% | 1.92x |
| 2 | PUMP/USD | 80.096 | 0.00256 | -0.35% | 1.13x |
| 3 | NEAR/USD | 79.791 | 2.9954 | +0.45% | 1.16x |
| 4 | HYPE/USD | 71.921 | 62.79 | +0.14% | 1.50x |
| 5 | ZBCN/USD | 71.364 | 0.001913 | +0.47% | 3.45x |
| 6 | PEARL/USD | 68.821 | 2.0448 | +0.23% | 1.06x |
| 7 | ZEC/USD | 67.513 | 793.69 | +0.01% | 2.13x |
| 8 | ETH/USD | 66.792 | 1710.69 | -0.01% | 3.14x |
| 9 | VVV/USD | 66.535 | 25.464 | -0.05% | 0.92x |
| 10 | XBT/USD | 62.584 | 60741.6 | -0.21% | 0.91x |
| 11 | ONDO/USD | 41.535 | 0.28447 | -0.14% | 3.03x |
| 12 | PAXG/USD | 40.743 | 3557.63 | +0.10% | 19.59x |

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

- Persisted scans: 1313; predictions: 10675; observations: 794725.
- Matured sampled outcomes across 1/6/24/48h: 15850; gap abstentions: 22327. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45048796454 · **Generation:** 1313 · **Legacy run:** 45048796454
**Main quote time:** 2026-11-22T17:21:20.649129+00:00 · **Legacy report time:** 2026-11-22T17:22:13.854810+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.35799 | 90.46 | -0.63% | 1.92x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | ZBCN/USD ⭐ | 0.001913 | 88.73 | +0.47% | 3.45x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 2.9954 | 83.59 | +0.45% | 1.16x | STRONG 87/100 | HIGH 62/100 | Watch |
| 4 | ETH/USD | 1710.69 | 81.73 | -0.01% | 3.14x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | PUMP/USD | 0.00256 | 79.63 | -0.35% | 1.13x | MODERATE 45/100 | VERY_HIGH 74/100 | Watch |
| 6 | ZEC/USD | 793.69 | 78.85 | +0.01% | 2.13x | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD ⭐ | 62.79 | 77.64 | +0.14% | 1.50x | STRONG 84/100 | HIGH 55/100 | Watch |
| 8 | PEARL/USD ⭐ | 2.0448 | 70.53 | +0.23% | 1.06x | STRONG 75/100 | HIGH 68/100 | Watch |
| 9 | VVV/USD | 25.464 | 65.50 | -0.05% | 0.92x | WEAK 38/100 | HIGH 68/100 | Watch |
| 10 | XBT/USD | 60741.6 | 60.59 | -0.21% | 0.91x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | PAXG/USD | 3557.63 | 56.26 | +0.10% | 19.59x | STRONG 73/100 | HIGH 55/100 | Watch |
| 12 | ONDO/USD | 0.28447 | 55.85 | -0.14% | 3.03x | MODERATE 58/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0055 | 88.66 | +0.45% | 1.16x | 12925 | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | PEARL/USD ⭐ | 2.0448 | 85.26 | +0.23% | 1.06x | 6863 | STRONG 88/100 | HIGH 62/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.87 | 83.19 | +0.14% | 1.50x | 10369 | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | ZBCN/USD ⭐ | 0.001915 | 81.95 | +0.47% | 3.45x | 5646 | STRONG 96/100 | VERY_HIGH 72/100 | Watch |
| 5 | LINK/USD | 8.7929 | 69.78 | +0.07% | 1.90x | 4864 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZBCN/USD, NEAR/USD, HYPE/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
