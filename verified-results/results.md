# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T17:31:01.642819+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45868173605
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e33eef96e5aa84463cbad0b7ee7575b8ea334a5c (atomic ledger/results publication)
**Ledger generation:** 1891 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 595; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WIF/USD | 0.1364 | 86.023 | 69.157 | +7.15% | +0.52% | 2.43x | 14.7 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | STRONG 93/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | LINK/USD | 9.1933 | 79.140 | 63.828 | +1.65% | +0.06% | 9.24x | 5.4 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04577 | 71.068 | 75.312 | +9.29% | +0.00% | 0.58x | 8.7 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | ADA/USD | 0.148738 | 69.769 | 67.435 | +2.04% | +0.06% | 1.20x | 3.6 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HBAR/USD | 0.05388 | 66.727 | 57.824 | +3.42% | +0.32% | 1.73x | 3.7 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.01761 | 66.192 | 68.175 | +6.60% | +0.23% | 0.69x | 17.0 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | SOL/USD | 70.77 | 64.974 | 58.072 | +0.54% | -0.18% | 1.78x | 1.4 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.94691 | 63.203 | 62.208 | +1.11% | -0.14% | 1.17x | 1.1 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | FET/USD | 0.1153 | 61.789 | 68.608 | +6.27% | -0.09% | 0.36x | 17.4 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | QNT/USD | 148.94 | 59.758 | 62.005 | +2.86% | -0.45% | 1.00x | 4.0 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0592 | 58.401 | 55.826 | +0.30% | +0.25% | 1.13x | 2.6 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 12 | DRV/USD | 0.3714 | 58.280 | 60.664 | +3.80% | +0.30% | 0.61x | 3.8 | 2026-11-26T17:30:54.695311+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.312 | 0.04577 | +0.00% | 0.58x |
| 2 | WIF/USD | 69.157 | 0.1364 | +0.52% | 2.43x |
| 3 | FET/USD | 68.608 | 0.1153 | -0.09% | 0.36x |
| 4 | 2Z/USD | 68.175 | 0.01761 | +0.23% | 0.69x |
| 5 | ADA/USD | 67.435 | 0.148738 | +0.06% | 1.20x |
| 6 | LINK/USD | 63.828 | 9.1933 | +0.06% | 9.24x |
| 7 | XRP/USD | 62.208 | 0.94691 | -0.14% | 1.17x |
| 8 | QNT/USD | 62.005 | 148.94 | -0.45% | 1.00x |
| 9 | DRV/USD | 60.664 | 0.3714 | +0.30% | 0.61x |
| 10 | SOL/USD | 58.072 | 70.77 | -0.18% | 1.78x |
| 11 | HBAR/USD | 57.824 | 0.05388 | +0.32% | 1.73x |
| 12 | NEAR/USD | 55.826 | 3.0592 | +0.25% | 1.13x |

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

- Persisted scans: 1891; predictions: 16427; observations: 1145677.
- Matured sampled outcomes across 1/6/24/48h: 35511; gap abstentions: 25099. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45868173605 · **Generation:** 1891 · **Legacy run:** 45868173605
**Main quote time:** 2026-11-26T17:31:01.642819+00:00 · **Legacy report time:** 2026-11-26T17:31:41.860426+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WIF/USD | 0.1364 | 86.02 | +0.52% | 2.43x | STRONG 93/100 | VERY_HIGH 73/100 | Watch |
| 2 | LINK/USD | 9.1933 | 79.14 | +0.06% | 9.24x | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD | 0.04577 | 71.07 | +0.00% | 0.58x | MODERATE 56/100 | VERY_HIGH 75/100 | Watch |
| 4 | ADA/USD ⭐ | 0.148738 | 69.77 | +0.06% | 1.20x | STRONG 70/100 | HIGH 62/100 | Watch |
| 5 | HBAR/USD ⭐ | 0.05388 | 66.73 | +0.32% | 1.73x | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 6 | 2Z/USD | 0.01761 | 66.19 | +0.23% | 0.69x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 7 | SOL/USD | 70.77 | 64.97 | -0.18% | 1.78x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.94691 | 63.20 | -0.14% | 1.17x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | FET/USD | 0.1153 | 61.79 | -0.09% | 0.36x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 10 | QNT/USD | 148.94 | 59.76 | -0.45% | 1.00x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | NEAR/USD | 3.0592 | 58.40 | +0.25% | 1.13x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 12 | DRV/USD | 0.3714 | 58.28 | +0.30% | 0.61x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05394 | 79.30 | +0.32% | 1.73x | 5353 | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.148654 | 68.53 | +0.06% | 1.20x | 10688 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ADA/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
