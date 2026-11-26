# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T09:36:26.244185+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45793237118
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e088f32d97846c3bfbdb264e041e59bccd620386 (atomic ledger/results publication)
**Ledger generation:** 1843 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 584; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.247 | 77.702 | 75.424 | +4.92% | -0.26% | 1.36x | 4.8 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SEI/USD | 0.03547 | 69.031 | 71.534 | +6.48% | -1.09% | 1.29x | 11.3 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.07077 | 67.945 | 71.680 | +6.79% | -0.65% | 0.95x | 11.3 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | ADA/USD | 0.149135 | 66.935 | 71.126 | +2.31% | +0.07% | 0.55x | 0.1 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | LTC/USD | 43.75 | 64.557 | 70.902 | +2.44% | -0.18% | 0.46x | 2.3 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.9013 | 64.254 | 64.774 | +10.18% | +1.46% | 0.22x | 40.4 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 92/100 | Do nothing | WATCH |
| 7 | HBAR/USD | 0.05366 | 62.742 | 56.293 | +2.99% | -0.33% | 1.81x | 3.7 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LINK/USD | 9.23331 | 59.794 | 68.757 | +2.09% | -0.19% | 0.20x | 1.7 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XDG/USD | 0.056654 | 57.357 | 59.068 | +1.24% | -0.15% | 0.90x | 0.0 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.95101 | 56.169 | 65.748 | +1.54% | -0.30% | 0.19x | 0.1 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | NEAR/USD | 3.0583 | 53.717 | 55.292 | +0.28% | -0.17% | 0.93x | 3.3 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XBT/USD | 60794.3 | 51.971 | 59.928 | +0.71% | -0.10% | 0.26x | 0.0 | 2026-11-26T09:36:18.173928+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 75.424 | 6.247 | -0.26% | 1.36x |
| 2 | SYRUP/USD | 71.680 | 0.07077 | -0.65% | 0.95x |
| 3 | SEI/USD | 71.534 | 0.03547 | -1.09% | 1.29x |
| 4 | ADA/USD | 71.126 | 0.149135 | +0.07% | 0.55x |
| 5 | LTC/USD | 70.902 | 43.75 | -0.18% | 0.46x |
| 6 | LINK/USD | 68.757 | 9.23331 | -0.19% | 0.20x |
| 7 | XRP/USD | 65.748 | 0.95101 | -0.30% | 0.19x |
| 8 | PIEVERSE/USD | 64.774 | 3.9013 | +1.46% | 0.22x |
| 9 | XBT/USD | 59.928 | 60794.3 | -0.10% | 0.26x |
| 10 | XDG/USD | 59.068 | 0.056654 | -0.15% | 0.90x |
| 11 | HBAR/USD | 56.293 | 0.05366 | -0.33% | 1.81x |
| 12 | NEAR/USD | 55.292 | 3.0583 | -0.17% | 0.93x |

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

- Persisted scans: 1843; predictions: 15851; observations: 1117404.
- Matured sampled outcomes across 1/6/24/48h: 34346; gap abstentions: 24470. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45793237118 · **Generation:** 1843 · **Legacy run:** 45793237118
**Main quote time:** 2026-11-26T09:36:26.244185+00:00 · **Legacy report time:** 2026-11-26T09:37:23.120357+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.247 | 77.70 | -0.26% | 1.36x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 2 | SEI/USD | 0.03547 | 69.03 | -1.09% | 1.29x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 3 | SYRUP/USD | 0.07077 | 67.94 | -0.65% | 0.95x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | ADA/USD | 0.149135 | 66.93 | +0.07% | 0.55x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 5 | LTC/USD | 43.75 | 64.56 | -0.18% | 0.46x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 6 | PIEVERSE/USD | 3.9013 | 64.25 | +1.46% | 0.22x | MODERATE 47/100 | EXTREME 92/100 | Do nothing |
| 7 | HBAR/USD | 0.05366 | 62.74 | -0.33% | 1.81x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | LINK/USD | 9.23331 | 59.79 | -0.19% | 0.20x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | XDG/USD | 0.056654 | 57.36 | -0.15% | 0.90x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 10 | XRP/USD | 0.95101 | 56.17 | -0.30% | 0.19x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | NEAR/USD | 3.0583 | 53.72 | -0.17% | 0.93x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 12 | XBT/USD | 60794.3 | 51.97 | -0.10% | 0.26x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

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
