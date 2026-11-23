# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T10:41:35.068692+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45158110994
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bc49ad9f3f7a510203a6c9030168d3756620cf46 (atomic ledger/results publication)
**Ledger generation:** 1418 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 152.27 | 84.098 | 86.712 | +6.16% | +1.20% | 0.14x | 6.5 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SOL/USD | 72.21 | 83.432 | 69.966 | +2.24% | +0.00% | 2.35x | 1.4 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 502.89 | 82.181 | 66.425 | +1.86% | +0.15% | 5.20x | 3.2 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03113 | 78.812 | 62.846 | +5.28% | +0.19% | 4.56x | 9.6 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | STRONG 84/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.08126 | 77.276 | 75.897 | +7.73% | +1.01% | 0.63x | 6.2 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | JUP/USD | 0.24146 | 70.403 | 74.412 | +7.52% | -0.29% | 0.75x | 11.6 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | SUI/USD | 0.67 | 68.319 | 69.519 | +2.18% | +0.10% | 0.83x | 1.5 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 8 | KAS/USD | 0.02733 | 67.589 | 66.416 | +5.89% | +0.74% | 0.75x | 18.3 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | PAXG/USD | 3609.73 | 66.351 | 51.084 | +1.05% | +0.05% | 24.13x | 0.7 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 10 | INJ/USD | 6.452 | 63.784 | 65.006 | +3.60% | +0.37% | 0.69x | 3.1 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 63.9 | 63.511 | 63.542 | +1.33% | +0.38% | 0.81x | 1.6 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.93862 | 61.883 | 62.829 | +1.19% | +0.12% | 0.85x | 1.1 | 2026-11-23T10:41:27.463170+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 86.712 | 152.27 | +1.20% | 0.14x |
| 2 | ALGO/USD | 75.897 | 0.08126 | +1.01% | 0.63x |
| 3 | JUP/USD | 74.412 | 0.24146 | -0.29% | 0.75x |
| 4 | SOL/USD | 69.966 | 72.21 | +0.00% | 2.35x |
| 5 | SUI/USD | 69.519 | 0.67 | +0.10% | 0.83x |
| 6 | XMR/USD | 66.425 | 502.89 | +0.15% | 5.20x |
| 7 | KAS/USD | 66.416 | 0.02733 | +0.74% | 0.75x |
| 8 | INJ/USD | 65.006 | 6.452 | +0.37% | 0.69x |
| 9 | HYPE/USD | 63.542 | 63.9 | +0.38% | 0.81x |
| 10 | UAI/USD | 62.846 | 0.03113 | +0.19% | 4.56x |
| 11 | XRP/USD | 62.829 | 0.93862 | +0.12% | 0.85x |
| 12 | PAXG/USD | 51.084 | 3609.73 | +0.05% | 24.13x |

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

- Persisted scans: 1418; predictions: 11783; observations: 858665.
- Matured sampled outcomes across 1/6/24/48h: 19452; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45158110994 · **Generation:** 1418 · **Legacy run:** 45158110994
**Main quote time:** 2026-11-23T10:41:35.068692+00:00 · **Legacy report time:** 2026-11-23T10:42:29.145601+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 152.27 | 84.10 | +1.20% | 0.14x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 2 | SOL/USD | 72.21 | 83.43 | +0.00% | 2.35x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD | 502.89 | 82.18 | +0.15% | 5.20x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03113 | 78.81 | +0.19% | 4.56x | STRONG 94/100 | HIGH 67/100 | Watch |
| 5 | ALGO/USD | 0.08126 | 77.28 | +1.01% | 0.63x | MODERATE 69/100 | VERY_HIGH 75/100 | Watch |
| 6 | JUP/USD | 0.24146 | 70.40 | -0.29% | 0.75x | WEAK 35/100 | EXTREME 87/100 | Do nothing |
| 7 | SUI/USD | 0.67 | 68.32 | +0.10% | 0.83x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 8 | KAS/USD | 0.02733 | 67.59 | +0.74% | 0.75x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 9 | PAXG/USD | 3609.73 | 66.35 | +0.05% | 24.13x | STRONG 78/100 | HIGH 55/100 | Watch |
| 10 | INJ/USD | 6.452 | 63.78 | +0.37% | 0.69x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 63.9 | 63.51 | +0.38% | 0.81x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.93862 | 61.88 | +0.12% | 0.85x | MODERATE 51/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD | 0.07599 | 85.86 | +0.42% | 4.32x | 4034 | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 2 | UAI/USD ⭐ | 0.03113 | 71.91 | +0.19% | 4.56x | 1787 | STRONG 86/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
