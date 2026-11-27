# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T04:51:27.728748+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45942171918
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 838974957bf42df3282974cf95c372a2c9f9e985 (atomic ledger/results publication)
**Ledger generation:** 1961 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 756.44 | 97.507 | 98.479 | +10.97% | -0.19% | 1.00x | 3.0 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | MODERATE 54/100 | HIGH 68/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.89 | 90.598 | 95.530 | +5.90% | -0.14% | 0.57x | 1.5 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ETH/USD | 1731.71 | 86.811 | 73.234 | +2.61% | +0.09% | 2.31x | 0.1 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LINK/USD | 9.5979 | 85.778 | 77.543 | +3.55% | +0.28% | 1.68x | 4.7 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | W/USD | 0.00951 | 70.680 | 72.447 | +7.95% | -0.10% | 0.88x | 10.5 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95962 | 68.033 | 67.474 | +1.79% | -0.06% | 1.08x | 0.1 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6829 | 63.039 | 69.308 | +2.28% | +0.07% | 0.34x | 2.9 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SOL/USD | 72.76 | 62.570 | 72.272 | +2.57% | -0.15% | 0.11x | 1.4 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | VVV/USD | 26.945 | 61.219 | 71.287 | +2.91% | -0.56% | 0.27x | 8.2 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | LTC/USD | 44.56 | 60.837 | 67.001 | +1.87% | -0.02% | 0.39x | 2.2 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ADA/USD | 0.151612 | 59.815 | 66.463 | +2.12% | +0.06% | 0.30x | 3.4 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 61410.5 | 58.733 | 65.550 | +1.51% | -0.02% | 0.33x | 0.0 | 2026-11-27T04:51:19.324500+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.479 | 756.44 | -0.19% | 1.00x |
| 2 | HYPE/USD | 95.530 | 65.89 | -0.14% | 0.57x |
| 3 | LINK/USD | 77.543 | 9.5979 | +0.28% | 1.68x |
| 4 | ETH/USD | 73.234 | 1731.71 | +0.09% | 2.31x |
| 5 | W/USD | 72.447 | 0.00951 | -0.10% | 0.88x |
| 6 | SOL/USD | 72.272 | 72.76 | -0.15% | 0.11x |
| 7 | VVV/USD | 71.287 | 26.945 | -0.56% | 0.27x |
| 8 | SUI/USD | 69.308 | 0.6829 | +0.07% | 0.34x |
| 9 | XRP/USD | 67.474 | 0.95962 | -0.06% | 1.08x |
| 10 | LTC/USD | 67.001 | 44.56 | -0.02% | 0.39x |
| 11 | ADA/USD | 66.463 | 0.151612 | +0.06% | 0.30x |
| 12 | XBT/USD | 65.550 | 61410.5 | -0.02% | 0.33x |

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

- Persisted scans: 1961; predictions: 17234; observations: 1187645.
- Matured sampled outcomes across 1/6/24/48h: 37970; gap abstentions: 25520. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45942171918 · **Generation:** 1961 · **Legacy run:** 45942171918
**Main quote time:** 2026-11-27T04:51:27.728748+00:00 · **Legacy report time:** 2026-11-27T04:52:03.011891+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 756.44 | 97.51 | -0.19% | 1.00x | MODERATE 54/100 | HIGH 68/100 | Watch |
| 2 | HYPE/USD | 65.89 | 90.60 | -0.14% | 0.57x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 3 | ETH/USD ⭐ | 1731.71 | 86.81 | +0.09% | 2.31x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD ⭐ | 9.5979 | 85.78 | +0.28% | 1.68x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 5 | W/USD | 0.00951 | 70.68 | -0.10% | 0.88x | WEAK 35/100 | VERY_HIGH 79/100 | Watch |
| 6 | XRP/USD | 0.95962 | 68.03 | -0.06% | 1.08x | WEAK 44/100 | HIGH 68/100 | Watch |
| 7 | SUI/USD | 0.6829 | 63.04 | +0.07% | 0.34x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 8 | SOL/USD | 72.76 | 62.57 | -0.15% | 0.11x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | VVV/USD | 26.945 | 61.22 | -0.56% | 0.27x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | LTC/USD | 44.56 | 60.84 | -0.02% | 0.39x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | ADA/USD | 0.151612 | 59.81 | +0.06% | 0.30x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 61410.5 | 58.73 | -0.02% | 0.33x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1731.95 | 88.88 | +0.09% | 2.31x | 32262 | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 9.59294 | 87.91 | +0.28% | 1.68x | 7470 | STRONG 99/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ETH/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
