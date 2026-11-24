# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T17:42:03.152782+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45450994814
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 17fad757b38d0ea6abff2b78f446fa5af8b1f9f2 (atomic ledger/results publication)
**Ledger generation:** 1605 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.14 | 88.413 | 70.087 | +3.11% | +0.67% | 3.57x | 13.4 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | STRONG 94/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.358 | 82.599 | 76.314 | +3.72% | +0.74% | 1.26x | 9.5 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31149 | 66.439 | 59.159 | +0.63% | +0.04% | 1.71x | 0.5 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01617 | 51.428 | 50.912 | +3.32% | +0.12% | 0.99x | 6.2 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | BAT/USD | 0.07808 | 46.052 | 25.429 | +1.18% | +1.23% | 2.45x | 30.8 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66436 | 35.153 | 44.213 | +0.27% | +0.06% | 0.06x | 1.2 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | DBR/USD | 0.01364 | 26.267 | 28.331 | +1.64% | -0.58% | 1.09x | 29.4 | 2026-11-24T17:41:59.181364+00:00 | Not calibrated | WEAK 13/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 76.314 | 25.358 | +0.74% | 1.26x |
| 2 | XMR/USD | 70.087 | 501.14 | +0.67% | 3.57x |
| 3 | GBP/USD | 59.159 | 1.31149 | +0.04% | 1.71x |
| 4 | 2Z/USD | 50.912 | 0.01617 | +0.12% | 0.99x |
| 5 | AUD/USD | 44.213 | 0.66436 | +0.06% | 0.06x |
| 6 | DBR/USD | 28.331 | 0.01364 | -0.58% | 1.09x |
| 7 | BAT/USD | 25.429 | 0.07808 | +1.23% | 2.45x |

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

- Persisted scans: 1605; predictions: 13789; observations: 972537.
- Matured sampled outcomes across 1/6/24/48h: 27705; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45450994814 · **Generation:** 1605 · **Legacy run:** 45450994814
**Main quote time:** 2026-11-24T17:42:03.152782+00:00 · **Legacy report time:** 2026-11-24T17:42:51.807818+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.14 | 88.41 | +0.67% | 3.57x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.358 | 82.60 | +0.74% | 1.26x | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | GBP/USD | 1.31149 | 66.44 | +0.04% | 1.71x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 4 | 2Z/USD | 0.01617 | 51.43 | +0.12% | 0.99x | MODERATE 46/100 | VERY_HIGH 74/100 | Watch |
| 5 | BAT/USD ⭐ | 0.07808 | 46.05 | +1.23% | 2.45x | STRONG 78/100 | VERY_HIGH 72/100 | Watch |
| 6 | AUD/USD | 0.66436 | 35.15 | +0.06% | 0.06x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 7 | DBR/USD | 0.01364 | 26.27 | -0.58% | 1.09x | WEAK 13/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.421 | 88.02 | +0.74% | 1.26x | 16526 | STRONG 89/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 501.01 | 84.01 | +0.67% | 3.57x | 8927 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | LUNA/USD | 4.746e-05 | 75.17 | +1.49% | 12.47x | 1645 | STRONG 78/100 | VERY_HIGH 82/100 | Watch |
| 4 | BAT/USD ⭐ | 0.07798 | 45.62 | +1.23% | 2.45x | 4125 | STRONG 83/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** XMR/USD, VVV/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
