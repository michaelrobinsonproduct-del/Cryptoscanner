# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T08:31:55.882558+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45966070554
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 281d8bd74145efd1f3a1a967624a3b15bf66960e (atomic ledger/results publication)
**Ledger generation:** 1983 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 745.89 | 94.767 | 99.933 | +9.42% | +0.42% | 0.27x | 0.1 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | INJ/USD | 6.494 | 89.419 | 69.688 | +4.88% | +0.95% | 3.04x | 4.6 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ADA/USD | 0.152908 | 87.488 | 71.093 | +3.00% | +0.28% | 5.79x | 4.3 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 65.49 | 82.895 | 90.263 | +5.26% | -0.23% | 0.38x | 3.1 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0581422 | 80.607 | 68.033 | +3.14% | -0.09% | 2.30x | 1.7 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XBT/USD | 61731.1 | 80.258 | 69.260 | +2.04% | -0.05% | 2.13x | 0.0 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.9787 | 80.227 | 81.080 | +3.81% | +0.19% | 0.82x | 1.2 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 9.58716 | 76.350 | 77.242 | +3.44% | +0.11% | 0.86x | 3.7 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SOL/USD | 73.11 | 76.077 | 75.729 | +3.06% | +0.07% | 1.00x | 1.4 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 10 | PAXG/USD | 3658.27 | 74.647 | 58.993 | +2.85% | +0.13% | 8.52x | 1.2 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 11 | UNI/USD | 4.8948 | 74.245 | 81.161 | +5.26% | +0.08% | 0.27x | 0.2 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6865 | 72.119 | 73.252 | +2.82% | +0.25% | 0.76x | 2.9 | 2026-11-27T08:31:47.544314+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.933 | 745.89 | +0.42% | 0.27x |
| 2 | HYPE/USD | 90.263 | 65.49 | -0.23% | 0.38x |
| 3 | UNI/USD | 81.161 | 4.8948 | +0.08% | 0.27x |
| 4 | XRP/USD | 81.080 | 0.9787 | +0.19% | 0.82x |
| 5 | LINK/USD | 77.242 | 9.58716 | +0.11% | 0.86x |
| 6 | SOL/USD | 75.729 | 73.11 | +0.07% | 1.00x |
| 7 | SUI/USD | 73.252 | 0.6865 | +0.25% | 0.76x |
| 8 | ADA/USD | 71.093 | 0.152908 | +0.28% | 5.79x |
| 9 | INJ/USD | 69.688 | 6.494 | +0.95% | 3.04x |
| 10 | XBT/USD | 69.260 | 61731.1 | -0.05% | 2.13x |
| 11 | XDG/USD | 68.033 | 0.0581422 | -0.09% | 2.30x |
| 12 | PAXG/USD | 58.993 | 3658.27 | +0.13% | 8.52x |

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

- Persisted scans: 1983; predictions: 17498; observations: 1200902.
- Matured sampled outcomes across 1/6/24/48h: 38729; gap abstentions: 25681. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45966070554 · **Generation:** 1983 · **Legacy run:** 45966070554
**Main quote time:** 2026-11-27T08:31:55.882558+00:00 · **Legacy report time:** 2026-11-27T08:32:48.766347+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 745.89 | 94.77 | +0.42% | 0.27x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 2 | INJ/USD ⭐ | 6.494 | 89.42 | +0.95% | 3.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.152908 | 87.49 | +0.28% | 5.79x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD | 65.49 | 82.89 | -0.23% | 0.38x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 5 | XDG/USD | 0.0581422 | 80.61 | -0.09% | 2.30x | STRONG 70/100 | HIGH 61/100 | Watch |
| 6 | XBT/USD | 61731.1 | 80.26 | -0.05% | 2.13x | STRONG 70/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.9787 | 80.23 | +0.19% | 0.82x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD | 9.58716 | 76.35 | +0.11% | 0.86x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 9 | SOL/USD ⭐ | 73.11 | 76.08 | +0.07% | 1.00x | STRONG 73/100 | HIGH 62/100 | Watch |
| 10 | PAXG/USD ⭐ | 3658.27 | 74.65 | +0.13% | 8.52x | STRONG 92/100 | HIGH 55/100 | Watch |
| 11 | UNI/USD | 4.8948 | 74.24 | +0.08% | 0.27x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6865 | 72.12 | +0.25% | 0.76x | MODERATE 66/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.152909 | 92.55 | +0.28% | 5.79x | 9808 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.513 | 88.31 | +0.95% | 3.04x | 5093 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 73.12 | 86.35 | +0.07% | 1.00x | 33783 | STRONG 78/100 | HIGH 62/100 | Watch |
| 4 | PAXG/USD ⭐ | 3658.27 | 81.19 | +0.13% | 8.52x | 2328 | STRONG 96/100 | HIGH 55/100 | Watch |
| 5 | FET/USD | 0.1263 | 77.09 | +0.72% | 1.52x | 2710 | STRONG 79/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** INJ/USD, ADA/USD, SOL/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
