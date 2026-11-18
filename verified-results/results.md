# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:40:14.361363+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44361104320
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 4d57062c7a5d9b15fbe36fecb7f350a368e27cef (atomic ledger/results publication)
**Ledger generation:** 626 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020006 | 73.193 | 59.289 | +7.16% | +0.68% | 2.05x | 33.6 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | STRONG 82/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04516 | 68.665 | 50.717 | +0.60% | +1.90% | 1.85x | 4.4 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | TRUST/USD | 0.04988 | 61.816 | 64.803 | +5.79% | +0.54% | 0.43x | 16.0 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3847 | 52.040 | 47.998 | +3.05% | -0.31% | 1.56x | 10.4 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05365 | 50.819 | 47.217 | +3.89% | +0.32% | 1.20x | 22.3 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | XPL/USD | 0.0467 | 29.533 | 27.177 | +0.65% | +0.00% | 1.24x | 21.5 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | ZAMA/USD | 0.0606 | 27.170 | 33.572 | +1.12% | +0.38% | 0.17x | 11.6 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | WEAK 39/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | FLR/USD | 0.00516 | 27.014 | 28.242 | +0.98% | -0.19% | 0.97x | 19.4 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | WEAK 14/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | AKE/USD | 0.01003651 | 22.341 | 26.193 | +0.52% | -0.50% | 0.87x | 22.2 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | WEAK 6/100 | EXTREME 85/100 | Do nothing | WATCH |
| 10 | AKT/USD | 0.5108 | 21.237 | 28.199 | +0.29% | +0.22% | 0.20x | 11.8 | 2026-11-18T17:40:10.258550+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TRUST/USD | 64.803 | 0.04988 | +0.54% | 0.43x |
| 2 | SENT/USD | 59.289 | 0.020006 | +0.68% | 2.05x |
| 3 | NIGHT/USD | 50.717 | 0.04516 | +1.90% | 1.85x |
| 4 | MNT/USD | 47.998 | 0.3847 | -0.31% | 1.56x |
| 5 | MEGA/USD | 47.217 | 0.05365 | +0.32% | 1.20x |
| 6 | ZAMA/USD | 33.572 | 0.0606 | +0.38% | 0.17x |
| 7 | FLR/USD | 28.242 | 0.00516 | -0.19% | 0.97x |
| 8 | AKT/USD | 28.199 | 0.5108 | +0.22% | 0.20x |
| 9 | XPL/USD | 27.177 | 0.0467 | +0.00% | 1.24x |
| 10 | AKE/USD | 26.193 | 0.01003651 | -0.50% | 0.87x |

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

- Persisted scans: 626; predictions: 5346; observations: 378241.
- Matured sampled outcomes across 1/6/24/48h: 4634; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44361104320 · **Generation:** 626 · **Legacy run:** 44361104320
**Main quote time:** 2026-11-18T17:40:14.361363+00:00 · **Legacy report time:** 2026-11-18T17:40:46.002702+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020006 | 73.19 | +0.68% | 2.05x | STRONG 92/100 | VERY_HIGH 79/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04516 | 68.67 | +1.90% | 1.85x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 3 | TRUST/USD | 0.04988 | 61.82 | +0.54% | 0.43x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 4 | MNT/USD | 0.3847 | 52.04 | -0.31% | 1.56x | WEAK 41/100 | VERY_HIGH 72/100 | Watch |
| 5 | MEGA/USD ⭐ | 0.05365 | 50.82 | +0.32% | 1.20x | MODERATE 60/100 | EXTREME 86/100 | Do nothing |
| 6 | XPL/USD | 0.0467 | 29.53 | +0.00% | 1.24x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | ZAMA/USD | 0.0606 | 27.17 | +0.38% | 0.17x | WEAK 39/100 | EXTREME 88/100 | Do nothing |
| 8 | FLR/USD | 0.00516 | 27.01 | -0.19% | 0.97x | WEAK 14/100 | EXTREME 86/100 | Do nothing |
| 9 | AKE/USD | 0.01003651 | 22.34 | -0.50% | 0.87x | WEAK 6/100 | EXTREME 85/100 | Do nothing |
| 10 | AKT/USD | 0.5108 | 21.24 | +0.22% | 0.20x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020006 | 76.89 | +0.68% | 2.05x | 5991 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05365 | 59.12 | +0.32% | 1.20x | 1196 | STRONG 70/100 | VERY_HIGH 80/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04516 | 51.22 | +1.90% | 1.85x | 16170 | STRONG 81/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SENT/USD, NIGHT/USD, MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
