# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T12:23:49.994135+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45392409072
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 758034a002142a5f8349e9b4a12dc1a37250dcf0 (atomic ledger/results publication)
**Ledger generation:** 1573 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.889 | 86.305 | 92.393 | +5.89% | +0.05% | 0.37x | 7.7 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XMR/USD | 500.44 | 85.758 | 70.067 | +2.97% | +0.14% | 2.54x | 11.4 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.3307 | 78.062 | 61.173 | +6.99% | +0.52% | 2.43x | 33.2 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | MON/USD | 0.01254 | 70.443 | 79.066 | +8.85% | -1.03% | 0.65x | 16.0 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | WEAK 35/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.462e-06 | 68.973 | 58.844 | +1.17% | -0.97% | 5.22x | 2.9 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04842 | 65.837 | 51.508 | +0.56% | +0.48% | 2.19x | 2.1 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LUNA/USD | 4.563e-05 | 52.544 | 53.481 | +4.97% | -1.39% | 1.60x | 26.3 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | GBP/USD | 1.30834 | 51.184 | 57.581 | +0.39% | +0.03% | 0.34x | 0.3 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | BAT/USD | 0.07786 | 34.804 | 36.764 | +0.89% | -0.23% | 0.92x | 3.9 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | BABY/USD | 0.00869 | 32.247 | 36.781 | +2.24% | +0.58% | 0.26x | 23.2 | 2026-11-24T12:23:43.877279+00:00 | Not calibrated | WEAK 36/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 92.393 | 25.889 | +0.05% | 0.37x |
| 2 | MON/USD | 79.066 | 0.01254 | -1.03% | 0.65x |
| 3 | XMR/USD | 70.067 | 500.44 | +0.14% | 2.54x |
| 4 | ICNT/USD | 61.173 | 0.3307 | +0.52% | 2.43x |
| 5 | PEPE/USD | 58.844 | 3.462e-06 | -0.97% | 5.22x |
| 6 | GBP/USD | 57.581 | 1.30834 | +0.03% | 0.34x |
| 7 | LUNA/USD | 53.481 | 4.563e-05 | -1.39% | 1.60x |
| 8 | NIGHT/USD | 51.508 | 0.04842 | +0.48% | 2.19x |
| 9 | BABY/USD | 36.781 | 0.00869 | +0.58% | 0.26x |
| 10 | BAT/USD | 36.764 | 0.07786 | -0.23% | 0.92x |

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

- Persisted scans: 1573; predictions: 13570; observations: 953055.
- Matured sampled outcomes across 1/6/24/48h: 26278; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45392409072 · **Generation:** 1573 · **Legacy run:** 45392409072
**Main quote time:** 2026-11-24T12:23:49.994135+00:00 · **Legacy report time:** 2026-11-24T12:25:03.636093+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.889 | 86.31 | +0.05% | 0.37x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 2 | XMR/USD ⭐ | 500.44 | 85.76 | +0.14% | 2.54x | STRONG 93/100 | HIGH 61/100 | Watch |
| 3 | ICNT/USD | 0.3307 | 78.06 | +0.52% | 2.43x | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 4 | MON/USD | 0.01254 | 70.44 | -1.03% | 0.65x | WEAK 35/100 | EXTREME 86/100 | Do nothing |
| 5 | PEPE/USD | 3.462e-06 | 68.97 | -0.97% | 5.22x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | NIGHT/USD ⭐ | 0.04842 | 65.84 | +0.48% | 2.19x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 7 | LUNA/USD | 4.563e-05 | 52.54 | -1.39% | 1.60x | WEAK 36/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | GBP/USD | 1.30834 | 51.18 | +0.03% | 0.34x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 9 | BAT/USD | 0.07786 | 34.80 | -0.23% | 0.92x | WEAK 22/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | BABY/USD | 0.00869 | 32.25 | +0.58% | 0.26x | WEAK 36/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 499.96 | 77.99 | +0.14% | 2.54x | 10965 | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04834 | 48.87 | +0.35% | 1.80x | 12332 | STRONG 79/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
