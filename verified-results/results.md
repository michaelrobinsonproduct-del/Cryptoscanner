# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:15:25.270336+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44626721918
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** d51817d931c9499888bfcf8c21a850fb1d4d4661 (atomic ledger/results publication)
**Ledger generation:** 868 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021358 | 74.549 | 55.299 | +3.65% | +0.85% | 2.71x | 9.4 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | STRONG 92/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | MEGA/USD | 0.06016 | 70.553 | 70.527 | +7.43% | +0.69% | 0.66x | 13.3 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | SKR/USD | 0.009991 | 59.839 | 50.641 | +3.72% | +0.23% | 1.80x | 13.0 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.791e-05 | 56.853 | 64.473 | +10.04% | +0.00% | 0.24x | 35.6 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | VVV/USD | 21.833 | 52.301 | 57.944 | +0.75% | -0.07% | 0.47x | 4.6 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | SYRUP/USD | 0.09608 | 50.316 | 31.012 | +1.18% | +0.86% | 4.48x | 17.7 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | USELESS/USD | 0.09803 | 46.457 | 48.264 | +2.58% | -0.30% | 0.97x | 18.4 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 8 | XPL/USD | 0.0466 | 38.352 | 32.037 | +1.30% | +0.43% | 1.42x | 21.5 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5336 | 37.263 | 47.767 | +3.01% | -0.47% | 0.18x | 11.2 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | WEAK 19/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | BLUR/USD | 0.00666 | 36.312 | 32.302 | +1.22% | +0.30% | 1.25x | 15.0 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | ALEO/USD | 0.03091 | 33.163 | 40.134 | +3.10% | -1.31% | 0.96x | 42.2 | 2026-11-19T22:15:18.291269+00:00 | Not calibrated | WEAK 7/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 70.527 | 0.06016 | +0.69% | 0.66x |
| 2 | LUNA/USD | 64.473 | 4.791e-05 | +0.00% | 0.24x |
| 3 | VVV/USD | 57.944 | 21.833 | -0.07% | 0.47x |
| 4 | SENT/USD | 55.299 | 0.021358 | +0.85% | 2.71x |
| 5 | SKR/USD | 50.641 | 0.009991 | +0.23% | 1.80x |
| 6 | USELESS/USD | 48.264 | 0.09803 | -0.30% | 0.97x |
| 7 | AKT/USD | 47.767 | 0.5336 | -0.47% | 0.18x |
| 8 | ALEO/USD | 40.134 | 0.03091 | -1.31% | 0.96x |
| 9 | BLUR/USD | 32.302 | 0.00666 | +0.30% | 1.25x |
| 10 | XPL/USD | 32.037 | 0.0466 | +0.43% | 1.42x |
| 11 | SYRUP/USD | 31.012 | 0.09608 | +0.86% | 4.48x |

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

- Persisted scans: 868; predictions: 7544; observations: 524538.
- Matured sampled outcomes across 1/6/24/48h: 7918; gap abstentions: 15732. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44626721918 · **Generation:** 868 · **Legacy run:** 44626721918
**Main quote time:** 2026-11-19T22:15:25.270336+00:00 · **Legacy report time:** 2026-11-19T22:16:06.592603+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021358 | 74.55 | +0.85% | 2.71x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | MEGA/USD | 0.06016 | 70.55 | +0.69% | 0.66x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 3 | SKR/USD ⭐ | 0.009991 | 59.84 | +0.23% | 1.80x | STRONG 80/100 | VERY_HIGH 73/100 | Watch |
| 4 | LUNA/USD | 4.791e-05 | 56.85 | +0.00% | 0.24x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | VVV/USD | 21.833 | 52.30 | -0.07% | 0.47x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | SYRUP/USD | 0.09608 | 50.32 | +0.86% | 4.48x | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 7 | USELESS/USD | 0.09803 | 46.46 | -0.30% | 0.97x | WEAK 23/100 | VERY_HIGH 74/100 | Do nothing |
| 8 | XPL/USD | 0.0466 | 38.35 | +0.43% | 1.42x | MODERATE 54/100 | VERY_HIGH 72/100 | Watch |
| 9 | AKT/USD | 0.5336 | 37.26 | -0.47% | 0.18x | WEAK 19/100 | EXTREME 87/100 | Do nothing |
| 10 | BLUR/USD | 0.00666 | 36.31 | +0.30% | 1.25x | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |
| 11 | ALEO/USD | 0.03091 | 33.16 | -1.31% | 0.96x | WEAK 7/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021358 | 80.70 | +0.85% | 2.71x | 14805 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.009991 | 60.64 | +0.23% | 1.80x | 1375 | STRONG 85/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
