# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T18:11:08.924078+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45053456435
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 3c844d56a2be32a99f3785a454a13c44fe0f785a (atomic ledger/results publication)
**Ledger generation:** 1318 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 62.82 | 83.698 | 71.468 | +2.58% | -0.55% | 2.86x | 3.2 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0077 | 78.865 | 82.779 | +4.21% | -0.15% | 0.68x | 3.3 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | VVV/USD | 25.623 | 77.948 | 72.594 | +2.90% | +0.13% | 1.47x | 5.5 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | DRV/USD | 0.36629 | 74.821 | 80.012 | +9.28% | +0.15% | 0.41x | 18.1 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.00255 | 74.181 | 83.639 | +8.79% | -0.82% | 0.46x | 3.9 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ZBCN/USD | 0.001904 | 73.869 | 66.198 | +10.25% | +0.00% | 1.77x | 26.3 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ZEC/USD | 792.47 | 72.231 | 66.602 | +1.84% | -0.59% | 1.86x | 2.5 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1711.85 | 64.739 | 67.275 | +1.76% | -0.19% | 0.84x | 0.1 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | STBL/USD | 0.017031 | 63.344 | 67.024 | +6.42% | +0.36% | 0.45x | 17.6 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | AERO/USD | 0.4224 | 59.121 | 65.591 | +6.00% | -0.33% | 0.52x | 16.5 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.6575 | 57.239 | 64.508 | +1.58% | -0.20% | 0.37x | 3.0 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LINK/USD | 8.8178 | 54.931 | 62.125 | +2.59% | -0.18% | 0.37x | 2.2 | 2026-11-22T18:11:01.125943+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 83.639 | 0.00255 | -0.82% | 0.46x |
| 2 | NEAR/USD | 82.779 | 3.0077 | -0.15% | 0.68x |
| 3 | DRV/USD | 80.012 | 0.36629 | +0.15% | 0.41x |
| 4 | VVV/USD | 72.594 | 25.623 | +0.13% | 1.47x |
| 5 | HYPE/USD | 71.468 | 62.82 | -0.55% | 2.86x |
| 6 | ETH/USD | 67.275 | 1711.85 | -0.19% | 0.84x |
| 7 | STBL/USD | 67.024 | 0.017031 | +0.36% | 0.45x |
| 8 | ZEC/USD | 66.602 | 792.47 | -0.59% | 1.86x |
| 9 | ZBCN/USD | 66.198 | 0.001904 | +0.00% | 1.77x |
| 10 | AERO/USD | 65.591 | 0.4224 | -0.33% | 0.52x |
| 11 | SUI/USD | 64.508 | 0.6575 | -0.20% | 0.37x |
| 12 | LINK/USD | 62.125 | 8.8178 | -0.18% | 0.37x |

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

- Persisted scans: 1318; predictions: 10735; observations: 797770.
- Matured sampled outcomes across 1/6/24/48h: 16030; gap abstentions: 22336. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45053456435 · **Generation:** 1318 · **Legacy run:** 45053456435
**Main quote time:** 2026-11-22T18:11:08.924078+00:00 · **Legacy report time:** 2026-11-22T18:11:51.360314+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 62.82 | 83.70 | -0.55% | 2.86x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 3.0077 | 78.87 | -0.15% | 0.68x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 3 | VVV/USD ⭐ | 25.623 | 77.95 | +0.13% | 1.47x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | DRV/USD | 0.36629 | 74.82 | +0.15% | 0.41x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 5 | PUMP/USD | 0.00255 | 74.18 | -0.82% | 0.46x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | ZBCN/USD | 0.001904 | 73.87 | +0.00% | 1.77x | MODERATE 62/100 | VERY_HIGH 72/100 | Watch |
| 7 | ZEC/USD | 792.47 | 72.23 | -0.59% | 1.86x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1711.85 | 64.74 | -0.19% | 0.84x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | STBL/USD | 0.017031 | 63.34 | +0.36% | 0.45x | MODERATE 57/100 | EXTREME 88/100 | Do nothing |
| 10 | AERO/USD | 0.4224 | 59.12 | -0.33% | 0.52x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 11 | SUI/USD | 0.6575 | 57.24 | -0.20% | 0.37x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LINK/USD | 8.8178 | 54.93 | -0.18% | 0.37x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.0288 | 81.82 | +0.87% | 1.67x | 6148 | STRONG 71/100 | VERY_HIGH 77/100 | Watch |
| 2 | VVV/USD ⭐ | 25.623 | 76.63 | +0.13% | 1.47x | 12277 | STRONG 83/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
