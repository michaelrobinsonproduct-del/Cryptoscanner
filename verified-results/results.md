# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:25:16.062951+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44346892804
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 4bf2c1b98130dcb4284bec4b051dd80cae8a29ec (atomic ledger/results publication)
**Ledger generation:** 612 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.04963 | 55.540 | 58.102 | +5.26% | +1.14% | 0.17x | 22.2 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 87/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.01947 | 52.010 | 59.029 | +4.29% | -0.33% | 0.46x | 4.1 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 31/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | TRX/USD | 0.308783 | 37.217 | 42.500 | +0.29% | -0.15% | 0.55x | 0.0 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | ZAMA/USD | 0.06063 | 31.192 | 34.833 | +1.17% | -0.26% | 0.77x | 9.9 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.01015582 | 28.752 | 31.291 | +1.72% | -1.08% | 1.29x | 28.4 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | MEGA/USD | 0.05271 | 26.012 | 35.200 | +2.07% | -0.08% | 0.12x | 20.8 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 8/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | FLR/USD | 0.00515 | 21.744 | 26.918 | +0.78% | -0.19% | 0.58x | 19.4 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | CT/USD | 0.1157 | 15.987 | 39.208 | +2.39% | -3.03% | 0.19x | 17.3 | 2026-11-18T16:25:11.529941+00:00 | Not calibrated | WEAK 8/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 59.029 | 0.01947 | -0.33% | 0.46x |
| 2 | TRUST/USD | 58.102 | 0.04963 | +1.14% | 0.17x |
| 3 | TRX/USD | 42.500 | 0.308783 | -0.15% | 0.55x |
| 4 | CT/USD | 39.208 | 0.1157 | -3.03% | 0.19x |
| 5 | MEGA/USD | 35.200 | 0.05271 | -0.08% | 0.12x |
| 6 | ZAMA/USD | 34.833 | 0.06063 | -0.26% | 0.77x |
| 7 | AKE/USD | 31.291 | 0.01015582 | -1.08% | 1.29x |
| 8 | FLR/USD | 26.918 | 0.00515 | -0.19% | 0.58x |

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

- Persisted scans: 612; predictions: 5254; observations: 369715.
- Matured sampled outcomes across 1/6/24/48h: 4480; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44346892804 · **Generation:** 612 · **Legacy run:** 44346892804
**Main quote time:** 2026-11-18T16:25:16.062951+00:00 · **Legacy report time:** 2026-11-18T16:25:45.884439+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.04963 | 55.54 | +1.14% | 0.17x | MODERATE 48/100 | EXTREME 87/100 | Do nothing |
| 2 | SENT/USD | 0.01947 | 52.01 | -0.33% | 0.46x | WEAK 31/100 | EXTREME 88/100 | Do nothing |
| 3 | TRX/USD | 0.308783 | 37.22 | -0.15% | 0.55x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | ZAMA/USD | 0.06063 | 31.19 | -0.26% | 0.77x | WEAK 21/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | AKE/USD | 0.01015582 | 28.75 | -1.08% | 1.29x | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | MEGA/USD | 0.05271 | 26.01 | -0.08% | 0.12x | WEAK 8/100 | EXTREME 100/100 | Do nothing |
| 7 | FLR/USD | 0.00515 | 21.74 | -0.19% | 0.58x | WEAK 11/100 | EXTREME 94/100 | Do nothing |
| 8 | CT/USD | 0.1157 | 15.99 | -3.03% | 0.19x | WEAK 8/100 | EXTREME 98/100 | Do nothing |

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
