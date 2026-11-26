# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T04:45:55.141798+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45757119400
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bf7fa907e4e11712e40b13cc6ecc4dd848ac9258 (atomic ledger/results publication)
**Ledger generation:** 1814 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 43.98 | 77.324 | 74.677 | +2.97% | +0.02% | 1.25x | 2.3 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 2 | TAO/USD | 184.1293 | 75.300 | 61.068 | +1.40% | -0.15% | 3.40x | 7.4 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PAXG/USD | 3588.98 | 74.099 | 57.835 | +0.54% | +0.25% | 12.38x | 1.9 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ADA/USD | 0.149014 | 72.024 | 68.868 | +2.23% | +0.10% | 1.26x | 3.4 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 61/100 | HIGH 55/100 | Watch | WATCH |
| 5 | BABY/USD | 0.00961 | 68.188 | 70.848 | +10.33% | +0.10% | 0.68x | 10.4 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | SEI/USD | 0.03519 | 61.062 | 67.109 | +5.64% | -0.26% | 0.52x | 8.5 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95694 | 61.047 | 69.919 | +2.18% | -0.04% | 0.13x | 0.6 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LINK/USD | 9.23484 | 58.977 | 65.858 | +2.10% | +0.03% | 0.30x | 3.4 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | AUD/USD | 0.66482 | 58.498 | 49.847 | +0.28% | +0.04% | 1.85x | 0.3 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 71.13 | 58.047 | 61.656 | +1.05% | -0.06% | 0.67x | 1.4 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1701.73 | 57.760 | 59.658 | +0.67% | +0.04% | 0.79x | 0.1 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SYRUP/USD | 0.07115 | 54.458 | 68.653 | +7.36% | -1.55% | 0.36x | 16.9 | 2026-11-26T04:45:47.122530+00:00 | Not calibrated | WEAK 27/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 74.677 | 43.98 | +0.02% | 1.25x |
| 2 | BABY/USD | 70.848 | 0.00961 | +0.10% | 0.68x |
| 3 | XRP/USD | 69.919 | 0.95694 | -0.04% | 0.13x |
| 4 | ADA/USD | 68.868 | 0.149014 | +0.10% | 1.26x |
| 5 | SYRUP/USD | 68.653 | 0.07115 | -1.55% | 0.36x |
| 6 | SEI/USD | 67.109 | 0.03519 | -0.26% | 0.52x |
| 7 | LINK/USD | 65.858 | 9.23484 | +0.03% | 0.30x |
| 8 | SOL/USD | 61.656 | 71.13 | -0.06% | 0.67x |
| 9 | TAO/USD | 61.068 | 184.1293 | -0.15% | 3.40x |
| 10 | ETH/USD | 59.658 | 1701.73 | +0.04% | 0.79x |
| 11 | PAXG/USD | 57.835 | 3588.98 | +0.25% | 12.38x |
| 12 | AUD/USD | 49.847 | 0.66482 | +0.04% | 1.85x |

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

- Persisted scans: 1814; predictions: 15503; observations: 1099770.
- Matured sampled outcomes across 1/6/24/48h: 33647; gap abstentions: 23887. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45757119400 · **Generation:** 1814 · **Legacy run:** 45757119400
**Main quote time:** 2026-11-26T04:45:55.141798+00:00 · **Legacy report time:** 2026-11-26T04:46:47.690975+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 43.98 | 77.32 | +0.02% | 1.25x | MODERATE 64/100 | HIGH 55/100 | Watch |
| 2 | TAO/USD | 184.1293 | 75.30 | -0.15% | 3.40x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | PAXG/USD | 3588.98 | 74.10 | +0.25% | 12.38x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 4 | ADA/USD ⭐ | 0.149014 | 72.02 | +0.10% | 1.26x | STRONG 71/100 | HIGH 55/100 | Watch |
| 5 | BABY/USD | 0.00961 | 68.19 | +0.10% | 0.68x | MODERATE 49/100 | EXTREME 88/100 | Do nothing |
| 6 | SEI/USD | 0.03519 | 61.06 | -0.26% | 0.52x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 7 | XRP/USD | 0.95694 | 61.05 | -0.04% | 0.13x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | LINK/USD | 9.23484 | 58.98 | +0.03% | 0.30x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | AUD/USD | 0.66482 | 58.50 | +0.04% | 1.85x | MODERATE 64/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD | 71.13 | 58.05 | -0.06% | 0.67x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1701.73 | 57.76 | +0.04% | 0.79x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | SYRUP/USD | 0.07115 | 54.46 | -1.55% | 0.36x | WEAK 27/100 | EXTREME 91/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.149136 | 70.74 | +0.10% | 1.26x | 11508 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
