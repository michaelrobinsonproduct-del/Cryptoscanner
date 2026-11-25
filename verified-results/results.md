# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T08:17:45.063079+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45574568934
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c4cfc745f6b25a2f8bce3b2b1925776f5eb79bbc (atomic ledger/results publication)
**Ledger generation:** 1692 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01044 | 98.547 | 85.189 | +10.24% | +2.09% | 1.29x | 19.2 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33229 | 67.798 | 72.154 | +5.73% | +0.14% | 0.49x | 10.5 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | CC/USD | 0.07549 | 52.295 | 35.300 | +0.59% | +0.40% | 10.52x | 6.6 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.48e-06 | 51.564 | 46.151 | +0.78% | +0.46% | 1.31x | 8.6 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 24.66 | 51.131 | 54.629 | +0.50% | +0.13% | 0.59x | 7.7 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PROS/USD | 0.7208 | 46.831 | 61.745 | +7.47% | -2.45% | 0.73x | 30.5 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | WEAK 18/100 | EXTREME 97/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.4709 | 45.945 | 38.860 | +1.29% | +0.92% | 1.25x | 4.2 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 8 | BABY/USD | 0.0086 | 45.646 | 55.178 | +4.12% | -2.81% | 1.45x | 11.6 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.092986 | 22.786 | 27.417 | +0.61% | +0.49% | 0.29x | 17.9 | 2026-11-25T08:17:37.454457+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.189 | 0.01044 | +2.09% | 1.29x |
| 2 | DRV/USD | 72.154 | 0.33229 | +0.14% | 0.49x |
| 3 | PROS/USD | 61.745 | 0.7208 | -2.45% | 0.73x |
| 4 | BABY/USD | 55.178 | 0.0086 | -2.81% | 1.45x |
| 5 | VVV/USD | 54.629 | 24.66 | +0.13% | 0.59x |
| 6 | PEPE/USD | 46.151 | 3.48e-06 | +0.46% | 1.31x |
| 7 | AKT/USD | 38.860 | 0.4709 | +0.92% | 1.25x |
| 8 | CC/USD | 35.300 | 0.07549 | +0.40% | 10.52x |
| 9 | CAP/USD | 27.417 | 0.092986 | +0.49% | 0.29x |

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

- Persisted scans: 1692; predictions: 14365; observations: 1025519.
- Matured sampled outcomes across 1/6/24/48h: 30824; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45574568934 · **Generation:** 1692 · **Legacy run:** 45574568934
**Main quote time:** 2026-11-25T08:17:45.063079+00:00 · **Legacy report time:** 2026-11-25T08:19:01.044599+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01044 | 98.55 | +2.09% | 1.29x | STRONG 89/100 | HIGH 61/100 | Watch |
| 2 | DRV/USD | 0.33229 | 67.80 | +0.14% | 0.49x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 3 | CC/USD ⭐ | 0.07549 | 52.29 | +0.40% | 10.52x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 4 | PEPE/USD ⭐ | 3.48e-06 | 51.56 | +0.46% | 1.31x | STRONG 81/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD | 24.66 | 51.13 | +0.13% | 0.59x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | PROS/USD | 0.7208 | 46.83 | -2.45% | 0.73x | WEAK 18/100 | EXTREME 97/100 | Do nothing |
| 7 | AKT/USD ⭐ | 0.4709 | 45.95 | +0.92% | 1.25x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 8 | BABY/USD | 0.0086 | 45.65 | -2.81% | 1.45x | WEAK 38/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | CAP/USD | 0.092986 | 22.79 | +0.49% | 0.29x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01051 | 89.39 | +2.09% | 1.29x | 19244 | STRONG 85/100 | HIGH 61/100 | Watch |
| 2 | TRX/USD | 0.30831 | 53.38 | +0.14% | 2.93x | 3552 | STRONG 72/100 | HIGH 55/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.49e-06 | 46.50 | +0.46% | 1.31x | 5789 | STRONG 78/100 | HIGH 55/100 | Watch |
| 4 | AKT/USD ⭐ | 0.4711 | 42.93 | +0.92% | 1.25x | 2759 | MODERATE 66/100 | HIGH 67/100 | Watch |
| 5 | CC/USD ⭐ | 0.07549 | 42.71 | +0.40% | 10.52x | 5473 | STRONG 86/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** MON/USD, CC/USD, PEPE/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
