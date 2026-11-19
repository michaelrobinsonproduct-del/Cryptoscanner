# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:10:28.361717+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44635196108
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** d4f9541523bdd89e155795c2847f3ab1b959b360 (atomic ledger/results publication)
**Ledger generation:** 876 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05977 | 60.118 | 68.680 | +6.73% | -0.18% | 0.24x | 16.8 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 2 | VVV/USD | 21.759 | 52.052 | 54.625 | +0.41% | -0.48% | 0.98x | 6.4 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 3 | INJ/USD | 7.045 | 47.018 | 49.740 | +0.92% | -0.10% | 0.78x | 4.3 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.021237 | 42.690 | 52.757 | +3.07% | -1.00% | 0.49x | 6.1 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 26/100 | EXTREME 85/100 | Do nothing | WATCH |
| 5 | USELESS/USD | 0.09861 | 42.641 | 50.449 | +3.19% | -0.53% | 0.49x | 24.4 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 16/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | CAP/USD | 0.096708 | 37.216 | 31.024 | +0.72% | +1.27% | 0.98x | 17.3 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | TRX/USD | 0.310109 | 36.150 | 44.167 | +0.27% | +0.01% | 0.19x | 0.0 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | LIGHTER/USD | 2.784 | 33.006 | 38.550 | +2.58% | -0.32% | 0.61x | 28.9 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 12/100 | EXTREME 93/100 | Do nothing | WATCH |
| 9 | REKT/USD | 7.27e-08 | 31.614 | 39.919 | +1.96% | -1.22% | 0.78x | 13.8 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 10 | AKT/USD | 0.5301 | 29.800 | 42.037 | +2.34% | -0.61% | 0.08x | 13.2 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 15/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | AKE/USD | 0.01047758 | 25.790 | 31.786 | +0.83% | -1.54% | 1.17x | 17.2 | 2026-11-19T23:10:20.030790+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 83/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 68.680 | 0.05977 | -0.18% | 0.24x |
| 2 | VVV/USD | 54.625 | 21.759 | -0.48% | 0.98x |
| 3 | SENT/USD | 52.757 | 0.021237 | -1.00% | 0.49x |
| 4 | USELESS/USD | 50.449 | 0.09861 | -0.53% | 0.49x |
| 5 | INJ/USD | 49.740 | 7.045 | -0.10% | 0.78x |
| 6 | TRX/USD | 44.167 | 0.310109 | +0.01% | 0.19x |
| 7 | AKT/USD | 42.037 | 0.5301 | -0.61% | 0.08x |
| 8 | REKT/USD | 39.919 | 7.27e-08 | -1.22% | 0.78x |
| 9 | LIGHTER/USD | 38.550 | 2.784 | -0.32% | 0.61x |
| 10 | AKE/USD | 31.786 | 0.01047758 | -1.54% | 1.17x |
| 11 | CAP/USD | 31.024 | 0.096708 | +1.27% | 0.98x |

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

- Persisted scans: 876; predictions: 7625; observations: 529354.
- Matured sampled outcomes across 1/6/24/48h: 8103; gap abstentions: 15799. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44635196108 · **Generation:** 876 · **Legacy run:** 44635196108
**Main quote time:** 2026-11-19T23:10:28.361717+00:00 · **Legacy report time:** 2026-11-19T23:11:11.735765+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05977 | 60.12 | -0.18% | 0.24x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 2 | VVV/USD | 21.759 | 52.05 | -0.48% | 0.98x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 3 | INJ/USD | 7.045 | 47.02 | -0.10% | 0.78x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 4 | SENT/USD | 0.021237 | 42.69 | -1.00% | 0.49x | WEAK 26/100 | EXTREME 85/100 | Do nothing |
| 5 | USELESS/USD | 0.09861 | 42.64 | -0.53% | 0.49x | WEAK 16/100 | EXTREME 88/100 | Do nothing |
| 6 | CAP/USD | 0.096708 | 37.22 | +1.27% | 0.98x | WEAK 44/100 | VERY_HIGH 73/100 | Watch |
| 7 | TRX/USD | 0.310109 | 36.15 | +0.01% | 0.19x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 8 | LIGHTER/USD | 2.784 | 33.01 | -0.32% | 0.61x | WEAK 12/100 | EXTREME 93/100 | Do nothing |
| 9 | REKT/USD | 7.27e-08 | 31.61 | -1.22% | 0.78x | WEAK 16/100 | VERY_HIGH 83/100 | Do nothing |
| 10 | AKT/USD | 0.5301 | 29.80 | -0.61% | 0.08x | WEAK 15/100 | EXTREME 87/100 | Do nothing |
| 11 | AKE/USD | 0.01047758 | 25.79 | -1.54% | 1.17x | WEAK 18/100 | VERY_HIGH 83/100 | Do nothing |

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
