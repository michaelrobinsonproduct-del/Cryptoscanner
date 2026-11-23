# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T09:11:52.608592+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45144514804
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4b91ab047b8ad0936f7f6616aa63f2d023543ec3 (atomic ledger/results publication)
**Ledger generation:** 1409 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 149.84 | 91.106 | 73.065 | +4.46% | +1.05% | 2.28x | 5.3 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ALGO/USD | 0.07939 | 87.306 | 67.758 | +5.25% | +0.91% | 4.16x | 6.3 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | STRONG 99/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | PEARL/USD | 2.2576 | 81.219 | 78.905 | +9.89% | +2.25% | 0.10x | 17.3 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.59 | 74.704 | 59.310 | +0.84% | +0.08% | 3.40x | 3.1 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | JUP/USD | 0.24202 | 73.922 | 71.632 | +7.77% | +0.15% | 1.15x | 16.6 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6691 | 73.564 | 68.558 | +2.04% | +0.16% | 1.42x | 1.5 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 72.45 | 73.099 | 72.347 | +2.58% | +0.04% | 1.05x | 1.4 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 8 | NEAR/USD | 2.9996 | 71.871 | 57.369 | +0.60% | -0.04% | 2.47x | 3.7 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6728 | 60.843 | 45.471 | +1.82% | +0.07% | 12.96x | 1.5 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 10 | XMR/USD | 502.87 | 60.772 | 63.512 | +1.86% | +0.44% | 0.51x | 9.0 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128488 | 59.097 | 58.934 | +0.75% | +0.15% | 0.94x | 1.8 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 61483.8 | 56.930 | 58.582 | +0.51% | +0.15% | 0.76x | 0.0 | 2026-11-23T09:11:43.922632+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 78.905 | 2.2576 | +2.25% | 0.10x |
| 2 | QNT/USD | 73.065 | 149.84 | +1.05% | 2.28x |
| 3 | SOL/USD | 72.347 | 72.45 | +0.04% | 1.05x |
| 4 | JUP/USD | 71.632 | 0.24202 | +0.15% | 1.15x |
| 5 | SUI/USD | 68.558 | 0.6691 | +0.16% | 1.42x |
| 6 | ALGO/USD | 67.758 | 0.07939 | +0.91% | 4.16x |
| 7 | XMR/USD | 63.512 | 502.87 | +0.44% | 0.51x |
| 8 | HYPE/USD | 59.310 | 63.59 | +0.08% | 3.40x |
| 9 | XLM/USD | 58.934 | 0.128488 | +0.15% | 0.94x |
| 10 | XBT/USD | 58.582 | 61483.8 | +0.15% | 0.76x |
| 11 | NEAR/USD | 57.369 | 2.9996 | -0.04% | 2.47x |
| 12 | DOT/USD | 45.471 | 0.6728 | +0.07% | 12.96x |

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

- Persisted scans: 1409; predictions: 11675; observations: 853184.
- Matured sampled outcomes across 1/6/24/48h: 19100; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45144514804 · **Generation:** 1409 · **Legacy run:** 45144514804
**Main quote time:** 2026-11-23T09:11:52.608592+00:00 · **Legacy report time:** 2026-11-23T09:12:43.001189+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 149.84 | 91.11 | +1.05% | 2.28x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.07939 | 87.31 | +0.91% | 4.16x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | PEARL/USD | 2.2576 | 81.22 | +2.25% | 0.10x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 4 | HYPE/USD | 63.59 | 74.70 | +0.08% | 3.40x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | JUP/USD ⭐ | 0.24202 | 73.92 | +0.15% | 1.15x | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |
| 6 | SUI/USD ⭐ | 0.6691 | 73.56 | +0.16% | 1.42x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 72.45 | 73.10 | +0.04% | 1.05x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 8 | NEAR/USD | 2.9996 | 71.87 | -0.04% | 2.47x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | DOT/USD | 0.6728 | 60.84 | +0.07% | 12.96x | STRONG 75/100 | HIGH 60/100 | Watch |
| 10 | XMR/USD | 502.87 | 60.77 | +0.44% | 0.51x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | XLM/USD | 0.128488 | 59.10 | +0.15% | 0.94x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 61483.8 | 56.93 | +0.15% | 0.76x | MODERATE 48/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 149.8 | 99.30 | +1.05% | 2.28x | 4750 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.0794 | 81.49 | +0.91% | 4.16x | 2432 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | JUP/USD ⭐ | 0.24146 | 77.42 | +0.15% | 1.15x | 3506 | STRONG 74/100 | HIGH 67/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6691 | 75.70 | +0.16% | 1.42x | 6467 | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | ADA/USD | 0.146702 | 63.32 | +0.21% | 1.54x | 7494 | STRONG 77/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, ALGO/USD, JUP/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
