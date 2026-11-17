# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T12:23:55.463886+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44082667193
**Source SHA:** 51cf90dde69583431478c570c3fd0bfd47a88250
**Previous ledger commit:** 4b482102e757b11486a51546ae8d1655afabeded (atomic ledger/results publication)
**Ledger generation:** 454 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.623 | 103.809 | 93.454 | +10.49% | +1.08% | 1.50x | 3.9 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 948.03 | 87.458 | 87.297 | +4.89% | +0.46% | 0.79x | 3.9 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 3 | VVV/USD | 21.543 | 84.725 | 86.968 | +6.92% | -0.12% | 0.84x | 6.0 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XMR/USD | 514.89 | 82.664 | 77.430 | +4.32% | -0.32% | 1.68x | 15.6 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.299 | 82.302 | 83.875 | +4.47% | +0.34% | 0.67x | 4.9 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | UNI/USD | 5.3487 | 81.862 | 66.937 | +3.63% | -0.01% | 4.19x | 5.2 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.96961 | 81.462 | 65.836 | +1.56% | +0.13% | 8.52x | 0.1 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LUNA/USD | 4.122e-05 | 74.782 | 68.467 | +10.51% | +0.39% | 1.44x | 16.9 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 9 | SOL/USD | 73.15 | 73.160 | 70.270 | +2.28% | -0.05% | 1.32x | 1.4 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 10 | AAVE/USD | 113.57 | 68.162 | 72.030 | +4.69% | -0.12% | 0.67x | 5.3 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | JUP/USD | 0.26153 | 65.895 | 73.522 | +8.72% | -0.96% | 0.72x | 12.6 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | BAT/USD | 0.10028 | 63.837 | 66.215 | +5.87% | +0.10% | 0.71x | 12.0 | 2026-11-17T12:23:46.793920+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 93.454 | 7.623 | +1.08% | 1.50x |
| 2 | ZEC/USD | 87.297 | 948.03 | +0.46% | 0.79x |
| 3 | VVV/USD | 86.968 | 21.543 | -0.12% | 0.84x |
| 4 | NEAR/USD | 83.875 | 3.299 | +0.34% | 0.67x |
| 5 | XMR/USD | 77.430 | 514.89 | -0.32% | 1.68x |
| 6 | JUP/USD | 73.522 | 0.26153 | -0.96% | 0.72x |
| 7 | AAVE/USD | 72.030 | 113.57 | -0.12% | 0.67x |
| 8 | SOL/USD | 70.270 | 73.15 | -0.05% | 1.32x |
| 9 | LUNA/USD | 68.467 | 4.122e-05 | +0.39% | 1.44x |
| 10 | UNI/USD | 66.937 | 5.3487 | -0.01% | 4.19x |
| 11 | BAT/USD | 66.215 | 0.10028 | +0.10% | 0.71x |
| 12 | XRP/USD | 65.836 | 0.96961 | +0.13% | 8.52x |

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

- Persisted scans: 454; predictions: 3929; observations: 273493.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12149. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44082667193 · **Generation:** 454 · **Legacy run:** 44082667193
**Main quote time:** 2026-11-17T12:23:55.463886+00:00 · **Legacy report time:** 2026-11-17T12:24:05.645866+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.623 | 103.81 | +1.08% | 1.50x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 948.03 | 87.46 | +0.46% | 0.79x | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD | 21.543 | 84.72 | -0.12% | 0.84x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 4 | XMR/USD | 514.89 | 82.66 | -0.32% | 1.68x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 5 | NEAR/USD | 3.299 | 82.30 | +0.34% | 0.67x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 6 | UNI/USD | 5.3487 | 81.86 | -0.01% | 4.19x | STRONG 71/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD ⭐ | 0.96961 | 81.46 | +0.13% | 8.52x | STRONG 96/100 | HIGH 55/100 | Watch |
| 8 | LUNA/USD | 4.122e-05 | 74.78 | +0.39% | 1.44x | STRONG 77/100 | HIGH 66/100 | Watch |
| 9 | SOL/USD | 73.15 | 73.16 | -0.05% | 1.32x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 10 | AAVE/USD | 113.57 | 68.16 | -0.12% | 0.67x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 11 | JUP/USD | 0.26153 | 65.90 | -0.96% | 0.72x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 12 | BAT/USD | 0.10028 | 63.84 | +0.10% | 0.71x | MODERATE 47/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.624 | 91.98 | +1.08% | 1.50x | 8427 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD ⭐ | 0.96998 | 79.30 | +0.13% | 8.52x | 31101 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | TRUMP/USD | 0.983 | 78.12 | +1.03% | 1.59x | 3089 | STRONG 79/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** INJ/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
