# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T07:07:47.850222+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46119505137
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f873d3f9db75ff0be5b6da73905619c54c7bfad3 (atomic ledger/results publication)
**Ledger generation:** 2121 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 424.82 | 67.143 | 75.145 | +4.31% | -0.85% | 0.62x | 20.0 | 2026-11-28T07:07:43.626057+00:00 | Not calibrated | WEAK 29/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | VVV/USD | 26.191 | 50.757 | 51.479 | +1.72% | -0.02% | 0.94x | 10.3 | 2026-11-28T07:07:43.626057+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 3 | ZEC/USD | 736.86 | 46.394 | 54.602 | +0.31% | -0.58% | 0.47x | 5.2 | 2026-11-28T07:07:43.626057+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | NEAR/USD | 3.0265 | 44.192 | 54.281 | +0.28% | -0.08% | 0.03x | 5.3 | 2026-11-28T07:07:43.626057+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | SHX/USD | 0.003366 | 37.893 | 25.560 | +0.54% | -0.53% | 22.89x | 17.8 | 2026-11-28T07:07:43.626057+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 75.145 | 424.82 | -0.85% | 0.62x |
| 2 | ZEC/USD | 54.602 | 736.86 | -0.58% | 0.47x |
| 3 | NEAR/USD | 54.281 | 3.0265 | -0.08% | 0.03x |
| 4 | VVV/USD | 51.479 | 26.191 | -0.02% | 0.94x |
| 5 | SHX/USD | 25.560 | 0.003366 | -0.53% | 22.89x |

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

- Persisted scans: 2121; predictions: 19007; observations: 1284372.
- Matured sampled outcomes across 1/6/24/48h: 44565; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46119505137 · **Generation:** 2121 · **Legacy run:** 46119505137
**Main quote time:** 2026-11-28T07:07:47.850222+00:00 · **Legacy report time:** 2026-11-28T07:08:42.310330+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 424.82 | 67.14 | -0.85% | 0.62x | WEAK 29/100 | EXTREME 88/100 | Do nothing |
| 2 | VVV/USD | 26.191 | 50.76 | -0.02% | 0.94x | WEAK 25/100 | VERY_HIGH 74/100 | Do nothing |
| 3 | ZEC/USD | 736.86 | 46.39 | -0.58% | 0.47x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | NEAR/USD | 3.0265 | 44.19 | -0.08% | 0.03x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | SHX/USD | 0.003366 | 37.89 | -0.53% | 22.89x | WEAK 44/100 | VERY_HIGH 79/100 | Watch |

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
