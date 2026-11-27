# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T13:52:20.219277+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46010443864
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** af99f2bc75edb0ec70c2c3c8d39e9618c47cfffe (atomic ledger/results publication)
**Ledger generation:** 2016 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.33 | 116.974 | 99.246 | +6.61% | +0.55% | 7.00x | 1.5 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 757.08 | 115.786 | 98.547 | +11.06% | +1.01% | 2.22x | 2.9 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 27.537 | 99.217 | 86.049 | +5.17% | +1.65% | 1.49x | 5.1 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6885 | 92.905 | 75.353 | +3.12% | +0.53% | 2.49x | 2.9 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | INJ/USD | 6.494 | 92.732 | 72.231 | +4.88% | +1.10% | 6.53x | 6.2 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | PEPE/USD | 3.633e-06 | 84.802 | 72.453 | +4.46% | +0.36% | 2.06x | 5.5 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XDG/USD | 0.058867 | 80.160 | 77.260 | +4.42% | +0.42% | 1.08x | 0.7 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XBT/USD | 61473.8 | 79.204 | 66.282 | +1.61% | +0.24% | 2.17x | 0.0 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XRP/USD | 0.97009 | 78.806 | 75.249 | +2.90% | +0.09% | 1.31x | 0.1 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ETH/USD | 1724.15 | 78.554 | 70.098 | +2.16% | +0.56% | 1.57x | 0.1 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | VIRTUAL/USD | 0.3884 | 76.686 | 74.557 | +6.59% | +0.52% | 0.95x | 5.2 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 12 | SOL/USD | 73.33 | 74.505 | 77.901 | +3.37% | +0.25% | 0.54x | 1.4 | 2026-11-27T13:52:12.788350+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 99.246 | 66.33 | +0.55% | 7.00x |
| 2 | ZEC/USD | 98.547 | 757.08 | +1.01% | 2.22x |
| 3 | VVV/USD | 86.049 | 27.537 | +1.65% | 1.49x |
| 4 | SOL/USD | 77.901 | 73.33 | +0.25% | 0.54x |
| 5 | XDG/USD | 77.260 | 0.058867 | +0.42% | 1.08x |
| 6 | SUI/USD | 75.353 | 0.6885 | +0.53% | 2.49x |
| 7 | XRP/USD | 75.249 | 0.97009 | +0.09% | 1.31x |
| 8 | VIRTUAL/USD | 74.557 | 0.3884 | +0.52% | 0.95x |
| 9 | PEPE/USD | 72.453 | 3.633e-06 | +0.36% | 2.06x |
| 10 | INJ/USD | 72.231 | 6.494 | +1.10% | 6.53x |
| 11 | ETH/USD | 70.098 | 1724.15 | +0.56% | 1.57x |
| 12 | XBT/USD | 66.282 | 61473.8 | +0.24% | 2.17x |

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

- Persisted scans: 2016; predictions: 17894; observations: 1220797.
- Matured sampled outcomes across 1/6/24/48h: 39905; gap abstentions: 25878. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46010443864 · **Generation:** 2016 · **Legacy run:** 46010443864
**Main quote time:** 2026-11-27T13:52:20.219277+00:00 · **Legacy report time:** 2026-11-27T13:53:02.112206+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.33 | 116.97 | +0.55% | 7.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 757.08 | 115.79 | +1.01% | 2.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 27.537 | 99.22 | +1.65% | 1.49x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6885 | 92.91 | +0.53% | 2.49x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | INJ/USD ⭐ | 6.494 | 92.73 | +1.10% | 6.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | PEPE/USD ⭐ | 3.633e-06 | 84.80 | +0.36% | 2.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.058867 | 80.16 | +0.42% | 1.08x | STRONG 85/100 | HIGH 62/100 | Watch |
| 8 | XBT/USD | 61473.8 | 79.20 | +0.24% | 2.17x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.97009 | 78.81 | +0.09% | 1.31x | STRONG 84/100 | HIGH 55/100 | Watch |
| 10 | ETH/USD ⭐ | 1724.15 | 78.55 | +0.56% | 1.57x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 11 | VIRTUAL/USD | 0.3884 | 76.69 | +0.52% | 0.95x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 12 | SOL/USD | 73.33 | 74.51 | +0.25% | 0.54x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.33 | 100.00 | +0.55% | 7.00x | 16045 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 757.44 | 100.00 | +1.01% | 2.22x | 39443 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6885 | 94.02 | +0.53% | 2.49x | 5274 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | INJ/USD ⭐ | 6.494 | 93.75 | +1.10% | 6.53x | 5068 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PEPE/USD ⭐ | 3.633e-06 | 93.20 | +0.36% | 2.06x | 5695 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD ⭐ | 27.471 | 92.94 | +1.65% | 1.49x | 9349 | STRONG 100/100 | HIGH 55/100 | Watch |
| 7 | TAO/USD | 189.9854 | 91.33 | +0.43% | 5.97x | 5757 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XRP/USD ⭐ | 0.96991 | 87.88 | +0.09% | 1.31x | 27230 | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | XDG/USD ⭐ | 0.0588512 | 87.45 | +0.42% | 1.08x | 6005 | STRONG 89/100 | HIGH 62/100 | Watch |
| 10 | WLD/USD | 0.2508 | 86.01 | +0.36% | 6.63x | 2849 | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 11 | ETH/USD ⭐ | 1725.27 | 82.55 | +0.56% | 1.57x | 36321 | STRONG 96/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** HYPE/USD, ZEC/USD, VVV/USD, SUI/USD, INJ/USD, PEPE/USD, XDG/USD, XRP/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
