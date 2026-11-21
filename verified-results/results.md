# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T19:51:29.001774+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44942996446
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 0df5266b64204a2d201f8506864b1f25bdd650f1 (atomic ledger/results publication)
**Ledger generation:** 1178 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 790.21 | 96.914 | 82.427 | +4.26% | -0.10% | 2.86x | 4.8 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 483.9 | 91.316 | 93.225 | +6.05% | +0.24% | 0.69x | 8.3 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XRP/USD | 0.93598 | 91.152 | 75.579 | +3.00% | +0.11% | 2.66x | 0.9 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.0452 | 85.349 | 90.039 | +7.06% | +0.24% | 0.41x | 6.6 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.9662 | 84.699 | 79.104 | +7.54% | +1.21% | 0.95x | 23.4 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | UNI/USD | 4.687 | 82.904 | 87.843 | +4.92% | +0.02% | 0.50x | 3.2 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1685.33 | 82.597 | 83.505 | +4.08% | +0.15% | 0.83x | 0.1 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XBT/USD | 60300 | 69.609 | 72.771 | +2.54% | +0.09% | 0.64x | 0.0 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SOL/USD | 70.52 | 69.261 | 72.731 | +2.63% | -0.16% | 0.73x | 1.4 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XLM/USD | 0.12933 | 65.309 | 66.020 | +1.67% | +0.12% | 0.87x | 1.4 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0552054 | 65.138 | 66.991 | +1.71% | +0.13% | 0.75x | 0.0 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PAXG/USD | 3555.39 | 64.647 | 54.339 | +0.68% | +0.08% | 1.99x | 0.6 | 2026-11-21T19:51:21.250011+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 93.225 | 483.9 | +0.24% | 0.69x |
| 2 | NIGHT/USD | 90.039 | 0.0452 | +0.24% | 0.41x |
| 3 | UNI/USD | 87.843 | 4.687 | +0.02% | 0.50x |
| 4 | ETH/USD | 83.505 | 1685.33 | +0.15% | 0.83x |
| 5 | ZEC/USD | 82.427 | 790.21 | -0.10% | 2.86x |
| 6 | PEARL/USD | 79.104 | 1.9662 | +1.21% | 0.95x |
| 7 | XRP/USD | 75.579 | 0.93598 | +0.11% | 2.66x |
| 8 | XBT/USD | 72.771 | 60300 | +0.09% | 0.64x |
| 9 | SOL/USD | 72.731 | 70.52 | -0.16% | 0.73x |
| 10 | XDG/USD | 66.991 | 0.0552054 | +0.13% | 0.75x |
| 11 | XLM/USD | 66.020 | 0.12933 | +0.12% | 0.87x |
| 12 | PAXG/USD | 54.339 | 3555.39 | +0.08% | 1.99x |

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

- Persisted scans: 1178; predictions: 9445; observations: 712583.
- Matured sampled outcomes across 1/6/24/48h: 12532; gap abstentions: 21244. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44942996446 · **Generation:** 1178 · **Legacy run:** 44942996446
**Main quote time:** 2026-11-21T19:51:29.001774+00:00 · **Legacy report time:** 2026-11-21T19:52:19.775487+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 790.21 | 96.91 | -0.10% | 2.86x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 483.9 | 91.32 | +0.24% | 0.69x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 3 | XRP/USD ⭐ | 0.93598 | 91.15 | +0.11% | 2.66x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD | 0.0452 | 85.35 | +0.24% | 0.41x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 5 | PEARL/USD | 1.9662 | 84.70 | +1.21% | 0.95x | MODERATE 62/100 | VERY_HIGH 74/100 | Watch |
| 6 | UNI/USD | 4.687 | 82.90 | +0.02% | 0.50x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1685.33 | 82.60 | +0.15% | 0.83x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 8 | XBT/USD | 60300 | 69.61 | +0.09% | 0.64x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 9 | SOL/USD | 70.52 | 69.26 | -0.16% | 0.73x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 10 | XLM/USD | 0.12933 | 65.31 | +0.12% | 0.87x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0552054 | 65.14 | +0.13% | 0.75x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 12 | PAXG/USD | 3555.39 | 64.65 | +0.08% | 1.99x | MODERATE 67/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.93547 | 93.46 | +0.11% | 2.66x | 54802 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SHX/USD | 0.003518 | 88.58 | +0.31% | 2.78x | 2704 | STRONG 99/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
