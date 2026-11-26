# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T21:11:16.066629+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45896161022
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2895a4818d08a360c6b767e2188264b40531b47b (atomic ledger/results publication)
**Ledger generation:** 1914 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.39123 | 96.137 | 78.519 | +9.34% | +0.52% | 3.17x | 7.7 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.5071 | 93.404 | 76.921 | +7.19% | +0.30% | 2.77x | 2.0 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | ADA/USD | 0.150821 | 93.002 | 77.829 | +3.46% | +0.03% | 4.11x | 2.9 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LTC/USD | 44.03 | 92.323 | 75.498 | +3.09% | +0.36% | 7.59x | 2.3 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | LINK/USD | 9.34291 | 88.289 | 71.713 | +3.30% | +0.32% | 3.80x | 4.2 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | HBAR/USD | 0.05498 | 85.383 | 71.857 | +5.53% | -0.27% | 2.49x | 3.6 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6749 | 75.549 | 60.919 | +1.29% | -0.07% | 17.95x | 1.5 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.39 | 73.144 | 74.318 | +2.87% | +0.44% | 0.66x | 1.6 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | WIF/USD | 0.1368 | 69.429 | 73.203 | +7.46% | -0.73% | 0.99x | 7.3 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | XRP/USD | 0.9519 | 67.883 | 66.413 | +1.64% | -0.00% | 1.15x | 0.1 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ETH/USD | 1702.92 | 66.592 | 60.151 | +0.74% | +0.03% | 1.63x | 0.1 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0569115 | 64.825 | 54.910 | +1.70% | -0.01% | 2.00x | 0.0 | 2026-11-26T21:11:07.678378+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 78.519 | 0.39123 | +0.52% | 3.17x |
| 2 | ADA/USD | 77.829 | 0.150821 | +0.03% | 4.11x |
| 3 | AKT/USD | 76.921 | 0.5071 | +0.30% | 2.77x |
| 4 | LTC/USD | 75.498 | 44.03 | +0.36% | 7.59x |
| 5 | HYPE/USD | 74.318 | 63.39 | +0.44% | 0.66x |
| 6 | WIF/USD | 73.203 | 0.1368 | -0.73% | 0.99x |
| 7 | HBAR/USD | 71.857 | 0.05498 | -0.27% | 2.49x |
| 8 | LINK/USD | 71.713 | 9.34291 | +0.32% | 3.80x |
| 9 | XRP/USD | 66.413 | 0.9519 | -0.00% | 1.15x |
| 10 | SUI/USD | 60.919 | 0.6749 | -0.07% | 17.95x |
| 11 | ETH/USD | 60.151 | 1702.92 | +0.03% | 1.63x |
| 12 | XDG/USD | 54.910 | 0.0569115 | -0.01% | 2.00x |

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

- Persisted scans: 1914; predictions: 16703; observations: 1159420.
- Matured sampled outcomes across 1/6/24/48h: 36308; gap abstentions: 25260. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45896161022 · **Generation:** 1914 · **Legacy run:** 45896161022
**Main quote time:** 2026-11-26T21:11:16.066629+00:00 · **Legacy report time:** 2026-11-26T21:11:59.541088+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.39123 | 96.14 | +0.52% | 3.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5071 | 93.40 | +0.30% | 2.77x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | ADA/USD | 0.150821 | 93.00 | +0.03% | 4.11x | STRONG 92/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD ⭐ | 44.03 | 92.32 | +0.36% | 7.59x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.34291 | 88.29 | +0.32% | 3.80x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | HBAR/USD | 0.05498 | 85.38 | -0.27% | 2.49x | STRONG 73/100 | HIGH 66/100 | Watch |
| 7 | SUI/USD | 0.6749 | 75.55 | -0.07% | 17.95x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | HYPE/USD | 63.39 | 73.14 | +0.44% | 0.66x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 9 | WIF/USD | 0.1368 | 69.43 | -0.73% | 0.99x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 10 | XRP/USD | 0.9519 | 67.88 | -0.00% | 1.15x | WEAK 44/100 | HIGH 68/100 | Watch |
| 11 | ETH/USD | 1702.92 | 66.59 | +0.03% | 1.63x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD | 0.0569115 | 64.83 | -0.01% | 2.00x | MODERATE 52/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.39168 | 98.48 | +0.52% | 3.17x | 7789 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.34999 | 95.49 | +0.32% | 3.80x | 6451 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 44.01 | 93.08 | +0.36% | 7.59x | 14430 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | AKT/USD ⭐ | 0.5071 | 90.77 | +0.30% | 2.77x | 2669 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** DRV/USD, AKT/USD, LTC/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
