# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T05:41:41.977478+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45334859235
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c4b6d9009b9477d6d2eda982fb7140dd80eff249 (atomic ledger/results publication)
**Ledger generation:** 1532 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.58e-06 | 81.005 | 81.274 | +4.62% | +0.36% | 0.79x | 2.8 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 2 | VVV/USD | 25.09 | 69.383 | 70.390 | +2.63% | -0.27% | 1.04x | 6.0 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XRP/USD | 0.9576 | 68.566 | 67.838 | +1.94% | +0.77% | 0.69x | 1.5 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | BAT/USD | 0.08088 | 68.563 | 62.445 | +4.81% | +1.30% | 0.96x | 6.2 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 5 | XMR/USD | 494.17 | 67.872 | 62.180 | +1.68% | +0.10% | 1.52x | 9.1 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LTC/USD | 41.95 | 66.558 | 62.765 | +1.28% | +0.36% | 1.20x | 2.4 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.0374 | 66.230 | 66.385 | +1.89% | +0.54% | 0.72x | 3.6 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XLM/USD | 0.131045 | 65.992 | 59.208 | +0.81% | +0.48% | 1.44x | 2.9 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HYPE/USD | 64.29 | 61.004 | 61.372 | +1.02% | +0.58% | 0.67x | 1.6 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | DOT/USD | 0.6905 | 60.602 | 48.303 | +2.22% | +0.52% | 1.97x | 4.4 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 11 | WLD/USD | 0.2451 | 58.937 | 53.185 | +2.85% | +1.07% | 1.04x | 4.1 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 64/100 | HIGH 67/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0567471 | 58.473 | 58.830 | +0.79% | +0.48% | 0.73x | 3.3 | 2026-11-24T05:41:34.152699+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEPE/USD | 81.274 | 3.58e-06 | +0.36% | 0.79x |
| 2 | VVV/USD | 70.390 | 25.09 | -0.27% | 1.04x |
| 3 | XRP/USD | 67.838 | 0.9576 | +0.77% | 0.69x |
| 4 | NEAR/USD | 66.385 | 3.0374 | +0.54% | 0.72x |
| 5 | LTC/USD | 62.765 | 41.95 | +0.36% | 1.20x |
| 6 | BAT/USD | 62.445 | 0.08088 | +1.30% | 0.96x |
| 7 | XMR/USD | 62.180 | 494.17 | +0.10% | 1.52x |
| 8 | HYPE/USD | 61.372 | 64.29 | +0.58% | 0.67x |
| 9 | XLM/USD | 59.208 | 0.131045 | +0.48% | 1.44x |
| 10 | XDG/USD | 58.830 | 0.0567471 | +0.48% | 0.73x |
| 11 | WLD/USD | 53.185 | 0.2451 | +1.07% | 1.04x |
| 12 | DOT/USD | 48.303 | 0.6905 | +0.52% | 1.97x |

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

- Persisted scans: 1532; predictions: 13117; observations: 928086.
- Matured sampled outcomes across 1/6/24/48h: 24562; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
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

**Writer:** 45334859235 · **Generation:** 1532 · **Legacy run:** 45334859235
**Main quote time:** 2026-11-24T05:41:41.977478+00:00 · **Legacy report time:** 2026-11-24T05:42:37.315576+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.58e-06 | 81.00 | +0.36% | 0.79x | STRONG 71/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD | 25.09 | 69.38 | -0.27% | 1.04x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 3 | XRP/USD | 0.9576 | 68.57 | +0.77% | 0.69x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 4 | BAT/USD | 0.08088 | 68.56 | +1.30% | 0.96x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 5 | XMR/USD | 494.17 | 67.87 | +0.10% | 1.52x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD ⭐ | 41.95 | 66.56 | +0.36% | 1.20x | STRONG 78/100 | HIGH 62/100 | Watch |
| 7 | NEAR/USD | 3.0374 | 66.23 | +0.54% | 0.72x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | XLM/USD | 0.131045 | 65.99 | +0.48% | 1.44x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | HYPE/USD | 64.29 | 61.00 | +0.58% | 0.67x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | DOT/USD ⭐ | 0.6905 | 60.60 | +0.52% | 1.97x | STRONG 85/100 | HIGH 60/100 | Consider small entry |
| 11 | WLD/USD ⭐ | 0.2451 | 58.94 | +1.07% | 1.04x | STRONG 74/100 | HIGH 67/100 | Watch |
| 12 | XDG/USD | 0.0567471 | 58.47 | +0.48% | 0.73x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD | 0.00886 | 76.93 | +1.85% | 1.13x | 2917 | MODERATE 68/100 | VERY_HIGH 80/100 | Watch |
| 2 | WLD/USD ⭐ | 0.2451 | 69.60 | +1.07% | 1.04x | 5095 | STRONG 80/100 | HIGH 67/100 | Watch |
| 3 | DOT/USD ⭐ | 0.6898 | 67.91 | +0.52% | 1.97x | 9521 | STRONG 89/100 | HIGH 60/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 41.95 | 64.46 | +0.36% | 1.20x | 13091 | STRONG 77/100 | HIGH 62/100 | Watch |
| 5 | UNI/USD | 4.9208 | 64.17 | +0.29% | 1.30x | 9324 | STRONG 77/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD, DOT/USD, WLD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
