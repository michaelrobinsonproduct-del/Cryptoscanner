# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:20:03.155722+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44243462818
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 34602c2d09e9a3ce4a1bdb6e1a70e100f7785cfe (atomic ledger/results publication)
**Ledger generation:** 541 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019473 | 77.032 | 57.009 | +4.31% | +1.00% | 2.74x | 8.2 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | STRONG 94/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | UP/USD | 0.05502 | 57.635 | 56.285 | +3.83% | -0.70% | 1.49x | 5.5 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | MODERATE 49/100 | HIGH 66/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.8374 | 46.474 | 35.801 | +1.49% | -0.87% | 6.69x | 19.0 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | CC/USD | 0.08358 | 42.754 | 46.193 | +1.77% | +0.35% | 0.48x | 3.6 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | XDC/USD | 0.0308 | 35.008 | 44.040 | +1.58% | -0.52% | 0.36x | 9.8 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | MEGA/USD | 0.0518 | 31.693 | 19.953 | +0.31% | -0.65% | 4.46x | 27.0 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | WEAK 36/100 | EXTREME 85/100 | Do nothing | WATCH |
| 7 | MELANIA/USD | 0.0497 | 30.302 | 25.051 | +2.05% | +0.20% | 1.42x | 40.2 | 2026-11-18T05:19:57.340144+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 57.009 | 0.019473 | +1.00% | 2.74x |
| 2 | UP/USD | 56.285 | 0.05502 | -0.70% | 1.49x |
| 3 | CC/USD | 46.193 | 0.08358 | +0.35% | 0.48x |
| 4 | XDC/USD | 44.040 | 0.0308 | -0.52% | 0.36x |
| 5 | PEARL/USD | 35.801 | 1.8374 | -0.87% | 6.69x |
| 6 | MELANIA/USD | 25.051 | 0.0497 | +0.20% | 1.42x |
| 7 | MEGA/USD | 19.953 | 0.0518 | -0.65% | 4.46x |

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

- Persisted scans: 541; predictions: 4567; observations: 326476.
- Matured sampled outcomes across 1/6/24/48h: 3666; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44243462818 · **Generation:** 541 · **Legacy run:** 44243462818
**Main quote time:** 2026-11-18T05:20:03.155722+00:00 · **Legacy report time:** 2026-11-18T05:20:18.805017+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019473 | 77.03 | +1.00% | 2.74x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 2 | UP/USD | 0.05502 | 57.63 | -0.70% | 1.49x | MODERATE 49/100 | HIGH 66/100 | Watch |
| 3 | PEARL/USD | 1.8374 | 46.47 | -0.87% | 6.69x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 4 | CC/USD | 0.08358 | 42.75 | +0.35% | 0.48x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 5 | XDC/USD | 0.0308 | 35.01 | -0.52% | 0.36x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | MEGA/USD | 0.0518 | 31.69 | -0.65% | 4.46x | WEAK 36/100 | EXTREME 85/100 | Do nothing |
| 7 | MELANIA/USD ⭐ | 0.0497 | 30.30 | +0.20% | 1.42x | MODERATE 55/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MELANIA/USD ⭐ | 0.0497 | 32.95 | +0.20% | 1.42x | 664 | MODERATE 61/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** MELANIA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
