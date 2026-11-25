# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T06:48:19.198768+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45562851936
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 58bcd64dc496c577dec8e5f0adc4d56eda07ef09 (atomic ledger/results publication)
**Ledger generation:** 1683 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33704 | 99.303 | 74.495 | +7.24% | +1.96% | 3.32x | 15.7 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01031 | 95.967 | 84.201 | +8.87% | +0.98% | 1.68x | 19.5 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | BABY/USD | 0.00902 | 80.122 | 71.702 | +9.20% | +1.02% | 1.33x | 11.1 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | STRONG 80/100 | HIGH 66/100 | Watch | WATCH |
| 4 | VVV/USD | 25.161 | 62.729 | 69.593 | +2.54% | +0.20% | 0.22x | 6.4 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.535e-06 | 62.374 | 55.252 | +2.37% | +0.71% | 1.36x | 11.3 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04124 | 51.595 | 34.647 | +0.63% | +0.39% | 3.45x | 7.3 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07224 | 50.957 | 49.980 | +3.69% | +0.01% | 1.09x | 15.2 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | AKT/USD | 0.4671 | 50.160 | 30.732 | +0.47% | +0.89% | 3.18x | 8.5 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 9 | CAP/USD | 0.094816 | 48.570 | 47.443 | +2.59% | +1.02% | 0.60x | 6.0 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | TRX/USD | 0.308797 | 37.405 | 43.560 | +0.35% | +0.07% | 0.35x | 0.0 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PENGU/USD | 0.00426 | 32.663 | 37.509 | +1.04% | +0.23% | 0.40x | 7.0 | 2026-11-25T06:48:11.709791+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 84.201 | 0.01031 | +0.98% | 1.68x |
| 2 | DRV/USD | 74.495 | 0.33704 | +1.96% | 3.32x |
| 3 | BABY/USD | 71.702 | 0.00902 | +1.02% | 1.33x |
| 4 | VVV/USD | 69.593 | 25.161 | +0.20% | 0.22x |
| 5 | PEPE/USD | 55.252 | 3.535e-06 | +0.71% | 1.36x |
| 6 | SYRUP/USD | 49.980 | 0.07224 | +0.01% | 1.09x |
| 7 | CAP/USD | 47.443 | 0.094816 | +1.02% | 0.60x |
| 8 | TRX/USD | 43.560 | 0.308797 | +0.07% | 0.35x |
| 9 | PENGU/USD | 37.509 | 0.00426 | +0.23% | 0.40x |
| 10 | SKY/USD | 34.647 | 0.04124 | +0.39% | 3.45x |
| 11 | AKT/USD | 30.732 | 0.4671 | +0.89% | 3.18x |

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

- Persisted scans: 1683; predictions: 14293; observations: 1020038.
- Matured sampled outcomes across 1/6/24/48h: 30482; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45562851936 · **Generation:** 1683 · **Legacy run:** 45562851936
**Main quote time:** 2026-11-25T06:48:19.198768+00:00 · **Legacy report time:** 2026-11-25T06:49:19.754450+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33704 | 99.30 | +1.96% | 3.32x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01031 | 95.97 | +0.98% | 1.68x | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 3 | BABY/USD ⭐ | 0.00902 | 80.12 | +1.02% | 1.33x | STRONG 90/100 | HIGH 66/100 | Watch |
| 4 | VVV/USD | 25.161 | 62.73 | +0.20% | 0.22x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 5 | PEPE/USD ⭐ | 3.535e-06 | 62.37 | +0.71% | 1.36x | STRONG 81/100 | HIGH 61/100 | Watch |
| 6 | SKY/USD | 0.04124 | 51.59 | +0.39% | 3.45x | STRONG 81/100 | HIGH 60/100 | Watch |
| 7 | SYRUP/USD | 0.07224 | 50.96 | +0.01% | 1.09x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 8 | AKT/USD | 0.4671 | 50.16 | +0.89% | 3.18x | STRONG 80/100 | HIGH 60/100 | Watch |
| 9 | CAP/USD | 0.094816 | 48.57 | +1.02% | 0.60x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 10 | TRX/USD | 0.308797 | 37.40 | +0.07% | 0.35x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 11 | PENGU/USD | 0.00426 | 32.66 | +0.23% | 0.40x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.3377 | 88.32 | +1.96% | 3.32x | 9085 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01026 | 87.01 | +0.98% | 1.68x | 18571 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | BABY/USD ⭐ | 0.009 | 75.69 | +1.02% | 1.33x | 3911 | STRONG 88/100 | HIGH 66/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.53e-06 | 64.57 | +0.71% | 1.36x | 5529 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, MON/USD, BABY/USD, PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
