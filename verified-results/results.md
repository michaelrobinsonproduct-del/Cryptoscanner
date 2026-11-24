# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T19:47:01.918493+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45473412234
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** afc69a2235828a93b5b6cd69c3ab82c4e33f6778 (atomic ledger/results publication)
**Ledger generation:** 1618 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501 | 76.109 | 76.475 | +3.08% | +0.03% | 0.95x | 0.2 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 2 | VVV/USD | 24.687 | 58.981 | 58.191 | +0.98% | -0.47% | 1.31x | 7.3 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 3 | GBP/USD | 1.3112 | 56.042 | 59.118 | +0.61% | +0.00% | 0.69x | 0.3 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01653 | 55.290 | 61.110 | +5.62% | -0.12% | 0.48x | 18.2 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | WEAK 28/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | LUNA/USD | 4.627e-05 | 53.352 | 61.716 | +6.44% | -0.13% | 0.23x | 30.3 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | WEAK 22/100 | EXTREME 93/100 | Do nothing | WATCH |
| 6 | AUD/USD | 0.66448 | 41.792 | 43.885 | +0.29% | +0.02% | 0.78x | 2.0 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.446e-06 | 41.593 | 46.897 | +0.70% | -0.81% | 0.87x | 2.9 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | NIGHT/USD | 0.04874 | 41.261 | 48.229 | +1.23% | -0.25% | 0.43x | 2.1 | 2026-11-24T19:46:58.288717+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 76.475 | 501 | +0.03% | 0.95x |
| 2 | LUNA/USD | 61.716 | 4.627e-05 | -0.13% | 0.23x |
| 3 | 2Z/USD | 61.110 | 0.01653 | -0.12% | 0.48x |
| 4 | GBP/USD | 59.118 | 1.3112 | +0.00% | 0.69x |
| 5 | VVV/USD | 58.191 | 24.687 | -0.47% | 1.31x |
| 6 | NIGHT/USD | 48.229 | 0.04874 | -0.25% | 0.43x |
| 7 | PEPE/USD | 46.897 | 3.446e-06 | -0.81% | 0.87x |
| 8 | AUD/USD | 43.885 | 0.66448 | +0.02% | 0.78x |

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

- Persisted scans: 1618; predictions: 13890; observations: 980454.
- Matured sampled outcomes across 1/6/24/48h: 28231; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45473412234 · **Generation:** 1618 · **Legacy run:** 45473412234
**Main quote time:** 2026-11-24T19:47:01.918493+00:00 · **Legacy report time:** 2026-11-24T19:48:11.488382+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 501 | 76.11 | +0.03% | 0.95x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 2 | VVV/USD | 24.687 | 58.98 | -0.47% | 1.31x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 3 | GBP/USD | 1.3112 | 56.04 | +0.00% | 0.69x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 4 | 2Z/USD | 0.01653 | 55.29 | -0.12% | 0.48x | WEAK 28/100 | EXTREME 94/100 | Do nothing |
| 5 | LUNA/USD | 4.627e-05 | 53.35 | -0.13% | 0.23x | WEAK 22/100 | EXTREME 93/100 | Do nothing |
| 6 | AUD/USD | 0.66448 | 41.79 | +0.02% | 0.78x | WEAK 41/100 | HIGH 62/100 | Watch |
| 7 | PEPE/USD | 3.446e-06 | 41.59 | -0.81% | 0.87x | WEAK 26/100 | HIGH 68/100 | Do nothing |
| 8 | NIGHT/USD | 0.04874 | 41.26 | -0.25% | 0.43x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
