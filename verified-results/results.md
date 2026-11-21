# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T20:21:07.306408+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44945672129
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** fea0c905a37770e1c77b6a8ea9d793ad0a438cc3 (atomic ledger/results publication)
**Ledger generation:** 1181 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04519 | 101.452 | 89.272 | +7.03% | +0.40% | 2.02x | 8.9 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 486.58 | 96.829 | 97.121 | +6.64% | -0.15% | 1.05x | 5.8 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 3 | UNI/USD | 4.6974 | 85.577 | 89.581 | +5.15% | +0.13% | 0.54x | 3.0 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEC/USD | 791.8 | 83.864 | 84.911 | +4.47% | +0.11% | 0.84x | 2.8 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ETH/USD | 1682.57 | 83.482 | 82.312 | +3.91% | -0.01% | 1.12x | 0.1 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 70.41 | 75.965 | 71.609 | +2.47% | +0.07% | 1.40x | 1.4 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 60195.7 | 70.320 | 71.529 | +2.36% | -0.01% | 0.88x | 0.0 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93386 | 67.222 | 74.320 | +2.77% | +0.14% | 0.22x | 0.1 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PAXG/USD | 3553.82 | 66.978 | 53.955 | +0.63% | -0.00% | 2.30x | 0.2 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.617 | 66.161 | 63.177 | +1.71% | -0.03% | 1.31x | 1.5 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0551601 | 65.939 | 66.406 | +1.63% | +0.18% | 0.86x | 0.0 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TAO/USD | 184.8959 | 61.075 | 69.626 | +2.43% | -0.03% | 0.16x | 4.8 | 2026-11-21T20:20:59.456741+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.121 | 486.58 | -0.15% | 1.05x |
| 2 | UNI/USD | 89.581 | 4.6974 | +0.13% | 0.54x |
| 3 | NIGHT/USD | 89.272 | 0.04519 | +0.40% | 2.02x |
| 4 | ZEC/USD | 84.911 | 791.8 | +0.11% | 0.84x |
| 5 | ETH/USD | 82.312 | 1682.57 | -0.01% | 1.12x |
| 6 | XRP/USD | 74.320 | 0.93386 | +0.14% | 0.22x |
| 7 | SOL/USD | 71.609 | 70.41 | +0.07% | 1.40x |
| 8 | XBT/USD | 71.529 | 60195.7 | -0.01% | 0.88x |
| 9 | TAO/USD | 69.626 | 184.8959 | -0.03% | 0.16x |
| 10 | XDG/USD | 66.406 | 0.0551601 | +0.18% | 0.86x |
| 11 | AVAX/USD | 63.177 | 6.617 | -0.03% | 1.31x |
| 12 | PAXG/USD | 53.955 | 3553.82 | -0.00% | 2.30x |

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

- Persisted scans: 1181; predictions: 9481; observations: 714407.
- Matured sampled outcomes across 1/6/24/48h: 12604; gap abstentions: 21308. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44945672129 · **Generation:** 1181 · **Legacy run:** 44945672129
**Main quote time:** 2026-11-21T20:21:07.306408+00:00 · **Legacy report time:** 2026-11-21T20:22:10.905691+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04519 | 101.45 | +0.40% | 2.02x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 486.58 | 96.83 | -0.15% | 1.05x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 3 | UNI/USD | 4.6974 | 85.58 | +0.13% | 0.54x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEC/USD | 791.8 | 83.86 | +0.11% | 0.84x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 5 | ETH/USD | 1682.57 | 83.48 | -0.01% | 1.12x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD ⭐ | 70.41 | 75.97 | +0.07% | 1.40x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD | 60195.7 | 70.32 | -0.01% | 0.88x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.93386 | 67.22 | +0.14% | 0.22x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | PAXG/USD | 3553.82 | 66.98 | -0.00% | 2.30x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 10 | AVAX/USD | 6.617 | 66.16 | -0.03% | 1.31x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 11 | XDG/USD | 0.0551601 | 65.94 | +0.18% | 0.86x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 12 | TAO/USD | 184.8959 | 61.08 | -0.03% | 0.16x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04519 | 86.49 | +0.40% | 2.02x | 11583 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 70.45 | 81.36 | +0.07% | 1.40x | 49779 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | ZBCN/USD | 0.001708 | 80.32 | +0.29% | 4.13x | 3201 | STRONG 90/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
