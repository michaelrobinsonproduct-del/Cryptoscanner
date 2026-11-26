# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T16:31:11.616413+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45859256581
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 222aa6d1e8954ef4f5fac2ab5c6625b43c311162 (atomic ledger/results publication)
**Ledger generation:** 1885 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04614 | 83.296 | 76.371 | +10.17% | +0.09% | 1.65x | 6.5 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 3.965 | 75.387 | 74.994 | +11.98% | +0.58% | 0.75x | 21.0 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | STBL/USD | 0.020399 | 73.873 | 67.900 | +8.01% | -0.03% | 1.61x | 16.2 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01778 | 68.787 | 68.178 | +7.63% | +0.97% | 0.58x | 16.9 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 59/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | WIF/USD | 0.1345 | 67.597 | 67.222 | +5.66% | -1.10% | 1.59x | 7.4 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 6 | LTC/USD | 43.46 | 63.371 | 66.141 | +1.76% | +0.05% | 0.70x | 2.3 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 70.66 | 61.491 | 56.977 | +0.38% | -0.28% | 1.59x | 1.4 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | HBAR/USD | 0.05355 | 59.523 | 53.699 | +2.78% | -0.26% | 1.71x | 3.7 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 50/100 | HIGH 66/100 | Watch | WATCH |
| 9 | INJ/USD | 6.143 | 54.396 | 62.268 | +3.17% | -0.69% | 0.56x | 3.3 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | DOT/USD | 0.6666 | 54.346 | 41.120 | +1.26% | -0.10% | 2.38x | 1.5 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0564432 | 53.980 | 51.900 | +0.87% | -0.37% | 1.39x | 0.0 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XRP/USD | 0.94734 | 53.440 | 62.740 | +1.15% | -0.21% | 0.18x | 0.6 | 2026-11-26T16:31:04.056366+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 76.371 | 0.04614 | +0.09% | 1.65x |
| 2 | PIEVERSE/USD | 74.994 | 3.965 | +0.58% | 0.75x |
| 3 | 2Z/USD | 68.178 | 0.01778 | +0.97% | 0.58x |
| 4 | STBL/USD | 67.900 | 0.020399 | -0.03% | 1.61x |
| 5 | WIF/USD | 67.222 | 0.1345 | -1.10% | 1.59x |
| 6 | LTC/USD | 66.141 | 43.46 | +0.05% | 0.70x |
| 7 | XRP/USD | 62.740 | 0.94734 | -0.21% | 0.18x |
| 8 | INJ/USD | 62.268 | 6.143 | -0.69% | 0.56x |
| 9 | SOL/USD | 56.977 | 70.66 | -0.28% | 1.59x |
| 10 | HBAR/USD | 53.699 | 0.05355 | -0.26% | 1.71x |
| 11 | XDG/USD | 51.900 | 0.0564432 | -0.37% | 1.39x |
| 12 | DOT/USD | 41.120 | 0.6666 | -0.10% | 2.38x |

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

- Persisted scans: 1885; predictions: 16355; observations: 1142111.
- Matured sampled outcomes across 1/6/24/48h: 35342; gap abstentions: 25069. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45859256581 · **Generation:** 1885 · **Legacy run:** 45859256581
**Main quote time:** 2026-11-26T16:31:11.616413+00:00 · **Legacy report time:** 2026-11-26T16:31:53.595572+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04614 | 83.30 | +0.09% | 1.65x | STRONG 87/100 | HIGH 60/100 | Watch |
| 2 | PIEVERSE/USD | 3.965 | 75.39 | +0.58% | 0.75x | MODERATE 58/100 | VERY_HIGH 82/100 | Watch |
| 3 | STBL/USD | 0.020399 | 73.87 | -0.03% | 1.61x | MODERATE 52/100 | VERY_HIGH 79/100 | Watch |
| 4 | 2Z/USD | 0.01778 | 68.79 | +0.97% | 0.58x | MODERATE 59/100 | EXTREME 88/100 | Do nothing |
| 5 | WIF/USD | 0.1345 | 67.60 | -1.10% | 1.59x | MODERATE 54/100 | VERY_HIGH 77/100 | Watch |
| 6 | LTC/USD | 43.46 | 63.37 | +0.05% | 0.70x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 70.66 | 61.49 | -0.28% | 1.59x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | HBAR/USD | 0.05355 | 59.52 | -0.26% | 1.71x | MODERATE 50/100 | HIGH 66/100 | Watch |
| 9 | INJ/USD | 6.143 | 54.40 | -0.69% | 0.56x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | DOT/USD | 0.6666 | 54.35 | -0.10% | 2.38x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 11 | XDG/USD | 0.0564432 | 53.98 | -0.37% | 1.39x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 12 | XRP/USD | 0.94734 | 53.44 | -0.21% | 0.18x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TREAD/USD | 1.2309 | 91.46 | +0.35% | 10.92x | 2631 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04609 | 75.63 | +0.09% | 1.65x | 6258 | STRONG 83/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
