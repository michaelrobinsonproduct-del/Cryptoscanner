# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T21:30:33.190100+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44619292808
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 1cdfb7342ce884a0203ff252e87f5414058d257f (atomic ledger/results publication)
**Ledger generation:** 862 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.038 | 70.936 | 64.580 | +1.69% | -0.41% | 1.84x | 4.5 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05965 | 61.367 | 64.605 | +6.52% | +0.84% | 0.25x | 25.2 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | CSPR/USD | 0.0017186 | 59.921 | 54.242 | +5.24% | +0.17% | 1.48x | 28.6 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | BMT/USD | 0.02004 | 59.836 | 69.384 | +6.14% | -0.45% | 0.27x | 10.0 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 35/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | PUMP/USD | 0.002615 | 57.606 | 42.031 | +0.73% | +0.11% | 2.54x | 11.5 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5368 | 55.499 | 47.462 | +3.63% | -1.39% | 2.78x | 20.5 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | LUNA/USD | 4.82e-05 | 54.812 | 64.013 | +10.70% | -1.10% | 0.63x | 37.4 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 17/100 | EXTREME 92/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.021285 | 54.481 | 53.698 | +3.30% | -0.22% | 1.19x | 7.5 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | SKR/USD | 0.010029 | 49.391 | 46.919 | +4.11% | -0.10% | 1.30x | 26.0 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 25/100 | EXTREME 85/100 | Do nothing | WATCH |
| 10 | ALEO/USD | 0.03109 | 47.833 | 46.874 | +3.70% | +0.16% | 1.02x | 35.5 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 11 | USELESS/USD | 0.09762 | 34.509 | 39.868 | +2.16% | -1.00% | 0.97x | 27.8 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 12/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 12 | SYRUP/USD | 0.09685 | 30.753 | 40.238 | +1.99% | -0.46% | 0.28x | 10.3 | 2026-11-19T21:30:26.055337+00:00 | Not calibrated | WEAK 15/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BMT/USD | 69.384 | 0.02004 | -0.45% | 0.27x |
| 2 | MEGA/USD | 64.605 | 0.05965 | +0.84% | 0.25x |
| 3 | VVV/USD | 64.580 | 22.038 | -0.41% | 1.84x |
| 4 | LUNA/USD | 64.013 | 4.82e-05 | -1.10% | 0.63x |
| 5 | CSPR/USD | 54.242 | 0.0017186 | +0.17% | 1.48x |
| 6 | SENT/USD | 53.698 | 0.021285 | -0.22% | 1.19x |
| 7 | AKT/USD | 47.462 | 0.5368 | -1.39% | 2.78x |
| 8 | SKR/USD | 46.919 | 0.010029 | -0.10% | 1.30x |
| 9 | ALEO/USD | 46.874 | 0.03109 | +0.16% | 1.02x |
| 10 | PUMP/USD | 42.031 | 0.002615 | +0.11% | 2.54x |
| 11 | SYRUP/USD | 40.238 | 0.09685 | -0.46% | 0.28x |
| 12 | USELESS/USD | 39.868 | 0.09762 | -1.00% | 0.97x |

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

- Persisted scans: 862; predictions: 7480; observations: 520929.
- Matured sampled outcomes across 1/6/24/48h: 7727; gap abstentions: 15694. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44619292808 · **Generation:** 862 · **Legacy run:** 44619292808
**Main quote time:** 2026-11-19T21:30:33.190100+00:00 · **Legacy report time:** 2026-11-19T21:31:15.424558+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.038 | 70.94 | -0.41% | 1.84x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 2 | MEGA/USD | 0.05965 | 61.37 | +0.84% | 0.25x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 3 | CSPR/USD ⭐ | 0.0017186 | 59.92 | +0.17% | 1.48x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 4 | BMT/USD | 0.02004 | 59.84 | -0.45% | 0.27x | WEAK 35/100 | EXTREME 88/100 | Do nothing |
| 5 | PUMP/USD | 0.002615 | 57.61 | +0.11% | 2.54x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | AKT/USD | 0.5368 | 55.50 | -1.39% | 2.78x | MODERATE 48/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | LUNA/USD | 4.82e-05 | 54.81 | -1.10% | 0.63x | WEAK 17/100 | EXTREME 92/100 | Do nothing |
| 8 | SENT/USD | 0.021285 | 54.48 | -0.22% | 1.19x | WEAK 37/100 | VERY_HIGH 73/100 | Watch |
| 9 | SKR/USD | 0.010029 | 49.39 | -0.10% | 1.30x | WEAK 25/100 | EXTREME 85/100 | Do nothing |
| 10 | ALEO/USD ⭐ | 0.03109 | 47.83 | +0.16% | 1.02x | WEAK 44/100 | VERY_HIGH 74/100 | Watch |
| 11 | USELESS/USD | 0.09762 | 34.51 | -1.00% | 0.97x | WEAK 12/100 | VERY_HIGH 84/100 | Do nothing |
| 12 | SYRUP/USD | 0.09685 | 30.75 | -0.46% | 0.28x | WEAK 15/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CSPR/USD ⭐ | 0.0017109 | 73.57 | +0.17% | 1.48x | 5745 | STRONG 72/100 | VERY_HIGH 72/100 | Watch |
| 2 | ALEO/USD ⭐ | 0.03102 | 69.38 | +0.16% | 1.02x | 11012 | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** CSPR/USD, ALEO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
