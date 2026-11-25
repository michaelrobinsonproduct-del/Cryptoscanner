# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T06:07:26.607763+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45557934671
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 12d6cbdaaeaf43c3b925a44d0357dcf08cd4fc82 (atomic ledger/results publication)
**Ledger generation:** 1679 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01004 | 90.191 | 85.662 | +6.02% | +0.30% | 1.30x | 10.0 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 2 | VVV/USD | 25.04 | 82.710 | 65.326 | +2.05% | +0.48% | 4.87x | 8.0 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | DRV/USD | 0.33034 | 62.030 | 70.690 | +5.11% | -0.59% | 0.43x | 4.2 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | BABY/USD | 0.00871 | 61.600 | 64.785 | +5.45% | -0.34% | 0.85x | 11.4 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | PEPE/USD | 3.5e-06 | 61.306 | 50.212 | +1.36% | +0.55% | 1.84x | 5.7 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 510.93 | 55.457 | 46.809 | +0.26% | +0.18% | 1.78x | 17.1 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SKY/USD | 0.04165 | 47.616 | 41.730 | +1.63% | +1.52% | 0.83x | 7.2 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 8 | PENGU/USD | 0.004235 | 41.693 | 34.350 | +0.45% | +0.09% | 1.69x | 4.7 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | MODERATE 56/100 | HIGH 60/100 | Watch | WATCH |
| 9 | RE/USD | 0.20424 | 38.842 | 32.300 | +1.80% | +0.81% | 1.25x | 22.1 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | WEAK 44/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | SYRUP/USD | 0.07115 | 34.235 | 34.665 | +2.12% | -0.45% | 1.18x | 23.9 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | WEAK 17/100 | EXTREME 85/100 | Do nothing | WATCH |
| 11 | CAP/USD | 0.092893 | 29.642 | 29.908 | +0.51% | +0.85% | 0.55x | 11.9 | 2026-11-25T06:07:18.063699+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.662 | 0.01004 | +0.30% | 1.30x |
| 2 | DRV/USD | 70.690 | 0.33034 | -0.59% | 0.43x |
| 3 | VVV/USD | 65.326 | 25.04 | +0.48% | 4.87x |
| 4 | BABY/USD | 64.785 | 0.00871 | -0.34% | 0.85x |
| 5 | PEPE/USD | 50.212 | 3.5e-06 | +0.55% | 1.84x |
| 6 | XMR/USD | 46.809 | 510.93 | +0.18% | 1.78x |
| 7 | SKY/USD | 41.730 | 0.04165 | +1.52% | 0.83x |
| 8 | SYRUP/USD | 34.665 | 0.07115 | -0.45% | 1.18x |
| 9 | PENGU/USD | 34.350 | 0.004235 | +0.09% | 1.69x |
| 10 | RE/USD | 32.300 | 0.20424 | +0.81% | 1.25x |
| 11 | CAP/USD | 29.908 | 0.092893 | +0.85% | 0.55x |

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

- Persisted scans: 1679; predictions: 14253; observations: 1017602.
- Matured sampled outcomes across 1/6/24/48h: 30340; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45557934671 · **Generation:** 1679 · **Legacy run:** 45557934671
**Main quote time:** 2026-11-25T06:07:26.607763+00:00 · **Legacy report time:** 2026-11-25T06:08:22.437300+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01004 | 90.19 | +0.30% | 1.30x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD ⭐ | 25.04 | 82.71 | +0.48% | 4.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | DRV/USD | 0.33034 | 62.03 | -0.59% | 0.43x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 4 | BABY/USD | 0.00871 | 61.60 | -0.34% | 0.85x | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | PEPE/USD ⭐ | 3.5e-06 | 61.31 | +0.55% | 1.84x | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 6 | XMR/USD | 510.93 | 55.46 | +0.18% | 1.78x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | SKY/USD | 0.04165 | 47.62 | +1.52% | 0.83x | MODERATE 54/100 | HIGH 67/100 | Watch |
| 8 | PENGU/USD | 0.004235 | 41.69 | +0.09% | 1.69x | MODERATE 56/100 | HIGH 60/100 | Watch |
| 9 | RE/USD ⭐ | 0.20424 | 38.84 | +0.81% | 1.25x | MODERATE 54/100 | EXTREME 86/100 | Do nothing |
| 10 | SYRUP/USD | 0.07115 | 34.23 | -0.45% | 1.18x | WEAK 17/100 | EXTREME 85/100 | Do nothing |
| 11 | CAP/USD | 0.092893 | 29.64 | +0.85% | 0.55x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01004 | 83.22 | +0.30% | 1.30x | 18604 | STRONG 97/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD ⭐ | 25.016 | 69.81 | +0.48% | 4.87x | 15197 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEPE/USD ⭐ | 3.5e-06 | 51.45 | +0.55% | 1.84x | 5356 | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 4 | RE/USD ⭐ | 0.20407 | 36.83 | +0.81% | 1.25x | 1481 | MODERATE 58/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** MON/USD, VVV/USD, PEPE/USD, RE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
