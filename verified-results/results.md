# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T21:21:07.689841+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45897339719
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c622374af0a461bf4a23daa8338231545cee8734 (atomic ledger/results publication)
**Ledger generation:** 1915 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38998 | 93.236 | 77.222 | +8.99% | +0.20% | 2.64x | 10.5 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 97/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.150947 | 92.968 | 77.507 | +3.55% | +0.09% | 4.88x | 4.7 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 44.06 | 91.334 | 74.856 | +3.16% | +0.30% | 6.63x | 4.5 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | AKT/USD | 0.5074 | 90.936 | 76.919 | +7.25% | -0.20% | 2.72x | 2.0 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 5 | LINK/USD | 9.34994 | 90.058 | 73.231 | +3.38% | +0.37% | 14.12x | 4.0 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | HBAR/USD | 0.05505 | 88.392 | 73.754 | +5.66% | -0.07% | 2.81x | 1.8 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1369 | 76.149 | 73.216 | +7.54% | +0.07% | 1.26x | 7.3 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | MODERATE 63/100 | HIGH 60/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6746 | 72.644 | 60.595 | +1.25% | +0.03% | 2.19x | 1.5 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1703.63 | 71.930 | 60.445 | +0.78% | +0.03% | 2.13x | 0.1 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 10 | INJ/USD | 6.291 | 71.391 | 76.910 | +5.66% | -0.02% | 0.46x | 4.8 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0569205 | 68.959 | 54.901 | +1.72% | +0.09% | 2.36x | 0.2 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XRP/USD | 0.95229 | 65.739 | 66.652 | +1.68% | -0.06% | 0.94x | 0.2 | 2026-11-26T21:21:01.471885+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ADA/USD | 77.507 | 0.150947 | +0.09% | 4.88x |
| 2 | DRV/USD | 77.222 | 0.38998 | +0.20% | 2.64x |
| 3 | AKT/USD | 76.919 | 0.5074 | -0.20% | 2.72x |
| 4 | INJ/USD | 76.910 | 6.291 | -0.02% | 0.46x |
| 5 | LTC/USD | 74.856 | 44.06 | +0.30% | 6.63x |
| 6 | HBAR/USD | 73.754 | 0.05505 | -0.07% | 2.81x |
| 7 | LINK/USD | 73.231 | 9.34994 | +0.37% | 14.12x |
| 8 | WIF/USD | 73.216 | 0.1369 | +0.07% | 1.26x |
| 9 | XRP/USD | 66.652 | 0.95229 | -0.06% | 0.94x |
| 10 | SUI/USD | 60.595 | 0.6746 | +0.03% | 2.19x |
| 11 | ETH/USD | 60.445 | 1703.63 | +0.03% | 2.13x |
| 12 | XDG/USD | 54.901 | 0.0569205 | +0.09% | 2.36x |

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

- Persisted scans: 1915; predictions: 16715; observations: 1160019.
- Matured sampled outcomes across 1/6/24/48h: 36344; gap abstentions: 25267. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45897339719 · **Generation:** 1915 · **Legacy run:** 45897339719
**Main quote time:** 2026-11-26T21:21:07.689841+00:00 · **Legacy report time:** 2026-11-26T21:21:57.385105+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.38998 | 93.24 | +0.20% | 2.64x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.150947 | 92.97 | +0.09% | 4.88x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD ⭐ | 44.06 | 91.33 | +0.30% | 6.63x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | AKT/USD | 0.5074 | 90.94 | -0.20% | 2.72x | STRONG 75/100 | HIGH 66/100 | Watch |
| 5 | LINK/USD ⭐ | 9.34994 | 90.06 | +0.37% | 14.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | HBAR/USD | 0.05505 | 88.39 | -0.07% | 2.81x | STRONG 74/100 | HIGH 66/100 | Watch |
| 7 | WIF/USD | 0.1369 | 76.15 | +0.07% | 1.26x | MODERATE 63/100 | HIGH 60/100 | Watch |
| 8 | SUI/USD | 0.6746 | 72.64 | +0.03% | 2.19x | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD | 1703.63 | 71.93 | +0.03% | 2.13x | STRONG 81/100 | HIGH 55/100 | Watch |
| 10 | INJ/USD | 6.291 | 71.39 | -0.02% | 0.46x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0569205 | 68.96 | +0.09% | 2.36x | STRONG 79/100 | HIGH 55/100 | Watch |
| 12 | XRP/USD | 0.95229 | 65.74 | -0.06% | 0.94x | WEAK 38/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.34994 | 94.02 | +0.37% | 14.12x | 6493 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 44.03 | 93.43 | +0.30% | 6.63x | 14425 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.150919 | 93.38 | +0.09% | 4.88x | 10384 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | DRV/USD ⭐ | 0.38998 | 81.66 | +0.20% | 2.64x | 8094 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** DRV/USD, ADA/USD, LTC/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
