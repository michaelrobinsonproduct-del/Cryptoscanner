# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T21:42:26.781753+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46071720839
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 684af994101a34132669d2868534d5f43326570e (atomic ledger/results publication)
**Ledger generation:** 2064 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 736.51 | 116.233 | 99.118 | +8.05% | +0.42% | 4.37x | 1.8 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05011 | 92.289 | 77.688 | +3.38% | -0.08% | 4.90x | 2.0 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 63.94 | 76.973 | 73.569 | +2.76% | -0.02% | 1.35x | 1.6 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PAXG/USD | 3642.65 | 74.566 | 59.584 | +2.42% | -0.00% | 30.12x | 1.5 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 71.87 | 74.397 | 63.481 | +1.31% | +0.13% | 2.03x | 1.4 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0575933 | 71.234 | 70.125 | +2.16% | -0.12% | 1.17x | 0.0 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 7 | RENDER/USD | 1.41 | 64.348 | 66.520 | +5.78% | +0.79% | 0.39x | 14.2 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6738 | 62.831 | 60.653 | +0.91% | -0.07% | 1.25x | 1.5 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | WEAK 41/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XAUT/USD | 3647 | 60.989 | 53.677 | +2.45% | -0.02% | 1.74x | 2.5 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 10 | TAO/USD | 187.7291 | 56.630 | 66.737 | +2.15% | -0.19% | 0.08x | 6.6 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | PUMP/USD | 0.002597 | 56.294 | 40.908 | +0.43% | +0.08% | 11.39x | 3.9 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 12 | LTC/USD | 44.36 | 55.502 | 63.794 | +1.42% | -0.09% | 0.22x | 2.3 | 2026-11-27T21:42:20.580834+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.118 | 736.51 | +0.42% | 4.37x |
| 2 | NIGHT/USD | 77.688 | 0.05011 | -0.08% | 4.90x |
| 3 | HYPE/USD | 73.569 | 63.94 | -0.02% | 1.35x |
| 4 | XDG/USD | 70.125 | 0.0575933 | -0.12% | 1.17x |
| 5 | TAO/USD | 66.737 | 187.7291 | -0.19% | 0.08x |
| 6 | RENDER/USD | 66.520 | 1.41 | +0.79% | 0.39x |
| 7 | LTC/USD | 63.794 | 44.36 | -0.09% | 0.22x |
| 8 | SOL/USD | 63.481 | 71.87 | +0.13% | 2.03x |
| 9 | SUI/USD | 60.653 | 0.6738 | -0.07% | 1.25x |
| 10 | PAXG/USD | 59.584 | 3642.65 | -0.00% | 30.12x |
| 11 | XAUT/USD | 53.677 | 3647 | -0.02% | 1.74x |
| 12 | PUMP/USD | 40.908 | 0.002597 | +0.08% | 11.39x |

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

- Persisted scans: 2064; predictions: 18470; observations: 1249832.
- Matured sampled outcomes across 1/6/24/48h: 41939; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46071720839 · **Generation:** 2064 · **Legacy run:** 46071720839
**Main quote time:** 2026-11-27T21:42:26.781753+00:00 · **Legacy report time:** 2026-11-27T21:43:07.527732+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 736.51 | 116.23 | +0.42% | 4.37x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD | 0.05011 | 92.29 | -0.08% | 4.90x | STRONG 76/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD | 63.94 | 76.97 | -0.02% | 1.35x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | PAXG/USD | 3642.65 | 74.57 | -0.00% | 30.12x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 71.87 | 74.40 | +0.13% | 2.03x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD | 0.0575933 | 71.23 | -0.12% | 1.17x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 7 | RENDER/USD | 1.41 | 64.35 | +0.79% | 0.39x | MODERATE 57/100 | VERY_HIGH 81/100 | Watch |
| 8 | SUI/USD | 0.6738 | 62.83 | -0.07% | 1.25x | WEAK 41/100 | HIGH 61/100 | Watch |
| 9 | XAUT/USD | 3647 | 60.99 | -0.02% | 1.74x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 10 | TAO/USD | 187.7291 | 56.63 | -0.19% | 0.08x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | PUMP/USD | 0.002597 | 56.29 | +0.08% | 11.39x | STRONG 73/100 | HIGH 55/100 | Watch |
| 12 | LTC/USD | 44.36 | 55.50 | -0.09% | 0.22x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 735.91 | 100.00 | +0.42% | 4.37x | 38586 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ENA/USD | 0.1039 | 78.00 | +0.19% | 31.06x | 2762 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
