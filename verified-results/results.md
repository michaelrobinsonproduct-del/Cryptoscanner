# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T10:31:10.843518+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45012686138
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 4f401255da7b9f3373586b44f7739982eb03a8cd (atomic ledger/results publication)
**Ledger generation:** 1270 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.971 | 89.575 | 73.690 | +2.93% | +0.95% | 2.11x | 3.7 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 62.36 | 81.840 | 66.198 | +1.83% | +0.13% | 4.41x | 3.2 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PEARL/USD | 2.046 | 81.306 | 73.369 | +5.01% | +0.74% | 1.42x | 9.3 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | TIA/USD | 0.3395 | 78.790 | 62.190 | +4.62% | +1.04% | 2.14x | 2.9 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | STRONG 94/100 | HIGH 67/100 | Consider small entry | WATCH |
| 5 | SUI/USD | 0.6601 | 68.599 | 67.325 | +1.98% | +0.12% | 1.07x | 3.0 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002458 | 64.150 | 69.665 | +4.86% | +0.49% | 0.20x | 12.2 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ZEC/USD | 797.39 | 63.971 | 69.091 | +2.47% | -0.32% | 0.65x | 6.4 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | TAO/USD | 190.6639 | 63.379 | 70.753 | +2.66% | -0.66% | 0.59x | 5.7 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | VVV/USD | 25.511 | 61.183 | 67.668 | +2.45% | +0.15% | 0.28x | 9.0 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ONDO/USD | 0.28442 | 60.860 | 44.979 | +1.00% | +0.18% | 4.15x | 0.7 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 11 | LINK/USD | 8.78291 | 59.863 | 66.426 | +2.19% | +0.20% | 0.24x | 3.5 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1706.99 | 58.924 | 65.253 | +1.47% | -0.19% | 0.46x | 0.1 | 2026-11-22T10:31:02.429230+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 73.690 | 2.971 | +0.95% | 2.11x |
| 2 | PEARL/USD | 73.369 | 2.046 | +0.74% | 1.42x |
| 3 | TAO/USD | 70.753 | 190.6639 | -0.66% | 0.59x |
| 4 | PUMP/USD | 69.665 | 0.002458 | +0.49% | 0.20x |
| 5 | ZEC/USD | 69.091 | 797.39 | -0.32% | 0.65x |
| 6 | VVV/USD | 67.668 | 25.511 | +0.15% | 0.28x |
| 7 | SUI/USD | 67.325 | 0.6601 | +0.12% | 1.07x |
| 8 | LINK/USD | 66.426 | 8.78291 | +0.20% | 0.24x |
| 9 | HYPE/USD | 66.198 | 62.36 | +0.13% | 4.41x |
| 10 | ETH/USD | 65.253 | 1706.99 | -0.19% | 0.46x |
| 11 | TIA/USD | 62.190 | 0.3395 | +1.04% | 2.14x |
| 12 | ONDO/USD | 44.979 | 0.28442 | +0.18% | 4.15x |

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

- Persisted scans: 1270; predictions: 10160; observations: 768539.
- Matured sampled outcomes across 1/6/24/48h: 14629; gap abstentions: 22190. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45012686138 · **Generation:** 1270 · **Legacy run:** 45012686138
**Main quote time:** 2026-11-22T10:31:10.843518+00:00 · **Legacy report time:** 2026-11-22T10:32:03.933989+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.971 | 89.57 | +0.95% | 2.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD | 62.36 | 81.84 | +0.13% | 4.41x | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | PEARL/USD ⭐ | 2.046 | 81.31 | +0.74% | 1.42x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | TIA/USD | 0.3395 | 78.79 | +1.04% | 2.14x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 5 | SUI/USD ⭐ | 0.6601 | 68.60 | +0.12% | 1.07x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 6 | PUMP/USD | 0.002458 | 64.15 | +0.49% | 0.20x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 7 | ZEC/USD | 797.39 | 63.97 | -0.32% | 0.65x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 8 | TAO/USD | 190.6639 | 63.38 | -0.66% | 0.59x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | VVV/USD | 25.511 | 61.18 | +0.15% | 0.28x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | ONDO/USD | 0.28442 | 60.86 | +0.18% | 4.15x | STRONG 75/100 | HIGH 55/100 | Watch |
| 11 | LINK/USD | 8.78291 | 59.86 | +0.20% | 0.24x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1706.99 | 58.92 | -0.19% | 0.46x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.046 | 95.69 | +0.74% | 1.42x | 8263 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.9774 | 87.11 | +0.95% | 2.11x | 12738 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6598 | 72.77 | +0.12% | 1.07x | 7723 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NEAR/USD, PEARL/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
