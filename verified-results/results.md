# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T18:21:34.195960+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45054420452
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 007025d2b28c3d8f697c3f04931c3c2845b20074 (atomic ledger/results publication)
**Ledger generation:** 1319 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.867 | 101.986 | 77.346 | +3.88% | +1.93% | 5.00x | 9.7 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 62.66 | 81.477 | 70.433 | +2.32% | -0.21% | 2.21x | 1.6 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9988 | 80.799 | 80.617 | +3.90% | -0.33% | 1.18x | 3.3 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002538 | 80.518 | 79.785 | +8.28% | +0.04% | 1.05x | 11.8 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | MODERATE 60/100 | HIGH 68/100 | Watch | WATCH |
| 5 | DRV/USD | 0.36735 | 79.986 | 84.453 | +9.59% | +0.17% | 0.47x | 9.3 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.629 | 70.500 | 70.264 | +6.64% | -1.65% | 1.85x | 30.4 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 7 | ETH/USD | 1711.78 | 65.876 | 67.246 | +1.75% | -0.04% | 0.88x | 0.1 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 791.19 | 58.624 | 64.690 | +1.67% | -0.43% | 0.61x | 4.0 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6562 | 57.840 | 63.100 | +1.37% | -0.18% | 0.57x | 3.0 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60648.4 | 57.465 | 61.498 | +0.93% | -0.15% | 0.67x | 0.0 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | LINK/USD | 8.80954 | 57.033 | 60.854 | +2.50% | -0.08% | 0.66x | 3.4 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | WLD/USD | 0.2355 | 45.431 | 54.918 | +3.43% | -0.34% | 0.22x | 4.2 | 2026-11-22T18:21:25.846269+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 84.453 | 0.36735 | +0.17% | 0.47x |
| 2 | NEAR/USD | 80.617 | 2.9988 | -0.33% | 1.18x |
| 3 | PUMP/USD | 79.785 | 0.002538 | +0.04% | 1.05x |
| 4 | VVV/USD | 77.346 | 25.867 | +1.93% | 5.00x |
| 5 | HYPE/USD | 70.433 | 62.66 | -0.21% | 2.21x |
| 6 | PIEVERSE/USD | 70.264 | 3.629 | -1.65% | 1.85x |
| 7 | ETH/USD | 67.246 | 1711.78 | -0.04% | 0.88x |
| 8 | ZEC/USD | 64.690 | 791.19 | -0.43% | 0.61x |
| 9 | SUI/USD | 63.100 | 0.6562 | -0.18% | 0.57x |
| 10 | XBT/USD | 61.498 | 60648.4 | -0.15% | 0.67x |
| 11 | LINK/USD | 60.854 | 8.80954 | -0.08% | 0.66x |
| 12 | WLD/USD | 54.918 | 0.2355 | -0.34% | 0.22x |

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

- Persisted scans: 1319; predictions: 10747; observations: 798379.
- Matured sampled outcomes across 1/6/24/48h: 16066; gap abstentions: 22336. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45054420452 · **Generation:** 1319 · **Legacy run:** 45054420452
**Main quote time:** 2026-11-22T18:21:34.195960+00:00 · **Legacy report time:** 2026-11-22T18:22:26.255865+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.867 | 101.99 | +1.93% | 5.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD | 62.66 | 81.48 | -0.21% | 2.21x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD | 2.9988 | 80.80 | -0.33% | 1.18x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 4 | PUMP/USD | 0.002538 | 80.52 | +0.04% | 1.05x | MODERATE 60/100 | HIGH 68/100 | Watch |
| 5 | DRV/USD | 0.36735 | 79.99 | +0.17% | 0.47x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 6 | PIEVERSE/USD | 3.629 | 70.50 | -1.65% | 1.85x | MODERATE 45/100 | VERY_HIGH 77/100 | Do nothing |
| 7 | ETH/USD | 1711.78 | 65.88 | -0.04% | 0.88x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD | 791.19 | 58.62 | -0.43% | 0.61x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SUI/USD | 0.6562 | 57.84 | -0.18% | 0.57x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XBT/USD | 60648.4 | 57.47 | -0.15% | 0.67x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | LINK/USD | 8.80954 | 57.03 | -0.08% | 0.66x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | WLD/USD | 0.2355 | 45.43 | -0.34% | 0.22x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.896 | 100.00 | +1.93% | 5.00x | 12410 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEARL/USD | 2.0152 | 75.89 | +1.51% | 1.42x | 6121 | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | ZBCN/USD | 0.001909 | 75.49 | +0.26% | 1.52x | 5759 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
