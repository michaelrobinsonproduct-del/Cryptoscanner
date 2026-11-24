# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T18:57:31.204051+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45464554615
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 64ff2445db0afe7e2faa866cb383f8f58198d3aa (atomic ledger/results publication)
**Ledger generation:** 1613 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | GBP/USD | 1.31105 | 73.968 | 59.113 | +0.60% | -0.03% | 3.69x | 0.2 | 2026-11-24T18:57:26.005354+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 502.86 | 69.255 | 74.276 | +3.46% | -0.67% | 0.83x | 10.0 | 2026-11-24T18:57:26.005354+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 3 | VVV/USD | 25.042 | 62.197 | 69.810 | +2.43% | +0.04% | 0.22x | 4.4 | 2026-11-24T18:57:26.005354+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.702e-05 | 50.634 | 60.833 | +8.17% | -0.25% | 0.11x | 32.0 | 2026-11-24T18:57:26.005354+00:00 | Not calibrated | WEAK 20/100 | EXTREME 93/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.04844 | 49.966 | 40.358 | +0.60% | -0.59% | 2.26x | 10.3 | 2026-11-24T18:57:26.005354+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.436e-06 | 40.226 | 44.064 | +0.41% | -0.38% | 0.81x | 5.8 | 2026-11-24T18:57:26.005354+00:00 | Not calibrated | WEAK 25/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.276 | 502.86 | -0.67% | 0.83x |
| 2 | VVV/USD | 69.810 | 25.042 | +0.04% | 0.22x |
| 3 | LUNA/USD | 60.833 | 4.702e-05 | -0.25% | 0.11x |
| 4 | GBP/USD | 59.113 | 1.31105 | -0.03% | 3.69x |
| 5 | PEPE/USD | 44.064 | 3.436e-06 | -0.38% | 0.81x |
| 6 | NIGHT/USD | 40.358 | 0.04844 | -0.59% | 2.26x |

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

- Persisted scans: 1613; predictions: 13851; observations: 977409.
- Matured sampled outcomes across 1/6/24/48h: 28028; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45464554615 · **Generation:** 1613 · **Legacy run:** 45464554615
**Main quote time:** 2026-11-24T18:57:31.204051+00:00 · **Legacy report time:** 2026-11-24T18:58:45.377940+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD | 1.31105 | 73.97 | -0.03% | 3.69x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 502.86 | 69.26 | -0.67% | 0.83x | WEAK 40/100 | HIGH 68/100 | Watch |
| 3 | VVV/USD | 25.042 | 62.20 | +0.04% | 0.22x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 4 | LUNA/USD | 4.702e-05 | 50.63 | -0.25% | 0.11x | WEAK 20/100 | EXTREME 93/100 | Do nothing |
| 5 | NIGHT/USD | 0.04844 | 49.97 | -0.59% | 2.26x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 6 | PEPE/USD | 3.436e-06 | 40.23 | -0.38% | 0.81x | WEAK 25/100 | HIGH 68/100 | Do nothing |

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
