# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:30:16.144325+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44359265762
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 2be6ee6993cc19ee7b5db8210c7498d953b10c55 (atomic ledger/results publication)
**Ledger generation:** 624 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019932 | 92.980 | 72.044 | +6.77% | +1.56% | 2.31x | 8.0 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | PEARL/USD | 2.024 | 65.428 | 80.940 | +11.79% | -1.67% | 0.28x | 12.3 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | WEAK 33/100 | EXTREME 86/100 | Do nothing | WATCH |
| 3 | TRUST/USD | 0.04979 | 64.457 | 65.454 | +5.60% | +1.30% | 0.25x | 12.1 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05373 | 60.198 | 49.231 | +4.05% | +0.92% | 1.64x | 20.5 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | CC/USD | 0.08355 | 56.235 | 44.642 | +1.73% | +1.26% | 1.53x | 6.0 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04521 | 54.788 | 40.369 | +0.71% | +2.01% | 1.44x | 26.6 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 7 | MNT/USD | 0.3855 | 48.279 | 49.506 | +3.27% | +0.03% | 0.86x | 10.4 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | XPL/USD | 0.0469 | 45.340 | 30.244 | +1.08% | +1.30% | 1.86x | 21.4 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | W/USD | 0.00898 | 40.594 | 29.665 | +0.56% | +1.70% | 1.24x | 11.1 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 10 | ZAMA/USD | 0.06081 | 39.408 | 36.049 | +1.47% | +1.18% | 0.75x | 11.5 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | AKE/USD | 0.01012428 | 35.980 | 34.676 | +1.40% | +1.26% | 0.50x | 17.3 | 2026-11-18T17:30:10.150661+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 80.940 | 2.024 | -1.67% | 0.28x |
| 2 | SENT/USD | 72.044 | 0.019932 | +1.56% | 2.31x |
| 3 | TRUST/USD | 65.454 | 0.04979 | +1.30% | 0.25x |
| 4 | MNT/USD | 49.506 | 0.3855 | +0.03% | 0.86x |
| 5 | MEGA/USD | 49.231 | 0.05373 | +0.92% | 1.64x |
| 6 | CC/USD | 44.642 | 0.08355 | +1.26% | 1.53x |
| 7 | NIGHT/USD | 40.369 | 0.04521 | +2.01% | 1.44x |
| 8 | ZAMA/USD | 36.049 | 0.06081 | +1.18% | 0.75x |
| 9 | AKE/USD | 34.676 | 0.01012428 | +1.26% | 0.50x |
| 10 | XPL/USD | 30.244 | 0.0469 | +1.30% | 1.86x |
| 11 | W/USD | 29.665 | 0.00898 | +1.70% | 1.24x |

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

- Persisted scans: 624; predictions: 5324; observations: 377023.
- Matured sampled outcomes across 1/6/24/48h: 4625; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44359265762 · **Generation:** 624 · **Legacy run:** 44359265762
**Main quote time:** 2026-11-18T17:30:16.144325+00:00 · **Legacy report time:** 2026-11-18T17:30:42.500369+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019932 | 92.98 | +1.56% | 2.31x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | PEARL/USD | 2.024 | 65.43 | -1.67% | 0.28x | WEAK 33/100 | EXTREME 86/100 | Do nothing |
| 3 | TRUST/USD | 0.04979 | 64.46 | +1.30% | 0.25x | MODERATE 57/100 | VERY_HIGH 81/100 | Watch |
| 4 | MEGA/USD ⭐ | 0.05373 | 60.20 | +0.92% | 1.64x | STRONG 75/100 | VERY_HIGH 79/100 | Watch |
| 5 | CC/USD ⭐ | 0.08355 | 56.23 | +1.26% | 1.53x | STRONG 83/100 | HIGH 60/100 | Consider small entry |
| 6 | NIGHT/USD ⭐ | 0.04521 | 54.79 | +2.01% | 1.44x | STRONG 72/100 | HIGH 67/100 | Watch |
| 7 | MNT/USD | 0.3855 | 48.28 | +0.03% | 0.86x | WEAK 39/100 | VERY_HIGH 73/100 | Watch |
| 8 | XPL/USD ⭐ | 0.0469 | 45.34 | +1.30% | 1.86x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 9 | W/USD | 0.00898 | 40.59 | +1.70% | 1.24x | MODERATE 50/100 | VERY_HIGH 80/100 | Watch |
| 10 | ZAMA/USD | 0.06081 | 39.41 | +1.18% | 0.75x | MODERATE 45/100 | EXTREME 88/100 | Do nothing |
| 11 | AKE/USD | 0.01012428 | 35.98 | +1.26% | 0.50x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019925 | 80.57 | +1.56% | 2.31x | 5957 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05368 | 63.40 | +0.92% | 1.64x | 1200 | STRONG 77/100 | VERY_HIGH 79/100 | Watch |
| 3 | CC/USD ⭐ | 0.08363 | 53.15 | +1.26% | 1.53x | 4982 | STRONG 82/100 | HIGH 60/100 | Consider small entry |
| 4 | NIGHT/USD ⭐ | 0.0452 | 49.26 | +2.01% | 1.44x | 16028 | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | XPL/USD ⭐ | 0.0468 | 30.96 | +1.30% | 1.86x | 1350 | MODERATE 60/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** SENT/USD, MEGA/USD, CC/USD, NIGHT/USD, XPL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
