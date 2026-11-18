# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:45:12.455789+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44327600628
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** a40e3a8fe533f7524dec768c0a0cbda9d55097bf (atomic ledger/results publication)
**Ledger generation:** 592 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04661 | 75.395 | 67.703 | +3.83% | -0.75% | 2.14x | 15.0 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 2 | CT/USD | 0.1206 | 68.331 | 67.680 | +6.73% | -1.07% | 1.60x | 16.6 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019644 | 62.357 | 65.089 | +5.22% | +0.30% | 0.58x | 5.1 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | STABLE/USD | 0.02311 | 53.997 | 63.012 | +9.79% | -0.30% | 0.25x | 26.0 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | VVV/USD | 21.109 | 51.949 | 41.315 | +0.39% | -0.41% | 2.27x | 19.9 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 6 | CC/USD | 0.08273 | 49.772 | 37.596 | +0.73% | -0.56% | 10.91x | 6.0 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309244 | 35.880 | 43.193 | +0.44% | -0.25% | 0.39x | 1.5 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | W/USD | 0.00897 | 29.699 | 29.269 | +0.45% | -0.55% | 1.32x | 11.2 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5165 | 26.295 | 33.597 | +1.41% | -1.28% | 0.91x | 17.4 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 10 | ME/USD | 0.0392 | 26.216 | 29.575 | +1.55% | -0.51% | 0.92x | 25.5 | 2026-11-18T14:45:06.503679+00:00 | Not calibrated | WEAK 8/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 67.703 | 0.04661 | -0.75% | 2.14x |
| 2 | CT/USD | 67.680 | 0.1206 | -1.07% | 1.60x |
| 3 | SENT/USD | 65.089 | 0.019644 | +0.30% | 0.58x |
| 4 | STABLE/USD | 63.012 | 0.02311 | -0.30% | 0.25x |
| 5 | TRX/USD | 43.193 | 0.309244 | -0.25% | 0.39x |
| 6 | VVV/USD | 41.315 | 21.109 | -0.41% | 2.27x |
| 7 | CC/USD | 37.596 | 0.08273 | -0.56% | 10.91x |
| 8 | AKT/USD | 33.597 | 0.5165 | -1.28% | 0.91x |
| 9 | ME/USD | 29.575 | 0.0392 | -0.51% | 0.92x |
| 10 | W/USD | 29.269 | 0.00897 | -0.55% | 1.32x |

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

- Persisted scans: 592; predictions: 5046; observations: 357535.
- Matured sampled outcomes across 1/6/24/48h: 4268; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44327600628 · **Generation:** 592 · **Legacy run:** 44327600628
**Main quote time:** 2026-11-18T14:45:12.455789+00:00 · **Legacy report time:** 2026-11-18T14:45:38.795285+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04661 | 75.39 | -0.75% | 2.14x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 2 | CT/USD | 0.1206 | 68.33 | -1.07% | 1.60x | MODERATE 49/100 | VERY_HIGH 83/100 | Watch |
| 3 | SENT/USD | 0.019644 | 62.36 | +0.30% | 0.58x | MODERATE 61/100 | VERY_HIGH 82/100 | Watch |
| 4 | STABLE/USD | 0.02311 | 54.00 | -0.30% | 0.25x | WEAK 22/100 | EXTREME 100/100 | Do nothing |
| 5 | VVV/USD | 21.109 | 51.95 | -0.41% | 2.27x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 6 | CC/USD | 0.08273 | 49.77 | -0.56% | 10.91x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 7 | TRX/USD | 0.309244 | 35.88 | -0.25% | 0.39x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | W/USD | 0.00897 | 29.70 | -0.55% | 1.32x | WEAK 30/100 | VERY_HIGH 72/100 | Do nothing |
| 9 | AKT/USD | 0.5165 | 26.30 | -1.28% | 0.91x | WEAK 13/100 | VERY_HIGH 83/100 | Do nothing |
| 10 | ME/USD | 0.0392 | 26.22 | -0.51% | 0.92x | WEAK 8/100 | EXTREME 92/100 | Do nothing |

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
