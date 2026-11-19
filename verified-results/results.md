# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:15:27.764662+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44531513961
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** f6b5bf694c315edc1330a277037f1bc817352ca4 (atomic ledger/results publication)
**Ledger generation:** 780 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LIGHTER/USD | 2.937 | 93.451 | 77.939 | +8.22% | +0.10% | 3.30x | 6.8 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | STRONG 92/100 | HIGH 60/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.963e-06 | 88.899 | 79.754 | +5.79% | -1.17% | 3.28x | 2.5 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | STRONG 74/100 | HIGH 65/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5532 | 87.206 | 72.955 | +6.80% | +0.77% | 2.04x | 7.2 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | STRONG 99/100 | HIGH 67/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 22.872 | 86.222 | 90.730 | +5.54% | -0.15% | 0.62x | 6.1 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XRP/USD | 0.98707 | 84.326 | 69.741 | +2.14% | -0.08% | 2.73x | 0.5 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 6 | HYPE/USD | 68.71 | 72.906 | 73.426 | +2.74% | -0.28% | 1.09x | 1.5 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 943.81 | 72.477 | 78.077 | +3.49% | -0.50% | 0.69x | 2.8 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.3934 | 67.652 | 73.021 | +2.91% | -0.07% | 0.50x | 4.7 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SENT/USD | 0.021855 | 63.755 | 74.596 | +6.07% | -0.78% | 0.30x | 2.3 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | XBT/USD | 63705 | 62.365 | 63.000 | +1.14% | -0.14% | 1.01x | 0.0 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ETH/USD | 1804.33 | 60.515 | 66.635 | +1.67% | +0.07% | 0.36x | 0.1 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.13786 | 57.143 | 56.443 | +0.49% | -0.26% | 1.20x | 3.9 | 2026-11-19T13:15:21.056004+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.730 | 22.872 | -0.15% | 0.62x |
| 2 | PEPE/USD | 79.754 | 3.963e-06 | -1.17% | 3.28x |
| 3 | ZEC/USD | 78.077 | 943.81 | -0.50% | 0.69x |
| 4 | LIGHTER/USD | 77.939 | 2.937 | +0.10% | 3.30x |
| 5 | SENT/USD | 74.596 | 0.021855 | -0.78% | 0.30x |
| 6 | HYPE/USD | 73.426 | 68.71 | -0.28% | 1.09x |
| 7 | NEAR/USD | 73.021 | 3.3934 | -0.07% | 0.50x |
| 8 | AKT/USD | 72.955 | 0.5532 | +0.77% | 2.04x |
| 9 | XRP/USD | 69.741 | 0.98707 | -0.08% | 2.73x |
| 10 | ETH/USD | 66.635 | 1804.33 | +0.07% | 0.36x |
| 11 | XBT/USD | 63.000 | 63705 | -0.14% | 1.01x |
| 12 | XLM/USD | 56.443 | 0.13786 | -0.26% | 1.20x |

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

- Persisted scans: 780; predictions: 6504; observations: 471958.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14952. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44531513961 · **Generation:** 780 · **Legacy run:** 44531513961
**Main quote time:** 2026-11-19T13:15:27.764662+00:00 · **Legacy report time:** 2026-11-19T13:16:19.014460+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.937 | 93.45 | +0.10% | 3.30x | STRONG 100/100 | HIGH 60/100 | Watch |
| 2 | PEPE/USD | 3.963e-06 | 88.90 | -1.17% | 3.28x | STRONG 74/100 | HIGH 65/100 | Watch |
| 3 | AKT/USD | 0.5532 | 87.21 | +0.77% | 2.04x | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 4 | VVV/USD | 22.872 | 86.22 | -0.15% | 0.62x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 5 | XRP/USD | 0.98707 | 84.33 | -0.08% | 2.73x | STRONG 72/100 | HIGH 61/100 | Watch |
| 6 | HYPE/USD | 68.71 | 72.91 | -0.28% | 1.09x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 943.81 | 72.48 | -0.50% | 0.69x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 8 | NEAR/USD | 3.3934 | 67.65 | -0.07% | 0.50x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | SENT/USD | 0.021855 | 63.75 | -0.78% | 0.30x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |
| 10 | XBT/USD | 63705 | 62.36 | -0.14% | 1.01x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | ETH/USD | 1804.33 | 60.52 | +0.07% | 0.36x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD | 0.13786 | 57.14 | -0.26% | 1.20x | WEAK 39/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.934 | 82.11 | +0.10% | 3.30x | 3818 | STRONG 91/100 | HIGH 66/100 | Watch |
| 2 | LUNA/USD | 4.556e-05 | 81.93 | +0.29% | 5.12x | 4680 | STRONG 81/100 | VERY_HIGH 72/100 | Watch |
| 3 | ADA/USD | 0.155225 | 76.26 | +0.32% | 1.14x | 11874 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LIGHTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
