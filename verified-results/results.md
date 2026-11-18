# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T12:55:08.072662+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44308417858
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 145a3592305c94e987fc7d4cd22ba81a80c59ad6 (atomic ledger/results publication)
**Ledger generation:** 570 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04653 | 65.034 | 62.644 | +3.65% | -0.02% | 1.25x | 23.7 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.019529 | 63.322 | 59.706 | +4.61% | +0.63% | 1.05x | 7.2 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | USELESS/USD | 0.10028 | 61.641 | 51.744 | +2.77% | +0.62% | 1.68x | 19.1 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 4 | STABLE/USD | 0.02318 | 50.567 | 60.837 | +10.12% | -0.86% | 0.40x | 30.3 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 20/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | ME/USD | 0.0403 | 45.810 | 49.934 | +4.40% | +0.00% | 0.59x | 24.8 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 33/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | MNT/USD | 0.3848 | 44.428 | 48.063 | +3.08% | -0.44% | 0.86x | 13.0 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5181 | 44.394 | 38.744 | +1.73% | -0.02% | 1.57x | 11.6 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | TRX/USD | 0.309662 | 39.458 | 45.127 | +0.57% | +0.06% | 0.40x | 0.5 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | CC/USD | 0.083 | 39.173 | 41.024 | +1.06% | -0.31% | 0.97x | 4.8 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | VVV/USD | 21.156 | 35.657 | 43.687 | +0.62% | -0.30% | 0.35x | 17.6 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | CAP/USD | 0.101543 | 35.274 | 30.158 | +0.56% | +0.17% | 1.43x | 10.2 | 2026-11-18T12:55:02.762338+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 62.644 | 0.04653 | -0.02% | 1.25x |
| 2 | STABLE/USD | 60.837 | 0.02318 | -0.86% | 0.40x |
| 3 | SENT/USD | 59.706 | 0.019529 | +0.63% | 1.05x |
| 4 | USELESS/USD | 51.744 | 0.10028 | +0.62% | 1.68x |
| 5 | ME/USD | 49.934 | 0.0403 | +0.00% | 0.59x |
| 6 | MNT/USD | 48.063 | 0.3848 | -0.44% | 0.86x |
| 7 | TRX/USD | 45.127 | 0.309662 | +0.06% | 0.40x |
| 8 | VVV/USD | 43.687 | 21.156 | -0.30% | 0.35x |
| 9 | CC/USD | 41.024 | 0.083 | -0.31% | 0.97x |
| 10 | AKT/USD | 38.744 | 0.5181 | -0.02% | 1.57x |
| 11 | CAP/USD | 30.158 | 0.101543 | +0.17% | 1.43x |

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

- Persisted scans: 570; predictions: 4813; observations: 344137.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 12973. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44308417858 · **Generation:** 570 · **Legacy run:** 44308417858
**Main quote time:** 2026-11-18T12:55:08.072662+00:00 · **Legacy report time:** 2026-11-18T12:55:31.933385+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04653 | 65.03 | -0.02% | 1.25x | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing |
| 2 | SENT/USD ⭐ | 0.019529 | 63.32 | +0.63% | 1.05x | STRONG 77/100 | VERY_HIGH 74/100 | Watch |
| 3 | USELESS/USD ⭐ | 0.10028 | 61.64 | +0.62% | 1.68x | STRONG 81/100 | HIGH 61/100 | Consider small entry |
| 4 | STABLE/USD | 0.02318 | 50.57 | -0.86% | 0.40x | WEAK 20/100 | EXTREME 100/100 | Do nothing |
| 5 | ME/USD | 0.0403 | 45.81 | +0.00% | 0.59x | WEAK 33/100 | EXTREME 94/100 | Do nothing |
| 6 | MNT/USD | 0.3848 | 44.43 | -0.44% | 0.86x | WEAK 22/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | AKT/USD | 0.5181 | 44.39 | -0.02% | 1.57x | WEAK 37/100 | VERY_HIGH 72/100 | Watch |
| 8 | TRX/USD | 0.309662 | 39.46 | +0.06% | 0.40x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 9 | CC/USD | 0.083 | 39.17 | -0.31% | 0.97x | WEAK 25/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | VVV/USD | 21.156 | 35.66 | -0.30% | 0.35x | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | CAP/USD ⭐ | 0.101543 | 35.27 | +0.17% | 1.43x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019529 | 72.70 | +0.63% | 1.05x | 5612 | STRONG 81/100 | VERY_HIGH 74/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.10028 | 66.93 | +0.62% | 1.68x | 5314 | STRONG 83/100 | HIGH 61/100 | Consider small entry |
| 3 | CAP/USD ⭐ | 0.101543 | 34.03 | +0.17% | 1.43x | 2575 | MODERATE 62/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, USELESS/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
