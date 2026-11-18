# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:25:03.377237+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44244051052
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 46f97d6bc67b952221bf8b7d8decfa0a38f7593e (atomic ledger/results publication)
**Ledger generation:** 542 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019696 | 71.351 | 65.428 | +5.50% | +1.29% | 0.95x | 8.1 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | UP/USD | 0.05537 | 71.289 | 60.980 | +4.49% | +0.02% | 2.02x | 5.4 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98518 | 64.293 | 56.279 | +0.27% | +0.45% | 1.57x | 1.2 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 4 | CC/USD | 0.08405 | 46.413 | 47.831 | +2.34% | +0.67% | 0.52x | 8.3 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05196 | 41.477 | 25.029 | +0.62% | +0.29% | 4.68x | 21.2 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | XDC/USD | 0.0308 | 36.703 | 45.666 | +1.58% | -0.36% | 0.28x | 6.5 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | MNT/USD | 0.3757 | 33.702 | 33.349 | +0.64% | +0.80% | 0.63x | 8.0 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | MELANIA/USD | 0.0496 | 23.073 | 23.459 | +1.85% | -0.40% | 1.16x | 40.6 | 2026-11-18T05:24:58.382772+00:00 | Not calibrated | WEAK 7/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 65.428 | 0.019696 | +1.29% | 0.95x |
| 2 | UP/USD | 60.980 | 0.05537 | +0.02% | 2.02x |
| 3 | XRP/USD | 56.279 | 0.98518 | +0.45% | 1.57x |
| 4 | CC/USD | 47.831 | 0.08405 | +0.67% | 0.52x |
| 5 | XDC/USD | 45.666 | 0.0308 | -0.36% | 0.28x |
| 6 | MNT/USD | 33.349 | 0.3757 | +0.80% | 0.63x |
| 7 | MEGA/USD | 25.029 | 0.05196 | +0.29% | 4.68x |
| 8 | MELANIA/USD | 23.459 | 0.0496 | -0.40% | 1.16x |

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

- Persisted scans: 542; predictions: 4575; observations: 327085.
- Matured sampled outcomes across 1/6/24/48h: 3699; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44244051052 · **Generation:** 542 · **Legacy run:** 44244051052
**Main quote time:** 2026-11-18T05:25:03.377237+00:00 · **Legacy report time:** 2026-11-18T05:25:23.823302+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019696 | 71.35 | +1.29% | 0.95x | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |
| 2 | UP/USD ⭐ | 0.05537 | 71.29 | +0.02% | 2.02x | STRONG 91/100 | HIGH 60/100 | Watch |
| 3 | XRP/USD ⭐ | 0.98518 | 64.29 | +0.45% | 1.57x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 4 | CC/USD | 0.08405 | 46.41 | +0.67% | 0.52x | MODERATE 53/100 | VERY_HIGH 75/100 | Watch |
| 5 | MEGA/USD | 0.05196 | 41.48 | +0.29% | 4.68x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 6 | XDC/USD | 0.0308 | 36.70 | -0.36% | 0.28x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | MNT/USD | 0.3757 | 33.70 | +0.80% | 0.63x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 8 | MELANIA/USD | 0.0496 | 23.07 | -0.40% | 1.16x | WEAK 7/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD ⭐ | 0.05522 | 85.33 | +0.62% | 3.21x | 6508 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.98454 | 59.12 | +0.79% | 1.98x | 31938 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 21.07 | 48.10 | +1.33% | 10.12x | 7532 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UP/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
