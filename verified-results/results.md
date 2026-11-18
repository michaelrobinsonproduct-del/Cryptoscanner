# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:45:15.880412+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44362017173
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 3e7f375dba1564cfe9b87a5d330cb0cc14b5f9ba (atomic ledger/results publication)
**Ledger generation:** 627 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019885 | 82.466 | 73.298 | +6.51% | -0.19% | 2.01x | 5.5 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.04989 | 69.043 | 70.942 | +5.81% | +0.20% | 0.71x | 4.0 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3838 | 60.408 | 47.613 | +2.81% | -0.44% | 3.30x | 7.8 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04513 | 55.317 | 49.133 | +0.53% | -0.15% | 1.70x | 6.7 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05362 | 51.861 | 47.739 | +3.83% | -0.07% | 1.45x | 20.5 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | WEAK 36/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.08244 | 34.962 | 34.558 | +0.38% | -1.33% | 1.70x | 7.3 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5112 | 26.974 | 33.651 | +0.37% | +0.22% | 0.22x | 2.0 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | ZAMA/USD | 0.06074 | 25.609 | 34.393 | +1.35% | -0.12% | 0.18x | 13.2 | 2026-11-18T17:45:10.557087+00:00 | Not calibrated | WEAK 13/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.298 | 0.019885 | -0.19% | 2.01x |
| 2 | TRUST/USD | 70.942 | 0.04989 | +0.20% | 0.71x |
| 3 | NIGHT/USD | 49.133 | 0.04513 | -0.15% | 1.70x |
| 4 | MEGA/USD | 47.739 | 0.05362 | -0.07% | 1.45x |
| 5 | MNT/USD | 47.613 | 0.3838 | -0.44% | 3.30x |
| 6 | CC/USD | 34.558 | 0.08244 | -1.33% | 1.70x |
| 7 | ZAMA/USD | 34.393 | 0.06074 | -0.12% | 0.18x |
| 8 | AKT/USD | 33.651 | 0.5112 | +0.22% | 0.22x |

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

- Persisted scans: 627; predictions: 5354; observations: 378850.
- Matured sampled outcomes across 1/6/24/48h: 4653; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44362017173 · **Generation:** 627 · **Legacy run:** 44362017173
**Main quote time:** 2026-11-18T17:45:15.880412+00:00 · **Legacy report time:** 2026-11-18T17:45:43.170255+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019885 | 82.47 | -0.19% | 2.01x | STRONG 71/100 | VERY_HIGH 73/100 | Watch |
| 2 | TRUST/USD | 0.04989 | 69.04 | +0.20% | 0.71x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 3 | MNT/USD | 0.3838 | 60.41 | -0.44% | 3.30x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 4 | NIGHT/USD | 0.04513 | 55.32 | -0.15% | 1.70x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 5 | MEGA/USD | 0.05362 | 51.86 | -0.07% | 1.45x | WEAK 36/100 | EXTREME 85/100 | Do nothing |
| 6 | CC/USD | 0.08244 | 34.96 | -1.33% | 1.70x | WEAK 37/100 | VERY_HIGH 70/100 | Do nothing |
| 7 | AKT/USD | 0.5112 | 26.97 | +0.22% | 0.22x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |
| 8 | ZAMA/USD | 0.06074 | 25.61 | -0.12% | 0.18x | WEAK 13/100 | EXTREME 94/100 | Do nothing |

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
