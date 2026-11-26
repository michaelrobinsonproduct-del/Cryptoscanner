# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T14:41:03.584448+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45841231969
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 602826cdb0edf0252b0fb2c095ccb7294d61209e (atomic ledger/results publication)
**Ledger generation:** 1874 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 590; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | FET/USD | 0.1155 | 84.481 | 69.913 | +6.45% | -0.09% | 12.49x | 17.3 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | WIF/USD | 0.1348 | 82.288 | 68.767 | +5.89% | -0.30% | 2.51x | 7.4 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ADA/USD | 0.14924 | 81.004 | 68.480 | +2.38% | +0.11% | 2.20x | 6.4 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LINK/USD | 9.24003 | 79.628 | 66.041 | +2.16% | -0.28% | 5.85x | 5.2 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95144 | 75.385 | 65.911 | +1.59% | +0.02% | 1.94x | 0.4 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.01783 | 74.316 | 73.437 | +7.93% | +1.02% | 0.58x | 5.6 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | XBT/USD | 60707.4 | 73.397 | 58.920 | +0.56% | -0.10% | 3.97x | 0.0 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZRO/USD | 1.096 | 69.581 | 75.074 | +7.03% | -1.35% | 1.13x | 18.3 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 9 | LTC/USD | 43.79 | 65.340 | 71.559 | +2.53% | -0.25% | 0.50x | 2.3 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | INJ/USD | 6.162 | 64.217 | 65.446 | +3.49% | -0.13% | 0.94x | 3.2 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0570401 | 63.344 | 60.535 | +1.93% | +0.04% | 1.26x | 0.4 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | MODERATE 57/100 | HIGH 55/100 | Watch | WATCH |
| 12 | SOL/USD | 71.25 | 61.763 | 62.850 | +1.22% | -0.15% | 0.97x | 1.4 | 2026-11-26T14:40:54.822238+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 75.074 | 1.096 | -1.35% | 1.13x |
| 2 | 2Z/USD | 73.437 | 0.01783 | +1.02% | 0.58x |
| 3 | LTC/USD | 71.559 | 43.79 | -0.25% | 0.50x |
| 4 | FET/USD | 69.913 | 0.1155 | -0.09% | 12.49x |
| 5 | WIF/USD | 68.767 | 0.1348 | -0.30% | 2.51x |
| 6 | ADA/USD | 68.480 | 0.14924 | +0.11% | 2.20x |
| 7 | LINK/USD | 66.041 | 9.24003 | -0.28% | 5.85x |
| 8 | XRP/USD | 65.911 | 0.95144 | +0.02% | 1.94x |
| 9 | INJ/USD | 65.446 | 6.162 | -0.13% | 0.94x |
| 10 | SOL/USD | 62.850 | 71.25 | -0.15% | 0.97x |
| 11 | XDG/USD | 60.535 | 0.0570401 | +0.04% | 1.26x |
| 12 | XBT/USD | 58.920 | 60707.4 | -0.10% | 3.97x |

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

- Persisted scans: 1874; predictions: 16223; observations: 1135600.
- Matured sampled outcomes across 1/6/24/48h: 35078; gap abstentions: 24929. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45841231969 · **Generation:** 1874 · **Legacy run:** 45841231969
**Main quote time:** 2026-11-26T14:41:03.584448+00:00 · **Legacy report time:** 2026-11-26T14:41:59.957068+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD | 0.1155 | 84.48 | -0.09% | 12.49x | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 2 | WIF/USD | 0.1348 | 82.29 | -0.30% | 2.51x | STRONG 71/100 | VERY_HIGH 73/100 | Watch |
| 3 | ADA/USD ⭐ | 0.14924 | 81.00 | +0.11% | 2.20x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD | 9.24003 | 79.63 | -0.28% | 5.85x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD | 0.95144 | 75.39 | +0.02% | 1.94x | STRONG 73/100 | HIGH 55/100 | Watch |
| 6 | 2Z/USD | 0.01783 | 74.32 | +1.02% | 0.58x | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |
| 7 | XBT/USD | 60707.4 | 73.40 | -0.10% | 3.97x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 8 | ZRO/USD | 1.096 | 69.58 | -1.35% | 1.13x | WEAK 40/100 | VERY_HIGH 78/100 | Do nothing |
| 9 | LTC/USD | 43.79 | 65.34 | -0.25% | 0.50x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | INJ/USD | 6.162 | 64.22 | -0.13% | 0.94x | WEAK 37/100 | HIGH 68/100 | Watch |
| 11 | XDG/USD | 0.0570401 | 63.34 | +0.04% | 1.26x | MODERATE 57/100 | HIGH 55/100 | Watch |
| 12 | SOL/USD | 71.25 | 61.76 | -0.15% | 0.97x | WEAK 36/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD | 0.05415 | 88.42 | +0.41% | 2.62x | 5574 | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 2 | PIEVERSE/USD | 4.0541 | 85.81 | +0.35% | 3.23x | 3570 | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.149059 | 76.55 | +0.11% | 2.20x | 11726 | STRONG 93/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
