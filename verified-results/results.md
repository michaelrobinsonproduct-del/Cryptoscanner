# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T08:21:47.945511+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45355123211
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 20df93041275c470eb039dc5bd721db405181278 (atomic ledger/results publication)
**Ledger generation:** 1549 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.557e-06 | 93.955 | 75.410 | +3.95% | +0.71% | 3.44x | 5.6 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.369 | 75.659 | 77.223 | +3.77% | +0.21% | 0.74x | 8.3 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XMR/USD | 496 | 70.213 | 69.273 | +2.05% | -0.51% | 1.35x | 0.2 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LINK/USD | 9.06804 | 69.470 | 58.754 | +0.70% | +0.04% | 2.05x | 2.3 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94528 | 61.475 | 59.336 | +0.63% | +0.17% | 1.13x | 0.1 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0046 | 56.470 | 58.495 | +0.78% | +0.26% | 0.67x | 4.0 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 63.92 | 51.870 | 57.297 | +0.44% | -0.09% | 0.50x | 1.6 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | BAT/USD | 0.07949 | 47.529 | 50.763 | +3.01% | -0.23% | 0.79x | 5.0 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 9 | LUNA/USD | 4.55e-05 | 46.788 | 52.626 | +4.67% | -0.18% | 0.50x | 24.3 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | WEAK 18/100 | EXTREME 93/100 | Do nothing | WATCH |
| 10 | LTC/USD | 41.55 | 46.337 | 54.789 | +0.31% | -0.12% | 0.21x | 4.8 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | NIGHT/USD | 0.04854 | 44.961 | 52.733 | +0.81% | -0.06% | 0.25x | 4.1 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | WLD/USD | 0.242 | 37.224 | 44.200 | +1.55% | -0.17% | 0.39x | 4.1 | 2026-11-24T08:21:39.220063+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.223 | 25.369 | +0.21% | 0.74x |
| 2 | PEPE/USD | 75.410 | 3.557e-06 | +0.71% | 3.44x |
| 3 | XMR/USD | 69.273 | 496 | -0.51% | 1.35x |
| 4 | XRP/USD | 59.336 | 0.94528 | +0.17% | 1.13x |
| 5 | LINK/USD | 58.754 | 9.06804 | +0.04% | 2.05x |
| 6 | NEAR/USD | 58.495 | 3.0046 | +0.26% | 0.67x |
| 7 | HYPE/USD | 57.297 | 63.92 | -0.09% | 0.50x |
| 8 | LTC/USD | 54.789 | 41.55 | -0.12% | 0.21x |
| 9 | NIGHT/USD | 52.733 | 0.04854 | -0.06% | 0.25x |
| 10 | LUNA/USD | 52.626 | 4.55e-05 | -0.18% | 0.50x |
| 11 | BAT/USD | 50.763 | 0.07949 | -0.23% | 0.79x |
| 12 | WLD/USD | 44.200 | 0.242 | -0.17% | 0.39x |

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

- Persisted scans: 1549; predictions: 13321; observations: 938439.
- Matured sampled outcomes across 1/6/24/48h: 25178; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45355123211 · **Generation:** 1549 · **Legacy run:** 45355123211
**Main quote time:** 2026-11-24T08:21:47.945511+00:00 · **Legacy report time:** 2026-11-24T08:22:55.142021+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.557e-06 | 93.95 | +0.71% | 3.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 25.369 | 75.66 | +0.21% | 0.74x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 3 | XMR/USD | 496 | 70.21 | -0.51% | 1.35x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 4 | LINK/USD | 9.06804 | 69.47 | +0.04% | 2.05x | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD ⭐ | 0.94528 | 61.48 | +0.17% | 1.13x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 6 | NEAR/USD | 3.0046 | 56.47 | +0.26% | 0.67x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD | 63.92 | 51.87 | -0.09% | 0.50x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | BAT/USD | 0.07949 | 47.53 | -0.23% | 0.79x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |
| 9 | LUNA/USD | 4.55e-05 | 46.79 | -0.18% | 0.50x | WEAK 18/100 | EXTREME 93/100 | Do nothing |
| 10 | LTC/USD | 41.55 | 46.34 | -0.12% | 0.21x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | NIGHT/USD | 0.04854 | 44.96 | -0.06% | 0.25x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | WLD/USD | 0.242 | 37.22 | -0.17% | 0.39x | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.556e-06 | 91.47 | +0.71% | 3.44x | 9122 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | BABY/USD | 0.00918 | 80.22 | +0.33% | 4.75x | 4017 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.94584 | 58.94 | +0.17% | 1.13x | 45659 | MODERATE 64/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEPE/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
