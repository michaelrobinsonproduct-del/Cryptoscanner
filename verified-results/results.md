# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:20:26.442482+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44457534326
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 2faa049f60484673848404163a71830b13dc7e3d (atomic ledger/results publication)
**Ledger generation:** 753 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.4006 | 88.969 | 74.996 | +3.13% | -0.21% | 3.67x | 3.8 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ETH/USD | 1794.61 | 76.086 | 62.801 | +1.12% | -0.34% | 2.90x | 0.1 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 22.412 | 75.605 | 72.816 | +3.42% | -0.12% | 1.34x | 5.4 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96973 | 70.774 | 57.382 | +0.35% | -0.32% | 9.34x | 0.1 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 74.25 | 67.564 | 61.085 | +0.97% | -0.26% | 1.78x | 1.3 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HYPE/USD | 67.38 | 65.390 | 59.491 | +0.75% | -0.22% | 1.70x | 1.5 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PYTH/USD | 0.05553 | 62.915 | 61.380 | +5.25% | +0.09% | 1.11x | 14.4 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | TAO/USD | 194.2572 | 61.823 | 59.597 | +1.20% | -0.36% | 1.40x | 7.6 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SENT/USD | 0.022184 | 60.408 | 70.408 | +7.66% | -9.69% | 3.04x | 13.2 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.09779 | 60.401 | 55.357 | +0.28% | -0.53% | 1.77x | 3.2 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0589589 | 59.633 | 52.410 | +0.43% | -0.26% | 1.85x | 0.0 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 12 | ZEC/USD | 924.75 | 57.175 | 62.176 | +1.40% | -0.51% | 0.76x | 5.3 | 2026-11-19T04:20:17.842917+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 74.996 | 3.4006 | -0.21% | 3.67x |
| 2 | VVV/USD | 72.816 | 22.412 | -0.12% | 1.34x |
| 3 | SENT/USD | 70.408 | 0.022184 | -9.69% | 3.04x |
| 4 | ETH/USD | 62.801 | 1794.61 | -0.34% | 2.90x |
| 5 | ZEC/USD | 62.176 | 924.75 | -0.51% | 0.76x |
| 6 | PYTH/USD | 61.380 | 0.05553 | +0.09% | 1.11x |
| 7 | SOL/USD | 61.085 | 74.25 | -0.26% | 1.78x |
| 8 | TAO/USD | 59.597 | 194.2572 | -0.36% | 1.40x |
| 9 | HYPE/USD | 59.491 | 67.38 | -0.22% | 1.70x |
| 10 | XRP/USD | 57.382 | 0.96973 | -0.32% | 9.34x |
| 11 | LINK/USD | 55.357 | 9.09779 | -0.53% | 1.77x |
| 12 | XDG/USD | 52.410 | 0.0589589 | -0.26% | 1.85x |

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

- Persisted scans: 753; predictions: 6180; observations: 455583.
- Matured sampled outcomes across 1/6/24/48h: 6162; gap abstentions: 13640. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44457534326 · **Generation:** 753 · **Legacy run:** 44457534326
**Main quote time:** 2026-11-19T04:20:26.442482+00:00 · **Legacy report time:** 2026-11-19T04:21:16.072023+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.4006 | 88.97 | -0.21% | 3.67x | STRONG 74/100 | HIGH 61/100 | Watch |
| 2 | ETH/USD | 1794.61 | 76.09 | -0.34% | 2.90x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 22.412 | 75.60 | -0.12% | 1.34x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.96973 | 70.77 | -0.32% | 9.34x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 74.25 | 67.56 | -0.26% | 1.78x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 6 | HYPE/USD | 67.38 | 65.39 | -0.22% | 1.70x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 7 | PYTH/USD ⭐ | 0.05553 | 62.92 | +0.09% | 1.11x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 8 | TAO/USD | 194.2572 | 61.82 | -0.36% | 1.40x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 9 | SENT/USD | 0.022184 | 60.41 | -9.69% | 3.04x | MODERATE 55/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LINK/USD | 9.09779 | 60.40 | -0.53% | 1.77x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 11 | XDG/USD | 0.0589589 | 59.63 | -0.26% | 1.85x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 12 | ZEC/USD | 924.75 | 57.17 | -0.51% | 0.76x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PYTH/USD ⭐ | 0.05557 | 66.73 | +0.09% | 1.11x | 2030 | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** PYTH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
