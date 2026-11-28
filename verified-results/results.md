# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T04:38:12.571531+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46108185695
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e75d0b4ea28b02ad6821d74a3c47e67885f3dd58 (atomic ledger/results publication)
**Ledger generation:** 2106 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.29 | 76.720 | 62.264 | +1.26% | -0.11% | 5.40x | 3.1 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 419 | 67.377 | 72.178 | +2.88% | -0.18% | 0.61x | 6.0 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SENT/USD | 0.024495 | 62.543 | 49.880 | +3.29% | -0.47% | 3.30x | 8.2 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ZEC/USD | 748.99 | 57.316 | 66.739 | +1.96% | -0.43% | 0.27x | 4.0 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | VVV/USD | 26.294 | 56.800 | 58.706 | +2.12% | +0.52% | 0.55x | 4.9 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0405 | 55.165 | 57.711 | +0.74% | -0.43% | 0.96x | 4.9 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | SEI/USD | 0.03863 | 41.860 | 30.336 | +0.57% | -0.70% | 35.66x | 13.0 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | BCH/USD | 209.33 | 33.420 | 42.264 | +1.13% | -0.19% | 0.21x | 4.3 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2731 | 8.595 | 19.080 | +0.26% | -0.22% | 0.06x | 29.3 | 2026-11-28T04:38:06.239132+00:00 | Not calibrated | WEAK 0/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 72.178 | 419 | -0.18% | 0.61x |
| 2 | ZEC/USD | 66.739 | 748.99 | -0.43% | 0.27x |
| 3 | HYPE/USD | 62.264 | 64.29 | -0.11% | 5.40x |
| 4 | VVV/USD | 58.706 | 26.294 | +0.52% | 0.55x |
| 5 | NEAR/USD | 57.711 | 3.0405 | -0.43% | 0.96x |
| 6 | SENT/USD | 49.880 | 0.024495 | -0.47% | 3.30x |
| 7 | BCH/USD | 42.264 | 209.33 | -0.19% | 0.21x |
| 8 | SEI/USD | 30.336 | 0.03863 | -0.70% | 35.66x |
| 9 | SPX/USD | 19.080 | 0.2731 | -0.22% | 0.06x |

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

- Persisted scans: 2106; predictions: 18913; observations: 1275282.
- Matured sampled outcomes across 1/6/24/48h: 43908; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46108185695 · **Generation:** 2106 · **Legacy run:** 46108185695
**Main quote time:** 2026-11-28T04:38:12.571531+00:00 · **Legacy report time:** 2026-11-28T04:39:10.334581+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 64.29 | 76.72 | -0.11% | 5.40x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 419 | 67.38 | -0.18% | 0.61x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 3 | SENT/USD | 0.024495 | 62.54 | -0.47% | 3.30x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 4 | ZEC/USD | 748.99 | 57.32 | -0.43% | 0.27x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | VVV/USD | 26.294 | 56.80 | +0.52% | 0.55x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | NEAR/USD | 3.0405 | 55.17 | -0.43% | 0.96x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 7 | SEI/USD | 0.03863 | 41.86 | -0.70% | 35.66x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 8 | BCH/USD | 209.33 | 33.42 | -0.19% | 0.21x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | SPX/USD | 0.2731 | 8.60 | -0.22% | 0.06x | WEAK 0/100 | EXTREME 93/100 | Do nothing |

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
