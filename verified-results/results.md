# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T23:51:58.953484+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45292099070
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7419f83bff580bfd556cd5ec2ab004a31d3a74a4 (atomic ledger/results publication)
**Ledger generation:** 1498 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 153.9 | 110.626 | 98.050 | +7.29% | -0.48% | 5.19x | 3.9 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08109 | 91.406 | 93.789 | +7.50% | -0.42% | 0.97x | 2.5 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 3 | UNI/USD | 4.8215 | 84.349 | 70.219 | +3.00% | -0.17% | 16.56x | 4.1 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LINK/USD | 8.98218 | 82.999 | 68.271 | +1.94% | -0.05% | 2.90x | 0.6 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LTC/USD | 41.32 | 78.554 | 74.009 | +2.89% | +0.00% | 1.45x | 2.4 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 6 | CAP/USD | 0.099937 | 75.803 | 76.049 | +6.80% | -1.22% | 1.58x | 6.1 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 7 | SHX/USD | 0.003599 | 70.343 | 70.802 | +6.64% | -0.08% | 1.00x | 11.1 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | WEAK 35/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | ADA/USD | 0.147976 | 69.792 | 70.517 | +2.33% | +0.06% | 0.90x | 1.6 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6716 | 65.360 | 71.230 | +2.42% | -0.27% | 0.55x | 1.5 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0562044 | 62.009 | 66.648 | +1.67% | -0.09% | 0.58x | 0.0 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93698 | 55.904 | 61.857 | +1.02% | -0.36% | 0.59x | 0.5 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XAUT/USD | 3611.3 | 54.748 | 40.923 | +1.10% | -0.23% | 2.87x | 0.3 | 2026-11-23T23:51:50.123164+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 98.050 | 153.9 | -0.48% | 5.19x |
| 2 | ALGO/USD | 93.789 | 0.08109 | -0.42% | 0.97x |
| 3 | CAP/USD | 76.049 | 0.099937 | -1.22% | 1.58x |
| 4 | LTC/USD | 74.009 | 41.32 | +0.00% | 1.45x |
| 5 | SUI/USD | 71.230 | 0.6716 | -0.27% | 0.55x |
| 6 | SHX/USD | 70.802 | 0.003599 | -0.08% | 1.00x |
| 7 | ADA/USD | 70.517 | 0.147976 | +0.06% | 0.90x |
| 8 | UNI/USD | 70.219 | 4.8215 | -0.17% | 16.56x |
| 9 | LINK/USD | 68.271 | 8.98218 | -0.05% | 2.90x |
| 10 | XDG/USD | 66.648 | 0.0562044 | -0.09% | 0.58x |
| 11 | XRP/USD | 61.857 | 0.93698 | -0.36% | 0.59x |
| 12 | XAUT/USD | 40.923 | 3611.3 | -0.23% | 2.87x |

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

- Persisted scans: 1498; predictions: 12743; observations: 907384.
- Matured sampled outcomes across 1/6/24/48h: 23272; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45292099070 · **Generation:** 1498 · **Legacy run:** 45292099070
**Main quote time:** 2026-11-23T23:51:58.953484+00:00 · **Legacy report time:** 2026-11-23T23:52:51.101366+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 153.9 | 110.63 | -0.48% | 5.19x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ALGO/USD | 0.08109 | 91.41 | -0.42% | 0.97x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 3 | UNI/USD | 4.8215 | 84.35 | -0.17% | 16.56x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | LINK/USD | 8.98218 | 83.00 | -0.05% | 2.90x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | LTC/USD | 41.32 | 78.55 | +0.00% | 1.45x | STRONG 74/100 | HIGH 55/100 | Watch |
| 6 | CAP/USD | 0.099937 | 75.80 | -1.22% | 1.58x | MODERATE 58/100 | VERY_HIGH 70/100 | Do nothing |
| 7 | SHX/USD | 0.003599 | 70.34 | -0.08% | 1.00x | WEAK 35/100 | EXTREME 86/100 | Do nothing |
| 8 | ADA/USD | 0.147976 | 69.79 | +0.06% | 0.90x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6716 | 65.36 | -0.27% | 0.55x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | XDG/USD | 0.0562044 | 62.01 | -0.09% | 0.58x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.93698 | 55.90 | -0.36% | 0.59x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XAUT/USD | 3611.3 | 54.75 | -0.23% | 2.87x | MODERATE 57/100 | HIGH 66/100 | Watch |

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
