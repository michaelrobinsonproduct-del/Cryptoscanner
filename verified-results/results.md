# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T23:52:36.105258+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46084609974
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 87da2b7f8b7b24eb7557df0b47be02ee08eb0a6f (atomic ledger/results publication)
**Ledger generation:** 2077 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 733.06 | 96.689 | 98.840 | +7.54% | +0.17% | 0.70x | 2.3 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | LTC/USD | 45.11 | 85.108 | 75.816 | +3.13% | +0.87% | 1.49x | 2.2 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SKY/USD | 0.05197 | 76.031 | 80.267 | +11.98% | +0.52% | 0.32x | 7.7 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94755 | 74.135 | 58.511 | +0.51% | +0.12% | 2.53x | 0.1 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05025 | 72.209 | 79.712 | +3.67% | -0.02% | 0.26x | 2.0 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8128 | 65.214 | 74.386 | +3.50% | -0.00% | 0.08x | 3.5 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0576142 | 61.856 | 70.098 | +2.20% | -0.02% | 0.19x | 0.6 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.33 | 57.146 | 66.698 | +1.78% | -0.03% | 0.06x | 1.6 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | LINK/USD | 9.35943 | 55.980 | 61.002 | +0.98% | +0.11% | 0.44x | 1.7 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | WIF/USD | 0.1429 | 55.913 | 63.408 | +5.07% | -0.14% | 0.32x | 7.0 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | WEAK 33/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | PAXG/USD | 3649.8 | 55.035 | 62.078 | +2.62% | -0.04% | 0.31x | 0.7 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SUI/USD | 0.6719 | 54.801 | 58.659 | +0.63% | +0.12% | 0.55x | 1.5 | 2026-11-27T23:52:29.218336+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.840 | 733.06 | +0.17% | 0.70x |
| 2 | SKY/USD | 80.267 | 0.05197 | +0.52% | 0.32x |
| 3 | NIGHT/USD | 79.712 | 0.05025 | -0.02% | 0.26x |
| 4 | LTC/USD | 75.816 | 45.11 | +0.87% | 1.49x |
| 5 | UNI/USD | 74.386 | 4.8128 | -0.00% | 0.08x |
| 6 | XDG/USD | 70.098 | 0.0576142 | -0.02% | 0.19x |
| 7 | HYPE/USD | 66.698 | 63.33 | -0.03% | 0.06x |
| 8 | WIF/USD | 63.408 | 0.1429 | -0.14% | 0.32x |
| 9 | PAXG/USD | 62.078 | 3649.8 | -0.04% | 0.31x |
| 10 | LINK/USD | 61.002 | 9.35943 | +0.11% | 0.44x |
| 11 | SUI/USD | 58.659 | 0.6719 | +0.12% | 0.55x |
| 12 | XRP/USD | 58.511 | 0.94755 | +0.12% | 2.53x |

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

- Persisted scans: 2077; predictions: 18626; observations: 1257710.
- Matured sampled outcomes across 1/6/24/48h: 42575; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46084609974 · **Generation:** 2077 · **Legacy run:** 46084609974
**Main quote time:** 2026-11-27T23:52:36.105258+00:00 · **Legacy report time:** 2026-11-27T23:53:21.309161+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 733.06 | 96.69 | +0.17% | 0.70x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 2 | LTC/USD ⭐ | 45.11 | 85.11 | +0.87% | 1.49x | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD | 0.05197 | 76.03 | +0.52% | 0.32x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 4 | XRP/USD | 0.94755 | 74.14 | +0.12% | 2.53x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.05025 | 72.21 | -0.02% | 0.26x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 6 | UNI/USD | 4.8128 | 65.21 | -0.00% | 0.08x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 7 | XDG/USD | 0.0576142 | 61.86 | -0.02% | 0.19x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | HYPE/USD | 63.33 | 57.15 | -0.03% | 0.06x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | LINK/USD | 9.35943 | 55.98 | +0.11% | 0.44x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 10 | WIF/USD | 0.1429 | 55.91 | -0.14% | 0.32x | WEAK 33/100 | EXTREME 88/100 | Do nothing |
| 11 | PAXG/USD | 3649.8 | 55.04 | -0.04% | 0.31x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SUI/USD | 0.6719 | 54.80 | +0.12% | 0.55x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 45.13 | 90.29 | +0.87% | 1.49x | 16073 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ENA/USD | 0.1038 | 73.14 | +0.10% | 2.07x | 2805 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
