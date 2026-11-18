# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:50:09.269971+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44340080487
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 494ab8cec5e0f8e796e3fcaf3922cf08e4e580e4 (atomic ledger/results publication)
**Ledger generation:** 605 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STABLE/USD | 0.02299 | 74.884 | 60.752 | +9.22% | -0.17% | 4.21x | 30.5 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 85/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.019561 | 64.567 | 57.839 | +4.78% | -1.65% | 2.88x | 13.3 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 3 | AKE/USD | 0.01051297 | 62.439 | 55.819 | +5.30% | +1.11% | 1.11x | 29.6 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3827 | 54.942 | 44.088 | +2.52% | -0.83% | 4.08x | 13.1 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | CT/USD | 0.1181 | 51.099 | 50.091 | +4.51% | -2.80% | 5.79x | 25.3 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 89/100 | Do nothing | WATCH |
| 6 | ZAMA/USD | 0.06048 | 47.322 | 33.065 | +0.92% | -0.15% | 4.33x | 9.9 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309156 | 44.365 | 43.560 | +0.41% | -0.25% | 1.20x | 0.0 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | RE/USD | 0.23841 | 32.397 | 39.953 | +2.61% | -0.33% | 0.41x | 18.0 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | WEAK 16/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | FLR/USD | 0.00515 | 24.765 | 27.004 | +0.78% | -0.39% | 0.97x | 19.4 | 2026-11-18T15:50:03.694454+00:00 | Not calibrated | WEAK 12/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | STABLE/USD | 60.752 | 0.02299 | -0.17% | 4.21x |
| 2 | SENT/USD | 57.839 | 0.019561 | -1.65% | 2.88x |
| 3 | AKE/USD | 55.819 | 0.01051297 | +1.11% | 1.11x |
| 4 | CT/USD | 50.091 | 0.1181 | -2.80% | 5.79x |
| 5 | MNT/USD | 44.088 | 0.3827 | -0.83% | 4.08x |
| 6 | TRX/USD | 43.560 | 0.309156 | -0.25% | 1.20x |
| 7 | RE/USD | 39.953 | 0.23841 | -0.33% | 0.41x |
| 8 | ZAMA/USD | 33.065 | 0.06048 | -0.15% | 4.33x |
| 9 | FLR/USD | 27.004 | 0.00515 | -0.39% | 0.97x |

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

- Persisted scans: 605; predictions: 5190; observations: 365452.
- Matured sampled outcomes across 1/6/24/48h: 4395; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44340080487 · **Generation:** 605 · **Legacy run:** 44340080487
**Main quote time:** 2026-11-18T15:50:09.269971+00:00 · **Legacy report time:** 2026-11-18T15:50:28.979362+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD | 0.02299 | 74.88 | -0.17% | 4.21x | MODERATE 57/100 | EXTREME 85/100 | Do nothing |
| 2 | SENT/USD | 0.019561 | 64.57 | -1.65% | 2.88x | MODERATE 57/100 | VERY_HIGH 83/100 | Do nothing |
| 3 | AKE/USD ⭐ | 0.01051297 | 62.44 | +1.11% | 1.11x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 4 | MNT/USD | 0.3827 | 54.94 | -0.83% | 4.08x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 5 | CT/USD | 0.1181 | 51.10 | -2.80% | 5.79x | MODERATE 46/100 | EXTREME 89/100 | Do nothing |
| 6 | ZAMA/USD | 0.06048 | 47.32 | -0.15% | 4.33x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 7 | TRX/USD | 0.309156 | 44.37 | -0.25% | 1.20x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 8 | RE/USD | 0.23841 | 32.40 | -0.33% | 0.41x | WEAK 16/100 | EXTREME 94/100 | Do nothing |
| 9 | FLR/USD | 0.00515 | 24.77 | -0.39% | 0.97x | WEAK 12/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD ⭐ | 0.01051297 | 75.89 | +1.11% | 1.11x | 2837 | STRONG 73/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
