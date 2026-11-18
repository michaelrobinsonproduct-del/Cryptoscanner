# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:30:33.555667+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44347845161
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7b3492c43dcdc10a529f396516017764b3e5d842 (atomic ledger/results publication)
**Ledger generation:** 613 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.04955 | 58.316 | 58.916 | +5.09% | +1.21% | 0.34x | 18.2 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019603 | 57.146 | 61.989 | +5.00% | +0.01% | 0.51x | 8.2 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05291 | 33.535 | 39.833 | +2.46% | +0.49% | 0.12x | 17.0 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | WEAK 42/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | ZAMA/USD | 0.06034 | 29.014 | 32.238 | +0.68% | -0.07% | 0.71x | 8.3 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | WEAK 20/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | CT/USD | 0.116 | 24.986 | 41.119 | +2.65% | -1.44% | 0.11x | 17.2 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | WEAK 12/100 | EXTREME 98/100 | Do nothing | WATCH |
| 6 | FLR/USD | 0.00515 | 21.047 | 26.884 | +0.78% | -0.19% | 0.51x | 19.5 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | AKE/USD | 0.01005629 | 15.651 | 19.368 | +0.72% | -2.48% | 1.87x | 38.2 | 2026-11-18T16:30:28.987653+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 61.989 | 0.019603 | +0.01% | 0.51x |
| 2 | TRUST/USD | 58.916 | 0.04955 | +1.21% | 0.34x |
| 3 | CT/USD | 41.119 | 0.116 | -1.44% | 0.11x |
| 4 | MEGA/USD | 39.833 | 0.05291 | +0.49% | 0.12x |
| 5 | ZAMA/USD | 32.238 | 0.06034 | -0.07% | 0.71x |
| 6 | FLR/USD | 26.884 | 0.00515 | -0.19% | 0.51x |
| 7 | AKE/USD | 19.368 | 0.01005629 | -2.48% | 1.87x |

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

- Persisted scans: 613; predictions: 5261; observations: 370324.
- Matured sampled outcomes across 1/6/24/48h: 4490; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44347845161 · **Generation:** 613 · **Legacy run:** 44347845161
**Main quote time:** 2026-11-18T16:30:33.555667+00:00 · **Legacy report time:** 2026-11-18T16:30:57.325299+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.04955 | 58.32 | +1.21% | 0.34x | MODERATE 54/100 | VERY_HIGH 81/100 | Watch |
| 2 | SENT/USD | 0.019603 | 57.15 | +0.01% | 0.51x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 3 | MEGA/USD | 0.05291 | 33.53 | +0.49% | 0.12x | WEAK 42/100 | EXTREME 88/100 | Do nothing |
| 4 | ZAMA/USD | 0.06034 | 29.01 | -0.07% | 0.71x | WEAK 20/100 | EXTREME 88/100 | Do nothing |
| 5 | CT/USD | 0.116 | 24.99 | -1.44% | 0.11x | WEAK 12/100 | EXTREME 98/100 | Do nothing |
| 6 | FLR/USD | 0.00515 | 21.05 | -0.19% | 0.51x | WEAK 11/100 | EXTREME 94/100 | Do nothing |
| 7 | AKE/USD | 0.01005629 | 15.65 | -2.48% | 1.87x | WEAK 13/100 | VERY_HIGH 82/100 | Do nothing |

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
