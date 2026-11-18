# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:10:21.318759+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44366611997
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** f62caa0be15aaac2599b15500693e54c58cbc1c7 (atomic ledger/results publication)
**Ledger generation:** 632 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.04985 | 77.211 | 65.306 | +5.73% | +0.26% | 2.06x | 14.1 | 2026-11-18T18:10:15.970572+00:00 | Not calibrated | STRONG 89/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.019936 | 75.923 | 72.580 | +6.79% | +0.35% | 1.16x | 7.0 | 2026-11-18T18:10:15.970572+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3833 | 55.136 | 45.398 | +2.68% | +0.55% | 1.70x | 10.4 | 2026-11-18T18:10:15.970572+00:00 | Not calibrated | MODERATE 68/100 | HIGH 66/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04553 | 48.385 | 55.481 | +1.43% | +0.31% | 0.14x | 6.6 | 2026-11-18T18:10:15.970572+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05292 | 28.545 | 40.910 | +2.48% | -1.34% | 0.44x | 15.1 | 2026-11-18T18:10:15.970572+00:00 | Not calibrated | WEAK 14/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.580 | 0.019936 | +0.35% | 1.16x |
| 2 | TRUST/USD | 65.306 | 0.04985 | +0.26% | 2.06x |
| 3 | NIGHT/USD | 55.481 | 0.04553 | +0.31% | 0.14x |
| 4 | MNT/USD | 45.398 | 0.3833 | +0.55% | 1.70x |
| 5 | MEGA/USD | 40.910 | 0.05292 | -1.34% | 0.44x |

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

- Persisted scans: 632; predictions: 5387; observations: 381895.
- Matured sampled outcomes across 1/6/24/48h: 4698; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44366611997 · **Generation:** 632 · **Legacy run:** 44366611997
**Main quote time:** 2026-11-18T18:10:21.318759+00:00 · **Legacy report time:** 2026-11-18T18:10:46.640923+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.04985 | 77.21 | +0.26% | 2.06x | STRONG 99/100 | HIGH 66/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.019936 | 75.92 | +0.35% | 1.16x | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3833 | 55.14 | +0.55% | 1.70x | STRONG 78/100 | HIGH 66/100 | Consider small entry |
| 4 | NIGHT/USD | 0.04553 | 48.38 | +0.31% | 0.14x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 5 | MEGA/USD | 0.05292 | 28.54 | -1.34% | 0.44x | WEAK 14/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD ⭐ | 0.04985 | 76.38 | +0.26% | 2.06x | 3301 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019936 | 72.34 | +0.35% | 1.16x | 6098 | STRONG 81/100 | VERY_HIGH 74/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3837 | 54.06 | +0.55% | 1.70x | 1807 | STRONG 77/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** TRUST/USD, SENT/USD, MNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
