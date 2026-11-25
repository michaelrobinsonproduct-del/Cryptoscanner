# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T06:17:37.295452+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45559145767
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6f48dc1e9fb5453360b6be6602d5ab4c28a8ee26 (atomic ledger/results publication)
**Ledger generation:** 1680 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01008 | 109.546 | 88.540 | +6.44% | +1.20% | 2.86x | 9.9 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.225 | 86.765 | 68.649 | +2.80% | +0.62% | 4.57x | 11.9 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | STRONG 93/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | PEPE/USD | 3.533e-06 | 76.584 | 54.550 | +2.32% | +1.41% | 3.90x | 11.3 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Consider small entry | WATCH |
| 4 | BABY/USD | 0.00885 | 76.400 | 71.688 | +7.14% | -0.11% | 1.53x | 11.3 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PENGU/USD | 0.004261 | 57.847 | 38.827 | +1.07% | +0.80% | 11.43x | 4.7 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 6 | CAP/USD | 0.093377 | 57.418 | 37.049 | +1.04% | +1.07% | 2.51x | 4.9 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 7 | DRV/USD | 0.33031 | 55.202 | 63.039 | +5.10% | -0.07% | 0.25x | 19.4 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | SYRUP/USD | 0.07148 | 43.567 | 40.158 | +2.60% | +0.69% | 1.00x | 19.6 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | SKY/USD | 0.04141 | 34.008 | 33.904 | +1.05% | -0.02% | 1.02x | 14.5 | 2026-11-25T06:17:30.560298+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 88.540 | 0.01008 | +1.20% | 2.86x |
| 2 | BABY/USD | 71.688 | 0.00885 | -0.11% | 1.53x |
| 3 | VVV/USD | 68.649 | 25.225 | +0.62% | 4.57x |
| 4 | DRV/USD | 63.039 | 0.33031 | -0.07% | 0.25x |
| 5 | PEPE/USD | 54.550 | 3.533e-06 | +1.41% | 3.90x |
| 6 | SYRUP/USD | 40.158 | 0.07148 | +0.69% | 1.00x |
| 7 | PENGU/USD | 38.827 | 0.004261 | +0.80% | 11.43x |
| 8 | CAP/USD | 37.049 | 0.093377 | +1.07% | 2.51x |
| 9 | SKY/USD | 33.904 | 0.04141 | -0.02% | 1.02x |

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

- Persisted scans: 1680; predictions: 14262; observations: 1018211.
- Matured sampled outcomes across 1/6/24/48h: 30379; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45559145767 · **Generation:** 1680 · **Legacy run:** 45559145767
**Main quote time:** 2026-11-25T06:17:37.295452+00:00 · **Legacy report time:** 2026-11-25T06:18:43.110813+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01008 | 109.55 | +1.20% | 2.86x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.225 | 86.76 | +0.62% | 4.57x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | PEPE/USD ⭐ | 3.533e-06 | 76.58 | +1.41% | 3.90x | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 4 | BABY/USD | 0.00885 | 76.40 | -0.11% | 1.53x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 5 | PENGU/USD ⭐ | 0.004261 | 57.85 | +0.80% | 11.43x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 6 | CAP/USD ⭐ | 0.093377 | 57.42 | +1.07% | 2.51x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 7 | DRV/USD | 0.33031 | 55.20 | -0.07% | 0.25x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | SYRUP/USD | 0.07148 | 43.57 | +0.69% | 1.00x | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |
| 9 | SKY/USD | 0.04141 | 34.01 | -0.02% | 1.02x | WEAK 22/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01008 | 92.14 | +1.20% | 2.86x | 18549 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.224 | 81.14 | +0.62% | 4.57x | 15113 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEPE/USD ⭐ | 3.529e-06 | 69.03 | +1.41% | 3.90x | 5473 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD | 2.8907 | 56.46 | +0.49% | 4.44x | 13537 | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | PENGU/USD ⭐ | 0.004261 | 53.05 | +0.80% | 11.43x | 2996 | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 6 | CAP/USD ⭐ | 0.093578 | 53.04 | +1.07% | 2.51x | 5280 | STRONG 92/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** MON/USD, VVV/USD, PEPE/USD, PENGU/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
