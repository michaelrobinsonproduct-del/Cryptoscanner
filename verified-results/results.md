# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:10:26.085943+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44651498468
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 2d80204619a98ce688ebda433079cfd9db84d2ca (atomic ledger/results publication)
**Ledger generation:** 894 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.7138 | 74.965 | 56.225 | +0.56% | +0.75% | 3.58x | 2.8 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XLM/USD | 0.134 | 70.362 | 60.512 | +0.98% | +0.58% | 1.69x | 2.7 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.0419 | 70.362 | 52.022 | +0.49% | +0.67% | 10.10x | 7.5 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XBT/USD | 62332.5 | 67.811 | 59.729 | +0.68% | +0.73% | 1.44x | 0.0 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 5 | UNI/USD | 4.9625 | 66.233 | 50.260 | +0.44% | +1.10% | 2.05x | 4.2 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0583099 | 65.853 | 47.059 | +0.32% | +0.76% | 2.86x | 0.0 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XMR/USD | 502.17 | 62.133 | 57.512 | +0.94% | +0.62% | 1.15x | 8.2 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ADA/USD | 0.152583 | 60.025 | 55.152 | +0.54% | +0.62% | 1.18x | 7.3 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.2211 | 57.110 | 54.712 | +0.47% | +1.15% | 0.67x | 7.2 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1762.84 | 56.453 | 57.728 | +0.43% | +0.82% | 0.46x | 0.5 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XRP/USD | 0.9655 | 55.267 | 59.509 | +0.65% | +0.79% | 0.18x | 0.1 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AVAX/USD | 7.009 | 50.163 | 41.889 | +0.29% | +0.92% | 1.37x | 8.6 | 2026-11-20T01:10:18.165315+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 60.512 | 0.134 | +0.58% | 1.69x |
| 2 | XBT/USD | 59.729 | 62332.5 | +0.73% | 1.44x |
| 3 | XRP/USD | 59.509 | 0.9655 | +0.79% | 0.18x |
| 4 | ETH/USD | 57.728 | 1762.84 | +0.82% | 0.46x |
| 5 | XMR/USD | 57.512 | 502.17 | +0.62% | 1.15x |
| 6 | SUI/USD | 56.225 | 0.7138 | +0.75% | 3.58x |
| 7 | ADA/USD | 55.152 | 0.152583 | +0.62% | 1.18x |
| 8 | NEAR/USD | 54.712 | 3.2211 | +1.15% | 0.67x |
| 9 | LINK/USD | 52.022 | 9.0419 | +0.67% | 10.10x |
| 10 | UNI/USD | 50.260 | 4.9625 | +1.10% | 2.05x |
| 11 | XDG/USD | 47.059 | 0.0583099 | +0.76% | 2.86x |
| 12 | AVAX/USD | 41.889 | 7.009 | +0.92% | 1.37x |

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

- Persisted scans: 894; predictions: 7797; observations: 540207.
- Matured sampled outcomes across 1/6/24/48h: 8546; gap abstentions: 16153. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44651498468 · **Generation:** 894 · **Legacy run:** 44651498468
**Main quote time:** 2026-11-20T01:10:26.085943+00:00 · **Legacy report time:** 2026-11-20T01:11:12.622542+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.7138 | 74.97 | +0.75% | 3.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XLM/USD ⭐ | 0.134 | 70.36 | +0.58% | 1.69x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.0419 | 70.36 | +0.67% | 10.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 62332.5 | 67.81 | +0.73% | 1.44x | STRONG 89/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD ⭐ | 4.9625 | 66.23 | +1.10% | 2.05x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 6 | XDG/USD | 0.0583099 | 65.85 | +0.76% | 2.86x | STRONG 88/100 | HIGH 55/100 | Watch |
| 7 | XMR/USD ⭐ | 502.17 | 62.13 | +0.62% | 1.15x | STRONG 76/100 | HIGH 62/100 | Watch |
| 8 | ADA/USD ⭐ | 0.152583 | 60.02 | +0.62% | 1.18x | STRONG 75/100 | HIGH 62/100 | Watch |
| 9 | NEAR/USD | 3.2211 | 57.11 | +1.15% | 0.67x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1762.84 | 56.45 | +0.82% | 0.46x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | XRP/USD | 0.9655 | 55.27 | +0.79% | 0.18x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | AVAX/USD | 7.009 | 50.16 | +0.92% | 1.37x | STRONG 70/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 62269 | 62.82 | +0.73% | 1.44x | 139643 | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | SYRUP/USD | 0.09885 | 62.47 | +1.27% | 2.40x | 2317 | STRONG 81/100 | HIGH 66/100 | Watch |
| 3 | SUI/USD ⭐ | 0.7123 | 60.04 | +0.75% | 3.58x | 5949 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | XLM/USD ⭐ | 0.134 | 56.15 | +0.58% | 1.69x | 10410 | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD ⭐ | 501.32 | 56.15 | +0.62% | 1.15x | 7852 | STRONG 73/100 | HIGH 62/100 | Watch |
| 6 | LINK/USD ⭐ | 9.02996 | 55.79 | +0.67% | 10.10x | 6288 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 7 | USELESS/USD | 0.10055 | 53.44 | +2.11% | 1.61x | 7669 | MODERATE 62/100 | HIGH 67/100 | Watch |
| 8 | LTC/USD | 42.33 | 51.41 | +0.62% | 1.24x | 12414 | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | ADA/USD ⭐ | 0.152348 | 50.94 | +0.62% | 1.18x | 11388 | STRONG 70/100 | HIGH 62/100 | Watch |
| 10 | UNI/USD ⭐ | 4.9533 | 47.80 | +1.10% | 2.05x | 9027 | STRONG 89/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SUI/USD, XLM/USD, LINK/USD, XBT/USD, UNI/USD, XMR/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
