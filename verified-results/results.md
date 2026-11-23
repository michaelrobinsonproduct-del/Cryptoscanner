# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T01:51:21.219011+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45096730610
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 89bf9a9c06d9178a501b69075e9c0360e194e907 (atomic ledger/results publication)
**Ledger generation:** 1364 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38515 | 64.555 | 70.414 | +4.42% | -0.46% | 0.65x | 11.4 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 2 | PAXG/USD | 3593.01 | 39.385 | 48.363 | +0.58% | -0.25% | 0.23x | 0.1 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | CC/USD | 0.07372 | 36.220 | 36.349 | +0.61% | +0.15% | 0.91x | 6.8 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 38/100 | HIGH 67/100 | Watch | WATCH |
| 4 | PEARL/USD | 2.0937 | 35.623 | 45.693 | +1.91% | -0.77% | 0.38x | 18.2 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | XAUT/USD | 3594.4 | 33.650 | 37.138 | +0.62% | -0.26% | 0.78x | 0.3 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | ALIGN/USD | 0.00354 | 21.946 | 19.058 | +0.28% | +1.43% | 0.57x | 28.2 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | ICNT/USD | 0.3551 | 10.345 | 21.808 | +0.82% | -1.31% | 0.51x | 33.9 | 2026-11-23T01:51:16.405922+00:00 | Not calibrated | WEAK 0/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 70.414 | 0.38515 | -0.46% | 0.65x |
| 2 | PAXG/USD | 48.363 | 3593.01 | -0.25% | 0.23x |
| 3 | PEARL/USD | 45.693 | 2.0937 | -0.77% | 0.38x |
| 4 | XAUT/USD | 37.138 | 3594.4 | -0.26% | 0.78x |
| 5 | CC/USD | 36.349 | 0.07372 | +0.15% | 0.91x |
| 6 | ICNT/USD | 21.808 | 0.3551 | -1.31% | 0.51x |
| 7 | ALIGN/USD | 19.058 | 0.00354 | +1.43% | 0.57x |

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

- Persisted scans: 1364; predictions: 11196; observations: 825782.
- Matured sampled outcomes across 1/6/24/48h: 17795; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 79 (sampled only; not a success-rate estimate).
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

**Writer:** 45096730610 · **Generation:** 1364 · **Legacy run:** 45096730610
**Main quote time:** 2026-11-23T01:51:21.219011+00:00 · **Legacy report time:** 2026-11-23T01:52:16.959467+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38515 | 64.55 | -0.46% | 0.65x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |
| 2 | PAXG/USD | 3593.01 | 39.38 | -0.25% | 0.23x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | CC/USD | 0.07372 | 36.22 | +0.15% | 0.91x | WEAK 38/100 | HIGH 67/100 | Watch |
| 4 | PEARL/USD | 2.0937 | 35.62 | -0.77% | 0.38x | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | XAUT/USD | 3594.4 | 33.65 | -0.26% | 0.78x | WEAK 22/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | ALIGN/USD | 0.00354 | 21.95 | +1.43% | 0.57x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 7 | ICNT/USD | 0.3551 | 10.35 | -1.31% | 0.51x | WEAK 0/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | EVAA/USD | 2.3588 | 37.77 | +1.46% | 1.44x | 3802 | MODERATE 54/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
