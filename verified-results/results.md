# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T00:52:41.645649+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45521087096
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f7834e1ba6cbdacb06c77fb6bc1b382cc90cc258 (atomic ledger/results publication)
**Ledger generation:** 1648 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04219 | 55.013 | 49.846 | +2.95% | +1.05% | 0.99x | 9.5 | 2026-11-25T00:52:36.210065+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 2 | PROS/USD | 0.6878 | 47.521 | 39.733 | +2.55% | +0.61% | 1.47x | 18.8 | 2026-11-25T00:52:36.210065+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66538 | 46.334 | 45.570 | +0.28% | -0.04% | 1.10x | 1.8 | 2026-11-25T00:52:36.210065+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.31507 | 32.237 | 30.170 | +0.25% | +1.10% | 0.66x | 11.7 | 2026-11-25T00:52:36.210065+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07047 | 28.364 | 27.506 | +1.15% | +0.14% | 1.01x | 24.2 | 2026-11-25T00:52:36.210065+00:00 | Not calibrated | WEAK 29/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | PEARL/USD | 2.1543 | 23.764 | 30.359 | +0.66% | -0.30% | 0.49x | 25.6 | 2026-11-25T00:52:36.210065+00:00 | Not calibrated | WEAK 7/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 49.846 | 0.04219 | +1.05% | 0.99x |
| 2 | AUD/USD | 45.570 | 0.66538 | -0.04% | 1.10x |
| 3 | PROS/USD | 39.733 | 0.6878 | +0.61% | 1.47x |
| 4 | PEARL/USD | 30.359 | 2.1543 | -0.30% | 0.49x |
| 5 | DRV/USD | 30.170 | 0.31507 | +1.10% | 0.66x |
| 6 | SYRUP/USD | 27.506 | 0.07047 | +0.14% | 1.01x |

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

- Persisted scans: 1648; predictions: 14087; observations: 998723.
- Matured sampled outcomes across 1/6/24/48h: 29352; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45521087096 · **Generation:** 1648 · **Legacy run:** 45521087096
**Main quote time:** 2026-11-25T00:52:41.645649+00:00 · **Legacy report time:** 2026-11-25T00:53:35.660367+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.04219 | 55.01 | +1.05% | 0.99x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 2 | PROS/USD ⭐ | 0.6878 | 47.52 | +0.61% | 1.47x | STRONG 74/100 | VERY_HIGH 73/100 | Watch |
| 3 | AUD/USD | 0.66538 | 46.33 | -0.04% | 1.10x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 4 | DRV/USD | 0.31507 | 32.24 | +1.10% | 0.66x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 5 | SYRUP/USD ⭐ | 0.07047 | 28.36 | +0.14% | 1.01x | WEAK 39/100 | EXTREME 86/100 | Do nothing |
| 6 | PEARL/USD | 2.1543 | 23.76 | -0.30% | 0.49x | WEAK 7/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD ⭐ | 0.689 | 51.26 | +0.61% | 1.47x | 1680 | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07047 | 37.22 | +0.14% | 1.01x | 3254 | WEAK 44/100 | EXTREME 86/100 | Do nothing |
| 3 | BCH/USD | 197.39 | 28.49 | +0.06% | 1.63x | 1847 | MODERATE 49/100 | HIGH 60/100 | Watch |

**Same-run overlap:** PROS/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
