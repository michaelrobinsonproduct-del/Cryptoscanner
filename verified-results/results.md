# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T18:31:06.547065+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44935814277
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** d3446ab96a8163ac8dbc1f3d54909c69fc04e3f2 (atomic ledger/results publication)
**Ledger generation:** 1170 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.731 | 92.543 | 95.175 | +5.91% | +0.38% | 0.55x | 2.3 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ETH/USD | 1681.81 | 88.553 | 81.984 | +3.86% | +0.25% | 1.53x | 0.1 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 789.96 | 86.224 | 82.196 | +4.23% | +0.81% | 1.00x | 4.8 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04507 | 85.931 | 89.387 | +6.75% | -1.37% | 1.34x | 6.7 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | MODERATE 63/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | XMR/USD | 479.07 | 82.371 | 86.927 | +4.99% | -0.59% | 0.84x | 6.0 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 6 | TAO/USD | 186.7756 | 80.505 | 76.879 | +3.47% | +0.25% | 1.24x | 4.8 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.9945 | 76.194 | 76.699 | +9.09% | +1.16% | 0.37x | 30.2 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | QNT/USD | 143.31 | 74.550 | 74.811 | +3.28% | +0.24% | 0.85x | 6.3 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 60096.1 | 74.418 | 70.344 | +2.19% | +0.23% | 1.29x | 0.0 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 70.65 | 70.790 | 74.056 | +2.82% | +0.11% | 0.62x | 1.4 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PAXG/USD | 3547.99 | 69.869 | 57.219 | +0.47% | +0.06% | 2.24x | 0.0 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XLM/USD | 0.128912 | 69.614 | 64.377 | +1.35% | +0.27% | 1.39x | 0.1 | 2026-11-21T18:30:58.698917+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 95.175 | 4.731 | +0.38% | 0.55x |
| 2 | NIGHT/USD | 89.387 | 0.04507 | -1.37% | 1.34x |
| 3 | XMR/USD | 86.927 | 479.07 | -0.59% | 0.84x |
| 4 | ZEC/USD | 82.196 | 789.96 | +0.81% | 1.00x |
| 5 | ETH/USD | 81.984 | 1681.81 | +0.25% | 1.53x |
| 6 | TAO/USD | 76.879 | 186.7756 | +0.25% | 1.24x |
| 7 | PEARL/USD | 76.699 | 1.9945 | +1.16% | 0.37x |
| 8 | QNT/USD | 74.811 | 143.31 | +0.24% | 0.85x |
| 9 | SOL/USD | 74.056 | 70.65 | +0.11% | 0.62x |
| 10 | XBT/USD | 70.344 | 60096.1 | +0.23% | 1.29x |
| 11 | XLM/USD | 64.377 | 0.128912 | +0.27% | 1.39x |
| 12 | PAXG/USD | 57.219 | 3547.99 | +0.06% | 2.24x |

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

- Persisted scans: 1170; predictions: 9349; observations: 707719.
- Matured sampled outcomes across 1/6/24/48h: 12346; gap abstentions: 21096. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44935814277 · **Generation:** 1170 · **Legacy run:** 44935814277
**Main quote time:** 2026-11-21T18:31:06.547065+00:00 · **Legacy report time:** 2026-11-21T18:31:59.257540+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.731 | 92.54 | +0.38% | 0.55x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 2 | ETH/USD ⭐ | 1681.81 | 88.55 | +0.25% | 1.53x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD | 789.96 | 86.22 | +0.81% | 1.00x | STRONG 73/100 | HIGH 62/100 | Watch |
| 4 | NIGHT/USD | 0.04507 | 85.93 | -1.37% | 1.34x | MODERATE 63/100 | HIGH 65/100 | Do nothing |
| 5 | XMR/USD | 479.07 | 82.37 | -0.59% | 0.84x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 6 | TAO/USD ⭐ | 186.7756 | 80.50 | +0.25% | 1.24x | STRONG 85/100 | HIGH 62/100 | Watch |
| 7 | PEARL/USD | 1.9945 | 76.19 | +1.16% | 0.37x | MODERATE 58/100 | VERY_HIGH 82/100 | Watch |
| 8 | QNT/USD | 143.31 | 74.55 | +0.24% | 0.85x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD ⭐ | 60096.1 | 74.42 | +0.23% | 1.29x | STRONG 82/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD | 70.65 | 70.79 | +0.11% | 0.62x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 11 | PAXG/USD | 3547.99 | 69.87 | +0.06% | 2.24x | STRONG 80/100 | HIGH 55/100 | Watch |
| 12 | XLM/USD | 0.128912 | 69.61 | +0.27% | 1.39x | STRONG 80/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1681.24 | 100.00 | +0.25% | 1.53x | 83079 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 186.7321 | 84.10 | +0.25% | 1.24x | 12575 | STRONG 87/100 | HIGH 62/100 | Watch |
| 3 | XBT/USD ⭐ | 60045.4 | 79.11 | +0.23% | 1.29x | 236175 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ETH/USD, TAO/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
