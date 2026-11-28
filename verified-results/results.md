# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T03:27:21.121475+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46102706264
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 271b41f4dc656d9bf2d058a870d02d20a3e09a10 (atomic ledger/results publication)
**Ledger generation:** 2099 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 748.26 | 67.782 | 66.104 | +1.86% | -0.42% | 1.38x | 3.9 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 414.11 | 66.508 | 62.410 | +1.68% | +0.16% | 1.33x | 8.7 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 3 | CC/USD | 0.07583 | 61.128 | 47.116 | +2.27% | +0.32% | 2.24x | 6.6 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Watch | WATCH |
| 4 | HYPE/USD | 64.19 | 53.921 | 61.938 | +1.10% | -0.36% | 0.38x | 1.6 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | VVV/USD | 26.119 | 52.837 | 52.266 | +1.44% | -0.19% | 1.15x | 8.8 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0409 | 50.492 | 58.456 | +0.75% | -0.20% | 0.30x | 3.6 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | BCH/USD | 208.99 | 45.297 | 41.716 | +0.96% | -0.02% | 1.37x | 4.3 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SENT/USD | 0.024188 | 41.307 | 44.674 | +2.00% | +0.45% | 0.44x | 0.4 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | SHX/USD | 0.003357 | 31.105 | 25.105 | +0.27% | -0.65% | 1.93x | 14.9 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | SPX/USD | 0.2731 | 29.560 | 20.887 | +0.26% | -0.11% | 1.92x | 25.7 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 11 | XCN/USD | 0.00302 | 6.160 | 19.338 | +0.33% | -0.66% | 0.01x | 33.2 | 2026-11-28T03:27:15.930594+00:00 | Not calibrated | WEAK 0/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 66.104 | 748.26 | -0.42% | 1.38x |
| 2 | XMR/USD | 62.410 | 414.11 | +0.16% | 1.33x |
| 3 | HYPE/USD | 61.938 | 64.19 | -0.36% | 0.38x |
| 4 | NEAR/USD | 58.456 | 3.0409 | -0.20% | 0.30x |
| 5 | VVV/USD | 52.266 | 26.119 | -0.19% | 1.15x |
| 6 | CC/USD | 47.116 | 0.07583 | +0.32% | 2.24x |
| 7 | SENT/USD | 44.674 | 0.024188 | +0.45% | 0.44x |
| 8 | BCH/USD | 41.716 | 208.99 | -0.02% | 1.37x |
| 9 | SHX/USD | 25.105 | 0.003357 | -0.65% | 1.93x |
| 10 | SPX/USD | 20.887 | 0.2731 | -0.11% | 1.92x |
| 11 | XCN/USD | 19.338 | 0.00302 | -0.66% | 0.01x |

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

- Persisted scans: 2099; predictions: 18846; observations: 1271040.
- Matured sampled outcomes across 1/6/24/48h: 43538; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46102706264 · **Generation:** 2099 · **Legacy run:** 46102706264
**Main quote time:** 2026-11-28T03:27:21.121475+00:00 · **Legacy report time:** 2026-11-28T03:28:06.460166+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 748.26 | 67.78 | -0.42% | 1.38x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD ⭐ | 414.11 | 66.51 | +0.16% | 1.33x | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | CC/USD ⭐ | 0.07583 | 61.13 | +0.32% | 2.24x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 4 | HYPE/USD | 64.19 | 53.92 | -0.36% | 0.38x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | VVV/USD | 26.119 | 52.84 | -0.19% | 1.15x | WEAK 36/100 | HIGH 68/100 | Watch |
| 6 | NEAR/USD | 3.0409 | 50.49 | -0.20% | 0.30x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | BCH/USD | 208.99 | 45.30 | -0.02% | 1.37x | WEAK 43/100 | HIGH 61/100 | Watch |
| 8 | SENT/USD | 0.024188 | 41.31 | +0.45% | 0.44x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 9 | SHX/USD | 0.003357 | 31.11 | -0.65% | 1.93x | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | SPX/USD | 0.2731 | 29.56 | -0.11% | 1.92x | WEAK 25/100 | VERY_HIGH 78/100 | Do nothing |
| 11 | XCN/USD | 0.00302 | 6.16 | -0.66% | 0.01x | WEAK 0/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07585 | 59.98 | +0.32% | 2.24x | 5238 | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 412.9 | 55.39 | +0.16% | 1.33x | 14692 | MODERATE 68/100 | HIGH 61/100 | Watch |

**Same-run overlap:** XMR/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
