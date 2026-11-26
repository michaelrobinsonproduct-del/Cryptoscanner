# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T05:15:57.726450+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45760289134
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 144b77834cea272d6f234c1705166111ae72951b (atomic ledger/results publication)
**Ledger generation:** 1817 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.95911 | 78.576 | 71.437 | +2.41% | +0.15% | 1.64x | 0.8 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6697 | 72.155 | 57.826 | +0.51% | -0.13% | 12.77x | 1.5 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 43.81 | 69.899 | 71.887 | +2.58% | -0.11% | 0.86x | 2.3 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.0717 | 67.473 | 66.662 | +8.19% | +0.60% | 0.78x | 20.9 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | XMR/USD | 518.78 | 66.369 | 57.382 | +0.35% | -0.02% | 1.91x | 0.2 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 6 | INJ/USD | 6.161 | 66.294 | 63.376 | +3.48% | +0.98% | 0.80x | 6.5 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ADA/USD | 0.149001 | 62.779 | 68.938 | +2.22% | +0.06% | 0.35x | 3.2 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HYPE/USD | 61.93 | 61.407 | 57.715 | +0.50% | +0.21% | 1.26x | 1.6 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 71.1 | 60.644 | 61.357 | +1.01% | +0.03% | 0.91x | 1.4 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XBT/USD | 60836.6 | 60.546 | 60.418 | +0.78% | -0.13% | 1.08x | 0.0 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XAUT/USD | 3585.5 | 59.327 | 44.411 | +0.46% | -0.02% | 4.55x | 0.3 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XDG/USD | 0.056685 | 58.972 | 59.285 | +1.30% | -0.10% | 1.02x | 0.0 | 2026-11-26T05:15:50.289156+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 71.887 | 43.81 | -0.11% | 0.86x |
| 2 | XRP/USD | 71.437 | 0.95911 | +0.15% | 1.64x |
| 3 | ADA/USD | 68.938 | 0.149001 | +0.06% | 0.35x |
| 4 | SYRUP/USD | 66.662 | 0.0717 | +0.60% | 0.78x |
| 5 | INJ/USD | 63.376 | 6.161 | +0.98% | 0.80x |
| 6 | SOL/USD | 61.357 | 71.1 | +0.03% | 0.91x |
| 7 | XBT/USD | 60.418 | 60836.6 | -0.13% | 1.08x |
| 8 | XDG/USD | 59.285 | 0.056685 | -0.10% | 1.02x |
| 9 | SUI/USD | 57.826 | 0.6697 | -0.13% | 12.77x |
| 10 | HYPE/USD | 57.715 | 61.93 | +0.21% | 1.26x |
| 11 | XMR/USD | 57.382 | 518.78 | -0.02% | 1.91x |
| 12 | XAUT/USD | 44.411 | 3585.5 | -0.02% | 4.55x |

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

- Persisted scans: 1817; predictions: 15539; observations: 1101597.
- Matured sampled outcomes across 1/6/24/48h: 33719; gap abstentions: 23943. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45760289134 · **Generation:** 1817 · **Legacy run:** 45760289134
**Main quote time:** 2026-11-26T05:15:57.726450+00:00 · **Legacy report time:** 2026-11-26T05:16:49.824878+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95911 | 78.58 | +0.15% | 1.64x | STRONG 84/100 | HIGH 55/100 | Watch |
| 2 | SUI/USD | 0.6697 | 72.15 | -0.13% | 12.77x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 43.81 | 69.90 | -0.11% | 0.86x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | SYRUP/USD | 0.0717 | 67.47 | +0.60% | 0.78x | MODERATE 54/100 | VERY_HIGH 79/100 | Watch |
| 5 | XMR/USD | 518.78 | 66.37 | -0.02% | 1.91x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 6 | INJ/USD | 6.161 | 66.29 | +0.98% | 0.80x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 7 | ADA/USD | 0.149001 | 62.78 | +0.06% | 0.35x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | HYPE/USD | 61.93 | 61.41 | +0.21% | 1.26x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD | 71.1 | 60.64 | +0.03% | 0.91x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 10 | XBT/USD | 60836.6 | 60.55 | -0.13% | 1.08x | WEAK 40/100 | HIGH 68/100 | Watch |
| 11 | XAUT/USD | 3585.5 | 59.33 | -0.02% | 4.55x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 12 | XDG/USD | 0.056685 | 58.97 | -0.10% | 1.02x | WEAK 39/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95938 | 84.03 | +0.15% | 1.64x | 42128 | STRONG 87/100 | HIGH 55/100 | Watch |
| 2 | PIEVERSE/USD | 3.7988 | 77.17 | +1.97% | 1.18x | 2296 | MODERATE 59/100 | EXTREME 89/100 | Do nothing |
| 3 | ME/USD | 0.0388 | 70.45 | +0.52% | 1.19x | 2299 | MODERATE 60/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
