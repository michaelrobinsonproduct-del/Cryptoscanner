# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:35:05.800519+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44245206704
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 4f0a9ac6d6d8514464cf33cb62b6e26f9a559cee (atomic ledger/results publication)
**Ledger generation:** 544 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UP/USD | 0.05529 | 76.228 | 61.772 | +4.34% | -0.11% | 3.04x | 1.8 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | MODERATE 68/100 | HIGH 66/100 | Watch | WATCH |
| 2 | XRP/USD | 0.987 | 74.970 | 57.881 | +0.45% | +0.42% | 2.72x | 0.6 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.019863 | 71.432 | 71.982 | +6.40% | +0.27% | 0.81x | 7.6 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | VVV/USD | 21.155 | 65.892 | 48.637 | +0.61% | +0.45% | 13.25x | 9.9 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.4102 | 65.056 | 58.317 | +0.52% | +0.69% | 1.33x | 0.6 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 6 | CC/USD | 0.08439 | 52.211 | 51.868 | +2.75% | +0.49% | 0.79x | 5.9 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 7 | QNT/USD | 156.49 | 46.760 | 41.514 | +0.32% | +0.85% | 1.10x | 13.4 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XDC/USD | 0.03088 | 39.509 | 44.361 | +1.85% | +0.26% | 0.38x | 13.0 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | MNT/USD | 0.3771 | 36.337 | 36.002 | +1.02% | +0.56% | 0.75x | 8.0 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 10 | PEARL/USD | 1.8438 | 32.251 | 37.382 | +1.84% | +0.35% | 0.31x | 20.6 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | WEAK 36/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | MELANIA/USD | 0.0496 | 27.305 | 33.724 | +1.85% | -0.20% | 0.46x | 20.0 | 2026-11-18T05:34:58.174946+00:00 | Not calibrated | WEAK 9/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 71.982 | 0.019863 | +0.27% | 0.81x |
| 2 | UP/USD | 61.772 | 0.05529 | -0.11% | 3.04x |
| 3 | NEAR/USD | 58.317 | 3.4102 | +0.69% | 1.33x |
| 4 | XRP/USD | 57.881 | 0.987 | +0.42% | 2.72x |
| 5 | CC/USD | 51.868 | 0.08439 | +0.49% | 0.79x |
| 6 | VVV/USD | 48.637 | 21.155 | +0.45% | 13.25x |
| 7 | XDC/USD | 44.361 | 0.03088 | +0.26% | 0.38x |
| 8 | QNT/USD | 41.514 | 156.49 | +0.85% | 1.10x |
| 9 | PEARL/USD | 37.382 | 1.8438 | +0.35% | 0.31x |
| 10 | MNT/USD | 36.002 | 0.3771 | +0.56% | 0.75x |
| 11 | MELANIA/USD | 33.724 | 0.0496 | -0.20% | 0.46x |

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

- Persisted scans: 544; predictions: 4595; observations: 328303.
- Matured sampled outcomes across 1/6/24/48h: 3746; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44245206704 · **Generation:** 544 · **Legacy run:** 44245206704
**Main quote time:** 2026-11-18T05:35:05.800519+00:00 · **Legacy report time:** 2026-11-18T05:35:21.743218+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD | 0.05529 | 76.23 | -0.11% | 3.04x | MODERATE 68/100 | HIGH 66/100 | Watch |
| 2 | XRP/USD ⭐ | 0.987 | 74.97 | +0.42% | 2.72x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD | 0.019863 | 71.43 | +0.27% | 0.81x | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |
| 4 | VVV/USD ⭐ | 21.155 | 65.89 | +0.45% | 13.25x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.4102 | 65.06 | +0.69% | 1.33x | STRONG 88/100 | HIGH 55/100 | Watch |
| 6 | CC/USD | 0.08439 | 52.21 | +0.49% | 0.79x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 7 | QNT/USD ⭐ | 156.49 | 46.76 | +0.85% | 1.10x | MODERATE 63/100 | HIGH 68/100 | Watch |
| 8 | XDC/USD | 0.03088 | 39.51 | +0.26% | 0.38x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 9 | MNT/USD | 0.3771 | 36.34 | +0.56% | 0.75x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 10 | PEARL/USD | 1.8438 | 32.25 | +0.35% | 0.31x | WEAK 36/100 | EXTREME 87/100 | Do nothing |
| 11 | MELANIA/USD | 0.0496 | 27.30 | -0.20% | 0.46x | WEAK 9/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.41 | 68.03 | +0.83% | 9.25x | 15890 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.98704 | 63.90 | +0.40% | 2.70x | 32104 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD | 75.23 | 52.96 | +0.13% | 1.29x | 38267 | MODERATE 51/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD ⭐ | 21.112 | 51.44 | +0.45% | 13.25x | 7519 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 5 | QNT/USD ⭐ | 156.47 | 49.95 | +1.91% | 10.18x | 4824 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 6 | XLM/USD | 0.141582 | 46.30 | +0.36% | 1.23x | 6729 | MODERATE 58/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD, VVV/USD, NEAR/USD, QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
