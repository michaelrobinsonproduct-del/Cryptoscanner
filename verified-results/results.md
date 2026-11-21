# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T18:20:53.247149+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44934894939
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** f4aa0baab75f83fe0068853fe91bca0a0c2e1f25 (atomic ledger/results publication)
**Ledger generation:** 1169 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04575 | 98.440 | 87.200 | +8.36% | -0.09% | 2.17x | 10.9 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7155 | 86.311 | 92.316 | +5.56% | +0.01% | 0.40x | 3.2 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XMR/USD | 479.19 | 81.942 | 87.312 | +5.02% | -0.19% | 0.56x | 5.6 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | QNT/USD | 143.7 | 81.522 | 76.789 | +3.56% | +0.00% | 1.47x | 6.3 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1678.57 | 80.719 | 80.583 | +3.66% | -0.10% | 1.06x | 0.1 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ZEC/USD | 785.44 | 74.269 | 78.452 | +3.63% | -0.05% | 0.61x | 3.9 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XBT/USD | 60014.8 | 71.425 | 69.376 | +2.05% | +0.04% | 1.19x | 0.0 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 8 | TAO/USD | 186.0359 | 68.836 | 70.809 | +3.06% | +0.13% | 0.74x | 11.3 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 70.47 | 65.924 | 72.221 | +2.56% | -0.18% | 0.46x | 1.4 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.08207 | 65.780 | 75.008 | +10.16% | -0.17% | 0.16x | 18.4 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | BNB/USD | 547.47 | 62.533 | 58.195 | +1.45% | +0.04% | 1.41x | 0.2 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92948 | 62.481 | 70.462 | +2.29% | -0.27% | 0.33x | 1.1 | 2026-11-21T18:20:44.782974+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 92.316 | 4.7155 | +0.01% | 0.40x |
| 2 | XMR/USD | 87.312 | 479.19 | -0.19% | 0.56x |
| 3 | NIGHT/USD | 87.200 | 0.04575 | -0.09% | 2.17x |
| 4 | ETH/USD | 80.583 | 1678.57 | -0.10% | 1.06x |
| 5 | ZEC/USD | 78.452 | 785.44 | -0.05% | 0.61x |
| 6 | QNT/USD | 76.789 | 143.7 | +0.00% | 1.47x |
| 7 | USELESS/USD | 75.008 | 0.08207 | -0.17% | 0.16x |
| 8 | SOL/USD | 72.221 | 70.47 | -0.18% | 0.46x |
| 9 | TAO/USD | 70.809 | 186.0359 | +0.13% | 0.74x |
| 10 | XRP/USD | 70.462 | 0.92948 | -0.27% | 0.33x |
| 11 | XBT/USD | 69.376 | 60014.8 | +0.04% | 1.19x |
| 12 | BNB/USD | 58.195 | 547.47 | +0.04% | 1.41x |

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

- Persisted scans: 1169; predictions: 9337; observations: 707111.
- Matured sampled outcomes across 1/6/24/48h: 12324; gap abstentions: 21068. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44934894939 · **Generation:** 1169 · **Legacy run:** 44934894939
**Main quote time:** 2026-11-21T18:20:53.247149+00:00 · **Legacy report time:** 2026-11-21T18:21:36.086420+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04575 | 98.44 | -0.09% | 2.17x | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | UNI/USD | 4.7155 | 86.31 | +0.01% | 0.40x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 3 | XMR/USD | 479.19 | 81.94 | -0.19% | 0.56x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 4 | QNT/USD | 143.7 | 81.52 | +0.00% | 1.47x | STRONG 76/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1678.57 | 80.72 | -0.10% | 1.06x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 6 | ZEC/USD | 785.44 | 74.27 | -0.05% | 0.61x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 7 | XBT/USD | 60014.8 | 71.43 | +0.04% | 1.19x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 8 | TAO/USD | 186.0359 | 68.84 | +0.13% | 0.74x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 70.47 | 65.92 | -0.18% | 0.46x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | USELESS/USD | 0.08207 | 65.78 | -0.17% | 0.16x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | BNB/USD | 547.47 | 62.53 | +0.04% | 1.41x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 12 | XRP/USD | 0.92948 | 62.48 | -0.27% | 0.33x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

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
