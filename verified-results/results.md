# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T11:40:43.384793+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44900148024
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 98f4062866c75cb5ebf5c12c80b0e770634b7df7 (atomic ledger/results publication)
**Ledger generation:** 1128 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | USELESS/USD | 0.07897 | 100.399 | 70.534 | +6.00% | +2.97% | 4.07x | 23.1 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | STRONG 95/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 21.904 | 100.160 | 91.350 | +5.62% | +0.45% | 1.66x | 5.9 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1651.99 | 88.628 | 69.092 | +2.02% | +0.91% | 3.59x | 0.1 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 470.13 | 80.003 | 70.386 | +3.03% | +1.34% | 1.29x | 11.7 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.4813 | 71.251 | 53.639 | +0.32% | +1.41% | 2.06x | 7.1 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | WINGS/USD | 0.001774 | 65.213 | 38.434 | +1.26% | +5.60% | 1.18x | 5.6 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 7 | AAVE/USD | 99.05 | 58.472 | 51.189 | +1.19% | +0.89% | 1.28x | 6.1 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 8 | TRX/USD | 0.302938 | 50.850 | 57.653 | +0.48% | +0.01% | 0.32x | 1.4 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SKY/USD | 0.04479 | 43.228 | 46.307 | +2.17% | +0.45% | 0.47x | 6.7 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | SENT/USD | 0.020926 | 32.427 | 38.431 | +1.61% | +0.04% | 0.38x | 7.7 | 2026-11-21T11:40:36.870472+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.350 | 21.904 | +0.45% | 1.66x |
| 2 | USELESS/USD | 70.534 | 0.07897 | +2.97% | 4.07x |
| 3 | XMR/USD | 70.386 | 470.13 | +1.34% | 1.29x |
| 4 | ETH/USD | 69.092 | 1651.99 | +0.91% | 3.59x |
| 5 | TRX/USD | 57.653 | 0.302938 | +0.01% | 0.32x |
| 6 | UNI/USD | 53.639 | 4.4813 | +1.41% | 2.06x |
| 7 | AAVE/USD | 51.189 | 99.05 | +0.89% | 1.28x |
| 8 | SKY/USD | 46.307 | 0.04479 | +0.45% | 0.47x |
| 9 | WINGS/USD | 38.434 | 0.001774 | +5.60% | 1.18x |
| 10 | SENT/USD | 38.431 | 0.020926 | +0.04% | 0.38x |

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

- Persisted scans: 1128; predictions: 8851; observations: 682183.
- Matured sampled outcomes across 1/6/24/48h: 11649; gap abstentions: 20351. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 12 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44900148024 · **Generation:** 1128 · **Legacy run:** 44900148024
**Main quote time:** 2026-11-21T11:40:43.384793+00:00 · **Legacy report time:** 2026-11-21T11:41:34.534040+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.07897 | 100.40 | +2.97% | 4.07x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 21.904 | 100.16 | +0.45% | 1.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1651.99 | 88.63 | +0.91% | 3.59x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 470.13 | 80.00 | +1.34% | 1.29x | STRONG 80/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.4813 | 71.25 | +1.41% | 2.06x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 6 | WINGS/USD | 0.001774 | 65.21 | +5.60% | 1.18x | MODERATE 68/100 | VERY_HIGH 77/100 | Watch |
| 7 | AAVE/USD ⭐ | 99.05 | 58.47 | +0.89% | 1.28x | STRONG 74/100 | HIGH 55/100 | Watch |
| 8 | TRX/USD | 0.302938 | 50.85 | +0.01% | 0.32x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 9 | SKY/USD | 0.04479 | 43.23 | +0.45% | 0.47x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 10 | SENT/USD | 0.020926 | 32.43 | +0.04% | 0.38x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD ⭐ | 0.07897 | 92.04 | +2.97% | 4.07x | 5000 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 21.901 | 88.97 | +0.45% | 1.66x | 14448 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1653.22 | 87.00 | +0.91% | 3.59x | 99978 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 471.14 | 83.51 | +1.34% | 1.29x | 11984 | STRONG 87/100 | HIGH 55/100 | Watch |
| 5 | ZEC/USD | 758.87 | 55.17 | +1.43% | 2.38x | 58470 | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | SOL/USD | 68.83 | 54.67 | +0.97% | 1.87x | 58056 | STRONG 72/100 | HIGH 55/100 | Watch |
| 7 | AAVE/USD ⭐ | 99.2 | 52.32 | +0.89% | 1.28x | 8282 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** USELESS/USD, VVV/USD, ETH/USD, XMR/USD, AAVE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
