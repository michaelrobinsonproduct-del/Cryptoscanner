# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T09:51:38.431808+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45150499422
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 033ca1564109c816fbb563f8336b9a77e524815a (atomic ledger/results publication)
**Ledger generation:** 1413 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 151.65 | 83.367 | 81.418 | +5.72% | -0.36% | 1.38x | 7.3 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.61 | 71.409 | 59.532 | +0.87% | -0.62% | 3.84x | 3.1 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | JUP/USD | 0.24317 | 69.737 | 75.049 | +8.28% | -0.18% | 0.56x | 10.3 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | XMR/USD | 504.65 | 69.567 | 67.238 | +2.22% | -0.17% | 1.32x | 6.5 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.07967 | 69.422 | 69.167 | +5.62% | -0.75% | 1.40x | 8.8 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 6 | XLM/USD | 0.128142 | 67.516 | 57.877 | +0.48% | -0.19% | 2.06x | 0.1 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 72.19 | 64.672 | 69.768 | +2.21% | -0.50% | 0.74x | 1.4 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | Q/USD | 0.027789 | 60.315 | 62.517 | +10.13% | -1.88% | 1.72x | 27.6 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | WEAK 40/100 | EXTREME 89/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6675 | 59.502 | 66.848 | +1.80% | -0.36% | 0.44x | 1.5 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93574 | 59.348 | 61.135 | +0.88% | -0.32% | 0.98x | 0.1 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | UAI/USD | 0.03107 | 58.114 | 61.373 | +5.07% | -0.39% | 0.87x | 9.6 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 12 | AUD/USD | 0.66472 | 57.828 | 43.084 | +0.48% | -0.05% | 3.52x | 0.8 | 2026-11-23T09:51:31.704525+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 81.418 | 151.65 | -0.36% | 1.38x |
| 2 | JUP/USD | 75.049 | 0.24317 | -0.18% | 0.56x |
| 3 | SOL/USD | 69.768 | 72.19 | -0.50% | 0.74x |
| 4 | ALGO/USD | 69.167 | 0.07967 | -0.75% | 1.40x |
| 5 | XMR/USD | 67.238 | 504.65 | -0.17% | 1.32x |
| 6 | SUI/USD | 66.848 | 0.6675 | -0.36% | 0.44x |
| 7 | Q/USD | 62.517 | 0.027789 | -1.88% | 1.72x |
| 8 | UAI/USD | 61.373 | 0.03107 | -0.39% | 0.87x |
| 9 | XRP/USD | 61.135 | 0.93574 | -0.32% | 0.98x |
| 10 | HYPE/USD | 59.532 | 63.61 | -0.62% | 3.84x |
| 11 | XLM/USD | 57.877 | 0.128142 | -0.19% | 2.06x |
| 12 | AUD/USD | 43.084 | 0.66472 | -0.05% | 3.52x |

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

- Persisted scans: 1413; predictions: 11723; observations: 855620.
- Matured sampled outcomes across 1/6/24/48h: 19246; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45150499422 · **Generation:** 1413 · **Legacy run:** 45150499422
**Main quote time:** 2026-11-23T09:51:38.431808+00:00 · **Legacy report time:** 2026-11-23T09:52:46.398329+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 151.65 | 83.37 | -0.36% | 1.38x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 63.61 | 71.41 | -0.62% | 3.84x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | JUP/USD | 0.24317 | 69.74 | -0.18% | 0.56x | WEAK 35/100 | EXTREME 87/100 | Do nothing |
| 4 | XMR/USD | 504.65 | 69.57 | -0.17% | 1.32x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 5 | ALGO/USD | 0.07967 | 69.42 | -0.75% | 1.40x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 6 | XLM/USD | 0.128142 | 67.52 | -0.19% | 2.06x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 72.19 | 64.67 | -0.50% | 0.74x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 8 | Q/USD | 0.027789 | 60.32 | -1.88% | 1.72x | WEAK 40/100 | EXTREME 89/100 | Do nothing |
| 9 | SUI/USD | 0.6675 | 59.50 | -0.36% | 0.44x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.93574 | 59.35 | -0.32% | 0.98x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | UAI/USD | 0.03107 | 58.11 | -0.39% | 0.87x | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing |
| 12 | AUD/USD | 0.66472 | 57.83 | -0.05% | 3.52x | MODERATE 59/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.337 | 83.12 | +1.61% | 1.04x | 7672 | STRONG 72/100 | HIGH 68/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
