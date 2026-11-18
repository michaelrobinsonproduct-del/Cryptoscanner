# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:15:07.573785+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44242856521
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** e667feaab4feda4154b4bcfb8e51b8619bc1495c (atomic ledger/results publication)
**Ledger generation:** 540 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019508 | 78.350 | 58.328 | +4.49% | +1.00% | 2.74x | 8.2 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | STRONG 94/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | UP/USD | 0.0551 | 55.953 | 54.603 | +3.98% | -0.70% | 1.49x | 10.9 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.8329 | 54.025 | 43.352 | +1.24% | -0.87% | 6.69x | 0.5 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.0522 | 45.341 | 29.285 | +1.08% | +0.21% | 2.56x | 19.2 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.08366 | 41.651 | 45.090 | +1.86% | +0.35% | 0.48x | 7.2 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | MELANIA/USD | 0.05 | 37.833 | 29.446 | +2.67% | +0.20% | 1.74x | 40.1 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 89/100 | Do nothing | WATCH |
| 7 | XDC/USD | 0.03076 | 35.694 | 44.725 | +1.45% | -0.52% | 0.36x | 6.5 | 2026-11-18T05:15:02.398969+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 58.328 | 0.019508 | +1.00% | 2.74x |
| 2 | UP/USD | 54.603 | 0.0551 | -0.70% | 1.49x |
| 3 | CC/USD | 45.090 | 0.08366 | +0.35% | 0.48x |
| 4 | XDC/USD | 44.725 | 0.03076 | -0.52% | 0.36x |
| 5 | PEARL/USD | 43.352 | 1.8329 | -0.87% | 6.69x |
| 6 | MELANIA/USD | 29.446 | 0.05 | +0.20% | 1.74x |
| 7 | MEGA/USD | 29.285 | 0.0522 | +0.21% | 2.56x |

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

- Persisted scans: 540; predictions: 4560; observations: 325867.
- Matured sampled outcomes across 1/6/24/48h: 3666; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44242856521 · **Generation:** 540 · **Legacy run:** 44242856521
**Main quote time:** 2026-11-18T05:15:07.573785+00:00 · **Legacy report time:** 2026-11-18T05:15:29.637978+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019508 | 78.35 | +1.00% | 2.74x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | UP/USD | 0.0551 | 55.95 | -0.70% | 1.49x | WEAK 43/100 | VERY_HIGH 72/100 | Watch |
| 3 | PEARL/USD | 1.8329 | 54.02 | -0.87% | 6.69x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 4 | MEGA/USD ⭐ | 0.0522 | 45.34 | +0.21% | 2.56x | STRONG 83/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.08366 | 41.65 | +0.35% | 0.48x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 6 | MELANIA/USD ⭐ | 0.05 | 37.83 | +0.20% | 1.74x | MODERATE 59/100 | EXTREME 89/100 | Do nothing |
| 7 | XDC/USD | 0.03076 | 35.69 | -0.52% | 0.36x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019481 | 80.56 | +1.00% | 2.74x | 4266 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MELANIA/USD ⭐ | 0.05 | 41.57 | +0.20% | 1.74x | 660 | MODERATE 61/100 | EXTREME 89/100 | Do nothing |
| 3 | MEGA/USD ⭐ | 0.0522 | 31.04 | +0.21% | 2.56x | 1244 | STRONG 71/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** SENT/USD, MEGA/USD, MELANIA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
