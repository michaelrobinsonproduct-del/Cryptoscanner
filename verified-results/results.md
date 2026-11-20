# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T02:05:27.054347+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44658176725
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b02ca150d5bbe264c2208d72724938749b5df4c7 (atomic ledger/results publication)
**Ledger generation:** 903 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4311 | 41.367 | 34.277 | +1.17% | -0.05% | 1.73x | 23.2 | 2026-11-20T02:05:23.615507+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 2 | NIGHT/USD | 0.0451 | 36.477 | 41.342 | +0.76% | +0.18% | 0.42x | 8.9 | 2026-11-20T02:05:23.615507+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | CAP/USD | 0.097313 | 26.728 | 30.968 | +0.72% | -0.48% | 0.82x | 17.0 | 2026-11-20T02:05:23.615507+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | SYRUP/USD | 0.09657 | 10.963 | 17.849 | +0.35% | +0.09% | 0.26x | 33.2 | 2026-11-20T02:05:23.615507+00:00 | Not calibrated | WEAK 15/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 41.342 | 0.0451 | +0.18% | 0.42x |
| 2 | ICNT/USD | 34.277 | 0.4311 | -0.05% | 1.73x |
| 3 | CAP/USD | 30.968 | 0.097313 | -0.48% | 0.82x |
| 4 | SYRUP/USD | 17.849 | 0.09657 | +0.09% | 0.26x |

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

- Persisted scans: 903; predictions: 7867; observations: 545634.
- Matured sampled outcomes across 1/6/24/48h: 8730; gap abstentions: 16323. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44658176725 · **Generation:** 903 · **Legacy run:** 44658176725
**Main quote time:** 2026-11-20T02:05:27.054347+00:00 · **Legacy report time:** 2026-11-20T02:06:10.465930+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.4311 | 41.37 | -0.05% | 1.73x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 2 | NIGHT/USD | 0.0451 | 36.48 | +0.18% | 0.42x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 3 | CAP/USD | 0.097313 | 26.73 | -0.48% | 0.82x | WEAK 13/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | SYRUP/USD | 0.09657 | 10.96 | +0.09% | 0.26x | WEAK 15/100 | EXTREME 87/100 | Do nothing |

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
