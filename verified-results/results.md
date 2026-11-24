# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T22:34:29.469193+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45501423391
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1e6f3287e81a36976ea2a275f519459a330723ef (atomic ledger/results publication)
**Ledger generation:** 1634 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 511.74 | 102.630 | 88.038 | +5.29% | +1.39% | 1.77x | 8.0 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | GBP/USD | 1.31107 | 73.998 | 59.010 | +0.60% | -0.00% | 3.73x | 0.4 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 24.928 | 69.478 | 65.134 | +1.96% | +1.25% | 0.81x | 7.2 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 4 | AUD/USD | 0.66442 | 60.030 | 44.284 | +0.28% | +0.15% | 9.33x | 2.7 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.501e-06 | 56.626 | 58.528 | +2.31% | +0.03% | 0.80x | 5.7 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04873 | 41.458 | 44.735 | +1.20% | +0.39% | 0.48x | 6.2 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SKY/USD | 0.04075 | 26.287 | 36.423 | +0.89% | -0.63% | 0.30x | 7.4 | 2026-11-24T22:34:23.771442+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 88.038 | 511.74 | +1.39% | 1.77x |
| 2 | VVV/USD | 65.134 | 24.928 | +1.25% | 0.81x |
| 3 | GBP/USD | 59.010 | 1.31107 | -0.00% | 3.73x |
| 4 | PEPE/USD | 58.528 | 3.501e-06 | +0.03% | 0.80x |
| 5 | NIGHT/USD | 44.735 | 0.04873 | +0.39% | 0.48x |
| 6 | AUD/USD | 44.284 | 0.66442 | +0.15% | 9.33x |
| 7 | SKY/USD | 36.423 | 0.04075 | -0.63% | 0.30x |

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

- Persisted scans: 1634; predictions: 13994; observations: 990197.
- Matured sampled outcomes across 1/6/24/48h: 28847; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45501423391 · **Generation:** 1634 · **Legacy run:** 45501423391
**Main quote time:** 2026-11-24T22:34:29.469193+00:00 · **Legacy report time:** 2026-11-24T22:35:44.173817+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 511.74 | 102.63 | +1.39% | 1.77x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | GBP/USD | 1.31107 | 74.00 | -0.00% | 3.73x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD ⭐ | 24.928 | 69.48 | +1.25% | 0.81x | STRONG 75/100 | HIGH 62/100 | Watch |
| 4 | AUD/USD | 0.66442 | 60.03 | +0.15% | 9.33x | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | PEPE/USD ⭐ | 3.501e-06 | 56.63 | +0.03% | 0.80x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 6 | NIGHT/USD | 0.04873 | 41.46 | +0.39% | 0.48x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | SKY/USD | 0.04075 | 26.29 | -0.63% | 0.30x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 511.17 | 100.00 | +1.25% | 2.71x | 7723 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.918 | 71.92 | +0.73% | 1.87x | 17002 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 3 | PEPE/USD ⭐ | 3.506e-06 | 65.34 | +0.37% | 1.01x | 6781 | STRONG 78/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD, VVV/USD, PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
