# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T07:41:39.169770+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45349695298
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1cbd1bbd45a3e45485d41a3b09e36bf9cd71e738 (atomic ledger/results publication)
**Ledger generation:** 1545 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04929 | 79.189 | 65.201 | +2.37% | -0.20% | 4.09x | 2.0 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 498.55 | 71.641 | 69.127 | +2.58% | +0.22% | 1.14x | 7.8 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 3 | LTC/USD | 41.54 | 69.977 | 55.824 | +0.29% | -0.05% | 2.44x | 2.4 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3336 | 68.777 | 65.401 | +7.93% | +1.31% | 0.68x | 24.1 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | BABY/USD | 0.00907 | 64.848 | 71.317 | +6.71% | +0.44% | 0.13x | 11.0 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0064 | 62.680 | 58.920 | +0.85% | -0.09% | 1.42x | 4.0 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.531e-06 | 61.868 | 70.092 | +3.19% | -0.20% | 0.28x | 5.7 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LINK/USD | 9.03374 | 60.024 | 55.319 | +0.32% | +0.00% | 1.47x | 3.8 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 9 | VVV/USD | 25.152 | 59.807 | 70.194 | +2.88% | -0.81% | 0.37x | 9.9 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | TIA/USD | 0.3422 | 56.944 | 43.839 | +1.91% | -0.38% | 2.78x | 2.9 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 11 | WLD/USD | 0.2413 | 54.198 | 42.075 | +1.26% | -0.58% | 3.55x | 4.1 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 12 | PENGU/USD | 0.004439 | 38.630 | 35.916 | +0.36% | -0.34% | 1.44x | 4.5 | 2026-11-24T07:41:32.644986+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BABY/USD | 71.317 | 0.00907 | +0.44% | 0.13x |
| 2 | VVV/USD | 70.194 | 25.152 | -0.81% | 0.37x |
| 3 | PEPE/USD | 70.092 | 3.531e-06 | -0.20% | 0.28x |
| 4 | XMR/USD | 69.127 | 498.55 | +0.22% | 1.14x |
| 5 | ICNT/USD | 65.401 | 0.3336 | +1.31% | 0.68x |
| 6 | NIGHT/USD | 65.201 | 0.04929 | -0.20% | 4.09x |
| 7 | NEAR/USD | 58.920 | 3.0064 | -0.09% | 1.42x |
| 8 | LTC/USD | 55.824 | 41.54 | -0.05% | 2.44x |
| 9 | LINK/USD | 55.319 | 9.03374 | +0.00% | 1.47x |
| 10 | TIA/USD | 43.839 | 0.3422 | -0.38% | 2.78x |
| 11 | WLD/USD | 42.075 | 0.2413 | -0.58% | 3.55x |
| 12 | PENGU/USD | 35.916 | 0.004439 | -0.34% | 1.44x |

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

- Persisted scans: 1545; predictions: 13273; observations: 936003.
- Matured sampled outcomes across 1/6/24/48h: 25008; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45349695298 · **Generation:** 1545 · **Legacy run:** 45349695298
**Main quote time:** 2026-11-24T07:41:39.169770+00:00 · **Legacy report time:** 2026-11-24T07:42:37.999819+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04929 | 79.19 | -0.20% | 4.09x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD ⭐ | 498.55 | 71.64 | +0.22% | 1.14x | STRONG 81/100 | HIGH 62/100 | Watch |
| 3 | LTC/USD | 41.54 | 69.98 | -0.05% | 2.44x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | ICNT/USD | 0.3336 | 68.78 | +1.31% | 0.68x | MODERATE 54/100 | EXTREME 87/100 | Do nothing |
| 5 | BABY/USD | 0.00907 | 64.85 | +0.44% | 0.13x | MODERATE 57/100 | VERY_HIGH 81/100 | Watch |
| 6 | NEAR/USD | 3.0064 | 62.68 | -0.09% | 1.42x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 7 | PEPE/USD | 3.531e-06 | 61.87 | -0.20% | 0.28x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | LINK/USD | 9.03374 | 60.02 | +0.00% | 1.47x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 9 | VVV/USD | 25.152 | 59.81 | -0.81% | 0.37x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | TIA/USD | 0.3422 | 56.94 | -0.38% | 2.78x | MODERATE 58/100 | HIGH 66/100 | Watch |
| 11 | WLD/USD | 0.2413 | 54.20 | -0.58% | 3.55x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 12 | PENGU/USD | 0.004439 | 38.63 | -0.34% | 1.44x | WEAK 39/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 497.42 | 66.90 | +0.22% | 1.14x | 11524 | STRONG 78/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
