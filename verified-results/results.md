# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T02:23:01.184837+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45311530629
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e6633e764659136f1532e9193709fa122a0733b4 (atomic ledger/results publication)
**Ledger generation:** 1512 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01205 | 93.711 | 65.967 | +4.60% | +2.55% | 11.06x | 8.3 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | AI/USD | 0.01603 | 71.018 | 61.682 | +5.25% | +1.64% | 1.11x | 12.5 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | LINK/USD | 9.04234 | 70.512 | 54.597 | +0.42% | +0.18% | 3.29x | 6.6 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PAXG/USD | 3642.68 | 68.115 | 51.886 | +0.60% | +0.25% | 7.07x | 1.4 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AAVE/USD | 97.83 | 67.645 | 50.133 | +0.80% | +0.50% | 4.40x | 5.1 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0564825 | 65.876 | 55.009 | +0.32% | +0.44% | 1.87x | 4.4 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04867 | 64.850 | 54.399 | +1.08% | -0.12% | 2.11x | 6.2 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.94409 | 63.856 | 57.866 | +0.50% | -0.01% | 1.60x | 1.3 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 9 | BCH/USD | 200.96 | 56.921 | 39.775 | +0.32% | +0.43% | 3.45x | 7.5 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.445e-06 | 56.529 | 50.365 | +0.67% | +0.26% | 1.49x | 5.8 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 11 | BLESS/USD | 0.014541 | 54.737 | 61.130 | +7.95% | -1.30% | 1.01x | 42.3 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | WEAK 22/100 | EXTREME 94/100 | Do nothing | WATCH |
| 12 | XAUT/USD | 3642.9 | 53.701 | 37.711 | +0.65% | +0.20% | 7.01x | 0.3 | 2026-11-24T02:22:54.504643+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 65.967 | 0.01205 | +2.55% | 11.06x |
| 2 | AI/USD | 61.682 | 0.01603 | +1.64% | 1.11x |
| 3 | BLESS/USD | 61.130 | 0.014541 | -1.30% | 1.01x |
| 4 | XRP/USD | 57.866 | 0.94409 | -0.01% | 1.60x |
| 5 | XDG/USD | 55.009 | 0.0564825 | +0.44% | 1.87x |
| 6 | LINK/USD | 54.597 | 9.04234 | +0.18% | 3.29x |
| 7 | NIGHT/USD | 54.399 | 0.04867 | -0.12% | 2.11x |
| 8 | PAXG/USD | 51.886 | 3642.68 | +0.25% | 7.07x |
| 9 | PEPE/USD | 50.365 | 3.445e-06 | +0.26% | 1.49x |
| 10 | AAVE/USD | 50.133 | 97.83 | +0.50% | 4.40x |
| 11 | BCH/USD | 39.775 | 200.96 | +0.43% | 3.45x |
| 12 | XAUT/USD | 37.711 | 3642.9 | +0.20% | 7.01x |

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

- Persisted scans: 1512; predictions: 12901; observations: 915909.
- Matured sampled outcomes across 1/6/24/48h: 23825; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45311530629 · **Generation:** 1512 · **Legacy run:** 45311530629
**Main quote time:** 2026-11-24T02:23:01.184837+00:00 · **Legacy report time:** 2026-11-24T02:24:00.959314+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01205 | 93.71 | +2.55% | 11.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AI/USD ⭐ | 0.01603 | 71.02 | +1.64% | 1.11x | STRONG 76/100 | VERY_HIGH 80/100 | Watch |
| 3 | LINK/USD ⭐ | 9.04234 | 70.51 | +0.18% | 3.29x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | PAXG/USD ⭐ | 3642.68 | 68.12 | +0.25% | 7.07x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 5 | AAVE/USD ⭐ | 97.83 | 67.64 | +0.50% | 4.40x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 6 | XDG/USD ⭐ | 0.0564825 | 65.88 | +0.44% | 1.87x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 7 | NIGHT/USD | 0.04867 | 64.85 | -0.12% | 2.11x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.94409 | 63.86 | -0.01% | 1.60x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 9 | BCH/USD | 200.96 | 56.92 | +0.43% | 3.45x | STRONG 83/100 | HIGH 55/100 | Watch |
| 10 | PEPE/USD ⭐ | 3.445e-06 | 56.53 | +0.26% | 1.49x | STRONG 83/100 | HIGH 55/100 | Watch |
| 11 | BLESS/USD | 0.014541 | 54.74 | -1.30% | 1.01x | WEAK 22/100 | EXTREME 94/100 | Do nothing |
| 12 | XAUT/USD ⭐ | 3642.9 | 53.70 | +0.20% | 7.01x | STRONG 82/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01201 | 90.38 | +2.55% | 11.06x | 6960 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AI/USD ⭐ | 0.01625 | 76.06 | +1.64% | 1.11x | 2688 | STRONG 78/100 | VERY_HIGH 80/100 | Watch |
| 3 | PAXG/USD ⭐ | 3639.68 | 60.29 | +0.25% | 7.07x | 5814 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | XDG/USD ⭐ | 0.0564892 | 59.33 | +0.44% | 1.87x | 10644 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.02754 | 54.75 | +0.18% | 3.29x | 8718 | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | AAVE/USD ⭐ | 97.83 | 54.12 | +0.50% | 4.40x | 6332 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 7 | XAUT/USD ⭐ | 3639.2 | 47.51 | +0.20% | 7.01x | 1906 | STRONG 79/100 | HIGH 60/100 | Watch |
| 8 | PEPE/USD ⭐ | 3.443e-06 | 46.63 | +0.26% | 1.49x | 9128 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** MON/USD, AI/USD, LINK/USD, PAXG/USD, AAVE/USD, XDG/USD, PEPE/USD, XAUT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
