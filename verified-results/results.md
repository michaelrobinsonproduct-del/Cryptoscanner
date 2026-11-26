# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T18:21:06.090057+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45875003250
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dd386d4b04426f37403d257ac04c61601be17290 (atomic ledger/results publication)
**Ledger generation:** 1896 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38343 | 97.505 | 79.871 | +7.16% | +0.53% | 4.15x | 2.6 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.95251 | 81.054 | 66.816 | +1.70% | +0.11% | 2.37x | 0.2 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | WIF/USD | 0.1388 | 79.016 | 69.377 | +9.03% | -0.65% | 2.29x | 14.4 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | FET/USD | 0.118 | 74.389 | 69.918 | +8.76% | +1.11% | 0.89x | 17.0 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | ADA/USD | 0.14949 | 72.995 | 71.459 | +2.55% | +0.18% | 1.06x | 2.8 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0568287 | 71.808 | 56.991 | +1.55% | -0.04% | 8.17x | 0.0 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 7 | STBL/USD | 0.020195 | 68.519 | 68.317 | +6.93% | -0.04% | 1.04x | 15.4 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | SKY/USD | 0.04565 | 67.980 | 76.527 | +9.00% | +0.11% | 0.09x | 6.6 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.05436 | 62.870 | 64.842 | +4.34% | +0.42% | 0.59x | 1.8 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | 2Z/USD | 0.01738 | 59.860 | 65.279 | +5.21% | -0.40% | 0.66x | 5.8 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | LINK/USD | 9.22551 | 59.572 | 66.877 | +2.00% | +0.01% | 0.27x | 4.3 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.502e-06 | 58.928 | 42.927 | +0.52% | +0.20% | 3.75x | 2.9 | 2026-11-26T18:20:58.481862+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 79.871 | 0.38343 | +0.53% | 4.15x |
| 2 | SKY/USD | 76.527 | 0.04565 | +0.11% | 0.09x |
| 3 | ADA/USD | 71.459 | 0.14949 | +0.18% | 1.06x |
| 4 | FET/USD | 69.918 | 0.118 | +1.11% | 0.89x |
| 5 | WIF/USD | 69.377 | 0.1388 | -0.65% | 2.29x |
| 6 | STBL/USD | 68.317 | 0.020195 | -0.04% | 1.04x |
| 7 | LINK/USD | 66.877 | 9.22551 | +0.01% | 0.27x |
| 8 | XRP/USD | 66.816 | 0.95251 | +0.11% | 2.37x |
| 9 | 2Z/USD | 65.279 | 0.01738 | -0.40% | 0.66x |
| 10 | HBAR/USD | 64.842 | 0.05436 | +0.42% | 0.59x |
| 11 | XDG/USD | 56.991 | 0.0568287 | -0.04% | 8.17x |
| 12 | PEPE/USD | 42.927 | 3.502e-06 | +0.20% | 3.75x |

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

- Persisted scans: 1896; predictions: 16487; observations: 1148657.
- Matured sampled outcomes across 1/6/24/48h: 35672; gap abstentions: 25132. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45875003250 · **Generation:** 1896 · **Legacy run:** 45875003250
**Main quote time:** 2026-11-26T18:21:06.090057+00:00 · **Legacy report time:** 2026-11-26T18:21:48.132962+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.38343 | 97.50 | +0.53% | 4.15x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95251 | 81.05 | +0.11% | 2.37x | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | WIF/USD | 0.1388 | 79.02 | -0.65% | 2.29x | MODERATE 65/100 | VERY_HIGH 79/100 | Watch |
| 4 | FET/USD | 0.118 | 74.39 | +1.11% | 0.89x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 5 | ADA/USD ⭐ | 0.14949 | 73.00 | +0.18% | 1.06x | STRONG 71/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD | 0.0568287 | 71.81 | -0.04% | 8.17x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 7 | STBL/USD | 0.020195 | 68.52 | -0.04% | 1.04x | WEAK 39/100 | EXTREME 86/100 | Do nothing |
| 8 | SKY/USD | 0.04565 | 67.98 | +0.11% | 0.09x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 9 | HBAR/USD | 0.05436 | 62.87 | +0.42% | 0.59x | MODERATE 61/100 | VERY_HIGH 75/100 | Watch |
| 10 | 2Z/USD | 0.01738 | 59.86 | -0.40% | 0.66x | WEAK 35/100 | VERY_HIGH 81/100 | Watch |
| 11 | LINK/USD | 9.22551 | 59.57 | +0.01% | 0.27x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | PEPE/USD | 3.502e-06 | 58.93 | +0.20% | 3.75x | STRONG 84/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.38421 | 83.29 | +0.53% | 4.15x | 7569 | STRONG 97/100 | VERY_HIGH 72/100 | Watch |
| 2 | ADA/USD ⭐ | 0.149597 | 79.62 | +0.18% | 1.06x | 10492 | STRONG 75/100 | HIGH 62/100 | Watch |
| 3 | XRP/USD ⭐ | 0.95258 | 78.12 | +0.11% | 2.37x | 30068 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, XRP/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
