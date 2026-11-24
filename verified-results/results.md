# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T08:51:37.732448+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45359499320
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0ed08671070610896aa2db1789fd24e68651b446 (atomic ledger/results publication)
**Ledger generation:** 1552 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.537e-06 | 83.096 | 69.871 | +3.36% | +0.17% | 2.24x | 8.5 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 498.42 | 76.700 | 64.325 | +2.55% | +0.62% | 1.93x | 17.1 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 63.96 | 76.599 | 57.738 | +0.50% | +0.77% | 3.95x | 1.6 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 41.61 | 70.768 | 55.808 | +0.46% | +0.65% | 2.17x | 4.8 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 25.161 | 70.639 | 71.445 | +2.92% | +0.06% | 0.89x | 7.9 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.629e-05 | 70.108 | 56.331 | +6.49% | +1.27% | 1.74x | 41.5 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9933 | 63.980 | 56.504 | +0.41% | +0.67% | 1.41x | 2.7 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LINK/USD | 9.08493 | 57.491 | 59.027 | +0.89% | +0.74% | 0.48x | 4.4 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94332 | 55.895 | 57.610 | +0.42% | +0.42% | 0.62x | 0.6 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | DOT/USD | 0.6788 | 52.466 | 35.472 | +0.49% | +0.40% | 6.32x | 4.4 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 11 | NIGHT/USD | 0.04841 | 51.517 | 49.625 | +0.54% | -0.19% | 1.28x | 6.2 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | WEAK 36/100 | HIGH 61/100 | Watch | WATCH |
| 12 | WLD/USD | 0.2407 | 42.047 | 38.273 | +1.01% | +0.50% | 1.13x | 8.3 | 2026-11-24T08:51:30.142959+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 71.445 | 25.161 | +0.06% | 0.89x |
| 2 | PEPE/USD | 69.871 | 3.537e-06 | +0.17% | 2.24x |
| 3 | XMR/USD | 64.325 | 498.42 | +0.62% | 1.93x |
| 4 | LINK/USD | 59.027 | 9.08493 | +0.74% | 0.48x |
| 5 | HYPE/USD | 57.738 | 63.96 | +0.77% | 3.95x |
| 6 | XRP/USD | 57.610 | 0.94332 | +0.42% | 0.62x |
| 7 | NEAR/USD | 56.504 | 2.9933 | +0.67% | 1.41x |
| 8 | LUNA/USD | 56.331 | 4.629e-05 | +1.27% | 1.74x |
| 9 | LTC/USD | 55.808 | 41.61 | +0.65% | 2.17x |
| 10 | NIGHT/USD | 49.625 | 0.04841 | -0.19% | 1.28x |
| 11 | WLD/USD | 38.273 | 0.2407 | +0.50% | 1.13x |
| 12 | DOT/USD | 35.472 | 0.6788 | +0.40% | 6.32x |

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

- Persisted scans: 1552; predictions: 13356; observations: 940266.
- Matured sampled outcomes across 1/6/24/48h: 25304; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45359499320 · **Generation:** 1552 · **Legacy run:** 45359499320
**Main quote time:** 2026-11-24T08:51:37.732448+00:00 · **Legacy report time:** 2026-11-24T08:52:28.340950+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.537e-06 | 83.10 | +0.17% | 2.24x | STRONG 97/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 498.42 | 76.70 | +0.62% | 1.93x | STRONG 88/100 | HIGH 61/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 63.96 | 76.60 | +0.77% | 3.95x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD | 41.61 | 70.77 | +0.65% | 2.17x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD | 25.161 | 70.64 | +0.06% | 0.89x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | LUNA/USD ⭐ | 4.629e-05 | 70.11 | +1.27% | 1.74x | STRONG 75/100 | VERY_HIGH 82/100 | Watch |
| 7 | NEAR/USD | 2.9933 | 63.98 | +0.67% | 1.41x | STRONG 77/100 | HIGH 55/100 | Watch |
| 8 | LINK/USD | 9.08493 | 57.49 | +0.74% | 0.48x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.94332 | 55.90 | +0.42% | 0.62x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 10 | DOT/USD | 0.6788 | 52.47 | +0.40% | 6.32x | STRONG 81/100 | HIGH 60/100 | Watch |
| 11 | NIGHT/USD | 0.04841 | 51.52 | -0.19% | 1.28x | WEAK 36/100 | HIGH 61/100 | Watch |
| 12 | WLD/USD | 0.2407 | 42.05 | +0.50% | 1.13x | MODERATE 56/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD | 0.00921 | 85.16 | +1.86% | 3.22x | 4608 | STRONG 88/100 | VERY_HIGH 72/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.534e-06 | 79.08 | +0.17% | 2.24x | 9168 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | BAT/USD | 0.07981 | 76.25 | +0.44% | 5.67x | 3609 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 498.69 | 73.85 | +0.62% | 1.93x | 11300 | STRONG 87/100 | HIGH 61/100 | Consider small entry |
| 5 | LUNA/USD ⭐ | 4.629e-05 | 71.62 | +1.27% | 1.74x | 1872 | STRONG 76/100 | VERY_HIGH 82/100 | Watch |
| 6 | HYPE/USD ⭐ | 63.91 | 64.28 | +0.77% | 3.95x | 30946 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** PEPE/USD, XMR/USD, HYPE/USD, LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
