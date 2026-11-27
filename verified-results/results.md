# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T21:22:32.270042+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46069548431
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c4d3eb68297f5bebb7733f45c7c028f7d5ea8bd4 (atomic ledger/results publication)
**Ledger generation:** 2062 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 735.12 | 113.885 | 99.252 | +7.84% | -0.07% | 3.21x | 1.5 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XDG/USD | 0.0576943 | 80.086 | 71.301 | +2.34% | -0.05% | 1.90x | 0.2 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TAO/USD | 187.7423 | 79.929 | 65.741 | +2.15% | -0.16% | 9.84x | 8.7 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.05021 | 79.764 | 78.139 | +3.59% | +0.36% | 0.98x | 4.0 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LTC/USD | 44.38 | 73.007 | 64.115 | +1.46% | -0.05% | 1.91x | 2.3 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XAUT/USD | 3646.8 | 69.844 | 54.721 | +2.45% | +0.02% | 10.62x | 0.3 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 64.08 | 69.029 | 75.145 | +2.99% | -0.02% | 0.40x | 1.6 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SPACE/USD | 0.004173 | 66.206 | 71.058 | +7.77% | +0.12% | 0.45x | 9.6 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94835 | 65.978 | 59.105 | +0.59% | -0.03% | 1.70x | 0.1 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.529e-06 | 63.462 | 54.680 | +1.47% | -0.03% | 1.89x | 2.8 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SOL/USD | 71.87 | 60.541 | 63.481 | +1.31% | -0.07% | 0.74x | 1.4 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | PAXG/USD | 3643.14 | 56.855 | 59.196 | +2.43% | +0.01% | 0.76x | 1.8 | 2026-11-27T21:22:24.450521+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.252 | 735.12 | -0.07% | 3.21x |
| 2 | NIGHT/USD | 78.139 | 0.05021 | +0.36% | 0.98x |
| 3 | HYPE/USD | 75.145 | 64.08 | -0.02% | 0.40x |
| 4 | XDG/USD | 71.301 | 0.0576943 | -0.05% | 1.90x |
| 5 | SPACE/USD | 71.058 | 0.004173 | +0.12% | 0.45x |
| 6 | TAO/USD | 65.741 | 187.7423 | -0.16% | 9.84x |
| 7 | LTC/USD | 64.115 | 44.38 | -0.05% | 1.91x |
| 8 | SOL/USD | 63.481 | 71.87 | -0.07% | 0.74x |
| 9 | PAXG/USD | 59.196 | 3643.14 | +0.01% | 0.76x |
| 10 | XRP/USD | 59.105 | 0.94835 | -0.03% | 1.70x |
| 11 | XAUT/USD | 54.721 | 3646.8 | +0.02% | 10.62x |
| 12 | PEPE/USD | 54.680 | 3.529e-06 | -0.03% | 1.89x |

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

- Persisted scans: 2062; predictions: 18446; observations: 1248620.
- Matured sampled outcomes across 1/6/24/48h: 41843; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46069548431 · **Generation:** 2062 · **Legacy run:** 46069548431
**Main quote time:** 2026-11-27T21:22:32.270042+00:00 · **Legacy report time:** 2026-11-27T21:23:16.995840+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 735.12 | 113.89 | -0.07% | 3.21x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XDG/USD | 0.0576943 | 80.09 | -0.05% | 1.90x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 3 | TAO/USD | 187.7423 | 79.93 | -0.16% | 9.84x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.05021 | 79.76 | +0.36% | 0.98x | STRONG 70/100 | HIGH 62/100 | Watch |
| 5 | LTC/USD | 44.38 | 73.01 | -0.05% | 1.91x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | XAUT/USD | 3646.8 | 69.84 | +0.02% | 10.62x | STRONG 80/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD | 64.08 | 69.03 | -0.02% | 0.40x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 8 | SPACE/USD | 0.004173 | 66.21 | +0.12% | 0.45x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |
| 9 | XRP/USD | 0.94835 | 65.98 | -0.03% | 1.70x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | PEPE/USD | 3.529e-06 | 63.46 | -0.03% | 1.89x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 11 | SOL/USD | 71.87 | 60.54 | -0.07% | 0.74x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | PAXG/USD | 3643.14 | 56.85 | +0.01% | 0.76x | MODERATE 48/100 | HIGH 62/100 | Watch |

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
