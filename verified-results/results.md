# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:55:24.938404+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44363848802
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 87e2ab09e0d5b4060488ae0fb2e5f100c168f8ac (atomic ledger/results publication)
**Ledger generation:** 629 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04539 | 73.108 | 55.562 | +1.11% | +0.51% | 5.16x | 2.2 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.019892 | 71.530 | 74.577 | +6.55% | -0.78% | 1.08x | 3.0 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | TRUST/USD | 0.04972 | 69.090 | 58.341 | +5.45% | -0.32% | 2.24x | 24.1 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3818 | 51.667 | 41.216 | +2.28% | -0.91% | 2.73x | 13.1 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05359 | 48.220 | 54.777 | +3.78% | -0.11% | 0.40x | 5.6 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | WEAK 29/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.08238 | 38.136 | 33.323 | +0.30% | -0.15% | 1.55x | 8.5 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06049 | 22.264 | 31.450 | +0.93% | -0.18% | 0.17x | 13.2 | 2026-11-18T17:55:20.432983+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.577 | 0.019892 | -0.78% | 1.08x |
| 2 | TRUST/USD | 58.341 | 0.04972 | -0.32% | 2.24x |
| 3 | NIGHT/USD | 55.562 | 0.04539 | +0.51% | 5.16x |
| 4 | MEGA/USD | 54.777 | 0.05359 | -0.11% | 0.40x |
| 5 | MNT/USD | 41.216 | 0.3818 | -0.91% | 2.73x |
| 6 | CC/USD | 33.323 | 0.08238 | -0.15% | 1.55x |
| 7 | ZAMA/USD | 31.450 | 0.06049 | -0.18% | 0.17x |

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

- Persisted scans: 629; predictions: 5369; observations: 380068.
- Matured sampled outcomes across 1/6/24/48h: 4673; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44363848802 · **Generation:** 629 · **Legacy run:** 44363848802
**Main quote time:** 2026-11-18T17:55:24.938404+00:00 · **Legacy report time:** 2026-11-18T17:55:48.701822+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04539 | 73.11 | +0.51% | 5.16x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD | 0.019892 | 71.53 | -0.78% | 1.08x | MODERATE 46/100 | VERY_HIGH 80/100 | Watch |
| 3 | TRUST/USD | 0.04972 | 69.09 | -0.32% | 2.24x | MODERATE 55/100 | VERY_HIGH 78/100 | Watch |
| 4 | MNT/USD | 0.3818 | 51.67 | -0.91% | 2.73x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 5 | MEGA/USD | 0.05359 | 48.22 | -0.11% | 0.40x | WEAK 29/100 | EXTREME 88/100 | Do nothing |
| 6 | CC/USD | 0.08238 | 38.14 | -0.15% | 1.55x | WEAK 39/100 | HIGH 66/100 | Watch |
| 7 | ZAMA/USD | 0.06049 | 22.26 | -0.18% | 0.17x | WEAK 11/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04544 | 59.39 | +0.51% | 5.16x | 16204 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
