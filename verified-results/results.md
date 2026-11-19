# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:32:58.566111+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44638092818
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** c6cf7eea39ba322d96b71f67260f7de204d7167c (atomic ledger/results publication)
**Ledger generation:** 880 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5296 | 61.714 | 44.352 | +2.24% | +0.47% | 33.58x | 7.6 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05921 | 60.417 | 65.447 | +5.73% | -0.47% | 0.73x | 13.5 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | USELESS/USD | 0.09823 | 52.694 | 52.233 | +2.79% | +0.06% | 1.02x | 15.3 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 4 | VVV/USD | 21.777 | 49.051 | 54.749 | +0.49% | +0.53% | 0.17x | 7.3 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | INJ/USD | 7.033 | 48.461 | 47.179 | +0.74% | +0.44% | 0.91x | 7.1 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.05295 | 36.901 | 31.018 | +0.36% | +0.66% | 1.26x | 9.5 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | MODERATE 53/100 | HIGH 60/100 | Watch | WATCH |
| 7 | AKE/USD | 0.01050577 | 32.451 | 36.329 | +1.11% | +0.29% | 0.47x | 12.0 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | BABY/USD | 0.00841 | 32.240 | 30.726 | +0.84% | +1.08% | 0.61x | 11.9 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | WEAK 41/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | LIGHTER/USD | 2.745 | 31.424 | 37.365 | +1.14% | -0.72% | 0.77x | 10.9 | 2026-11-19T23:32:51.550819+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 65.447 | 0.05921 | -0.47% | 0.73x |
| 2 | VVV/USD | 54.749 | 21.777 | +0.53% | 0.17x |
| 3 | USELESS/USD | 52.233 | 0.09823 | +0.06% | 1.02x |
| 4 | INJ/USD | 47.179 | 7.033 | +0.44% | 0.91x |
| 5 | AKT/USD | 44.352 | 0.5296 | +0.47% | 33.58x |
| 6 | LIGHTER/USD | 37.365 | 2.745 | -0.72% | 0.77x |
| 7 | AKE/USD | 36.329 | 0.01050577 | +0.29% | 0.47x |
| 8 | PYTH/USD | 31.018 | 0.05295 | +0.66% | 1.26x |
| 9 | BABY/USD | 30.726 | 0.00841 | +1.08% | 0.61x |

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

- Persisted scans: 880; predictions: 7667; observations: 531765.
- Matured sampled outcomes across 1/6/24/48h: 8186; gap abstentions: 15862. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44638092818 · **Generation:** 880 · **Legacy run:** 44638092818
**Main quote time:** 2026-11-19T23:32:58.566111+00:00 · **Legacy report time:** 2026-11-19T23:33:51.262216+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5296 | 61.71 | +0.47% | 33.58x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 2 | MEGA/USD | 0.05921 | 60.42 | -0.47% | 0.73x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 3 | USELESS/USD ⭐ | 0.09823 | 52.69 | +0.06% | 1.02x | MODERATE 56/100 | HIGH 68/100 | Watch |
| 4 | VVV/USD | 21.777 | 49.05 | +0.53% | 0.17x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 5 | INJ/USD | 7.033 | 48.46 | +0.44% | 0.91x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 6 | PYTH/USD | 0.05295 | 36.90 | +0.66% | 1.26x | MODERATE 53/100 | HIGH 60/100 | Watch |
| 7 | AKE/USD | 0.01050577 | 32.45 | +0.29% | 0.47x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 8 | BABY/USD | 0.00841 | 32.24 | +1.08% | 0.61x | WEAK 41/100 | EXTREME 88/100 | Do nothing |
| 9 | LIGHTER/USD | 2.745 | 31.42 | -0.72% | 0.77x | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5305 | 69.30 | +0.47% | 33.58x | 3571 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | USELESS/USD ⭐ | 0.09843 | 64.49 | +0.06% | 1.02x | 6088 | MODERATE 62/100 | HIGH 68/100 | Watch |
| 3 | SENT/USD | 0.021142 | 64.28 | +0.14% | 8.87x | 14711 | STRONG 72/100 | HIGH 66/100 | Watch |
| 4 | TRX/USD | 0.309799 | 46.70 | +0.12% | 1.01x | 5170 | MODERATE 48/100 | HIGH 62/100 | Watch |

**Same-run overlap:** AKT/USD, USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
