# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:40:16.219322+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44338187462
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 96dbd3c870ef304fca669cbf55e6f312dfb953e1 (atomic ledger/results publication)
**Ledger generation:** 603 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.9592 | 78.129 | 80.515 | +8.21% | +0.89% | 0.32x | 8.7 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | STABLE/USD | 0.02294 | 77.734 | 65.120 | +8.98% | -0.48% | 3.11x | 21.8 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | MODERATE 59/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | SENT/USD | 0.01971 | 72.205 | 66.284 | +5.58% | +0.08% | 1.55x | 7.6 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 4 | CT/USD | 0.1204 | 69.488 | 67.827 | +6.55% | -2.67% | 4.69x | 16.7 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3853 | 55.788 | 51.623 | +3.21% | -0.08% | 1.46x | 7.8 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | MODERATE 48/100 | HIGH 66/100 | Watch | WATCH |
| 6 | TRX/USD | 0.3097 | 48.530 | 44.781 | +0.58% | -0.13% | 1.44x | 0.5 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04523 | 40.539 | 49.924 | +0.76% | -0.13% | 0.13x | 6.6 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKE/USD | 0.010336 | 39.475 | 42.599 | +3.52% | -0.92% | 1.15x | 31.2 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 20/100 | EXTREME 85/100 | Do nothing | WATCH |
| 9 | RE/USD | 0.23972 | 37.153 | 41.394 | +3.18% | +0.38% | 0.39x | 23.0 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 39/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | FLR/USD | 0.00518 | 28.351 | 31.169 | +1.37% | -0.38% | 0.91x | 19.3 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 14/100 | EXTREME 86/100 | Do nothing | WATCH |
| 11 | ZAMA/USD | 0.06021 | 20.819 | 30.726 | +0.47% | -0.35% | 0.18x | 8.3 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 15/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | XPL/USD | 0.0466 | 19.907 | 25.286 | +0.43% | -0.43% | 0.68x | 21.5 | 2026-11-18T15:40:07.264296+00:00 | Not calibrated | WEAK 5/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 80.515 | 1.9592 | +0.89% | 0.32x |
| 2 | CT/USD | 67.827 | 0.1204 | -2.67% | 4.69x |
| 3 | SENT/USD | 66.284 | 0.01971 | +0.08% | 1.55x |
| 4 | STABLE/USD | 65.120 | 0.02294 | -0.48% | 3.11x |
| 5 | MNT/USD | 51.623 | 0.3853 | -0.08% | 1.46x |
| 6 | NIGHT/USD | 49.924 | 0.04523 | -0.13% | 0.13x |
| 7 | TRX/USD | 44.781 | 0.3097 | -0.13% | 1.44x |
| 8 | AKE/USD | 42.599 | 0.010336 | -0.92% | 1.15x |
| 9 | RE/USD | 41.394 | 0.23972 | +0.38% | 0.39x |
| 10 | FLR/USD | 31.169 | 0.00518 | -0.38% | 0.91x |
| 11 | ZAMA/USD | 30.726 | 0.06021 | -0.35% | 0.18x |
| 12 | XPL/USD | 25.286 | 0.0466 | -0.43% | 0.68x |

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

- Persisted scans: 603; predictions: 5172; observations: 364234.
- Matured sampled outcomes across 1/6/24/48h: 4383; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44338187462 · **Generation:** 603 · **Legacy run:** 44338187462
**Main quote time:** 2026-11-18T15:40:16.219322+00:00 · **Legacy report time:** 2026-11-18T15:40:38.922418+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.9592 | 78.13 | +0.89% | 0.32x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 2 | STABLE/USD | 0.02294 | 77.73 | -0.48% | 3.11x | MODERATE 59/100 | EXTREME 85/100 | Do nothing |
| 3 | SENT/USD ⭐ | 0.01971 | 72.21 | +0.08% | 1.55x | STRONG 81/100 | HIGH 67/100 | Watch |
| 4 | CT/USD | 0.1204 | 69.49 | -2.67% | 4.69x | MODERATE 60/100 | VERY_HIGH 83/100 | Do nothing |
| 5 | MNT/USD | 0.3853 | 55.79 | -0.08% | 1.46x | MODERATE 48/100 | HIGH 66/100 | Watch |
| 6 | TRX/USD | 0.3097 | 48.53 | -0.13% | 1.44x | WEAK 44/100 | HIGH 61/100 | Watch |
| 7 | NIGHT/USD | 0.04523 | 40.54 | -0.13% | 0.13x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKE/USD | 0.010336 | 39.48 | -0.92% | 1.15x | WEAK 20/100 | EXTREME 85/100 | Do nothing |
| 9 | RE/USD | 0.23972 | 37.15 | +0.38% | 0.39x | WEAK 39/100 | EXTREME 94/100 | Do nothing |
| 10 | FLR/USD | 0.00518 | 28.35 | -0.38% | 0.91x | WEAK 14/100 | EXTREME 86/100 | Do nothing |
| 11 | ZAMA/USD | 0.06021 | 20.82 | -0.35% | 0.18x | WEAK 15/100 | EXTREME 88/100 | Do nothing |
| 12 | XPL/USD | 0.0466 | 19.91 | -0.43% | 0.68x | WEAK 5/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019672 | 73.09 | +0.08% | 1.55x | 5879 | STRONG 82/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
