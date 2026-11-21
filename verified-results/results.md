# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T15:50:47.081349+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44921229356
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 2483b9fa47f766029e17d3e66d533d156967f2c9 (atomic ledger/results publication)
**Ledger generation:** 1153 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BEAM/USD | 0.003596 | 94.824 | 69.898 | +9.70% | +1.99% | 8.57x | 13.9 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 97/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 23.15 | 90.545 | 96.324 | +11.63% | +0.24% | 0.30x | 7.4 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XMR/USD | 477.57 | 86.660 | 82.931 | +4.66% | +1.29% | 0.73x | 9.4 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7096 | 85.909 | 91.284 | +5.43% | +0.49% | 0.22x | 3.4 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1683.31 | 83.208 | 82.632 | +3.95% | +0.38% | 0.87x | 0.1 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 6 | TAO/USD | 187.7282 | 81.124 | 80.566 | +4.00% | +0.14% | 0.98x | 4.9 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ZEC/USD | 791.03 | 80.910 | 83.691 | +4.37% | +0.89% | 0.28x | 3.8 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.92257 | 70.336 | 64.376 | +1.53% | +0.12% | 1.54x | 2.6 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.08219 | 69.339 | 71.942 | +10.32% | +0.62% | 0.43x | 26.7 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | SOL/USD | 70.36 | 68.134 | 71.099 | +2.40% | +0.31% | 0.55x | 1.4 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | CC/USD | 0.0766 | 67.391 | 58.029 | +2.75% | +0.04% | 1.92x | 2.6 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XBT/USD | 59920 | 66.870 | 68.247 | +1.89% | +0.30% | 0.71x | 0.0 | 2026-11-21T15:50:39.069585+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.324 | 23.15 | +0.24% | 0.30x |
| 2 | UNI/USD | 91.284 | 4.7096 | +0.49% | 0.22x |
| 3 | ZEC/USD | 83.691 | 791.03 | +0.89% | 0.28x |
| 4 | XMR/USD | 82.931 | 477.57 | +1.29% | 0.73x |
| 5 | ETH/USD | 82.632 | 1683.31 | +0.38% | 0.87x |
| 6 | TAO/USD | 80.566 | 187.7282 | +0.14% | 0.98x |
| 7 | USELESS/USD | 71.942 | 0.08219 | +0.62% | 0.43x |
| 8 | SOL/USD | 71.099 | 70.36 | +0.31% | 0.55x |
| 9 | BEAM/USD | 69.898 | 0.003596 | +1.99% | 8.57x |
| 10 | XBT/USD | 68.247 | 59920 | +0.30% | 0.71x |
| 11 | XRP/USD | 64.376 | 0.92257 | +0.12% | 1.54x |
| 12 | CC/USD | 58.029 | 0.0766 | +0.04% | 1.92x |

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

- Persisted scans: 1153; predictions: 9145; observations: 697383.
- Matured sampled outcomes across 1/6/24/48h: 12025; gap abstentions: 20700. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44921229356 · **Generation:** 1153 · **Legacy run:** 44921229356
**Main quote time:** 2026-11-21T15:50:47.081349+00:00 · **Legacy report time:** 2026-11-21T15:51:32.729961+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BEAM/USD | 0.003596 | 94.82 | +1.99% | 8.57x | STRONG 97/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD | 23.15 | 90.54 | +0.24% | 0.30x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 3 | XMR/USD | 477.57 | 86.66 | +1.29% | 0.73x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 4 | UNI/USD | 4.7096 | 85.91 | +0.49% | 0.22x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD | 1683.31 | 83.21 | +0.38% | 0.87x | STRONG 72/100 | HIGH 62/100 | Watch |
| 6 | TAO/USD | 187.7282 | 81.12 | +0.14% | 0.98x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 7 | ZEC/USD | 791.03 | 80.91 | +0.89% | 0.28x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.92257 | 70.34 | +0.12% | 1.54x | STRONG 70/100 | HIGH 55/100 | Watch |
| 9 | USELESS/USD | 0.08219 | 69.34 | +0.62% | 0.43x | MODERATE 55/100 | VERY_HIGH 82/100 | Watch |
| 10 | SOL/USD | 70.36 | 68.13 | +0.31% | 0.55x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 11 | CC/USD | 0.0766 | 67.39 | +0.04% | 1.92x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 12 | XBT/USD | 59920 | 66.87 | +0.30% | 0.71x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
