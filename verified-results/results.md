# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T10:12:26.578236+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45979715766
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4d35e4fbb51ca1fd503e8bc7e783827b707a6982 (atomic ledger/results publication)
**Ledger generation:** 1993 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.8968 | 93.179 | 78.230 | +5.31% | -0.01% | 5.93x | 7.2 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 750.19 | 92.730 | 97.666 | +10.05% | -0.33% | 0.67x | 4.7 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.7 | 90.879 | 93.390 | +5.59% | -0.02% | 0.76x | 1.5 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ENA/USD | 0.1069 | 88.358 | 72.423 | +6.47% | +0.19% | 7.31x | 18.7 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.618e-06 | 87.113 | 70.590 | +4.03% | +0.30% | 3.73x | 2.8 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XBT/USD | 61611.4 | 77.645 | 67.875 | +1.84% | +0.08% | 1.94x | 0.0 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 73.43 | 77.486 | 78.889 | +3.51% | +0.11% | 0.81x | 1.4 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97786 | 74.545 | 79.996 | +3.72% | -0.00% | 0.46x | 2.1 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ETH/USD | 1726.98 | 70.991 | 71.272 | +2.33% | -0.04% | 0.99x | 0.1 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6881 | 70.369 | 75.660 | +3.06% | -0.19% | 0.57x | 1.5 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | LINK/USD | 9.5597 | 69.509 | 75.528 | +3.14% | -0.15% | 0.47x | 2.9 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | LTC/USD | 44.44 | 68.851 | 64.310 | +1.60% | +0.25% | 1.33x | 2.3 | 2026-11-27T10:12:18.418820+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.666 | 750.19 | -0.33% | 0.67x |
| 2 | HYPE/USD | 93.390 | 65.7 | -0.02% | 0.76x |
| 3 | XRP/USD | 79.996 | 0.97786 | -0.00% | 0.46x |
| 4 | SOL/USD | 78.889 | 73.43 | +0.11% | 0.81x |
| 5 | UNI/USD | 78.230 | 4.8968 | -0.01% | 5.93x |
| 6 | SUI/USD | 75.660 | 0.6881 | -0.19% | 0.57x |
| 7 | LINK/USD | 75.528 | 9.5597 | -0.15% | 0.47x |
| 8 | ENA/USD | 72.423 | 0.1069 | +0.19% | 7.31x |
| 9 | ETH/USD | 71.272 | 1726.98 | -0.04% | 0.99x |
| 10 | PEPE/USD | 70.590 | 3.618e-06 | +0.30% | 3.73x |
| 11 | XBT/USD | 67.875 | 61611.4 | +0.08% | 1.94x |
| 12 | LTC/USD | 64.310 | 44.44 | +0.25% | 1.33x |

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

- Persisted scans: 1993; predictions: 17618; observations: 1206931.
- Matured sampled outcomes across 1/6/24/48h: 39101; gap abstentions: 25769. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45979715766 · **Generation:** 1993 · **Legacy run:** 45979715766
**Main quote time:** 2026-11-27T10:12:26.578236+00:00 · **Legacy report time:** 2026-11-27T10:13:22.157338+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.8968 | 93.18 | -0.01% | 5.93x | STRONG 77/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 750.19 | 92.73 | -0.33% | 0.67x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD | 65.7 | 90.88 | -0.02% | 0.76x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 4 | ENA/USD | 0.1069 | 88.36 | +0.19% | 7.31x | STRONG 84/100 | HIGH 61/100 | Watch |
| 5 | PEPE/USD ⭐ | 3.618e-06 | 87.11 | +0.30% | 3.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XBT/USD | 61611.4 | 77.64 | +0.08% | 1.94x | STRONG 74/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 73.43 | 77.49 | +0.11% | 0.81x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 8 | XRP/USD | 0.97786 | 74.55 | -0.00% | 0.46x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 9 | ETH/USD | 1726.98 | 70.99 | -0.04% | 0.99x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | SUI/USD | 0.6881 | 70.37 | -0.19% | 0.57x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | LINK/USD | 9.5597 | 69.51 | -0.15% | 0.47x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 12 | LTC/USD | 44.44 | 68.85 | +0.25% | 1.33x | STRONG 79/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.613e-06 | 89.68 | +0.30% | 3.73x | 5625 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | FET/USD | 0.1282 | 83.04 | +0.87% | 2.82x | 2888 | STRONG 92/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
