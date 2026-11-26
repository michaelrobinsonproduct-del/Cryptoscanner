# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T10:06:19.326288+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45797884462
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5c9b58d90ab1bc21f0e8dd413e2842c2b0d50cb5 (atomic ledger/results publication)
**Ledger generation:** 1846 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 584; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03588 | 76.330 | 73.071 | +7.72% | +0.96% | 0.85x | 8.3 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XBT/USD | 60818.8 | 74.607 | 60.212 | +0.75% | -0.12% | 2.67x | 0.0 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 71.04 | 73.378 | 60.760 | +0.92% | -0.18% | 2.35x | 1.4 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 43.62 | 72.471 | 68.768 | +2.13% | -0.30% | 1.52x | 2.3 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 9.24511 | 72.289 | 68.913 | +2.22% | -0.19% | 1.43x | 3.2 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XMR/USD | 524.74 | 68.095 | 63.261 | +1.51% | +0.15% | 1.41x | 4.6 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 7 | INJ/USD | 6.238 | 67.148 | 73.661 | +4.77% | +0.11% | 0.29x | 6.4 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.0661 | 63.825 | 57.249 | +0.53% | +0.29% | 1.51x | 2.9 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95345 | 61.491 | 67.571 | +1.80% | +0.01% | 0.39x | 0.1 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SYRUP/USD | 0.07081 | 60.447 | 65.313 | +6.85% | +0.01% | 0.51x | 24.0 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | WEAK 40/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1701.94 | 58.931 | 59.745 | +0.68% | -0.06% | 0.95x | 0.1 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | ADA/USD | 0.148673 | 58.740 | 67.124 | +1.99% | -0.34% | 0.33x | 3.6 | 2026-11-26T10:06:10.618157+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 73.661 | 6.238 | +0.11% | 0.29x |
| 2 | SEI/USD | 73.071 | 0.03588 | +0.96% | 0.85x |
| 3 | LINK/USD | 68.913 | 9.24511 | -0.19% | 1.43x |
| 4 | LTC/USD | 68.768 | 43.62 | -0.30% | 1.52x |
| 5 | XRP/USD | 67.571 | 0.95345 | +0.01% | 0.39x |
| 6 | ADA/USD | 67.124 | 0.148673 | -0.34% | 0.33x |
| 7 | SYRUP/USD | 65.313 | 0.07081 | +0.01% | 0.51x |
| 8 | XMR/USD | 63.261 | 524.74 | +0.15% | 1.41x |
| 9 | SOL/USD | 60.760 | 71.04 | -0.18% | 2.35x |
| 10 | XBT/USD | 60.212 | 60818.8 | -0.12% | 2.67x |
| 11 | ETH/USD | 59.745 | 1701.94 | -0.06% | 0.95x |
| 12 | NEAR/USD | 57.249 | 3.0661 | +0.29% | 1.51x |

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

- Persisted scans: 1846; predictions: 15887; observations: 1119156.
- Matured sampled outcomes across 1/6/24/48h: 34418; gap abstentions: 24521. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45797884462 · **Generation:** 1846 · **Legacy run:** 45797884462
**Main quote time:** 2026-11-26T10:06:19.326288+00:00 · **Legacy report time:** 2026-11-26T10:07:13.318987+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD | 0.03588 | 76.33 | +0.96% | 0.85x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 2 | XBT/USD | 60818.8 | 74.61 | -0.12% | 2.67x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD | 71.04 | 73.38 | -0.18% | 2.35x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 43.62 | 72.47 | -0.30% | 1.52x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 9.24511 | 72.29 | -0.19% | 1.43x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 6 | XMR/USD | 524.74 | 68.10 | +0.15% | 1.41x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 7 | INJ/USD | 6.238 | 67.15 | +0.11% | 0.29x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 8 | NEAR/USD | 3.0661 | 63.82 | +0.29% | 1.51x | STRONG 77/100 | HIGH 55/100 | Watch |
| 9 | XRP/USD | 0.95345 | 61.49 | +0.01% | 0.39x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | SYRUP/USD | 0.07081 | 60.45 | +0.01% | 0.51x | WEAK 40/100 | EXTREME 87/100 | Do nothing |
| 11 | ETH/USD | 1701.94 | 58.93 | -0.06% | 0.95x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | ADA/USD | 0.148673 | 58.74 | -0.34% | 0.33x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 4.0182 | 81.97 | +1.82% | 1.06x | 3309 | MODERATE 61/100 | VERY_HIGH 84/100 | Watch |
| 2 | ME/USD | 0.0401 | 74.29 | +0.76% | 1.24x | 2720 | MODERATE 62/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
