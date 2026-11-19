# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:40:26.777889+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44535648160
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 6d3b0e096bca85e137dc02cddfaf2e507f371632 (atomic ledger/results publication)
**Ledger generation:** 784 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.042 | 114.922 | 95.809 | +6.33% | +0.82% | 2.84x | 7.0 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 947.26 | 90.925 | 79.251 | +3.87% | +0.51% | 1.91x | 5.7 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3997 | 85.200 | 75.097 | +3.10% | +0.20% | 1.91x | 3.2 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.993e-06 | 77.416 | 80.514 | +6.59% | +1.11% | 0.13x | 10.0 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ETH/USD | 1805.07 | 76.876 | 66.927 | +1.71% | +0.17% | 1.91x | 0.1 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ADA/USD | 0.15545 | 70.316 | 74.387 | +2.77% | +0.10% | 0.54x | 0.1 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.98889 | 69.039 | 71.110 | +2.33% | +0.27% | 0.66x | 0.4 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SENT/USD | 0.021775 | 68.205 | 71.891 | +5.68% | -0.33% | 0.80x | 2.3 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | LIGHTER/USD | 2.943 | 67.936 | 76.164 | +8.44% | -0.14% | 0.24x | 10.2 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | SOL/USD | 74.92 | 67.373 | 67.468 | +1.88% | +0.31% | 0.84x | 1.3 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 11 | HYPE/USD | 68.69 | 64.724 | 72.488 | +2.71% | +0.06% | 0.19x | 2.9 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 63685.5 | 63.903 | 62.783 | +1.11% | +0.05% | 1.09x | 0.0 | 2026-11-19T13:40:18.701116+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.809 | 23.042 | +0.82% | 2.84x |
| 2 | PEPE/USD | 80.514 | 3.993e-06 | +1.11% | 0.13x |
| 3 | ZEC/USD | 79.251 | 947.26 | +0.51% | 1.91x |
| 4 | LIGHTER/USD | 76.164 | 2.943 | -0.14% | 0.24x |
| 5 | NEAR/USD | 75.097 | 3.3997 | +0.20% | 1.91x |
| 6 | ADA/USD | 74.387 | 0.15545 | +0.10% | 0.54x |
| 7 | HYPE/USD | 72.488 | 68.69 | +0.06% | 0.19x |
| 8 | SENT/USD | 71.891 | 0.021775 | -0.33% | 0.80x |
| 9 | XRP/USD | 71.110 | 0.98889 | +0.27% | 0.66x |
| 10 | SOL/USD | 67.468 | 74.92 | +0.31% | 0.84x |
| 11 | ETH/USD | 66.927 | 1805.07 | +0.17% | 1.91x |
| 12 | XBT/USD | 62.783 | 63685.5 | +0.05% | 1.09x |

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

- Persisted scans: 784; predictions: 6552; observations: 474330.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14983. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44535648160 · **Generation:** 784 · **Legacy run:** 44535648160
**Main quote time:** 2026-11-19T13:40:26.777889+00:00 · **Legacy report time:** 2026-11-19T13:41:09.718656+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.042 | 114.92 | +0.82% | 2.84x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 947.26 | 90.92 | +0.51% | 1.91x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.3997 | 85.20 | +0.20% | 1.91x | STRONG 88/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD | 3.993e-06 | 77.42 | +1.11% | 0.13x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 5 | ETH/USD | 1805.07 | 76.88 | +0.17% | 1.91x | STRONG 73/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD | 0.15545 | 70.32 | +0.10% | 0.54x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.98889 | 69.04 | +0.27% | 0.66x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | SENT/USD | 0.021775 | 68.20 | -0.33% | 0.80x | WEAK 39/100 | VERY_HIGH 73/100 | Watch |
| 9 | LIGHTER/USD | 2.943 | 67.94 | -0.14% | 0.24x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 10 | SOL/USD | 74.92 | 67.37 | +0.31% | 0.84x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 11 | HYPE/USD | 68.69 | 64.72 | +0.06% | 0.19x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 63685.5 | 63.90 | +0.05% | 1.09x | MODERATE 57/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.042 | 94.83 | +0.82% | 2.84x | 11880 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 946.8 | 93.95 | +0.51% | 1.91x | 21074 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.3953 | 86.56 | +0.20% | 1.91x | 15116 | STRONG 88/100 | HIGH 55/100 | Watch |
| 4 | PENGU/USD | 0.004867 | 83.99 | +0.19% | 10.16x | 2723 | STRONG 87/100 | HIGH 60/100 | Watch |

**Same-run overlap:** VVV/USD, ZEC/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
