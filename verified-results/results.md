# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T11:50:59.131474+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45814030505
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d8f3fdc0bf028cc9ffd56f4f47f50931236ef2b5 (atomic ledger/results publication)
**Ledger generation:** 1857 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03696 | 88.708 | 72.272 | +10.96% | +0.71% | 2.29x | 10.8 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | STRONG 94/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | XDG/USD | 0.0567902 | 76.988 | 61.030 | +1.49% | +0.19% | 3.94x | 0.3 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04499 | 76.581 | 77.740 | +7.43% | +0.56% | 0.60x | 2.2 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | XRP/USD | 0.95228 | 73.004 | 66.067 | +1.68% | +0.09% | 1.65x | 1.4 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 5 | HBAR/USD | 0.05402 | 70.129 | 60.892 | +3.69% | +0.60% | 1.63x | 3.7 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | FET/USD | 0.1153 | 68.906 | 68.675 | +6.27% | +0.09% | 0.98x | 17.4 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | LTC/USD | 43.55 | 67.625 | 67.619 | +1.97% | +0.28% | 0.86x | 2.3 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 8 | INJ/USD | 6.179 | 65.903 | 67.346 | +3.78% | -0.10% | 0.90x | 4.9 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SYRUP/USD | 0.07134 | 65.415 | 67.446 | +7.65% | -0.52% | 1.05x | 19.7 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | LINK/USD | 9.24058 | 64.979 | 69.465 | +2.17% | +0.12% | 0.49x | 1.4 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.148479 | 64.679 | 67.302 | +1.86% | +0.27% | 0.60x | 1.4 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | WIF/USD | 0.1338 | 64.534 | 63.198 | +5.11% | +0.00% | 1.13x | 7.5 | 2026-11-26T11:50:51.221375+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 77.740 | 0.04499 | +0.56% | 0.60x |
| 2 | SEI/USD | 72.272 | 0.03696 | +0.71% | 2.29x |
| 3 | LINK/USD | 69.465 | 9.24058 | +0.12% | 0.49x |
| 4 | FET/USD | 68.675 | 0.1153 | +0.09% | 0.98x |
| 5 | LTC/USD | 67.619 | 43.55 | +0.28% | 0.86x |
| 6 | SYRUP/USD | 67.446 | 0.07134 | -0.52% | 1.05x |
| 7 | INJ/USD | 67.346 | 6.179 | -0.10% | 0.90x |
| 8 | ADA/USD | 67.302 | 0.148479 | +0.27% | 0.60x |
| 9 | XRP/USD | 66.067 | 0.95228 | +0.09% | 1.65x |
| 10 | WIF/USD | 63.198 | 0.1338 | +0.00% | 1.13x |
| 11 | XDG/USD | 61.030 | 0.0567902 | +0.19% | 3.94x |
| 12 | HBAR/USD | 60.892 | 0.05402 | +0.60% | 1.63x |

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

- Persisted scans: 1857; predictions: 16019; observations: 1125597.
- Matured sampled outcomes across 1/6/24/48h: 34658; gap abstentions: 24684. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45814030505 · **Generation:** 1857 · **Legacy run:** 45814030505
**Main quote time:** 2026-11-26T11:50:59.131474+00:00 · **Legacy report time:** 2026-11-26T11:51:57.615182+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03696 | 88.71 | +0.71% | 2.29x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | XDG/USD | 0.0567902 | 76.99 | +0.19% | 3.94x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD | 0.04499 | 76.58 | +0.56% | 0.60x | MODERATE 68/100 | VERY_HIGH 75/100 | Watch |
| 4 | XRP/USD ⭐ | 0.95228 | 73.00 | +0.09% | 1.65x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | HBAR/USD ⭐ | 0.05402 | 70.13 | +0.60% | 1.63x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 6 | FET/USD | 0.1153 | 68.91 | +0.09% | 0.98x | MODERATE 49/100 | VERY_HIGH 73/100 | Watch |
| 7 | LTC/USD | 43.55 | 67.62 | +0.28% | 0.86x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 8 | INJ/USD | 6.179 | 65.90 | -0.10% | 0.90x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | SYRUP/USD | 0.07134 | 65.42 | -0.52% | 1.05x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |
| 10 | LINK/USD | 9.24058 | 64.98 | +0.12% | 0.49x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.148479 | 64.68 | +0.27% | 0.60x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 12 | WIF/USD | 0.1338 | 64.53 | +0.00% | 1.13x | MODERATE 57/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05399 | 81.58 | +0.60% | 1.63x | 6137 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | SEI/USD ⭐ | 0.03701 | 78.89 | +0.71% | 2.29x | 2773 | STRONG 99/100 | HIGH 66/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95192 | 74.34 | +0.09% | 1.65x | 38398 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SEI/USD, XRP/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
