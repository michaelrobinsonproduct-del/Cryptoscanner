# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T23:11:53.565739+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45286320889
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1802f119087fb1cdcf59d9dfca43a21df08d8f22 (atomic ledger/results publication)
**Ledger generation:** 1494 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.82 | 114.130 | 97.751 | +8.63% | +0.28% | 3.98x | 4.5 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ALGO/USD | 0.08106 | 96.068 | 90.612 | +7.46% | +0.30% | 1.40x | 8.6 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ATOM/USD | 1.2668 | 89.836 | 75.795 | +8.09% | +0.67% | 2.07x | 4.7 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 41.2 | 87.763 | 71.914 | +2.59% | +0.39% | 2.39x | 2.4 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PEARL/USD | 2.2848 | 80.363 | 95.837 | +11.21% | -2.49% | 0.70x | 8.3 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | XDG/USD | 0.0561594 | 76.095 | 66.078 | +1.58% | +0.42% | 1.79x | 0.0 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SOL/USD | 71.94 | 73.504 | 67.288 | +1.85% | +0.26% | 1.49x | 1.4 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 8 | TRX/USD | 0.30915 | 66.074 | 50.674 | +1.30% | +0.08% | 3.34x | 0.0 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94044 | 63.772 | 64.682 | +1.39% | +0.48% | 0.67x | 0.1 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SHX/USD | 0.003604 | 63.010 | 70.795 | +6.79% | -0.28% | 0.36x | 11.1 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | CAP/USD | 0.101718 | 62.617 | 70.114 | +8.71% | -0.07% | 0.28x | 18.1 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | XAUT/USD | 3624.6 | 59.364 | 44.240 | +1.47% | +0.02% | 85.43x | 0.6 | 2026-11-23T23:11:44.812048+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.751 | 155.82 | +0.28% | 3.98x |
| 2 | PEARL/USD | 95.837 | 2.2848 | -2.49% | 0.70x |
| 3 | ALGO/USD | 90.612 | 0.08106 | +0.30% | 1.40x |
| 4 | ATOM/USD | 75.795 | 1.2668 | +0.67% | 2.07x |
| 5 | LTC/USD | 71.914 | 41.2 | +0.39% | 2.39x |
| 6 | SHX/USD | 70.795 | 0.003604 | -0.28% | 0.36x |
| 7 | CAP/USD | 70.114 | 0.101718 | -0.07% | 0.28x |
| 8 | SOL/USD | 67.288 | 71.94 | +0.26% | 1.49x |
| 9 | XDG/USD | 66.078 | 0.0561594 | +0.42% | 1.79x |
| 10 | XRP/USD | 64.682 | 0.94044 | +0.48% | 0.67x |
| 11 | TRX/USD | 50.674 | 0.30915 | +0.08% | 3.34x |
| 12 | XAUT/USD | 44.240 | 3624.6 | +0.02% | 85.43x |

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

- Persisted scans: 1494; predictions: 12695; observations: 904948.
- Matured sampled outcomes across 1/6/24/48h: 23080; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45286320889 · **Generation:** 1494 · **Legacy run:** 45286320889
**Main quote time:** 2026-11-23T23:11:53.565739+00:00 · **Legacy report time:** 2026-11-23T23:12:59.272908+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.82 | 114.13 | +0.28% | 3.98x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.08106 | 96.07 | +0.30% | 1.40x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ATOM/USD ⭐ | 1.2668 | 89.84 | +0.67% | 2.07x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 41.2 | 87.76 | +0.39% | 2.39x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PEARL/USD | 2.2848 | 80.36 | -2.49% | 0.70x | MODERATE 45/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | XDG/USD | 0.0561594 | 76.09 | +0.42% | 1.79x | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 7 | SOL/USD ⭐ | 71.94 | 73.50 | +0.26% | 1.49x | STRONG 92/100 | HIGH 55/100 | Watch |
| 8 | TRX/USD | 0.30915 | 66.07 | +0.08% | 3.34x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | XRP/USD | 0.94044 | 63.77 | +0.48% | 0.67x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | SHX/USD | 0.003604 | 63.01 | -0.28% | 0.36x | WEAK 32/100 | EXTREME 94/100 | Do nothing |
| 11 | CAP/USD | 0.101718 | 62.62 | -0.07% | 0.28x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 12 | XAUT/USD | 3624.6 | 59.36 | +0.02% | 85.43x | STRONG 75/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 155.64 | 93.83 | +0.28% | 3.98x | 12420 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.08106 | 89.56 | +0.30% | 1.40x | 10110 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD ⭐ | 41.17 | 84.05 | +0.39% | 2.39x | 12775 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ATOM/USD ⭐ | 1.2667 | 78.18 | +0.67% | 2.07x | 3721 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 71.85 | 72.69 | +0.26% | 1.49x | 45735 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, ALGO/USD, ATOM/USD, LTC/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
