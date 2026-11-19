# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:15:30.822939+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44635950141
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 54b25ec44ddc6f8d26cbccfe567ece6ff42729ef (atomic ledger/results publication)
**Ledger generation:** 877 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05973 | 58.084 | 67.865 | +6.66% | -0.48% | 0.26x | 18.4 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 29/100 | EXTREME 87/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.021355 | 55.768 | 55.622 | +3.64% | -0.53% | 1.28x | 8.4 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 38/100 | HIGH 66/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5311 | 51.553 | 43.538 | +2.53% | -1.40% | 7.19x | 13.2 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | VVV/USD | 21.855 | 48.638 | 57.969 | +0.85% | -0.45% | 0.29x | 5.9 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | INJ/USD | 7.08 | 47.347 | 52.602 | +1.42% | -0.42% | 0.69x | 5.7 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | USELESS/USD | 0.09893 | 46.973 | 54.414 | +3.53% | -0.52% | 0.52x | 21.3 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 18/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | CSPR/USD | 0.0016751 | 41.864 | 47.195 | +2.57% | +0.03% | 0.45x | 5.4 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | LIGHTER/USD | 2.774 | 36.203 | 43.162 | +2.21% | -1.03% | 0.82x | 14.5 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.096598 | 28.278 | 26.177 | +0.61% | +0.65% | 0.88x | 25.4 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | AKE/USD | 0.01047524 | 15.186 | 24.775 | +0.81% | -0.85% | 0.46x | 30.9 | 2026-11-19T23:15:22.542940+00:00 | Not calibrated | WEAK 3/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 67.865 | 0.05973 | -0.48% | 0.26x |
| 2 | VVV/USD | 57.969 | 21.855 | -0.45% | 0.29x |
| 3 | SENT/USD | 55.622 | 0.021355 | -0.53% | 1.28x |
| 4 | USELESS/USD | 54.414 | 0.09893 | -0.52% | 0.52x |
| 5 | INJ/USD | 52.602 | 7.08 | -0.42% | 0.69x |
| 6 | CSPR/USD | 47.195 | 0.0016751 | +0.03% | 0.45x |
| 7 | AKT/USD | 43.538 | 0.5311 | -1.40% | 7.19x |
| 8 | LIGHTER/USD | 43.162 | 2.774 | -1.03% | 0.82x |
| 9 | CAP/USD | 26.177 | 0.096598 | +0.65% | 0.88x |
| 10 | AKE/USD | 24.775 | 0.01047524 | -0.85% | 0.46x |

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

- Persisted scans: 877; predictions: 7635; observations: 529956.
- Matured sampled outcomes across 1/6/24/48h: 8115; gap abstentions: 15811. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44635950141 · **Generation:** 877 · **Legacy run:** 44635950141
**Main quote time:** 2026-11-19T23:15:30.822939+00:00 · **Legacy report time:** 2026-11-19T23:16:17.707122+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05973 | 58.08 | -0.48% | 0.26x | WEAK 29/100 | EXTREME 87/100 | Do nothing |
| 2 | SENT/USD | 0.021355 | 55.77 | -0.53% | 1.28x | WEAK 38/100 | HIGH 66/100 | Watch |
| 3 | AKT/USD | 0.5311 | 51.55 | -1.40% | 7.19x | MODERATE 51/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | VVV/USD | 21.855 | 48.64 | -0.45% | 0.29x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | INJ/USD | 7.08 | 47.35 | -0.42% | 0.69x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | USELESS/USD | 0.09893 | 46.97 | -0.52% | 0.52x | WEAK 18/100 | EXTREME 88/100 | Do nothing |
| 7 | CSPR/USD | 0.0016751 | 41.86 | +0.03% | 0.45x | WEAK 41/100 | VERY_HIGH 75/100 | Watch |
| 8 | LIGHTER/USD | 2.774 | 36.20 | -1.03% | 0.82x | WEAK 18/100 | VERY_HIGH 83/100 | Do nothing |
| 9 | CAP/USD | 0.096598 | 28.28 | +0.65% | 0.88x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | AKE/USD | 0.01047524 | 15.19 | -0.85% | 0.46x | WEAK 3/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
