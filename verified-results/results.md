# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:20:26.351974+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44652773742
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** c77c7c4777c21616aa8d8e7904db72fb268525e1 (atomic ledger/results publication)
**Ledger generation:** 896 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.7139 | 74.398 | 55.804 | +0.58% | +0.72% | 4.22x | 4.2 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XBT/USD | 62394.4 | 70.076 | 59.876 | +0.78% | +0.54% | 1.75x | 1.1 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.03256 | 67.845 | 53.270 | +0.39% | -0.08% | 9.30x | 3.5 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XMR/USD | 503.59 | 67.731 | 61.610 | +1.23% | +0.81% | 1.21x | 4.0 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XLM/USD | 0.134171 | 61.349 | 60.148 | +1.11% | +0.57% | 0.84x | 5.2 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ADA/USD | 0.15237 | 61.028 | 55.054 | +0.40% | +0.26% | 1.47x | 5.5 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XRP/USD | 0.96598 | 55.602 | 58.617 | +0.70% | +0.58% | 0.41x | 2.6 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1762.26 | 55.058 | 56.447 | +0.39% | +0.49% | 0.62x | 2.6 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SYRUP/USD | 0.09828 | 54.585 | 41.107 | +2.13% | -0.30% | 4.21x | 11.2 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | BCH/USD | 207.32 | 54.469 | 36.509 | +0.52% | +0.59% | 4.05x | 7.7 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 11 | STRK/USD | 0.03181 | 50.797 | 35.167 | +0.38% | +0.13% | 3.25x | 6.3 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 12 | CAP/USD | 0.097399 | 46.229 | 33.753 | +0.81% | +1.01% | 1.74x | 13.0 | 2026-11-20T01:20:18.150276+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 61.610 | 503.59 | +0.81% | 1.21x |
| 2 | XLM/USD | 60.148 | 0.134171 | +0.57% | 0.84x |
| 3 | XBT/USD | 59.876 | 62394.4 | +0.54% | 1.75x |
| 4 | XRP/USD | 58.617 | 0.96598 | +0.58% | 0.41x |
| 5 | ETH/USD | 56.447 | 1762.26 | +0.49% | 0.62x |
| 6 | SUI/USD | 55.804 | 0.7139 | +0.72% | 4.22x |
| 7 | ADA/USD | 55.054 | 0.15237 | +0.26% | 1.47x |
| 8 | LINK/USD | 53.270 | 9.03256 | -0.08% | 9.30x |
| 9 | SYRUP/USD | 41.107 | 0.09828 | -0.30% | 4.21x |
| 10 | BCH/USD | 36.509 | 207.32 | +0.59% | 4.05x |
| 11 | STRK/USD | 35.167 | 0.03181 | +0.13% | 3.25x |
| 12 | CAP/USD | 33.753 | 0.097399 | +1.01% | 1.74x |

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

- Persisted scans: 896; predictions: 7821; observations: 541413.
- Matured sampled outcomes across 1/6/24/48h: 8578; gap abstentions: 16188. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44652773742 · **Generation:** 896 · **Legacy run:** 44652773742
**Main quote time:** 2026-11-20T01:20:26.351974+00:00 · **Legacy report time:** 2026-11-20T01:21:11.084735+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.7139 | 74.40 | +0.72% | 4.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 62394.4 | 70.08 | +0.54% | 1.75x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD | 9.03256 | 67.85 | -0.08% | 9.30x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD ⭐ | 503.59 | 67.73 | +0.81% | 1.21x | STRONG 79/100 | HIGH 62/100 | Watch |
| 5 | XLM/USD | 0.134171 | 61.35 | +0.57% | 0.84x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 6 | ADA/USD ⭐ | 0.15237 | 61.03 | +0.26% | 1.47x | STRONG 86/100 | HIGH 55/100 | Watch |
| 7 | XRP/USD | 0.96598 | 55.60 | +0.58% | 0.41x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD | 1762.26 | 55.06 | +0.49% | 0.62x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 9 | SYRUP/USD | 0.09828 | 54.59 | -0.30% | 4.21x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 10 | BCH/USD | 207.32 | 54.47 | +0.59% | 4.05x | STRONG 82/100 | HIGH 55/100 | Watch |
| 11 | STRK/USD | 0.03181 | 50.80 | +0.13% | 3.25x | STRONG 70/100 | HIGH 60/100 | Watch |
| 12 | CAP/USD | 0.097399 | 46.23 | +1.01% | 1.74x | MODERATE 63/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 62392 | 65.86 | +0.54% | 1.75x | 139506 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.7132 | 64.41 | +0.72% | 4.22x | 5973 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | ICNT/USD | 0.4338 | 59.32 | +1.36% | 2.74x | 7237 | STRONG 80/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD ⭐ | 503.36 | 59.10 | +0.81% | 1.21x | 7968 | STRONG 75/100 | HIGH 62/100 | Watch |
| 5 | XDG/USD | 0.0582467 | 55.62 | +0.53% | 2.43x | 5235 | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD | 42.38 | 52.72 | +0.57% | 1.25x | 12398 | MODERATE 61/100 | HIGH 62/100 | Watch |
| 7 | UNI/USD | 4.9485 | 51.46 | +0.64% | 3.34x | 9034 | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | ADA/USD ⭐ | 0.15237 | 51.19 | +0.26% | 1.47x | 11346 | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | AVAX/USD | 7.004 | 48.66 | +0.33% | 3.17x | 4872 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SUI/USD, XBT/USD, XMR/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
