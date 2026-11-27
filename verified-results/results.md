# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T19:22:14.612825+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46055887368
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1dd2eac8828934aaf0f8ed4f88d461036858b35e (atomic ledger/results publication)
**Ledger generation:** 2049 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 747.62 | 94.230 | 98.594 | +9.68% | +0.13% | 0.50x | 2.8 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.93 | 88.848 | 72.674 | +2.75% | +0.23% | 6.01x | 3.1 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.8265 | 80.724 | 77.169 | +3.79% | +0.12% | 1.30x | 3.7 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0578333 | 76.555 | 72.967 | +2.59% | +0.24% | 1.24x | 0.3 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LINK/USD | 9.40157 | 73.416 | 64.619 | +1.44% | +0.07% | 1.84x | 0.9 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.05007 | 72.758 | 77.109 | +3.30% | +0.32% | 0.40x | 2.0 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.536e-06 | 72.733 | 56.034 | +1.67% | +0.34% | 3.12x | 2.8 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | PAXG/USD | 3632.91 | 72.620 | 57.286 | +2.14% | +0.07% | 4.38x | 0.7 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95138 | 70.921 | 61.355 | +0.92% | +0.12% | 1.90x | 0.1 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 72.08 | 67.858 | 65.555 | +1.61% | +0.21% | 1.13x | 1.4 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 11 | PIEVERSE/USD | 4.2266 | 67.213 | 73.454 | +8.79% | +0.34% | 0.20x | 18.0 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | SPACE/USD | 0.004255 | 62.778 | 71.163 | +9.89% | -0.70% | 0.51x | 9.4 | 2026-11-27T19:22:08.655541+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.594 | 747.62 | +0.13% | 0.50x |
| 2 | UNI/USD | 77.169 | 4.8265 | +0.12% | 1.30x |
| 3 | NIGHT/USD | 77.109 | 0.05007 | +0.32% | 0.40x |
| 4 | PIEVERSE/USD | 73.454 | 4.2266 | +0.34% | 0.20x |
| 5 | XDG/USD | 72.967 | 0.0578333 | +0.24% | 1.24x |
| 6 | HYPE/USD | 72.674 | 63.93 | +0.23% | 6.01x |
| 7 | SPACE/USD | 71.163 | 0.004255 | -0.70% | 0.51x |
| 8 | SOL/USD | 65.555 | 72.08 | +0.21% | 1.13x |
| 9 | LINK/USD | 64.619 | 9.40157 | +0.07% | 1.84x |
| 10 | XRP/USD | 61.355 | 0.95138 | +0.12% | 1.90x |
| 11 | PAXG/USD | 57.286 | 3632.91 | +0.07% | 4.38x |
| 12 | PEPE/USD | 56.034 | 3.536e-06 | +0.34% | 3.12x |

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

- Persisted scans: 2049; predictions: 18290; observations: 1240754.
- Matured sampled outcomes across 1/6/24/48h: 41243; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46055887368 · **Generation:** 2049 · **Legacy run:** 46055887368
**Main quote time:** 2026-11-27T19:22:14.612825+00:00 · **Legacy report time:** 2026-11-27T19:22:54.376123+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 747.62 | 94.23 | +0.13% | 0.50x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD ⭐ | 63.93 | 88.85 | +0.23% | 6.01x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.8265 | 80.72 | +0.12% | 1.30x | STRONG 75/100 | HIGH 55/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0578333 | 76.56 | +0.24% | 1.24x | STRONG 83/100 | HIGH 62/100 | Watch |
| 5 | LINK/USD | 9.40157 | 73.42 | +0.07% | 1.84x | STRONG 72/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.05007 | 72.76 | +0.32% | 0.40x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | PEPE/USD | 3.536e-06 | 72.73 | +0.34% | 3.12x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 8 | PAXG/USD ⭐ | 3632.91 | 72.62 | +0.07% | 4.38x | STRONG 91/100 | HIGH 55/100 | Watch |
| 9 | XRP/USD | 0.95138 | 70.92 | +0.12% | 1.90x | STRONG 70/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD ⭐ | 72.08 | 67.86 | +0.21% | 1.13x | STRONG 79/100 | HIGH 62/100 | Watch |
| 11 | PIEVERSE/USD | 4.2266 | 67.21 | +0.34% | 0.20x | MODERATE 59/100 | VERY_HIGH 76/100 | Watch |
| 12 | SPACE/USD | 0.004255 | 62.78 | -0.70% | 0.51x | WEAK 36/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 63.93 | 90.56 | +0.23% | 6.01x | 20919 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.8265 | 89.27 | +0.12% | 1.30x | 10073 | STRONG 80/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0578812 | 85.54 | +0.24% | 1.24x | 13171 | STRONG 88/100 | HIGH 62/100 | Watch |
| 4 | ENA/USD | 0.1041 | 80.13 | +0.19% | 7.12x | 2669 | STRONG 85/100 | HIGH 55/100 | Watch |
| 5 | PAXG/USD ⭐ | 3632.93 | 76.69 | +0.07% | 4.38x | 4670 | STRONG 93/100 | HIGH 55/100 | Watch |
| 6 | SOL/USD ⭐ | 72.09 | 69.81 | +0.21% | 1.13x | 45379 | STRONG 80/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD, UNI/USD, XDG/USD, PAXG/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
