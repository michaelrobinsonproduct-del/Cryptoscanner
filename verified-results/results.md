# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:40:21.899049+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44600602184
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** a90885ee6712bcb78c1491991e2e4bf0b9f479a9 (atomic ledger/results publication)
**Ledger generation:** 846 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.505 | 74.166 | 79.938 | +3.85% | -0.31% | 0.58x | 4.0 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010128 | 73.109 | 64.144 | +5.14% | -0.14% | 1.97x | 5.9 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | CT/USD | 0.1305 | 67.990 | 65.355 | +10.41% | +0.85% | 0.84x | 23.1 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5504 | 65.973 | 71.331 | +6.25% | +0.07% | 0.43x | 9.1 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05898 | 56.222 | 63.440 | +5.32% | +0.03% | 0.26x | 11.9 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.05394 | 55.451 | 42.482 | +2.24% | -0.41% | 2.53x | 11.1 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ADA/USD | 0.15276 | 53.440 | 59.941 | +1.00% | -0.03% | 0.36x | 4.1 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 67.55 | 51.725 | 59.791 | +1.00% | -0.56% | 0.47x | 4.4 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | ONDO/USD | 0.29842 | 49.634 | 36.287 | +0.26% | -0.33% | 12.37x | 3.0 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 10 | SHIB/USD | 3.823e-06 | 49.574 | 34.312 | +0.76% | +0.05% | 5.87x | 7.8 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 11 | SENT/USD | 0.021377 | 47.401 | 56.786 | +3.75% | -0.60% | 0.36x | 7.5 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | INJ/USD | 7.073 | 43.722 | 52.208 | +1.32% | +0.04% | 0.13x | 4.2 | 2026-11-19T19:40:13.581888+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.938 | 22.505 | -0.31% | 0.58x |
| 2 | AKT/USD | 71.331 | 0.5504 | +0.07% | 0.43x |
| 3 | CT/USD | 65.355 | 0.1305 | +0.85% | 0.84x |
| 4 | SKR/USD | 64.144 | 0.010128 | -0.14% | 1.97x |
| 5 | MEGA/USD | 63.440 | 0.05898 | +0.03% | 0.26x |
| 6 | ADA/USD | 59.941 | 0.15276 | -0.03% | 0.36x |
| 7 | HYPE/USD | 59.791 | 67.55 | -0.56% | 0.47x |
| 8 | SENT/USD | 56.786 | 0.021377 | -0.60% | 0.36x |
| 9 | INJ/USD | 52.208 | 7.073 | +0.04% | 0.13x |
| 10 | PYTH/USD | 42.482 | 0.05394 | -0.41% | 2.53x |
| 11 | ONDO/USD | 36.287 | 0.29842 | -0.33% | 12.37x |
| 12 | SHIB/USD | 34.312 | 3.823e-06 | +0.05% | 5.87x |

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

- Persisted scans: 846; predictions: 7296; observations: 511331.
- Matured sampled outcomes across 1/6/24/48h: 7307; gap abstentions: 15612. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44600602184 · **Generation:** 846 · **Legacy run:** 44600602184
**Main quote time:** 2026-11-19T19:40:21.899049+00:00 · **Legacy report time:** 2026-11-19T19:41:02.275340+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.505 | 74.17 | -0.31% | 0.58x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 2 | SKR/USD | 0.010128 | 73.11 | -0.14% | 1.97x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 3 | CT/USD | 0.1305 | 67.99 | +0.85% | 0.84x | MODERATE 54/100 | VERY_HIGH 79/100 | Watch |
| 4 | AKT/USD | 0.5504 | 65.97 | +0.07% | 0.43x | MODERATE 53/100 | VERY_HIGH 75/100 | Watch |
| 5 | MEGA/USD | 0.05898 | 56.22 | +0.03% | 0.26x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |
| 6 | PYTH/USD | 0.05394 | 55.45 | -0.41% | 2.53x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 7 | ADA/USD | 0.15276 | 53.44 | -0.03% | 0.36x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | HYPE/USD | 67.55 | 51.72 | -0.56% | 0.47x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | ONDO/USD | 0.29842 | 49.63 | -0.33% | 12.37x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 10 | SHIB/USD | 3.823e-06 | 49.57 | +0.05% | 5.87x | STRONG 70/100 | HIGH 60/100 | Watch |
| 11 | SENT/USD | 0.021377 | 47.40 | -0.60% | 0.36x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | INJ/USD | 7.073 | 43.72 | +0.04% | 0.13x | WEAK 42/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.942e-05 | 77.02 | +0.59% | 1.19x | 6652 | MODERATE 59/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
