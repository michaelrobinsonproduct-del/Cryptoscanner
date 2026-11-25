# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T23:46:20.320296+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45723658939
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 748dc871e535b3bf0c88e326efdb9697e8abbb4b (atomic ledger/results publication)
**Ledger generation:** 1783 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0131 | 90.571 | 84.383 | +4.46% | +0.21% | 1.52x | 3.7 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 762.77 | 86.086 | 76.115 | +3.23% | +0.71% | 1.64x | 3.0 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 42.49 | 82.830 | 81.926 | +4.01% | +0.40% | 0.89x | 2.4 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.3 | 65.155 | 70.087 | +2.39% | +0.36% | 0.33x | 3.3 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XMR/USD | 521.32 | 63.420 | 68.701 | +2.30% | +0.20% | 0.37x | 4.8 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6645 | 63.385 | 71.872 | +2.63% | +0.21% | 0.05x | 3.0 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1690.19 | 60.694 | 60.178 | +0.74% | +0.24% | 0.93x | 0.1 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ONDO/USD | 0.28161 | 60.247 | 44.411 | +1.32% | +0.17% | 6.98x | 1.1 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93538 | 59.317 | 63.707 | +1.27% | +0.31% | 0.41x | 0.4 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 60265.7 | 56.085 | 61.136 | +0.88% | +0.34% | 0.32x | 0.0 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TAO/USD | 181.1491 | 54.318 | 53.597 | +0.26% | +0.26% | 0.94x | 6.4 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PAXG/USD | 3571.77 | 54.011 | 60.429 | +0.85% | +0.36% | 0.18x | 1.0 | 2026-11-25T23:46:12.452384+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 84.383 | 3.0131 | +0.21% | 1.52x |
| 2 | LTC/USD | 81.926 | 42.49 | +0.40% | 0.89x |
| 3 | ZEC/USD | 76.115 | 762.77 | +0.71% | 1.64x |
| 4 | SUI/USD | 71.872 | 0.6645 | +0.21% | 0.05x |
| 5 | HYPE/USD | 70.087 | 61.3 | +0.36% | 0.33x |
| 6 | XMR/USD | 68.701 | 521.32 | +0.20% | 0.37x |
| 7 | XRP/USD | 63.707 | 0.93538 | +0.31% | 0.41x |
| 8 | XBT/USD | 61.136 | 60265.7 | +0.34% | 0.32x |
| 9 | PAXG/USD | 60.429 | 3571.77 | +0.36% | 0.18x |
| 10 | ETH/USD | 60.178 | 1690.19 | +0.24% | 0.93x |
| 11 | TAO/USD | 53.597 | 181.1491 | +0.26% | 0.94x |
| 12 | ONDO/USD | 44.411 | 0.28161 | +0.17% | 6.98x |

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

- Persisted scans: 1783; predictions: 15140; observations: 1080891.
- Matured sampled outcomes across 1/6/24/48h: 32916; gap abstentions: 23414. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45723658939 · **Generation:** 1783 · **Legacy run:** 45723658939
**Main quote time:** 2026-11-25T23:46:20.320296+00:00 · **Legacy report time:** 2026-11-25T23:47:24.059896+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0131 | 90.57 | +0.21% | 1.52x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 762.77 | 86.09 | +0.71% | 1.64x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD | 42.49 | 82.83 | +0.40% | 0.89x | STRONG 71/100 | HIGH 62/100 | Watch |
| 4 | HYPE/USD | 61.3 | 65.16 | +0.36% | 0.33x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 5 | XMR/USD | 521.32 | 63.42 | +0.20% | 0.37x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 6 | SUI/USD | 0.6645 | 63.39 | +0.21% | 0.05x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1690.19 | 60.69 | +0.24% | 0.93x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 8 | ONDO/USD | 0.28161 | 60.25 | +0.17% | 6.98x | STRONG 75/100 | HIGH 60/100 | Watch |
| 9 | XRP/USD | 0.93538 | 59.32 | +0.31% | 0.41x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 60265.7 | 56.08 | +0.34% | 0.32x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | TAO/USD | 181.1491 | 54.32 | +0.26% | 0.94x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 12 | PAXG/USD | 3571.77 | 54.01 | +0.36% | 0.18x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0152 | 97.37 | +0.21% | 1.52x | 17305 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 762.56 | 89.11 | +0.71% | 1.64x | 43310 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XLM/USD | 0.127638 | 82.66 | +0.29% | 6.03x | 8260 | STRONG 96/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NEAR/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
