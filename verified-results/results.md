# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:20:23.515071+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44564801666
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** da12c3b7c1434333ded5e5e8509516610a6f7901 (atomic ledger/results publication)
**Ledger generation:** 811 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BMT/USD | 0.02019 | 86.223 | 71.223 | +6.94% | +0.00% | 2.67x | 9.9 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | STRONG 88/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 22.579 | 74.979 | 80.551 | +4.19% | +0.42% | 0.23x | 7.6 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SKR/USD | 0.010377 | 72.519 | 65.904 | +7.72% | -1.68% | 2.80x | 20.3 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | HYPE/USD | 67.57 | 68.826 | 61.481 | +1.03% | -0.38% | 1.93x | 1.5 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5446 | 68.029 | 63.736 | +5.14% | -0.37% | 1.61x | 7.4 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | SENT/USD | 0.021616 | 64.352 | 64.524 | +4.91% | +1.53% | 0.22x | 8.3 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | PYTH/USD | 0.05629 | 63.437 | 69.174 | +6.69% | -0.67% | 0.76x | 16.1 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 8 | TRUST/USD | 0.05467 | 61.961 | 62.432 | +11.12% | +1.18% | 0.36x | 27.5 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | SYRUP/USD | 0.10199 | 60.273 | 71.050 | +7.40% | -1.39% | 0.62x | 10.8 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | WEAK 30/100 | EXTREME 98/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.97135 | 56.336 | 58.556 | +0.52% | +0.05% | 0.75x | 0.1 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 11 | USELESS/USD | 0.10073 | 55.493 | 63.664 | +5.41% | -0.04% | 0.20x | 22.9 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | ADA/USD | 0.152228 | 50.363 | 56.748 | +0.64% | +0.21% | 0.25x | 5.5 | 2026-11-19T16:20:15.165491+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.551 | 22.579 | +0.42% | 0.23x |
| 2 | BMT/USD | 71.223 | 0.02019 | +0.00% | 2.67x |
| 3 | SYRUP/USD | 71.050 | 0.10199 | -1.39% | 0.62x |
| 4 | PYTH/USD | 69.174 | 0.05629 | -0.67% | 0.76x |
| 5 | SKR/USD | 65.904 | 0.010377 | -1.68% | 2.80x |
| 6 | SENT/USD | 64.524 | 0.021616 | +1.53% | 0.22x |
| 7 | AKT/USD | 63.736 | 0.5446 | -0.37% | 1.61x |
| 8 | USELESS/USD | 63.664 | 0.10073 | -0.04% | 0.20x |
| 9 | TRUST/USD | 62.432 | 0.05467 | +1.18% | 0.36x |
| 10 | HYPE/USD | 61.481 | 67.57 | -0.38% | 1.93x |
| 11 | XRP/USD | 58.556 | 0.97135 | +0.05% | 0.75x |
| 12 | ADA/USD | 56.748 | 0.152228 | +0.21% | 0.25x |

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

- Persisted scans: 811; predictions: 6876; observations: 490393.
- Matured sampled outcomes across 1/6/24/48h: 6875; gap abstentions: 15330. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44564801666 · **Generation:** 811 · **Legacy run:** 44564801666
**Main quote time:** 2026-11-19T16:20:23.515071+00:00 · **Legacy report time:** 2026-11-19T16:21:07.121246+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD | 0.02019 | 86.22 | +0.00% | 2.67x | STRONG 88/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD | 22.579 | 74.98 | +0.42% | 0.23x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 3 | SKR/USD | 0.010377 | 72.52 | -1.68% | 2.80x | MODERATE 56/100 | EXTREME 89/100 | Do nothing |
| 4 | HYPE/USD | 67.57 | 68.83 | -0.38% | 1.93x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 5 | AKT/USD | 0.5446 | 68.03 | -0.37% | 1.61x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 6 | SENT/USD | 0.021616 | 64.35 | +1.53% | 0.22x | MODERATE 62/100 | VERY_HIGH 75/100 | Watch |
| 7 | PYTH/USD | 0.05629 | 63.44 | -0.67% | 0.76x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |
| 8 | TRUST/USD | 0.05467 | 61.96 | +1.18% | 0.36x | MODERATE 51/100 | EXTREME 94/100 | Do nothing |
| 9 | SYRUP/USD | 0.10199 | 60.27 | -1.39% | 0.62x | WEAK 30/100 | EXTREME 98/100 | Do nothing |
| 10 | XRP/USD | 0.97135 | 56.34 | +0.05% | 0.75x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 11 | USELESS/USD | 0.10073 | 55.49 | -0.04% | 0.20x | WEAK 23/100 | EXTREME 88/100 | Do nothing |
| 12 | ADA/USD | 0.152228 | 50.36 | +0.21% | 0.25x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002661 | 64.53 | +0.15% | 2.17x | 4135 | STRONG 72/100 | HIGH 61/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
