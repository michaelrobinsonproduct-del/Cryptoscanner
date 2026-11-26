# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T08:56:28.878702+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45787157925
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f6daf421b21c9d33d805eac3a4f48ede8b8d275e (atomic ledger/results publication)
**Ledger generation:** 1839 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.237 | 89.337 | 72.076 | +4.75% | +0.45% | 4.22x | 8.0 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.24102 | 86.586 | 69.186 | +2.17% | +0.48% | 20.20x | 2.0 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.95703 | 85.745 | 69.986 | +2.19% | +0.15% | 3.11x | 0.6 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.14842 | 82.731 | 65.807 | +1.82% | +0.38% | 2.63x | 3.8 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | QNT/USD | 148.2 | 80.162 | 62.551 | +2.35% | +0.52% | 3.59x | 6.1 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | LTC/USD | 43.6 | 79.319 | 68.440 | +2.08% | +0.44% | 1.87x | 2.3 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XBT/USD | 60896.5 | 77.890 | 61.113 | +0.87% | +0.36% | 3.08x | 0.0 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | HBAR/USD | 0.05399 | 76.373 | 60.723 | +3.63% | +0.13% | 3.30x | 3.7 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 71.07 | 74.480 | 61.059 | +0.97% | +0.18% | 2.25x | 1.4 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SYRUP/USD | 0.07272 | 68.197 | 67.042 | +9.73% | -0.07% | 1.15x | 20.6 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | WEAK 34/100 | EXTREME 85/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1698.89 | 63.680 | 57.393 | +0.50% | +0.43% | 1.41x | 2.2 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BNB/USD | 554.84 | 53.777 | 38.073 | +0.33% | +0.14% | 5.95x | 2.3 | 2026-11-26T08:56:20.158238+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 72.076 | 6.237 | +0.45% | 4.22x |
| 2 | XRP/USD | 69.986 | 0.95703 | +0.15% | 3.11x |
| 3 | LINK/USD | 69.186 | 9.24102 | +0.48% | 20.20x |
| 4 | LTC/USD | 68.440 | 43.6 | +0.44% | 1.87x |
| 5 | SYRUP/USD | 67.042 | 0.07272 | -0.07% | 1.15x |
| 6 | ADA/USD | 65.807 | 0.14842 | +0.38% | 2.63x |
| 7 | QNT/USD | 62.551 | 148.2 | +0.52% | 3.59x |
| 8 | XBT/USD | 61.113 | 60896.5 | +0.36% | 3.08x |
| 9 | SOL/USD | 61.059 | 71.07 | +0.18% | 2.25x |
| 10 | HBAR/USD | 60.723 | 0.05399 | +0.13% | 3.30x |
| 11 | ETH/USD | 57.393 | 1698.89 | +0.43% | 1.41x |
| 12 | BNB/USD | 38.073 | 554.84 | +0.14% | 5.95x |

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

- Persisted scans: 1839; predictions: 15803; observations: 1114993.
- Matured sampled outcomes across 1/6/24/48h: 34238; gap abstentions: 24385. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45787157925 · **Generation:** 1839 · **Legacy run:** 45787157925
**Main quote time:** 2026-11-26T08:56:28.878702+00:00 · **Legacy report time:** 2026-11-26T08:57:38.069248+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.237 | 89.34 | +0.45% | 4.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.24102 | 86.59 | +0.48% | 20.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95703 | 85.75 | +0.15% | 3.11x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD ⭐ | 0.14842 | 82.73 | +0.38% | 2.63x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | QNT/USD | 148.2 | 80.16 | +0.52% | 3.59x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 6 | LTC/USD ⭐ | 43.6 | 79.32 | +0.44% | 1.87x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD | 60896.5 | 77.89 | +0.36% | 3.08x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 8 | HBAR/USD ⭐ | 0.05399 | 76.37 | +0.13% | 3.30x | STRONG 93/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD | 71.07 | 74.48 | +0.18% | 2.25x | STRONG 82/100 | HIGH 55/100 | Watch |
| 10 | SYRUP/USD | 0.07272 | 68.20 | -0.07% | 1.15x | WEAK 34/100 | EXTREME 85/100 | Do nothing |
| 11 | ETH/USD | 1698.89 | 63.68 | +0.43% | 1.41x | STRONG 77/100 | HIGH 55/100 | Watch |
| 12 | BNB/USD | 554.84 | 53.78 | +0.14% | 5.95x | STRONG 72/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05405 | 87.21 | +0.13% | 3.30x | 6297 | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | INJ/USD ⭐ | 6.237 | 87.04 | +0.45% | 4.22x | 6815 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.9565 | 85.80 | +0.15% | 3.11x | 41128 | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD ⭐ | 9.24102 | 81.49 | +0.48% | 20.20x | 9234 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | LTC/USD ⭐ | 43.59 | 76.92 | +0.44% | 1.87x | 15505 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 6 | ADA/USD ⭐ | 0.148364 | 75.62 | +0.38% | 2.63x | 12468 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SKY/USD | 0.04368 | 75.07 | +0.21% | 1.23x | 4131 | STRONG 73/100 | HIGH 67/100 | Watch |

**Same-run overlap:** INJ/USD, LINK/USD, XRP/USD, ADA/USD, LTC/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
