# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:31:41.702114+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45165685562
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d8fb0f0ebd3f9eef184f07ba19b7f543ed347e75 (atomic ledger/results publication)
**Ledger generation:** 1424 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.32 | 107.280 | 88.612 | +8.98% | +2.83% | 1.45x | 8.3 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | JUP/USD | 0.24298 | 86.447 | 74.572 | +8.20% | +0.11% | 2.13x | 11.5 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 3 | ALGO/USD | 0.0823 | 86.311 | 74.227 | +9.11% | -0.58% | 4.04x | 10.9 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | ICP/USD | 2.06 | 75.582 | 62.519 | +4.78% | -0.39% | 4.05x | 9.7 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 68/100 | HIGH 66/100 | Watch | WATCH |
| 5 | SOL/USD | 72.49 | 73.252 | 72.744 | +2.63% | +0.40% | 0.85x | 1.4 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | HYPE/USD | 64.18 | 69.487 | 66.654 | +1.78% | +0.25% | 1.16x | 1.6 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93914 | 66.373 | 63.435 | +1.25% | +0.19% | 1.20x | 0.6 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XLM/USD | 0.128952 | 65.871 | 61.894 | +1.12% | +0.19% | 1.30x | 0.5 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6701 | 63.161 | 69.626 | +2.20% | +0.18% | 0.26x | 1.5 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XMR/USD | 503.6 | 60.113 | 66.042 | +2.00% | +0.30% | 0.26x | 6.0 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61343.8 | 56.062 | 56.980 | +0.28% | +0.19% | 0.82x | 0.0 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0557339 | 55.783 | 52.009 | +0.81% | +0.34% | 1.21x | 0.9 | 2026-11-23T11:31:35.408155+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 88.612 | 156.32 | +2.83% | 1.45x |
| 2 | JUP/USD | 74.572 | 0.24298 | +0.11% | 2.13x |
| 3 | ALGO/USD | 74.227 | 0.0823 | -0.58% | 4.04x |
| 4 | SOL/USD | 72.744 | 72.49 | +0.40% | 0.85x |
| 5 | SUI/USD | 69.626 | 0.6701 | +0.18% | 0.26x |
| 6 | HYPE/USD | 66.654 | 64.18 | +0.25% | 1.16x |
| 7 | XMR/USD | 66.042 | 503.6 | +0.30% | 0.26x |
| 8 | XRP/USD | 63.435 | 0.93914 | +0.19% | 1.20x |
| 9 | ICP/USD | 62.519 | 2.06 | -0.39% | 4.05x |
| 10 | XLM/USD | 61.894 | 0.128952 | +0.19% | 1.30x |
| 11 | XBT/USD | 56.980 | 61343.8 | +0.19% | 0.82x |
| 12 | XDG/USD | 52.009 | 0.0557339 | +0.34% | 1.21x |

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

- Persisted scans: 1424; predictions: 11855; observations: 862319.
- Matured sampled outcomes across 1/6/24/48h: 19667; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45165685562 · **Generation:** 1424 · **Legacy run:** 45165685562
**Main quote time:** 2026-11-23T11:31:41.702114+00:00 · **Legacy report time:** 2026-11-23T11:32:48.525557+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.32 | 107.28 | +2.83% | 1.45x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | JUP/USD ⭐ | 0.24298 | 86.45 | +0.11% | 2.13x | STRONG 93/100 | HIGH 66/100 | Watch |
| 3 | ALGO/USD | 0.0823 | 86.31 | -0.58% | 4.04x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 4 | ICP/USD | 2.06 | 75.58 | -0.39% | 4.05x | MODERATE 68/100 | HIGH 66/100 | Watch |
| 5 | SOL/USD | 72.49 | 73.25 | +0.40% | 0.85x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 6 | HYPE/USD ⭐ | 64.18 | 69.49 | +0.25% | 1.16x | STRONG 80/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD ⭐ | 0.93914 | 66.37 | +0.19% | 1.20x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 8 | XLM/USD ⭐ | 0.128952 | 65.87 | +0.19% | 1.30x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | SUI/USD | 0.6701 | 63.16 | +0.18% | 0.26x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 10 | XMR/USD | 503.6 | 60.11 | +0.30% | 0.26x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61343.8 | 56.06 | +0.19% | 0.82x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 12 | XDG/USD | 0.0557339 | 55.78 | +0.34% | 1.21x | MODERATE 63/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.69 | 90.46 | +2.83% | 1.45x | 5700 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | JUP/USD ⭐ | 0.24236 | 78.07 | +0.11% | 2.13x | 3526 | STRONG 89/100 | HIGH 66/100 | Watch |
| 3 | HYPE/USD ⭐ | 64.18 | 71.58 | +0.25% | 1.16x | 9910 | STRONG 81/100 | HIGH 62/100 | Watch |
| 4 | DOT/USD | 0.6756 | 71.55 | +0.10% | 9.05x | 7639 | STRONG 81/100 | HIGH 60/100 | Watch |
| 5 | XLM/USD ⭐ | 0.128939 | 66.53 | +0.19% | 1.30x | 12745 | STRONG 78/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD ⭐ | 0.9393 | 66.45 | +0.19% | 1.20x | 20514 | MODERATE 68/100 | HIGH 62/100 | Watch |

**Same-run overlap:** QNT/USD, JUP/USD, HYPE/USD, XRP/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
