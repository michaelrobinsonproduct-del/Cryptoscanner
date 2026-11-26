# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T13:31:19.392498+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45829647212
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 82408437d9d25c58d823b6cae766dc01efbef5d1 (atomic ledger/results publication)
**Ledger generation:** 1867 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.22407 | 76.086 | 67.243 | +1.99% | -0.05% | 1.91x | 3.3 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 2 | INJ/USD | 6.149 | 75.787 | 63.054 | +3.28% | -0.45% | 5.46x | 6.5 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ETH/USD | 1703.07 | 74.813 | 60.213 | +0.75% | +0.01% | 2.46x | 0.1 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | QNT/USD | 151.21 | 71.520 | 75.983 | +4.43% | -0.09% | 0.60x | 6.6 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | LTC/USD | 43.62 | 64.404 | 67.621 | +2.13% | +0.07% | 0.64x | 4.6 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ADA/USD | 0.14895 | 63.359 | 69.129 | +2.18% | +0.07% | 0.39x | 2.3 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03625 | 62.866 | 74.073 | +8.83% | -0.96% | 0.36x | 8.3 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | XRP/USD | 0.94946 | 57.920 | 64.589 | +1.38% | +0.18% | 0.24x | 0.1 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60776.5 | 56.053 | 59.721 | +0.68% | +0.06% | 0.60x | 0.0 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0568118 | 55.839 | 61.019 | +1.52% | -0.01% | 0.48x | 0.0 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SOL/USD | 70.86 | 51.411 | 58.968 | +0.67% | -0.07% | 0.28x | 1.4 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ASTER/USD | 0.49631 | 37.268 | 36.645 | +0.66% | -0.17% | 1.15x | 3.2 | 2026-11-26T13:31:12.447292+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 75.983 | 151.21 | -0.09% | 0.60x |
| 2 | SEI/USD | 74.073 | 0.03625 | -0.96% | 0.36x |
| 3 | ADA/USD | 69.129 | 0.14895 | +0.07% | 0.39x |
| 4 | LTC/USD | 67.621 | 43.62 | +0.07% | 0.64x |
| 5 | LINK/USD | 67.243 | 9.22407 | -0.05% | 1.91x |
| 6 | XRP/USD | 64.589 | 0.94946 | +0.18% | 0.24x |
| 7 | INJ/USD | 63.054 | 6.149 | -0.45% | 5.46x |
| 8 | XDG/USD | 61.019 | 0.0568118 | -0.01% | 0.48x |
| 9 | ETH/USD | 60.213 | 1703.07 | +0.01% | 2.46x |
| 10 | XBT/USD | 59.721 | 60776.5 | +0.06% | 0.60x |
| 11 | SOL/USD | 58.968 | 70.86 | -0.07% | 0.28x |
| 12 | ASTER/USD | 36.645 | 0.49631 | -0.17% | 1.15x |

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

- Persisted scans: 1867; predictions: 16139; observations: 1131477.
- Matured sampled outcomes across 1/6/24/48h: 34910; gap abstentions: 24834. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45829647212 · **Generation:** 1867 · **Legacy run:** 45829647212
**Main quote time:** 2026-11-26T13:31:19.392498+00:00 · **Legacy report time:** 2026-11-26T13:32:40.371925+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.22407 | 76.09 | -0.05% | 1.91x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 2 | INJ/USD | 6.149 | 75.79 | -0.45% | 5.46x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | ETH/USD | 1703.07 | 74.81 | +0.01% | 2.46x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | QNT/USD | 151.21 | 71.52 | -0.09% | 0.60x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 5 | LTC/USD | 43.62 | 64.40 | +0.07% | 0.64x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 6 | ADA/USD | 0.14895 | 63.36 | +0.07% | 0.39x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 7 | SEI/USD | 0.03625 | 62.87 | -0.96% | 0.36x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 8 | XRP/USD | 0.94946 | 57.92 | +0.18% | 0.24x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60776.5 | 56.05 | +0.06% | 0.60x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 10 | XDG/USD | 0.0568118 | 55.84 | -0.01% | 0.48x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SOL/USD | 70.86 | 51.41 | -0.07% | 0.28x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ASTER/USD | 0.49631 | 37.27 | -0.17% | 1.15x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BAT/USD | 0.08148 | 81.73 | +0.73% | 6.56x | 3066 | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 2 | SKY/USD | 0.04724 | 76.24 | +0.32% | 1.04x | 5501 | STRONG 73/100 | HIGH 67/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
