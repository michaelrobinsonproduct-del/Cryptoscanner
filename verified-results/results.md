# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T19:56:13.223831+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45689784358
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e142514077efc9ff25eb1451fa9ce20a901698e3 (atomic ledger/results publication)
**Ledger generation:** 1759 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 61.31 | 76.936 | 70.203 | +2.41% | +0.02% | 1.67x | 3.3 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002522 | 76.516 | 63.258 | +3.40% | +0.40% | 2.13x | 4.0 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 42.51 | 75.053 | 82.269 | +4.06% | +0.00% | 0.28x | 2.4 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94062 | 73.496 | 67.839 | +1.84% | -0.13% | 1.63x | 0.1 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6636 | 66.123 | 71.652 | +2.49% | -0.20% | 0.54x | 1.5 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0559601 | 64.129 | 54.274 | +1.31% | -0.00% | 1.99x | 0.6 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XPL/USD | 0.0481 | 63.786 | 71.974 | +9.32% | -0.82% | 0.59x | 20.8 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | SOL/USD | 70.42 | 63.183 | 62.537 | +1.18% | +0.11% | 1.01x | 1.4 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ZEC/USD | 753.17 | 62.598 | 66.536 | +1.93% | -0.39% | 0.80x | 4.0 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.485e-06 | 61.840 | 50.892 | +0.93% | +0.09% | 2.05x | 2.9 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 11 | LINK/USD | 9.10134 | 58.967 | 65.608 | +2.94% | +0.05% | 0.31x | 5.6 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ADA/USD | 0.146907 | 58.298 | 66.119 | +1.77% | +0.00% | 0.22x | 2.5 | 2026-11-25T19:56:06.121204+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 82.269 | 42.51 | +0.00% | 0.28x |
| 2 | XPL/USD | 71.974 | 0.0481 | -0.82% | 0.59x |
| 3 | SUI/USD | 71.652 | 0.6636 | -0.20% | 0.54x |
| 4 | HYPE/USD | 70.203 | 61.31 | +0.02% | 1.67x |
| 5 | XRP/USD | 67.839 | 0.94062 | -0.13% | 1.63x |
| 6 | ZEC/USD | 66.536 | 753.17 | -0.39% | 0.80x |
| 7 | ADA/USD | 66.119 | 0.146907 | +0.00% | 0.22x |
| 8 | LINK/USD | 65.608 | 9.10134 | +0.05% | 0.31x |
| 9 | PUMP/USD | 63.258 | 0.002522 | +0.40% | 2.13x |
| 10 | SOL/USD | 62.537 | 70.42 | +0.11% | 1.01x |
| 11 | XDG/USD | 54.274 | 0.0559601 | -0.00% | 1.99x |
| 12 | PEPE/USD | 50.892 | 3.485e-06 | +0.09% | 2.05x |

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

- Persisted scans: 1759; predictions: 14852; observations: 1066275.
- Matured sampled outcomes across 1/6/24/48h: 32606; gap abstentions: 22896. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45689784358 · **Generation:** 1759 · **Legacy run:** 45689784358
**Main quote time:** 2026-11-25T19:56:13.223831+00:00 · **Legacy report time:** 2026-11-25T19:57:19.092609+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 61.31 | 76.94 | +0.02% | 1.67x | STRONG 73/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002522 | 76.52 | +0.40% | 2.13x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD | 42.51 | 75.05 | +0.00% | 0.28x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | XRP/USD | 0.94062 | 73.50 | -0.13% | 1.63x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | SUI/USD | 0.6636 | 66.12 | -0.20% | 0.54x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 6 | XDG/USD | 0.0559601 | 64.13 | -0.00% | 1.99x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | XPL/USD | 0.0481 | 63.79 | -0.82% | 0.59x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 8 | SOL/USD | 70.42 | 63.18 | +0.11% | 1.01x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 9 | ZEC/USD | 753.17 | 62.60 | -0.39% | 0.80x | WEAK 36/100 | HIGH 68/100 | Watch |
| 10 | PEPE/USD | 3.485e-06 | 61.84 | +0.09% | 2.05x | STRONG 76/100 | HIGH 55/100 | Watch |
| 11 | LINK/USD | 9.10134 | 58.97 | +0.05% | 0.31x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | ADA/USD | 0.146907 | 58.30 | +0.00% | 0.22x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002519 | 80.95 | +0.40% | 2.13x | 5129 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
