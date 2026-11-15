# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T12:19:24.596517+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43713206445
**Source SHA:** 2f30269316c847a4ba711151fcbb5ed3ab468275
**Previous ledger commit:** dd03e720afb8a56be0a48cbfe9e4bdfc2373d2ee (atomic ledger/results publication)
**Ledger generation:** 431 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AAVE/USD | 107.54 | 105.409 | 87.412 | +6.95% | +0.60% | 6.79x | 7.4 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05024 | 104.723 | 91.181 | +5.88% | -0.12% | 2.41x | 10.0 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 68.12 | 104.575 | 95.003 | +5.92% | +0.28% | 1.82x | 2.9 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.7324 | 103.840 | 86.091 | +4.54% | +0.55% | 12.14x | 1.4 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ZEC/USD | 921.78 | 101.320 | 97.446 | +6.70% | +0.15% | 1.31x | 5.1 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 6 | QNT/USD | 153 | 100.758 | 96.406 | +6.76% | +0.64% | 1.11x | 7.2 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ADA/USD | 0.156301 | 94.841 | 93.199 | +5.85% | +0.72% | 0.80x | 5.6 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ETH/USD | 1827.85 | 94.469 | 78.599 | +3.38% | +0.17% | 4.25x | 0.1 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XRP/USD | 0.96659 | 93.786 | 94.110 | +5.78% | +0.32% | 0.81x | 2.7 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 72.56 | 92.712 | 76.536 | +3.27% | +0.24% | 2.56x | 2.8 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | UNI/USD | 5.1775 | 91.910 | 94.655 | +6.05% | +0.87% | 0.29x | 5.4 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TAO/USD | 193.7676 | 90.602 | 89.916 | +5.38% | +0.40% | 0.87x | 5.5 | 2026-11-15T12:19:17.708796+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.446 | 921.78 | +0.15% | 1.31x |
| 2 | QNT/USD | 96.406 | 153 | +0.64% | 1.11x |
| 3 | HYPE/USD | 95.003 | 68.12 | +0.28% | 1.82x |
| 4 | UNI/USD | 94.655 | 5.1775 | +0.87% | 0.29x |
| 5 | XRP/USD | 94.110 | 0.96659 | +0.32% | 0.81x |
| 6 | ADA/USD | 93.199 | 0.156301 | +0.72% | 0.80x |
| 7 | NIGHT/USD | 91.181 | 0.05024 | -0.12% | 2.41x |
| 8 | TAO/USD | 89.916 | 193.7676 | +0.40% | 0.87x |
| 9 | AAVE/USD | 87.412 | 107.54 | +0.60% | 6.79x |
| 10 | SUI/USD | 86.091 | 0.7324 | +0.55% | 12.14x |
| 11 | ETH/USD | 78.599 | 1827.85 | +0.17% | 4.25x |
| 12 | SOL/USD | 76.536 | 72.56 | +0.24% | 2.56x |

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

- Persisted scans: 431; predictions: 3688; observations: 259532.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 10963. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 43713206445 · **Generation:** 431 · **Legacy run:** 43713206445
**Main quote time:** 2026-11-15T12:19:24.596517+00:00 · **Legacy report time:** 2026-11-15T12:19:40.495251+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD | 107.54 | 105.41 | +0.60% | 6.79x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD | 0.05024 | 104.72 | -0.12% | 2.41x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD ⭐ | 68.12 | 104.58 | +0.28% | 1.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.7324 | 103.84 | +0.55% | 12.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 921.78 | 101.32 | +0.15% | 1.31x | STRONG 95/100 | HIGH 55/100 | Watch |
| 6 | QNT/USD ⭐ | 153 | 100.76 | +0.64% | 1.11x | STRONG 95/100 | HIGH 62/100 | Watch |
| 7 | ADA/USD | 0.156301 | 94.84 | +0.72% | 0.80x | STRONG 77/100 | HIGH 62/100 | Watch |
| 8 | ETH/USD ⭐ | 1827.85 | 94.47 | +0.17% | 4.25x | STRONG 100/100 | HIGH 55/100 | Watch |
| 9 | XRP/USD | 0.96659 | 93.79 | +0.32% | 0.81x | STRONG 77/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD ⭐ | 72.56 | 92.71 | +0.24% | 2.56x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | UNI/USD | 5.1775 | 91.91 | +0.87% | 0.29x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 12 | TAO/USD | 193.7676 | 90.60 | +0.40% | 0.87x | STRONG 75/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.29695 | 100.00 | +0.45% | 1.98x | 15645 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.7341 | 100.00 | +0.55% | 12.14x | 24443 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1831.29 | 97.24 | +0.17% | 4.25x | 99893 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | SOL/USD ⭐ | 72.66 | 97.17 | +0.24% | 2.56x | 68783 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | HYPE/USD ⭐ | 68.21 | 95.31 | +0.28% | 1.82x | 33699 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | PEPE/USD | 4.042e-06 | 95.02 | +0.67% | 6.60x | 9153 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | DOT/USD | 0.7411 | 92.43 | +0.89% | 1.66x | 13933 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 8 | QNT/USD ⭐ | 153.4 | 87.38 | +0.64% | 1.11x | 12077 | STRONG 84/100 | HIGH 68/100 | Watch |
| 9 | ZEC/USD ⭐ | 921.78 | 86.70 | +0.15% | 1.31x | 41641 | STRONG 83/100 | HIGH 61/100 | Watch |

**Same-run overlap:** HYPE/USD, SUI/USD, ZEC/USD, QNT/USD, ETH/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
