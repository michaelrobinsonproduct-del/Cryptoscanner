# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T07:27:47.387409+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46121075041
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2454c80214e31f63bcf5aa3cc15e20095a56907d (atomic ledger/results publication)
**Ledger generation:** 2123 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0367 | 74.491 | 57.809 | +0.61% | +0.34% | 20.17x | 3.0 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SPACE/USD | 0.004352 | 71.877 | 47.191 | +4.16% | +1.94% | 7.07x | 25.4 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | ZEC/USD | 737.27 | 70.139 | 55.605 | +0.37% | -0.09% | 3.39x | 3.9 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XMR/USD | 423.48 | 68.819 | 75.295 | +3.98% | -0.63% | 0.67x | 15.1 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | VVV/USD | 26.329 | 64.401 | 56.241 | +2.25% | +0.83% | 1.40x | 8.4 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.81 | 53.843 | 57.744 | +0.50% | +0.30% | 0.46x | 1.6 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03877 | 45.373 | 36.495 | +0.94% | +0.52% | 1.63x | 5.2 | 2026-11-28T07:27:42.684125+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 75.295 | 423.48 | -0.63% | 0.67x |
| 2 | NEAR/USD | 57.809 | 3.0367 | +0.34% | 20.17x |
| 3 | HYPE/USD | 57.744 | 63.81 | +0.30% | 0.46x |
| 4 | VVV/USD | 56.241 | 26.329 | +0.83% | 1.40x |
| 5 | ZEC/USD | 55.605 | 737.27 | -0.09% | 3.39x |
| 6 | SPACE/USD | 47.191 | 0.004352 | +1.94% | 7.07x |
| 7 | SEI/USD | 36.495 | 0.03877 | +0.52% | 1.63x |

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

- Persisted scans: 2123; predictions: 19021; observations: 1285584.
- Matured sampled outcomes across 1/6/24/48h: 44639; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46121075041 · **Generation:** 2123 · **Legacy run:** 46121075041
**Main quote time:** 2026-11-28T07:27:47.387409+00:00 · **Legacy report time:** 2026-11-28T07:28:36.899087+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0367 | 74.49 | +0.34% | 20.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SPACE/USD ⭐ | 0.004352 | 71.88 | +1.94% | 7.07x | STRONG 91/100 | VERY_HIGH 79/100 | Watch |
| 3 | ZEC/USD | 737.27 | 70.14 | -0.09% | 3.39x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD | 423.48 | 68.82 | -0.63% | 0.67x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | VVV/USD ⭐ | 26.329 | 64.40 | +0.83% | 1.40x | STRONG 87/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 63.81 | 53.84 | +0.30% | 0.46x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | SEI/USD ⭐ | 0.03877 | 45.37 | +0.52% | 1.63x | STRONG 78/100 | HIGH 60/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004329 | 74.89 | +1.94% | 7.07x | 2073 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.0374 | 64.03 | +0.34% | 20.17x | 13976 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 26.26 | 58.69 | +0.83% | 1.40x | 7632 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | SEI/USD ⭐ | 0.03878 | 39.14 | +0.52% | 1.63x | 3873 | STRONG 70/100 | HIGH 66/100 | Watch |

**Same-run overlap:** NEAR/USD, SPACE/USD, VVV/USD, SEI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
