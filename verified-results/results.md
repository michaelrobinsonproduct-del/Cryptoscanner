# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T13:31:45.366834+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45184446514
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b73575ffe4330b1523eb327f0933ce0d152ef854 (atomic ledger/results publication)
**Ledger generation:** 1436 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.1 | 80.606 | 64.982 | +1.65% | +0.12% | 2.66x | 3.1 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | QNT/USD | 156.38 | 77.542 | 88.815 | +9.02% | -0.74% | 0.24x | 8.3 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | CCD/USD | 0.002923 | 76.959 | 74.223 | +9.89% | +0.76% | 0.89x | 3.4 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | SOL/USD | 72.39 | 70.176 | 71.752 | +2.49% | +0.23% | 0.72x | 1.4 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6686 | 69.754 | 68.023 | +1.97% | +0.18% | 1.08x | 1.5 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PAXG/USD | 3614.05 | 67.979 | 52.178 | +1.17% | +0.16% | 33.12x | 1.1 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XMR/USD | 502.3 | 61.802 | 64.093 | +1.74% | -0.18% | 0.86x | 6.2 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0555832 | 59.778 | 50.017 | +0.54% | -0.02% | 1.99x | 0.7 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93957 | 58.823 | 63.653 | +1.30% | -0.04% | 0.53x | 0.9 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LTC/USD | 40.96 | 58.342 | 54.980 | +1.99% | +0.34% | 1.17x | 2.4 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XAUT/USD | 3612 | 56.778 | 41.044 | +1.12% | +0.15% | 3.43x | 0.6 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 12 | AAVE/USD | 98.29 | 56.484 | 37.491 | +0.44% | +0.80% | 3.52x | 4.1 | 2026-11-23T13:31:38.861393+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 88.815 | 156.38 | -0.74% | 0.24x |
| 2 | CCD/USD | 74.223 | 0.002923 | +0.76% | 0.89x |
| 3 | SOL/USD | 71.752 | 72.39 | +0.23% | 0.72x |
| 4 | SUI/USD | 68.023 | 0.6686 | +0.18% | 1.08x |
| 5 | HYPE/USD | 64.982 | 64.1 | +0.12% | 2.66x |
| 6 | XMR/USD | 64.093 | 502.3 | -0.18% | 0.86x |
| 7 | XRP/USD | 63.653 | 0.93957 | -0.04% | 0.53x |
| 8 | LTC/USD | 54.980 | 40.96 | +0.34% | 1.17x |
| 9 | PAXG/USD | 52.178 | 3614.05 | +0.16% | 33.12x |
| 10 | XDG/USD | 50.017 | 0.0555832 | -0.02% | 1.99x |
| 11 | XAUT/USD | 41.044 | 3612 | +0.15% | 3.43x |
| 12 | AAVE/USD | 37.491 | 98.29 | +0.80% | 3.52x |

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

- Persisted scans: 1436; predictions: 11999; observations: 869626.
- Matured sampled outcomes across 1/6/24/48h: 20239; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45184446514 · **Generation:** 1436 · **Legacy run:** 45184446514
**Main quote time:** 2026-11-23T13:31:45.366834+00:00 · **Legacy report time:** 2026-11-23T13:32:53.565574+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.1 | 80.61 | +0.12% | 2.66x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | QNT/USD | 156.38 | 77.54 | -0.74% | 0.24x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 3 | CCD/USD | 0.002923 | 76.96 | +0.76% | 0.89x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 4 | SOL/USD | 72.39 | 70.18 | +0.23% | 0.72x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6686 | 69.75 | +0.18% | 1.08x | STRONG 70/100 | HIGH 62/100 | Watch |
| 6 | PAXG/USD | 3614.05 | 67.98 | +0.16% | 33.12x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | XMR/USD | 502.3 | 61.80 | -0.18% | 0.86x | WEAK 36/100 | HIGH 68/100 | Watch |
| 8 | XDG/USD | 0.0555832 | 59.78 | -0.02% | 1.99x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 9 | XRP/USD | 0.93957 | 58.82 | -0.04% | 0.53x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LTC/USD | 40.96 | 58.34 | +0.34% | 1.17x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 11 | XAUT/USD | 3612 | 56.78 | +0.15% | 3.43x | STRONG 73/100 | HIGH 60/100 | Watch |
| 12 | AAVE/USD | 98.29 | 56.48 | +0.80% | 3.52x | STRONG 83/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.2999 | 93.84 | +2.14% | 15.48x | 8941 | STRONG 97/100 | HIGH 61/100 | Consider small entry |
| 2 | ALGO/USD | 0.08441 | 80.06 | +0.75% | 1.78x | 4492 | STRONG 85/100 | HIGH 60/100 | Consider small entry |
| 3 | INJ/USD | 6.411 | 77.51 | +0.17% | 3.42x | 4193 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | HYPE/USD ⭐ | 63.9 | 71.88 | +0.12% | 2.66x | 9440 | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6673 | 71.11 | +0.18% | 1.08x | 5884 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
