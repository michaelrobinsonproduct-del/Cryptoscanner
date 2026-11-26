# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T12:01:02.604854+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45815491759
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6c67026a4a32f71401db8b5a9e6fd55dd3598743 (atomic ledger/results publication)
**Ledger generation:** 1858 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | FET/USD | 0.116 | 93.458 | 74.549 | +6.91% | +0.78% | 3.98x | 8.6 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 6.228 | 84.870 | 73.309 | +4.60% | +0.37% | 1.97x | 4.8 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SKY/USD | 0.04537 | 82.972 | 74.541 | +8.33% | +1.14% | 1.27x | 8.8 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | STRONG 76/100 | HIGH 60/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.07174 | 81.134 | 67.487 | +8.25% | +0.10% | 2.32x | 19.6 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95167 | 68.831 | 66.241 | +1.61% | -0.13% | 1.33x | 0.1 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SEI/USD | 0.03702 | 65.404 | 72.319 | +11.14% | -0.05% | 0.34x | 10.8 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | XDG/USD | 0.0568113 | 64.072 | 60.691 | +1.52% | +0.05% | 1.31x | 1.6 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LTC/USD | 43.5 | 63.870 | 66.799 | +1.85% | -0.02% | 0.72x | 2.3 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ETH/USD | 1698.89 | 60.932 | 58.482 | +0.50% | -0.02% | 1.25x | 0.1 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | WEAK 40/100 | HIGH 61/100 | Watch | WATCH |
| 10 | LINK/USD | 9.21727 | 60.558 | 66.146 | +1.91% | +0.02% | 0.43x | 4.4 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.148547 | 60.435 | 66.518 | +1.91% | +0.18% | 0.30x | 3.6 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | QNT/USD | 148.45 | 59.222 | 63.482 | +2.52% | +0.09% | 0.53x | 6.1 | 2026-11-26T12:00:56.750763+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | FET/USD | 74.549 | 0.116 | +0.78% | 3.98x |
| 2 | SKY/USD | 74.541 | 0.04537 | +1.14% | 1.27x |
| 3 | INJ/USD | 73.309 | 6.228 | +0.37% | 1.97x |
| 4 | SEI/USD | 72.319 | 0.03702 | -0.05% | 0.34x |
| 5 | SYRUP/USD | 67.487 | 0.07174 | +0.10% | 2.32x |
| 6 | LTC/USD | 66.799 | 43.5 | -0.02% | 0.72x |
| 7 | ADA/USD | 66.518 | 0.148547 | +0.18% | 0.30x |
| 8 | XRP/USD | 66.241 | 0.95167 | -0.13% | 1.33x |
| 9 | LINK/USD | 66.146 | 9.21727 | +0.02% | 0.43x |
| 10 | QNT/USD | 63.482 | 148.45 | +0.09% | 0.53x |
| 11 | XDG/USD | 60.691 | 0.0568113 | +0.05% | 1.31x |
| 12 | ETH/USD | 58.482 | 1698.89 | -0.02% | 1.25x |

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

- Persisted scans: 1858; predictions: 16031; observations: 1126185.
- Matured sampled outcomes across 1/6/24/48h: 34694; gap abstentions: 24699. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45815491759 · **Generation:** 1858 · **Legacy run:** 45815491759
**Main quote time:** 2026-11-26T12:01:02.604854+00:00 · **Legacy report time:** 2026-11-26T12:01:59.923162+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD ⭐ | 0.116 | 93.46 | +0.78% | 3.98x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.228 | 84.87 | +0.37% | 1.97x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.04537 | 82.97 | +1.14% | 1.27x | STRONG 86/100 | HIGH 60/100 | Watch |
| 4 | SYRUP/USD ⭐ | 0.07174 | 81.13 | +0.10% | 2.32x | STRONG 91/100 | HIGH 66/100 | Watch |
| 5 | XRP/USD | 0.95167 | 68.83 | -0.13% | 1.33x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 6 | SEI/USD | 0.03702 | 65.40 | -0.05% | 0.34x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 7 | XDG/USD ⭐ | 0.0568113 | 64.07 | +0.05% | 1.31x | STRONG 77/100 | HIGH 55/100 | Watch |
| 8 | LTC/USD | 43.5 | 63.87 | -0.02% | 0.72x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | ETH/USD | 1698.89 | 60.93 | -0.02% | 1.25x | WEAK 40/100 | HIGH 61/100 | Watch |
| 10 | LINK/USD | 9.21727 | 60.56 | +0.02% | 0.43x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.148547 | 60.43 | +0.18% | 0.30x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | QNT/USD | 148.45 | 59.22 | +0.09% | 0.53x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.231 | 94.93 | +0.37% | 1.97x | 7273 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1162 | 80.33 | +0.78% | 3.98x | 2360 | STRONG 95/100 | VERY_HIGH 72/100 | Watch |
| 3 | ALGO/USD | 0.08103 | 77.54 | +0.24% | 2.07x | 5073 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | SYRUP/USD ⭐ | 0.07175 | 76.92 | +0.10% | 2.32x | 3893 | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 5 | SKY/USD ⭐ | 0.04551 | 76.89 | +1.14% | 1.27x | 4380 | STRONG 83/100 | HIGH 60/100 | Watch |
| 6 | XDG/USD ⭐ | 0.0569596 | 71.17 | +0.05% | 1.31x | 7857 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** FET/USD, INJ/USD, SKY/USD, SYRUP/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
