# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T23:22:22.317897+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46081848016
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2cfbc56239b99d3adba50e1d47a1913b5836e6ab (atomic ledger/results publication)
**Ledger generation:** 2074 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 724.96 | 86.677 | 97.536 | +6.35% | -0.56% | 0.20x | 3.9 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XDG/USD | 0.0574475 | 82.003 | 67.497 | +1.90% | -0.10% | 6.69x | 1.7 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 44.55 | 81.616 | 66.840 | +1.85% | -0.04% | 7.37x | 2.2 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.97 | 71.217 | 62.644 | +1.21% | -1.29% | 24.09x | 1.6 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | MODERATE 66/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | XAUT/USD | 3652 | 70.527 | 55.801 | +2.59% | -0.05% | 20.24x | 0.5 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.05007 | 69.481 | 77.109 | +3.30% | -0.30% | 0.39x | 2.0 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SKY/USD | 0.05119 | 67.730 | 76.086 | +10.30% | -0.64% | 0.48x | 15.6 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 8 | SOL/USD | 71.36 | 67.590 | 58.444 | +0.59% | -0.32% | 2.08x | 1.4 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PAXG/USD | 3647.78 | 62.970 | 62.099 | +2.56% | -0.04% | 1.11x | 0.9 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | LINK/USD | 9.32308 | 62.504 | 57.932 | +0.59% | -0.21% | 1.56x | 2.4 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 11 | UNI/USD | 4.8031 | 62.445 | 72.260 | +3.29% | -0.35% | 0.19x | 4.8 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | TAO/USD | 185.4293 | 55.969 | 58.980 | +0.90% | -0.38% | 0.89x | 4.6 | 2026-11-27T23:22:13.687997+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.536 | 724.96 | -0.56% | 0.20x |
| 2 | NIGHT/USD | 77.109 | 0.05007 | -0.30% | 0.39x |
| 3 | SKY/USD | 76.086 | 0.05119 | -0.64% | 0.48x |
| 4 | UNI/USD | 72.260 | 4.8031 | -0.35% | 0.19x |
| 5 | XDG/USD | 67.497 | 0.0574475 | -0.10% | 6.69x |
| 6 | LTC/USD | 66.840 | 44.55 | -0.04% | 7.37x |
| 7 | HYPE/USD | 62.644 | 62.97 | -1.29% | 24.09x |
| 8 | PAXG/USD | 62.099 | 3647.78 | -0.04% | 1.11x |
| 9 | TAO/USD | 58.980 | 185.4293 | -0.38% | 0.89x |
| 10 | SOL/USD | 58.444 | 71.36 | -0.32% | 2.08x |
| 11 | LINK/USD | 57.932 | 9.32308 | -0.21% | 1.56x |
| 12 | XAUT/USD | 55.801 | 3652 | -0.05% | 20.24x |

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

- Persisted scans: 2074; predictions: 18590; observations: 1255892.
- Matured sampled outcomes across 1/6/24/48h: 42431; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46081848016 · **Generation:** 2074 · **Legacy run:** 46081848016
**Main quote time:** 2026-11-27T23:22:22.317897+00:00 · **Legacy report time:** 2026-11-27T23:23:08.341669+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 724.96 | 86.68 | -0.56% | 0.20x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 2 | XDG/USD | 0.0574475 | 82.00 | -0.10% | 6.69x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 44.55 | 81.62 | -0.04% | 7.37x | STRONG 71/100 | HIGH 61/100 | Watch |
| 4 | HYPE/USD | 62.97 | 71.22 | -1.29% | 24.09x | MODERATE 66/100 | HIGH 65/100 | Do nothing |
| 5 | XAUT/USD | 3652 | 70.53 | -0.05% | 20.24x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | NIGHT/USD | 0.05007 | 69.48 | -0.30% | 0.39x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | SKY/USD | 0.05119 | 67.73 | -0.64% | 0.48x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 8 | SOL/USD | 71.36 | 67.59 | -0.32% | 2.08x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 9 | PAXG/USD | 3647.78 | 62.97 | -0.04% | 1.11x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | LINK/USD | 9.32308 | 62.50 | -0.21% | 1.56x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 11 | UNI/USD | 4.8031 | 62.45 | -0.35% | 0.19x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | TAO/USD | 185.4293 | 55.97 | -0.38% | 0.89x | WEAK 33/100 | HIGH 68/100 | Do nothing |

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
