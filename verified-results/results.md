# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T11:42:07.451213+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45992276815
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bee243abffe31be6f3d4639624899a5150444d9e (atomic ledger/results publication)
**Ledger generation:** 2002 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 759.38 | 94.340 | 97.299 | +11.40% | -0.06% | 0.73x | 5.4 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6884 | 89.957 | 75.248 | +3.10% | -0.06% | 3.53x | 2.9 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.92 | 84.382 | 95.110 | +5.95% | -0.23% | 0.04x | 3.0 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0587607 | 78.241 | 76.832 | +4.23% | +0.01% | 1.13x | 0.0 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ADA/USD | 0.152942 | 76.290 | 71.756 | +3.02% | -0.07% | 1.49x | 1.4 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.641e-06 | 74.970 | 75.564 | +4.69% | +0.03% | 0.93x | 2.7 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04894 | 72.787 | 54.804 | +0.97% | +0.60% | 15.47x | 2.0 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | SOL/USD | 73.25 | 72.770 | 77.111 | +3.26% | +0.01% | 0.56x | 1.4 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.9774 | 71.905 | 80.677 | +3.68% | -0.23% | 0.24x | 0.1 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ETH/USD | 1729.17 | 69.946 | 72.180 | +2.46% | +0.14% | 0.71x | 0.1 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61739 | 67.213 | 69.351 | +2.05% | +0.17% | 0.70x | 0.0 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 9.55197 | 66.269 | 75.263 | +3.06% | +0.01% | 0.09x | 2.3 | 2026-11-27T11:42:00.616185+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.299 | 759.38 | -0.06% | 0.73x |
| 2 | HYPE/USD | 95.110 | 65.92 | -0.23% | 0.04x |
| 3 | XRP/USD | 80.677 | 0.9774 | -0.23% | 0.24x |
| 4 | SOL/USD | 77.111 | 73.25 | +0.01% | 0.56x |
| 5 | XDG/USD | 76.832 | 0.0587607 | +0.01% | 1.13x |
| 6 | PEPE/USD | 75.564 | 3.641e-06 | +0.03% | 0.93x |
| 7 | LINK/USD | 75.263 | 9.55197 | +0.01% | 0.09x |
| 8 | SUI/USD | 75.248 | 0.6884 | -0.06% | 3.53x |
| 9 | ETH/USD | 72.180 | 1729.17 | +0.14% | 0.71x |
| 10 | ADA/USD | 71.756 | 0.152942 | -0.07% | 1.49x |
| 11 | XBT/USD | 69.351 | 61739 | +0.17% | 0.70x |
| 12 | NIGHT/USD | 54.804 | 0.04894 | +0.60% | 15.47x |

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

- Persisted scans: 2002; predictions: 17726; observations: 1212355.
- Matured sampled outcomes across 1/6/24/48h: 39425; gap abstentions: 25811. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45992276815 · **Generation:** 2002 · **Legacy run:** 45992276815
**Main quote time:** 2026-11-27T11:42:07.451213+00:00 · **Legacy report time:** 2026-11-27T11:42:59.935577+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 759.38 | 94.34 | -0.06% | 0.73x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 2 | SUI/USD | 0.6884 | 89.96 | -0.06% | 3.53x | STRONG 75/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD | 65.92 | 84.38 | -0.23% | 0.04x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 4 | XDG/USD | 0.0587607 | 78.24 | +0.01% | 1.13x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 5 | ADA/USD | 0.152942 | 76.29 | -0.07% | 1.49x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 6 | PEPE/USD | 3.641e-06 | 74.97 | +0.03% | 0.93x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 7 | NIGHT/USD | 0.04894 | 72.79 | +0.60% | 15.47x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD | 73.25 | 72.77 | +0.01% | 0.56x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.9774 | 71.90 | -0.23% | 0.24x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 10 | ETH/USD | 1729.17 | 69.95 | +0.14% | 0.71x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61739 | 67.21 | +0.17% | 0.70x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 9.55197 | 66.27 | +0.01% | 0.09x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.494 | 95.79 | +0.40% | 5.37x | 4900 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD | 0.002685 | 89.33 | +0.11% | 6.60x | 3955 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
