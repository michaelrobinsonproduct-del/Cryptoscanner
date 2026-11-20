# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:30:28.627957+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44646282963
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 32298a24459549a26ac7b060cb835ca93934b1dc (atomic ledger/results publication)
**Ledger generation:** 887 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.7 | 71.798 | 55.235 | +0.65% | +0.31% | 5.27x | 8.6 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XLM/USD | 0.13305 | 48.493 | 54.477 | +0.26% | +0.08% | 0.36x | 4.7 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | CAP/USD | 0.097215 | 46.535 | 34.370 | +0.62% | -0.02% | 2.23x | 9.2 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.428 | 42.522 | 28.918 | +0.45% | -0.28% | 2.77x | 23.4 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5359 | 38.594 | 28.491 | +0.45% | -0.98% | 9.65x | 15.0 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.012465 | 38.361 | 34.036 | +2.26% | +1.21% | 0.83x | 28.2 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.05919 | 33.904 | 34.973 | +1.60% | +1.21% | 0.29x | 16.9 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | STRK/USD | 0.03194 | 31.890 | 36.414 | +0.79% | +0.19% | 0.45x | 9.4 | 2026-11-20T00:30:20.142184+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 55.235 | 500.7 | +0.31% | 5.27x |
| 2 | XLM/USD | 54.477 | 0.13305 | +0.08% | 0.36x |
| 3 | STRK/USD | 36.414 | 0.03194 | +0.19% | 0.45x |
| 4 | MEGA/USD | 34.973 | 0.05919 | +1.21% | 0.29x |
| 5 | CAP/USD | 34.370 | 0.097215 | -0.02% | 2.23x |
| 6 | BLESS/USD | 34.036 | 0.012465 | +1.21% | 0.83x |
| 7 | ICNT/USD | 28.918 | 0.428 | -0.28% | 2.77x |
| 8 | AKT/USD | 28.491 | 0.5359 | -0.98% | 9.65x |

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

- Persisted scans: 887; predictions: 7743; observations: 535986.
- Matured sampled outcomes across 1/6/24/48h: 8411; gap abstentions: 16054. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44646282963 · **Generation:** 887 · **Legacy run:** 44646282963
**Main quote time:** 2026-11-20T00:30:28.627957+00:00 · **Legacy report time:** 2026-11-20T00:31:24.054324+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 500.7 | 71.80 | +0.31% | 5.27x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XLM/USD | 0.13305 | 48.49 | +0.08% | 0.36x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 3 | CAP/USD | 0.097215 | 46.53 | -0.02% | 2.23x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 4 | ICNT/USD | 0.428 | 42.52 | -0.28% | 2.77x | WEAK 41/100 | VERY_HIGH 73/100 | Watch |
| 5 | AKT/USD | 0.5359 | 38.59 | -0.98% | 9.65x | WEAK 44/100 | VERY_HIGH 72/100 | Watch |
| 6 | BLESS/USD | 0.012465 | 38.36 | +1.21% | 0.83x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 7 | MEGA/USD | 0.05919 | 33.90 | +1.21% | 0.29x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 8 | STRK/USD | 0.03194 | 31.89 | +0.19% | 0.45x | WEAK 36/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 500.87 | 54.11 | +0.31% | 5.27x | 7878 | STRONG 87/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
