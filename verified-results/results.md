# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T15:22:15.184406+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46023891644
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ebfdf3c4594206cb235d5103d5d312505ae04751 (atomic ledger/results publication)
**Ledger generation:** 2025 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 726.77 | 120.666 | 97.729 | +6.62% | +1.59% | 2.67x | 4.5 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | FET/USD | 0.1253 | 80.421 | 56.967 | +4.07% | +1.69% | 2.82x | 15.9 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | STRONG 90/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.0571 | 80.249 | 59.672 | +1.29% | +1.12% | 8.83x | 8.7 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 71.13 | 76.916 | 56.172 | +0.27% | +1.15% | 4.82x | 1.4 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | HYPE/USD | 63.67 | 68.501 | 70.527 | +2.33% | +0.25% | 0.67x | 1.6 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | JUP/USD | 0.24519 | 62.794 | 48.960 | +3.64% | +0.71% | 2.03x | 19.7 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 7 | LIGHTER/USD | 2.587 | 59.862 | 52.873 | +4.23% | +0.89% | 1.26x | 19.3 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 8 | VVV/USD | 26.438 | 58.743 | 53.279 | +0.97% | +1.14% | 0.98x | 9.5 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 9 | UNI/USD | 4.7204 | 56.505 | 59.636 | +1.51% | +1.18% | 0.09x | 6.8 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | INJ/USD | 6.263 | 54.112 | 49.063 | +1.15% | +1.56% | 0.72x | 1.6 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | VIRTUAL/USD | 0.3711 | 48.979 | 41.362 | +1.84% | +1.09% | 1.22x | 8.1 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 12 | PAXG/USD | 3608.83 | 46.477 | 52.074 | +1.46% | -0.12% | 0.50x | 0.1 | 2026-11-27T15:22:08.663839+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.729 | 726.77 | +1.59% | 2.67x |
| 2 | HYPE/USD | 70.527 | 63.67 | +0.25% | 0.67x |
| 3 | XDG/USD | 59.672 | 0.0571 | +1.12% | 8.83x |
| 4 | UNI/USD | 59.636 | 4.7204 | +1.18% | 0.09x |
| 5 | FET/USD | 56.967 | 0.1253 | +1.69% | 2.82x |
| 6 | SOL/USD | 56.172 | 71.13 | +1.15% | 4.82x |
| 7 | VVV/USD | 53.279 | 26.438 | +1.14% | 0.98x |
| 8 | LIGHTER/USD | 52.873 | 2.587 | +0.89% | 1.26x |
| 9 | PAXG/USD | 52.074 | 3608.83 | -0.12% | 0.50x |
| 10 | INJ/USD | 49.063 | 6.263 | +1.56% | 0.72x |
| 11 | JUP/USD | 48.960 | 0.24519 | +0.71% | 2.03x |
| 12 | VIRTUAL/USD | 41.362 | 0.3711 | +1.09% | 1.22x |

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

- Persisted scans: 2025; predictions: 18002; observations: 1226234.
- Matured sampled outcomes across 1/6/24/48h: 40229; gap abstentions: 25924. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46023891644 · **Generation:** 2025 · **Legacy run:** 46023891644
**Main quote time:** 2026-11-27T15:22:15.184406+00:00 · **Legacy report time:** 2026-11-27T15:22:59.600467+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 726.77 | 120.67 | +1.59% | 2.67x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1253 | 80.42 | +1.69% | 2.82x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0571 | 80.25 | +1.12% | 8.83x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 71.13 | 76.92 | +1.15% | 4.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | HYPE/USD | 63.67 | 68.50 | +0.25% | 0.67x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | JUP/USD ⭐ | 0.24519 | 62.79 | +0.71% | 2.03x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 7 | LIGHTER/USD ⭐ | 2.587 | 59.86 | +0.89% | 1.26x | STRONG 70/100 | HIGH 66/100 | Watch |
| 8 | VVV/USD | 26.438 | 58.74 | +1.14% | 0.98x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 9 | UNI/USD | 4.7204 | 56.50 | +1.18% | 0.09x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 10 | INJ/USD | 6.263 | 54.11 | +1.56% | 0.72x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 11 | VIRTUAL/USD | 0.3711 | 48.98 | +1.09% | 1.22x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 12 | PAXG/USD | 3608.83 | 46.48 | -0.12% | 0.50x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 730.23 | 96.46 | +1.59% | 2.67x | 39312 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | FET/USD ⭐ | 0.1256 | 86.23 | +1.69% | 2.82x | 3573 | STRONG 98/100 | VERY_HIGH 72/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0572169 | 73.24 | +1.12% | 8.83x | 10708 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | JUP/USD ⭐ | 0.24519 | 70.56 | +0.71% | 2.03x | 2234 | STRONG 95/100 | HIGH 66/100 | Consider small entry |
| 5 | LIGHTER/USD ⭐ | 2.592 | 67.99 | +0.89% | 1.26x | 1746 | STRONG 74/100 | HIGH 66/100 | Watch |
| 6 | SOL/USD ⭐ | 71.3 | 66.73 | +1.15% | 4.82x | 40181 | STRONG 98/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, FET/USD, XDG/USD, SOL/USD, JUP/USD, LIGHTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
