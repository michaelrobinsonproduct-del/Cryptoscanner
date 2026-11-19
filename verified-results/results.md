# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T21:05:42.205053+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44615078322
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 270e059a26ac7d345e8ba6b579de9ea1ecc0f0fb (atomic ledger/results publication)
**Ledger generation:** 859 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 601; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALEO/USD | 0.03113 | 84.567 | 63.374 | +3.84% | +1.24% | 3.48x | 3.2 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SYRUP/USD | 0.09617 | 72.708 | 34.647 | +1.27% | +4.61% | 10.07x | 11.4 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | STRONG 86/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5437 | 72.184 | 60.564 | +4.96% | -0.68% | 2.90x | 12.9 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05945 | 60.117 | 67.735 | +6.16% | -0.37% | 0.42x | 15.2 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | USELESS/USD | 0.09843 | 58.338 | 53.752 | +3.00% | -0.14% | 1.53x | 11.2 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | WEAK 44/100 | HIGH 67/100 | Watch | WATCH |
| 6 | WINGS/USD | 0.001957 | 56.392 | 49.386 | +2.89% | -0.46% | 1.93x | 5.1 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | MODERATE 48/100 | HIGH 66/100 | Watch | WATCH |
| 7 | BLESS/USD | 0.011623 | 56.363 | 38.071 | +2.74% | +1.45% | 2.10x | 25.9 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | SKR/USD | 0.010067 | 55.853 | 58.200 | +4.51% | -0.46% | 1.00x | 8.9 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | VVV/USD | 22.05 | 54.530 | 63.839 | +1.75% | -0.72% | 0.43x | 6.8 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | GRASS/USD | 0.4225 | 53.831 | 57.208 | +4.27% | +0.14% | 0.59x | 14.3 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | PUMP/USD | 0.002621 | 53.022 | 41.813 | +0.96% | -0.76% | 4.28x | 15.3 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 12 | CSPR/USD | 0.0017298 | 52.867 | 64.342 | +5.92% | -1.33% | 0.52x | 18.0 | 2026-11-19T21:05:34.903944+00:00 | Not calibrated | WEAK 26/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 67.735 | 0.05945 | -0.37% | 0.42x |
| 2 | CSPR/USD | 64.342 | 0.0017298 | -1.33% | 0.52x |
| 3 | VVV/USD | 63.839 | 22.05 | -0.72% | 0.43x |
| 4 | ALEO/USD | 63.374 | 0.03113 | +1.24% | 3.48x |
| 5 | AKT/USD | 60.564 | 0.5437 | -0.68% | 2.90x |
| 6 | SKR/USD | 58.200 | 0.010067 | -0.46% | 1.00x |
| 7 | GRASS/USD | 57.208 | 0.4225 | +0.14% | 0.59x |
| 8 | USELESS/USD | 53.752 | 0.09843 | -0.14% | 1.53x |
| 9 | WINGS/USD | 49.386 | 0.001957 | -0.46% | 1.93x |
| 10 | PUMP/USD | 41.813 | 0.002621 | -0.76% | 4.28x |
| 11 | BLESS/USD | 38.071 | 0.011623 | +1.45% | 2.10x |
| 12 | SYRUP/USD | 34.647 | 0.09617 | +4.61% | 10.07x |

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

- Persisted scans: 859; predictions: 7447; observations: 519126.
- Matured sampled outcomes across 1/6/24/48h: 7643; gap abstentions: 15680. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44615078322 · **Generation:** 859 · **Legacy run:** 44615078322
**Main quote time:** 2026-11-19T21:05:42.205053+00:00 · **Legacy report time:** 2026-11-19T21:06:28.468143+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALEO/USD | 0.03113 | 84.57 | +1.24% | 3.48x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | SYRUP/USD | 0.09617 | 72.71 | +4.61% | 10.07x | STRONG 86/100 | VERY_HIGH 83/100 | Watch |
| 3 | AKT/USD | 0.5437 | 72.18 | -0.68% | 2.90x | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |
| 4 | MEGA/USD | 0.05945 | 60.12 | -0.37% | 0.42x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 5 | USELESS/USD | 0.09843 | 58.34 | -0.14% | 1.53x | WEAK 44/100 | HIGH 67/100 | Watch |
| 6 | WINGS/USD | 0.001957 | 56.39 | -0.46% | 1.93x | MODERATE 48/100 | HIGH 66/100 | Watch |
| 7 | BLESS/USD | 0.011623 | 56.36 | +1.45% | 2.10x | STRONG 73/100 | VERY_HIGH 72/100 | Watch |
| 8 | SKR/USD | 0.010067 | 55.85 | -0.46% | 1.00x | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | VVV/USD | 22.05 | 54.53 | -0.72% | 0.43x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | GRASS/USD | 0.4225 | 53.83 | +0.14% | 0.59x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 11 | PUMP/USD | 0.002621 | 53.02 | -0.76% | 4.28x | MODERATE 52/100 | HIGH 67/100 | Watch |
| 12 | CSPR/USD | 0.0017298 | 52.87 | -1.33% | 0.52x | WEAK 26/100 | EXTREME 91/100 | Do nothing |

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
