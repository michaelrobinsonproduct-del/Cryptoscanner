# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T16:12:12.041422+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45433837930
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0bfeee164f7476fa11be4077157c35f5e6fb186b (atomic ledger/results publication)
**Ledger generation:** 1596 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.586e-05 | 64.077 | 53.507 | +5.50% | -0.89% | 5.18x | 32.7 | 2026-11-24T16:12:09.893098+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 85/100 | Do nothing | WATCH |
| 2 | XMR/USD | 491.2 | 59.539 | 56.148 | +1.07% | +0.01% | 1.33x | 12.6 | 2026-11-24T16:12:09.893098+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31084 | 56.203 | 58.810 | +0.58% | -0.00% | 0.74x | 0.5 | 2026-11-24T16:12:09.893098+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | VVV/USD | 24.562 | 49.061 | 53.578 | +0.47% | +0.59% | 0.25x | 9.4 | 2026-11-24T16:12:09.893098+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.01598 | 40.615 | 42.365 | +2.11% | -0.50% | 1.08x | 6.3 | 2026-11-24T16:12:09.893098+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | GBP/USD | 58.810 | 1.31084 | -0.00% | 0.74x |
| 2 | XMR/USD | 56.148 | 491.2 | +0.01% | 1.33x |
| 3 | VVV/USD | 53.578 | 24.562 | +0.59% | 0.25x |
| 4 | LUNA/USD | 53.507 | 4.586e-05 | -0.89% | 5.18x |
| 5 | 2Z/USD | 42.365 | 0.01598 | -0.50% | 1.08x |

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

- Persisted scans: 1596; predictions: 13731; observations: 967056.
- Matured sampled outcomes across 1/6/24/48h: 27334; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45433837930 · **Generation:** 1596 · **Legacy run:** 45433837930
**Main quote time:** 2026-11-24T16:12:12.041422+00:00 · **Legacy report time:** 2026-11-24T16:13:03.412913+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.586e-05 | 64.08 | -0.89% | 5.18x | MODERATE 52/100 | EXTREME 85/100 | Do nothing |
| 2 | XMR/USD | 491.2 | 59.54 | +0.01% | 1.33x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 3 | GBP/USD | 1.31084 | 56.20 | -0.00% | 0.74x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | VVV/USD | 24.562 | 49.06 | +0.59% | 0.25x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 5 | 2Z/USD | 0.01598 | 40.62 | -0.50% | 1.08x | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing |

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
