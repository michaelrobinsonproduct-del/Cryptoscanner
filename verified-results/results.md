# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T04:01:30.655898+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45937296893
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4585af00e0957a723032c97db8248d1bf60a9476 (atomic ledger/results publication)
**Ledger generation:** 1956 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.98 | 101.794 | 96.544 | +6.04% | +0.27% | 1.39x | 1.5 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 758.03 | 88.903 | 94.060 | +11.20% | +0.32% | 0.33x | 11.9 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | LINK/USD | 9.48467 | 83.636 | 69.825 | +2.33% | -0.12% | 2.44x | 3.0 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.63 | 79.370 | 70.988 | +2.38% | -0.16% | 1.92x | 1.4 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 27.115 | 72.486 | 75.489 | +3.56% | +0.24% | 0.58x | 8.9 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | W/USD | 0.00957 | 71.542 | 72.162 | +8.63% | -0.52% | 1.20x | 10.5 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | XBT/USD | 61358.9 | 66.269 | 64.953 | +1.42% | -0.09% | 1.18x | 0.0 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ETH/USD | 1727.8 | 64.497 | 71.612 | +2.38% | +0.02% | 0.28x | 0.1 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95923 | 62.774 | 67.184 | +1.75% | -0.18% | 0.65x | 0.1 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | LTC/USD | 44.37 | 60.461 | 63.599 | +1.44% | -0.07% | 0.72x | 2.3 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XMR/USD | 465.68 | 59.557 | 64.616 | +1.91% | -0.02% | 0.50x | 7.5 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6794 | 56.291 | 66.130 | +1.75% | -0.13% | 0.08x | 1.5 | 2026-11-27T04:01:24.077119+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 96.544 | 65.98 | +0.27% | 1.39x |
| 2 | ZEC/USD | 94.060 | 758.03 | +0.32% | 0.33x |
| 3 | VVV/USD | 75.489 | 27.115 | +0.24% | 0.58x |
| 4 | W/USD | 72.162 | 0.00957 | -0.52% | 1.20x |
| 5 | ETH/USD | 71.612 | 1727.8 | +0.02% | 0.28x |
| 6 | SOL/USD | 70.988 | 72.63 | -0.16% | 1.92x |
| 7 | LINK/USD | 69.825 | 9.48467 | -0.12% | 2.44x |
| 8 | XRP/USD | 67.184 | 0.95923 | -0.18% | 0.65x |
| 9 | SUI/USD | 66.130 | 0.6794 | -0.13% | 0.08x |
| 10 | XBT/USD | 64.953 | 61358.9 | -0.09% | 1.18x |
| 11 | XMR/USD | 64.616 | 465.68 | -0.02% | 0.50x |
| 12 | LTC/USD | 63.599 | 44.37 | -0.07% | 0.72x |

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

- Persisted scans: 1956; predictions: 17174; observations: 1184640.
- Matured sampled outcomes across 1/6/24/48h: 37778; gap abstentions: 25491. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45937296893 · **Generation:** 1956 · **Legacy run:** 45937296893
**Main quote time:** 2026-11-27T04:01:30.655898+00:00 · **Legacy report time:** 2026-11-27T04:02:20.695387+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.98 | 101.79 | +0.27% | 1.39x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 758.03 | 88.90 | +0.32% | 0.33x | MODERATE 69/100 | VERY_HIGH 76/100 | Watch |
| 3 | LINK/USD | 9.48467 | 83.64 | -0.12% | 2.44x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.63 | 79.37 | -0.16% | 1.92x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD | 27.115 | 72.49 | +0.24% | 0.58x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 6 | W/USD | 0.00957 | 71.54 | -0.52% | 1.20x | WEAK 41/100 | VERY_HIGH 79/100 | Watch |
| 7 | XBT/USD | 61358.9 | 66.27 | -0.09% | 1.18x | WEAK 43/100 | HIGH 68/100 | Watch |
| 8 | ETH/USD | 1727.8 | 64.50 | +0.02% | 0.28x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.95923 | 62.77 | -0.18% | 0.65x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | LTC/USD | 44.37 | 60.46 | -0.07% | 0.72x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | XMR/USD | 465.68 | 59.56 | -0.02% | 0.50x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | SUI/USD | 0.6794 | 56.29 | -0.13% | 0.08x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.92 | 96.30 | +0.27% | 1.39x | 14709 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
