# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:45:13.269389+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44372992772
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6f050405de1a28f930ee5d38c68f84dcb6ee34bc (atomic ledger/results publication)
**Ledger generation:** 639 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019901 | 75.656 | 72.106 | +6.60% | -0.06% | 1.39x | 8.0 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | STABLE/USD | 0.02341 | 57.691 | 63.155 | +11.21% | +0.26% | 0.33x | 25.7 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | MEGA/USD | 0.05356 | 54.057 | 45.011 | +3.72% | +0.71% | 1.55x | 24.3 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.0453 | 52.743 | 52.207 | +0.91% | +0.38% | 0.87x | 4.4 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 5 | W/USD | 0.00898 | 42.182 | 29.648 | +0.56% | +0.90% | 1.80x | 11.1 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | MNT/USD | 0.385 | 41.397 | 49.915 | +3.13% | -0.05% | 0.17x | 7.8 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.08246 | 36.967 | 36.182 | +0.40% | +0.35% | 0.90x | 3.6 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5113 | 34.396 | 27.900 | +0.39% | +0.18% | 1.56x | 13.7 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 47/100 | HIGH 66/100 | Watch | WATCH |
| 9 | SPACE/USD | 0.003379 | 33.723 | 33.864 | +1.08% | +1.50% | 0.23x | 8.9 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | UAI/USD | 0.03363 | 32.694 | 28.670 | +0.75% | +1.27% | 0.77x | 14.9 | 2026-11-18T18:45:07.270972+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 80/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.106 | 0.019901 | -0.06% | 1.39x |
| 2 | STABLE/USD | 63.155 | 0.02341 | +0.26% | 0.33x |
| 3 | NIGHT/USD | 52.207 | 0.0453 | +0.38% | 0.87x |
| 4 | MNT/USD | 49.915 | 0.385 | -0.05% | 0.17x |
| 5 | MEGA/USD | 45.011 | 0.05356 | +0.71% | 1.55x |
| 6 | CC/USD | 36.182 | 0.08246 | +0.35% | 0.90x |
| 7 | SPACE/USD | 33.864 | 0.003379 | +1.50% | 0.23x |
| 8 | W/USD | 29.648 | 0.00898 | +0.90% | 1.80x |
| 9 | UAI/USD | 28.670 | 0.03363 | +1.27% | 0.77x |
| 10 | AKT/USD | 27.900 | 0.5113 | +0.18% | 1.56x |

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

- Persisted scans: 639; predictions: 5426; observations: 386158.
- Matured sampled outcomes across 1/6/24/48h: 4725; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44372992772 · **Generation:** 639 · **Legacy run:** 44372992772
**Main quote time:** 2026-11-18T18:45:13.269389+00:00 · **Legacy report time:** 2026-11-18T18:45:44.758931+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019901 | 75.66 | -0.06% | 1.39x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |
| 2 | STABLE/USD | 0.02341 | 57.69 | +0.26% | 0.33x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |
| 3 | MEGA/USD ⭐ | 0.05356 | 54.06 | +0.71% | 1.55x | STRONG 72/100 | VERY_HIGH 79/100 | Watch |
| 4 | NIGHT/USD | 0.0453 | 52.74 | +0.38% | 0.87x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 5 | W/USD | 0.00898 | 42.18 | +0.90% | 1.80x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 6 | MNT/USD | 0.385 | 41.40 | -0.05% | 0.17x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | CC/USD | 0.08246 | 36.97 | +0.35% | 0.90x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 8 | AKT/USD ⭐ | 0.5113 | 34.40 | +0.18% | 1.56x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 9 | SPACE/USD | 0.003379 | 33.72 | +1.50% | 0.23x | MODERATE 47/100 | VERY_HIGH 82/100 | Watch |
| 10 | UAI/USD | 0.03363 | 32.69 | +1.27% | 0.77x | WEAK 41/100 | VERY_HIGH 80/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05356 | 59.66 | +0.71% | 1.55x | 1204 | STRONG 80/100 | VERY_HIGH 73/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5113 | 30.69 | +0.18% | 1.56x | 4485 | MODERATE 60/100 | HIGH 60/100 | Watch |

**Same-run overlap:** MEGA/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
