# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T09:02:01.308352+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45143085432
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8c3ce057d9f889d34ec1956c42532a566e15680c (atomic ledger/results publication)
**Ledger generation:** 1408 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.07929 | 85.363 | 66.801 | +5.12% | +0.71% | 14.32x | 6.3 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | STRONG 98/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | PEARL/USD | 2.2438 | 84.354 | 79.524 | +9.22% | +2.23% | 0.37x | 16.1 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | QNT/USD | 148.33 | 82.774 | 65.436 | +3.41% | +0.47% | 2.58x | 5.4 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 63.53 | 74.824 | 59.431 | +0.75% | +0.08% | 4.20x | 1.6 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 72.31 | 68.806 | 70.959 | +2.38% | -0.03% | 0.80x | 1.4 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 6 | JUP/USD | 0.24211 | 64.093 | 73.858 | +7.81% | -1.06% | 0.55x | 12.0 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | WEAK 32/100 | EXTREME 91/100 | Do nothing | WATCH |
| 7 | XMR/USD | 501.85 | 63.935 | 60.466 | +1.65% | +0.44% | 1.13x | 12.1 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | MODERATE 62/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6664 | 62.707 | 65.673 | +1.63% | -0.01% | 0.71x | 1.5 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93895 | 60.685 | 63.238 | +1.23% | +0.07% | 0.71x | 0.7 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | GBP/USD | 1.31281 | 60.624 | 56.989 | +0.29% | -0.05% | 1.39x | 0.1 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 11 | PAXG/USD | 3599.32 | 55.571 | 49.980 | +0.76% | +0.01% | 1.55x | 1.0 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XLM/USD | 0.12817 | 55.197 | 57.532 | +0.50% | -0.09% | 0.81x | 0.9 | 2026-11-23T09:01:52.388584+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 79.524 | 2.2438 | +2.23% | 0.37x |
| 2 | JUP/USD | 73.858 | 0.24211 | -1.06% | 0.55x |
| 3 | SOL/USD | 70.959 | 72.31 | -0.03% | 0.80x |
| 4 | ALGO/USD | 66.801 | 0.07929 | +0.71% | 14.32x |
| 5 | SUI/USD | 65.673 | 0.6664 | -0.01% | 0.71x |
| 6 | QNT/USD | 65.436 | 148.33 | +0.47% | 2.58x |
| 7 | XRP/USD | 63.238 | 0.93895 | +0.07% | 0.71x |
| 8 | XMR/USD | 60.466 | 501.85 | +0.44% | 1.13x |
| 9 | HYPE/USD | 59.431 | 63.53 | +0.08% | 4.20x |
| 10 | XLM/USD | 57.532 | 0.12817 | -0.09% | 0.81x |
| 11 | GBP/USD | 56.989 | 1.31281 | -0.05% | 1.39x |
| 12 | PAXG/USD | 49.980 | 3599.32 | +0.01% | 1.55x |

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

- Persisted scans: 1408; predictions: 11663; observations: 852575.
- Matured sampled outcomes across 1/6/24/48h: 19068; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
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

**Writer:** 45143085432 · **Generation:** 1408 · **Legacy run:** 45143085432
**Main quote time:** 2026-11-23T09:02:01.308352+00:00 · **Legacy report time:** 2026-11-23T09:03:10.799836+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.07929 | 85.36 | +0.71% | 14.32x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | PEARL/USD | 2.2438 | 84.35 | +2.23% | 0.37x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 3 | QNT/USD ⭐ | 148.33 | 82.77 | +0.47% | 2.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD | 63.53 | 74.82 | +0.08% | 4.20x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 72.31 | 68.81 | -0.03% | 0.80x | WEAK 39/100 | HIGH 68/100 | Watch |
| 6 | JUP/USD | 0.24211 | 64.09 | -1.06% | 0.55x | WEAK 32/100 | EXTREME 91/100 | Do nothing |
| 7 | XMR/USD ⭐ | 501.85 | 63.94 | +0.44% | 1.13x | STRONG 72/100 | HIGH 68/100 | Watch |
| 8 | SUI/USD | 0.6664 | 62.71 | -0.01% | 0.71x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | XRP/USD | 0.93895 | 60.69 | +0.07% | 0.71x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | GBP/USD | 1.31281 | 60.62 | -0.05% | 1.39x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 11 | PAXG/USD | 3599.32 | 55.57 | +0.01% | 1.55x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 12 | XLM/USD | 0.12817 | 55.20 | -0.09% | 0.81x | WEAK 33/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.07958 | 80.54 | +0.71% | 14.32x | 2389 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | QNT/USD ⭐ | 148.33 | 79.17 | +0.47% | 2.58x | 4679 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD ⭐ | 502.11 | 64.68 | +0.44% | 1.13x | 8514 | STRONG 77/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ALGO/USD, QNT/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
