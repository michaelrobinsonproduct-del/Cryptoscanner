# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T09:51:44.480465+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45368858510
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6911fa9f05aff0f17c05f5e3b3d5d24a9332ec92 (atomic ledger/results publication)
**Ledger generation:** 1558 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.35 | 84.145 | 80.038 | +3.69% | +1.75% | 0.54x | 1.6 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | MON/USD | 0.01254 | 76.155 | 82.493 | +8.85% | -1.03% | 0.88x | 8.0 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | XMR/USD | 497.07 | 67.620 | 64.773 | +2.27% | -0.33% | 1.45x | 12.3 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.494e-06 | 55.214 | 62.429 | +2.10% | -0.09% | 0.32x | 5.7 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | BABY/USD | 0.0089 | 52.950 | 60.024 | +4.71% | +0.11% | 0.24x | 11.2 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.01629 | 52.612 | 43.955 | +4.09% | +0.18% | 1.77x | 30.8 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | INX/USD | 0.004018 | 35.752 | 40.770 | +3.08% | -1.98% | 1.49x | 25.0 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | BAT/USD | 0.07855 | 32.620 | 41.703 | +1.79% | -0.82% | 0.50x | 6.4 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | ATOM/USD | 1.2904 | 30.049 | 33.456 | +0.64% | -0.35% | 0.84x | 8.5 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | XTZ/USD | 0.21386 | 27.194 | 28.186 | +0.47% | +0.07% | 0.87x | 12.2 | 2026-11-24T09:51:38.971094+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 82.493 | 0.01254 | -1.03% | 0.88x |
| 2 | VVV/USD | 80.038 | 25.35 | +1.75% | 0.54x |
| 3 | XMR/USD | 64.773 | 497.07 | -0.33% | 1.45x |
| 4 | PEPE/USD | 62.429 | 3.494e-06 | -0.09% | 0.32x |
| 5 | BABY/USD | 60.024 | 0.0089 | +0.11% | 0.24x |
| 6 | 2Z/USD | 43.955 | 0.01629 | +0.18% | 1.77x |
| 7 | BAT/USD | 41.703 | 0.07855 | -0.82% | 0.50x |
| 8 | INX/USD | 40.770 | 0.004018 | -1.98% | 1.49x |
| 9 | ATOM/USD | 33.456 | 1.2904 | -0.35% | 0.84x |
| 10 | XTZ/USD | 28.186 | 0.21386 | +0.07% | 0.87x |

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

- Persisted scans: 1558; predictions: 13419; observations: 943920.
- Matured sampled outcomes across 1/6/24/48h: 25590; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45368858510 · **Generation:** 1558 · **Legacy run:** 45368858510
**Main quote time:** 2026-11-24T09:51:44.480465+00:00 · **Legacy report time:** 2026-11-24T09:52:56.044618+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.35 | 84.14 | +1.75% | 0.54x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 2 | MON/USD | 0.01254 | 76.16 | -1.03% | 0.88x | WEAK 43/100 | VERY_HIGH 72/100 | Watch |
| 3 | XMR/USD | 497.07 | 67.62 | -0.33% | 1.45x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 4 | PEPE/USD | 3.494e-06 | 55.21 | -0.09% | 0.32x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | BABY/USD | 0.0089 | 52.95 | +0.11% | 0.24x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 6 | 2Z/USD ⭐ | 0.01629 | 52.61 | +0.18% | 1.77x | MODERATE 61/100 | VERY_HIGH 79/100 | Watch |
| 7 | INX/USD | 0.004018 | 35.75 | -1.98% | 1.49x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | BAT/USD | 0.07855 | 32.62 | -0.82% | 0.50x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | ATOM/USD | 1.2904 | 30.05 | -0.35% | 0.84x | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | XTZ/USD | 0.21386 | 27.19 | +0.07% | 0.87x | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD ⭐ | 0.01629 | 64.11 | +0.18% | 1.77x | 1119 | STRONG 77/100 | HIGH 67/100 | Watch |

**Same-run overlap:** 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
