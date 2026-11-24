# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T12:41:58.710606+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45395638878
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1fec280496a13f3ec908912ea1d79e9705a299a9 (atomic ledger/results publication)
**Ledger generation:** 1575 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.756 | 83.778 | 88.184 | +5.35% | -0.47% | 0.80x | 8.5 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 2 | MON/USD | 0.01231 | 79.199 | 78.769 | +6.86% | -1.68% | 1.88x | 16.3 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 3 | XMR/USD | 499.32 | 71.326 | 69.248 | +2.74% | -0.20% | 1.31x | 9.8 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04887 | 56.654 | 53.050 | +1.50% | +0.85% | 0.94x | 12.3 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 5 | GBP/USD | 1.30908 | 51.661 | 57.940 | +0.45% | +0.03% | 0.35x | 0.4 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.441e-06 | 41.083 | 51.588 | +0.56% | -0.69% | 0.30x | 8.7 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66431 | 40.236 | 48.523 | +0.26% | +0.06% | 0.14x | 2.0 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | 2Z/USD | 0.01602 | 26.850 | 31.682 | +2.36% | -0.99% | 1.01x | 31.2 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | WEAK 13/100 | EXTREME 92/100 | Do nothing | WATCH |
| 9 | BABY/USD | 0.00854 | 6.423 | 18.467 | +0.47% | -0.70% | 0.14x | 35.0 | 2026-11-24T12:41:53.676592+00:00 | Not calibrated | WEAK 0/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 88.184 | 25.756 | -0.47% | 0.80x |
| 2 | MON/USD | 78.769 | 0.01231 | -1.68% | 1.88x |
| 3 | XMR/USD | 69.248 | 499.32 | -0.20% | 1.31x |
| 4 | GBP/USD | 57.940 | 1.30908 | +0.03% | 0.35x |
| 5 | NIGHT/USD | 53.050 | 0.04887 | +0.85% | 0.94x |
| 6 | PEPE/USD | 51.588 | 3.441e-06 | -0.69% | 0.30x |
| 7 | AUD/USD | 48.523 | 0.66431 | +0.06% | 0.14x |
| 8 | 2Z/USD | 31.682 | 0.01602 | -0.99% | 1.01x |
| 9 | BABY/USD | 18.467 | 0.00854 | -0.70% | 0.14x |

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

- Persisted scans: 1575; predictions: 13587; observations: 954273.
- Matured sampled outcomes across 1/6/24/48h: 26381; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45395638878 · **Generation:** 1575 · **Legacy run:** 45395638878
**Main quote time:** 2026-11-24T12:41:58.710606+00:00 · **Legacy report time:** 2026-11-24T12:43:12.759444+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.756 | 83.78 | -0.47% | 0.80x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 2 | MON/USD | 0.01231 | 79.20 | -1.68% | 1.88x | MODERATE 55/100 | VERY_HIGH 71/100 | Do nothing |
| 3 | XMR/USD | 499.32 | 71.33 | -0.20% | 1.31x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04887 | 56.65 | +0.85% | 0.94x | MODERATE 53/100 | HIGH 68/100 | Watch |
| 5 | GBP/USD | 1.30908 | 51.66 | +0.03% | 0.35x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEPE/USD | 3.441e-06 | 41.08 | -0.69% | 0.30x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | AUD/USD | 0.66431 | 40.24 | +0.06% | 0.14x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 8 | 2Z/USD | 0.01602 | 26.85 | -0.99% | 1.01x | WEAK 13/100 | EXTREME 92/100 | Do nothing |
| 9 | BABY/USD | 0.00854 | 6.42 | -0.70% | 0.14x | WEAK 0/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
