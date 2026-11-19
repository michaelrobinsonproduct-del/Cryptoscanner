# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:15:31.617712+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44606634695
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** e3cca65a4f1e261d481372085a0afd5412ef85e7 (atomic ledger/results publication)
**Ledger generation:** 853 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.275 | 82.933 | 72.716 | +2.79% | -0.96% | 19.57x | 3.6 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5525 | 81.811 | 71.828 | +6.66% | -1.00% | 10.98x | 10.9 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ALEO/USD | 0.03149 | 78.539 | 70.143 | +5.04% | +2.04% | 0.82x | 3.2 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ADA/USD | 0.151936 | 59.314 | 56.049 | +0.45% | -0.48% | 1.57x | 4.2 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010089 | 52.879 | 57.825 | +4.73% | -0.03% | 0.52x | 12.9 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | WEAK 26/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.020999 | 50.968 | 44.048 | +1.91% | -0.52% | 1.95x | 7.1 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | MODERATE 45/100 | HIGH 66/100 | Watch | WATCH |
| 7 | PYTH/USD | 0.05342 | 46.199 | 35.560 | +1.25% | -0.87% | 3.11x | 11.2 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | INJ/USD | 7.053 | 44.034 | 48.449 | +1.03% | -0.06% | 0.59x | 7.1 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | CSPR/USD | 0.0017911 | 43.828 | 61.248 | +9.67% | -2.54% | 0.53x | 31.3 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | WEAK 17/100 | EXTREME 97/100 | Do nothing | WATCH |
| 10 | TRX/USD | 0.310131 | 41.388 | 42.971 | +0.27% | +0.00% | 0.84x | 0.0 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SHIB/USD | 3.804e-06 | 24.918 | 30.912 | +0.26% | -0.44% | 0.62x | 7.9 | 2026-11-19T20:15:25.142825+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.716 | 22.275 | -0.96% | 19.57x |
| 2 | AKT/USD | 71.828 | 0.5525 | -1.00% | 10.98x |
| 3 | ALEO/USD | 70.143 | 0.03149 | +2.04% | 0.82x |
| 4 | CSPR/USD | 61.248 | 0.0017911 | -2.54% | 0.53x |
| 5 | SKR/USD | 57.825 | 0.010089 | -0.03% | 0.52x |
| 6 | ADA/USD | 56.049 | 0.151936 | -0.48% | 1.57x |
| 7 | INJ/USD | 48.449 | 7.053 | -0.06% | 0.59x |
| 8 | SENT/USD | 44.048 | 0.020999 | -0.52% | 1.95x |
| 9 | TRX/USD | 42.971 | 0.310131 | +0.00% | 0.84x |
| 10 | PYTH/USD | 35.560 | 0.05342 | -0.87% | 3.11x |
| 11 | SHIB/USD | 30.912 | 3.804e-06 | -0.44% | 0.62x |

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

- Persisted scans: 853; predictions: 7379; observations: 515524.
- Matured sampled outcomes across 1/6/24/48h: 7439; gap abstentions: 15641. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44606634695 · **Generation:** 853 · **Legacy run:** 44606634695
**Main quote time:** 2026-11-19T20:15:31.617712+00:00 · **Legacy report time:** 2026-11-19T20:16:34.078088+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.275 | 82.93 | -0.96% | 19.57x | STRONG 71/100 | HIGH 61/100 | Watch |
| 2 | AKT/USD | 0.5525 | 81.81 | -1.00% | 10.98x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 3 | ALEO/USD | 0.03149 | 78.54 | +2.04% | 0.82x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 4 | ADA/USD | 0.151936 | 59.31 | -0.48% | 1.57x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 5 | SKR/USD | 0.010089 | 52.88 | -0.03% | 0.52x | WEAK 26/100 | EXTREME 94/100 | Do nothing |
| 6 | SENT/USD | 0.020999 | 50.97 | -0.52% | 1.95x | MODERATE 45/100 | HIGH 66/100 | Watch |
| 7 | PYTH/USD | 0.05342 | 46.20 | -0.87% | 3.11x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 8 | INJ/USD | 7.053 | 44.03 | -0.06% | 0.59x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | CSPR/USD | 0.0017911 | 43.83 | -2.54% | 0.53x | WEAK 17/100 | EXTREME 97/100 | Do nothing |
| 10 | TRX/USD | 0.310131 | 41.39 | +0.00% | 0.84x | WEAK 41/100 | HIGH 62/100 | Watch |
| 11 | SHIB/USD | 3.804e-06 | 24.92 | -0.44% | 0.62x | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing |

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
