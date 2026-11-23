# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:04:40.637974+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45161052084
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 19d984542c01f05a672df014567589f15135717e (atomic ledger/results publication)
**Ledger generation:** 1421 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 152.64 | 91.349 | 88.897 | +6.41% | +0.07% | 1.21x | 5.9 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XRP/USD | 0.93955 | 75.359 | 63.691 | +1.29% | -0.04% | 2.19x | 0.7 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | JUP/USD | 0.24091 | 74.713 | 74.757 | +7.28% | +0.02% | 0.99x | 10.8 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | ALGO/USD | 0.08155 | 73.943 | 74.756 | +8.11% | -0.12% | 0.98x | 8.6 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.07616 | 70.901 | 61.234 | +3.94% | +0.28% | 1.83x | 2.6 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 72.15 | 69.274 | 69.371 | +2.15% | +0.08% | 0.95x | 1.4 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XLM/USD | 0.129087 | 66.826 | 62.527 | +1.22% | +0.15% | 1.35x | 0.2 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 8 | HYPE/USD | 64.25 | 65.349 | 66.653 | +1.89% | +0.33% | 0.71x | 3.1 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SUI/USD | 0.669 | 65.304 | 67.704 | +2.03% | +0.06% | 0.73x | 3.0 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XMR/USD | 502.41 | 63.957 | 63.451 | +1.76% | -0.06% | 1.08x | 7.8 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | KAS/USD | 0.02714 | 58.857 | 61.204 | +5.15% | -0.70% | 1.11x | 18.5 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 12 | XBT/USD | 61346.5 | 56.621 | 57.011 | +0.29% | +0.16% | 0.88x | 0.0 | 2026-11-23T11:04:32.028533+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 88.897 | 152.64 | +0.07% | 1.21x |
| 2 | JUP/USD | 74.757 | 0.24091 | +0.02% | 0.99x |
| 3 | ALGO/USD | 74.756 | 0.08155 | -0.12% | 0.98x |
| 4 | SOL/USD | 69.371 | 72.15 | +0.08% | 0.95x |
| 5 | SUI/USD | 67.704 | 0.669 | +0.06% | 0.73x |
| 6 | HYPE/USD | 66.653 | 64.25 | +0.33% | 0.71x |
| 7 | XRP/USD | 63.691 | 0.93955 | -0.04% | 2.19x |
| 8 | XMR/USD | 63.451 | 502.41 | -0.06% | 1.08x |
| 9 | XLM/USD | 62.527 | 0.129087 | +0.15% | 1.35x |
| 10 | CC/USD | 61.234 | 0.07616 | +0.28% | 1.83x |
| 11 | KAS/USD | 61.204 | 0.02714 | -0.70% | 1.11x |
| 12 | XBT/USD | 57.011 | 61346.5 | +0.16% | 0.88x |

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

- Persisted scans: 1421; predictions: 11819; observations: 860492.
- Matured sampled outcomes across 1/6/24/48h: 19538; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45161052084 · **Generation:** 1421 · **Legacy run:** 45161052084
**Main quote time:** 2026-11-23T11:04:40.637974+00:00 · **Legacy report time:** 2026-11-23T11:05:48.274460+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 152.64 | 91.35 | +0.07% | 1.21x | STRONG 71/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD | 0.93955 | 75.36 | -0.04% | 2.19x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | JUP/USD | 0.24091 | 74.71 | +0.02% | 0.99x | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |
| 4 | ALGO/USD | 0.08155 | 73.94 | -0.12% | 0.98x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.07616 | 70.90 | +0.28% | 1.83x | STRONG 80/100 | HIGH 60/100 | Consider small entry |
| 6 | SOL/USD | 72.15 | 69.27 | +0.08% | 0.95x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 7 | XLM/USD ⭐ | 0.129087 | 66.83 | +0.15% | 1.35x | STRONG 78/100 | HIGH 55/100 | Watch |
| 8 | HYPE/USD | 64.25 | 65.35 | +0.33% | 0.71x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 9 | SUI/USD | 0.669 | 65.30 | +0.06% | 0.73x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | XMR/USD | 502.41 | 63.96 | -0.06% | 1.08x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | KAS/USD | 0.02714 | 58.86 | -0.70% | 1.11x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 12 | XBT/USD | 61346.5 | 56.62 | +0.16% | 0.88x | MODERATE 48/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.129078 | 67.55 | +0.21% | 1.26x | 11802 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
