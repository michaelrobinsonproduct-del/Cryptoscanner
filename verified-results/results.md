# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T08:36:13.794072+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45784325688
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 805067a35c6703c81881004a2a4db547eab74ba8 (atomic ledger/results publication)
**Ledger generation:** 1837 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.95409 | 83.218 | 68.050 | +1.87% | +0.03% | 4.15x | 0.1 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LINK/USD | 9.16916 | 79.384 | 63.855 | +1.38% | +0.11% | 3.16x | 0.0 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.07336 | 74.872 | 72.573 | +10.70% | +0.66% | 0.90x | 9.6 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 4 | SOL/USD | 70.91 | 74.114 | 59.466 | +0.74% | -0.07% | 3.65x | 1.4 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | INJ/USD | 6.181 | 65.195 | 65.907 | +3.81% | +0.24% | 0.81x | 6.5 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XBT/USD | 60588.1 | 64.691 | 57.537 | +0.36% | -0.04% | 1.74x | 0.0 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AAVE/USD | 96 | 61.629 | 45.532 | +0.67% | +0.22% | 8.35x | 2.1 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0565399 | 58.032 | 57.215 | +1.04% | +0.02% | 1.07x | 0.2 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ADA/USD | 0.147778 | 57.324 | 62.984 | +1.38% | +0.12% | 0.37x | 3.3 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | CC/USD | 0.07918 | 54.511 | 49.074 | +2.23% | +0.57% | 1.26x | 3.8 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 62/100 | HIGH 60/100 | Watch | WATCH |
| 11 | LTC/USD | 43.3 | 54.381 | 62.359 | +1.38% | -0.12% | 0.26x | 4.6 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SKY/USD | 0.04366 | 52.028 | 58.860 | +4.25% | +0.02% | 0.31x | 9.2 | 2026-11-26T08:36:05.593684+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 72.573 | 0.07336 | +0.66% | 0.90x |
| 2 | XRP/USD | 68.050 | 0.95409 | +0.03% | 4.15x |
| 3 | INJ/USD | 65.907 | 6.181 | +0.24% | 0.81x |
| 4 | LINK/USD | 63.855 | 9.16916 | +0.11% | 3.16x |
| 5 | ADA/USD | 62.984 | 0.147778 | +0.12% | 0.37x |
| 6 | LTC/USD | 62.359 | 43.3 | -0.12% | 0.26x |
| 7 | SOL/USD | 59.466 | 70.91 | -0.07% | 3.65x |
| 8 | SKY/USD | 58.860 | 0.04366 | +0.02% | 0.31x |
| 9 | XBT/USD | 57.537 | 60588.1 | -0.04% | 1.74x |
| 10 | XDG/USD | 57.215 | 0.0565399 | +0.02% | 1.07x |
| 11 | CC/USD | 49.074 | 0.07918 | +0.57% | 1.26x |
| 12 | AAVE/USD | 45.532 | 96 | +0.22% | 8.35x |

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

- Persisted scans: 1837; predictions: 15779; observations: 1113775.
- Matured sampled outcomes across 1/6/24/48h: 34190; gap abstentions: 24344. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45784325688 · **Generation:** 1837 · **Legacy run:** 45784325688
**Main quote time:** 2026-11-26T08:36:13.794072+00:00 · **Legacy report time:** 2026-11-26T08:37:08.359610+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.95409 | 83.22 | +0.03% | 4.15x | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 9.16916 | 79.38 | +0.11% | 3.16x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | SYRUP/USD | 0.07336 | 74.87 | +0.66% | 0.90x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 4 | SOL/USD | 70.91 | 74.11 | -0.07% | 3.65x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | INJ/USD | 6.181 | 65.20 | +0.24% | 0.81x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | XBT/USD | 60588.1 | 64.69 | -0.04% | 1.74x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | AAVE/USD | 96 | 61.63 | +0.22% | 8.35x | STRONG 86/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD | 0.0565399 | 58.03 | +0.02% | 1.07x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 9 | ADA/USD | 0.147778 | 57.32 | +0.12% | 0.37x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | CC/USD | 0.07918 | 54.51 | +0.57% | 1.26x | MODERATE 62/100 | HIGH 60/100 | Watch |
| 11 | LTC/USD | 43.3 | 54.38 | -0.12% | 0.26x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SKY/USD | 0.04366 | 52.03 | +0.02% | 0.31x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08014 | 76.41 | +0.39% | 90.03x | 5424 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.17129 | 74.34 | +0.11% | 3.16x | 9167 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
