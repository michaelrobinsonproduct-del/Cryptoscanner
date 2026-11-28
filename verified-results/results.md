# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T11:02:57.190627+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46137443302
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 42cccc991468226f6f5889edba7aa14b3d9372b7 (atomic ledger/results publication)
**Ledger generation:** 2145 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.788 | 77.837 | 67.973 | +4.04% | +0.38% | 1.80x | 9.0 | 2026-11-28T11:02:53.817796+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05249 | 77.527 | 82.537 | +4.48% | -0.36% | 0.68x | 7.6 | 2026-11-28T11:02:53.817796+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004417 | 77.267 | 70.482 | +5.72% | -1.64% | 6.99x | 2.3 | 2026-11-28T11:02:53.817796+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024502 | 49.765 | 53.392 | +3.32% | +0.20% | 0.54x | 2.4 | 2026-11-28T11:02:53.817796+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | PIEVERSE/USD | 3.9868 | 33.200 | 44.290 | +3.28% | -0.41% | 0.10x | 32.6 | 2026-11-28T11:02:53.817796+00:00 | Not calibrated | WEAK 12/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.07444 | 31.364 | 34.761 | +0.39% | -0.24% | 0.78x | 4.0 | 2026-11-28T11:02:53.817796+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 82.537 | 0.05249 | -0.36% | 0.68x |
| 2 | SPACE/USD | 70.482 | 0.004417 | -1.64% | 6.99x |
| 3 | VVV/USD | 67.973 | 26.788 | +0.38% | 1.80x |
| 4 | SENT/USD | 53.392 | 0.024502 | +0.20% | 0.54x |
| 5 | PIEVERSE/USD | 44.290 | 3.9868 | -0.41% | 0.10x |
| 6 | CC/USD | 34.761 | 0.07444 | -0.24% | 0.78x |

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

- Persisted scans: 2145; predictions: 19140; observations: 1298916.
- Matured sampled outcomes across 1/6/24/48h: 45525; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46137443302 · **Generation:** 2145 · **Legacy run:** 46137443302
**Main quote time:** 2026-11-28T11:02:57.190627+00:00 · **Legacy report time:** 2026-11-28T11:03:49.206022+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.788 | 77.84 | +0.38% | 1.80x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD | 0.05249 | 77.53 | -0.36% | 0.68x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 3 | SPACE/USD | 0.004417 | 77.27 | -1.64% | 6.99x | MODERATE 69/100 | VERY_HIGH 77/100 | Do nothing |
| 4 | SENT/USD | 0.024502 | 49.77 | +0.20% | 0.54x | MODERATE 55/100 | VERY_HIGH 82/100 | Watch |
| 5 | PIEVERSE/USD | 3.9868 | 33.20 | -0.41% | 0.10x | WEAK 12/100 | EXTREME 88/100 | Do nothing |
| 6 | CC/USD | 0.07444 | 31.36 | -0.24% | 0.78x | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.788 | 82.85 | +0.38% | 1.80x | 7749 | STRONG 96/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
