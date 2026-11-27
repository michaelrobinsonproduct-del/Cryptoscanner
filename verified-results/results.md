# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T23:32:38.615178+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46082777463
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1d1e2217ab771849cafe53b3c4a5cf1f68cf647d (atomic ledger/results publication)
**Ledger generation:** 2075 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 729.23 | 91.168 | 98.491 | +6.98% | -0.06% | 0.30x | 3.0 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | LTC/USD | 44.65 | 84.117 | 68.443 | +2.08% | +0.13% | 4.73x | 2.2 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 63.26 | 78.306 | 65.119 | +1.67% | -0.36% | 56.89x | 3.2 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0575847 | 75.706 | 70.018 | +2.15% | +0.20% | 1.47x | 0.0 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 71.42 | 74.527 | 59.036 | +0.68% | +0.10% | 4.04x | 1.4 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.05021 | 74.075 | 79.133 | +3.59% | +0.00% | 0.49x | 2.0 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SKY/USD | 0.05173 | 72.827 | 81.135 | +11.46% | -0.29% | 0.31x | 5.8 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | FET/USD | 0.127 | 68.401 | 67.533 | +5.48% | +0.64% | 0.77x | 15.8 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 9 | UNI/USD | 4.8129 | 64.812 | 74.412 | +3.50% | -0.19% | 0.14x | 3.5 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | LINK/USD | 9.34639 | 64.721 | 59.572 | +0.84% | +0.17% | 1.43x | 2.6 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 11 | TAO/USD | 186.1737 | 60.991 | 62.724 | +1.30% | +0.19% | 0.73x | 2.8 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PAXG/USD | 3651.14 | 59.841 | 62.341 | +2.65% | +0.07% | 0.71x | 0.8 | 2026-11-27T23:32:31.825148+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.491 | 729.23 | -0.06% | 0.30x |
| 2 | SKY/USD | 81.135 | 0.05173 | -0.29% | 0.31x |
| 3 | NIGHT/USD | 79.133 | 0.05021 | +0.00% | 0.49x |
| 4 | UNI/USD | 74.412 | 4.8129 | -0.19% | 0.14x |
| 5 | XDG/USD | 70.018 | 0.0575847 | +0.20% | 1.47x |
| 6 | LTC/USD | 68.443 | 44.65 | +0.13% | 4.73x |
| 7 | FET/USD | 67.533 | 0.127 | +0.64% | 0.77x |
| 8 | HYPE/USD | 65.119 | 63.26 | -0.36% | 56.89x |
| 9 | TAO/USD | 62.724 | 186.1737 | +0.19% | 0.73x |
| 10 | PAXG/USD | 62.341 | 3651.14 | +0.07% | 0.71x |
| 11 | LINK/USD | 59.572 | 9.34639 | +0.17% | 1.43x |
| 12 | SOL/USD | 59.036 | 71.42 | +0.10% | 4.04x |

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

- Persisted scans: 2075; predictions: 18602; observations: 1256498.
- Matured sampled outcomes across 1/6/24/48h: 42479; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46082777463 · **Generation:** 2075 · **Legacy run:** 46082777463
**Main quote time:** 2026-11-27T23:32:38.615178+00:00 · **Legacy report time:** 2026-11-27T23:33:29.215546+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 729.23 | 91.17 | -0.06% | 0.30x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | LTC/USD ⭐ | 44.65 | 84.12 | +0.13% | 4.73x | STRONG 97/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 63.26 | 78.31 | -0.36% | 56.89x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0575847 | 75.71 | +0.20% | 1.47x | STRONG 93/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 71.42 | 74.53 | +0.10% | 4.04x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.05021 | 74.08 | +0.00% | 0.49x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | SKY/USD | 0.05173 | 72.83 | -0.29% | 0.31x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 8 | FET/USD | 0.127 | 68.40 | +0.64% | 0.77x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 9 | UNI/USD | 4.8129 | 64.81 | -0.19% | 0.14x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | LINK/USD | 9.34639 | 64.72 | +0.17% | 1.43x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 11 | TAO/USD | 186.1737 | 60.99 | +0.19% | 0.73x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | PAXG/USD | 3651.14 | 59.84 | +0.07% | 0.71x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 44.65 | 80.89 | +0.13% | 4.73x | 15791 | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0575847 | 79.75 | +0.20% | 1.47x | 13333 | STRONG 95/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
