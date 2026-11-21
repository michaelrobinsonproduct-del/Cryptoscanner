# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T13:30:42.200231+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44909109146
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 623cd65d7ceddf12d84fca7381606f8433b70201 (atomic ledger/results publication)
**Ledger generation:** 1139 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ETH/USD | 1674.04 | 90.620 | 78.445 | +3.38% | +0.34% | 2.05x | 0.4 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.6124 | 89.684 | 70.158 | +3.25% | +2.19% | 1.86x | 15.2 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 22.697 | 84.245 | 94.048 | +9.44% | -1.39% | 0.71x | 11.9 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | WEAK 42/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | TAO/USD | 185.5715 | 83.358 | 70.064 | +2.81% | +0.26% | 2.20x | 9.1 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | USELESS/USD | 0.07866 | 77.143 | 60.165 | +5.58% | +1.78% | 1.81x | 38.1 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 6 | XRP/USD | 0.91259 | 75.115 | 57.003 | +0.43% | +0.62% | 2.67x | 2.0 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ZEC/USD | 777.88 | 72.361 | 69.458 | +2.63% | -0.18% | 1.38x | 8.0 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 8 | CT/USD | 0.1304 | 72.351 | 68.843 | +7.68% | +1.32% | 0.69x | 15.3 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | XMR/USD | 470.7 | 67.518 | 74.026 | +3.16% | +0.30% | 0.20x | 6.2 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PAXG/USD | 3541.48 | 67.480 | 56.567 | +0.28% | +0.23% | 1.97x | 0.8 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0545247 | 66.669 | 58.193 | +0.46% | +0.43% | 1.63x | 0.1 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XBT/USD | 59492.1 | 63.421 | 63.154 | +1.17% | +0.54% | 0.76x | 0.0 | 2026-11-21T13:30:35.820837+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.048 | 22.697 | -1.39% | 0.71x |
| 2 | ETH/USD | 78.445 | 1674.04 | +0.34% | 2.05x |
| 3 | XMR/USD | 74.026 | 470.7 | +0.30% | 0.20x |
| 4 | UNI/USD | 70.158 | 4.6124 | +2.19% | 1.86x |
| 5 | TAO/USD | 70.064 | 185.5715 | +0.26% | 2.20x |
| 6 | ZEC/USD | 69.458 | 777.88 | -0.18% | 1.38x |
| 7 | CT/USD | 68.843 | 0.1304 | +1.32% | 0.69x |
| 8 | XBT/USD | 63.154 | 59492.1 | +0.54% | 0.76x |
| 9 | USELESS/USD | 60.165 | 0.07866 | +1.78% | 1.81x |
| 10 | XDG/USD | 58.193 | 0.0545247 | +0.43% | 1.63x |
| 11 | XRP/USD | 57.003 | 0.91259 | +0.62% | 2.67x |
| 12 | PAXG/USD | 56.567 | 3541.48 | +0.23% | 1.97x |

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

- Persisted scans: 1139; predictions: 8977; observations: 688871.
- Matured sampled outcomes across 1/6/24/48h: 11766; gap abstentions: 20390. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44909109146 · **Generation:** 1139 · **Legacy run:** 44909109146
**Main quote time:** 2026-11-21T13:30:42.200231+00:00 · **Legacy report time:** 2026-11-21T13:31:22.590448+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1674.04 | 90.62 | +0.34% | 2.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.6124 | 89.68 | +2.19% | 1.86x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 3 | VVV/USD | 22.697 | 84.24 | -1.39% | 0.71x | WEAK 42/100 | EXTREME 86/100 | Do nothing |
| 4 | TAO/USD ⭐ | 185.5715 | 83.36 | +0.26% | 2.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | USELESS/USD ⭐ | 0.07866 | 77.14 | +1.78% | 1.81x | STRONG 79/100 | HIGH 67/100 | Consider small entry |
| 6 | XRP/USD | 0.91259 | 75.11 | +0.62% | 2.67x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 7 | ZEC/USD | 777.88 | 72.36 | -0.18% | 1.38x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 8 | CT/USD | 0.1304 | 72.35 | +1.32% | 0.69x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 9 | XMR/USD | 470.7 | 67.52 | +0.30% | 0.20x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 10 | PAXG/USD | 3541.48 | 67.48 | +0.23% | 1.97x | STRONG 79/100 | HIGH 55/100 | Watch |
| 11 | XDG/USD | 0.0545247 | 66.67 | +0.43% | 1.63x | STRONG 78/100 | HIGH 55/100 | Watch |
| 12 | XBT/USD | 59492.1 | 63.42 | +0.54% | 0.76x | MODERATE 62/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1674.1 | 97.69 | +0.34% | 2.05x | 100604 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.6159 | 86.94 | +2.19% | 1.86x | 12881 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | USELESS/USD ⭐ | 0.0783 | 84.63 | +1.78% | 1.81x | 5053 | STRONG 87/100 | HIGH 67/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 185.5715 | 76.34 | +0.26% | 2.20x | 16570 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ETH/USD, UNI/USD, TAO/USD, USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
