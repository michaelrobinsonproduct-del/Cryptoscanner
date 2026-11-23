# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T16:52:03.567088+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45220847088
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** aaef3e7fd13cb42ddd030b0ebd47b35229b03178 (atomic ledger/results publication)
**Ledger generation:** 1456 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.6992 | 106.951 | 99.285 | +6.63% | -1.47% | 3.90x | 1.4 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | UNI/USD | 5.0182 | 103.143 | 93.560 | +7.20% | -1.08% | 6.84x | 5.0 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Watch | WATCH |
| 3 | SOL/USD | 74.32 | 100.922 | 90.898 | +5.22% | -0.99% | 2.50x | 1.3 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97389 | 100.414 | 89.928 | +5.00% | -0.90% | 2.55x | 0.1 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XDG/USD | 0.057978 | 98.832 | 88.881 | +4.87% | -1.01% | 2.81x | 0.5 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | STRONG 79/100 | HIGH 65/100 | Watch | WATCH |
| 6 | LINK/USD | 9.19169 | 96.572 | 85.227 | +4.32% | -0.73% | 7.63x | 0.0 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LTC/USD | 42.56 | 87.986 | 95.658 | +5.98% | -0.68% | 0.57x | 2.3 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ZEC/USD | 839.71 | 83.038 | 89.299 | +5.29% | -0.86% | 0.80x | 5.5 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 9 | INJ/USD | 6.788 | 82.893 | 94.633 | +8.99% | -1.04% | 0.34x | 5.9 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 10 | HYPE/USD | 65.94 | 80.463 | 86.211 | +4.57% | -0.27% | 0.56x | 1.5 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XLM/USD | 0.133 | 79.389 | 84.585 | +4.29% | -1.41% | 1.19x | 0.9 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 12 | ADA/USD | 0.152653 | 78.085 | 92.200 | +5.57% | -1.31% | 0.25x | 3.5 | 2026-11-23T16:51:56.783655+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SUI/USD | 99.285 | 0.6992 | -1.47% | 3.90x |
| 2 | LTC/USD | 95.658 | 42.56 | -0.68% | 0.57x |
| 3 | INJ/USD | 94.633 | 6.788 | -1.04% | 0.34x |
| 4 | UNI/USD | 93.560 | 5.0182 | -1.08% | 6.84x |
| 5 | ADA/USD | 92.200 | 0.152653 | -1.31% | 0.25x |
| 6 | SOL/USD | 90.898 | 74.32 | -0.99% | 2.50x |
| 7 | XRP/USD | 89.928 | 0.97389 | -0.90% | 2.55x |
| 8 | ZEC/USD | 89.299 | 839.71 | -0.86% | 0.80x |
| 9 | XDG/USD | 88.881 | 0.057978 | -1.01% | 2.81x |
| 10 | HYPE/USD | 86.211 | 65.94 | -0.27% | 0.56x |
| 11 | LINK/USD | 85.227 | 9.19169 | -0.73% | 7.63x |
| 12 | XLM/USD | 84.585 | 0.133 | -1.41% | 1.19x |

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

- Persisted scans: 1456; predictions: 12239; observations: 881806.
- Matured sampled outcomes across 1/6/24/48h: 21196; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45220847088 · **Generation:** 1456 · **Legacy run:** 45220847088
**Main quote time:** 2026-11-23T16:52:03.567088+00:00 · **Legacy report time:** 2026-11-23T16:53:12.603077+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.6992 | 106.95 | -1.47% | 3.90x | STRONG 80/100 | HIGH 65/100 | Do nothing |
| 2 | UNI/USD | 5.0182 | 103.14 | -1.08% | 6.84x | STRONG 80/100 | HIGH 65/100 | Watch |
| 3 | SOL/USD | 74.32 | 100.92 | -0.99% | 2.50x | STRONG 80/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.97389 | 100.41 | -0.90% | 2.55x | STRONG 80/100 | HIGH 61/100 | Watch |
| 5 | XDG/USD | 0.057978 | 98.83 | -1.01% | 2.81x | STRONG 79/100 | HIGH 65/100 | Watch |
| 6 | LINK/USD | 9.19169 | 96.57 | -0.73% | 7.63x | STRONG 78/100 | HIGH 61/100 | Watch |
| 7 | LTC/USD | 42.56 | 87.99 | -0.68% | 0.57x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 8 | ZEC/USD | 839.71 | 83.04 | -0.86% | 0.80x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 9 | INJ/USD | 6.788 | 82.89 | -1.04% | 0.34x | MODERATE 46/100 | VERY_HIGH 80/100 | Watch |
| 10 | HYPE/USD | 65.94 | 80.46 | -0.27% | 0.56x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 11 | XLM/USD | 0.133 | 79.39 | -1.41% | 1.19x | MODERATE 50/100 | VERY_HIGH 72/100 | Do nothing |
| 12 | ADA/USD | 0.152653 | 78.08 | -1.31% | 0.25x | WEAK 44/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
