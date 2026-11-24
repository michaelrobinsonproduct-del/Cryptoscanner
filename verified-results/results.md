# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:50:44.410466+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45452536897
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d0bbf3c58a61cfcee56e793f47d2dd942514fa81 (atomic ledger/results publication)
**Ledger generation:** 1606 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 502.27 | 91.392 | 74.513 | +3.34% | +0.38% | 5.98x | 7.8 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LUNA/USD | 4.865e-05 | 87.248 | 58.194 | +11.92% | +2.81% | 19.40x | 37.2 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | VVV/USD | 25.375 | 77.641 | 73.843 | +3.79% | +0.12% | 1.32x | 15.4 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01632 | 77.024 | 57.698 | +4.28% | +0.87% | 3.97x | 6.1 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | STRONG 94/100 | HIGH 67/100 | Consider small entry | WATCH |
| 5 | GBP/USD | 1.3118 | 74.139 | 59.059 | +0.66% | +0.02% | 2.67x | 1.1 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66433 | 43.614 | 43.744 | +0.26% | +0.00% | 0.98x | 2.1 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | WEAK 42/100 | HIGH 62/100 | Watch | WATCH |
| 7 | BAT/USD | 0.07778 | 29.892 | 32.954 | +0.79% | +0.09% | 0.65x | 10.3 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | DBR/USD | 0.01363 | 19.241 | 27.819 | +1.56% | -0.44% | 0.36x | 29.3 | 2026-11-24T17:50:40.773740+00:00 | Not calibrated | WEAK 5/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.513 | 502.27 | +0.38% | 5.98x |
| 2 | VVV/USD | 73.843 | 25.375 | +0.12% | 1.32x |
| 3 | GBP/USD | 59.059 | 1.3118 | +0.02% | 2.67x |
| 4 | LUNA/USD | 58.194 | 4.865e-05 | +2.81% | 19.40x |
| 5 | 2Z/USD | 57.698 | 0.01632 | +0.87% | 3.97x |
| 6 | AUD/USD | 43.744 | 0.66433 | +0.00% | 0.98x |
| 7 | BAT/USD | 32.954 | 0.07778 | +0.09% | 0.65x |
| 8 | DBR/USD | 27.819 | 0.01363 | -0.44% | 0.36x |

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

- Persisted scans: 1606; predictions: 13797; observations: 973146.
- Matured sampled outcomes across 1/6/24/48h: 27745; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45452536897 · **Generation:** 1606 · **Legacy run:** 45452536897
**Main quote time:** 2026-11-24T17:50:44.410466+00:00 · **Legacy report time:** 2026-11-24T17:51:56.194742+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 502.27 | 91.39 | +0.38% | 5.98x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LUNA/USD | 4.865e-05 | 87.25 | +2.81% | 19.40x | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 3 | VVV/USD ⭐ | 25.375 | 77.64 | +0.12% | 1.32x | STRONG 79/100 | HIGH 61/100 | Watch |
| 4 | 2Z/USD ⭐ | 0.01632 | 77.02 | +0.87% | 3.97x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 5 | GBP/USD | 1.3118 | 74.14 | +0.02% | 2.67x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | AUD/USD | 0.66433 | 43.61 | +0.00% | 0.98x | WEAK 42/100 | HIGH 62/100 | Watch |
| 7 | BAT/USD | 0.07778 | 29.89 | +0.09% | 0.65x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | DBR/USD | 0.01363 | 19.24 | -0.44% | 0.36x | WEAK 5/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.89 | 94.33 | +0.38% | 5.98x | 8972 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.339 | 83.15 | +0.12% | 1.32x | 17084 | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | 2Z/USD ⭐ | 0.01632 | 70.98 | +0.87% | 3.97x | 1429 | STRONG 95/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** XMR/USD, VVV/USD, 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
