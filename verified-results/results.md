# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T03:15:54.951826+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45747638710
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fd2ed2b8a8f1779536a6920937fa1accc1d8f95c (atomic ledger/results publication)
**Ledger generation:** 1805 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 184.9855 | 80.814 | 65.078 | +1.87% | +0.15% | 2.64x | 6.0 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | TIA/USD | 0.3511 | 75.797 | 59.368 | +4.34% | +0.29% | 4.30x | 5.7 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | STRONG 93/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | XBT/USD | 60677.6 | 74.038 | 58.575 | +0.51% | +0.09% | 2.76x | 0.0 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.0705 | 73.060 | 68.894 | +6.38% | +0.27% | 1.28x | 15.6 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | MODERATE 67/100 | HIGH 66/100 | Watch | WATCH |
| 5 | ETH/USD | 1696.54 | 72.556 | 57.509 | +0.36% | +0.01% | 2.79x | 0.1 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 61.89 | 71.428 | 57.259 | +0.44% | +0.75% | 2.04x | 1.6 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XRP/USD | 0.95675 | 69.721 | 70.038 | +2.16% | +0.20% | 0.87x | 0.1 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148329 | 66.126 | 67.255 | +1.76% | +0.13% | 0.82x | 0.1 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.538e-06 | 64.454 | 54.662 | +1.55% | +0.40% | 1.78x | 2.8 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 10 | LTC/USD | 43.56 | 62.224 | 67.783 | +1.99% | +0.28% | 0.31x | 2.3 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SOL/USD | 71.18 | 58.195 | 62.154 | +1.12% | +0.14% | 0.53x | 1.4 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ZEC/USD | 777.47 | 58.153 | 60.182 | +0.94% | +0.36% | 0.61x | 2.8 | 2026-11-26T03:15:48.646121+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 70.038 | 0.95675 | +0.20% | 0.87x |
| 2 | SYRUP/USD | 68.894 | 0.0705 | +0.27% | 1.28x |
| 3 | LTC/USD | 67.783 | 43.56 | +0.28% | 0.31x |
| 4 | ADA/USD | 67.255 | 0.148329 | +0.13% | 0.82x |
| 5 | TAO/USD | 65.078 | 184.9855 | +0.15% | 2.64x |
| 6 | SOL/USD | 62.154 | 71.18 | +0.14% | 0.53x |
| 7 | ZEC/USD | 60.182 | 777.47 | +0.36% | 0.61x |
| 8 | TIA/USD | 59.368 | 0.3511 | +0.29% | 4.30x |
| 9 | XBT/USD | 58.575 | 60677.6 | +0.09% | 2.76x |
| 10 | ETH/USD | 57.509 | 1696.54 | +0.01% | 2.79x |
| 11 | HYPE/USD | 57.259 | 61.89 | +0.75% | 2.04x |
| 12 | PEPE/USD | 54.662 | 3.538e-06 | +0.40% | 1.78x |

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

- Persisted scans: 1805; predictions: 15395; observations: 1094289.
- Matured sampled outcomes across 1/6/24/48h: 33419; gap abstentions: 23759. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45747638710 · **Generation:** 1805 · **Legacy run:** 45747638710
**Main quote time:** 2026-11-26T03:15:54.951826+00:00 · **Legacy report time:** 2026-11-26T03:16:58.723803+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 184.9855 | 80.81 | +0.15% | 2.64x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | TIA/USD ⭐ | 0.3511 | 75.80 | +0.29% | 4.30x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | XBT/USD | 60677.6 | 74.04 | +0.09% | 2.76x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | SYRUP/USD ⭐ | 0.0705 | 73.06 | +0.27% | 1.28x | STRONG 77/100 | HIGH 66/100 | Watch |
| 5 | ETH/USD | 1696.54 | 72.56 | +0.01% | 2.79x | STRONG 81/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 61.89 | 71.43 | +0.75% | 2.04x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD | 0.95675 | 69.72 | +0.20% | 0.87x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 8 | ADA/USD | 0.148329 | 66.13 | +0.13% | 0.82x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 9 | PEPE/USD | 3.538e-06 | 64.45 | +0.40% | 1.78x | STRONG 77/100 | HIGH 55/100 | Watch |
| 10 | LTC/USD | 43.56 | 62.22 | +0.28% | 0.31x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | SOL/USD | 71.18 | 58.20 | +0.14% | 0.53x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | ZEC/USD | 777.47 | 58.15 | +0.36% | 0.61x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TIA/USD ⭐ | 0.3508 | 83.55 | +0.29% | 4.30x | 4101 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SYRUP/USD ⭐ | 0.07038 | 73.17 | +0.27% | 1.28x | 3524 | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** TIA/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
