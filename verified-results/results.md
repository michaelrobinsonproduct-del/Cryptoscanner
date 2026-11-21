# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T12:40:51.002443+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44905002926
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** d5e4ecd76baafca2594ac985e4c489b7134fe2ef (atomic ledger/results publication)
**Ledger generation:** 1134 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.675 | 116.368 | 96.250 | +9.34% | +1.21% | 2.41x | 7.5 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ETH/USD | 1662.54 | 78.679 | 73.653 | +2.67% | +0.46% | 1.27x | 0.1 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 467.69 | 75.763 | 64.466 | +2.50% | -0.74% | 3.23x | 16.0 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ZEC/USD | 768.47 | 72.948 | 59.680 | +1.39% | +0.08% | 2.29x | 10.1 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.4951 | 71.348 | 56.814 | +0.62% | -0.09% | 8.98x | 5.1 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ZAMA/USD | 0.05894 | 70.299 | 49.897 | +3.39% | +1.08% | 11.97x | 10.2 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | SOL/USD | 69.22 | 66.411 | 59.473 | +0.74% | +0.22% | 1.59x | 1.4 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 8 | AAVE/USD | 100.24 | 64.207 | 59.887 | +2.40% | +0.91% | 0.98x | 6.0 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 9 | TAO/USD | 182.6512 | 57.472 | 59.638 | +1.19% | +0.71% | 0.43x | 7.3 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | AKT/USD | 0.5077 | 54.059 | 37.577 | +0.75% | +0.30% | 4.49x | 2.0 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 11 | TRX/USD | 0.302629 | 52.204 | 57.001 | +0.37% | +0.06% | 0.49x | 1.2 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SENT/USD | 0.021041 | 47.924 | 42.611 | +2.17% | -0.36% | 1.71x | 7.1 | 2026-11-21T12:40:44.708204+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.250 | 22.675 | +1.21% | 2.41x |
| 2 | ETH/USD | 73.653 | 1662.54 | +0.46% | 1.27x |
| 3 | XMR/USD | 64.466 | 467.69 | -0.74% | 3.23x |
| 4 | AAVE/USD | 59.887 | 100.24 | +0.91% | 0.98x |
| 5 | ZEC/USD | 59.680 | 768.47 | +0.08% | 2.29x |
| 6 | TAO/USD | 59.638 | 182.6512 | +0.71% | 0.43x |
| 7 | SOL/USD | 59.473 | 69.22 | +0.22% | 1.59x |
| 8 | TRX/USD | 57.001 | 0.302629 | +0.06% | 0.49x |
| 9 | UNI/USD | 56.814 | 4.4951 | -0.09% | 8.98x |
| 10 | ZAMA/USD | 49.897 | 0.05894 | +1.08% | 11.97x |
| 11 | SENT/USD | 42.611 | 0.021041 | -0.36% | 1.71x |
| 12 | AKT/USD | 37.577 | 0.5077 | +0.30% | 4.49x |

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

- Persisted scans: 1134; predictions: 8919; observations: 685831.
- Matured sampled outcomes across 1/6/24/48h: 11714; gap abstentions: 20379. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44905002926 · **Generation:** 1134 · **Legacy run:** 44905002926
**Main quote time:** 2026-11-21T12:40:51.002443+00:00 · **Legacy report time:** 2026-11-21T12:41:54.262580+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.675 | 116.37 | +1.21% | 2.41x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1662.54 | 78.68 | +0.46% | 1.27x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD | 467.69 | 75.76 | -0.74% | 3.23x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 4 | ZEC/USD ⭐ | 768.47 | 72.95 | +0.08% | 2.29x | STRONG 86/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.4951 | 71.35 | -0.09% | 8.98x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 6 | ZAMA/USD ⭐ | 0.05894 | 70.30 | +1.08% | 11.97x | STRONG 95/100 | VERY_HIGH 73/100 | Watch |
| 7 | SOL/USD ⭐ | 69.22 | 66.41 | +0.22% | 1.59x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 8 | AAVE/USD | 100.24 | 64.21 | +0.91% | 0.98x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 9 | TAO/USD | 182.6512 | 57.47 | +0.71% | 0.43x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 10 | AKT/USD | 0.5077 | 54.06 | +0.30% | 4.49x | STRONG 82/100 | HIGH 60/100 | Watch |
| 11 | TRX/USD | 0.302629 | 52.20 | +0.06% | 0.49x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 12 | SENT/USD | 0.021041 | 47.92 | -0.36% | 1.71x | WEAK 44/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.707 | 94.25 | +1.21% | 2.41x | 14437 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1661.81 | 85.84 | +0.46% | 1.27x | 99872 | STRONG 88/100 | HIGH 55/100 | Watch |
| 3 | ZAMA/USD ⭐ | 0.05868 | 69.17 | +1.08% | 11.97x | 2879 | STRONG 95/100 | VERY_HIGH 73/100 | Watch |
| 4 | ZEC/USD ⭐ | 768.63 | 68.38 | +0.08% | 2.29x | 57483 | STRONG 89/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD ⭐ | 69.22 | 58.12 | +0.22% | 1.59x | 57886 | STRONG 84/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, ETH/USD, ZEC/USD, ZAMA/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
