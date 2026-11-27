# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T10:21:55.534031+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45981133917
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c70aaf2f665ec91c057c31926a99c3637e3c07b5 (atomic ledger/results publication)
**Ledger generation:** 1994 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 750.7 | 94.291 | 97.868 | +10.13% | -0.86% | 1.07x | 4.3 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 2 | XRP/USD | 0.97744 | 93.170 | 79.581 | +3.68% | +0.06% | 2.33x | 2.4 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.53 | 84.961 | 91.476 | +5.32% | -0.23% | 0.46x | 1.5 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152154 | 79.330 | 67.882 | +2.49% | -0.13% | 2.21x | 2.7 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 73.28 | 75.620 | 77.407 | +3.30% | -0.26% | 0.95x | 1.4 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 6 | LTC/USD | 44.45 | 72.664 | 64.492 | +1.62% | +0.14% | 1.75x | 2.3 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 61576.1 | 67.819 | 67.466 | +1.78% | -0.07% | 1.07x | 0.0 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | INJ/USD | 6.499 | 67.174 | 69.580 | +4.96% | -0.57% | 1.04x | 4.6 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6869 | 66.909 | 73.673 | +2.88% | -0.16% | 0.40x | 2.9 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ENA/USD | 0.1067 | 66.653 | 71.328 | +6.27% | +0.19% | 0.44x | 18.8 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XAUT/USD | 3659.7 | 66.219 | 51.301 | +2.81% | -0.02% | 6.03x | 0.3 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 12 | ETH/USD | 1726.13 | 65.698 | 70.919 | +2.28% | -0.05% | 0.50x | 0.1 | 2026-11-27T10:21:47.541940+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.868 | 750.7 | -0.86% | 1.07x |
| 2 | HYPE/USD | 91.476 | 65.53 | -0.23% | 0.46x |
| 3 | XRP/USD | 79.581 | 0.97744 | +0.06% | 2.33x |
| 4 | SOL/USD | 77.407 | 73.28 | -0.26% | 0.95x |
| 5 | SUI/USD | 73.673 | 0.6869 | -0.16% | 0.40x |
| 6 | ENA/USD | 71.328 | 0.1067 | +0.19% | 0.44x |
| 7 | ETH/USD | 70.919 | 1726.13 | -0.05% | 0.50x |
| 8 | INJ/USD | 69.580 | 6.499 | -0.57% | 1.04x |
| 9 | ADA/USD | 67.882 | 0.152154 | -0.13% | 2.21x |
| 10 | XBT/USD | 67.466 | 61576.1 | -0.07% | 1.07x |
| 11 | LTC/USD | 64.492 | 44.45 | +0.14% | 1.75x |
| 12 | XAUT/USD | 51.301 | 3659.7 | -0.02% | 6.03x |

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

- Persisted scans: 1994; predictions: 17630; observations: 1207533.
- Matured sampled outcomes across 1/6/24/48h: 39137; gap abstentions: 25769. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45981133917 · **Generation:** 1994 · **Legacy run:** 45981133917
**Main quote time:** 2026-11-27T10:21:55.534031+00:00 · **Legacy report time:** 2026-11-27T10:22:31.471026+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 750.7 | 94.29 | -0.86% | 1.07x | MODERATE 57/100 | HIGH 68/100 | Watch |
| 2 | XRP/USD ⭐ | 0.97744 | 93.17 | +0.06% | 2.33x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 65.53 | 84.96 | -0.23% | 0.46x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 4 | ADA/USD | 0.152154 | 79.33 | -0.13% | 2.21x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 73.28 | 75.62 | -0.26% | 0.95x | WEAK 43/100 | HIGH 68/100 | Watch |
| 6 | LTC/USD | 44.45 | 72.66 | +0.14% | 1.75x | STRONG 71/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD | 61576.1 | 67.82 | -0.07% | 1.07x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | INJ/USD | 6.499 | 67.17 | -0.57% | 1.04x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.6869 | 66.91 | -0.16% | 0.40x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | ENA/USD | 0.1067 | 66.65 | +0.19% | 0.44x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 11 | XAUT/USD | 3659.7 | 66.22 | -0.02% | 6.03x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 12 | ETH/USD | 1726.13 | 65.70 | -0.05% | 0.50x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.97783 | 98.47 | +0.06% | 2.33x | 26463 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | FET/USD | 0.1271 | 81.38 | +0.08% | 3.08x | 2899 | STRONG 76/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
