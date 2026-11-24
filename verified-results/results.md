# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T08:31:40.325174+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45356572551
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3c7b9e2af8f309eee712fe2598b2283c3f6cf502 (atomic ledger/results publication)
**Ledger generation:** 1550 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.535e-06 | 86.126 | 70.702 | +3.30% | +0.08% | 4.09x | 5.7 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 2 | BABY/USD | 0.00911 | 85.585 | 71.685 | +7.18% | -0.22% | 7.81x | 11.0 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | XMR/USD | 495.72 | 80.117 | 65.742 | +2.00% | -0.12% | 3.90x | 6.5 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 25.241 | 65.192 | 73.540 | +3.24% | -0.09% | 0.21x | 8.3 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | LINK/USD | 9.04474 | 52.111 | 56.397 | +0.44% | -0.18% | 0.66x | 3.4 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | DOT/USD | 0.6775 | 46.820 | 34.328 | +0.30% | -0.34% | 2.42x | 4.4 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.3236 | 45.222 | 49.794 | +4.69% | +0.47% | 0.31x | 31.0 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | NIGHT/USD | 0.04848 | 45.000 | 52.886 | +0.69% | -0.27% | 0.35x | 2.1 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | WLD/USD | 0.2408 | 35.062 | 40.620 | +1.05% | -0.08% | 0.49x | 4.2 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | TIA/USD | 0.3389 | 34.848 | 35.452 | +0.92% | -0.29% | 1.09x | 5.9 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 11 | SPX/USD | 0.2805 | 15.599 | 24.033 | +0.32% | +0.04% | 0.14x | 21.4 | 2026-11-24T08:31:34.546965+00:00 | Not calibrated | WEAK 18/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.540 | 25.241 | -0.09% | 0.21x |
| 2 | BABY/USD | 71.685 | 0.00911 | -0.22% | 7.81x |
| 3 | PEPE/USD | 70.702 | 3.535e-06 | +0.08% | 4.09x |
| 4 | XMR/USD | 65.742 | 495.72 | -0.12% | 3.90x |
| 5 | LINK/USD | 56.397 | 9.04474 | -0.18% | 0.66x |
| 6 | NIGHT/USD | 52.886 | 0.04848 | -0.27% | 0.35x |
| 7 | ICNT/USD | 49.794 | 0.3236 | +0.47% | 0.31x |
| 8 | WLD/USD | 40.620 | 0.2408 | -0.08% | 0.49x |
| 9 | TIA/USD | 35.452 | 0.3389 | -0.29% | 1.09x |
| 10 | DOT/USD | 34.328 | 0.6775 | -0.34% | 2.42x |
| 11 | SPX/USD | 24.033 | 0.2805 | +0.04% | 0.14x |

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

- Persisted scans: 1550; predictions: 13332; observations: 939048.
- Matured sampled outcomes across 1/6/24/48h: 25219; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 141 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45356572551 · **Generation:** 1550 · **Legacy run:** 45356572551
**Main quote time:** 2026-11-24T08:31:40.325174+00:00 · **Legacy report time:** 2026-11-24T08:32:31.932479+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.535e-06 | 86.13 | +0.08% | 4.09x | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | BABY/USD | 0.00911 | 85.59 | -0.22% | 7.81x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 3 | XMR/USD | 495.72 | 80.12 | -0.12% | 3.90x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 25.241 | 65.19 | -0.09% | 0.21x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 5 | LINK/USD | 9.04474 | 52.11 | -0.18% | 0.66x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | DOT/USD | 0.6775 | 46.82 | -0.34% | 2.42x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 7 | ICNT/USD | 0.3236 | 45.22 | +0.47% | 0.31x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 8 | NIGHT/USD | 0.04848 | 45.00 | -0.27% | 0.35x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | WLD/USD | 0.2408 | 35.06 | -0.08% | 0.49x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | TIA/USD | 0.3389 | 34.85 | -0.29% | 1.09x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 11 | SPX/USD | 0.2805 | 15.60 | +0.04% | 0.14x | WEAK 18/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.535e-06 | 85.79 | +0.08% | 4.09x | 9096 | STRONG 98/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
