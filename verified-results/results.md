# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T03:30:10.856993+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44010601165
**Source SHA:** d368ec72564813f9b0a53eca24a9b768cfd51747
**Previous ledger commit:** dd6d42ab126288babd44d5689a28de458126f0cb (atomic ledger/results publication)
**Ledger generation:** 452 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AAVE/USD | 112.58 | 88.852 | 67.100 | +3.78% | +1.35% | 5.67x | 5.3 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 7.217 | 86.412 | 74.784 | +4.61% | +1.26% | 1.53x | 5.5 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.2254 | 86.299 | 67.504 | +2.14% | +0.76% | 3.18x | 5.0 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ZEC/USD | 918.76 | 82.500 | 63.257 | +1.65% | +0.85% | 4.54x | 6.6 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 20.915 | 81.612 | 61.663 | +3.81% | +0.99% | 4.85x | 12.0 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 91/100 | HIGH 61/100 | Consider small entry | WATCH |
| 6 | NIGHT/USD | 0.04958 | 78.410 | 76.723 | +4.40% | +0.96% | 0.69x | 18.2 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SUI/USD | 0.727 | 76.904 | 57.813 | +1.06% | +0.82% | 2.91x | 1.4 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XDG/USD | 0.059277 | 74.346 | 59.654 | +0.67% | +0.61% | 2.17x | 0.0 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XRP/USD | 0.96339 | 71.920 | 60.704 | +0.90% | +0.51% | 1.87x | 1.2 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | ETH/USD | 1827.62 | 71.844 | 58.386 | +0.49% | +0.61% | 2.04x | 0.1 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | SOL/USD | 72.46 | 67.992 | 63.510 | +1.31% | +0.57% | 1.16x | 1.4 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 12 | ZRO/USD | 1.527 | 65.490 | 63.459 | +4.52% | -0.46% | 1.43x | 13.1 | 2026-11-17T03:30:04.945728+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 76.723 | 0.04958 | +0.96% | 0.69x |
| 2 | INJ/USD | 74.784 | 7.217 | +1.26% | 1.53x |
| 3 | NEAR/USD | 67.504 | 3.2254 | +0.76% | 3.18x |
| 4 | AAVE/USD | 67.100 | 112.58 | +1.35% | 5.67x |
| 5 | SOL/USD | 63.510 | 72.46 | +0.57% | 1.16x |
| 6 | ZRO/USD | 63.459 | 1.527 | -0.46% | 1.43x |
| 7 | ZEC/USD | 63.257 | 918.76 | +0.85% | 4.54x |
| 8 | VVV/USD | 61.663 | 20.915 | +0.99% | 4.85x |
| 9 | XRP/USD | 60.704 | 0.96339 | +0.51% | 1.87x |
| 10 | XDG/USD | 59.654 | 0.059277 | +0.61% | 2.17x |
| 11 | ETH/USD | 58.386 | 1827.62 | +0.61% | 2.04x |
| 12 | SUI/USD | 57.813 | 0.727 | +0.82% | 2.91x |

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

- Persisted scans: 452; predictions: 3905; observations: 272279.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12037. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44010601165 · **Generation:** 452 · **Legacy run:** 44010601165
**Main quote time:** 2026-11-17T03:30:10.856993+00:00 · **Legacy report time:** 2026-11-17T03:30:22.001795+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD ⭐ | 112.58 | 88.85 | +1.35% | 5.67x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.217 | 86.41 | +1.26% | 1.53x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.2254 | 86.30 | +0.76% | 3.18x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 918.76 | 82.50 | +0.85% | 4.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD ⭐ | 20.915 | 81.61 | +0.99% | 4.85x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 6 | NIGHT/USD | 0.04958 | 78.41 | +0.96% | 0.69x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 7 | SUI/USD ⭐ | 0.727 | 76.90 | +0.82% | 2.91x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XDG/USD ⭐ | 0.059277 | 74.35 | +0.61% | 2.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.96339 | 71.92 | +0.51% | 1.87x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 10 | ETH/USD ⭐ | 1827.62 | 71.84 | +0.61% | 2.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | SOL/USD ⭐ | 72.46 | 67.99 | +0.57% | 1.16x | STRONG 79/100 | HIGH 62/100 | Watch |
| 12 | ZRO/USD | 1.527 | 65.49 | -0.46% | 1.43x | MODERATE 48/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD ⭐ | 112.58 | 93.50 | +1.35% | 5.67x | 4098 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.237 | 85.09 | +1.26% | 1.53x | 7865 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 20.906 | 84.71 | +0.99% | 4.85x | 6429 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 3.2243 | 80.72 | +0.76% | 3.18x | 10777 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 918.76 | 70.86 | +0.85% | 4.54x | 27423 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.7266 | 69.00 | +0.82% | 2.91x | 6609 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD ⭐ | 0.96367 | 67.99 | +0.51% | 1.87x | 32783 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 72.46 | 67.37 | +0.57% | 1.16x | 35249 | STRONG 79/100 | HIGH 62/100 | Watch |
| 9 | XDG/USD ⭐ | 0.059277 | 66.44 | +0.61% | 2.17x | 9722 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 10 | ETH/USD ⭐ | 1828.52 | 64.33 | +0.61% | 2.04x | 48843 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 11 | XBT/USD | 64964.4 | 62.26 | +0.54% | 2.47x | 193557 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** AAVE/USD, INJ/USD, NEAR/USD, ZEC/USD, VVV/USD, SUI/USD, XDG/USD, XRP/USD, ETH/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
