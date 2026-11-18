# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:15:15.971304+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44344919835
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 91c3115fc0977cc18d1a6b691342a995bfe27001 (atomic ledger/results publication)
**Ledger generation:** 610 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019577 | 55.553 | 61.012 | +4.86% | -0.56% | 0.73x | 8.2 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 33/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | INFI/USD | 0.1323 | 45.953 | 49.238 | +4.17% | -1.19% | 1.27x | 22.7 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 23/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | TRUST/USD | 0.04896 | 39.821 | 47.019 | +3.84% | +0.16% | 0.20x | 24.5 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.1177 | 37.691 | 51.781 | +4.16% | -1.01% | 0.10x | 16.9 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 19/100 | EXTREME 98/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.309052 | 35.266 | 43.178 | +0.37% | -0.03% | 0.22x | 0.0 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | AKE/USD | 0.01031152 | 28.015 | 39.030 | +3.28% | -1.27% | 0.53x | 34.8 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 9/100 | EXTREME 97/100 | Do nothing | WATCH |
| 7 | MEGA/USD | 0.05265 | 27.995 | 37.230 | +1.96% | +0.06% | 0.05x | 15.2 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 29/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | ZAMA/USD | 0.06038 | 27.904 | 31.891 | +0.75% | -0.31% | 0.76x | 9.9 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | FLR/USD | 0.00516 | 23.531 | 18.602 | +0.98% | +0.00% | 1.49x | 38.9 | 2026-11-18T16:15:11.074243+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 61.012 | 0.019577 | -0.56% | 0.73x |
| 2 | CT/USD | 51.781 | 0.1177 | -1.01% | 0.10x |
| 3 | INFI/USD | 49.238 | 0.1323 | -1.19% | 1.27x |
| 4 | TRUST/USD | 47.019 | 0.04896 | +0.16% | 0.20x |
| 5 | TRX/USD | 43.178 | 0.309052 | -0.03% | 0.22x |
| 6 | AKE/USD | 39.030 | 0.01031152 | -1.27% | 0.53x |
| 7 | MEGA/USD | 37.230 | 0.05265 | +0.06% | 0.05x |
| 8 | ZAMA/USD | 31.891 | 0.06038 | -0.31% | 0.76x |
| 9 | FLR/USD | 18.602 | 0.00516 | +0.00% | 1.49x |

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

- Persisted scans: 610; predictions: 5238; observations: 368497.
- Matured sampled outcomes across 1/6/24/48h: 4448; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44344919835 · **Generation:** 610 · **Legacy run:** 44344919835
**Main quote time:** 2026-11-18T16:15:15.971304+00:00 · **Legacy report time:** 2026-11-18T16:15:43.586141+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019577 | 55.55 | -0.56% | 0.73x | WEAK 33/100 | EXTREME 88/100 | Do nothing |
| 2 | INFI/USD | 0.1323 | 45.95 | -1.19% | 1.27x | WEAK 23/100 | EXTREME 89/100 | Do nothing |
| 3 | TRUST/USD | 0.04896 | 39.82 | +0.16% | 0.20x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 4 | CT/USD | 0.1177 | 37.69 | -1.01% | 0.10x | WEAK 19/100 | EXTREME 98/100 | Do nothing |
| 5 | TRX/USD | 0.309052 | 35.27 | -0.03% | 0.22x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | AKE/USD | 0.01031152 | 28.02 | -1.27% | 0.53x | WEAK 9/100 | EXTREME 97/100 | Do nothing |
| 7 | MEGA/USD | 0.05265 | 28.00 | +0.06% | 0.05x | WEAK 29/100 | EXTREME 88/100 | Do nothing |
| 8 | ZAMA/USD | 0.06038 | 27.90 | -0.31% | 0.76x | WEAK 19/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | FLR/USD | 0.00516 | 23.53 | +0.00% | 1.49x | WEAK 32/100 | VERY_HIGH 79/100 | Do nothing |

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
