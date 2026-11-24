# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T03:21:27.415217+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45318708442
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c33e2d4d08a98bca3237ba1786770b93f65a37a1 (atomic ledger/results publication)
**Ledger generation:** 1518 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01208 | 69.761 | 68.948 | +4.86% | -0.33% | 1.25x | 8.3 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04843 | 49.448 | 49.541 | +0.58% | -0.58% | 1.28x | 8.3 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | WEAK 35/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XDC/USD | 0.02621 | 45.470 | 33.887 | +0.89% | -0.68% | 3.92x | 15.3 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | AI/USD | 0.01567 | 36.313 | 48.173 | +2.89% | -1.52% | 0.57x | 6.4 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | WEAK 23/100 | EXTREME 92/100 | Do nothing | WATCH |
| 5 | XTZ/USD | 0.21368 | 35.495 | 27.511 | +0.39% | -0.27% | 1.93x | 12.2 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 6 | BAT/USD | 0.07773 | 27.438 | 32.389 | +0.73% | -0.21% | 0.61x | 9.0 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | BABY/USD | 0.00853 | 22.451 | 27.610 | +0.35% | -0.47% | 0.72x | 11.7 | 2026-11-24T03:21:24.365976+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 68.948 | 0.01208 | -0.33% | 1.25x |
| 2 | NIGHT/USD | 49.541 | 0.04843 | -0.58% | 1.28x |
| 3 | AI/USD | 48.173 | 0.01567 | -1.52% | 0.57x |
| 4 | XDC/USD | 33.887 | 0.02621 | -0.68% | 3.92x |
| 5 | BAT/USD | 32.389 | 0.07773 | -0.21% | 0.61x |
| 6 | BABY/USD | 27.610 | 0.00853 | -0.47% | 0.72x |
| 7 | XTZ/USD | 27.511 | 0.21368 | -0.27% | 1.93x |

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

- Persisted scans: 1518; predictions: 12955; observations: 919561.
- Matured sampled outcomes across 1/6/24/48h: 24067; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45318708442 · **Generation:** 1518 · **Legacy run:** 45318708442
**Main quote time:** 2026-11-24T03:21:27.415217+00:00 · **Legacy report time:** 2026-11-24T03:22:36.143638+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01208 | 69.76 | -0.33% | 1.25x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 2 | NIGHT/USD | 0.04843 | 49.45 | -0.58% | 1.28x | WEAK 35/100 | HIGH 61/100 | Watch |
| 3 | XDC/USD | 0.02621 | 45.47 | -0.68% | 3.92x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 4 | AI/USD | 0.01567 | 36.31 | -1.52% | 0.57x | WEAK 23/100 | EXTREME 92/100 | Do nothing |
| 5 | XTZ/USD | 0.21368 | 35.50 | -0.27% | 1.93x | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing |
| 6 | BAT/USD | 0.07773 | 27.44 | -0.21% | 0.61x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | BABY/USD | 0.00853 | 22.45 | -0.47% | 0.72x | WEAK 11/100 | EXTREME 94/100 | Do nothing |

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
