# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T06:57:33.078006+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45564092150
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2668fe54e865d83aa39ec9a0bf09ae17b802c582 (atomic ledger/results publication)
**Ledger generation:** 1684 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.3368 | 84.883 | 73.145 | +7.17% | -0.11% | 2.23x | 18.4 | 2026-11-25T06:57:25.226198+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 2 | MON/USD | 0.01031 | 84.002 | 84.277 | +8.87% | -1.25% | 1.60x | 19.4 | 2026-11-25T06:57:25.226198+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 3 | BABY/USD | 0.00905 | 78.533 | 71.645 | +9.56% | +0.45% | 1.47x | 11.0 | 2026-11-25T06:57:25.226198+00:00 | Not calibrated | STRONG 79/100 | HIGH 66/100 | Watch | WATCH |
| 4 | VVV/USD | 25.009 | 55.392 | 63.632 | +1.92% | -0.11% | 0.23x | 9.6 | 2026-11-25T06:57:25.226198+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.508e-06 | 49.585 | 52.501 | +1.59% | +0.06% | 0.68x | 5.7 | 2026-11-25T06:57:25.226198+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | CAP/USD | 0.093635 | 40.421 | 38.550 | +1.32% | +0.06% | 1.16x | 5.9 | 2026-11-25T06:57:25.226198+00:00 | Not calibrated | MODERATE 45/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 84.277 | 0.01031 | -1.25% | 1.60x |
| 2 | DRV/USD | 73.145 | 0.3368 | -0.11% | 2.23x |
| 3 | BABY/USD | 71.645 | 0.00905 | +0.45% | 1.47x |
| 4 | VVV/USD | 63.632 | 25.009 | -0.11% | 0.23x |
| 5 | PEPE/USD | 52.501 | 3.508e-06 | +0.06% | 0.68x |
| 6 | CAP/USD | 38.550 | 0.093635 | +0.06% | 1.16x |

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

- Persisted scans: 1684; predictions: 14299; observations: 1020647.
- Matured sampled outcomes across 1/6/24/48h: 30518; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 18; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45564092150 · **Generation:** 1684 · **Legacy run:** 45564092150
**Main quote time:** 2026-11-25T06:57:33.078006+00:00 · **Legacy report time:** 2026-11-25T06:58:47.443863+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.3368 | 84.88 | -0.11% | 2.23x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 2 | MON/USD | 0.01031 | 84.00 | -1.25% | 1.60x | MODERATE 57/100 | VERY_HIGH 71/100 | Do nothing |
| 3 | BABY/USD ⭐ | 0.00905 | 78.53 | +0.45% | 1.47x | STRONG 89/100 | HIGH 66/100 | Watch |
| 4 | VVV/USD | 25.009 | 55.39 | -0.11% | 0.23x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | PEPE/USD | 3.508e-06 | 49.59 | +0.06% | 0.68x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 6 | CAP/USD ⭐ | 0.093635 | 40.42 | +0.06% | 1.16x | MODERATE 55/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00905 | 74.50 | +0.45% | 1.47x | 3797 | STRONG 87/100 | HIGH 66/100 | Watch |
| 2 | CAP/USD ⭐ | 0.093576 | 42.01 | +0.06% | 1.16x | 5293 | MODERATE 56/100 | HIGH 67/100 | Watch |

**Same-run overlap:** BABY/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
