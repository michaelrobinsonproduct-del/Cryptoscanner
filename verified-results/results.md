# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T10:55:56.538478+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45805668330
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 46a651edb8d6a7113c4544ddd1915e18a99ccc0d (atomic ledger/results publication)
**Ledger generation:** 1851 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 585; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.94892 | 78.353 | 63.922 | +1.32% | -0.11% | 4.09x | 0.6 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SEI/USD | 0.03581 | 74.156 | 71.794 | +7.51% | -0.42% | 1.45x | 11.2 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0564611 | 70.516 | 56.521 | +0.90% | -0.20% | 3.48x | 0.4 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | HBAR/USD | 0.05361 | 69.006 | 55.494 | +2.90% | -0.30% | 3.95x | 3.7 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07104 | 67.945 | 72.441 | +7.20% | +0.55% | 0.27x | 9.9 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | LINK/USD | 9.1757 | 62.745 | 63.501 | +1.45% | -0.40% | 1.13x | 3.3 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | CC/USD | 0.0794 | 62.077 | 51.137 | +2.52% | -0.81% | 3.29x | 3.8 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 8 | ADA/USD | 0.14773 | 61.692 | 62.075 | +1.34% | -0.26% | 1.09x | 4.7 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XMR/USD | 519.03 | 60.465 | 50.014 | +0.40% | -0.91% | 2.76x | 15.6 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 10 | INJ/USD | 6.155 | 58.149 | 64.868 | +3.38% | -0.29% | 0.47x | 4.9 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | LTC/USD | 43.28 | 56.370 | 63.187 | +1.33% | -0.32% | 0.48x | 2.3 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6683 | 35.166 | 42.988 | +1.52% | -0.33% | 0.38x | 1.5 | 2026-11-26T10:55:47.438797+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 72.441 | 0.07104 | +0.55% | 0.27x |
| 2 | SEI/USD | 71.794 | 0.03581 | -0.42% | 1.45x |
| 3 | INJ/USD | 64.868 | 6.155 | -0.29% | 0.47x |
| 4 | XRP/USD | 63.922 | 0.94892 | -0.11% | 4.09x |
| 5 | LINK/USD | 63.501 | 9.1757 | -0.40% | 1.13x |
| 6 | LTC/USD | 63.187 | 43.28 | -0.32% | 0.48x |
| 7 | ADA/USD | 62.075 | 0.14773 | -0.26% | 1.09x |
| 8 | XDG/USD | 56.521 | 0.0564611 | -0.20% | 3.48x |
| 9 | HBAR/USD | 55.494 | 0.05361 | -0.30% | 3.95x |
| 10 | CC/USD | 51.137 | 0.0794 | -0.81% | 3.29x |
| 11 | XMR/USD | 50.014 | 519.03 | -0.91% | 2.76x |
| 12 | DOT/USD | 42.988 | 0.6683 | -0.33% | 0.38x |

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

- Persisted scans: 1851; predictions: 15947; observations: 1122080.
- Matured sampled outcomes across 1/6/24/48h: 34538; gap abstentions: 24598. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45805668330 · **Generation:** 1851 · **Legacy run:** 45805668330
**Main quote time:** 2026-11-26T10:55:56.538478+00:00 · **Legacy report time:** 2026-11-26T10:56:49.778587+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.94892 | 78.35 | -0.11% | 4.09x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | SEI/USD | 0.03581 | 74.16 | -0.42% | 1.45x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 3 | XDG/USD | 0.0564611 | 70.52 | -0.20% | 3.48x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | HBAR/USD | 0.05361 | 69.01 | -0.30% | 3.95x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | SYRUP/USD | 0.07104 | 67.94 | +0.55% | 0.27x | MODERATE 64/100 | VERY_HIGH 75/100 | Watch |
| 6 | LINK/USD | 9.1757 | 62.74 | -0.40% | 1.13x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | CC/USD | 0.0794 | 62.08 | -0.81% | 3.29x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 8 | ADA/USD | 0.14773 | 61.69 | -0.26% | 1.09x | WEAK 41/100 | HIGH 68/100 | Watch |
| 9 | XMR/USD | 519.03 | 60.46 | -0.91% | 2.76x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 10 | INJ/USD | 6.155 | 58.15 | -0.29% | 0.47x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | LTC/USD | 43.28 | 56.37 | -0.32% | 0.48x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | DOT/USD | 0.6683 | 35.17 | -0.33% | 0.38x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |

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
