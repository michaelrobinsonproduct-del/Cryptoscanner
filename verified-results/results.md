# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T02:01:36.212927+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45309060592
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b60ed988ff50cb30b148d56c817d2025ddc111ac (atomic ledger/results publication)
**Ledger generation:** 1510 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01183 | 73.114 | 52.095 | +2.69% | +1.20% | 3.44x | 8.4 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.04573 | 66.157 | 54.921 | +0.45% | -0.75% | 2.55x | 6.5 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PAXG/USD | 3643.5 | 64.903 | 52.665 | +0.62% | -0.55% | 2.82x | 0.1 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AI/USD | 0.01591 | 64.757 | 59.242 | +4.46% | +0.63% | 1.23x | 6.3 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94528 | 62.836 | 58.966 | +0.63% | -0.58% | 1.68x | 0.8 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AAVE/USD | 97.91 | 60.635 | 50.635 | +0.89% | -1.00% | 3.20x | 5.1 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.47e-06 | 55.799 | 56.646 | +1.40% | -0.86% | 1.34x | 2.9 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0566553 | 53.361 | 59.115 | +0.62% | -0.68% | 0.76x | 0.5 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | ADA/USD | 0.149172 | 50.607 | 56.374 | +0.49% | -0.77% | 0.81x | 4.1 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | VVV/USD | 24.644 | 47.946 | 56.347 | +0.80% | -0.42% | 0.37x | 8.5 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XLM/USD | 0.130903 | 46.214 | 57.603 | +0.70% | -0.68% | 0.20x | 4.6 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | NIGHT/USD | 0.04883 | 43.146 | 53.328 | +1.41% | -0.55% | 0.26x | 12.3 | 2026-11-24T02:01:26.857645+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 59.242 | 0.01591 | +0.63% | 1.23x |
| 2 | XDG/USD | 59.115 | 0.0566553 | -0.68% | 0.76x |
| 3 | XRP/USD | 58.966 | 0.94528 | -0.58% | 1.68x |
| 4 | XLM/USD | 57.603 | 0.130903 | -0.68% | 0.20x |
| 5 | PEPE/USD | 56.646 | 3.47e-06 | -0.86% | 1.34x |
| 6 | ADA/USD | 56.374 | 0.149172 | -0.77% | 0.81x |
| 7 | VVV/USD | 56.347 | 24.644 | -0.42% | 0.37x |
| 8 | LINK/USD | 54.921 | 9.04573 | -0.75% | 2.55x |
| 9 | NIGHT/USD | 53.328 | 0.04883 | -0.55% | 0.26x |
| 10 | PAXG/USD | 52.665 | 3643.5 | -0.55% | 2.82x |
| 11 | MON/USD | 52.095 | 0.01183 | +1.20% | 3.44x |
| 12 | AAVE/USD | 50.635 | 97.91 | -1.00% | 3.20x |

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

- Persisted scans: 1510; predictions: 12877; observations: 914691.
- Matured sampled outcomes across 1/6/24/48h: 23752; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45309060592 · **Generation:** 1510 · **Legacy run:** 45309060592
**Main quote time:** 2026-11-24T02:01:36.212927+00:00 · **Legacy report time:** 2026-11-24T02:02:27.026582+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01183 | 73.11 | +1.20% | 3.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD | 9.04573 | 66.16 | -0.75% | 2.55x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 3 | PAXG/USD | 3643.5 | 64.90 | -0.55% | 2.82x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 4 | AI/USD ⭐ | 0.01591 | 64.76 | +0.63% | 1.23x | STRONG 77/100 | VERY_HIGH 74/100 | Watch |
| 5 | XRP/USD | 0.94528 | 62.84 | -0.58% | 1.68x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 6 | AAVE/USD | 97.91 | 60.64 | -1.00% | 3.20x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | PEPE/USD | 3.47e-06 | 55.80 | -0.86% | 1.34x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 8 | XDG/USD | 0.0566553 | 53.36 | -0.68% | 0.76x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 9 | ADA/USD | 0.149172 | 50.61 | -0.77% | 0.81x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 10 | VVV/USD | 24.644 | 47.95 | -0.42% | 0.37x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XLM/USD | 0.130903 | 46.21 | -0.68% | 0.20x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | NIGHT/USD | 0.04883 | 43.15 | -0.55% | 0.26x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.015113 | 82.05 | +0.78% | 2.28x | 5275 | STRONG 81/100 | VERY_HIGH 77/100 | Watch |
| 2 | AI/USD ⭐ | 0.01591 | 75.90 | +0.63% | 1.23x | 2725 | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 3 | MON/USD ⭐ | 0.01186 | 73.54 | +1.20% | 3.44x | 6706 | STRONG 97/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** MON/USD, AI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
