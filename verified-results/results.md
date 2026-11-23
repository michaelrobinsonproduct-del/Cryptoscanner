# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T09:41:53.015923+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45149063334
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c81500e5f2ccc86592efc746d87b5bb6f6ce190e (atomic ledger/results publication)
**Ledger generation:** 1412 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.24406 | 90.931 | 75.931 | +8.68% | +0.00% | 4.83x | 8.6 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 2 | QNT/USD | 152.92 | 90.047 | 85.708 | +6.61% | +1.05% | 0.91x | 10.5 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | STRONG 70/100 | HIGH 68/100 | Watch | WATCH |
| 3 | HYPE/USD | 63.93 | 78.639 | 63.874 | +1.38% | -0.05% | 2.67x | 1.6 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.35 | 75.935 | 71.355 | +2.44% | -0.15% | 1.53x | 1.4 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XBT/USD | 61510.4 | 71.132 | 58.886 | +0.56% | -0.26% | 2.35x | 0.0 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ALGO/USD | 0.08019 | 66.873 | 74.611 | +6.31% | -0.09% | 0.27x | 7.5 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | XMR/USD | 504.66 | 63.520 | 67.156 | +2.22% | -0.18% | 0.73x | 6.7 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6694 | 62.709 | 68.132 | +2.09% | -0.12% | 0.52x | 3.0 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93714 | 61.985 | 62.192 | +1.03% | -0.25% | 1.11x | 0.1 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0554909 | 61.260 | 51.094 | +0.37% | -0.33% | 2.18x | 0.8 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128171 | 59.065 | 58.041 | +0.50% | -0.33% | 1.27x | 0.1 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | WEAK 40/100 | HIGH 61/100 | Watch | WATCH |
| 12 | UAI/USD | 0.03107 | 54.047 | 59.747 | +5.07% | -1.21% | 1.03x | 12.9 | 2026-11-23T09:41:44.242594+00:00 | Not calibrated | WEAK 32/100 | EXTREME 90/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 85.708 | 152.92 | +1.05% | 0.91x |
| 2 | JUP/USD | 75.931 | 0.24406 | +0.00% | 4.83x |
| 3 | ALGO/USD | 74.611 | 0.08019 | -0.09% | 0.27x |
| 4 | SOL/USD | 71.355 | 72.35 | -0.15% | 1.53x |
| 5 | SUI/USD | 68.132 | 0.6694 | -0.12% | 0.52x |
| 6 | XMR/USD | 67.156 | 504.66 | -0.18% | 0.73x |
| 7 | HYPE/USD | 63.874 | 63.93 | -0.05% | 2.67x |
| 8 | XRP/USD | 62.192 | 0.93714 | -0.25% | 1.11x |
| 9 | UAI/USD | 59.747 | 0.03107 | -1.21% | 1.03x |
| 10 | XBT/USD | 58.886 | 61510.4 | -0.26% | 2.35x |
| 11 | XLM/USD | 58.041 | 0.128171 | -0.33% | 1.27x |
| 12 | XDG/USD | 51.094 | 0.0554909 | -0.33% | 2.18x |

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

- Persisted scans: 1412; predictions: 11711; observations: 855011.
- Matured sampled outcomes across 1/6/24/48h: 19212; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45149063334 · **Generation:** 1412 · **Legacy run:** 45149063334
**Main quote time:** 2026-11-23T09:41:53.015923+00:00 · **Legacy report time:** 2026-11-23T09:42:42.793233+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.24406 | 90.93 | +0.00% | 4.83x | STRONG 90/100 | HIGH 60/100 | Watch |
| 2 | QNT/USD | 152.92 | 90.05 | +1.05% | 0.91x | STRONG 70/100 | HIGH 68/100 | Watch |
| 3 | HYPE/USD | 63.93 | 78.64 | -0.05% | 2.67x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.35 | 75.94 | -0.15% | 1.53x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 5 | XBT/USD | 61510.4 | 71.13 | -0.26% | 2.35x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 6 | ALGO/USD | 0.08019 | 66.87 | -0.09% | 0.27x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 7 | XMR/USD | 504.66 | 63.52 | -0.18% | 0.73x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 8 | SUI/USD | 0.6694 | 62.71 | -0.12% | 0.52x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | XRP/USD | 0.93714 | 61.99 | -0.25% | 1.11x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | XDG/USD | 0.0554909 | 61.26 | -0.33% | 2.18x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 11 | XLM/USD | 0.128171 | 59.07 | -0.33% | 1.27x | WEAK 40/100 | HIGH 61/100 | Watch |
| 12 | UAI/USD | 0.03107 | 54.05 | -1.21% | 1.03x | WEAK 32/100 | EXTREME 90/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.3371 | 90.26 | +1.43% | 4.03x | 7559 | STRONG 90/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
