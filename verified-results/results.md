# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T17:01:17.449763+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45046874207
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** ad03c66653396ab1526f3c1aef1e1cf5f3e0c5de (atomic ledger/results publication)
**Ledger generation:** 1311 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002572 | 101.146 | 80.075 | +9.73% | +1.21% | 3.92x | 11.7 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.36152 | 85.012 | 88.388 | +7.85% | -0.27% | 0.80x | 0.6 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ETH/USD | 1719.55 | 75.033 | 70.479 | +2.22% | -0.03% | 1.47x | 0.1 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XBT/USD | 61131.1 | 74.823 | 67.121 | +1.73% | -0.16% | 1.85x | 0.0 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.12 | 74.749 | 74.904 | +3.07% | +0.33% | 0.82x | 3.2 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9892 | 71.516 | 78.283 | +3.57% | -0.30% | 0.47x | 3.3 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ZEC/USD | 794.57 | 68.824 | 68.054 | +2.11% | +0.14% | 1.01x | 3.4 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ZBCN/USD | 0.001905 | 67.089 | 71.347 | +10.31% | -0.05% | 0.60x | 15.7 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6589 | 61.710 | 66.785 | +1.79% | -0.24% | 0.61x | 1.5 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SOL/USD | 70.53 | 58.128 | 57.882 | +0.51% | +0.00% | 1.02x | 1.4 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.691 | 57.359 | 54.605 | +1.95% | -0.07% | 1.31x | 1.5 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 12 | ONDO/USD | 0.28529 | 55.728 | 42.876 | +1.31% | -0.01% | 2.29x | 1.8 | 2026-11-22T17:01:10.847436+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 88.388 | 0.36152 | -0.27% | 0.80x |
| 2 | PUMP/USD | 80.075 | 0.002572 | +1.21% | 3.92x |
| 3 | NEAR/USD | 78.283 | 2.9892 | -0.30% | 0.47x |
| 4 | HYPE/USD | 74.904 | 63.12 | +0.33% | 0.82x |
| 5 | ZBCN/USD | 71.347 | 0.001905 | -0.05% | 0.60x |
| 6 | ETH/USD | 70.479 | 1719.55 | -0.03% | 1.47x |
| 7 | ZEC/USD | 68.054 | 794.57 | +0.14% | 1.01x |
| 8 | XBT/USD | 67.121 | 61131.1 | -0.16% | 1.85x |
| 9 | SUI/USD | 66.785 | 0.6589 | -0.24% | 0.61x |
| 10 | SOL/USD | 57.882 | 70.53 | +0.00% | 1.02x |
| 11 | AVAX/USD | 54.605 | 6.691 | -0.07% | 1.31x |
| 12 | ONDO/USD | 42.876 | 0.28529 | -0.01% | 2.29x |

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

- Persisted scans: 1311; predictions: 10651; observations: 793507.
- Matured sampled outcomes across 1/6/24/48h: 15766; gap abstentions: 22326. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45046874207 · **Generation:** 1311 · **Legacy run:** 45046874207
**Main quote time:** 2026-11-22T17:01:17.449763+00:00 · **Legacy report time:** 2026-11-22T17:02:21.688152+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002572 | 101.15 | +1.21% | 3.92x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD | 0.36152 | 85.01 | -0.27% | 0.80x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 3 | ETH/USD | 1719.55 | 75.03 | -0.03% | 1.47x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | XBT/USD | 61131.1 | 74.82 | -0.16% | 1.85x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD | 63.12 | 74.75 | +0.33% | 0.82x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 6 | NEAR/USD | 2.9892 | 71.52 | -0.30% | 0.47x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | ZEC/USD ⭐ | 794.57 | 68.82 | +0.14% | 1.01x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 8 | ZBCN/USD | 0.001905 | 67.09 | -0.05% | 0.60x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 9 | SUI/USD | 0.6589 | 61.71 | -0.24% | 0.61x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | SOL/USD | 70.53 | 58.13 | +0.00% | 1.02x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 11 | AVAX/USD | 6.691 | 57.36 | -0.07% | 1.31x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 12 | ONDO/USD | 0.28529 | 55.73 | -0.01% | 2.29x | MODERATE 58/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002572 | 88.18 | +1.21% | 3.92x | 4028 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | PEARL/USD | 2.034 | 79.70 | +0.44% | 1.31x | 6885 | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD ⭐ | 794.15 | 70.79 | +0.14% | 1.01x | 21154 | STRONG 70/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PUMP/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
