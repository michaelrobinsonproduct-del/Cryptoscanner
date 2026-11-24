# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T10:01:51.695461+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45370412876
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8df9be5a89eb4ab91873e21ae18ae93510ba5875 (atomic ledger/results publication)
**Ledger generation:** 1559 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 496.43 | 72.195 | 65.148 | +2.14% | -0.34% | 1.87x | 9.7 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 2 | MON/USD | 0.01249 | 71.294 | 78.387 | +8.42% | -1.27% | 0.92x | 16.1 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 3 | VVV/USD | 25.164 | 70.637 | 71.526 | +2.93% | +0.66% | 0.58x | 7.9 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01618 | 61.916 | 51.338 | +3.39% | -0.61% | 2.36x | 6.2 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.481e-06 | 54.496 | 61.124 | +1.72% | -0.09% | 0.38x | 2.9 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | ATOM/USD | 1.2912 | 48.445 | 33.523 | +0.70% | -0.02% | 2.72x | 9.3 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 7 | INX/USD | 0.003985 | 29.624 | 37.253 | +2.23% | -0.91% | 0.69x | 20.2 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | WEAK 10/100 | EXTREME 93/100 | Do nothing | WATCH |
| 8 | BAT/USD | 0.07806 | 21.530 | 27.613 | +1.15% | -1.19% | 0.99x | 25.7 | 2026-11-24T10:01:44.236235+00:00 | Not calibrated | WEAK 6/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.387 | 0.01249 | -1.27% | 0.92x |
| 2 | VVV/USD | 71.526 | 25.164 | +0.66% | 0.58x |
| 3 | XMR/USD | 65.148 | 496.43 | -0.34% | 1.87x |
| 4 | PEPE/USD | 61.124 | 3.481e-06 | -0.09% | 0.38x |
| 5 | 2Z/USD | 51.338 | 0.01618 | -0.61% | 2.36x |
| 6 | INX/USD | 37.253 | 0.003985 | -0.91% | 0.69x |
| 7 | ATOM/USD | 33.523 | 1.2912 | -0.02% | 2.72x |
| 8 | BAT/USD | 27.613 | 0.07806 | -1.19% | 0.99x |

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

- Persisted scans: 1559; predictions: 13427; observations: 944529.
- Matured sampled outcomes across 1/6/24/48h: 25628; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45370412876 · **Generation:** 1559 · **Legacy run:** 45370412876
**Main quote time:** 2026-11-24T10:01:51.695461+00:00 · **Legacy report time:** 2026-11-24T10:02:59.756090+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 496.43 | 72.19 | -0.34% | 1.87x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 2 | MON/USD | 0.01249 | 71.29 | -1.27% | 0.92x | WEAK 36/100 | VERY_HIGH 78/100 | Do nothing |
| 3 | VVV/USD | 25.164 | 70.64 | +0.66% | 0.58x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 4 | 2Z/USD | 0.01618 | 61.92 | -0.61% | 2.36x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 5 | PEPE/USD | 3.481e-06 | 54.50 | -0.09% | 0.38x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | ATOM/USD | 1.2912 | 48.45 | -0.02% | 2.72x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 7 | INX/USD | 0.003985 | 29.62 | -0.91% | 0.69x | WEAK 10/100 | EXTREME 93/100 | Do nothing |
| 8 | BAT/USD | 0.07806 | 21.53 | -1.19% | 0.99x | WEAK 6/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD | 1.30621 | 62.14 | +0.06% | 3.05x | 22416 | STRONG 76/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
