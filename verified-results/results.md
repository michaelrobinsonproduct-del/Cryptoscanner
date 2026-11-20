# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:15:30.174919+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44652139801
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 9d1b31a7ab7af692960e779ec1f08f11d2562da1 (atomic ledger/results publication)
**Ledger generation:** 895 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.712 | 67.466 | 53.664 | +0.31% | +0.25% | 2.25x | 4.2 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XBT/USD | 62264.2 | 67.026 | 58.130 | +0.57% | +0.35% | 1.71x | 1.7 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XLM/USD | 0.133765 | 60.270 | 59.010 | +0.80% | +0.12% | 1.07x | 3.2 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XMR/USD | 501.29 | 57.484 | 59.263 | +0.77% | +0.25% | 0.70x | 2.2 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XRP/USD | 0.96461 | 53.309 | 58.445 | +0.56% | +0.41% | 0.28x | 0.9 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.10016 | 52.986 | 38.549 | +0.92% | +1.17% | 1.86x | 19.0 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.4312 | 43.417 | 34.337 | +1.20% | +1.61% | 1.11x | 23.3 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | CAP/USD | 0.097002 | 42.582 | 29.740 | +0.40% | +0.28% | 2.15x | 15.3 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | STRONG 71/100 | HIGH 66/100 | Watch | WATCH |
| 9 | BAT/USD | 0.0888 | 38.818 | 21.792 | +0.42% | +0.41% | 3.34x | 24.8 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | HBAR/USD | 0.054 | 32.074 | 38.212 | +0.45% | +0.33% | 0.22x | 3.7 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AKT/USD | 0.536 | 28.655 | 30.547 | +0.47% | +0.60% | 0.51x | 11.2 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | RARE/USD | 0.01332 | 14.215 | 23.144 | +0.45% | -3.55% | 1.88x | 22.5 | 2026-11-20T01:15:24.242928+00:00 | Not calibrated | WEAK 17/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 59.263 | 501.29 | +0.25% | 0.70x |
| 2 | XLM/USD | 59.010 | 0.133765 | +0.12% | 1.07x |
| 3 | XRP/USD | 58.445 | 0.96461 | +0.41% | 0.28x |
| 4 | XBT/USD | 58.130 | 62264.2 | +0.35% | 1.71x |
| 5 | SUI/USD | 53.664 | 0.712 | +0.25% | 2.25x |
| 6 | USELESS/USD | 38.549 | 0.10016 | +1.17% | 1.86x |
| 7 | HBAR/USD | 38.212 | 0.054 | +0.33% | 0.22x |
| 8 | ICNT/USD | 34.337 | 0.4312 | +1.61% | 1.11x |
| 9 | AKT/USD | 30.547 | 0.536 | +0.60% | 0.51x |
| 10 | CAP/USD | 29.740 | 0.097002 | +0.28% | 2.15x |
| 11 | RARE/USD | 23.144 | 0.01332 | -3.55% | 1.88x |
| 12 | BAT/USD | 21.792 | 0.0888 | +0.41% | 3.34x |

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

- Persisted scans: 895; predictions: 7809; observations: 540810.
- Matured sampled outcomes across 1/6/24/48h: 8569; gap abstentions: 16171. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44652139801 · **Generation:** 895 · **Legacy run:** 44652139801
**Main quote time:** 2026-11-20T01:15:30.174919+00:00 · **Legacy report time:** 2026-11-20T01:16:35.552778+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.712 | 67.47 | +0.25% | 2.25x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 62264.2 | 67.03 | +0.35% | 1.71x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 3 | XLM/USD ⭐ | 0.133765 | 60.27 | +0.12% | 1.07x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 4 | XMR/USD | 501.29 | 57.48 | +0.25% | 0.70x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 5 | XRP/USD | 0.96461 | 53.31 | +0.41% | 0.28x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | USELESS/USD ⭐ | 0.10016 | 52.99 | +1.17% | 1.86x | STRONG 76/100 | HIGH 61/100 | Consider small entry |
| 7 | ICNT/USD ⭐ | 0.4312 | 43.42 | +1.61% | 1.11x | MODERATE 57/100 | VERY_HIGH 74/100 | Watch |
| 8 | CAP/USD | 0.097002 | 42.58 | +0.28% | 2.15x | STRONG 71/100 | HIGH 66/100 | Watch |
| 9 | BAT/USD | 0.0888 | 38.82 | +0.41% | 3.34x | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |
| 10 | HBAR/USD | 0.054 | 32.07 | +0.33% | 0.22x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 11 | AKT/USD | 0.536 | 28.65 | +0.60% | 0.51x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 12 | RARE/USD | 0.01332 | 14.21 | -3.55% | 1.88x | WEAK 17/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 62358.1 | 64.49 | +0.35% | 1.71x | 139591 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD | 73.15 | 59.16 | +0.19% | 3.95x | 37244 | STRONG 75/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD | 0.0582357 | 56.95 | +0.27% | 3.28x | 5251 | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD ⭐ | 0.7126 | 56.11 | +0.25% | 2.25x | 5944 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 5 | XLM/USD ⭐ | 0.13377 | 53.94 | +0.12% | 1.07x | 10393 | MODERATE 62/100 | HIGH 62/100 | Watch |
| 6 | USELESS/USD ⭐ | 0.10062 | 52.51 | +1.17% | 1.86x | 7739 | STRONG 71/100 | HIGH 67/100 | Watch |
| 7 | ICNT/USD ⭐ | 0.4333 | 52.11 | +1.61% | 1.11x | 7227 | MODERATE 61/100 | VERY_HIGH 74/100 | Watch |
| 8 | LTC/USD | 42.38 | 51.37 | +0.17% | 1.22x | 12396 | MODERATE 51/100 | HIGH 62/100 | Watch |
| 9 | UNI/USD | 4.9544 | 48.88 | +0.43% | 2.34x | 9021 | STRONG 79/100 | HIGH 55/100 | Watch |
| 10 | ADA/USD | 0.152364 | 48.33 | +0.05% | 1.21x | 11356 | MODERATE 49/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SUI/USD, XBT/USD, XLM/USD, USELESS/USD, ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
