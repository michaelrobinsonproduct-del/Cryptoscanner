# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T20:00:32.950167+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44604000880
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** cf0308170fb60d208b7e98ae250d9e91cc2ca83e (atomic ledger/results publication)
**Ledger generation:** 850 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5561 | 92.915 | 71.840 | +7.36% | +1.22% | 4.29x | 10.8 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | STRONG 96/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.43 | 87.613 | 74.387 | +3.50% | -0.35% | 7.84x | 10.3 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 3 | SKR/USD | 0.010083 | 67.161 | 56.897 | +4.67% | -0.47% | 2.26x | 13.9 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152539 | 65.576 | 57.964 | +0.85% | -0.26% | 1.89x | 6.0 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.53 | 54.318 | 60.322 | +0.97% | -0.47% | 0.64x | 3.0 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | CT/USD | 0.1288 | 52.828 | 65.242 | +8.97% | -0.62% | 0.07x | 23.3 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 21/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | TRX/USD | 0.310132 | 45.544 | 42.473 | +0.28% | -0.09% | 1.35x | 1.0 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 8 | INJ/USD | 7.072 | 44.585 | 51.812 | +1.30% | -0.28% | 0.42x | 4.2 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SENT/USD | 0.021108 | 43.339 | 47.319 | +2.44% | -1.11% | 1.16x | 8.1 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 10 | PYTH/USD | 0.05389 | 40.997 | 40.896 | +2.14% | -0.28% | 1.15x | 13.0 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | TIA/USD | 0.3458 | 36.543 | 30.860 | +0.35% | -0.17% | 1.65x | 5.8 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 12 | ONDO/USD | 0.29913 | 30.216 | 37.559 | +0.50% | +0.00% | 0.26x | 4.0 | 2026-11-19T20:00:23.650903+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 74.387 | 22.43 | -0.35% | 7.84x |
| 2 | AKT/USD | 71.840 | 0.5561 | +1.22% | 4.29x |
| 3 | CT/USD | 65.242 | 0.1288 | -0.62% | 0.07x |
| 4 | HYPE/USD | 60.322 | 67.53 | -0.47% | 0.64x |
| 5 | ADA/USD | 57.964 | 0.152539 | -0.26% | 1.89x |
| 6 | SKR/USD | 56.897 | 0.010083 | -0.47% | 2.26x |
| 7 | INJ/USD | 51.812 | 7.072 | -0.28% | 0.42x |
| 8 | SENT/USD | 47.319 | 0.021108 | -1.11% | 1.16x |
| 9 | TRX/USD | 42.473 | 0.310132 | -0.09% | 1.35x |
| 10 | PYTH/USD | 40.896 | 0.05389 | -0.28% | 1.15x |
| 11 | ONDO/USD | 37.559 | 0.29913 | +0.00% | 0.26x |
| 12 | TIA/USD | 30.860 | 0.3458 | -0.17% | 1.65x |

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

- Persisted scans: 850; predictions: 7344; observations: 513727.
- Matured sampled outcomes across 1/6/24/48h: 7391; gap abstentions: 15631. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44604000880 · **Generation:** 850 · **Legacy run:** 44604000880
**Main quote time:** 2026-11-19T20:00:32.950167+00:00 · **Legacy report time:** 2026-11-19T20:01:35.967437+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5561 | 92.92 | +1.22% | 4.29x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD | 22.43 | 87.61 | -0.35% | 7.84x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 3 | SKR/USD | 0.010083 | 67.16 | -0.47% | 2.26x | MODERATE 59/100 | VERY_HIGH 79/100 | Watch |
| 4 | ADA/USD | 0.152539 | 65.58 | -0.26% | 1.89x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD | 67.53 | 54.32 | -0.47% | 0.64x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | CT/USD | 0.1288 | 52.83 | -0.62% | 0.07x | WEAK 21/100 | EXTREME 93/100 | Do nothing |
| 7 | TRX/USD | 0.310132 | 45.54 | -0.09% | 1.35x | WEAK 43/100 | HIGH 61/100 | Watch |
| 8 | INJ/USD | 7.072 | 44.59 | -0.28% | 0.42x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SENT/USD | 0.021108 | 43.34 | -1.11% | 1.16x | WEAK 32/100 | VERY_HIGH 77/100 | Do nothing |
| 10 | PYTH/USD | 0.05389 | 41.00 | -0.28% | 1.15x | WEAK 25/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | TIA/USD | 0.3458 | 36.54 | -0.17% | 1.65x | WEAK 38/100 | VERY_HIGH 73/100 | Watch |
| 12 | ONDO/USD | 0.29913 | 30.22 | +0.00% | 0.26x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5561 | 82.99 | +1.22% | 4.29x | 3368 | STRONG 100/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
