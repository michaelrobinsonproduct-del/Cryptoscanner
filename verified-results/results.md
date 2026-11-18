# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:05:11.826601+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44331392018
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** d1f316816da377204dc80a8166356b7ff0a1dce3 (atomic ledger/results publication)
**Ledger generation:** 596 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1228 | 82.750 | 63.739 | +8.67% | +1.32% | 2.24x | 24.5 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | STRONG 86/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | STABLE/USD | 0.02318 | 79.143 | 60.887 | +10.12% | +0.65% | 4.60x | 30.3 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3863 | 67.346 | 50.918 | +3.48% | +0.29% | 2.57x | 13.0 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | STRONG 84/100 | HIGH 66/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01056455 | 62.851 | 61.478 | +5.81% | +1.28% | 0.50x | 25.7 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.309974 | 61.465 | 45.484 | +0.67% | +0.20% | 2.77x | 0.6 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SENT/USD | 0.019494 | 57.768 | 57.889 | +4.42% | -1.13% | 1.55x | 8.2 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04519 | 54.227 | 46.969 | +0.67% | -1.55% | 3.55x | 11.1 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.08281 | 53.814 | 39.658 | +0.83% | -0.17% | 8.82x | 3.6 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 9 | ZAMA/USD | 0.0606 | 46.183 | 32.828 | +1.12% | -0.33% | 3.95x | 13.2 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | AKT/USD | 0.5167 | 42.931 | 41.594 | +1.45% | -0.29% | 1.28x | 1.9 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | WEAK 31/100 | HIGH 66/100 | Do nothing | WATCH |
| 11 | XPL/USD | 0.0468 | 29.133 | 28.233 | +0.86% | +0.00% | 1.09x | 21.5 | 2026-11-18T15:05:06.285804+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CT/USD | 63.739 | 0.1228 | +1.32% | 2.24x |
| 2 | AKE/USD | 61.478 | 0.01056455 | +1.28% | 0.50x |
| 3 | STABLE/USD | 60.887 | 0.02318 | +0.65% | 4.60x |
| 4 | SENT/USD | 57.889 | 0.019494 | -1.13% | 1.55x |
| 5 | MNT/USD | 50.918 | 0.3863 | +0.29% | 2.57x |
| 6 | NIGHT/USD | 46.969 | 0.04519 | -1.55% | 3.55x |
| 7 | TRX/USD | 45.484 | 0.309974 | +0.20% | 2.77x |
| 8 | AKT/USD | 41.594 | 0.5167 | -0.29% | 1.28x |
| 9 | CC/USD | 39.658 | 0.08281 | -0.17% | 8.82x |
| 10 | ZAMA/USD | 32.828 | 0.0606 | -0.33% | 3.95x |
| 11 | XPL/USD | 28.233 | 0.0468 | +0.00% | 1.09x |

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

- Persisted scans: 596; predictions: 5088; observations: 359971.
- Matured sampled outcomes across 1/6/24/48h: 4306; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44331392018 · **Generation:** 596 · **Legacy run:** 44331392018
**Main quote time:** 2026-11-18T15:05:11.826601+00:00 · **Legacy report time:** 2026-11-18T15:05:37.081203+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1228 | 82.75 | +1.32% | 2.24x | STRONG 96/100 | VERY_HIGH 79/100 | Watch |
| 2 | STABLE/USD ⭐ | 0.02318 | 79.14 | +0.65% | 4.60x | STRONG 95/100 | VERY_HIGH 79/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3863 | 67.35 | +0.29% | 2.57x | STRONG 94/100 | HIGH 66/100 | Consider small entry |
| 4 | AKE/USD | 0.01056455 | 62.85 | +1.28% | 0.50x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 5 | TRX/USD ⭐ | 0.309974 | 61.47 | +0.20% | 2.77x | STRONG 86/100 | HIGH 55/100 | Watch |
| 6 | SENT/USD | 0.019494 | 57.77 | -1.13% | 1.55x | MODERATE 49/100 | VERY_HIGH 77/100 | Watch |
| 7 | NIGHT/USD | 0.04519 | 54.23 | -1.55% | 3.55x | MODERATE 52/100 | VERY_HIGH 71/100 | Do nothing |
| 8 | CC/USD | 0.08281 | 53.81 | -0.17% | 8.82x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 9 | ZAMA/USD | 0.0606 | 46.18 | -0.33% | 3.95x | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |
| 10 | AKT/USD | 0.5167 | 42.93 | -0.29% | 1.28x | WEAK 31/100 | HIGH 66/100 | Do nothing |
| 11 | XPL/USD | 0.0468 | 29.13 | +0.00% | 1.09x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.02318 | 80.56 | +0.65% | 4.60x | 2886 | STRONG 95/100 | VERY_HIGH 79/100 | Watch |
| 2 | CT/USD ⭐ | 0.1224 | 67.76 | +1.32% | 2.24x | 1230 | STRONG 89/100 | VERY_HIGH 79/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3863 | 67.52 | +0.29% | 2.57x | 2013 | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 4 | TRX/USD ⭐ | 0.309974 | 57.82 | +0.20% | 2.77x | 4253 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** CT/USD, STABLE/USD, MNT/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
