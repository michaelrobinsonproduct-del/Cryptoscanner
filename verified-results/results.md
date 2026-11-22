# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T22:01:14.676483+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45075132589
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 4b02cea06f0060ae50fbb038ad8c92b46d40bc50 (atomic ledger/results publication)
**Ledger generation:** 1341 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37529 | 92.446 | 87.959 | +11.96% | +0.18% | 1.36x | 2.1 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04917 | 88.571 | 92.525 | +11.04% | +0.20% | 0.50x | 2.0 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002575 | 85.366 | 82.796 | +9.85% | +0.08% | 1.22x | 7.8 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 4 | STBL/USD | 0.017184 | 83.594 | 73.112 | +7.37% | +0.02% | 2.04x | 5.8 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ZEC/USD | 795.51 | 76.097 | 70.535 | +2.23% | +0.42% | 1.34x | 0.1 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9893 | 71.376 | 77.972 | +3.57% | -0.30% | 0.49x | 4.0 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | VVV/USD | 26.04 | 70.958 | 79.350 | +4.58% | -0.60% | 0.46x | 15.4 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | ETH/USD | 1716.39 | 66.749 | 69.164 | +2.03% | -0.30% | 0.91x | 0.1 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.57 | 63.880 | 68.603 | +2.17% | -0.16% | 0.61x | 3.2 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XBT/USD | 60841.8 | 59.548 | 63.751 | +1.25% | -0.19% | 0.67x | 0.0 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | BNB/USD | 556.9 | 57.831 | 49.317 | +1.73% | -0.14% | 1.92x | 0.2 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6551 | 54.822 | 62.501 | +1.21% | -0.15% | 0.31x | 1.5 | 2026-11-22T22:01:06.167067+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 92.525 | 0.04917 | +0.20% | 0.50x |
| 2 | DRV/USD | 87.959 | 0.37529 | +0.18% | 1.36x |
| 3 | PUMP/USD | 82.796 | 0.002575 | +0.08% | 1.22x |
| 4 | VVV/USD | 79.350 | 26.04 | -0.60% | 0.46x |
| 5 | NEAR/USD | 77.972 | 2.9893 | -0.30% | 0.49x |
| 6 | STBL/USD | 73.112 | 0.017184 | +0.02% | 2.04x |
| 7 | ZEC/USD | 70.535 | 795.51 | +0.42% | 1.34x |
| 8 | ETH/USD | 69.164 | 1716.39 | -0.30% | 0.91x |
| 9 | HYPE/USD | 68.603 | 62.57 | -0.16% | 0.61x |
| 10 | XBT/USD | 63.751 | 60841.8 | -0.19% | 0.67x |
| 11 | SUI/USD | 62.501 | 0.6551 | -0.15% | 0.31x |
| 12 | BNB/USD | 49.317 | 556.9 | -0.14% | 1.92x |

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

- Persisted scans: 1341; predictions: 11011; observations: 811777.
- Matured sampled outcomes across 1/6/24/48h: 16881; gap abstentions: 22369. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45075132589 · **Generation:** 1341 · **Legacy run:** 45075132589
**Main quote time:** 2026-11-22T22:01:14.676483+00:00 · **Legacy report time:** 2026-11-22T22:02:11.429871+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37529 | 92.45 | +0.18% | 1.36x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.04917 | 88.57 | +0.20% | 0.50x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 3 | PUMP/USD ⭐ | 0.002575 | 85.37 | +0.08% | 1.22x | STRONG 78/100 | HIGH 62/100 | Watch |
| 4 | STBL/USD | 0.017184 | 83.59 | +0.02% | 2.04x | STRONG 87/100 | HIGH 67/100 | Watch |
| 5 | ZEC/USD ⭐ | 795.51 | 76.10 | +0.42% | 1.34x | STRONG 93/100 | HIGH 55/100 | Watch |
| 6 | NEAR/USD | 2.9893 | 71.38 | -0.30% | 0.49x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | VVV/USD | 26.04 | 70.96 | -0.60% | 0.46x | WEAK 35/100 | VERY_HIGH 82/100 | Watch |
| 8 | ETH/USD | 1716.39 | 66.75 | -0.30% | 0.91x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | HYPE/USD | 62.57 | 63.88 | -0.16% | 0.61x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XBT/USD | 60841.8 | 59.55 | -0.19% | 0.67x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | BNB/USD | 556.9 | 57.83 | -0.14% | 1.92x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 12 | SUI/USD | 0.6551 | 54.82 | -0.15% | 0.31x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37506 | 80.38 | +0.18% | 1.36x | 17520 | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002569 | 78.10 | +0.08% | 1.22x | 4247 | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | ZEC/USD ⭐ | 793.56 | 71.32 | +0.42% | 1.34x | 18824 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, PUMP/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
