# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T22:42:31.173471+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46077969339
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 188345b5617c12e40f633dc9be2a2e2f8424a939 (atomic ledger/results publication)
**Ledger generation:** 2070 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 723.37 | 105.044 | 96.796 | +6.12% | +0.58% | 1.54x | 2.1 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 63.56 | 86.656 | 69.289 | +2.15% | +0.47% | 29.92x | 1.6 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.0501 | 82.950 | 77.543 | +3.36% | +0.24% | 1.42x | 2.0 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8059 | 72.857 | 73.057 | +3.35% | +0.21% | 0.88x | 4.0 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XAUT/USD | 3651.1 | 70.622 | 55.649 | +2.57% | -0.01% | 4.63x | 0.5 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 71.45 | 69.285 | 59.333 | +0.72% | +0.11% | 1.94x | 1.4 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0573365 | 66.020 | 66.788 | +1.71% | +0.26% | 0.80x | 0.3 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LIGHTER/USD | 2.617 | 65.556 | 67.630 | +5.44% | -0.15% | 0.87x | 7.6 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | LTC/USD | 44.4 | 62.543 | 63.214 | +1.51% | +0.41% | 0.73x | 4.5 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.29736 | 61.242 | 54.640 | +0.31% | +0.23% | 1.55x | 5.1 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 11 | RENDER/USD | 1.396 | 60.527 | 62.543 | +4.73% | +0.14% | 0.73x | 7.2 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | PAXG/USD | 3647.23 | 58.895 | 61.996 | +2.54% | +0.02% | 0.68x | 0.0 | 2026-11-27T22:42:24.077544+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.796 | 723.37 | +0.58% | 1.54x |
| 2 | NIGHT/USD | 77.543 | 0.0501 | +0.24% | 1.42x |
| 3 | UNI/USD | 73.057 | 4.8059 | +0.21% | 0.88x |
| 4 | HYPE/USD | 69.289 | 63.56 | +0.47% | 29.92x |
| 5 | LIGHTER/USD | 67.630 | 2.617 | -0.15% | 0.87x |
| 6 | XDG/USD | 66.788 | 0.0573365 | +0.26% | 0.80x |
| 7 | LTC/USD | 63.214 | 44.4 | +0.41% | 0.73x |
| 8 | RENDER/USD | 62.543 | 1.396 | +0.14% | 0.73x |
| 9 | PAXG/USD | 61.996 | 3647.23 | +0.02% | 0.68x |
| 10 | SOL/USD | 59.333 | 71.45 | +0.11% | 1.94x |
| 11 | XAUT/USD | 55.649 | 3651.1 | -0.01% | 4.63x |
| 12 | LINK/USD | 54.640 | 9.29736 | +0.23% | 1.55x |

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

- Persisted scans: 2070; predictions: 18542; observations: 1253468.
- Matured sampled outcomes across 1/6/24/48h: 42239; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46077969339 · **Generation:** 2070 · **Legacy run:** 46077969339
**Main quote time:** 2026-11-27T22:42:31.173471+00:00 · **Legacy report time:** 2026-11-27T22:43:16.139757+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 723.37 | 105.04 | +0.58% | 1.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 63.56 | 86.66 | +0.47% | 29.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.0501 | 82.95 | +0.24% | 1.42x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 4.8059 | 72.86 | +0.21% | 0.88x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 5 | XAUT/USD | 3651.1 | 70.62 | -0.01% | 4.63x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 71.45 | 69.29 | +0.11% | 1.94x | STRONG 70/100 | HIGH 55/100 | Watch |
| 7 | XDG/USD | 0.0573365 | 66.02 | +0.26% | 0.80x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 8 | LIGHTER/USD | 2.617 | 65.56 | -0.15% | 0.87x | WEAK 38/100 | VERY_HIGH 73/100 | Watch |
| 9 | LTC/USD | 44.4 | 62.54 | +0.41% | 0.73x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.29736 | 61.24 | +0.23% | 1.55x | STRONG 76/100 | HIGH 55/100 | Watch |
| 11 | RENDER/USD | 1.396 | 60.53 | +0.14% | 0.73x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |
| 12 | PAXG/USD | 3647.23 | 58.89 | +0.02% | 0.68x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 723.3 | 100.00 | +0.58% | 1.54x | 37232 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.05011 | 91.01 | +0.24% | 1.42x | 19318 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD ⭐ | 63.52 | 83.34 | +0.47% | 29.92x | 19116 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, HYPE/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
