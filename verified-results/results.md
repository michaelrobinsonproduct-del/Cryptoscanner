# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T12:12:31.073075+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46143264352
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 47c0cc8ed134326ad3471bfcf27b5e3fae22e706 (atomic ledger/results publication)
**Ledger generation:** 2152 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 437.94 | 88.079 | 83.166 | +7.53% | +0.64% | 1.17x | 33.7 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05425 | 86.485 | 94.768 | +7.98% | -1.21% | 0.78x | 7.4 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 3 | VVV/USD | 27.182 | 84.100 | 78.874 | +5.57% | +0.51% | 1.27x | 7.7 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004424 | 66.816 | 68.244 | +5.89% | -1.30% | 1.51x | 9.0 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.024528 | 59.249 | 52.213 | +3.43% | -1.59% | 2.76x | 6.5 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 6 | AKE/USD | 0.00113334 | 48.442 | 57.363 | +4.31% | -0.71% | 0.46x | 18.6 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | WEAK 24/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.07454 | 32.368 | 32.851 | +0.53% | +0.36% | 0.77x | 9.4 | 2026-11-28T12:12:26.618321+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 94.768 | 0.05425 | -1.21% | 0.78x |
| 2 | XMR/USD | 83.166 | 437.94 | +0.64% | 1.17x |
| 3 | VVV/USD | 78.874 | 27.182 | +0.51% | 1.27x |
| 4 | SPACE/USD | 68.244 | 0.004424 | -1.30% | 1.51x |
| 5 | AKE/USD | 57.363 | 0.00113334 | -0.71% | 0.46x |
| 6 | SENT/USD | 52.213 | 0.024528 | -1.59% | 2.76x |
| 7 | CC/USD | 32.851 | 0.07454 | +0.36% | 0.77x |

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

- Persisted scans: 2152; predictions: 19187; observations: 1303158.
- Matured sampled outcomes across 1/6/24/48h: 45776; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46143264352 · **Generation:** 2152 · **Legacy run:** 46143264352
**Main quote time:** 2026-11-28T12:12:31.073075+00:00 · **Legacy report time:** 2026-11-28T12:13:07.881334+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 437.94 | 88.08 | +0.64% | 1.17x | STRONG 79/100 | VERY_HIGH 74/100 | Watch |
| 2 | NIGHT/USD | 0.05425 | 86.49 | -1.21% | 0.78x | MODERATE 48/100 | VERY_HIGH 72/100 | Do nothing |
| 3 | VVV/USD ⭐ | 27.182 | 84.10 | +0.51% | 1.27x | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | SPACE/USD | 0.004424 | 66.82 | -1.30% | 1.51x | MODERATE 53/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | SENT/USD | 0.024528 | 59.25 | -1.59% | 2.76x | MODERATE 60/100 | VERY_HIGH 77/100 | Do nothing |
| 6 | AKE/USD | 0.00113334 | 48.44 | -0.71% | 0.46x | WEAK 24/100 | EXTREME 87/100 | Do nothing |
| 7 | CC/USD | 0.07454 | 32.37 | +0.36% | 0.77x | MODERATE 46/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 437.94 | 87.61 | +0.64% | 1.17x | 17130 | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD ⭐ | 27.217 | 80.88 | +0.51% | 1.27x | 7612 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
