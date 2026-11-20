# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:20:34.470618+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44686994045
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** cf46c36eaa9ef83ae5e20385a578609a046139f2 (atomic ledger/results publication)
**Ledger generation:** 940 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PROS/USD | 0.5924 | 66.637 | 64.907 | +9.97% | +1.23% | 0.56x | 22.0 | 2026-11-20T06:20:29.572823+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 94/100 | Do nothing | WATCH |
| 2 | XRP/USD | 0.96528 | 62.581 | 58.830 | +0.63% | -0.23% | 1.49x | 1.1 | 2026-11-20T06:20:29.572823+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.133213 | 50.977 | 55.491 | +0.39% | -0.30% | 0.70x | 4.4 | 2026-11-20T06:20:29.572823+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | AUD/USD | 0.66743 | 32.495 | 41.115 | +0.29% | +0.08% | 0.10x | 0.1 | 2026-11-20T06:20:29.572823+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010225 | 31.408 | 35.823 | +1.78% | -0.17% | 0.64x | 15.7 | 2026-11-20T06:20:29.572823+00:00 | Not calibrated | WEAK 16/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.4318 | 25.154 | 37.973 | +1.34% | -2.00% | 0.72x | 18.5 | 2026-11-20T06:20:29.572823+00:00 | Not calibrated | WEAK 13/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 64.907 | 0.5924 | +1.23% | 0.56x |
| 2 | XRP/USD | 58.830 | 0.96528 | -0.23% | 1.49x |
| 3 | XLM/USD | 55.491 | 0.133213 | -0.30% | 0.70x |
| 4 | AUD/USD | 41.115 | 0.66743 | +0.08% | 0.10x |
| 5 | ICNT/USD | 37.973 | 0.4318 | -2.00% | 0.72x |
| 6 | SKR/USD | 35.823 | 0.010225 | -0.17% | 0.64x |

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

- Persisted scans: 940; predictions: 7981; observations: 567971.
- Matured sampled outcomes across 1/6/24/48h: 9360; gap abstentions: 17184. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44686994045 · **Generation:** 940 · **Legacy run:** 44686994045
**Main quote time:** 2026-11-20T06:20:34.470618+00:00 · **Legacy report time:** 2026-11-20T06:21:40.026802+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD | 0.5924 | 66.64 | +1.23% | 0.56x | MODERATE 53/100 | EXTREME 94/100 | Do nothing |
| 2 | XRP/USD | 0.96528 | 62.58 | -0.23% | 1.49x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD | 0.133213 | 50.98 | -0.30% | 0.70x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | AUD/USD | 0.66743 | 32.49 | +0.08% | 0.10x | WEAK 36/100 | VERY_HIGH 70/100 | Watch |
| 5 | SKR/USD | 0.010225 | 31.41 | -0.17% | 0.64x | WEAK 16/100 | EXTREME 94/100 | Do nothing |
| 6 | ICNT/USD | 0.4318 | 25.15 | -2.00% | 0.72x | WEAK 13/100 | EXTREME 86/100 | Do nothing |

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
