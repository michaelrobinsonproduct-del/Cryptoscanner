# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T02:06:16.124807+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45739974230
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4af825a692528175f569d5a7fedfc027cd68218f (atomic ledger/results publication)
**Ledger generation:** 1797 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 3.8289 | 90.392 | 64.763 | +8.13% | +2.13% | 3.44x | 29.4 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | STRONG 90/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | LTC/USD | 43.7 | 86.922 | 70.081 | +2.32% | +0.37% | 3.48x | 2.3 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.95468 | 85.918 | 67.915 | +1.93% | +0.60% | 3.98x | 1.3 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 184.7531 | 79.339 | 62.659 | +1.74% | +0.34% | 3.33x | 9.0 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 30.137 | 78.270 | 74.271 | +3.23% | +0.56% | 1.12x | 6.6 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ZEC/USD | 778.97 | 65.880 | 60.070 | +1.14% | +0.53% | 1.32x | 5.8 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 60793.6 | 65.707 | 59.920 | +0.70% | -0.08% | 1.62x | 0.0 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148106 | 65.605 | 64.597 | +1.60% | +0.40% | 0.90x | 3.2 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6766 | 63.500 | 65.082 | +1.55% | +0.19% | 0.75x | 1.5 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 71.13 | 57.786 | 61.656 | +1.05% | +0.24% | 0.49x | 1.4 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0918 | 56.954 | 62.512 | +1.37% | -0.24% | 0.56x | 4.2 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0567189 | 56.780 | 59.060 | +1.36% | +0.11% | 0.72x | 0.4 | 2026-11-26T02:06:07.601973+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 74.271 | 30.137 | +0.56% | 1.12x |
| 2 | LTC/USD | 70.081 | 43.7 | +0.37% | 3.48x |
| 3 | XRP/USD | 67.915 | 0.95468 | +0.60% | 3.98x |
| 4 | SUI/USD | 65.082 | 0.6766 | +0.19% | 0.75x |
| 5 | PIEVERSE/USD | 64.763 | 3.8289 | +2.13% | 3.44x |
| 6 | ADA/USD | 64.597 | 0.148106 | +0.40% | 0.90x |
| 7 | TAO/USD | 62.659 | 184.7531 | +0.34% | 3.33x |
| 8 | NEAR/USD | 62.512 | 3.0918 | -0.24% | 0.56x |
| 9 | SOL/USD | 61.656 | 71.13 | +0.24% | 0.49x |
| 10 | ZEC/USD | 60.070 | 778.97 | +0.53% | 1.32x |
| 11 | XBT/USD | 59.920 | 60793.6 | -0.08% | 1.62x |
| 12 | XDG/USD | 59.060 | 0.0567189 | +0.11% | 0.72x |

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

- Persisted scans: 1797; predictions: 15299; observations: 1089417.
- Matured sampled outcomes across 1/6/24/48h: 33239; gap abstentions: 23648. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45739974230 · **Generation:** 1797 · **Legacy run:** 45739974230
**Main quote time:** 2026-11-26T02:06:16.124807+00:00 · **Legacy report time:** 2026-11-26T02:07:35.344692+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.8289 | 90.39 | +2.13% | 3.44x | STRONG 100/100 | VERY_HIGH 72/100 | Watch |
| 2 | LTC/USD ⭐ | 43.7 | 86.92 | +0.37% | 3.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95468 | 85.92 | +0.60% | 3.98x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD | 184.7531 | 79.34 | +0.34% | 3.33x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD ⭐ | 30.137 | 78.27 | +0.56% | 1.12x | STRONG 84/100 | HIGH 62/100 | Watch |
| 6 | ZEC/USD | 778.97 | 65.88 | +0.53% | 1.32x | STRONG 78/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD | 60793.6 | 65.71 | -0.08% | 1.62x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.148106 | 65.60 | +0.40% | 0.90x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6766 | 63.50 | +0.19% | 0.75x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 71.13 | 57.79 | +0.24% | 0.49x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 3.0918 | 56.95 | -0.24% | 0.56x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0567189 | 56.78 | +0.11% | 0.72x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.8289 | 81.69 | +2.13% | 3.44x | 1995 | STRONG 91/100 | VERY_HIGH 82/100 | Watch |
| 2 | XRP/USD ⭐ | 0.95458 | 81.54 | +0.60% | 3.98x | 42398 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 43.74 | 80.89 | +0.37% | 3.48x | 14885 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD ⭐ | 30.115 | 76.98 | +0.56% | 1.12x | 18674 | STRONG 78/100 | HIGH 68/100 | Watch |
| 5 | TIA/USD | 0.3469 | 76.06 | +0.52% | 2.38x | 3237 | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 6 | PEPE/USD | 3.559e-06 | 62.87 | +0.40% | 1.25x | 7071 | MODERATE 66/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PIEVERSE/USD, LTC/USD, XRP/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
