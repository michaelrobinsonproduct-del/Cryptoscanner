# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T20:30:54.225967+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45891409094
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 67d8c70297c57d3f22c6c697f06b1d1680070a78 (atomic ledger/results publication)
**Ledger generation:** 1910 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04597 | 85.747 | 77.474 | +9.77% | -0.09% | 1.87x | 4.4 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95256 | 82.253 | 66.906 | +1.71% | +0.07% | 2.63x | 0.1 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZRO/USD | 1.101 | 77.359 | 75.788 | +7.52% | -0.54% | 1.43x | 9.1 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 4 | WIF/USD | 0.1384 | 76.465 | 73.238 | +8.72% | +0.14% | 1.25x | 7.2 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | MODERATE 63/100 | HIGH 60/100 | Watch | WATCH |
| 5 | QNT/USD | 148.8 | 76.246 | 61.044 | +2.76% | +0.04% | 3.16x | 0.7 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HBAR/USD | 0.05503 | 75.641 | 71.568 | +5.62% | +0.16% | 1.33x | 5.5 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 7 | ADA/USD | 0.150686 | 72.915 | 77.080 | +3.37% | -0.01% | 0.59x | 3.1 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LTC/USD | 43.74 | 68.732 | 70.738 | +2.41% | +0.32% | 0.64x | 2.3 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | DRV/USD | 0.38621 | 66.118 | 77.403 | +7.94% | -0.79% | 0.27x | 10.1 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | XDG/USD | 0.0569539 | 62.809 | 57.067 | +1.78% | -0.04% | 1.59x | 0.5 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 11 | FET/USD | 0.1197 | 62.182 | 70.368 | +10.32% | -0.67% | 0.51x | 16.7 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | XBT/USD | 60623.9 | 60.652 | 57.952 | +0.42% | -0.02% | 1.28x | 0.0 | 2026-11-26T20:30:48.236571+00:00 | Not calibrated | WEAK 40/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 77.474 | 0.04597 | -0.09% | 1.87x |
| 2 | DRV/USD | 77.403 | 0.38621 | -0.79% | 0.27x |
| 3 | ADA/USD | 77.080 | 0.150686 | -0.01% | 0.59x |
| 4 | ZRO/USD | 75.788 | 1.101 | -0.54% | 1.43x |
| 5 | WIF/USD | 73.238 | 0.1384 | +0.14% | 1.25x |
| 6 | HBAR/USD | 71.568 | 0.05503 | +0.16% | 1.33x |
| 7 | LTC/USD | 70.738 | 43.74 | +0.32% | 0.64x |
| 8 | FET/USD | 70.368 | 0.1197 | -0.67% | 0.51x |
| 9 | XRP/USD | 66.906 | 0.95256 | +0.07% | 2.63x |
| 10 | QNT/USD | 61.044 | 148.8 | +0.04% | 3.16x |
| 11 | XBT/USD | 57.952 | 60623.9 | -0.02% | 1.28x |
| 12 | XDG/USD | 57.067 | 0.0569539 | -0.04% | 1.59x |

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

- Persisted scans: 1910; predictions: 16655; observations: 1157024.
- Matured sampled outcomes across 1/6/24/48h: 36140; gap abstentions: 25232. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45891409094 · **Generation:** 1910 · **Legacy run:** 45891409094
**Main quote time:** 2026-11-26T20:30:54.225967+00:00 · **Legacy report time:** 2026-11-26T20:31:30.824324+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.04597 | 85.75 | -0.09% | 1.87x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 2 | XRP/USD ⭐ | 0.95256 | 82.25 | +0.07% | 2.63x | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | ZRO/USD | 1.101 | 77.36 | -0.54% | 1.43x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 4 | WIF/USD | 0.1384 | 76.47 | +0.14% | 1.25x | MODERATE 63/100 | HIGH 60/100 | Watch |
| 5 | QNT/USD | 148.8 | 76.25 | +0.04% | 3.16x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | HBAR/USD ⭐ | 0.05503 | 75.64 | +0.16% | 1.33x | STRONG 83/100 | HIGH 60/100 | Watch |
| 7 | ADA/USD | 0.150686 | 72.91 | -0.01% | 0.59x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 8 | LTC/USD | 43.74 | 68.73 | +0.32% | 0.64x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | DRV/USD | 0.38621 | 66.12 | -0.79% | 0.27x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | XDG/USD | 0.0569539 | 62.81 | -0.04% | 1.59x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 11 | FET/USD | 0.1197 | 62.18 | -0.67% | 0.51x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 12 | XBT/USD | 60623.9 | 60.65 | -0.02% | 1.28x | WEAK 40/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08118 | 88.35 | +0.20% | 12.10x | 3592 | STRONG 89/100 | HIGH 60/100 | Watch |
| 2 | HBAR/USD ⭐ | 0.05507 | 82.49 | +0.16% | 1.33x | 4815 | STRONG 86/100 | HIGH 60/100 | Watch |
| 3 | HYPE/USD | 62.9 | 80.63 | +0.69% | 3.77x | 13349 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.95283 | 78.75 | +0.07% | 2.63x | 23866 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
