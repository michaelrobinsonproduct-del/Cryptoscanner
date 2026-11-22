# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:10:57.909086+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44970110489
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 2e46081016cccf6c0906ea22f1c189d0f2fc835f (atomic ledger/results publication)
**Ledger generation:** 1212 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.34287 | 67.810 | 46.184 | +2.29% | +3.87% | 1.23x | 35.0 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 84/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9002 | 64.171 | 57.165 | +0.48% | +0.29% | 1.56x | 2.4 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | BNB/USD | 549.5 | 61.786 | 46.212 | +0.38% | +0.11% | 5.61x | 1.6 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 4 | RENDER/USD | 1.31 | 49.799 | 33.650 | +0.46% | +0.23% | 4.19x | 15.3 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 25.081 | 49.449 | 56.697 | +0.73% | +0.07% | 0.24x | 6.8 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | TRUMP/USD | 0.89 | 45.834 | 32.680 | +0.45% | +0.23% | 2.20x | 11.2 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 7 | CAP/USD | 0.092979 | 39.343 | 40.569 | +1.11% | +0.25% | 0.75x | 6.1 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 8 | BLUR/USD | 0.00709 | 22.985 | 25.824 | +0.28% | +0.57% | 0.43x | 14.1 | 2026-11-22T01:10:50.226427+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 57.165 | 2.9002 | +0.29% | 1.56x |
| 2 | VVV/USD | 56.697 | 25.081 | +0.07% | 0.24x |
| 3 | BNB/USD | 46.212 | 549.5 | +0.11% | 5.61x |
| 4 | DRV/USD | 46.184 | 0.34287 | +3.87% | 1.23x |
| 5 | CAP/USD | 40.569 | 0.092979 | +0.25% | 0.75x |
| 6 | RENDER/USD | 33.650 | 1.31 | +0.23% | 4.19x |
| 7 | TRUMP/USD | 32.680 | 0.89 | +0.23% | 2.20x |
| 8 | BLUR/USD | 25.824 | 0.00709 | +0.57% | 0.43x |

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

- Persisted scans: 1212; predictions: 9804; observations: 733254.
- Matured sampled outcomes across 1/6/24/48h: 13353; gap abstentions: 21781. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 17 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44970110489 · **Generation:** 1212 · **Legacy run:** 44970110489
**Main quote time:** 2026-11-22T01:10:57.909086+00:00 · **Legacy report time:** 2026-11-22T01:12:03.246347+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34287 | 67.81 | +3.87% | 1.23x | MODERATE 64/100 | VERY_HIGH 84/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.9002 | 64.17 | +0.29% | 1.56x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 3 | BNB/USD ⭐ | 549.5 | 61.79 | +0.11% | 5.61x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | RENDER/USD | 1.31 | 49.80 | +0.23% | 4.19x | STRONG 75/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD | 25.081 | 49.45 | +0.07% | 0.24x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 6 | TRUMP/USD | 0.89 | 45.83 | +0.23% | 2.20x | STRONG 73/100 | HIGH 66/100 | Watch |
| 7 | CAP/USD | 0.092979 | 39.34 | +0.25% | 0.75x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 8 | BLUR/USD | 0.00709 | 22.99 | +0.57% | 0.43x | WEAK 36/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34341 | 70.94 | +3.87% | 1.23x | 16080 | STRONG 70/100 | VERY_HIGH 84/100 | Watch |
| 2 | ZEC/USD | 780.39 | 63.43 | +0.09% | 3.10x | 39772 | STRONG 77/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 61.38 | 59.83 | +0.11% | 5.43x | 28122 | STRONG 75/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 2.908 | 58.61 | +0.29% | 1.56x | 20615 | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 5 | LTC/USD | 39.78 | 56.72 | +0.20% | 3.67x | 14299 | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | BNB/USD ⭐ | 549.5 | 55.99 | +0.11% | 5.61x | 7071 | STRONG 83/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, NEAR/USD, BNB/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
