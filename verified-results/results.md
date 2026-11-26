# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T21:03:28.217706+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45894957149
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7d28e45c248a2fe3d6abf755ae99872f81fb68e6 (atomic ledger/results publication)
**Ledger generation:** 1913 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38826 | 92.669 | 78.895 | +8.51% | +0.58% | 2.09x | 6.7 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HBAR/USD | 0.05517 | 88.379 | 74.404 | +5.89% | -0.09% | 2.44x | 3.6 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 3 | ADA/USD | 0.150865 | 86.850 | 77.611 | +3.50% | -0.18% | 2.02x | 3.7 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5087 | 79.779 | 76.909 | +7.52% | +0.38% | 1.10x | 2.0 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 5 | LTC/USD | 43.98 | 79.728 | 73.540 | +2.97% | +0.18% | 1.53x | 4.5 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.16 | 68.917 | 70.911 | +2.50% | +0.24% | 0.68x | 3.2 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XBT/USD | 60731.4 | 66.634 | 59.199 | +0.60% | -0.06% | 1.77x | 0.0 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95179 | 63.285 | 66.173 | +1.63% | +0.07% | 0.68x | 0.4 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TREAD/USD | 1.1274 | 60.729 | 64.133 | +4.71% | +1.11% | 0.11x | 0.9 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | ETH/USD | 1703.26 | 59.610 | 60.116 | +0.76% | -0.03% | 0.96x | 0.4 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0568861 | 54.578 | 55.997 | +1.66% | -0.11% | 0.91x | 0.0 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | BNB/USD | 555.16 | 41.468 | 37.421 | +0.39% | -0.14% | 1.48x | 0.9 | 2026-11-26T21:03:19.677764+00:00 | Not calibrated | WEAK 41/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 78.895 | 0.38826 | +0.58% | 2.09x |
| 2 | ADA/USD | 77.611 | 0.150865 | -0.18% | 2.02x |
| 3 | AKT/USD | 76.909 | 0.5087 | +0.38% | 1.10x |
| 4 | HBAR/USD | 74.404 | 0.05517 | -0.09% | 2.44x |
| 5 | LTC/USD | 73.540 | 43.98 | +0.18% | 1.53x |
| 6 | HYPE/USD | 70.911 | 63.16 | +0.24% | 0.68x |
| 7 | XRP/USD | 66.173 | 0.95179 | +0.07% | 0.68x |
| 8 | TREAD/USD | 64.133 | 1.1274 | +1.11% | 0.11x |
| 9 | ETH/USD | 60.116 | 1703.26 | -0.03% | 0.96x |
| 10 | XBT/USD | 59.199 | 60731.4 | -0.06% | 1.77x |
| 11 | XDG/USD | 55.997 | 0.0568861 | -0.11% | 0.91x |
| 12 | BNB/USD | 37.421 | 555.16 | -0.14% | 1.48x |

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

- Persisted scans: 1913; predictions: 16691; observations: 1158821.
- Matured sampled outcomes across 1/6/24/48h: 36272; gap abstentions: 25260. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45894957149 · **Generation:** 1913 · **Legacy run:** 45894957149
**Main quote time:** 2026-11-26T21:03:28.217706+00:00 · **Legacy report time:** 2026-11-26T21:04:20.532649+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.38826 | 92.67 | +0.58% | 2.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HBAR/USD | 0.05517 | 88.38 | -0.09% | 2.44x | STRONG 74/100 | HIGH 66/100 | Watch |
| 3 | ADA/USD | 0.150865 | 86.85 | -0.18% | 2.02x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5087 | 79.78 | +0.38% | 1.10x | STRONG 85/100 | HIGH 67/100 | Watch |
| 5 | LTC/USD ⭐ | 43.98 | 79.73 | +0.18% | 1.53x | STRONG 85/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 63.16 | 68.92 | +0.24% | 0.68x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 7 | XBT/USD | 60731.4 | 66.63 | -0.06% | 1.77x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.95179 | 63.28 | +0.07% | 0.68x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | TREAD/USD | 1.1274 | 60.73 | +1.11% | 0.11x | MODERATE 60/100 | VERY_HIGH 82/100 | Watch |
| 10 | ETH/USD | 1703.26 | 59.61 | -0.03% | 0.96x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | XDG/USD | 0.0568861 | 54.58 | -0.11% | 0.91x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 12 | BNB/USD | 555.16 | 41.47 | -0.14% | 1.48x | WEAK 41/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 43.98 | 85.79 | +0.18% | 1.53x | 14362 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD | 9.3157 | 84.04 | +0.22% | 1.78x | 6379 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 3 | DRV/USD ⭐ | 0.38826 | 81.51 | +0.58% | 2.09x | 7669 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | AKT/USD ⭐ | 0.5085 | 73.26 | +0.38% | 1.10x | 2651 | STRONG 82/100 | HIGH 67/100 | Watch |

**Same-run overlap:** DRV/USD, AKT/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
