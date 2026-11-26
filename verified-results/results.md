# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T10:36:36.041728+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45802606122
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a448b138cb875833b19701c055477b8c8a9502fd (atomic ledger/results publication)
**Ledger generation:** 1849 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 585; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07078 | 82.018 | 69.619 | +6.81% | -0.52% | 4.26x | 15.6 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | INJ/USD | 6.188 | 80.976 | 67.185 | +3.93% | -0.24% | 2.64x | 8.1 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SEI/USD | 0.03586 | 78.187 | 71.735 | +7.66% | +0.56% | 1.37x | 11.1 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | STRONG 79/100 | HIGH 66/100 | Watch | WATCH |
| 4 | XRP/USD | 0.95072 | 76.760 | 65.320 | +1.51% | -0.21% | 2.25x | 0.5 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.147948 | 75.918 | 64.040 | +1.49% | -0.48% | 2.43x | 2.8 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 9.22266 | 60.517 | 67.355 | +1.97% | -0.07% | 0.35x | 2.9 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | LTC/USD | 43.44 | 60.460 | 65.813 | +1.71% | -0.30% | 0.61x | 2.3 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0566286 | 56.614 | 58.680 | +1.20% | -0.04% | 0.81x | 0.0 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | SOL/USD | 70.8 | 56.188 | 58.371 | +0.58% | -0.17% | 0.87x | 1.4 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | ETH/USD | 1698.56 | 55.818 | 58.346 | +0.48% | -0.08% | 0.79x | 0.1 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | XBT/USD | 60685.8 | 53.035 | 58.670 | +0.53% | -0.16% | 0.51x | 0.0 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | DCR/USD | 10.547 | 50.121 | 34.409 | +0.54% | +0.14% | 3.59x | 0.9 | 2026-11-26T10:36:29.694371+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 71.735 | 0.03586 | +0.56% | 1.37x |
| 2 | SYRUP/USD | 69.619 | 0.07078 | -0.52% | 4.26x |
| 3 | LINK/USD | 67.355 | 9.22266 | -0.07% | 0.35x |
| 4 | INJ/USD | 67.185 | 6.188 | -0.24% | 2.64x |
| 5 | LTC/USD | 65.813 | 43.44 | -0.30% | 0.61x |
| 6 | XRP/USD | 65.320 | 0.95072 | -0.21% | 2.25x |
| 7 | ADA/USD | 64.040 | 0.147948 | -0.48% | 2.43x |
| 8 | XDG/USD | 58.680 | 0.0566286 | -0.04% | 0.81x |
| 9 | XBT/USD | 58.670 | 60685.8 | -0.16% | 0.51x |
| 10 | SOL/USD | 58.371 | 70.8 | -0.17% | 0.87x |
| 11 | ETH/USD | 58.346 | 1698.56 | -0.08% | 0.79x |
| 12 | DCR/USD | 34.409 | 10.547 | +0.14% | 3.59x |

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

- Persisted scans: 1849; predictions: 15923; observations: 1120910.
- Matured sampled outcomes across 1/6/24/48h: 34490; gap abstentions: 24571. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45802606122 · **Generation:** 1849 · **Legacy run:** 45802606122
**Main quote time:** 2026-11-26T10:36:36.041728+00:00 · **Legacy report time:** 2026-11-26T10:37:48.361020+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.07078 | 82.02 | -0.52% | 4.26x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 2 | INJ/USD | 6.188 | 80.98 | -0.24% | 2.64x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | SEI/USD ⭐ | 0.03586 | 78.19 | +0.56% | 1.37x | STRONG 89/100 | HIGH 66/100 | Watch |
| 4 | XRP/USD | 0.95072 | 76.76 | -0.21% | 2.25x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD | 0.147948 | 75.92 | -0.48% | 2.43x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD | 9.22266 | 60.52 | -0.07% | 0.35x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 7 | LTC/USD | 43.44 | 60.46 | -0.30% | 0.61x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 8 | XDG/USD | 0.0566286 | 56.61 | -0.04% | 0.81x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 9 | SOL/USD | 70.8 | 56.19 | -0.17% | 0.87x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 10 | ETH/USD | 1698.56 | 55.82 | -0.08% | 0.79x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 11 | XBT/USD | 60685.8 | 53.03 | -0.16% | 0.51x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | DCR/USD | 10.547 | 50.12 | +0.14% | 3.59x | STRONG 70/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03595 | 72.13 | +0.56% | 1.37x | 2352 | STRONG 91/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SEI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
