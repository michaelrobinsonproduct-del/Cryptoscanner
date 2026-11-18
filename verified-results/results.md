# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:45:10.494778+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44339128848
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 8992e8a3aed5a5f92ad402659a82ea0983896b32 (atomic ledger/results publication)
**Ledger generation:** 604 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STABLE/USD | 0.02301 | 77.541 | 62.975 | +9.31% | -0.09% | 4.49x | 26.1 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | MODERATE 59/100 | EXTREME 85/100 | Do nothing | WATCH |
| 2 | CT/USD | 0.1202 | 71.470 | 67.455 | +6.37% | -2.20% | 4.78x | 16.6 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 3 | PEARL/USD | 1.9526 | 70.539 | 75.366 | +7.85% | +0.50% | 0.27x | 19.0 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | SENT/USD | 0.019623 | 69.316 | 63.267 | +5.11% | -1.14% | 2.18x | 7.1 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 5 | AKE/USD | 0.0104783 | 57.824 | 52.971 | +4.95% | +0.62% | 1.18x | 30.4 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | MNT/USD | 0.3838 | 51.827 | 47.477 | +2.81% | -0.54% | 1.71x | 10.4 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309483 | 47.427 | 44.039 | +0.51% | -0.16% | 1.42x | 0.7 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 8 | RE/USD | 0.23855 | 33.213 | 41.215 | +2.67% | -0.72% | 0.56x | 16.4 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | WEAK 17/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | FLR/USD | 0.00515 | 24.670 | 27.015 | +0.78% | -0.77% | 1.15x | 19.4 | 2026-11-18T15:45:05.417928+00:00 | Not calibrated | WEAK 17/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 75.366 | 1.9526 | +0.50% | 0.27x |
| 2 | CT/USD | 67.455 | 0.1202 | -2.20% | 4.78x |
| 3 | SENT/USD | 63.267 | 0.019623 | -1.14% | 2.18x |
| 4 | STABLE/USD | 62.975 | 0.02301 | -0.09% | 4.49x |
| 5 | AKE/USD | 52.971 | 0.0104783 | +0.62% | 1.18x |
| 6 | MNT/USD | 47.477 | 0.3838 | -0.54% | 1.71x |
| 7 | TRX/USD | 44.039 | 0.309483 | -0.16% | 1.42x |
| 8 | RE/USD | 41.215 | 0.23855 | -0.72% | 0.56x |
| 9 | FLR/USD | 27.015 | 0.00515 | -0.77% | 1.15x |

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

- Persisted scans: 604; predictions: 5181; observations: 364843.
- Matured sampled outcomes across 1/6/24/48h: 4383; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44339128848 · **Generation:** 604 · **Legacy run:** 44339128848
**Main quote time:** 2026-11-18T15:45:10.494778+00:00 · **Legacy report time:** 2026-11-18T15:45:35.316146+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD | 0.02301 | 77.54 | -0.09% | 4.49x | MODERATE 59/100 | EXTREME 85/100 | Do nothing |
| 2 | CT/USD | 0.1202 | 71.47 | -2.20% | 4.78x | MODERATE 61/100 | VERY_HIGH 83/100 | Do nothing |
| 3 | PEARL/USD | 1.9526 | 70.54 | +0.50% | 0.27x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 4 | SENT/USD | 0.019623 | 69.32 | -1.14% | 2.18x | MODERATE 65/100 | VERY_HIGH 77/100 | Watch |
| 5 | AKE/USD ⭐ | 0.0104783 | 57.82 | +0.62% | 1.18x | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |
| 6 | MNT/USD | 0.3838 | 51.83 | -0.54% | 1.71x | WEAK 41/100 | VERY_HIGH 72/100 | Watch |
| 7 | TRX/USD | 0.309483 | 47.43 | -0.16% | 1.42x | WEAK 44/100 | HIGH 61/100 | Watch |
| 8 | RE/USD | 0.23855 | 33.21 | -0.72% | 0.56x | WEAK 17/100 | EXTREME 94/100 | Do nothing |
| 9 | FLR/USD | 0.00515 | 24.67 | -0.77% | 1.15x | WEAK 17/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD ⭐ | 0.0104783 | 74.69 | +0.62% | 1.18x | 2828 | STRONG 72/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
