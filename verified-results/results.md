# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:55:43.468109+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46099935787
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b6411bd46de8836fbfcd2d57f3a95352c6521581 (atomic ledger/results publication)
**Ledger generation:** 2096 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.36 | 71.702 | 63.815 | +1.37% | +0.05% | 1.77x | 1.6 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0398 | 63.528 | 58.364 | +0.72% | -0.09% | 1.56x | 3.3 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 748.81 | 58.195 | 67.234 | +1.94% | -0.74% | 0.47x | 2.7 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024084 | 55.884 | 41.581 | +1.56% | -0.07% | 2.46x | 0.4 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | XMR/USD | 411.25 | 48.797 | 48.586 | +0.98% | +0.40% | 0.82x | 26.5 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | CC/USD | 0.07526 | 47.443 | 41.609 | +1.50% | +0.44% | 1.36x | 6.7 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 7 | ONDO/USD | 0.28821 | 46.459 | 33.398 | +0.38% | -0.08% | 2.34x | 9.0 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 8 | VVV/USD | 25.985 | 42.530 | 49.130 | +0.92% | -0.45% | 0.57x | 8.1 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | BCH/USD | 209.32 | 39.521 | 42.384 | +1.12% | +0.02% | 0.70x | 5.7 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | BIGTIME/USD | 0.005731 | 14.880 | 27.499 | +0.99% | -1.96% | 0.72x | 21.0 | 2026-11-28T02:55:35.398337+00:00 | Not calibrated | WEAK 2/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 67.234 | 748.81 | -0.74% | 0.47x |
| 2 | HYPE/USD | 63.815 | 64.36 | +0.05% | 1.77x |
| 3 | NEAR/USD | 58.364 | 3.0398 | -0.09% | 1.56x |
| 4 | VVV/USD | 49.130 | 25.985 | -0.45% | 0.57x |
| 5 | XMR/USD | 48.586 | 411.25 | +0.40% | 0.82x |
| 6 | BCH/USD | 42.384 | 209.32 | +0.02% | 0.70x |
| 7 | CC/USD | 41.609 | 0.07526 | +0.44% | 1.36x |
| 8 | SENT/USD | 41.581 | 0.024084 | -0.07% | 2.46x |
| 9 | ONDO/USD | 33.398 | 0.28821 | -0.08% | 2.34x |
| 10 | BIGTIME/USD | 27.499 | 0.005731 | -1.96% | 0.72x |

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

- Persisted scans: 2096; predictions: 18811; observations: 1269222.
- Matured sampled outcomes across 1/6/24/48h: 43358; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46099935787 · **Generation:** 2096 · **Legacy run:** 46099935787
**Main quote time:** 2026-11-28T02:55:43.468109+00:00 · **Legacy report time:** 2026-11-28T02:56:40.697639+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 64.36 | 71.70 | +0.05% | 1.77x | STRONG 71/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 3.0398 | 63.53 | -0.09% | 1.56x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD | 748.81 | 58.20 | -0.74% | 0.47x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | SENT/USD | 0.024084 | 55.88 | -0.07% | 2.46x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |
| 5 | XMR/USD | 411.25 | 48.80 | +0.40% | 0.82x | WEAK 44/100 | VERY_HIGH 74/100 | Watch |
| 6 | CC/USD ⭐ | 0.07526 | 47.44 | +0.44% | 1.36x | STRONG 79/100 | HIGH 60/100 | Watch |
| 7 | ONDO/USD | 0.28821 | 46.46 | -0.08% | 2.34x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 8 | VVV/USD | 25.985 | 42.53 | -0.45% | 0.57x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | BCH/USD | 209.32 | 39.52 | +0.02% | 0.70x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 10 | BIGTIME/USD | 0.005731 | 14.88 | -1.96% | 0.72x | WEAK 2/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AUD/USD | 0.66547 | 52.40 | +0.10% | 6.40x | 4041 | STRONG 71/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD | 71.69 | 52.31 | +0.14% | 1.29x | 43419 | MODERATE 51/100 | HIGH 55/100 | Watch |
| 3 | CC/USD ⭐ | 0.07526 | 47.10 | +0.44% | 1.36x | 5204 | STRONG 79/100 | HIGH 60/100 | Watch |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
