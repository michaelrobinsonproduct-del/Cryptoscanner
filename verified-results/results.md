# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T15:10:59.204331+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45846240944
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 084a8644d157835eb4bc4a7596cafa939f8d6cd6 (atomic ledger/results publication)
**Ledger generation:** 1877 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STBL/USD | 0.020312 | 87.766 | 68.725 | +7.55% | +0.81% | 46.65x | 14.3 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | STRONG 94/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04553 | 76.885 | 71.804 | +8.72% | -0.83% | 1.92x | 15.4 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | VELO/USD | 0.002455 | 73.604 | 71.887 | +8.10% | -2.66% | 2.89x | 8.2 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 4 | LTC/USD | 43.01 | 67.553 | 58.755 | +0.70% | -1.24% | 4.56x | 2.3 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 64/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | SEI/USD | 0.03673 | 67.464 | 73.362 | +10.27% | -1.16% | 0.99x | 10.9 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 6 | LINK/USD | 9.08138 | 64.279 | 55.019 | +0.41% | -1.15% | 10.93x | 5.7 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Watch | WATCH |
| 7 | ADA/USD | 0.146532 | 63.504 | 56.305 | +0.52% | -1.56% | 5.61x | 4.7 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Do nothing | WATCH |
| 8 | ZRO/USD | 1.061 | 63.016 | 59.515 | +3.61% | -2.30% | 6.01x | 9.4 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Do nothing | WATCH |
| 9 | DCR/USD | 10.602 | 51.645 | 37.351 | +1.07% | -0.14% | 3.18x | 1.9 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | QNT/USD | 146.41 | 50.946 | 48.405 | +1.11% | -1.75% | 2.13x | 6.8 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 55/100 | HIGH 65/100 | Do nothing | WATCH |
| 11 | HBAR/USD | 0.05311 | 42.737 | 46.148 | +1.94% | -1.45% | 1.38x | 7.5 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 12 | ALGO/USD | 0.07841 | 42.072 | 35.813 | +0.41% | -1.75% | 8.45x | 6.4 | 2026-11-26T15:10:52.461387+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 73.362 | 0.03673 | -1.16% | 0.99x |
| 2 | VELO/USD | 71.887 | 0.002455 | -2.66% | 2.89x |
| 3 | SKY/USD | 71.804 | 0.04553 | -0.83% | 1.92x |
| 4 | STBL/USD | 68.725 | 0.020312 | +0.81% | 46.65x |
| 5 | ZRO/USD | 59.515 | 1.061 | -2.30% | 6.01x |
| 6 | LTC/USD | 58.755 | 43.01 | -1.24% | 4.56x |
| 7 | ADA/USD | 56.305 | 0.146532 | -1.56% | 5.61x |
| 8 | LINK/USD | 55.019 | 9.08138 | -1.15% | 10.93x |
| 9 | QNT/USD | 48.405 | 146.41 | -1.75% | 2.13x |
| 10 | HBAR/USD | 46.148 | 0.05311 | -1.45% | 1.38x |
| 11 | DCR/USD | 37.351 | 10.602 | -0.14% | 3.18x |
| 12 | ALGO/USD | 35.813 | 0.07841 | -1.75% | 8.45x |

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

- Persisted scans: 1877; predictions: 16259; observations: 1137373.
- Matured sampled outcomes across 1/6/24/48h: 35150; gap abstentions: 24969. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45846240944 · **Generation:** 1877 · **Legacy run:** 45846240944
**Main quote time:** 2026-11-26T15:10:59.204331+00:00 · **Legacy report time:** 2026-11-26T15:11:49.959952+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STBL/USD ⭐ | 0.020312 | 87.77 | +0.81% | 46.65x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | SKY/USD | 0.04553 | 76.88 | -0.83% | 1.92x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 3 | VELO/USD | 0.002455 | 73.60 | -2.66% | 2.89x | MODERATE 67/100 | VERY_HIGH 77/100 | Do nothing |
| 4 | LTC/USD | 43.01 | 67.55 | -1.24% | 4.56x | MODERATE 64/100 | HIGH 65/100 | Do nothing |
| 5 | SEI/USD | 0.03673 | 67.46 | -1.16% | 0.99x | WEAK 34/100 | VERY_HIGH 83/100 | Do nothing |
| 6 | LINK/USD | 9.08138 | 64.28 | -1.15% | 10.93x | MODERATE 62/100 | HIGH 65/100 | Watch |
| 7 | ADA/USD | 0.146532 | 63.50 | -1.56% | 5.61x | MODERATE 62/100 | HIGH 65/100 | Do nothing |
| 8 | ZRO/USD | 1.061 | 63.02 | -2.30% | 6.01x | MODERATE 62/100 | HIGH 65/100 | Do nothing |
| 9 | DCR/USD | 10.602 | 51.64 | -0.14% | 3.18x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 10 | QNT/USD | 146.41 | 50.95 | -1.75% | 2.13x | MODERATE 55/100 | HIGH 65/100 | Do nothing |
| 11 | HBAR/USD | 0.05311 | 42.74 | -1.45% | 1.38x | WEAK 41/100 | VERY_HIGH 70/100 | Do nothing |
| 12 | ALGO/USD | 0.07841 | 42.07 | -1.75% | 8.45x | MODERATE 51/100 | VERY_HIGH 70/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STBL/USD ⭐ | 0.02035 | 69.38 | +0.81% | 46.65x | 1252 | STRONG 90/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** STBL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
