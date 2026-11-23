# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T08:42:26.637315+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45140404098
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f6617cfcd8a8645df547ad3caad2c64bbba37686 (atomic ledger/results publication)
**Ledger generation:** 1406 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.93891 | 80.140 | 63.208 | +1.23% | +0.39% | 2.57x | 0.7 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 499.27 | 78.305 | 62.783 | +1.13% | +0.10% | 14.64x | 0.2 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SOL/USD | 72.37 | 78.286 | 71.554 | +2.46% | +0.25% | 1.55x | 1.4 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | GBP/USD | 1.31373 | 70.049 | 57.252 | +0.36% | +0.12% | 2.22x | 0.5 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | JUP/USD | 0.24499 | 69.615 | 73.949 | +9.09% | +0.47% | 0.33x | 11.9 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0555455 | 66.804 | 51.245 | +0.47% | +0.11% | 22.71x | 0.6 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 61424.3 | 63.623 | 57.901 | +0.42% | +0.43% | 1.36x | 0.0 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 8 | QNT/USD | 147.38 | 62.857 | 59.380 | +2.75% | -0.05% | 1.37x | 6.8 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ALGO/USD | 0.07865 | 62.271 | 60.040 | +4.27% | +0.56% | 0.94x | 7.6 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 10 | ADA/USD | 0.146111 | 59.822 | 54.919 | +1.04% | +0.14% | 1.42x | 2.3 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6666 | 58.490 | 65.136 | +1.66% | -0.08% | 0.37x | 3.0 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | KAS/USD | 0.02703 | 57.425 | 59.732 | +4.73% | +0.15% | 0.70x | 14.8 | 2026-11-23T08:42:18.299295+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 73.949 | 0.24499 | +0.47% | 0.33x |
| 2 | SOL/USD | 71.554 | 72.37 | +0.25% | 1.55x |
| 3 | SUI/USD | 65.136 | 0.6666 | -0.08% | 0.37x |
| 4 | XRP/USD | 63.208 | 0.93891 | +0.39% | 2.57x |
| 5 | XMR/USD | 62.783 | 499.27 | +0.10% | 14.64x |
| 6 | ALGO/USD | 60.040 | 0.07865 | +0.56% | 0.94x |
| 7 | KAS/USD | 59.732 | 0.02703 | +0.15% | 0.70x |
| 8 | QNT/USD | 59.380 | 147.38 | -0.05% | 1.37x |
| 9 | XBT/USD | 57.901 | 61424.3 | +0.43% | 1.36x |
| 10 | GBP/USD | 57.252 | 1.31373 | +0.12% | 2.22x |
| 11 | ADA/USD | 54.919 | 0.146111 | +0.14% | 1.42x |
| 12 | XDG/USD | 51.245 | 0.0555455 | +0.11% | 22.71x |

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

- Persisted scans: 1406; predictions: 11639; observations: 851357.
- Matured sampled outcomes across 1/6/24/48h: 19008; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 129 (sampled only; not a success-rate estimate).
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

**Writer:** 45140404098 · **Generation:** 1406 · **Legacy run:** 45140404098
**Main quote time:** 2026-11-23T08:42:26.637315+00:00 · **Legacy report time:** 2026-11-23T08:43:35.474881+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.93891 | 80.14 | +0.39% | 2.57x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 499.27 | 78.30 | +0.10% | 14.64x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 72.37 | 78.29 | +0.25% | 1.55x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | GBP/USD | 1.31373 | 70.05 | +0.12% | 2.22x | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | JUP/USD | 0.24499 | 69.61 | +0.47% | 0.33x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 6 | XDG/USD | 0.0555455 | 66.80 | +0.11% | 22.71x | STRONG 78/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD | 61424.3 | 63.62 | +0.43% | 1.36x | STRONG 77/100 | HIGH 55/100 | Watch |
| 8 | QNT/USD | 147.38 | 62.86 | -0.05% | 1.37x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 9 | ALGO/USD | 0.07865 | 62.27 | +0.56% | 0.94x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 10 | ADA/USD | 0.146111 | 59.82 | +0.14% | 1.42x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 11 | SUI/USD | 0.6666 | 58.49 | -0.08% | 0.37x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | KAS/USD | 0.02703 | 57.42 | +0.15% | 0.70x | WEAK 44/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.37 | 81.74 | +0.25% | 1.55x | 29803 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.93958 | 73.31 | +0.39% | 2.57x | 21020 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | POL/USD | 0.07819 | 67.88 | +0.06% | 4.49x | 1288 | STRONG 79/100 | HIGH 67/100 | Watch |
| 4 | HYPE/USD | 63.56 | 62.93 | +0.65% | 1.65x | 9916 | STRONG 76/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
