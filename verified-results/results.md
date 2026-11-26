# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T23:03:40.795239+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45908183252
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2fdb6841924c4c8697a513560614a457c1d7bea5 (atomic ledger/results publication)
**Ledger generation:** 1925 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 600; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.3887 | 75.866 | 80.072 | +8.64% | -0.18% | 0.67x | 7.0 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | LTC/USD | 43.88 | 68.178 | 73.036 | +2.74% | -0.05% | 0.54x | 2.3 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5029 | 66.799 | 73.023 | +6.30% | -0.20% | 0.48x | 8.0 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | ZRO/USD | 1.122 | 65.927 | 72.086 | +9.57% | -0.09% | 0.43x | 17.8 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07137 | 63.114 | 69.928 | +7.70% | +0.34% | 0.15x | 14.0 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | LINK/USD | 9.27561 | 59.521 | 70.767 | +2.56% | -0.30% | 0.03x | 4.2 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.14 | 57.047 | 60.102 | +0.84% | -0.32% | 0.85x | 1.6 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | XRP/USD | 0.94387 | 56.573 | 60.411 | +0.78% | -0.22% | 0.73x | 0.1 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SOL/USD | 70.97 | 56.509 | 60.063 | +0.82% | -0.29% | 0.79x | 1.4 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | PENGU/USD | 0.004365 | 39.482 | 30.550 | +0.37% | -0.43% | 2.11x | 6.9 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0563247 | 37.091 | 46.671 | +0.65% | -0.16% | 0.12x | 1.5 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ONDO/USD | 0.28723 | 35.128 | 43.231 | +1.67% | -0.26% | 0.32x | 2.1 | 2026-11-26T23:03:33.008316+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 80.072 | 0.3887 | -0.18% | 0.67x |
| 2 | LTC/USD | 73.036 | 43.88 | -0.05% | 0.54x |
| 3 | AKT/USD | 73.023 | 0.5029 | -0.20% | 0.48x |
| 4 | ZRO/USD | 72.086 | 1.122 | -0.09% | 0.43x |
| 5 | LINK/USD | 70.767 | 9.27561 | -0.30% | 0.03x |
| 6 | SYRUP/USD | 69.928 | 0.07137 | +0.34% | 0.15x |
| 7 | XRP/USD | 60.411 | 0.94387 | -0.22% | 0.73x |
| 8 | HYPE/USD | 60.102 | 62.14 | -0.32% | 0.85x |
| 9 | SOL/USD | 60.063 | 70.97 | -0.29% | 0.79x |
| 10 | XDG/USD | 46.671 | 0.0563247 | -0.16% | 0.12x |
| 11 | ONDO/USD | 43.231 | 0.28723 | -0.26% | 0.32x |
| 12 | PENGU/USD | 30.550 | 0.004365 | -0.43% | 2.11x |

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

- Persisted scans: 1925; predictions: 16835; observations: 1166011.
- Matured sampled outcomes across 1/6/24/48h: 36716; gap abstentions: 25330. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
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

**Writer:** 45908183252 · **Generation:** 1925 · **Legacy run:** 45908183252
**Main quote time:** 2026-11-26T23:03:40.795239+00:00 · **Legacy report time:** 2026-11-26T23:04:32.210766+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.3887 | 75.87 | -0.18% | 0.67x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 2 | LTC/USD | 43.88 | 68.18 | -0.05% | 0.54x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 3 | AKT/USD | 0.5029 | 66.80 | -0.20% | 0.48x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 4 | ZRO/USD | 1.122 | 65.93 | -0.09% | 0.43x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 5 | SYRUP/USD | 0.07137 | 63.11 | +0.34% | 0.15x | MODERATE 57/100 | VERY_HIGH 81/100 | Watch |
| 6 | LINK/USD | 9.27561 | 59.52 | -0.30% | 0.03x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 7 | HYPE/USD | 62.14 | 57.05 | -0.32% | 0.85x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 8 | XRP/USD | 0.94387 | 56.57 | -0.22% | 0.73x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SOL/USD | 70.97 | 56.51 | -0.29% | 0.79x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 10 | PENGU/USD | 0.004365 | 39.48 | -0.43% | 2.11x | MODERATE 50/100 | VERY_HIGH 73/100 | Watch |
| 11 | XDG/USD | 0.0563247 | 37.09 | -0.16% | 0.12x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ONDO/USD | 0.28723 | 35.13 | -0.26% | 0.32x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |

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
