# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:05:12.851656+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44320303470
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e80b9f675102bb733e02ad9e400e2e1f69deb115 (atomic ledger/results publication)
**Ledger generation:** 584 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05481 | 70.956 | 64.080 | +6.14% | +1.01% | 1.18x | 20.1 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 86/100 | Do nothing | WATCH |
| 2 | NIGHT/USD | 0.04692 | 70.477 | 71.704 | +4.52% | +0.41% | 0.67x | 17.0 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019316 | 68.381 | 52.204 | +3.47% | +0.41% | 2.41x | 6.2 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | STRONG 89/100 | HIGH 67/100 | Watch | WATCH |
| 4 | TRX/USD | 0.309636 | 60.175 | 45.131 | +0.56% | +0.01% | 3.03x | 1.0 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | CAP/USD | 0.102291 | 54.206 | 37.391 | +1.30% | +0.36% | 3.31x | 6.1 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | STRONG 82/100 | HIGH 67/100 | Watch | WATCH |
| 6 | XRP/USD | 0.98792 | 51.558 | 58.385 | +0.55% | +0.05% | 0.29x | 0.9 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | VVV/USD | 21.189 | 47.693 | 52.544 | +0.78% | -0.29% | 0.66x | 2.4 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5203 | 37.111 | 43.756 | +2.16% | -0.38% | 0.53x | 7.7 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | PEARL/USD | 1.8351 | 35.756 | 37.704 | +1.36% | +0.74% | 0.43x | 20.2 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | CC/USD | 0.08307 | 35.643 | 42.245 | +1.14% | -0.18% | 0.43x | 2.4 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | W/USD | 0.00902 | 34.883 | 33.207 | +1.01% | -0.44% | 1.39x | 11.1 | 2026-11-18T14:05:06.224843+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 71.704 | 0.04692 | +0.41% | 0.67x |
| 2 | MEGA/USD | 64.080 | 0.05481 | +1.01% | 1.18x |
| 3 | XRP/USD | 58.385 | 0.98792 | +0.05% | 0.29x |
| 4 | VVV/USD | 52.544 | 21.189 | -0.29% | 0.66x |
| 5 | SENT/USD | 52.204 | 0.019316 | +0.41% | 2.41x |
| 6 | TRX/USD | 45.131 | 0.309636 | +0.01% | 3.03x |
| 7 | AKT/USD | 43.756 | 0.5203 | -0.38% | 0.53x |
| 8 | CC/USD | 42.245 | 0.08307 | -0.18% | 0.43x |
| 9 | PEARL/USD | 37.704 | 1.8351 | +0.74% | 0.43x |
| 10 | CAP/USD | 37.391 | 0.102291 | +0.36% | 3.31x |
| 11 | W/USD | 33.207 | 0.00902 | -0.44% | 1.39x |

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

- Persisted scans: 584; predictions: 4962; observations: 352663.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13099. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44320303470 · **Generation:** 584 · **Legacy run:** 44320303470
**Main quote time:** 2026-11-18T14:05:12.851656+00:00 · **Legacy report time:** 2026-11-18T14:05:37.281706+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05481 | 70.96 | +1.01% | 1.18x | STRONG 70/100 | EXTREME 86/100 | Do nothing |
| 2 | NIGHT/USD | 0.04692 | 70.48 | +0.41% | 0.67x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 3 | SENT/USD ⭐ | 0.019316 | 68.38 | +0.41% | 2.41x | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 4 | TRX/USD | 0.309636 | 60.17 | +0.01% | 3.03x | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | CAP/USD | 0.102291 | 54.21 | +0.36% | 3.31x | STRONG 82/100 | HIGH 67/100 | Watch |
| 6 | XRP/USD | 0.98792 | 51.56 | +0.05% | 0.29x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 7 | VVV/USD | 21.189 | 47.69 | -0.29% | 0.66x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKT/USD | 0.5203 | 37.11 | -0.38% | 0.53x | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | PEARL/USD | 1.8351 | 35.76 | +0.74% | 0.43x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |
| 10 | CC/USD | 0.08307 | 35.64 | -0.18% | 0.43x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | W/USD | 0.00902 | 34.88 | -0.44% | 1.39x | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019316 | 73.65 | +0.41% | 2.41x | 5675 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05488 | 62.84 | +1.01% | 1.18x | 1247 | STRONG 71/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** MEGA/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
