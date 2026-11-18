# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T07:10:18.291209+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44256694229
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** f998731b6465bba0cece3731298c29d3c0697ff0 (atomic ledger/results publication)
**Ledger generation:** 563 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.9212 | 79.700 | 65.272 | +6.11% | -0.11% | 58.39x | 27.1 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | XRP/USD | 0.98967 | 77.550 | 59.683 | +0.73% | +0.57% | 3.36x | 0.8 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.019455 | 57.461 | 56.293 | +4.21% | +0.96% | 0.64x | 8.2 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | TRX/USD | 0.309162 | 53.294 | 43.015 | +0.41% | +0.09% | 1.98x | 0.7 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | MODERATE 62/100 | HIGH 55/100 | Watch | WATCH |
| 5 | MNT/USD | 0.379 | 39.760 | 32.974 | +1.53% | +0.32% | 1.52x | 21.1 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01033141 | 39.010 | 44.939 | +3.48% | +0.30% | 0.25x | 27.9 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | WEAK 40/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | XDC/USD | 0.03087 | 36.716 | 44.695 | +1.81% | -0.13% | 0.27x | 13.0 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5176 | 35.410 | 38.982 | +1.63% | +0.50% | 0.39x | 9.7 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | TRUST/USD | 0.04772 | 34.037 | 38.610 | +1.21% | +0.42% | 0.33x | 6.3 | 2026-11-18T07:10:09.452834+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 65.272 | 1.9212 | -0.11% | 58.39x |
| 2 | XRP/USD | 59.683 | 0.98967 | +0.57% | 3.36x |
| 3 | SENT/USD | 56.293 | 0.019455 | +0.96% | 0.64x |
| 4 | AKE/USD | 44.939 | 0.01033141 | +0.30% | 0.25x |
| 5 | XDC/USD | 44.695 | 0.03087 | -0.13% | 0.27x |
| 6 | TRX/USD | 43.015 | 0.309162 | +0.09% | 1.98x |
| 7 | AKT/USD | 38.982 | 0.5176 | +0.50% | 0.39x |
| 8 | TRUST/USD | 38.610 | 0.04772 | +0.42% | 0.33x |
| 9 | MNT/USD | 32.974 | 0.379 | +0.32% | 1.52x |

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

- Persisted scans: 563; predictions: 4747; observations: 339874.
- Matured sampled outcomes across 1/6/24/48h: 4079; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44256694229 · **Generation:** 563 · **Legacy run:** 44256694229
**Main quote time:** 2026-11-18T07:10:18.291209+00:00 · **Legacy report time:** 2026-11-18T07:10:37.168579+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.9212 | 79.70 | -0.11% | 58.39x | MODERATE 60/100 | VERY_HIGH 78/100 | Watch |
| 2 | XRP/USD ⭐ | 0.98967 | 77.55 | +0.57% | 3.36x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD | 0.019455 | 57.46 | +0.96% | 0.64x | MODERATE 59/100 | VERY_HIGH 82/100 | Watch |
| 4 | TRX/USD ⭐ | 0.309162 | 53.29 | +0.09% | 1.98x | STRONG 72/100 | HIGH 55/100 | Watch |
| 5 | MNT/USD | 0.379 | 39.76 | +0.32% | 1.52x | MODERATE 55/100 | VERY_HIGH 72/100 | Watch |
| 6 | AKE/USD | 0.01033141 | 39.01 | +0.30% | 0.25x | WEAK 40/100 | EXTREME 87/100 | Do nothing |
| 7 | XDC/USD | 0.03087 | 36.72 | -0.13% | 0.27x | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | AKT/USD | 0.5176 | 35.41 | +0.50% | 0.39x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 9 | TRUST/USD | 0.04772 | 34.04 | +0.42% | 0.33x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.98964 | 70.20 | +0.57% | 3.36x | 32122 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TRX/USD ⭐ | 0.309162 | 52.35 | +0.09% | 1.98x | 4119 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
