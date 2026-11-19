# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:05:26.252211+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44529869151
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 9a7f599146f846bfaa30601bbc1bcc4d492f7cd8 (atomic ledger/results publication)
**Ledger generation:** 778 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.975e-06 | 88.295 | 79.508 | +6.11% | -1.24% | 5.62x | 7.5 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | STRONG 74/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | VVV/USD | 22.799 | 88.087 | 88.586 | +5.21% | -0.39% | 1.14x | 5.7 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | MODERATE 54/100 | HIGH 68/100 | Watch | WATCH |
| 3 | HYPE/USD | 68.73 | 73.787 | 72.907 | +2.77% | +0.29% | 0.94x | 2.9 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XRP/USD | 0.98791 | 72.635 | 70.552 | +2.23% | +0.25% | 1.08x | 0.1 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5487 | 71.048 | 72.206 | +5.93% | +0.31% | 0.73x | 1.8 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | ZEC/USD | 947.16 | 70.614 | 79.915 | +3.86% | -0.20% | 0.17x | 4.2 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.3928 | 70.114 | 73.339 | +2.89% | -0.06% | 0.71x | 3.8 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SENT/USD | 0.022064 | 65.485 | 74.668 | +7.08% | -0.46% | 0.31x | 7.3 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | ETH/USD | 1804.51 | 62.959 | 66.706 | +1.68% | +0.02% | 0.62x | 0.1 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 63741.7 | 59.245 | 63.408 | +1.20% | -0.20% | 0.68x | 0.0 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | LINK/USD | 9.21799 | 57.064 | 65.568 | +1.60% | -0.08% | 0.19x | 1.3 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0595071 | 54.356 | 60.886 | +1.37% | -0.07% | 0.38x | 0.0 | 2026-11-19T13:05:19.529631+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 88.586 | 22.799 | -0.39% | 1.14x |
| 2 | ZEC/USD | 79.915 | 947.16 | -0.20% | 0.17x |
| 3 | PEPE/USD | 79.508 | 3.975e-06 | -1.24% | 5.62x |
| 4 | SENT/USD | 74.668 | 0.022064 | -0.46% | 0.31x |
| 5 | NEAR/USD | 73.339 | 3.3928 | -0.06% | 0.71x |
| 6 | HYPE/USD | 72.907 | 68.73 | +0.29% | 0.94x |
| 7 | AKT/USD | 72.206 | 0.5487 | +0.31% | 0.73x |
| 8 | XRP/USD | 70.552 | 0.98791 | +0.25% | 1.08x |
| 9 | ETH/USD | 66.706 | 1804.51 | +0.02% | 0.62x |
| 10 | LINK/USD | 65.568 | 9.21799 | -0.08% | 0.19x |
| 11 | XBT/USD | 63.408 | 63741.7 | -0.20% | 0.68x |
| 12 | XDG/USD | 60.886 | 0.0595071 | -0.07% | 0.38x |

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

- Persisted scans: 778; predictions: 6480; observations: 470774.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14916. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44529869151 · **Generation:** 778 · **Legacy run:** 44529869151
**Main quote time:** 2026-11-19T13:05:26.252211+00:00 · **Legacy report time:** 2026-11-19T13:06:07.589996+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.975e-06 | 88.30 | -1.24% | 5.62x | STRONG 74/100 | HIGH 65/100 | Do nothing |
| 2 | VVV/USD | 22.799 | 88.09 | -0.39% | 1.14x | MODERATE 54/100 | HIGH 68/100 | Watch |
| 3 | HYPE/USD | 68.73 | 73.79 | +0.29% | 0.94x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.98791 | 72.64 | +0.25% | 1.08x | STRONG 81/100 | HIGH 62/100 | Watch |
| 5 | AKT/USD | 0.5487 | 71.05 | +0.31% | 0.73x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 6 | ZEC/USD | 947.16 | 70.61 | -0.20% | 0.17x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | NEAR/USD | 3.3928 | 70.11 | -0.06% | 0.71x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 8 | SENT/USD | 0.022064 | 65.49 | -0.46% | 0.31x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 9 | ETH/USD | 1804.51 | 62.96 | +0.02% | 0.62x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 63741.7 | 59.25 | -0.20% | 0.68x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | LINK/USD | 9.21799 | 57.06 | -0.08% | 0.19x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0595071 | 54.36 | -0.07% | 0.38x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.98896 | 80.93 | +0.25% | 1.08x | 34417 | STRONG 85/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
