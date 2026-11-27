# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T21:32:17.806614+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46070639073
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 782b4dbcd5bff38db24d687710c80c367d4122e8 (atomic ledger/results publication)
**Ledger generation:** 2063 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 736.32 | 116.891 | 99.661 | +8.02% | +0.45% | 4.10x | 0.7 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05015 | 91.692 | 75.277 | +3.47% | +0.58% | 2.35x | 8.0 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | PAXG/USD | 3643.28 | 74.560 | 59.630 | +2.43% | -0.01% | 11.79x | 1.5 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0575706 | 71.628 | 69.548 | +2.12% | -0.06% | 1.24x | 0.6 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XAUT/USD | 3646.8 | 69.913 | 54.721 | +2.45% | +0.04% | 2.62x | 0.3 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 64 | 69.484 | 74.245 | +2.86% | +0.11% | 0.47x | 1.6 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LTC/USD | 44.35 | 69.206 | 62.506 | +1.39% | +0.20% | 1.57x | 4.5 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148857 | 67.522 | 52.831 | +0.27% | -0.06% | 3.23x | 3.9 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SPACE/USD | 0.004193 | 65.749 | 71.082 | +8.29% | +0.70% | 0.12x | 9.6 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.523e-06 | 63.475 | 53.470 | +1.29% | +0.06% | 1.97x | 2.8 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 11 | LINK/USD | 9.34173 | 63.049 | 59.755 | +0.79% | -0.02% | 1.34x | 1.6 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SOL/USD | 71.86 | 62.145 | 63.382 | +1.30% | -0.13% | 0.94x | 1.4 | 2026-11-27T21:32:11.834880+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.661 | 736.32 | +0.45% | 4.10x |
| 2 | NIGHT/USD | 75.277 | 0.05015 | +0.58% | 2.35x |
| 3 | HYPE/USD | 74.245 | 64 | +0.11% | 0.47x |
| 4 | SPACE/USD | 71.082 | 0.004193 | +0.70% | 0.12x |
| 5 | XDG/USD | 69.548 | 0.0575706 | -0.06% | 1.24x |
| 6 | SOL/USD | 63.382 | 71.86 | -0.13% | 0.94x |
| 7 | LTC/USD | 62.506 | 44.35 | +0.20% | 1.57x |
| 8 | LINK/USD | 59.755 | 9.34173 | -0.02% | 1.34x |
| 9 | PAXG/USD | 59.630 | 3643.28 | -0.01% | 11.79x |
| 10 | XAUT/USD | 54.721 | 3646.8 | +0.04% | 2.62x |
| 11 | PEPE/USD | 53.470 | 3.523e-06 | +0.06% | 1.97x |
| 12 | ADA/USD | 52.831 | 0.148857 | -0.06% | 3.23x |

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

- Persisted scans: 2063; predictions: 18458; observations: 1249226.
- Matured sampled outcomes across 1/6/24/48h: 41879; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46070639073 · **Generation:** 2063 · **Legacy run:** 46070639073
**Main quote time:** 2026-11-27T21:32:17.806614+00:00 · **Legacy report time:** 2026-11-27T21:33:02.302547+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 736.32 | 116.89 | +0.45% | 4.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.05015 | 91.69 | +0.58% | 2.35x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PAXG/USD | 3643.28 | 74.56 | -0.01% | 11.79x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | XDG/USD | 0.0575706 | 71.63 | -0.06% | 1.24x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 5 | XAUT/USD | 3646.8 | 69.91 | +0.04% | 2.62x | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 64 | 69.48 | +0.11% | 0.47x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 7 | LTC/USD | 44.35 | 69.21 | +0.20% | 1.57x | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | ADA/USD | 0.148857 | 67.52 | -0.06% | 3.23x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 9 | SPACE/USD | 0.004193 | 65.75 | +0.70% | 0.12x | MODERATE 63/100 | VERY_HIGH 82/100 | Watch |
| 10 | PEPE/USD | 3.523e-06 | 63.48 | +0.06% | 1.97x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 11 | LINK/USD | 9.34173 | 63.05 | -0.02% | 1.34x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 12 | SOL/USD | 71.86 | 62.15 | -0.13% | 0.94x | WEAK 36/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 737.37 | 100.00 | +0.45% | 4.10x | 38769 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.05022 | 98.49 | +0.58% | 2.35x | 18513 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
