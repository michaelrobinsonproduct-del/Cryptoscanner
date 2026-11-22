# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T16:51:17.046353+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45045975392
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** a7b5e8573aa36d477b29a7eab9f3c9f45c3db524 (atomic ledger/results publication)
**Ledger generation:** 1310 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04953 | 102.793 | 88.297 | +11.86% | -0.10% | 7.08x | 10.1 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002546 | 82.466 | 81.819 | +8.62% | +0.12% | 1.01x | 7.9 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 3 | DRV/USD | 0.3623 | 82.107 | 83.694 | +8.08% | +0.01% | 0.84x | 9.9 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XBT/USD | 61166.5 | 79.753 | 67.533 | +1.79% | -0.05% | 2.25x | 0.0 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9912 | 77.718 | 78.436 | +3.63% | +0.26% | 0.80x | 4.0 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ETH/USD | 1718.9 | 74.830 | 70.209 | +2.18% | -0.01% | 1.47x | 0.1 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.96 | 71.983 | 73.073 | +2.81% | +0.08% | 0.85x | 3.2 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 8 | PEARL/USD | 2.0489 | 70.889 | 71.843 | +5.16% | +1.12% | 0.34x | 12.7 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 70.53 | 66.399 | 57.173 | +0.51% | +0.13% | 1.86x | 2.8 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 10 | BNB/USD | 558.46 | 65.959 | 50.645 | +2.02% | +0.06% | 3.66x | 1.4 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ZBCN/USD | 0.001908 | 60.734 | 68.514 | +10.48% | +0.16% | 0.14x | 21.0 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | WEAK 40/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6651 | 60.146 | 44.544 | +1.85% | +0.12% | 17.47x | 1.5 | 2026-11-22T16:51:10.438610+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.297 | 0.04953 | -0.10% | 7.08x |
| 2 | DRV/USD | 83.694 | 0.3623 | +0.01% | 0.84x |
| 3 | PUMP/USD | 81.819 | 0.002546 | +0.12% | 1.01x |
| 4 | NEAR/USD | 78.436 | 2.9912 | +0.26% | 0.80x |
| 5 | HYPE/USD | 73.073 | 62.96 | +0.08% | 0.85x |
| 6 | PEARL/USD | 71.843 | 2.0489 | +1.12% | 0.34x |
| 7 | ETH/USD | 70.209 | 1718.9 | -0.01% | 1.47x |
| 8 | ZBCN/USD | 68.514 | 0.001908 | +0.16% | 0.14x |
| 9 | XBT/USD | 67.533 | 61166.5 | -0.05% | 2.25x |
| 10 | SOL/USD | 57.173 | 70.53 | +0.13% | 1.86x |
| 11 | BNB/USD | 50.645 | 558.46 | +0.06% | 3.66x |
| 12 | DOT/USD | 44.544 | 0.6651 | +0.12% | 17.47x |

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

- Persisted scans: 1310; predictions: 10639; observations: 792898.
- Matured sampled outcomes across 1/6/24/48h: 15730; gap abstentions: 22324. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45045975392 · **Generation:** 1310 · **Legacy run:** 45045975392
**Main quote time:** 2026-11-22T16:51:17.046353+00:00 · **Legacy report time:** 2026-11-22T16:52:20.762579+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04953 | 102.79 | -0.10% | 7.08x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002546 | 82.47 | +0.12% | 1.01x | STRONG 76/100 | HIGH 62/100 | Watch |
| 3 | DRV/USD | 0.3623 | 82.11 | +0.01% | 0.84x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 4 | XBT/USD | 61166.5 | 79.75 | -0.05% | 2.25x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 2.9912 | 77.72 | +0.26% | 0.80x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 6 | ETH/USD | 1718.9 | 74.83 | -0.01% | 1.47x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | HYPE/USD | 62.96 | 71.98 | +0.08% | 0.85x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 8 | PEARL/USD | 2.0489 | 70.89 | +1.12% | 0.34x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 70.53 | 66.40 | +0.13% | 1.86x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 10 | BNB/USD | 558.46 | 65.96 | +0.06% | 3.66x | STRONG 78/100 | HIGH 55/100 | Watch |
| 11 | ZBCN/USD | 0.001908 | 60.73 | +0.16% | 0.14x | WEAK 40/100 | EXTREME 87/100 | Do nothing |
| 12 | DOT/USD | 0.6651 | 60.15 | +0.12% | 17.47x | STRONG 75/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002549 | 76.84 | +0.12% | 1.01x | 4003 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
