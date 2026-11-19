# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:55:24.166208+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44454663390
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 34e9573cfc9215baa39071ca0ee9ef05b52ded44 (atomic ledger/results publication)
**Ledger generation:** 748 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022507 | 88.388 | 73.638 | +9.23% | +1.19% | 1.88x | 6.2 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 89/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.29 | 86.305 | 67.120 | +2.86% | +0.84% | 6.23x | 7.6 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1787.3 | 77.435 | 59.918 | +0.71% | +0.50% | 3.05x | 0.1 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.7247 | 76.975 | 59.267 | +0.81% | +0.54% | 6.32x | 2.8 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NEAR/USD | 3.3847 | 76.745 | 71.467 | +2.65% | +0.90% | 1.08x | 4.1 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ZEC/USD | 918.81 | 73.988 | 58.742 | +0.75% | +1.02% | 2.01x | 3.0 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | TAO/USD | 193.7467 | 66.953 | 58.328 | +0.93% | +0.53% | 1.60x | 6.4 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LUNA/USD | 4.703e-05 | 65.983 | 57.549 | +8.02% | -0.57% | 2.13x | 40.5 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | SOL/USD | 74.06 | 63.437 | 59.275 | +0.71% | +0.53% | 1.15x | 1.4 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 10 | HYPE/USD | 67.26 | 62.618 | 58.234 | +0.57% | +0.46% | 1.21x | 1.5 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 11 | LTC/USD | 44.41 | 55.746 | 51.676 | +0.91% | +0.38% | 1.21x | 2.3 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0588958 | 54.879 | 51.391 | +0.33% | +0.46% | 1.12x | 0.0 | 2026-11-19T03:55:18.198786+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.638 | 0.022507 | +1.19% | 1.88x |
| 2 | NEAR/USD | 71.467 | 3.3847 | +0.90% | 1.08x |
| 3 | VVV/USD | 67.120 | 22.29 | +0.84% | 6.23x |
| 4 | ETH/USD | 59.918 | 1787.3 | +0.50% | 3.05x |
| 5 | SOL/USD | 59.275 | 74.06 | +0.53% | 1.15x |
| 6 | SUI/USD | 59.267 | 0.7247 | +0.54% | 6.32x |
| 7 | ZEC/USD | 58.742 | 918.81 | +1.02% | 2.01x |
| 8 | TAO/USD | 58.328 | 193.7467 | +0.53% | 1.60x |
| 9 | HYPE/USD | 58.234 | 67.26 | +0.46% | 1.21x |
| 10 | LUNA/USD | 57.549 | 4.703e-05 | -0.57% | 2.13x |
| 11 | LTC/USD | 51.676 | 44.41 | +0.38% | 1.21x |
| 12 | XDG/USD | 51.391 | 0.0588958 | +0.46% | 1.12x |

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

- Persisted scans: 748; predictions: 6120; observations: 452539.
- Matured sampled outcomes across 1/6/24/48h: 6080; gap abstentions: 13589. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44454663390 · **Generation:** 748 · **Legacy run:** 44454663390
**Main quote time:** 2026-11-19T03:55:24.166208+00:00 · **Legacy report time:** 2026-11-19T03:55:58.335609+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022507 | 88.39 | +1.19% | 1.88x | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.29 | 86.31 | +0.84% | 6.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1787.3 | 77.44 | +0.50% | 3.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.7247 | 76.98 | +0.54% | 6.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.3847 | 76.75 | +0.90% | 1.08x | STRONG 83/100 | HIGH 62/100 | Watch |
| 6 | ZEC/USD ⭐ | 918.81 | 73.99 | +1.02% | 2.01x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | TAO/USD | 193.7467 | 66.95 | +0.53% | 1.60x | STRONG 78/100 | HIGH 55/100 | Watch |
| 8 | LUNA/USD | 4.703e-05 | 65.98 | -0.57% | 2.13x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 9 | SOL/USD ⭐ | 74.06 | 63.44 | +0.53% | 1.15x | STRONG 77/100 | HIGH 62/100 | Watch |
| 10 | HYPE/USD ⭐ | 67.26 | 62.62 | +0.46% | 1.21x | STRONG 76/100 | HIGH 62/100 | Watch |
| 11 | LTC/USD | 44.41 | 55.75 | +0.38% | 1.21x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 12 | XDG/USD | 0.0588958 | 54.88 | +0.46% | 1.12x | MODERATE 62/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.02245 | 85.10 | +1.19% | 1.88x | 8435 | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3878 | 80.82 | +0.90% | 1.08x | 13776 | STRONG 85/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD ⭐ | 22.29 | 79.35 | +0.84% | 6.23x | 8695 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1786.58 | 69.39 | +0.50% | 3.05x | 58181 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SUI/USD ⭐ | 0.7246 | 68.38 | +0.54% | 6.32x | 6711 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 6 | ZEC/USD ⭐ | 918.48 | 61.84 | +1.02% | 2.01x | 21723 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 7 | HYPE/USD ⭐ | 67.26 | 58.06 | +0.46% | 1.21x | 14464 | STRONG 74/100 | HIGH 62/100 | Watch |
| 8 | SOL/USD ⭐ | 74.04 | 56.95 | +0.53% | 1.15x | 35151 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SENT/USD, VVV/USD, ETH/USD, SUI/USD, NEAR/USD, ZEC/USD, SOL/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
