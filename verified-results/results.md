# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:45:23.590770+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44558226496
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 0dba60a1464894e8fe79d9f038978877a80e74a3 (atomic ledger/results publication)
**Ledger generation:** 805 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 67.79 | 72.416 | 62.311 | +1.36% | -0.98% | 2.61x | 4.4 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 920.58 | 68.257 | 58.964 | +0.95% | -1.14% | 4.15x | 5.3 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 64/100 | HIGH 65/100 | Watch | WATCH |
| 3 | VVV/USD | 22.375 | 68.050 | 73.047 | +3.25% | -2.15% | 1.58x | 9.4 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 54/100 | HIGH 65/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.021301 | 66.571 | 55.262 | +3.38% | -0.74% | 2.62x | 5.2 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 5 | SKR/USD | 0.01037 | 66.261 | 69.243 | +7.65% | +0.17% | 0.61x | 13.5 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5478 | 65.773 | 65.360 | +5.75% | -0.67% | 1.38x | 12.8 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | BILL/USD | 0.00428 | 63.859 | 63.996 | +8.35% | -1.38% | 1.68x | 23.5 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | WEAK 42/100 | EXTREME 89/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.15191 | 61.225 | 56.224 | +0.43% | -1.00% | 2.00x | 3.6 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 61/100 | HIGH 65/100 | Watch | WATCH |
| 9 | PYTH/USD | 0.05606 | 58.328 | 66.981 | +6.25% | -1.15% | 0.71x | 17.9 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | WEAK 29/100 | EXTREME 91/100 | Do nothing | WATCH |
| 10 | INJ/USD | 7.076 | 57.033 | 51.062 | +1.36% | -1.81% | 2.95x | 4.2 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 59/100 | HIGH 65/100 | Do nothing | WATCH |
| 11 | MNT/USD | 0.391 | 53.138 | 41.314 | +1.88% | -0.64% | 3.00x | 5.1 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 12 | SYRUP/USD | 0.10207 | 50.277 | 63.682 | +7.49% | -2.07% | 0.70x | 25.4 | 2026-11-19T15:45:14.942309+00:00 | Not calibrated | WEAK 20/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.047 | 22.375 | -2.15% | 1.58x |
| 2 | SKR/USD | 69.243 | 0.01037 | +0.17% | 0.61x |
| 3 | PYTH/USD | 66.981 | 0.05606 | -1.15% | 0.71x |
| 4 | AKT/USD | 65.360 | 0.5478 | -0.67% | 1.38x |
| 5 | BILL/USD | 63.996 | 0.00428 | -1.38% | 1.68x |
| 6 | SYRUP/USD | 63.682 | 0.10207 | -2.07% | 0.70x |
| 7 | HYPE/USD | 62.311 | 67.79 | -0.98% | 2.61x |
| 8 | ZEC/USD | 58.964 | 920.58 | -1.14% | 4.15x |
| 9 | ADA/USD | 56.224 | 0.15191 | -1.00% | 2.00x |
| 10 | SENT/USD | 55.262 | 0.021301 | -0.74% | 2.62x |
| 11 | INJ/USD | 51.062 | 7.076 | -1.81% | 2.95x |
| 12 | MNT/USD | 41.314 | 0.391 | -0.64% | 3.00x |

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

- Persisted scans: 805; predictions: 6804; observations: 486815.
- Matured sampled outcomes across 1/6/24/48h: 6803; gap abstentions: 15247. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44558226496 · **Generation:** 805 · **Legacy run:** 44558226496
**Main quote time:** 2026-11-19T15:45:23.590770+00:00 · **Legacy report time:** 2026-11-19T15:46:09.679280+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 67.79 | 72.42 | -0.98% | 2.61x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 920.58 | 68.26 | -1.14% | 4.15x | MODERATE 64/100 | HIGH 65/100 | Watch |
| 3 | VVV/USD | 22.375 | 68.05 | -2.15% | 1.58x | MODERATE 54/100 | HIGH 65/100 | Do nothing |
| 4 | SENT/USD | 0.021301 | 66.57 | -0.74% | 2.62x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 5 | SKR/USD | 0.01037 | 66.26 | +0.17% | 0.61x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 6 | AKT/USD | 0.5478 | 65.77 | -0.67% | 1.38x | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |
| 7 | BILL/USD | 0.00428 | 63.86 | -1.38% | 1.68x | WEAK 42/100 | EXTREME 89/100 | Do nothing |
| 8 | ADA/USD | 0.15191 | 61.22 | -1.00% | 2.00x | MODERATE 61/100 | HIGH 65/100 | Watch |
| 9 | PYTH/USD | 0.05606 | 58.33 | -1.15% | 0.71x | WEAK 29/100 | EXTREME 91/100 | Do nothing |
| 10 | INJ/USD | 7.076 | 57.03 | -1.81% | 2.95x | MODERATE 59/100 | HIGH 65/100 | Do nothing |
| 11 | MNT/USD | 0.391 | 53.14 | -0.64% | 3.00x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 12 | SYRUP/USD | 0.10207 | 50.28 | -2.07% | 0.70x | WEAK 20/100 | EXTREME 100/100 | Do nothing |

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
