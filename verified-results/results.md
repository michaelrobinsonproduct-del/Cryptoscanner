# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T05:57:32.876782+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45556805870
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cf6e32821d8301b706e0e310b4ca81777fb46fe5 (atomic ledger/results publication)
**Ledger generation:** 1678 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.034 | 88.759 | 65.551 | +2.02% | +1.70% | 2.47x | 7.2 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.00995 | 76.438 | 78.757 | +5.07% | +0.40% | 0.57x | 10.1 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00887 | 75.785 | 71.745 | +7.38% | +1.96% | 0.42x | 11.3 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.487e-06 | 70.039 | 49.094 | +0.98% | +1.19% | 5.14x | 2.9 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | DRV/USD | 0.33148 | 66.748 | 72.157 | +5.47% | +0.38% | 0.27x | 6.3 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XMR/USD | 512.04 | 60.016 | 53.894 | +0.48% | -0.07% | 1.65x | 6.5 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07138 | 49.247 | 39.124 | +2.45% | -0.11% | 2.07x | 19.6 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | PENGU/USD | 0.004238 | 40.662 | 36.024 | +0.52% | +0.83% | 1.05x | 2.4 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 9 | SKY/USD | 0.04148 | 38.952 | 38.807 | +1.22% | +0.39% | 0.82x | 7.2 | 2026-11-25T05:57:24.920694+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.757 | 0.00995 | +0.40% | 0.57x |
| 2 | DRV/USD | 72.157 | 0.33148 | +0.38% | 0.27x |
| 3 | BABY/USD | 71.745 | 0.00887 | +1.96% | 0.42x |
| 4 | VVV/USD | 65.551 | 25.034 | +1.70% | 2.47x |
| 5 | XMR/USD | 53.894 | 512.04 | -0.07% | 1.65x |
| 6 | PEPE/USD | 49.094 | 3.487e-06 | +1.19% | 5.14x |
| 7 | SYRUP/USD | 39.124 | 0.07138 | -0.11% | 2.07x |
| 8 | SKY/USD | 38.807 | 0.04148 | +0.39% | 0.82x |
| 9 | PENGU/USD | 36.024 | 0.004238 | +0.83% | 1.05x |

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

- Persisted scans: 1678; predictions: 14242; observations: 1016993.
- Matured sampled outcomes across 1/6/24/48h: 30301; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45556805870 · **Generation:** 1678 · **Legacy run:** 45556805870
**Main quote time:** 2026-11-25T05:57:32.876782+00:00 · **Legacy report time:** 2026-11-25T05:58:27.482792+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.034 | 88.76 | +1.70% | 2.47x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD | 0.00995 | 76.44 | +0.40% | 0.57x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 3 | BABY/USD | 0.00887 | 75.78 | +1.96% | 0.42x | MODERATE 63/100 | VERY_HIGH 81/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.487e-06 | 70.04 | +1.19% | 5.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | DRV/USD | 0.33148 | 66.75 | +0.38% | 0.27x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 6 | XMR/USD | 512.04 | 60.02 | -0.07% | 1.65x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 7 | SYRUP/USD | 0.07138 | 49.25 | -0.11% | 2.07x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 8 | PENGU/USD ⭐ | 0.004238 | 40.66 | +0.83% | 1.05x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 9 | SKY/USD | 0.04148 | 38.95 | +0.39% | 0.82x | MODERATE 49/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.009 | 71.02 | +1.70% | 2.47x | 15288 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEPE/USD ⭐ | 3.48e-06 | 60.37 | +1.19% | 5.14x | 5400 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | PENGU/USD ⭐ | 0.004228 | 35.77 | +0.83% | 1.05x | 2922 | MODERATE 63/100 | HIGH 67/100 | Watch |

**Same-run overlap:** VVV/USD, PEPE/USD, PENGU/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
