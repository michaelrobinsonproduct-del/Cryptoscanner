# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T15:21:22.184262+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45847945735
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6188b98f4079da79a01f6304e1653e73a72795bc (atomic ledger/results publication)
**Ledger generation:** 1878 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.0461 | 81.263 | 74.139 | +10.08% | -0.04% | 1.73x | 10.8 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | LINK/USD | 9.11907 | 75.037 | 59.707 | +0.82% | +0.07% | 11.04x | 2.1 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ADA/USD | 0.147139 | 74.929 | 59.024 | +0.94% | +0.18% | 7.75x | 5.1 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LTC/USD | 43.21 | 74.840 | 60.880 | +1.17% | -0.21% | 5.69x | 4.6 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZRO/USD | 1.067 | 72.572 | 58.974 | +4.20% | -0.28% | 14.85x | 18.7 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94089 | 72.540 | 58.183 | +0.46% | -0.13% | 7.16x | 0.1 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SEI/USD | 0.03688 | 69.097 | 73.499 | +10.72% | -0.73% | 0.93x | 10.8 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | QNT/USD | 147.31 | 68.860 | 52.736 | +1.73% | +0.22% | 2.91x | 7.5 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0562483 | 64.335 | 49.847 | +0.52% | -0.10% | 6.99x | 1.7 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 10 | WIF/USD | 0.1333 | 60.835 | 60.507 | +4.71% | +0.53% | 0.77x | 7.5 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | ALGO/USD | 0.07891 | 57.365 | 40.903 | +1.05% | +0.29% | 8.55x | 5.1 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05331 | 55.187 | 50.805 | +2.32% | -0.58% | 1.73x | 3.8 | 2026-11-26T15:21:14.975644+00:00 | Not calibrated | MODERATE 48/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 74.139 | 0.0461 | -0.04% | 1.73x |
| 2 | SEI/USD | 73.499 | 0.03688 | -0.73% | 0.93x |
| 3 | LTC/USD | 60.880 | 43.21 | -0.21% | 5.69x |
| 4 | WIF/USD | 60.507 | 0.1333 | +0.53% | 0.77x |
| 5 | LINK/USD | 59.707 | 9.11907 | +0.07% | 11.04x |
| 6 | ADA/USD | 59.024 | 0.147139 | +0.18% | 7.75x |
| 7 | ZRO/USD | 58.974 | 1.067 | -0.28% | 14.85x |
| 8 | XRP/USD | 58.183 | 0.94089 | -0.13% | 7.16x |
| 9 | QNT/USD | 52.736 | 147.31 | +0.22% | 2.91x |
| 10 | HBAR/USD | 50.805 | 0.05331 | -0.58% | 1.73x |
| 11 | XDG/USD | 49.847 | 0.0562483 | -0.10% | 6.99x |
| 12 | ALGO/USD | 40.903 | 0.07891 | +0.29% | 8.55x |

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

- Persisted scans: 1878; predictions: 16271; observations: 1137965.
- Matured sampled outcomes across 1/6/24/48h: 35186; gap abstentions: 24981. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45847945735 · **Generation:** 1878 · **Legacy run:** 45847945735
**Main quote time:** 2026-11-26T15:21:22.184262+00:00 · **Legacy report time:** 2026-11-26T15:22:34.965763+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.0461 | 81.26 | -0.04% | 1.73x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 2 | LINK/USD | 9.11907 | 75.04 | +0.07% | 11.04x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD | 0.147139 | 74.93 | +0.18% | 7.75x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD | 43.21 | 74.84 | -0.21% | 5.69x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | ZRO/USD | 1.067 | 72.57 | -0.28% | 14.85x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 6 | XRP/USD | 0.94089 | 72.54 | -0.13% | 7.16x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 7 | SEI/USD | 0.03688 | 69.10 | -0.73% | 0.93x | WEAK 35/100 | VERY_HIGH 79/100 | Watch |
| 8 | QNT/USD | 147.31 | 68.86 | +0.22% | 2.91x | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | XDG/USD | 0.0562483 | 64.34 | -0.10% | 6.99x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 10 | WIF/USD | 0.1333 | 60.83 | +0.53% | 0.77x | MODERATE 60/100 | VERY_HIGH 74/100 | Watch |
| 11 | ALGO/USD | 0.07891 | 57.37 | +0.29% | 8.55x | STRONG 84/100 | HIGH 60/100 | Watch |
| 12 | HBAR/USD | 0.05331 | 55.19 | -0.58% | 1.73x | MODERATE 48/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SSV/USD | 2.651 | 73.49 | +1.30% | 3.90x | 1519 | STRONG 77/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
