# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:35:17.130622+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44360202138
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ebec57b373fda2102c09daf88052404bbb3ff2ad (atomic ledger/results publication)
**Ledger generation:** 625 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020045 | 89.868 | 70.578 | +7.37% | +1.71% | 2.08x | 11.0 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.04993 | 75.056 | 72.566 | +5.90% | +1.94% | 0.28x | 2.0 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04531 | 69.647 | 48.861 | +0.94% | +2.46% | 1.85x | 13.2 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05382 | 58.109 | 51.449 | +4.22% | +0.71% | 1.31x | 18.5 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | XRP/USD | 0.98507 | 58.039 | 56.404 | +0.26% | +0.91% | 0.71x | 0.8 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | CC/USD | 0.08328 | 46.809 | 35.174 | +1.40% | +1.06% | 1.63x | 20.5 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06086 | 46.614 | 35.826 | +1.55% | +1.10% | 1.53x | 13.1 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | MNT/USD | 0.3857 | 45.085 | 48.591 | +3.32% | -0.21% | 0.75x | 13.0 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 9 | XPL/USD | 0.0469 | 41.592 | 30.265 | +1.08% | +0.86% | 1.70x | 21.3 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | W/USD | 0.00903 | 34.283 | 28.081 | +1.12% | +1.46% | 0.89x | 22.2 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | WEAK 37/100 | EXTREME 86/100 | Do nothing | WATCH |
| 11 | AKT/USD | 0.5126 | 26.855 | 29.726 | +0.65% | +1.04% | 0.19x | 13.7 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | AKE/USD | 0.01003651 | 19.698 | 24.451 | +0.52% | -0.05% | 0.55x | 25.5 | 2026-11-18T17:35:11.373920+00:00 | Not calibrated | WEAK 5/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TRUST/USD | 72.566 | 0.04993 | +1.94% | 0.28x |
| 2 | SENT/USD | 70.578 | 0.020045 | +1.71% | 2.08x |
| 3 | XRP/USD | 56.404 | 0.98507 | +0.91% | 0.71x |
| 4 | MEGA/USD | 51.449 | 0.05382 | +0.71% | 1.31x |
| 5 | NIGHT/USD | 48.861 | 0.04531 | +2.46% | 1.85x |
| 6 | MNT/USD | 48.591 | 0.3857 | -0.21% | 0.75x |
| 7 | ZAMA/USD | 35.826 | 0.06086 | +1.10% | 1.53x |
| 8 | CC/USD | 35.174 | 0.08328 | +1.06% | 1.63x |
| 9 | XPL/USD | 30.265 | 0.0469 | +0.86% | 1.70x |
| 10 | AKT/USD | 29.726 | 0.5126 | +1.04% | 0.19x |
| 11 | W/USD | 28.081 | 0.00903 | +1.46% | 0.89x |
| 12 | AKE/USD | 24.451 | 0.01003651 | -0.05% | 0.55x |

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

- Persisted scans: 625; predictions: 5336; observations: 377632.
- Matured sampled outcomes across 1/6/24/48h: 4634; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44360202138 · **Generation:** 625 · **Legacy run:** 44360202138
**Main quote time:** 2026-11-18T17:35:17.130622+00:00 · **Legacy report time:** 2026-11-18T17:35:47.297227+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020045 | 89.87 | +1.71% | 2.08x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | TRUST/USD | 0.04993 | 75.06 | +1.94% | 0.28x | MODERATE 68/100 | VERY_HIGH 75/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04531 | 69.65 | +2.46% | 1.85x | STRONG 85/100 | HIGH 61/100 | Consider small entry |
| 4 | MEGA/USD ⭐ | 0.05382 | 58.11 | +0.71% | 1.31x | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 5 | XRP/USD | 0.98507 | 58.04 | +0.91% | 0.71x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | CC/USD ⭐ | 0.08328 | 46.81 | +1.06% | 1.63x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 7 | ZAMA/USD ⭐ | 0.06086 | 46.61 | +1.10% | 1.53x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 8 | MNT/USD | 0.3857 | 45.09 | -0.21% | 0.75x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |
| 9 | XPL/USD | 0.0469 | 41.59 | +0.86% | 1.70x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 10 | W/USD | 0.00903 | 34.28 | +1.46% | 0.89x | WEAK 37/100 | EXTREME 86/100 | Do nothing |
| 11 | AKT/USD | 0.5126 | 26.85 | +1.04% | 0.19x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 12 | AKE/USD | 0.01003651 | 19.70 | -0.05% | 0.55x | WEAK 5/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020025 | 80.06 | +1.71% | 2.08x | 5986 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05398 | 62.05 | +0.71% | 1.31x | 1198 | STRONG 76/100 | VERY_HIGH 79/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04522 | 52.94 | +2.46% | 1.85x | 16215 | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 4 | ZAMA/USD ⭐ | 0.06077 | 45.15 | +1.10% | 1.53x | 2996 | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD ⭐ | 0.08293 | 43.27 | +1.06% | 1.63x | 5037 | STRONG 77/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SENT/USD, NIGHT/USD, MEGA/USD, CC/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
