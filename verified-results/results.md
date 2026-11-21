# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T15:00:47.970138+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44916760956
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** c6e085ddebbad79ce75752db1196d1baef9f0bce (atomic ledger/results publication)
**Ledger generation:** 1148 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7177 | 86.311 | 90.755 | +5.61% | +0.24% | 0.44x | 7.0 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 791.3 | 82.224 | 82.491 | +4.41% | -0.10% | 1.02x | 6.7 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ETH/USD | 1688.06 | 81.207 | 84.685 | +4.25% | +0.23% | 0.54x | 0.1 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XMR/USD | 473.61 | 79.860 | 80.515 | +3.80% | +0.05% | 0.91x | 2.1 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | TAO/USD | 187.454 | 72.080 | 77.009 | +3.85% | -0.31% | 0.66x | 9.9 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 70.57 | 68.142 | 72.532 | +2.71% | +0.14% | 0.49x | 2.8 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XBT/USD | 60242.9 | 67.045 | 72.091 | +2.44% | +0.07% | 0.46x | 0.0 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.92897 | 64.912 | 70.122 | +2.23% | +0.15% | 0.40x | 1.0 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | AAVE/USD | 100.18 | 64.035 | 61.908 | +2.34% | -0.24% | 1.33x | 3.0 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0552317 | 63.279 | 67.312 | +1.76% | +0.04% | 0.58x | 0.1 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 2.899 | 60.468 | 66.793 | +1.98% | -0.01% | 0.37x | 4.1 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | TRX/USD | 0.304835 | 59.120 | 62.717 | +1.10% | -0.05% | 0.66x | 0.0 | 2026-11-21T15:00:41.851823+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 90.755 | 4.7177 | +0.24% | 0.44x |
| 2 | ETH/USD | 84.685 | 1688.06 | +0.23% | 0.54x |
| 3 | ZEC/USD | 82.491 | 791.3 | -0.10% | 1.02x |
| 4 | XMR/USD | 80.515 | 473.61 | +0.05% | 0.91x |
| 5 | TAO/USD | 77.009 | 187.454 | -0.31% | 0.66x |
| 6 | SOL/USD | 72.532 | 70.57 | +0.14% | 0.49x |
| 7 | XBT/USD | 72.091 | 60242.9 | +0.07% | 0.46x |
| 8 | XRP/USD | 70.122 | 0.92897 | +0.15% | 0.40x |
| 9 | XDG/USD | 67.312 | 0.0552317 | +0.04% | 0.58x |
| 10 | NEAR/USD | 66.793 | 2.899 | -0.01% | 0.37x |
| 11 | TRX/USD | 62.717 | 0.304835 | -0.05% | 0.66x |
| 12 | AAVE/USD | 61.908 | 100.18 | -0.24% | 1.33x |

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

- Persisted scans: 1148; predictions: 9085; observations: 694343.
- Matured sampled outcomes across 1/6/24/48h: 11940; gap abstentions: 20590. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44916760956 · **Generation:** 1148 · **Legacy run:** 44916760956
**Main quote time:** 2026-11-21T15:00:47.970138+00:00 · **Legacy report time:** 2026-11-21T15:01:52.489443+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.7177 | 86.31 | +0.24% | 0.44x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD | 791.3 | 82.22 | -0.10% | 1.02x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 3 | ETH/USD | 1688.06 | 81.21 | +0.23% | 0.54x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 4 | XMR/USD | 473.61 | 79.86 | +0.05% | 0.91x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | TAO/USD | 187.454 | 72.08 | -0.31% | 0.66x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 70.57 | 68.14 | +0.14% | 0.49x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 7 | XBT/USD | 60242.9 | 67.05 | +0.07% | 0.46x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.92897 | 64.91 | +0.15% | 0.40x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | AAVE/USD | 100.18 | 64.03 | -0.24% | 1.33x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | XDG/USD | 0.0552317 | 63.28 | +0.04% | 0.58x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 2.899 | 60.47 | -0.01% | 0.37x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | TRX/USD | 0.304835 | 59.12 | -0.05% | 0.66x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

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
