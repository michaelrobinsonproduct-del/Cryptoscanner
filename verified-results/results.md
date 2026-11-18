# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T00:00:16.992525+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44204076087
**Source SHA:** 113db7a045b71125e52affc5c74a39ca3094a032
**Previous ledger commit:** 8c293145149417500b5095ef3a9f2374beb7cfa3 (atomic ledger/results publication)
**Ledger generation:** 477 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3929 | 94.320 | 97.346 | +7.45% | +0.34% | 0.53x | 5.3 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | RENDER/USD | 1.483 | 90.788 | 72.735 | +7.70% | +0.61% | 3.03x | 13.5 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | AKT/USD | 0.5098 | 71.219 | 71.206 | +6.56% | +0.39% | 0.80x | 11.8 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | SUI/USD | 0.7384 | 66.288 | 72.810 | +2.64% | +0.07% | 0.31x | 1.4 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | VVV/USD | 21.064 | 65.420 | 75.468 | +4.55% | -0.29% | 0.14x | 8.1 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XLM/USD | 0.141332 | 63.275 | 59.789 | +2.57% | +0.22% | 1.24x | 3.7 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | POL/USD | 0.083 | 58.729 | 63.745 | +4.81% | +0.28% | 0.36x | 7.2 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | AAVE/USD | 112.43 | 55.436 | 65.695 | +3.64% | -0.24% | 0.09x | 4.4 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | ENA/USD | 0.1177 | 54.958 | 62.991 | +2.71% | -0.17% | 0.28x | 8.5 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | AVAX/USD | 7.286 | 54.213 | 60.025 | +2.46% | +0.08% | 0.38x | 4.1 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 69.94 | 47.402 | 54.862 | +0.29% | +0.07% | 0.22x | 4.3 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TRX/USD | 0.307962 | 43.103 | 46.217 | +1.01% | -0.03% | 0.70x | 0.0 | 2026-11-18T00:00:08.573088+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 97.346 | 3.3929 | +0.34% | 0.53x |
| 2 | VVV/USD | 75.468 | 21.064 | -0.29% | 0.14x |
| 3 | SUI/USD | 72.810 | 0.7384 | +0.07% | 0.31x |
| 4 | RENDER/USD | 72.735 | 1.483 | +0.61% | 3.03x |
| 5 | AKT/USD | 71.206 | 0.5098 | +0.39% | 0.80x |
| 6 | AAVE/USD | 65.695 | 112.43 | -0.24% | 0.09x |
| 7 | POL/USD | 63.745 | 0.083 | +0.28% | 0.36x |
| 8 | ENA/USD | 62.991 | 0.1177 | -0.17% | 0.28x |
| 9 | AVAX/USD | 60.025 | 7.286 | +0.08% | 0.38x |
| 10 | XLM/USD | 59.789 | 0.141332 | +0.22% | 1.24x |
| 11 | HYPE/USD | 54.862 | 69.94 | +0.07% | 0.22x |
| 12 | TRX/USD | 46.217 | 0.307962 | -0.03% | 0.70x |

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

- Persisted scans: 477; predictions: 4205; observations: 287500.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44204076087 · **Generation:** 477 · **Legacy run:** 44204076087
**Main quote time:** 2026-11-18T00:00:16.992525+00:00 · **Legacy report time:** 2026-11-18T00:00:28.492647+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.3929 | 94.32 | +0.34% | 0.53x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 2 | RENDER/USD | 1.483 | 90.79 | +0.61% | 3.03x | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 3 | AKT/USD | 0.5098 | 71.22 | +0.39% | 0.80x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 4 | SUI/USD | 0.7384 | 66.29 | +0.07% | 0.31x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 5 | VVV/USD | 21.064 | 65.42 | -0.29% | 0.14x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 6 | XLM/USD | 0.141332 | 63.27 | +0.22% | 1.24x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | POL/USD | 0.083 | 58.73 | +0.28% | 0.36x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 8 | AAVE/USD | 112.43 | 55.44 | -0.24% | 0.09x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | ENA/USD | 0.1177 | 54.96 | -0.17% | 0.28x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | AVAX/USD | 7.286 | 54.21 | +0.08% | 0.38x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 69.94 | 47.40 | +0.07% | 0.22x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 12 | TRX/USD | 0.307962 | 43.10 | -0.03% | 0.70x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |

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
