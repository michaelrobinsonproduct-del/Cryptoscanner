# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T14:22:19.432927+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46014899147
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 41e909cc3345dc8e74b7c54d651286cdf29b5837 (atomic ledger/results publication)
**Ledger generation:** 2019 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 604; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.9016 | 95.491 | 81.409 | +5.41% | -0.18% | 3.29x | 4.1 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 752.21 | 91.676 | 98.072 | +10.35% | -0.35% | 0.54x | 3.9 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.95 | 88.868 | 96.206 | +5.99% | -0.15% | 0.34x | 1.5 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0587196 | 88.290 | 75.428 | +4.16% | -0.43% | 3.60x | 1.1 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ENA/USD | 0.1064 | 88.179 | 74.118 | +5.98% | -0.19% | 2.76x | 9.4 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 6 | FET/USD | 0.129 | 75.463 | 72.236 | +7.14% | -1.30% | 1.97x | 15.5 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | XRP/USD | 0.96438 | 70.075 | 71.009 | +2.29% | -0.24% | 1.03x | 0.1 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ETH/USD | 1721.62 | 69.779 | 69.048 | +2.01% | -0.16% | 1.15x | 0.1 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SOL/USD | 73.03 | 66.722 | 74.938 | +2.95% | -0.33% | 0.34x | 1.4 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | INJ/USD | 6.492 | 66.445 | 73.474 | +4.84% | +0.46% | 0.07x | 3.1 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61334.7 | 65.024 | 64.673 | +1.38% | -0.11% | 1.09x | 0.0 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 12 | VVV/USD | 27.201 | 62.548 | 75.390 | +3.89% | -1.04% | 0.23x | 7.0 | 2026-11-27T14:22:12.805761+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 80/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.072 | 752.21 | -0.35% | 0.54x |
| 2 | HYPE/USD | 96.206 | 65.95 | -0.15% | 0.34x |
| 3 | UNI/USD | 81.409 | 4.9016 | -0.18% | 3.29x |
| 4 | XDG/USD | 75.428 | 0.0587196 | -0.43% | 3.60x |
| 5 | VVV/USD | 75.390 | 27.201 | -1.04% | 0.23x |
| 6 | SOL/USD | 74.938 | 73.03 | -0.33% | 0.34x |
| 7 | ENA/USD | 74.118 | 0.1064 | -0.19% | 2.76x |
| 8 | INJ/USD | 73.474 | 6.492 | +0.46% | 0.07x |
| 9 | FET/USD | 72.236 | 0.129 | -1.30% | 1.97x |
| 10 | XRP/USD | 71.009 | 0.96438 | -0.24% | 1.03x |
| 11 | ETH/USD | 69.048 | 1721.62 | -0.16% | 1.15x |
| 12 | XBT/USD | 64.673 | 61334.7 | -0.11% | 1.09x |

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

- Persisted scans: 2019; predictions: 17930; observations: 1222608.
- Matured sampled outcomes across 1/6/24/48h: 40013; gap abstentions: 25894. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46014899147 · **Generation:** 2019 · **Legacy run:** 46014899147
**Main quote time:** 2026-11-27T14:22:19.432927+00:00 · **Legacy report time:** 2026-11-27T14:23:12.663056+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.9016 | 95.49 | -0.18% | 3.29x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 752.21 | 91.68 | -0.35% | 0.54x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD | 65.95 | 88.87 | -0.15% | 0.34x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 4 | XDG/USD | 0.0587196 | 88.29 | -0.43% | 3.60x | STRONG 74/100 | HIGH 61/100 | Watch |
| 5 | ENA/USD | 0.1064 | 88.18 | -0.19% | 2.76x | STRONG 74/100 | HIGH 61/100 | Watch |
| 6 | FET/USD | 0.129 | 75.46 | -1.30% | 1.97x | MODERATE 53/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | XRP/USD | 0.96438 | 70.08 | -0.24% | 1.03x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 8 | ETH/USD | 1721.62 | 69.78 | -0.16% | 1.15x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 9 | SOL/USD | 73.03 | 66.72 | -0.33% | 0.34x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | INJ/USD | 6.492 | 66.45 | +0.46% | 0.07x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61334.7 | 65.02 | -0.11% | 1.09x | WEAK 43/100 | HIGH 68/100 | Watch |
| 12 | VVV/USD | 27.201 | 62.55 | -1.04% | 0.23x | WEAK 36/100 | VERY_HIGH 80/100 | Watch |

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
