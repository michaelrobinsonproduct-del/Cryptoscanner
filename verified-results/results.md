# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T06:19:11.033213+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43684845364
**Source SHA:** 5f8133b47b24d2e1afbf7bbca0cef03585730969
**Previous ledger commit:** 858b08376003eb0473c41157e6438afb3f4191a0 (atomic ledger/results publication)
**Ledger generation:** 430 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05018 | 98.659 | 87.301 | +5.75% | +0.63% | 1.82x | 15.9 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | STRONG 89/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.95648 | 96.233 | 86.822 | +4.67% | -0.65% | 2.26x | 1.8 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 490.91 | 93.320 | 80.884 | +4.41% | +0.25% | 2.12x | 10.0 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ZEC/USD | 893.43 | 88.724 | 78.897 | +3.42% | -1.03% | 3.35x | 0.1 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | STRONG 74/100 | HIGH 65/100 | Watch | WATCH |
| 5 | SUI/USD | 0.716 | 81.424 | 69.689 | +2.20% | -0.65% | 8.36x | 1.4 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AAVE/USD | 105.79 | 80.692 | 77.386 | +5.21% | -0.41% | 1.53x | 7.6 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XLM/USD | 0.13745 | 76.895 | 64.648 | +1.45% | -0.55% | 2.52x | 1.0 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.1109 | 72.284 | 71.222 | +2.71% | -0.80% | 1.50x | 5.5 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 9 | INJ/USD | 6.986 | 67.953 | 71.659 | +2.58% | -1.14% | 1.20x | 2.9 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | LINK/USD | 9.1 | 66.637 | 69.290 | +2.38% | -0.50% | 0.99x | 4.8 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ETH/USD | 1794.94 | 66.001 | 65.570 | +1.51% | -0.64% | 1.36x | 0.1 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0579637 | 64.573 | 62.610 | +1.13% | -0.63% | 1.51x | 0.6 | 2026-11-15T06:19:02.491765+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 87.301 | 0.05018 | +0.63% | 1.82x |
| 2 | XRP/USD | 86.822 | 0.95648 | -0.65% | 2.26x |
| 3 | XMR/USD | 80.884 | 490.91 | +0.25% | 2.12x |
| 4 | ZEC/USD | 78.897 | 893.43 | -1.03% | 3.35x |
| 5 | AAVE/USD | 77.386 | 105.79 | -0.41% | 1.53x |
| 6 | INJ/USD | 71.659 | 6.986 | -1.14% | 1.20x |
| 7 | NEAR/USD | 71.222 | 3.1109 | -0.80% | 1.50x |
| 8 | SUI/USD | 69.689 | 0.716 | -0.65% | 8.36x |
| 9 | LINK/USD | 69.290 | 9.1 | -0.50% | 0.99x |
| 10 | ETH/USD | 65.570 | 1794.94 | -0.64% | 1.36x |
| 11 | XLM/USD | 64.648 | 0.13745 | -0.55% | 2.52x |
| 12 | XDG/USD | 62.610 | 0.0579637 | -0.63% | 1.51x |

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

- Persisted scans: 430; predictions: 3676; observations: 258925.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 10786. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 43684845364 · **Generation:** 430 · **Legacy run:** 43684845364
**Main quote time:** 2026-11-15T06:19:11.033213+00:00 · **Legacy report time:** 2026-11-15T06:19:28.272570+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05018 | 98.66 | +0.63% | 1.82x | STRONG 99/100 | HIGH 61/100 | Consider small entry |
| 2 | XRP/USD | 0.95648 | 96.23 | -0.65% | 2.26x | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD ⭐ | 490.91 | 93.32 | +0.25% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZEC/USD | 893.43 | 88.72 | -1.03% | 3.35x | STRONG 74/100 | HIGH 65/100 | Watch |
| 5 | SUI/USD | 0.716 | 81.42 | -0.65% | 8.36x | STRONG 71/100 | HIGH 61/100 | Watch |
| 6 | AAVE/USD | 105.79 | 80.69 | -0.41% | 1.53x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | XLM/USD | 0.13745 | 76.89 | -0.55% | 2.52x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | NEAR/USD | 3.1109 | 72.28 | -0.80% | 1.50x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 9 | INJ/USD | 6.986 | 67.95 | -1.14% | 1.20x | WEAK 44/100 | VERY_HIGH 72/100 | Watch |
| 10 | LINK/USD | 9.1 | 66.64 | -0.50% | 0.99x | WEAK 38/100 | HIGH 68/100 | Watch |
| 11 | ETH/USD | 1794.94 | 66.00 | -0.64% | 1.36x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 12 | XDG/USD | 0.0579637 | 64.57 | -0.63% | 1.51x | MODERATE 52/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 490.91 | 90.23 | +0.25% | 2.12x | 14545 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.05018 | 90.17 | +0.63% | 1.82x | 26183 | STRONG 95/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
