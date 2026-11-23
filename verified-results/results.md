# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T16:42:22.024546+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45218988425
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c1b904373fc24212d2152e968b95f2f0355ff2ff (atomic ledger/results publication)
**Ledger generation:** 1455 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.9943 | 101.035 | 90.605 | +6.69% | -0.91% | 3.90x | 9.2 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SOL/USD | 74.16 | 90.802 | 88.636 | +5.00% | -1.18% | 1.81x | 2.7 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | MODERATE 65/100 | HIGH 65/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6997 | 88.585 | 98.571 | +6.71% | -1.75% | 0.88x | 2.9 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 4 | LTC/USD | 42.56 | 87.490 | 94.480 | +5.98% | -0.35% | 0.48x | 4.7 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | DOT/USD | 0.6996 | 86.100 | 76.177 | +5.87% | -0.44% | 2.21x | 1.4 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97168 | 84.925 | 88.209 | +4.76% | -1.09% | 1.22x | 0.2 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0577754 | 81.283 | 84.688 | +4.51% | -1.06% | 1.19x | 3.7 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | INJ/USD | 6.762 | 80.957 | 92.289 | +8.57% | -0.65% | 0.19x | 10.4 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | PAXG/USD | 3652.75 | 80.927 | 66.590 | +2.25% | -0.13% | 3.09x | 1.4 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ADA/USD | 0.152441 | 77.242 | 89.727 | +5.42% | -0.92% | 0.21x | 6.4 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XLM/USD | 0.13296 | 76.373 | 83.462 | +4.26% | -1.03% | 0.81x | 2.7 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.574e-06 | 71.686 | 80.269 | +5.46% | -1.86% | 1.07x | 5.6 | 2026-11-23T16:42:13.898259+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SUI/USD | 98.571 | 0.6997 | -1.75% | 0.88x |
| 2 | LTC/USD | 94.480 | 42.56 | -0.35% | 0.48x |
| 3 | INJ/USD | 92.289 | 6.762 | -0.65% | 0.19x |
| 4 | UNI/USD | 90.605 | 4.9943 | -0.91% | 3.90x |
| 5 | ADA/USD | 89.727 | 0.152441 | -0.92% | 0.21x |
| 6 | SOL/USD | 88.636 | 74.16 | -1.18% | 1.81x |
| 7 | XRP/USD | 88.209 | 0.97168 | -1.09% | 1.22x |
| 8 | XDG/USD | 84.688 | 0.0577754 | -1.06% | 1.19x |
| 9 | XLM/USD | 83.462 | 0.13296 | -1.03% | 0.81x |
| 10 | PEPE/USD | 80.269 | 3.574e-06 | -1.86% | 1.07x |
| 11 | DOT/USD | 76.177 | 0.6996 | -0.44% | 2.21x |
| 12 | PAXG/USD | 66.590 | 3652.75 | -0.13% | 3.09x |

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

- Persisted scans: 1455; predictions: 12227; observations: 881197.
- Matured sampled outcomes across 1/6/24/48h: 21148; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45218988425 · **Generation:** 1455 · **Legacy run:** 45218988425
**Main quote time:** 2026-11-23T16:42:22.024546+00:00 · **Legacy report time:** 2026-11-23T16:43:32.509966+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.9943 | 101.03 | -0.91% | 3.90x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD | 74.16 | 90.80 | -1.18% | 1.81x | MODERATE 65/100 | HIGH 65/100 | Watch |
| 3 | SUI/USD | 0.6997 | 88.58 | -1.75% | 0.88x | MODERATE 49/100 | VERY_HIGH 72/100 | Do nothing |
| 4 | LTC/USD | 42.56 | 87.49 | -0.35% | 0.48x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 5 | DOT/USD | 0.6996 | 86.10 | -0.44% | 2.21x | STRONG 73/100 | HIGH 66/100 | Watch |
| 6 | XRP/USD | 0.97168 | 84.92 | -1.09% | 1.22x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 7 | XDG/USD | 0.0577754 | 81.28 | -1.06% | 1.19x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 8 | INJ/USD | 6.762 | 80.96 | -0.65% | 0.19x | WEAK 40/100 | VERY_HIGH 82/100 | Watch |
| 9 | PAXG/USD | 3652.75 | 80.93 | -0.13% | 3.09x | STRONG 70/100 | HIGH 61/100 | Watch |
| 10 | ADA/USD | 0.152441 | 77.24 | -0.92% | 0.21x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 11 | XLM/USD | 0.13296 | 76.37 | -1.03% | 0.81x | WEAK 43/100 | VERY_HIGH 72/100 | Watch |
| 12 | PEPE/USD | 3.574e-06 | 71.69 | -1.86% | 1.07x | MODERATE 46/100 | VERY_HIGH 72/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.351 | 98.63 | +0.24% | 1.99x | 11691 | STRONG 94/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
