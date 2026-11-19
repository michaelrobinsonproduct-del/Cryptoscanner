# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:20:28.009651+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44532334884
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** bb657e7b6412befe755a73b40d3a778524cf8166 (atomic ledger/results publication)
**Ledger generation:** 781 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LIGHTER/USD | 2.939 | 94.478 | 77.943 | +8.29% | +0.31% | 3.73x | 6.8 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | PEPE/USD | 3.957e-06 | 90.343 | 77.356 | +5.63% | -0.40% | 2.58x | 5.0 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98704 | 84.542 | 69.922 | +2.14% | -0.08% | 3.05x | 0.1 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 22.825 | 82.962 | 89.207 | +5.33% | +0.14% | 0.31x | 6.1 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ADA/USD | 0.155245 | 75.156 | 72.472 | +2.64% | +0.50% | 1.02x | 2.0 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.4031 | 72.944 | 75.087 | +3.21% | +0.24% | 0.66x | 4.7 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 68.66 | 72.424 | 72.902 | +2.66% | -0.10% | 1.00x | 1.5 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 943.07 | 71.386 | 77.456 | +3.41% | -0.43% | 0.61x | 2.9 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ETH/USD | 1803.36 | 64.887 | 66.253 | +1.61% | -0.07% | 0.90x | 0.1 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XBT/USD | 63691.4 | 61.450 | 62.849 | +1.12% | -0.07% | 0.89x | 0.0 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SOL/USD | 74.7 | 60.654 | 65.372 | +1.58% | +0.01% | 0.52x | 1.3 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SENT/USD | 0.02185 | 60.578 | 73.054 | +6.04% | -0.86% | 0.18x | 5.0 | 2026-11-19T13:20:20.207727+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 89.207 | 22.825 | +0.14% | 0.31x |
| 2 | LIGHTER/USD | 77.943 | 2.939 | +0.31% | 3.73x |
| 3 | ZEC/USD | 77.456 | 943.07 | -0.43% | 0.61x |
| 4 | PEPE/USD | 77.356 | 3.957e-06 | -0.40% | 2.58x |
| 5 | NEAR/USD | 75.087 | 3.4031 | +0.24% | 0.66x |
| 6 | SENT/USD | 73.054 | 0.02185 | -0.86% | 0.18x |
| 7 | HYPE/USD | 72.902 | 68.66 | -0.10% | 1.00x |
| 8 | ADA/USD | 72.472 | 0.155245 | +0.50% | 1.02x |
| 9 | XRP/USD | 69.922 | 0.98704 | -0.08% | 3.05x |
| 10 | ETH/USD | 66.253 | 1803.36 | -0.07% | 0.90x |
| 11 | SOL/USD | 65.372 | 74.7 | +0.01% | 0.52x |
| 12 | XBT/USD | 62.849 | 63691.4 | -0.07% | 0.89x |

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

- Persisted scans: 781; predictions: 6516; observations: 472551.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14952. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44532334884 · **Generation:** 781 · **Legacy run:** 44532334884
**Main quote time:** 2026-11-19T13:20:28.009651+00:00 · **Legacy report time:** 2026-11-19T13:21:11.057182+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.939 | 94.48 | +0.31% | 3.73x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | PEPE/USD | 3.957e-06 | 90.34 | -0.40% | 2.58x | STRONG 75/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.98704 | 84.54 | -0.08% | 3.05x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 22.825 | 82.96 | +0.14% | 0.31x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 5 | ADA/USD ⭐ | 0.155245 | 75.16 | +0.50% | 1.02x | STRONG 83/100 | HIGH 62/100 | Watch |
| 6 | NEAR/USD | 3.4031 | 72.94 | +0.24% | 0.66x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD | 68.66 | 72.42 | -0.10% | 1.00x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD | 943.07 | 71.39 | -0.43% | 0.61x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 9 | ETH/USD | 1803.36 | 64.89 | -0.07% | 0.90x | WEAK 37/100 | HIGH 68/100 | Watch |
| 10 | XBT/USD | 63691.4 | 61.45 | -0.07% | 0.89x | WEAK 36/100 | HIGH 68/100 | Watch |
| 11 | SOL/USD | 74.7 | 60.65 | +0.01% | 0.52x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | SENT/USD | 0.02185 | 60.58 | -0.86% | 0.18x | WEAK 35/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.264 | 87.20 | +0.72% | 1.14x | 6653 | STRONG 79/100 | HIGH 62/100 | Watch |
| 2 | LIGHTER/USD ⭐ | 2.942 | 82.73 | +0.31% | 3.73x | 3814 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | LUNA/USD | 4.619e-05 | 79.38 | +1.01% | 1.80x | 4700 | STRONG 70/100 | VERY_HIGH 72/100 | Watch |
| 4 | ADA/USD ⭐ | 0.155239 | 75.01 | +0.50% | 1.02x | 11926 | STRONG 83/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LIGHTER/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
