# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T11:00:45.025748+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44896915864
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** e6c3fa3f375241a36bcf97a28d68911bb1460891 (atomic ledger/results publication)
**Ledger generation:** 1124 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.942 | 85.976 | 91.256 | +5.80% | -0.20% | 0.57x | 8.7 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 467.82 | 69.244 | 68.405 | +2.53% | +0.41% | 0.88x | 8.6 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04478 | 66.439 | 47.280 | +2.14% | +0.83% | 2.86x | 4.5 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ETH/USD | 1638.14 | 60.810 | 63.105 | +1.16% | +0.07% | 0.73x | 0.1 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.07708 | 56.971 | 60.022 | +3.46% | +0.81% | 0.29x | 7.8 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | TRX/USD | 0.302973 | 55.784 | 58.394 | +0.49% | +0.10% | 0.69x | 0.0 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SENT/USD | 0.020828 | 50.385 | 35.792 | +1.13% | -0.08% | 6.32x | 6.2 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | ZAMA/USD | 0.05799 | 39.416 | 39.204 | +1.72% | +0.02% | 1.01x | 8.6 | 2026-11-21T11:00:37.481064+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.256 | 21.942 | -0.20% | 0.57x |
| 2 | XMR/USD | 68.405 | 467.82 | +0.41% | 0.88x |
| 3 | ETH/USD | 63.105 | 1638.14 | +0.07% | 0.73x |
| 4 | USELESS/USD | 60.022 | 0.07708 | +0.81% | 0.29x |
| 5 | TRX/USD | 58.394 | 0.302973 | +0.10% | 0.69x |
| 6 | SKY/USD | 47.280 | 0.04478 | +0.83% | 2.86x |
| 7 | ZAMA/USD | 39.204 | 0.05799 | +0.02% | 1.01x |
| 8 | SENT/USD | 35.792 | 0.020828 | -0.08% | 6.32x |

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

- Persisted scans: 1124; predictions: 8819; observations: 679751.
- Matured sampled outcomes across 1/6/24/48h: 11604; gap abstentions: 20331. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44896915864 · **Generation:** 1124 · **Legacy run:** 44896915864
**Main quote time:** 2026-11-21T11:00:45.025748+00:00 · **Legacy report time:** 2026-11-21T11:01:34.996919+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.942 | 85.98 | -0.20% | 0.57x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 467.82 | 69.24 | +0.41% | 0.88x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04478 | 66.44 | +0.83% | 2.86x | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 4 | ETH/USD | 1638.14 | 60.81 | +0.07% | 0.73x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 5 | USELESS/USD | 0.07708 | 56.97 | +0.81% | 0.29x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | TRX/USD | 0.302973 | 55.78 | +0.10% | 0.69x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 7 | SENT/USD | 0.020828 | 50.38 | -0.08% | 6.32x | MODERATE 55/100 | VERY_HIGH 73/100 | Watch |
| 8 | ZAMA/USD | 0.05799 | 39.42 | +0.02% | 1.01x | MODERATE 45/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04463 | 56.24 | +0.83% | 2.86x | 4519 | STRONG 88/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
