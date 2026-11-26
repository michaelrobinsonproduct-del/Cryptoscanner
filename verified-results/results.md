# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T17:41:40.538606+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45869585286
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fab8942443744711a50ab4e951db2a8930bf3a06 (atomic ledger/results publication)
**Ledger generation:** 1892 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.19162 | 79.522 | 65.062 | +1.63% | -0.11% | 6.01x | 2.6 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04568 | 79.260 | 75.454 | +9.07% | -1.30% | 2.03x | 8.8 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 3 | STBL/USD | 0.020192 | 76.824 | 65.580 | +6.92% | -0.05% | 2.15x | 20.8 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | HBAR/USD | 0.05394 | 74.985 | 59.614 | +3.53% | +0.07% | 6.24x | 1.9 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 5 | ADA/USD | 0.148927 | 74.847 | 68.179 | +2.17% | +0.09% | 1.62x | 4.0 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 6 | WIF/USD | 0.1371 | 67.859 | 65.551 | +7.70% | +0.74% | 0.86x | 21.9 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | 2Z/USD | 0.01751 | 66.441 | 65.076 | +5.99% | -0.06% | 1.17x | 17.1 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | LTC/USD | 43.23 | 66.032 | 62.366 | +1.22% | -0.39% | 1.56x | 2.3 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | FET/USD | 0.116 | 65.001 | 69.752 | +6.91% | +0.09% | 0.48x | 17.3 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | QNT/USD | 149.1 | 63.905 | 62.438 | +2.97% | -0.20% | 1.25x | 4.7 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0717 | 63.790 | 59.678 | +0.71% | +0.15% | 1.33x | 0.7 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XRP/USD | 0.94829 | 63.026 | 63.715 | +1.25% | -0.21% | 1.03x | 0.1 | 2026-11-26T17:41:32.409340+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.454 | 0.04568 | -1.30% | 2.03x |
| 2 | FET/USD | 69.752 | 0.116 | +0.09% | 0.48x |
| 3 | ADA/USD | 68.179 | 0.148927 | +0.09% | 1.62x |
| 4 | STBL/USD | 65.580 | 0.020192 | -0.05% | 2.15x |
| 5 | WIF/USD | 65.551 | 0.1371 | +0.74% | 0.86x |
| 6 | 2Z/USD | 65.076 | 0.01751 | -0.06% | 1.17x |
| 7 | LINK/USD | 65.062 | 9.19162 | -0.11% | 6.01x |
| 8 | XRP/USD | 63.715 | 0.94829 | -0.21% | 1.03x |
| 9 | QNT/USD | 62.438 | 149.1 | -0.20% | 1.25x |
| 10 | LTC/USD | 62.366 | 43.23 | -0.39% | 1.56x |
| 11 | NEAR/USD | 59.678 | 3.0717 | +0.15% | 1.33x |
| 12 | HBAR/USD | 59.614 | 0.05394 | +0.07% | 6.24x |

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

- Persisted scans: 1892; predictions: 16439; observations: 1146273.
- Matured sampled outcomes across 1/6/24/48h: 35539; gap abstentions: 25105. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45869585286 · **Generation:** 1892 · **Legacy run:** 45869585286
**Main quote time:** 2026-11-26T17:41:40.538606+00:00 · **Legacy report time:** 2026-11-26T17:42:31.450917+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.19162 | 79.52 | -0.11% | 6.01x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | SKY/USD | 0.04568 | 79.26 | -1.30% | 2.03x | STRONG 70/100 | VERY_HIGH 70/100 | Do nothing |
| 3 | STBL/USD | 0.020192 | 76.82 | -0.05% | 2.15x | MODERATE 58/100 | EXTREME 85/100 | Do nothing |
| 4 | HBAR/USD ⭐ | 0.05394 | 74.98 | +0.07% | 6.24x | STRONG 92/100 | HIGH 60/100 | Watch |
| 5 | ADA/USD ⭐ | 0.148927 | 74.85 | +0.09% | 1.62x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | WIF/USD | 0.1371 | 67.86 | +0.74% | 0.86x | MODERATE 54/100 | EXTREME 86/100 | Do nothing |
| 7 | 2Z/USD | 0.01751 | 66.44 | -0.06% | 1.17x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |
| 8 | LTC/USD | 43.23 | 66.03 | -0.39% | 1.56x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | FET/USD | 0.116 | 65.00 | +0.09% | 0.48x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 10 | QNT/USD | 149.1 | 63.90 | -0.20% | 1.25x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | NEAR/USD | 3.0717 | 63.79 | +0.15% | 1.33x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 12 | XRP/USD | 0.94829 | 63.03 | -0.21% | 1.03x | WEAK 42/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05391 | 82.97 | +0.07% | 6.24x | 5320 | STRONG 96/100 | HIGH 60/100 | Watch |
| 2 | DRV/USD | 0.37284 | 74.93 | +0.13% | 1.24x | 7519 | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 3 | ADA/USD ⭐ | 0.148927 | 72.27 | +0.09% | 1.62x | 10624 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HBAR/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
