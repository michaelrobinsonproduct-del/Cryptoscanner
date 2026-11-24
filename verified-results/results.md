# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T12:52:31.531672+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45397264523
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9f399954ba8732ea097d833634c62b04f2af62d9 (atomic ledger/results publication)
**Ledger generation:** 1576 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.719 | 89.140 | 88.666 | +5.20% | +0.77% | 0.66x | 5.5 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | MON/USD | 0.01228 | 70.855 | 78.873 | +6.60% | -0.81% | 0.60x | 16.3 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XMR/USD | 499.13 | 70.763 | 65.367 | +2.70% | +0.13% | 1.48x | 17.0 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PAXG/USD | 3633.7 | 65.674 | 49.039 | +0.35% | +0.33% | 2.98x | 1.2 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04895 | 60.494 | 57.993 | +1.66% | +0.72% | 0.89x | 4.1 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 6 | GBP/USD | 1.30945 | 60.354 | 58.025 | +0.48% | +0.07% | 1.20x | 0.6 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.441e-06 | 46.885 | 54.428 | +0.56% | +0.15% | 0.17x | 2.9 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | AUD/USD | 0.66451 | 41.377 | 49.262 | +0.29% | +0.04% | 0.19x | 0.9 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | 2Z/USD | 0.01602 | 40.790 | 44.163 | +2.36% | -0.62% | 0.97x | 6.2 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 10 | XAUT/USD | 3631.3 | 29.282 | 34.886 | +0.33% | +0.28% | 0.30x | 0.3 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | BABY/USD | 0.00857 | 28.863 | 32.610 | +0.82% | +0.35% | 0.45x | 11.7 | 2026-11-24T12:52:24.219106+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 88.666 | 25.719 | +0.77% | 0.66x |
| 2 | MON/USD | 78.873 | 0.01228 | -0.81% | 0.60x |
| 3 | XMR/USD | 65.367 | 499.13 | +0.13% | 1.48x |
| 4 | GBP/USD | 58.025 | 1.30945 | +0.07% | 1.20x |
| 5 | NIGHT/USD | 57.993 | 0.04895 | +0.72% | 0.89x |
| 6 | PEPE/USD | 54.428 | 3.441e-06 | +0.15% | 0.17x |
| 7 | AUD/USD | 49.262 | 0.66451 | +0.04% | 0.19x |
| 8 | PAXG/USD | 49.039 | 3633.7 | +0.33% | 2.98x |
| 9 | 2Z/USD | 44.163 | 0.01602 | -0.62% | 0.97x |
| 10 | XAUT/USD | 34.886 | 3631.3 | +0.28% | 0.30x |
| 11 | BABY/USD | 32.610 | 0.00857 | +0.35% | 0.45x |

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

- Persisted scans: 1576; predictions: 13598; observations: 954882.
- Matured sampled outcomes across 1/6/24/48h: 26429; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45397264523 · **Generation:** 1576 · **Legacy run:** 45397264523
**Main quote time:** 2026-11-24T12:52:31.531672+00:00 · **Legacy report time:** 2026-11-24T12:53:25.691471+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.719 | 89.14 | +0.77% | 0.66x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 2 | MON/USD | 0.01228 | 70.86 | -0.81% | 0.60x | WEAK 35/100 | VERY_HIGH 82/100 | Watch |
| 3 | XMR/USD ⭐ | 499.13 | 70.76 | +0.13% | 1.48x | STRONG 75/100 | HIGH 61/100 | Watch |
| 4 | PAXG/USD ⭐ | 3633.7 | 65.67 | +0.33% | 2.98x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | NIGHT/USD | 0.04895 | 60.49 | +0.72% | 0.89x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 6 | GBP/USD ⭐ | 1.30945 | 60.35 | +0.07% | 1.20x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 7 | PEPE/USD | 3.441e-06 | 46.88 | +0.15% | 0.17x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 8 | AUD/USD | 0.66451 | 41.38 | +0.04% | 0.19x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 9 | 2Z/USD | 0.01602 | 40.79 | -0.62% | 0.97x | WEAK 25/100 | VERY_HIGH 80/100 | Do nothing |
| 10 | XAUT/USD | 3631.3 | 29.28 | +0.28% | 0.30x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 11 | BABY/USD | 0.00857 | 28.86 | +0.35% | 0.45x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 499.5 | 72.57 | +0.13% | 1.48x | 10978 | STRONG 76/100 | HIGH 61/100 | Watch |
| 2 | GBP/USD ⭐ | 1.30933 | 57.22 | +0.07% | 1.20x | 22350 | MODERATE 64/100 | HIGH 62/100 | Watch |
| 3 | PAXG/USD ⭐ | 3633.7 | 55.96 | +0.33% | 2.98x | 4442 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, PAXG/USD, GBP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
