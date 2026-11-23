# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T06:51:39.391348+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45126746953
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3315c85d59e990011bbfbc05b202a03f8c8298c0 (atomic ledger/results publication)
**Ledger generation:** 1395 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 18s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01635 | 84.531 | 67.073 | +11.83% | +0.49% | 15.36x | 18.3 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | JUP/USD | 0.23954 | 72.132 | 74.677 | +6.67% | +0.42% | 0.54x | 9.6 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | SOL/USD | 71.84 | 68.039 | 66.296 | +1.71% | +0.32% | 1.01x | 1.4 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XRP/USD | 0.93826 | 65.103 | 62.292 | +1.16% | +0.11% | 1.23x | 1.6 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XMR/USD | 498.07 | 60.140 | 58.872 | +0.88% | +0.15% | 1.05x | 4.6 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6646 | 59.363 | 63.749 | +1.36% | +0.30% | 0.41x | 1.5 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | GBP/USD | 1.3123 | 58.966 | 56.602 | +0.25% | +0.04% | 1.22x | 0.3 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XBT/USD | 61348.9 | 57.937 | 57.038 | +0.29% | +0.03% | 1.08x | 0.0 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XAUT/USD | 3612 | 57.162 | 41.094 | +1.12% | +0.21% | 8.16x | 0.3 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 10 | NIGHT/USD | 0.05004 | 54.975 | 61.303 | +1.77% | -0.44% | 0.59x | 4.0 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | NEAR/USD | 3.004 | 54.896 | 60.069 | +0.75% | +0.40% | 0.28x | 0.3 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | CC/USD | 0.07611 | 51.752 | 59.096 | +3.88% | +0.16% | 0.19x | 6.6 | 2026-11-23T06:51:21.313167+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 74.677 | 0.23954 | +0.42% | 0.54x |
| 2 | AI/USD | 67.073 | 0.01635 | +0.49% | 15.36x |
| 3 | SOL/USD | 66.296 | 71.84 | +0.32% | 1.01x |
| 4 | SUI/USD | 63.749 | 0.6646 | +0.30% | 0.41x |
| 5 | XRP/USD | 62.292 | 0.93826 | +0.11% | 1.23x |
| 6 | NIGHT/USD | 61.303 | 0.05004 | -0.44% | 0.59x |
| 7 | NEAR/USD | 60.069 | 3.004 | +0.40% | 0.28x |
| 8 | CC/USD | 59.096 | 0.07611 | +0.16% | 0.19x |
| 9 | XMR/USD | 58.872 | 498.07 | +0.15% | 1.05x |
| 10 | XBT/USD | 57.038 | 61348.9 | +0.03% | 1.08x |
| 11 | GBP/USD | 56.602 | 1.3123 | +0.04% | 1.22x |
| 12 | XAUT/USD | 41.094 | 3612 | +0.21% | 8.16x |

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

- Persisted scans: 1395; predictions: 11507; observations: 844659.
- Matured sampled outcomes across 1/6/24/48h: 18709; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 123 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45126746953 · **Generation:** 1395 · **Legacy run:** 45126746953
**Main quote time:** 2026-11-23T06:51:39.391348+00:00 · **Legacy report time:** 2026-11-23T06:52:34.614375+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01635 | 84.53 | +0.49% | 15.36x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | JUP/USD | 0.23954 | 72.13 | +0.42% | 0.54x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 3 | SOL/USD ⭐ | 71.84 | 68.04 | +0.32% | 1.01x | STRONG 79/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93826 | 65.10 | +0.11% | 1.23x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 5 | XMR/USD | 498.07 | 60.14 | +0.15% | 1.05x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | SUI/USD | 0.6646 | 59.36 | +0.30% | 0.41x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 7 | GBP/USD | 1.3123 | 58.97 | +0.04% | 1.22x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 8 | XBT/USD | 61348.9 | 57.94 | +0.03% | 1.08x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 9 | XAUT/USD | 3612 | 57.16 | +0.21% | 8.16x | STRONG 84/100 | HIGH 60/100 | Watch |
| 10 | NIGHT/USD | 0.05004 | 54.98 | -0.44% | 0.59x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | NEAR/USD | 3.004 | 54.90 | +0.40% | 0.28x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 12 | CC/USD | 0.07611 | 51.75 | +0.16% | 0.19x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.955 | 89.75 | +1.24% | 11.96x | 6524 | STRONG 85/100 | HIGH 67/100 | Consider small entry |
| 2 | XDC/USD | 0.02745 | 83.18 | +1.93% | 4.23x | 2310 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 3 | AI/USD ⭐ | 0.01635 | 80.22 | +0.49% | 15.36x | 3172 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 4 | SOL/USD ⭐ | 71.85 | 70.96 | +0.32% | 1.01x | 30016 | STRONG 80/100 | HIGH 62/100 | Watch |
| 5 | PEARL/USD | 2.1131 | 70.31 | +0.46% | 2.47x | 7097 | STRONG 85/100 | HIGH 61/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.93992 | 67.55 | +0.11% | 1.23x | 21084 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** AI/USD, SOL/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
