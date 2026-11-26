# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T01:16:10.502071+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45734397051
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d672f3837afb339ca70f3409c572ac348f1877f0 (atomic ledger/results publication)
**Ledger generation:** 1792 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 30.066 | 71.921 | 67.903 | +2.98% | -0.07% | 1.44x | 16.0 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0986 | 63.167 | 64.079 | +1.60% | +0.78% | 0.52x | 4.2 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6735 | 55.741 | 61.080 | +1.08% | +0.45% | 0.24x | 3.0 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LTC/USD | 43.12 | 54.715 | 60.560 | +0.96% | +0.30% | 0.26x | 2.3 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002626 | 54.415 | 56.490 | +1.90% | +0.61% | 0.49x | 3.8 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94325 | 54.094 | 59.841 | +0.71% | +0.44% | 0.21x | 0.3 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 70.98 | 54.023 | 59.458 | +0.84% | +0.37% | 0.27x | 2.8 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 60704.6 | 53.933 | 58.888 | +0.56% | +0.44% | 0.28x | 0.0 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1702.38 | 53.833 | 59.927 | +0.71% | +0.47% | 0.16x | 0.1 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ADA/USD | 0.147074 | 52.631 | 59.732 | +0.89% | +0.37% | 0.11x | 3.1 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0565403 | 51.366 | 57.060 | +1.04% | +0.37% | 0.25x | 0.5 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TAO/USD | 183.0773 | 48.217 | 57.138 | +0.82% | -0.31% | 0.26x | 7.2 | 2026-11-26T01:16:02.299496+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 67.903 | 30.066 | -0.07% | 1.44x |
| 2 | NEAR/USD | 64.079 | 3.0986 | +0.78% | 0.52x |
| 3 | SUI/USD | 61.080 | 0.6735 | +0.45% | 0.24x |
| 4 | LTC/USD | 60.560 | 43.12 | +0.30% | 0.26x |
| 5 | ETH/USD | 59.927 | 1702.38 | +0.47% | 0.16x |
| 6 | XRP/USD | 59.841 | 0.94325 | +0.44% | 0.21x |
| 7 | ADA/USD | 59.732 | 0.147074 | +0.37% | 0.11x |
| 8 | SOL/USD | 59.458 | 70.98 | +0.37% | 0.27x |
| 9 | XBT/USD | 58.888 | 60704.6 | +0.44% | 0.28x |
| 10 | TAO/USD | 57.138 | 183.0773 | -0.31% | 0.26x |
| 11 | XDG/USD | 57.060 | 0.0565403 | +0.37% | 0.25x |
| 12 | PUMP/USD | 56.490 | 0.002626 | +0.61% | 0.49x |

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

- Persisted scans: 1792; predictions: 15239; observations: 1086372.
- Matured sampled outcomes across 1/6/24/48h: 33128; gap abstentions: 23560. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45734397051 · **Generation:** 1792 · **Legacy run:** 45734397051
**Main quote time:** 2026-11-26T01:16:10.502071+00:00 · **Legacy report time:** 2026-11-26T01:17:06.504646+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 30.066 | 71.92 | -0.07% | 1.44x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD | 3.0986 | 63.17 | +0.78% | 0.52x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 3 | SUI/USD | 0.6735 | 55.74 | +0.45% | 0.24x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | LTC/USD | 43.12 | 54.72 | +0.30% | 0.26x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | PUMP/USD | 0.002626 | 54.42 | +0.61% | 0.49x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.94325 | 54.09 | +0.44% | 0.21x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 70.98 | 54.02 | +0.37% | 0.27x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 60704.6 | 53.93 | +0.44% | 0.28x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1702.38 | 53.83 | +0.47% | 0.16x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | ADA/USD | 0.147074 | 52.63 | +0.37% | 0.11x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0565403 | 51.37 | +0.37% | 0.25x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | TAO/USD | 183.0773 | 48.22 | -0.31% | 0.26x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.07382 | 58.47 | +1.23% | 1.14x | 3430 | MODERATE 54/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
