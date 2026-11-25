# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T08:47:26.608342+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45578947910
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8a9896d43127a3d90779a5a7b579ef8ab5368b11 (atomic ledger/results publication)
**Ledger generation:** 1695 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33795 | 96.971 | 73.833 | +7.53% | +1.63% | 5.46x | 17.5 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | PROS/USD | 0.7117 | 59.489 | 60.777 | +6.11% | +0.51% | 0.62x | 28.1 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | BABY/USD | 0.0087 | 58.332 | 63.243 | +5.33% | +0.58% | 0.22x | 11.4 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | VVV/USD | 24.654 | 48.204 | 54.263 | +0.47% | -0.19% | 0.49x | 8.1 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.479e-06 | 42.755 | 48.844 | +0.75% | -0.06% | 0.42x | 2.9 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.473 | 36.252 | 41.013 | +1.74% | +0.11% | 0.47x | 6.3 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05045 | 35.358 | 37.794 | +0.38% | +0.46% | 0.53x | 2.0 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | ATOM/USD | 1.2564 | 26.059 | 31.626 | +0.88% | +0.22% | 0.33x | 13.5 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | TON/USD | 0.934 | 24.902 | 29.189 | +0.32% | +0.43% | 0.36x | 10.7 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | CC/USD | 0.07532 | 24.013 | 32.368 | +0.36% | -0.13% | 0.23x | 9.3 | 2026-11-25T08:47:19.519246+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 73.833 | 0.33795 | +1.63% | 5.46x |
| 2 | BABY/USD | 63.243 | 0.0087 | +0.58% | 0.22x |
| 3 | PROS/USD | 60.777 | 0.7117 | +0.51% | 0.62x |
| 4 | VVV/USD | 54.263 | 24.654 | -0.19% | 0.49x |
| 5 | PEPE/USD | 48.844 | 3.479e-06 | -0.06% | 0.42x |
| 6 | AKT/USD | 41.013 | 0.473 | +0.11% | 0.47x |
| 7 | HBAR/USD | 37.794 | 0.05045 | +0.46% | 0.53x |
| 8 | CC/USD | 32.368 | 0.07532 | -0.13% | 0.23x |
| 9 | ATOM/USD | 31.626 | 1.2564 | +0.22% | 0.33x |
| 10 | TON/USD | 29.189 | 0.934 | +0.43% | 0.36x |

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

- Persisted scans: 1695; predictions: 14394; observations: 1027343.
- Matured sampled outcomes across 1/6/24/48h: 30933; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45578947910 · **Generation:** 1695 · **Legacy run:** 45578947910
**Main quote time:** 2026-11-25T08:47:26.608342+00:00 · **Legacy report time:** 2026-11-25T08:48:13.380228+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33795 | 96.97 | +1.63% | 5.46x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | PROS/USD | 0.7117 | 59.49 | +0.51% | 0.62x | MODERATE 50/100 | EXTREME 87/100 | Do nothing |
| 3 | BABY/USD | 0.0087 | 58.33 | +0.58% | 0.22x | MODERATE 54/100 | VERY_HIGH 81/100 | Watch |
| 4 | VVV/USD | 24.654 | 48.20 | -0.19% | 0.49x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | PEPE/USD | 3.479e-06 | 42.76 | -0.06% | 0.42x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | AKT/USD | 0.473 | 36.25 | +0.11% | 0.47x | WEAK 38/100 | VERY_HIGH 75/100 | Watch |
| 7 | HBAR/USD | 0.05045 | 35.36 | +0.46% | 0.53x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 8 | ATOM/USD | 1.2564 | 26.06 | +0.22% | 0.33x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 9 | TON/USD | 0.934 | 24.90 | +0.43% | 0.36x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |
| 10 | CC/USD | 0.07532 | 24.01 | -0.13% | 0.23x | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33732 | 87.42 | +1.63% | 5.46x | 9276 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
