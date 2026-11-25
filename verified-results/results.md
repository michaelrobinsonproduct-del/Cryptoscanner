# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T09:17:43.823911+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45583535420
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 327d5c1605c46cd6c740f001f40790f5096582b3 (atomic ledger/results publication)
**Ledger generation:** 1698 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01054 | 79.119 | 85.902 | +11.30% | -2.06% | 1.35x | 19.0 | 2026-11-25T09:17:38.091994+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | DRV/USD | 0.33483 | 68.124 | 78.111 | +6.54% | -1.05% | 0.52x | 9.0 | 2026-11-25T09:17:38.091994+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | VVV/USD | 24.688 | 66.928 | 56.242 | +0.61% | -0.86% | 3.31x | 6.1 | 2026-11-25T09:17:38.091994+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 4 | BABY/USD | 0.00868 | 43.370 | 49.912 | +5.08% | -1.24% | 0.97x | 34.5 | 2026-11-25T09:17:38.091994+00:00 | Not calibrated | WEAK 17/100 | EXTREME 96/100 | Do nothing | WATCH |
| 5 | PROS/USD | 0.7014 | 34.520 | 44.194 | +4.58% | -0.93% | 0.50x | 39.7 | 2026-11-25T09:17:38.091994+00:00 | Not calibrated | WEAK 7/100 | EXTREME 93/100 | Do nothing | WATCH |
| 6 | ATOM/USD | 1.2556 | 26.020 | 32.757 | +0.82% | -0.81% | 0.73x | 10.4 | 2026-11-25T09:17:38.091994+00:00 | Not calibrated | WEAK 13/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.902 | 0.01054 | -2.06% | 1.35x |
| 2 | DRV/USD | 78.111 | 0.33483 | -1.05% | 0.52x |
| 3 | VVV/USD | 56.242 | 24.688 | -0.86% | 3.31x |
| 4 | BABY/USD | 49.912 | 0.00868 | -1.24% | 0.97x |
| 5 | PROS/USD | 44.194 | 0.7014 | -0.93% | 0.50x |
| 6 | ATOM/USD | 32.757 | 1.2556 | -0.81% | 0.73x |

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

- Persisted scans: 1698; predictions: 14414; observations: 1029167.
- Matured sampled outcomes across 1/6/24/48h: 31041; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45583535420 · **Generation:** 1698 · **Legacy run:** 45583535420
**Main quote time:** 2026-11-25T09:17:43.823911+00:00 · **Legacy report time:** 2026-11-25T09:19:00.274242+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01054 | 79.12 | -2.06% | 1.35x | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | DRV/USD | 0.33483 | 68.12 | -1.05% | 0.52x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 3 | VVV/USD | 24.688 | 66.93 | -0.86% | 3.31x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 4 | BABY/USD | 0.00868 | 43.37 | -1.24% | 0.97x | WEAK 17/100 | EXTREME 96/100 | Do nothing |
| 5 | PROS/USD | 0.7014 | 34.52 | -0.93% | 0.50x | WEAK 7/100 | EXTREME 93/100 | Do nothing |
| 6 | ATOM/USD | 1.2556 | 26.02 | -0.81% | 0.73x | WEAK 13/100 | EXTREME 87/100 | Do nothing |

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
