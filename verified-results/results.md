# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T11:41:08.891930+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45812564667
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** eb5dc0382962fc4592ea28223e45ce0752e24aa4 (atomic ledger/results publication)
**Ledger generation:** 1856 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 587; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04474 | 83.808 | 75.479 | +6.83% | +0.58% | 1.54x | 6.7 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | FET/USD | 0.1151 | 82.846 | 67.411 | +6.08% | +0.09% | 11.36x | 17.4 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SEI/USD | 0.03645 | 81.254 | 73.536 | +9.43% | +0.33% | 1.61x | 8.2 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | ZRO/USD | 1.09 | 76.904 | 76.019 | +6.45% | +0.46% | 0.86x | 18.4 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | MODERATE 63/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95226 | 67.927 | 66.682 | +1.68% | -0.05% | 1.15x | 0.1 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 6 | LTC/USD | 43.5 | 67.594 | 66.798 | +1.85% | -0.11% | 1.14x | 2.3 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0567411 | 66.738 | 60.533 | +1.40% | -0.04% | 1.64x | 0.0 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | INJ/USD | 6.189 | 65.373 | 68.815 | +3.95% | +0.08% | 0.62x | 4.8 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 9.225 | 64.668 | 67.760 | +2.00% | -0.02% | 0.70x | 2.4 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SYRUP/USD | 0.07148 | 62.696 | 62.590 | +7.86% | -0.13% | 1.07x | 29.4 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | WEAK 31/100 | EXTREME 85/100 | Do nothing | WATCH |
| 11 | ADA/USD | 0.147974 | 59.183 | 63.996 | +1.51% | -0.34% | 0.69x | 3.2 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.0539 | 58.586 | 60.219 | +3.45% | +0.52% | 0.58x | 1.9 | 2026-11-26T11:41:02.926061+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 76.019 | 1.09 | +0.46% | 0.86x |
| 2 | SKY/USD | 75.479 | 0.04474 | +0.58% | 1.54x |
| 3 | SEI/USD | 73.536 | 0.03645 | +0.33% | 1.61x |
| 4 | INJ/USD | 68.815 | 6.189 | +0.08% | 0.62x |
| 5 | LINK/USD | 67.760 | 9.225 | -0.02% | 0.70x |
| 6 | FET/USD | 67.411 | 0.1151 | +0.09% | 11.36x |
| 7 | LTC/USD | 66.798 | 43.5 | -0.11% | 1.14x |
| 8 | XRP/USD | 66.682 | 0.95226 | -0.05% | 1.15x |
| 9 | ADA/USD | 63.996 | 0.147974 | -0.34% | 0.69x |
| 10 | SYRUP/USD | 62.590 | 0.07148 | -0.13% | 1.07x |
| 11 | XDG/USD | 60.533 | 0.0567411 | -0.04% | 1.64x |
| 12 | HBAR/USD | 60.219 | 0.0539 | +0.52% | 0.58x |

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

- Persisted scans: 1856; predictions: 16007; observations: 1125009.
- Matured sampled outcomes across 1/6/24/48h: 34646; gap abstentions: 24668. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45812564667 · **Generation:** 1856 · **Legacy run:** 45812564667
**Main quote time:** 2026-11-26T11:41:08.891930+00:00 · **Legacy report time:** 2026-11-26T11:42:26.852618+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04474 | 83.81 | +0.58% | 1.54x | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1151 | 82.85 | +0.09% | 11.36x | STRONG 91/100 | HIGH 66/100 | Watch |
| 3 | SEI/USD ⭐ | 0.03645 | 81.25 | +0.33% | 1.61x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 4 | ZRO/USD | 1.09 | 76.90 | +0.46% | 0.86x | MODERATE 63/100 | HIGH 68/100 | Watch |
| 5 | XRP/USD | 0.95226 | 67.93 | -0.05% | 1.15x | WEAK 44/100 | HIGH 68/100 | Watch |
| 6 | LTC/USD | 43.5 | 67.59 | -0.11% | 1.14x | WEAK 44/100 | HIGH 68/100 | Watch |
| 7 | XDG/USD | 0.0567411 | 66.74 | -0.04% | 1.64x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | INJ/USD | 6.189 | 65.37 | +0.08% | 0.62x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 9.225 | 64.67 | -0.02% | 0.70x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | SYRUP/USD | 0.07148 | 62.70 | -0.13% | 1.07x | WEAK 31/100 | EXTREME 85/100 | Do nothing |
| 11 | ADA/USD | 0.147974 | 59.18 | -0.34% | 0.69x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | HBAR/USD | 0.0539 | 58.59 | +0.52% | 0.58x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04484 | 77.84 | +0.58% | 1.54x | 4241 | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1153 | 77.50 | +0.09% | 11.36x | 2298 | STRONG 89/100 | HIGH 66/100 | Watch |
| 3 | SEI/USD ⭐ | 0.03666 | 75.01 | +0.33% | 1.61x | 2741 | STRONG 93/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD, FET/USD, SEI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
