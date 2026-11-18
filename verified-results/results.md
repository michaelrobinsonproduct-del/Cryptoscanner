# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:15:20.303402+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44221789708
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 079a5248b354b6f012f2297e5ff0eeff2d7312c3 (atomic ledger/results publication)
**Ledger generation:** 504 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 22s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.8465 | 65.955 | 38.268 | +1.99% | +2.54% | 4.28x | 22.3 | 2026-11-18T02:14:58.485585+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5211 | 64.263 | 47.616 | +2.32% | +0.33% | 2.66x | 1.9 | 2026-11-18T02:14:58.485585+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 3 | TON/USD | 1.09 | 60.178 | 42.873 | +1.21% | +0.46% | 11.16x | 9.2 | 2026-11-18T02:14:58.485585+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UP/USD | 0.05535 | 56.597 | 59.938 | +4.45% | +0.16% | 0.58x | 5.4 | 2026-11-18T02:14:58.485585+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SENT/USD | 0.01879 | 37.629 | 31.134 | +0.65% | +0.71% | 1.29x | 8.5 | 2026-11-18T02:14:58.485585+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 6 | CAP/USD | 0.101412 | 22.115 | 33.135 | +0.43% | -0.50% | 0.15x | 4.6 | 2026-11-18T02:14:58.485585+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 59.938 | 0.05535 | +0.16% | 0.58x |
| 2 | AKT/USD | 47.616 | 0.5211 | +0.33% | 2.66x |
| 3 | TON/USD | 42.873 | 1.09 | +0.46% | 11.16x |
| 4 | PEARL/USD | 38.268 | 1.8465 | +2.54% | 4.28x |
| 5 | CAP/USD | 33.135 | 0.101412 | -0.50% | 0.15x |
| 6 | SENT/USD | 31.134 | 0.01879 | +0.71% | 1.29x |

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

- Persisted scans: 504; predictions: 4298; observations: 303943.
- Matured sampled outcomes across 1/6/24/48h: 3463; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44221789708 · **Generation:** 504 · **Legacy run:** 44221789708
**Main quote time:** 2026-11-18T02:15:20.303402+00:00 · **Legacy report time:** 2026-11-18T02:15:32.586696+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8465 | 65.95 | +2.54% | 4.28x | STRONG 88/100 | VERY_HIGH 72/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5211 | 64.26 | +0.33% | 2.66x | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 3 | TON/USD ⭐ | 1.09 | 60.18 | +0.46% | 11.16x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | UP/USD | 0.05535 | 56.60 | +0.16% | 0.58x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 5 | SENT/USD ⭐ | 0.01879 | 37.63 | +0.71% | 1.29x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 6 | CAP/USD | 0.101412 | 22.12 | -0.50% | 0.15x | WEAK 16/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5219 | 74.06 | +0.60% | 3.18x | 3626 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.8465 | 64.91 | +2.59% | 5.15x | 4360 | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 3 | TON/USD ⭐ | 1.089 | 44.21 | +0.83% | 1.24x | 5401 | MODERATE 67/100 | HIGH 62/100 | Watch |
| 4 | SENT/USD ⭐ | 0.018766 | 34.27 | +0.71% | 1.29x | 3817 | MODERATE 62/100 | HIGH 67/100 | Watch |

**Same-run overlap:** PEARL/USD, AKT/USD, TON/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
