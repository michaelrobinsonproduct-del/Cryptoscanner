# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T02:07:13.295623+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45530330482
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 604188ce6fd69566dee2a3bb5b6ea0db934dc4d3 (atomic ledger/results publication)
**Ledger generation:** 1655 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.32256 | 49.306 | 52.025 | +2.63% | +0.27% | 0.59x | 1.9 | 2026-11-25T02:07:09.591258+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04115 | 34.236 | 33.169 | +0.41% | -0.02% | 1.12x | 7.3 | 2026-11-25T02:07:09.591258+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.092845 | 33.477 | 30.286 | +0.46% | +0.82% | 0.91x | 10.7 | 2026-11-25T02:07:09.591258+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | GWEI/USD | 0.010336 | 10.507 | 21.204 | +0.30% | -1.36% | 0.61x | 23.3 | 2026-11-25T02:07:09.591258+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 52.025 | 0.32256 | +0.27% | 0.59x |
| 2 | SKY/USD | 33.169 | 0.04115 | -0.02% | 1.12x |
| 3 | CAP/USD | 30.286 | 0.092845 | +0.82% | 0.91x |
| 4 | GWEI/USD | 21.204 | 0.010336 | -1.36% | 0.61x |

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

- Persisted scans: 1655; predictions: 14120; observations: 1002986.
- Matured sampled outcomes across 1/6/24/48h: 29563; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45530330482 · **Generation:** 1655 · **Legacy run:** 45530330482
**Main quote time:** 2026-11-25T02:07:13.295623+00:00 · **Legacy report time:** 2026-11-25T02:08:12.183328+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.32256 | 49.31 | +0.27% | 0.59x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 2 | SKY/USD | 0.04115 | 34.24 | -0.02% | 1.12x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 3 | CAP/USD | 0.092845 | 33.48 | +0.82% | 0.91x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 4 | GWEI/USD | 0.010336 | 10.51 | -1.36% | 0.61x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.04223 | 15.58 | +0.52% | 1.99x | 946 | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
