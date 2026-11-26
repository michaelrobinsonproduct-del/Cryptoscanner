# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T20:27:03.295050+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45890958990
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 33d8b0c40acac072da0e22a7ab5c1e011e4dd061 (atomic ledger/results publication)
**Ledger generation:** 1909 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04605 | 92.718 | 78.571 | +9.96% | +0.66% | 2.09x | 2.2 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | ALGO/USD | 0.08114 | 78.390 | 61.162 | +3.91% | +0.45% | 8.48x | 1.2 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | STRONG 94/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.95068 | 77.487 | 65.501 | +1.51% | -0.05% | 2.22x | 0.1 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | W/USD | 0.00882 | 74.572 | 70.324 | +6.27% | +0.11% | 1.37x | 11.4 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | MODERATE 67/100 | HIGH 66/100 | Watch | WATCH |
| 5 | ZRO/USD | 1.101 | 72.868 | 71.239 | +7.52% | -0.09% | 1.21x | 18.2 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | WIF/USD | 0.1383 | 71.131 | 73.239 | +8.64% | -0.65% | 1.11x | 7.2 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0568748 | 69.503 | 56.321 | +1.64% | -0.23% | 2.43x | 0.1 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.150239 | 69.502 | 74.564 | +3.07% | -0.09% | 0.54x | 3.8 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | DRV/USD | 0.38623 | 68.749 | 76.909 | +7.95% | -0.14% | 0.26x | 11.1 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | AKT/USD | 0.5088 | 68.068 | 76.949 | +7.55% | +0.00% | 0.11x | 2.0 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | FET/USD | 0.1192 | 61.575 | 70.325 | +9.86% | -0.91% | 0.58x | 16.8 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | ETH/USD | 1700.59 | 60.123 | 59.186 | +0.60% | -0.07% | 1.13x | 0.1 | 2026-11-26T20:26:57.426107+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 78.571 | 0.04605 | +0.66% | 2.09x |
| 2 | AKT/USD | 76.949 | 0.5088 | +0.00% | 0.11x |
| 3 | DRV/USD | 76.909 | 0.38623 | -0.14% | 0.26x |
| 4 | ADA/USD | 74.564 | 0.150239 | -0.09% | 0.54x |
| 5 | WIF/USD | 73.239 | 0.1383 | -0.65% | 1.11x |
| 6 | ZRO/USD | 71.239 | 1.101 | -0.09% | 1.21x |
| 7 | FET/USD | 70.325 | 0.1192 | -0.91% | 0.58x |
| 8 | W/USD | 70.324 | 0.00882 | +0.11% | 1.37x |
| 9 | XRP/USD | 65.501 | 0.95068 | -0.05% | 2.22x |
| 10 | ALGO/USD | 61.162 | 0.08114 | +0.45% | 8.48x |
| 11 | ETH/USD | 59.186 | 1700.59 | -0.07% | 1.13x |
| 12 | XDG/USD | 56.321 | 0.0568748 | -0.23% | 2.43x |

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

- Persisted scans: 1909; predictions: 16643; observations: 1156425.
- Matured sampled outcomes across 1/6/24/48h: 36140; gap abstentions: 25232. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45890958990 · **Generation:** 1909 · **Legacy run:** 45890958990
**Main quote time:** 2026-11-26T20:27:03.295050+00:00 · **Legacy report time:** 2026-11-26T20:27:40.013964+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04605 | 92.72 | +0.66% | 2.09x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.08114 | 78.39 | +0.45% | 8.48x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | XRP/USD | 0.95068 | 77.49 | -0.05% | 2.22x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | W/USD | 0.00882 | 74.57 | +0.11% | 1.37x | MODERATE 67/100 | HIGH 66/100 | Watch |
| 5 | ZRO/USD | 1.101 | 72.87 | -0.09% | 1.21x | WEAK 41/100 | VERY_HIGH 79/100 | Watch |
| 6 | WIF/USD | 0.1383 | 71.13 | -0.65% | 1.11x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 7 | XDG/USD | 0.0568748 | 69.50 | -0.23% | 2.43x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD | 0.150239 | 69.50 | -0.09% | 0.54x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | DRV/USD | 0.38623 | 68.75 | -0.14% | 0.26x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | AKT/USD | 0.5088 | 68.07 | +0.00% | 0.11x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 11 | FET/USD | 0.1192 | 61.58 | -0.91% | 0.58x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 12 | ETH/USD | 1700.59 | 60.12 | -0.07% | 1.13x | WEAK 40/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04599 | 85.41 | +0.66% | 2.09x | 6537 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.08108 | 85.08 | +0.45% | 8.48x | 3586 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD, ALGO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
