# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:30:03.941587+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44230789058
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** b80f0d8697e750085683b43ced50f5988cf76a1d (atomic ledger/results publication)
**Ledger generation:** 519 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 513.9 | 72.912 | 52.643 | +0.99% | +1.05% | 9.17x | 18.5 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | PIEVERSE/USD | 2.1742 | 55.438 | 56.567 | +6.13% | +0.75% | 0.51x | 36.4 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | TON/USD | 1.08 | 49.659 | 36.256 | +0.28% | +0.09% | 2.29x | 9.3 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06039 | 47.933 | 31.355 | +0.77% | +0.32% | 4.39x | 14.9 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.8305 | 40.032 | 34.475 | +1.10% | +1.11% | 1.00x | 17.0 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | CC/USD | 0.08342 | 36.865 | 43.114 | +1.57% | -0.02% | 0.39x | 6.0 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | ICNT/USD | 0.2804 | 33.970 | 34.271 | +1.56% | -1.09% | 1.52x | 17.8 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5173 | 32.621 | 41.443 | +1.57% | -0.71% | 0.47x | 3.9 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | SENT/USD | 0.018727 | 22.921 | 29.013 | +0.31% | -0.11% | 0.45x | 8.0 | 2026-11-18T03:29:59.308078+00:00 | Not calibrated | WEAK 16/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 56.567 | 2.1742 | +0.75% | 0.51x |
| 2 | XMR/USD | 52.643 | 513.9 | +1.05% | 9.17x |
| 3 | CC/USD | 43.114 | 0.08342 | -0.02% | 0.39x |
| 4 | AKT/USD | 41.443 | 0.5173 | -0.71% | 0.47x |
| 5 | TON/USD | 36.256 | 1.08 | +0.09% | 2.29x |
| 6 | PEARL/USD | 34.475 | 1.8305 | +1.11% | 1.00x |
| 7 | ICNT/USD | 34.271 | 0.2804 | -1.09% | 1.52x |
| 8 | ZAMA/USD | 31.355 | 0.06039 | +0.32% | 4.39x |
| 9 | SENT/USD | 29.013 | 0.018727 | -0.11% | 0.45x |

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

- Persisted scans: 519; predictions: 4388; observations: 313078.
- Matured sampled outcomes across 1/6/24/48h: 3514; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44230789058 · **Generation:** 519 · **Legacy run:** 44230789058
**Main quote time:** 2026-11-18T03:30:03.941587+00:00 · **Legacy report time:** 2026-11-18T03:30:16.854131+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 513.9 | 72.91 | +1.05% | 9.17x | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 2 | PIEVERSE/USD | 2.1742 | 55.44 | +0.75% | 0.51x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 3 | TON/USD ⭐ | 1.08 | 49.66 | +0.09% | 2.29x | STRONG 80/100 | HIGH 55/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.06039 | 47.93 | +0.32% | 4.39x | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 5 | PEARL/USD ⭐ | 1.8305 | 40.03 | +1.11% | 1.00x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 6 | CC/USD | 0.08342 | 36.87 | -0.02% | 0.39x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | ICNT/USD | 0.2804 | 33.97 | -1.09% | 1.52x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKT/USD | 0.5173 | 32.62 | -0.71% | 0.47x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | SENT/USD | 0.018727 | 22.92 | -0.11% | 0.45x | WEAK 16/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 513.04 | 58.88 | +1.36% | 9.41x | 13187 | STRONG 89/100 | HIGH 61/100 | Consider small entry |
| 2 | ZAMA/USD ⭐ | 0.06047 | 43.82 | +0.32% | 4.39x | 4484 | STRONG 82/100 | HIGH 66/100 | Consider small entry |
| 3 | PEARL/USD ⭐ | 1.8305 | 41.73 | +1.11% | 1.00x | 4235 | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 4 | TON/USD ⭐ | 1.08 | 36.16 | +0.09% | 2.29x | 5395 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD, TON/USD, ZAMA/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
