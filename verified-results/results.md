# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:55:15.488435+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44341034450
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ee69d713ff8b90679bc0c9ac1e6f2ce72edb9423 (atomic ledger/results publication)
**Ledger generation:** 606 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STABLE/USD | 0.02301 | 83.831 | 67.305 | +9.31% | +0.31% | 4.69x | 17.4 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019561 | 70.465 | 60.400 | +4.78% | -0.99% | 2.87x | 8.2 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | INFI/USD | 0.1409 | 69.031 | 65.824 | +10.94% | +2.10% | 0.27x | 21.3 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.119 | 62.045 | 59.936 | +5.31% | -1.16% | 1.79x | 16.8 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3841 | 61.319 | 48.006 | +2.89% | -0.34% | 4.42x | 10.4 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01041119 | 47.775 | 49.126 | +4.28% | +0.73% | 0.50x | 28.6 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | WEAK 44/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | ZAMA/USD | 0.06055 | 44.753 | 27.264 | +1.03% | +0.50% | 5.13x | 23.2 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | TRX/USD | 0.309141 | 37.189 | 43.542 | +0.40% | -0.18% | 0.45x | 0.0 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | CC/USD | 0.08236 | 36.263 | 33.886 | +0.28% | +0.05% | 1.21x | 7.3 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |
| 10 | FLR/USD | 0.00515 | 28.702 | 27.006 | +0.78% | -0.58% | 1.46x | 19.4 | 2026-11-18T15:55:10.350824+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | STABLE/USD | 67.305 | 0.02301 | +0.31% | 4.69x |
| 2 | INFI/USD | 65.824 | 0.1409 | +2.10% | 0.27x |
| 3 | SENT/USD | 60.400 | 0.019561 | -0.99% | 2.87x |
| 4 | CT/USD | 59.936 | 0.119 | -1.16% | 1.79x |
| 5 | AKE/USD | 49.126 | 0.01041119 | +0.73% | 0.50x |
| 6 | MNT/USD | 48.006 | 0.3841 | -0.34% | 4.42x |
| 7 | TRX/USD | 43.542 | 0.309141 | -0.18% | 0.45x |
| 8 | CC/USD | 33.886 | 0.08236 | +0.05% | 1.21x |
| 9 | ZAMA/USD | 27.264 | 0.06055 | +0.50% | 5.13x |
| 10 | FLR/USD | 27.006 | 0.00515 | -0.58% | 1.46x |

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

- Persisted scans: 606; predictions: 5200; observations: 366061.
- Matured sampled outcomes across 1/6/24/48h: 4406; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44341034450 · **Generation:** 606 · **Legacy run:** 44341034450
**Main quote time:** 2026-11-18T15:55:15.488435+00:00 · **Legacy report time:** 2026-11-18T15:55:46.216646+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.02301 | 83.83 | +0.31% | 4.69x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.019561 | 70.46 | -0.99% | 2.87x | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |
| 3 | INFI/USD | 0.1409 | 69.03 | +2.10% | 0.27x | MODERATE 55/100 | EXTREME 94/100 | Do nothing |
| 4 | CT/USD | 0.119 | 62.05 | -1.16% | 1.79x | MODERATE 46/100 | VERY_HIGH 83/100 | Watch |
| 5 | MNT/USD | 0.3841 | 61.32 | -0.34% | 4.42x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 6 | AKE/USD | 0.01041119 | 47.78 | +0.73% | 0.50x | WEAK 44/100 | EXTREME 87/100 | Do nothing |
| 7 | ZAMA/USD ⭐ | 0.06055 | 44.75 | +0.50% | 5.13x | STRONG 77/100 | VERY_HIGH 79/100 | Watch |
| 8 | TRX/USD | 0.309141 | 37.19 | -0.18% | 0.45x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | CC/USD | 0.08236 | 36.26 | +0.05% | 1.21x | WEAK 43/100 | HIGH 67/100 | Watch |
| 10 | FLR/USD | 0.00515 | 28.70 | -0.58% | 1.46x | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.02301 | 79.52 | +0.31% | 4.69x | 2823 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | ZAMA/USD ⭐ | 0.06055 | 44.87 | +0.50% | 5.13x | 3483 | STRONG 87/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** STABLE/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
