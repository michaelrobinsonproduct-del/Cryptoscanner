# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T18:41:00.336710+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44936725167
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 4dfab679cf9d6ceb737805bc2fe2a51c5952e994 (atomic ledger/results publication)
**Ledger generation:** 1171 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7196 | 107.887 | 93.173 | +5.65% | -0.06% | 2.71x | 2.8 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 486.95 | 98.203 | 94.960 | +6.72% | +1.31% | 0.67x | 10.1 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ETH/USD | 1682.21 | 97.017 | 82.156 | +3.88% | -0.03% | 2.58x | 0.1 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZEC/USD | 791.92 | 93.235 | 85.148 | +4.49% | +0.49% | 1.57x | 2.5 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NIGHT/USD | 0.04529 | 86.753 | 86.409 | +7.27% | -0.66% | 1.36x | 13.3 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 6 | LINK/USD | 8.62582 | 78.593 | 62.207 | +1.13% | +0.28% | 7.99x | 1.4 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | TAO/USD | 186.3847 | 77.537 | 75.127 | +3.26% | +0.23% | 1.13x | 5.3 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93208 | 76.593 | 72.573 | +2.57% | +0.16% | 1.32x | 0.9 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 70.73 | 75.619 | 74.872 | +2.94% | +0.11% | 1.02x | 1.4 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0553397 | 75.174 | 68.587 | +1.96% | +0.36% | 1.48x | 0.3 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XBT/USD | 60087.3 | 66.680 | 70.239 | +2.18% | -0.00% | 0.64x | 0.0 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | TRX/USD | 0.304734 | 65.130 | 53.873 | +1.07% | -0.00% | 2.13x | 0.0 | 2026-11-21T18:40:54.033314+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.960 | 486.95 | +1.31% | 0.67x |
| 2 | UNI/USD | 93.173 | 4.7196 | -0.06% | 2.71x |
| 3 | NIGHT/USD | 86.409 | 0.04529 | -0.66% | 1.36x |
| 4 | ZEC/USD | 85.148 | 791.92 | +0.49% | 1.57x |
| 5 | ETH/USD | 82.156 | 1682.21 | -0.03% | 2.58x |
| 6 | TAO/USD | 75.127 | 186.3847 | +0.23% | 1.13x |
| 7 | SOL/USD | 74.872 | 70.73 | +0.11% | 1.02x |
| 8 | XRP/USD | 72.573 | 0.93208 | +0.16% | 1.32x |
| 9 | XBT/USD | 70.239 | 60087.3 | -0.00% | 0.64x |
| 10 | XDG/USD | 68.587 | 0.0553397 | +0.36% | 1.48x |
| 11 | LINK/USD | 62.207 | 8.62582 | +0.28% | 7.99x |
| 12 | TRX/USD | 53.873 | 0.304734 | -0.00% | 2.13x |

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

- Persisted scans: 1171; predictions: 9361; observations: 708327.
- Matured sampled outcomes across 1/6/24/48h: 12368; gap abstentions: 21121. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44936725167 · **Generation:** 1171 · **Legacy run:** 44936725167
**Main quote time:** 2026-11-21T18:41:00.336710+00:00 · **Legacy report time:** 2026-11-21T18:42:04.415826+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.7196 | 107.89 | -0.06% | 2.71x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 486.95 | 98.20 | +1.31% | 0.67x | STRONG 74/100 | VERY_HIGH 76/100 | Watch |
| 3 | ETH/USD | 1682.21 | 97.02 | -0.03% | 2.58x | STRONG 79/100 | HIGH 61/100 | Watch |
| 4 | ZEC/USD ⭐ | 791.92 | 93.24 | +0.49% | 1.57x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NIGHT/USD | 0.04529 | 86.75 | -0.66% | 1.36x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 6 | LINK/USD | 8.62582 | 78.59 | +0.28% | 7.99x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 7 | TAO/USD ⭐ | 186.3847 | 77.54 | +0.23% | 1.13x | STRONG 84/100 | HIGH 62/100 | Watch |
| 8 | XRP/USD ⭐ | 0.93208 | 76.59 | +0.16% | 1.32x | STRONG 83/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD ⭐ | 70.73 | 75.62 | +0.11% | 1.02x | STRONG 73/100 | HIGH 62/100 | Watch |
| 10 | XDG/USD ⭐ | 0.0553397 | 75.17 | +0.36% | 1.48x | STRONG 93/100 | HIGH 55/100 | Watch |
| 11 | XBT/USD | 60087.3 | 66.68 | -0.00% | 0.64x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 12 | TRX/USD | 0.304734 | 65.13 | -0.00% | 2.13x | MODERATE 63/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 791.94 | 98.42 | +0.49% | 1.57x | 46177 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 186.3847 | 85.17 | +0.23% | 1.13x | 12517 | STRONG 88/100 | HIGH 62/100 | Watch |
| 3 | SOL/USD ⭐ | 70.72 | 84.69 | +0.11% | 1.02x | 51869 | STRONG 77/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93186 | 82.40 | +0.16% | 1.32x | 59731 | STRONG 86/100 | HIGH 55/100 | Watch |
| 5 | ZBCN/USD | 0.00166 | 77.55 | +0.18% | 2.39x | 3405 | MODERATE 69/100 | VERY_HIGH 72/100 | Watch |
| 6 | XDG/USD ⭐ | 0.0552658 | 76.36 | +0.36% | 1.48x | 16049 | STRONG 93/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, TAO/USD, XRP/USD, SOL/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
