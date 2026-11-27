# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T15:12:16.348710+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46022367844
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 02d8d13744a2c1a4cd90bb9fc9cd51cc86ef0656 (atomic ledger/results publication)
**Ledger generation:** 2024 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 728.53 | 102.418 | 92.930 | +6.88% | -1.10% | 2.73x | 14.1 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | VVV/USD | 26.826 | 74.639 | 63.669 | +2.46% | -0.12% | 2.16x | 10.1 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 3 | SOL/USD | 71.35 | 72.072 | 58.345 | +0.58% | -0.25% | 3.00x | 1.4 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.79 | 69.730 | 70.315 | +2.52% | -0.57% | 1.22x | 4.7 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 5 | FET/USD | 0.1264 | 68.853 | 55.455 | +4.98% | -0.32% | 4.79x | 31.6 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 6 | LIGHTER/USD | 2.613 | 64.677 | 58.300 | +5.28% | -0.96% | 2.12x | 23.0 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 7 | RENDER/USD | 1.364 | 58.745 | 42.267 | +2.33% | +0.30% | 16.86x | 14.7 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | STRONG 79/100 | HIGH 66/100 | Watch | WATCH |
| 8 | INJ/USD | 6.262 | 58.366 | 46.333 | +1.13% | -0.59% | 2.54x | 6.4 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XDG/USD | 0.057026 | 55.020 | 55.280 | +1.16% | -0.22% | 1.08x | 3.2 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PAXG/USD | 3614.96 | 51.281 | 52.936 | +1.64% | -0.43% | 1.05x | 0.2 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 11 | UNI/USD | 4.7329 | 49.195 | 60.104 | +1.78% | -0.51% | 0.16x | 10.1 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 12 | KAVA/USD | 0.0267 | 48.997 | 57.384 | +7.23% | -1.48% | 0.90x | 37.3 | 2026-11-27T15:12:07.897896+00:00 | Not calibrated | WEAK 14/100 | EXTREME 96/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 92.930 | 728.53 | -1.10% | 2.73x |
| 2 | HYPE/USD | 70.315 | 63.79 | -0.57% | 1.22x |
| 3 | VVV/USD | 63.669 | 26.826 | -0.12% | 2.16x |
| 4 | UNI/USD | 60.104 | 4.7329 | -0.51% | 0.16x |
| 5 | SOL/USD | 58.345 | 71.35 | -0.25% | 3.00x |
| 6 | LIGHTER/USD | 58.300 | 2.613 | -0.96% | 2.12x |
| 7 | KAVA/USD | 57.384 | 0.0267 | -1.48% | 0.90x |
| 8 | FET/USD | 55.455 | 0.1264 | -0.32% | 4.79x |
| 9 | XDG/USD | 55.280 | 0.057026 | -0.22% | 1.08x |
| 10 | PAXG/USD | 52.936 | 3614.96 | -0.43% | 1.05x |
| 11 | INJ/USD | 46.333 | 6.262 | -0.59% | 2.54x |
| 12 | RENDER/USD | 42.267 | 1.364 | +0.30% | 16.86x |

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

- Persisted scans: 2024; predictions: 17990; observations: 1225629.
- Matured sampled outcomes across 1/6/24/48h: 40193; gap abstentions: 25919. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46022367844 · **Generation:** 2024 · **Legacy run:** 46022367844
**Main quote time:** 2026-11-27T15:12:16.348710+00:00 · **Legacy report time:** 2026-11-27T15:13:01.079035+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 728.53 | 102.42 | -1.10% | 2.73x | STRONG 75/100 | VERY_HIGH 71/100 | Watch |
| 2 | VVV/USD | 26.826 | 74.64 | -0.12% | 2.16x | MODERATE 62/100 | HIGH 67/100 | Watch |
| 3 | SOL/USD | 71.35 | 72.07 | -0.25% | 3.00x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | HYPE/USD | 63.79 | 69.73 | -0.57% | 1.22x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 5 | FET/USD | 0.1264 | 68.85 | -0.32% | 4.79x | MODERATE 54/100 | VERY_HIGH 78/100 | Watch |
| 6 | LIGHTER/USD | 2.613 | 64.68 | -0.96% | 2.12x | MODERATE 52/100 | VERY_HIGH 78/100 | Watch |
| 7 | RENDER/USD | 1.364 | 58.74 | +0.30% | 16.86x | STRONG 79/100 | HIGH 66/100 | Watch |
| 8 | INJ/USD | 6.262 | 58.37 | -0.59% | 2.54x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 9 | XDG/USD | 0.057026 | 55.02 | -0.22% | 1.08x | WEAK 38/100 | HIGH 68/100 | Watch |
| 10 | PAXG/USD | 3614.96 | 51.28 | -0.43% | 1.05x | WEAK 36/100 | HIGH 68/100 | Watch |
| 11 | UNI/USD | 4.7329 | 49.19 | -0.51% | 0.16x | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing |
| 12 | KAVA/USD | 0.0267 | 49.00 | -1.48% | 0.90x | WEAK 14/100 | EXTREME 96/100 | Do nothing |

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
