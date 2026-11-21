# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T22:51:05.756588+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44958719786
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 1cf550f996fab0687cbbb1b52db8618ef2998b32 (atomic ledger/results publication)
**Ledger generation:** 1197 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 489.28 | 92.202 | 96.729 | +7.23% | -0.62% | 0.86x | 6.5 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04481 | 87.064 | 87.388 | +6.13% | -0.31% | 1.12x | 6.7 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | MODERATE 54/100 | HIGH 68/100 | Watch | WATCH |
| 3 | UNI/USD | 4.6993 | 81.189 | 89.388 | +5.20% | -0.07% | 0.22x | 3.6 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.956 | 75.760 | 77.318 | +6.98% | -0.38% | 1.04x | 21.5 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | ETH/USD | 1678.39 | 74.533 | 80.505 | +3.65% | -0.00% | 0.40x | 0.1 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | QNT/USD | 143.17 | 73.234 | 75.500 | +3.18% | +0.30% | 0.62x | 3.5 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | TAO/USD | 185.6834 | 71.311 | 72.401 | +2.87% | +0.30% | 0.74x | 5.3 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 60045 | 66.883 | 69.735 | +2.11% | -0.13% | 0.78x | 0.0 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ZEC/USD | 780.8 | 63.770 | 72.875 | +3.02% | -0.28% | 0.23x | 6.5 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.92607 | 63.703 | 68.211 | +1.91% | -0.02% | 0.56x | 0.3 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0549619 | 62.620 | 63.695 | +1.27% | -0.06% | 0.92x | 0.3 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 12 | SOL/USD | 69.99 | 62.137 | 67.326 | +1.86% | -0.09% | 0.52x | 1.4 | 2026-11-21T22:50:59.714755+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.729 | 489.28 | -0.62% | 0.86x |
| 2 | UNI/USD | 89.388 | 4.6993 | -0.07% | 0.22x |
| 3 | NIGHT/USD | 87.388 | 0.04481 | -0.31% | 1.12x |
| 4 | ETH/USD | 80.505 | 1678.39 | -0.00% | 0.40x |
| 5 | PEARL/USD | 77.318 | 1.956 | -0.38% | 1.04x |
| 6 | QNT/USD | 75.500 | 143.17 | +0.30% | 0.62x |
| 7 | ZEC/USD | 72.875 | 780.8 | -0.28% | 0.23x |
| 8 | TAO/USD | 72.401 | 185.6834 | +0.30% | 0.74x |
| 9 | XBT/USD | 69.735 | 60045 | -0.13% | 0.78x |
| 10 | XRP/USD | 68.211 | 0.92607 | -0.02% | 0.56x |
| 11 | SOL/USD | 67.326 | 69.99 | -0.09% | 0.52x |
| 12 | XDG/USD | 63.695 | 0.0549619 | -0.06% | 0.92x |

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

- Persisted scans: 1197; predictions: 9673; observations: 724135.
- Matured sampled outcomes across 1/6/24/48h: 12964; gap abstentions: 21569. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44958719786 · **Generation:** 1197 · **Legacy run:** 44958719786
**Main quote time:** 2026-11-21T22:51:05.756588+00:00 · **Legacy report time:** 2026-11-21T22:51:50.654134+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 489.28 | 92.20 | -0.62% | 0.86x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 2 | NIGHT/USD | 0.04481 | 87.06 | -0.31% | 1.12x | MODERATE 54/100 | HIGH 68/100 | Watch |
| 3 | UNI/USD | 4.6993 | 81.19 | -0.07% | 0.22x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 4 | PEARL/USD | 1.956 | 75.76 | -0.38% | 1.04x | WEAK 38/100 | VERY_HIGH 80/100 | Watch |
| 5 | ETH/USD | 1678.39 | 74.53 | -0.00% | 0.40x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | QNT/USD | 143.17 | 73.23 | +0.30% | 0.62x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 7 | TAO/USD | 185.6834 | 71.31 | +0.30% | 0.74x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 60045 | 66.88 | -0.13% | 0.78x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | ZEC/USD | 780.8 | 63.77 | -0.28% | 0.23x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.92607 | 63.70 | -0.02% | 0.56x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0549619 | 62.62 | -0.06% | 0.92x | WEAK 36/100 | HIGH 68/100 | Watch |
| 12 | SOL/USD | 69.99 | 62.14 | -0.09% | 0.52x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

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
