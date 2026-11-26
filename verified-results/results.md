# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T20:20:51.195009+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45890211829
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 70fe78236977d33a7daa9b69885eeda0642ed68c (atomic ledger/results publication)
**Ledger generation:** 1908 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.106 | 81.564 | 76.201 | +8.01% | -0.18% | 1.63x | 9.0 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04617 | 80.922 | 77.481 | +10.24% | +0.98% | 0.85x | 4.3 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 3 | W/USD | 0.00882 | 73.715 | 70.344 | +6.27% | +0.00% | 1.34x | 11.4 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 67/100 | HIGH 66/100 | Watch | WATCH |
| 4 | XRP/USD | 0.95011 | 72.771 | 64.970 | +1.45% | -0.17% | 1.86x | 0.3 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 5 | DRV/USD | 0.38886 | 71.575 | 78.039 | +8.68% | +0.60% | 0.05x | 9.0 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5091 | 69.709 | 76.965 | +7.61% | +0.34% | 0.11x | 2.0 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1387 | 68.895 | 73.228 | +8.96% | -0.14% | 0.64x | 7.2 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | ADA/USD | 0.150432 | 67.122 | 74.828 | +3.20% | -0.01% | 0.23x | 5.1 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | LTC/USD | 43.66 | 65.420 | 69.425 | +2.22% | +0.18% | 0.51x | 2.3 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0569595 | 64.591 | 57.285 | +1.79% | -0.18% | 1.82x | 0.3 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ETH/USD | 1702.29 | 62.017 | 59.890 | +0.70% | -0.01% | 1.22x | 0.1 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 12 | SOL/USD | 71.28 | 59.644 | 63.149 | +1.26% | +0.10% | 0.60x | 1.4 | 2026-11-26T20:20:43.781115+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 78.039 | 0.38886 | +0.60% | 0.05x |
| 2 | SKY/USD | 77.481 | 0.04617 | +0.98% | 0.85x |
| 3 | AKT/USD | 76.965 | 0.5091 | +0.34% | 0.11x |
| 4 | ZRO/USD | 76.201 | 1.106 | -0.18% | 1.63x |
| 5 | ADA/USD | 74.828 | 0.150432 | -0.01% | 0.23x |
| 6 | WIF/USD | 73.228 | 0.1387 | -0.14% | 0.64x |
| 7 | W/USD | 70.344 | 0.00882 | +0.00% | 1.34x |
| 8 | LTC/USD | 69.425 | 43.66 | +0.18% | 0.51x |
| 9 | XRP/USD | 64.970 | 0.95011 | -0.17% | 1.86x |
| 10 | SOL/USD | 63.149 | 71.28 | +0.10% | 0.60x |
| 11 | ETH/USD | 59.890 | 1702.29 | -0.01% | 1.22x |
| 12 | XDG/USD | 57.285 | 0.0569595 | -0.18% | 1.82x |

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

- Persisted scans: 1908; predictions: 16631; observations: 1155826.
- Matured sampled outcomes across 1/6/24/48h: 36104; gap abstentions: 25223. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45890211829 · **Generation:** 1908 · **Legacy run:** 45890211829
**Main quote time:** 2026-11-26T20:20:51.195009+00:00 · **Legacy report time:** 2026-11-26T20:21:27.631898+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD | 1.106 | 81.56 | -0.18% | 1.63x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 2 | SKY/USD | 0.04617 | 80.92 | +0.98% | 0.85x | STRONG 70/100 | HIGH 67/100 | Watch |
| 3 | W/USD | 0.00882 | 73.72 | +0.00% | 1.34x | MODERATE 67/100 | HIGH 66/100 | Watch |
| 4 | XRP/USD | 0.95011 | 72.77 | -0.17% | 1.86x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 5 | DRV/USD | 0.38886 | 71.58 | +0.60% | 0.05x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 6 | AKT/USD | 0.5091 | 69.71 | +0.34% | 0.11x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 7 | WIF/USD | 0.1387 | 68.89 | -0.14% | 0.64x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 8 | ADA/USD | 0.150432 | 67.12 | -0.01% | 0.23x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | LTC/USD | 43.66 | 65.42 | +0.18% | 0.51x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | XDG/USD | 0.0569595 | 64.59 | -0.18% | 1.82x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 11 | ETH/USD | 1702.29 | 62.02 | -0.01% | 1.22x | WEAK 41/100 | HIGH 68/100 | Watch |
| 12 | SOL/USD | 71.28 | 59.64 | +0.10% | 0.60x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08126 | 94.84 | +0.54% | 8.48x | 3557 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
