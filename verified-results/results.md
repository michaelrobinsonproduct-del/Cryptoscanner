# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T15:02:11.432643+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46020843595
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 042ed90eff4010e3baa45fb33a2568161c9cffbf (atomic ledger/results publication)
**Ledger generation:** 2023 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 604; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 720.92 | 98.539 | 91.920 | +5.76% | -1.68% | 8.30x | 6.8 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | STRONG 79/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | HYPE/USD | 63.46 | 76.313 | 67.374 | +1.99% | -1.21% | 17.26x | 3.2 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | LIGHTER/USD | 2.604 | 66.829 | 57.520 | +4.92% | -1.14% | 2.50x | 19.2 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | VVV/USD | 26.532 | 65.854 | 53.496 | +1.33% | -0.53% | 7.10x | 14.7 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 5 | UNI/USD | 4.7012 | 59.818 | 54.049 | +1.10% | -1.85% | 14.44x | 12.8 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 6 | XDG/USD | 0.0565818 | 55.952 | 48.790 | +0.37% | -1.57% | 4.64x | 4.9 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 58/100 | HIGH 65/100 | Do nothing | WATCH |
| 7 | FET/USD | 0.1246 | 55.814 | 48.324 | +3.49% | -1.50% | 23.31x | 24.1 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | PAXG/USD | 3616.86 | 54.509 | 52.193 | +1.69% | -0.00% | 1.23x | 2.4 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | RENDER/USD | 1.351 | 49.920 | 35.289 | +1.35% | -0.07% | 27.07x | 14.8 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | INJ/USD | 6.219 | 48.458 | 40.827 | +0.44% | -1.47% | 13.47x | 8.0 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 54/100 | HIGH 65/100 | Do nothing | WATCH |
| 11 | TON/USD | 0.976 | 43.170 | 31.720 | +1.35% | -0.71% | 3.24x | 20.5 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 12 | VIRTUAL/USD | 0.3673 | 39.168 | 32.561 | +0.80% | -1.68% | 13.84x | 10.9 | 2026-11-27T15:02:03.986949+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 91.920 | 720.92 | -1.68% | 8.30x |
| 2 | HYPE/USD | 67.374 | 63.46 | -1.21% | 17.26x |
| 3 | LIGHTER/USD | 57.520 | 2.604 | -1.14% | 2.50x |
| 4 | UNI/USD | 54.049 | 4.7012 | -1.85% | 14.44x |
| 5 | VVV/USD | 53.496 | 26.532 | -0.53% | 7.10x |
| 6 | PAXG/USD | 52.193 | 3616.86 | -0.00% | 1.23x |
| 7 | XDG/USD | 48.790 | 0.0565818 | -1.57% | 4.64x |
| 8 | FET/USD | 48.324 | 0.1246 | -1.50% | 23.31x |
| 9 | INJ/USD | 40.827 | 6.219 | -1.47% | 13.47x |
| 10 | RENDER/USD | 35.289 | 1.351 | -0.07% | 27.07x |
| 11 | VIRTUAL/USD | 32.561 | 0.3673 | -1.68% | 13.84x |
| 12 | TON/USD | 31.720 | 0.976 | -0.71% | 3.24x |

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

- Persisted scans: 2023; predictions: 17978; observations: 1225024.
- Matured sampled outcomes across 1/6/24/48h: 40157; gap abstentions: 25913. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46020843595 · **Generation:** 2023 · **Legacy run:** 46020843595
**Main quote time:** 2026-11-27T15:02:11.432643+00:00 · **Legacy report time:** 2026-11-27T15:02:54.882482+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 720.92 | 98.54 | -1.68% | 8.30x | STRONG 79/100 | HIGH 65/100 | Do nothing |
| 2 | HYPE/USD | 63.46 | 76.31 | -1.21% | 17.26x | MODERATE 68/100 | HIGH 65/100 | Do nothing |
| 3 | LIGHTER/USD | 2.604 | 66.83 | -1.14% | 2.50x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |
| 4 | VVV/USD | 26.532 | 65.85 | -0.53% | 7.10x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 5 | UNI/USD | 4.7012 | 59.82 | -1.85% | 14.44x | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing |
| 6 | XDG/USD | 0.0565818 | 55.95 | -1.57% | 4.64x | MODERATE 58/100 | HIGH 65/100 | Do nothing |
| 7 | FET/USD | 0.1246 | 55.81 | -1.50% | 23.31x | MODERATE 48/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | PAXG/USD | 3616.86 | 54.51 | -0.00% | 1.23x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | RENDER/USD | 1.351 | 49.92 | -0.07% | 27.07x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 10 | INJ/USD | 6.219 | 48.46 | -1.47% | 13.47x | MODERATE 54/100 | HIGH 65/100 | Do nothing |
| 11 | TON/USD | 0.976 | 43.17 | -0.71% | 3.24x | WEAK 42/100 | VERY_HIGH 78/100 | Watch |
| 12 | VIRTUAL/USD | 0.3673 | 39.17 | -1.68% | 13.84x | MODERATE 45/100 | VERY_HIGH 76/100 | Do nothing |

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
