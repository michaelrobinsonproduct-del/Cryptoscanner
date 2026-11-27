# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T07:41:35.769982+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45959978611
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** db84ab783c85d9b4ff6d7e6623328709bfb094b4 (atomic ledger/results publication)
**Ledger generation:** 1978 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.48 | 99.263 | 90.146 | +5.24% | -1.18% | 3.65x | 3.1 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Watch | WATCH |
| 2 | ZEC/USD | 739.63 | 96.417 | 96.685 | +8.50% | -1.25% | 1.60x | 6.6 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | LINK/USD | 9.55887 | 87.986 | 74.361 | +3.13% | -0.27% | 2.78x | 5.1 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97553 | 86.058 | 78.981 | +3.48% | -0.16% | 1.79x | 0.7 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0580376 | 79.590 | 65.832 | +2.95% | -0.25% | 5.38x | 2.4 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 72.98 | 77.607 | 74.445 | +2.88% | -0.12% | 1.38x | 1.4 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ETH/USD | 1727.08 | 76.365 | 70.850 | +2.33% | -0.51% | 1.80x | 1.0 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | UNI/USD | 4.8841 | 76.120 | 75.281 | +5.03% | -0.28% | 1.22x | 5.9 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 9 | VVV/USD | 27.106 | 69.456 | 75.796 | +3.53% | -0.32% | 0.53x | 7.8 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XBT/USD | 61518.9 | 68.108 | 66.804 | +1.69% | -0.50% | 1.38x | 0.0 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SUI/USD | 0.683 | 67.370 | 70.307 | +2.29% | -0.22% | 0.82x | 1.5 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | W/USD | 0.00954 | 65.846 | 73.259 | +8.29% | -1.03% | 0.78x | 10.5 | 2026-11-27T07:41:28.170148+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 83/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.685 | 739.63 | -1.25% | 1.60x |
| 2 | HYPE/USD | 90.146 | 65.48 | -1.18% | 3.65x |
| 3 | XRP/USD | 78.981 | 0.97553 | -0.16% | 1.79x |
| 4 | VVV/USD | 75.796 | 27.106 | -0.32% | 0.53x |
| 5 | UNI/USD | 75.281 | 4.8841 | -0.28% | 1.22x |
| 6 | SOL/USD | 74.445 | 72.98 | -0.12% | 1.38x |
| 7 | LINK/USD | 74.361 | 9.55887 | -0.27% | 2.78x |
| 8 | W/USD | 73.259 | 0.00954 | -1.03% | 0.78x |
| 9 | ETH/USD | 70.850 | 1727.08 | -0.51% | 1.80x |
| 10 | SUI/USD | 70.307 | 0.683 | -0.22% | 0.82x |
| 11 | XBT/USD | 66.804 | 61518.9 | -0.50% | 1.38x |
| 12 | XDG/USD | 65.832 | 0.0580376 | -0.25% | 5.38x |

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

- Persisted scans: 1978; predictions: 17438; observations: 1197887.
- Matured sampled outcomes across 1/6/24/48h: 38537; gap abstentions: 25643. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45959978611 · **Generation:** 1978 · **Legacy run:** 45959978611
**Main quote time:** 2026-11-27T07:41:35.769982+00:00 · **Legacy report time:** 2026-11-27T07:42:09.467841+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.48 | 99.26 | -1.18% | 3.65x | STRONG 80/100 | HIGH 65/100 | Watch |
| 2 | ZEC/USD | 739.63 | 96.42 | -1.25% | 1.60x | MODERATE 68/100 | HIGH 65/100 | Do nothing |
| 3 | LINK/USD | 9.55887 | 87.99 | -0.27% | 2.78x | STRONG 74/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.97553 | 86.06 | -0.16% | 1.79x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | XDG/USD | 0.0580376 | 79.59 | -0.25% | 5.38x | STRONG 70/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 72.98 | 77.61 | -0.12% | 1.38x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 7 | ETH/USD | 1727.08 | 76.36 | -0.51% | 1.80x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | UNI/USD | 4.8841 | 76.12 | -0.28% | 1.22x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 9 | VVV/USD | 27.106 | 69.46 | -0.32% | 0.53x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 10 | XBT/USD | 61518.9 | 68.11 | -0.50% | 1.38x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 11 | SUI/USD | 0.683 | 67.37 | -0.22% | 0.82x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | W/USD | 0.00954 | 65.85 | -1.03% | 0.78x | WEAK 33/100 | VERY_HIGH 83/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 4.0395 | 75.18 | +0.14% | 1.17x | 2636 | MODERATE 53/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
