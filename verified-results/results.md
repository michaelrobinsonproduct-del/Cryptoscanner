# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T06:41:28.667977+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45125585827
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f6e17144b349ac61fa89a835667328d95d0de854 (atomic ledger/results publication)
**Ledger generation:** 1394 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.23939 | 81.788 | 72.562 | +6.60% | -0.77% | 2.31x | 13.8 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | XRP/USD | 0.93848 | 77.159 | 62.830 | +1.18% | -0.13% | 11.31x | 0.9 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05028 | 61.824 | 61.834 | +2.26% | +0.44% | 0.78x | 10.0 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SOL/USD | 71.66 | 60.987 | 64.511 | +1.46% | -0.07% | 0.68x | 1.4 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XLM/USD | 0.128208 | 59.731 | 58.055 | +0.53% | +0.25% | 1.04x | 0.2 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 6 | CC/USD | 0.07606 | 57.719 | 59.264 | +3.81% | +0.26% | 0.71x | 5.3 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6634 | 56.815 | 62.467 | +1.17% | +0.26% | 0.31x | 1.5 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | QNT/USD | 147.2 | 56.770 | 58.333 | +2.62% | +0.69% | 0.50x | 6.1 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XAUT/USD | 3605.6 | 55.388 | 39.694 | +0.94% | +0.14% | 6.92x | 0.6 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 10 | XBT/USD | 61384.5 | 53.869 | 57.445 | +0.35% | -0.18% | 0.73x | 0.0 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | GBP/USD | 1.31233 | 52.093 | 56.694 | +0.25% | +0.02% | 0.53x | 0.2 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0555286 | 49.942 | 48.717 | +0.44% | +0.09% | 1.08x | 2.1 | 2026-11-23T06:41:22.486929+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 72.562 | 0.23939 | -0.77% | 2.31x |
| 2 | SOL/USD | 64.511 | 71.66 | -0.07% | 0.68x |
| 3 | XRP/USD | 62.830 | 0.93848 | -0.13% | 11.31x |
| 4 | SUI/USD | 62.467 | 0.6634 | +0.26% | 0.31x |
| 5 | NIGHT/USD | 61.834 | 0.05028 | +0.44% | 0.78x |
| 6 | CC/USD | 59.264 | 0.07606 | +0.26% | 0.71x |
| 7 | QNT/USD | 58.333 | 147.2 | +0.69% | 0.50x |
| 8 | XLM/USD | 58.055 | 0.128208 | +0.25% | 1.04x |
| 9 | XBT/USD | 57.445 | 61384.5 | -0.18% | 0.73x |
| 10 | GBP/USD | 56.694 | 1.31233 | +0.02% | 0.53x |
| 11 | XDG/USD | 48.717 | 0.0555286 | +0.09% | 1.08x |
| 12 | XAUT/USD | 39.694 | 3605.6 | +0.14% | 6.92x |

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

- Persisted scans: 1394; predictions: 11495; observations: 844050.
- Matured sampled outcomes across 1/6/24/48h: 18689; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 123 (sampled only; not a success-rate estimate).
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

**Writer:** 45125585827 · **Generation:** 1394 · **Legacy run:** 45125585827
**Main quote time:** 2026-11-23T06:41:28.667977+00:00 · **Legacy report time:** 2026-11-23T06:42:16.972404+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.23939 | 81.79 | -0.77% | 2.31x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 2 | XRP/USD | 0.93848 | 77.16 | -0.13% | 11.31x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD | 0.05028 | 61.82 | +0.44% | 0.78x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 4 | SOL/USD | 71.66 | 60.99 | -0.07% | 0.68x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 5 | XLM/USD ⭐ | 0.128208 | 59.73 | +0.25% | 1.04x | STRONG 75/100 | HIGH 62/100 | Watch |
| 6 | CC/USD | 0.07606 | 57.72 | +0.26% | 0.71x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 7 | SUI/USD | 0.6634 | 56.82 | +0.26% | 0.31x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 8 | QNT/USD | 147.2 | 56.77 | +0.69% | 0.50x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 9 | XAUT/USD | 3605.6 | 55.39 | +0.14% | 6.92x | STRONG 73/100 | HIGH 60/100 | Watch |
| 10 | XBT/USD | 61384.5 | 53.87 | -0.18% | 0.73x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | GBP/USD | 1.31233 | 52.09 | +0.02% | 0.53x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0555286 | 49.94 | +0.09% | 1.08x | MODERATE 50/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD | 0.02722 | 78.25 | +0.63% | 14.96x | 2243 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 2 | ALGO/USD | 0.07829 | 66.60 | +0.29% | 1.19x | 2119 | MODERATE 68/100 | HIGH 67/100 | Watch |
| 3 | PEARL/USD | 2.1075 | 61.21 | +0.21% | 1.23x | 7024 | MODERATE 56/100 | VERY_HIGH 74/100 | Watch |
| 4 | UNI/USD | 4.7791 | 60.79 | +0.09% | 1.05x | 4485 | MODERATE 55/100 | HIGH 62/100 | Watch |
| 5 | XLM/USD ⭐ | 0.128323 | 59.76 | +0.25% | 1.04x | 8727 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
