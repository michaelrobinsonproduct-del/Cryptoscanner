# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T21:57:12.767753+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45274388567
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 86fad6bae068a76333e93e4ad5e6afdf306803e3 (atomic ledger/results publication)
**Ledger generation:** 1486 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 157.14 | 91.597 | 95.227 | +9.55% | -0.16% | 0.72x | 9.5 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08143 | 83.085 | 91.883 | +7.95% | +0.01% | 0.11x | 6.1 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ATOM/USD | 1.2628 | 76.738 | 72.904 | +7.75% | +0.12% | 1.32x | 10.3 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 68/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6727 | 76.500 | 71.662 | +2.59% | -0.30% | 1.63x | 3.0 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XLM/USD | 0.130978 | 76.040 | 72.982 | +2.71% | +0.18% | 1.21x | 1.9 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | INJ/USD | 6.417 | 75.768 | 71.052 | +3.03% | -0.40% | 1.67x | 6.2 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LTC/USD | 41.24 | 72.689 | 72.613 | +2.69% | -0.05% | 1.03x | 2.4 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | CAP/USD | 0.103829 | 71.125 | 76.122 | +10.96% | +0.47% | 0.26x | 6.1 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | UAI/USD | 0.03209 | 65.641 | 72.886 | +8.52% | -0.22% | 0.38x | 6.3 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | WEAK 38/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | SOL/USD | 72.17 | 65.592 | 69.570 | +2.18% | -0.12% | 0.66x | 1.4 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | TRX/USD | 0.309178 | 65.007 | 50.271 | +1.31% | -0.05% | 3.58x | 1.1 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0564503 | 62.840 | 69.691 | +2.11% | -0.04% | 0.34x | 0.2 | 2026-11-23T21:57:03.924096+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 95.227 | 157.14 | -0.16% | 0.72x |
| 2 | ALGO/USD | 91.883 | 0.08143 | +0.01% | 0.11x |
| 3 | CAP/USD | 76.122 | 0.103829 | +0.47% | 0.26x |
| 4 | XLM/USD | 72.982 | 0.130978 | +0.18% | 1.21x |
| 5 | ATOM/USD | 72.904 | 1.2628 | +0.12% | 1.32x |
| 6 | UAI/USD | 72.886 | 0.03209 | -0.22% | 0.38x |
| 7 | LTC/USD | 72.613 | 41.24 | -0.05% | 1.03x |
| 8 | SUI/USD | 71.662 | 0.6727 | -0.30% | 1.63x |
| 9 | INJ/USD | 71.052 | 6.417 | -0.40% | 1.67x |
| 10 | XDG/USD | 69.691 | 0.0564503 | -0.04% | 0.34x |
| 11 | SOL/USD | 69.570 | 72.17 | -0.12% | 0.66x |
| 12 | TRX/USD | 50.271 | 0.309178 | -0.05% | 3.58x |

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

- Persisted scans: 1486; predictions: 12599; observations: 900076.
- Matured sampled outcomes across 1/6/24/48h: 22708; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45274388567 · **Generation:** 1486 · **Legacy run:** 45274388567
**Main quote time:** 2026-11-23T21:57:12.767753+00:00 · **Legacy report time:** 2026-11-23T21:58:03.757049+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 157.14 | 91.60 | -0.16% | 0.72x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | ALGO/USD | 0.08143 | 83.09 | +0.01% | 0.11x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 3 | ATOM/USD ⭐ | 1.2628 | 76.74 | +0.12% | 1.32x | STRONG 78/100 | HIGH 66/100 | Watch |
| 4 | SUI/USD | 0.6727 | 76.50 | -0.30% | 1.63x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 5 | XLM/USD ⭐ | 0.130978 | 76.04 | +0.18% | 1.21x | STRONG 73/100 | HIGH 62/100 | Watch |
| 6 | INJ/USD | 6.417 | 75.77 | -0.40% | 1.67x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | LTC/USD | 41.24 | 72.69 | -0.05% | 1.03x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | CAP/USD | 0.103829 | 71.13 | +0.47% | 0.26x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 9 | UAI/USD | 0.03209 | 65.64 | -0.22% | 0.38x | WEAK 38/100 | EXTREME 88/100 | Do nothing |
| 10 | SOL/USD | 72.17 | 65.59 | -0.12% | 0.66x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 11 | TRX/USD | 0.309178 | 65.01 | -0.05% | 3.58x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 12 | XDG/USD | 0.0564503 | 62.84 | -0.04% | 0.34x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.131074 | 74.41 | +0.18% | 1.21x | 18397 | STRONG 72/100 | HIGH 62/100 | Watch |
| 2 | ATOM/USD ⭐ | 1.2628 | 73.49 | +0.12% | 1.32x | 3680 | STRONG 82/100 | HIGH 60/100 | Watch |

**Same-run overlap:** ATOM/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
