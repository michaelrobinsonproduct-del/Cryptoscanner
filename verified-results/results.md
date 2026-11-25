# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T18:08:32.810632+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45671370414
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7372c2a465faa9aeba5da5817e794032457fdfdb (atomic ledger/results publication)
**Ledger generation:** 1748 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.397 | 86.187 | 83.498 | +7.58% | +0.53% | 1.00x | 33.0 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | DRV/USD | 0.34382 | 73.988 | 76.423 | +9.40% | -0.44% | 0.98x | 14.8 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | XPL/USD | 0.0476 | 67.964 | 70.964 | +8.18% | +0.42% | 0.49x | 21.1 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | HYPE/USD | 60.4 | 66.933 | 59.541 | +0.89% | +1.22% | 1.13x | 3.3 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LTC/USD | 41.74 | 64.220 | 67.854 | +2.18% | -0.17% | 0.72x | 4.8 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | INJ/USD | 5.955 | 54.864 | 46.538 | +1.83% | +0.70% | 1.48x | 10.1 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XMR/USD | 516.19 | 54.179 | 57.849 | +1.29% | -0.12% | 0.69x | 12.4 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | XLM/USD | 0.125763 | 52.062 | 50.450 | +1.38% | +0.38% | 0.97x | 5.2 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 8.89232 | 47.440 | 47.026 | +0.58% | +0.37% | 0.86x | 4.5 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 10 | BCH/USD | 200.58 | 47.273 | 42.644 | +1.73% | -0.17% | 1.55x | 6.0 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | WEAK 44/100 | HIGH 66/100 | Watch | WATCH |
| 11 | STBL/USD | 0.018767 | 45.353 | 52.966 | +5.20% | -1.00% | 0.74x | 28.3 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | WEAK 18/100 | EXTREME 100/100 | Do nothing | WATCH |
| 12 | HBAR/USD | 0.0508 | 43.684 | 42.266 | +1.07% | +0.12% | 1.08x | 2.0 | 2026-11-25T18:08:24.952536+00:00 | Not calibrated | MODERATE 47/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 83.498 | 26.397 | +0.53% | 1.00x |
| 2 | DRV/USD | 76.423 | 0.34382 | -0.44% | 0.98x |
| 3 | XPL/USD | 70.964 | 0.0476 | +0.42% | 0.49x |
| 4 | LTC/USD | 67.854 | 41.74 | -0.17% | 0.72x |
| 5 | HYPE/USD | 59.541 | 60.4 | +1.22% | 1.13x |
| 6 | XMR/USD | 57.849 | 516.19 | -0.12% | 0.69x |
| 7 | STBL/USD | 52.966 | 0.018767 | -1.00% | 0.74x |
| 8 | XLM/USD | 50.450 | 0.125763 | +0.38% | 0.97x |
| 9 | LINK/USD | 47.026 | 8.89232 | +0.37% | 0.86x |
| 10 | INJ/USD | 46.538 | 5.955 | +0.70% | 1.48x |
| 11 | BCH/USD | 42.644 | 200.58 | -0.17% | 1.55x |
| 12 | HBAR/USD | 42.266 | 0.0508 | +0.12% | 1.08x |

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

- Persisted scans: 1748; predictions: 14720; observations: 1059576.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22637. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45671370414 · **Generation:** 1748 · **Legacy run:** 45671370414
**Main quote time:** 2026-11-25T18:08:32.810632+00:00 · **Legacy report time:** 2026-11-25T18:09:49.019885+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.397 | 86.19 | +0.53% | 1.00x | STRONG 78/100 | VERY_HIGH 74/100 | Watch |
| 2 | DRV/USD | 0.34382 | 73.99 | -0.44% | 0.98x | WEAK 37/100 | VERY_HIGH 74/100 | Watch |
| 3 | XPL/USD | 0.0476 | 67.96 | +0.42% | 0.49x | MODERATE 54/100 | EXTREME 87/100 | Do nothing |
| 4 | HYPE/USD ⭐ | 60.4 | 66.93 | +1.22% | 1.13x | STRONG 78/100 | HIGH 62/100 | Watch |
| 5 | LTC/USD | 41.74 | 64.22 | -0.17% | 0.72x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 6 | INJ/USD | 5.955 | 54.86 | +0.70% | 1.48x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 7 | XMR/USD | 516.19 | 54.18 | -0.12% | 0.69x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | XLM/USD | 0.125763 | 52.06 | +0.38% | 0.97x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD | 8.89232 | 47.44 | +0.37% | 0.86x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 10 | BCH/USD | 200.58 | 47.27 | -0.17% | 1.55x | WEAK 44/100 | HIGH 66/100 | Watch |
| 11 | STBL/USD | 0.018767 | 45.35 | -1.00% | 0.74x | WEAK 18/100 | EXTREME 100/100 | Do nothing |
| 12 | HBAR/USD | 0.0508 | 43.68 | +0.12% | 1.08x | MODERATE 47/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.49 | 86.60 | +0.53% | 1.00x | 10034 | STRONG 83/100 | HIGH 68/100 | Watch |
| 2 | HYPE/USD ⭐ | 60.42 | 60.59 | +1.22% | 1.13x | 21556 | STRONG 75/100 | HIGH 62/100 | Watch |
| 3 | XRP/USD | 0.92483 | 56.06 | +0.21% | 1.51x | 34338 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
