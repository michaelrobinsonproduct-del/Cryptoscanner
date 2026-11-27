# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T09:52:03.383353+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45976924214
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 23448566f9a90781b4e362d4bc3d55d6f61f1679 (atomic ledger/results publication)
**Ledger generation:** 1991 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.09 | 110.364 | 97.025 | +6.22% | -0.33% | 31.84x | 3.0 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LINK/USD | 9.58501 | 90.766 | 76.849 | +3.42% | -0.22% | 3.76x | 4.1 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 27.157 | 86.741 | 75.191 | +3.72% | +0.16% | 2.08x | 7.0 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1729.96 | 86.175 | 72.508 | +2.51% | -0.27% | 3.28x | 0.1 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZEC/USD | 756.89 | 85.825 | 97.484 | +11.04% | -0.61% | 0.14x | 5.0 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 73.48 | 83.910 | 79.383 | +3.58% | -0.30% | 1.60x | 1.4 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 7 | INJ/USD | 6.514 | 76.413 | 69.939 | +5.20% | -0.29% | 1.79x | 7.7 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97915 | 74.050 | 81.210 | +3.86% | +0.18% | 0.20x | 1.6 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ENA/USD | 0.1068 | 73.307 | 76.721 | +6.37% | -0.47% | 0.89x | 9.4 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 10 | UNI/USD | 4.903 | 70.366 | 80.445 | +5.44% | -0.43% | 0.21x | 4.5 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0583643 | 68.806 | 71.690 | +3.53% | -0.13% | 0.78x | 0.7 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XBT/USD | 61649.8 | 66.858 | 68.319 | +1.90% | -0.28% | 0.99x | 0.0 | 2026-11-27T09:51:54.471442+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.484 | 756.89 | -0.61% | 0.14x |
| 2 | HYPE/USD | 97.025 | 66.09 | -0.33% | 31.84x |
| 3 | XRP/USD | 81.210 | 0.97915 | +0.18% | 0.20x |
| 4 | UNI/USD | 80.445 | 4.903 | -0.43% | 0.21x |
| 5 | SOL/USD | 79.383 | 73.48 | -0.30% | 1.60x |
| 6 | LINK/USD | 76.849 | 9.58501 | -0.22% | 3.76x |
| 7 | ENA/USD | 76.721 | 0.1068 | -0.47% | 0.89x |
| 8 | VVV/USD | 75.191 | 27.157 | +0.16% | 2.08x |
| 9 | ETH/USD | 72.508 | 1729.96 | -0.27% | 3.28x |
| 10 | XDG/USD | 71.690 | 0.0583643 | -0.13% | 0.78x |
| 11 | INJ/USD | 69.939 | 6.514 | -0.29% | 1.79x |
| 12 | XBT/USD | 68.319 | 61649.8 | -0.28% | 0.99x |

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

- Persisted scans: 1991; predictions: 17594; observations: 1205726.
- Matured sampled outcomes across 1/6/24/48h: 39029; gap abstentions: 25751. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45976924214 · **Generation:** 1991 · **Legacy run:** 45976924214
**Main quote time:** 2026-11-27T09:52:03.383353+00:00 · **Legacy report time:** 2026-11-27T09:52:46.193387+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 66.09 | 110.36 | -0.33% | 31.84x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | LINK/USD | 9.58501 | 90.77 | -0.22% | 3.76x | STRONG 75/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD ⭐ | 27.157 | 86.74 | +0.16% | 2.08x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1729.96 | 86.18 | -0.27% | 3.28x | STRONG 73/100 | HIGH 61/100 | Watch |
| 5 | ZEC/USD | 756.89 | 85.83 | -0.61% | 0.14x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 73.48 | 83.91 | -0.30% | 1.60x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 7 | INJ/USD | 6.514 | 76.41 | -0.29% | 1.79x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.97915 | 74.05 | +0.18% | 0.20x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | ENA/USD | 0.1068 | 73.31 | -0.47% | 0.89x | WEAK 42/100 | HIGH 68/100 | Watch |
| 10 | UNI/USD | 4.903 | 70.37 | -0.43% | 0.21x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0583643 | 68.81 | -0.13% | 0.78x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | XBT/USD | 61649.8 | 66.86 | -0.28% | 0.99x | WEAK 38/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.614e-06 | 89.36 | +0.08% | 8.90x | 5543 | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD ⭐ | 27.157 | 85.00 | +0.16% | 2.08x | 9705 | STRONG 98/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
