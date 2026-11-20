# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T03:20:33.837249+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44666951443
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 40f6f0e0e01aba8a9a78941a180b9d1abcb11284 (atomic ledger/results publication)
**Ledger generation:** 914 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XBT/USD | 62163.9 | 73.991 | 57.823 | +0.40% | +0.23% | 2.79x | 0.0 | 2026-11-20T03:20:30.407102+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PROS/USD | 0.5856 | 66.056 | 67.235 | +8.71% | +1.40% | 0.18x | 17.3 | 2026-11-20T03:20:30.407102+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | SAPIEN/USD | 0.04157 | 46.818 | 51.718 | +3.51% | -0.57% | 0.80x | 7.2 | 2026-11-20T03:20:30.407102+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04528 | 39.574 | 42.471 | +1.16% | +0.71% | 0.35x | 13.3 | 2026-11-20T03:20:30.407102+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | BMT/USD | 0.02103 | 33.490 | 50.397 | +4.73% | -2.23% | 0.42x | 28.4 | 2026-11-20T03:20:30.407102+00:00 | Not calibrated | WEAK 12/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.428 | 27.788 | 31.461 | +0.45% | -0.05% | 0.66x | 18.7 | 2026-11-20T03:20:30.407102+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 67.235 | 0.5856 | +1.40% | 0.18x |
| 2 | XBT/USD | 57.823 | 62163.9 | +0.23% | 2.79x |
| 3 | SAPIEN/USD | 51.718 | 0.04157 | -0.57% | 0.80x |
| 4 | BMT/USD | 50.397 | 0.02103 | -2.23% | 0.42x |
| 5 | NIGHT/USD | 42.471 | 0.04528 | +0.71% | 0.35x |
| 6 | ICNT/USD | 31.461 | 0.428 | -0.05% | 0.66x |

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

- Persisted scans: 914; predictions: 7902; observations: 552267.
- Matured sampled outcomes across 1/6/24/48h: 9005; gap abstentions: 16519. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44666951443 · **Generation:** 914 · **Legacy run:** 44666951443
**Main quote time:** 2026-11-20T03:20:33.837249+00:00 · **Legacy report time:** 2026-11-20T03:21:38.075474+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 62163.9 | 73.99 | +0.23% | 2.79x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PROS/USD | 0.5856 | 66.06 | +1.40% | 0.18x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 3 | SAPIEN/USD | 0.04157 | 46.82 | -0.57% | 0.80x | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing |
| 4 | NIGHT/USD | 0.04528 | 39.57 | +0.71% | 0.35x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | BMT/USD | 0.02103 | 33.49 | -2.23% | 0.42x | WEAK 12/100 | EXTREME 100/100 | Do nothing |
| 6 | ICNT/USD | 0.428 | 27.79 | -0.05% | 0.66x | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 62069.2 | 61.68 | +0.23% | 2.79x | 145120 | STRONG 96/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
