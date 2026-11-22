# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T13:11:04.985933+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45025998530
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** fd253adf8084fc6e87d2c6b209b6bd3143fae6fd (atomic ledger/results publication)
**Ledger generation:** 1287 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 191.584 | 87.321 | 72.166 | +3.15% | +0.15% | 2.44x | 5.0 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.0468 | 74.963 | 77.465 | +5.69% | +0.09% | 0.71x | 15.0 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | DRV/USD | 0.35988 | 74.734 | 85.761 | +7.36% | -1.91% | 0.85x | 2.2 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 4 | PUMP/USD | 0.002493 | 70.838 | 81.333 | +6.36% | -0.40% | 0.15x | 12.0 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | HYPE/USD | 62.76 | 70.540 | 70.779 | +2.48% | -0.02% | 0.98x | 3.2 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | INJ/USD | 6.261 | 69.778 | 74.036 | +4.82% | -0.06% | 0.61x | 4.8 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9837 | 67.300 | 76.945 | +3.37% | -0.23% | 0.15x | 3.4 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | VVV/USD | 25.536 | 61.498 | 67.383 | +2.55% | +0.51% | 0.16x | 11.0 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ZEC/USD | 792.32 | 60.319 | 66.024 | +1.82% | +0.29% | 0.29x | 3.4 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SUI/USD | 0.658 | 56.914 | 65.811 | +1.65% | -0.26% | 0.24x | 1.5 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1701.08 | 53.926 | 62.793 | +1.12% | -0.25% | 0.24x | 0.1 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XBT/USD | 60606.8 | 52.958 | 61.013 | +0.86% | -0.15% | 0.27x | 0.0 | 2026-11-22T13:10:59.256174+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 85.761 | 0.35988 | -1.91% | 0.85x |
| 2 | PUMP/USD | 81.333 | 0.002493 | -0.40% | 0.15x |
| 3 | NIGHT/USD | 77.465 | 0.0468 | +0.09% | 0.71x |
| 4 | NEAR/USD | 76.945 | 2.9837 | -0.23% | 0.15x |
| 5 | INJ/USD | 74.036 | 6.261 | -0.06% | 0.61x |
| 6 | TAO/USD | 72.166 | 191.584 | +0.15% | 2.44x |
| 7 | HYPE/USD | 70.779 | 62.76 | -0.02% | 0.98x |
| 8 | VVV/USD | 67.383 | 25.536 | +0.51% | 0.16x |
| 9 | ZEC/USD | 66.024 | 792.32 | +0.29% | 0.29x |
| 10 | SUI/USD | 65.811 | 0.658 | -0.26% | 0.24x |
| 11 | ETH/USD | 62.793 | 1701.08 | -0.25% | 0.24x |
| 12 | XBT/USD | 61.013 | 60606.8 | -0.15% | 0.27x |

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

- Persisted scans: 1287; predictions: 10364; observations: 778892.
- Matured sampled outcomes across 1/6/24/48h: 15005; gap abstentions: 22253. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45025998530 · **Generation:** 1287 · **Legacy run:** 45025998530
**Main quote time:** 2026-11-22T13:11:04.985933+00:00 · **Legacy report time:** 2026-11-22T13:11:49.943573+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 191.584 | 87.32 | +0.15% | 2.44x | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.0468 | 74.96 | +0.09% | 0.71x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 3 | DRV/USD | 0.35988 | 74.73 | -1.91% | 0.85x | WEAK 42/100 | VERY_HIGH 72/100 | Do nothing |
| 4 | PUMP/USD | 0.002493 | 70.84 | -0.40% | 0.15x | WEAK 35/100 | VERY_HIGH 82/100 | Watch |
| 5 | HYPE/USD | 62.76 | 70.54 | -0.02% | 0.98x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | INJ/USD | 6.261 | 69.78 | -0.06% | 0.61x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | NEAR/USD | 2.9837 | 67.30 | -0.23% | 0.15x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 8 | VVV/USD | 25.536 | 61.50 | +0.51% | 0.16x | MODERATE 56/100 | VERY_HIGH 76/100 | Watch |
| 9 | ZEC/USD | 792.32 | 60.32 | +0.29% | 0.29x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | SUI/USD | 0.658 | 56.91 | -0.26% | 0.24x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1701.08 | 53.93 | -0.25% | 0.24x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XBT/USD | 60606.8 | 52.96 | -0.15% | 0.27x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 191.6111 | 79.79 | +0.15% | 2.44x | 6555 | STRONG 95/100 | HIGH 55/100 | Watch |

**Same-run overlap:** TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
