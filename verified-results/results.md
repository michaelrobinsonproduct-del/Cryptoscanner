# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T11:40:51.056008+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44729391263
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** da107f1f7baf2b5bca22989b01df6fbaa4b86bb3 (atomic ledger/results publication)
**Ledger generation:** 973 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022008 | 53.896 | 52.539 | +3.38% | +0.32% | 0.98x | 8.2 | 2026-11-20T11:40:46.932467+00:00 | Not calibrated | MODERATE 57/100 | HIGH 67/100 | Watch | WATCH |
| 2 | MON/USD | 0.01403 | 43.922 | 43.742 | +1.96% | +1.01% | 0.51x | 7.1 | 2026-11-20T11:40:46.932467+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.4334 | 41.973 | 39.898 | +1.71% | -0.14% | 1.28x | 20.8 | 2026-11-20T11:40:46.932467+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 4 | AERO/USD | 0.419 | 41.355 | 34.758 | +0.96% | +0.07% | 1.62x | 9.6 | 2026-11-20T11:40:46.932467+00:00 | Not calibrated | MODERATE 56/100 | HIGH 60/100 | Watch | WATCH |
| 5 | WINGS/USD | 0.00188 | 5.561 | 26.349 | +1.95% | -2.96% | 0.40x | 37.3 | 2026-11-20T11:40:46.932467+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 52.539 | 0.022008 | +0.32% | 0.98x |
| 2 | MON/USD | 43.742 | 0.01403 | +1.01% | 0.51x |
| 3 | ICNT/USD | 39.898 | 0.4334 | -0.14% | 1.28x |
| 4 | AERO/USD | 34.758 | 0.419 | +0.07% | 1.62x |
| 5 | WINGS/USD | 26.349 | 0.00188 | -2.96% | 0.40x |

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

- Persisted scans: 973; predictions: 8197; observations: 587965.
- Matured sampled outcomes across 1/6/24/48h: 9844; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44729391263 · **Generation:** 973 · **Legacy run:** 44729391263
**Main quote time:** 2026-11-20T11:40:51.056008+00:00 · **Legacy report time:** 2026-11-20T11:41:51.227811+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.022008 | 53.90 | +0.32% | 0.98x | MODERATE 57/100 | HIGH 67/100 | Watch |
| 2 | MON/USD | 0.01403 | 43.92 | +1.01% | 0.51x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 3 | ICNT/USD | 0.4334 | 41.97 | -0.14% | 1.28x | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing |
| 4 | AERO/USD ⭐ | 0.419 | 41.36 | +0.07% | 1.62x | MODERATE 66/100 | HIGH 60/100 | Watch |
| 5 | WINGS/USD | 0.00188 | 5.56 | -2.96% | 0.40x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AERO/USD ⭐ | 0.419 | 34.37 | +0.07% | 1.62x | 1557 | MODERATE 62/100 | HIGH 60/100 | Watch |

**Same-run overlap:** AERO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
