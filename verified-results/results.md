# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:35:21.808597+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44437935326
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7561e203c81dfe82e505fbab1eaad807b1543afa (atomic ledger/results publication)
**Ledger generation:** 720 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021312 | 55.448 | 51.709 | +3.43% | -0.14% | 1.44x | 7.5 | 2026-11-19T01:35:18.111208+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05736 | 45.588 | 36.014 | +2.43% | -0.64% | 2.28x | 24.4 | 2026-11-19T01:35:18.111208+00:00 | Not calibrated | WEAK 43/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | DRV/USD | 0.26647 | 32.771 | 35.046 | +0.67% | -0.39% | 0.97x | 5.6 | 2026-11-19T01:35:18.111208+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 4 | STABLE/USD | 0.02281 | 29.088 | 19.783 | +0.31% | +0.18% | 1.84x | 26.4 | 2026-11-19T01:35:18.111208+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | PYTH/USD | 0.05308 | 16.511 | 29.343 | +0.61% | -0.75% | 0.09x | 13.2 | 2026-11-19T01:35:18.111208+00:00 | Not calibrated | WEAK 8/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 51.709 | 0.021312 | -0.14% | 1.44x |
| 2 | MEGA/USD | 36.014 | 0.05736 | -0.64% | 2.28x |
| 3 | DRV/USD | 35.046 | 0.26647 | -0.39% | 0.97x |
| 4 | PYTH/USD | 29.343 | 0.05308 | -0.75% | 0.09x |
| 5 | STABLE/USD | 19.783 | 0.02281 | +0.18% | 1.84x |

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

- Persisted scans: 720; predictions: 5840; observations: 435487.
- Matured sampled outcomes across 1/6/24/48h: 5740; gap abstentions: 13456. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44437935326 · **Generation:** 720 · **Legacy run:** 44437935326
**Main quote time:** 2026-11-19T01:35:21.808597+00:00 · **Legacy report time:** 2026-11-19T01:35:53.550485+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021312 | 55.45 | -0.14% | 1.44x | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |
| 2 | MEGA/USD | 0.05736 | 45.59 | -0.64% | 2.28x | WEAK 43/100 | EXTREME 85/100 | Do nothing |
| 3 | DRV/USD | 0.26647 | 32.77 | -0.39% | 0.97x | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing |
| 4 | STABLE/USD ⭐ | 0.02281 | 29.09 | +0.18% | 1.84x | MODERATE 50/100 | VERY_HIGH 79/100 | Watch |
| 5 | PYTH/USD | 0.05308 | 16.51 | -0.75% | 0.09x | WEAK 8/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.02281 | 26.41 | +0.18% | 1.84x | 2201 | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** STABLE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
