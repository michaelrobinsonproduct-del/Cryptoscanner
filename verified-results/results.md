# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T04:11:27.863641+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45110130912
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 6fdb5203cb8ddf589251ce1cf91a92ced86ebe04 (atomic ledger/results publication)
**Ledger generation:** 1379 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.07579 | 60.791 | 57.077 | +3.44% | +0.60% | 1.07x | 4.0 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 2 | SOL/USD | 71.19 | 58.090 | 59.848 | +0.79% | +0.13% | 0.76x | 1.4 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 3 | VVV/USD | 26.906 | 55.110 | 59.756 | +1.39% | +0.65% | 0.21x | 6.3 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XMR/USD | 498.01 | 53.998 | 59.089 | +0.87% | -0.07% | 0.53x | 4.0 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | NEAR/USD | 3.0085 | 53.984 | 58.797 | +0.90% | +0.23% | 0.40x | 5.0 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.9308 | 49.301 | 57.138 | +0.35% | +0.08% | 0.18x | 0.6 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1729 | 49.009 | 57.629 | +0.43% | +0.05% | 0.11x | 0.8 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | UNI/USD | 4.7752 | 46.959 | 53.115 | +2.01% | +0.36% | 0.21x | 5.9 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XAUT/USD | 3593.1 | 45.935 | 37.128 | +0.59% | -0.01% | 1.88x | 0.3 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | WEAK 43/100 | HIGH 66/100 | Watch | WATCH |
| 10 | BLESS/USD | 0.017181 | 45.920 | 63.681 | +6.76% | -2.65% | 0.55x | 40.2 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | WEAK 13/100 | EXTREME 100/100 | Do nothing | WATCH |
| 11 | JUP/USD | 0.2312 | 44.758 | 49.645 | +2.95% | -0.57% | 0.80x | 9.5 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 12 | LINK/USD | 8.88243 | 42.773 | 48.353 | +0.81% | +0.34% | 0.27x | 1.3 | 2026-11-23T04:11:21.674711+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 63.681 | 0.017181 | -2.65% | 0.55x |
| 2 | SOL/USD | 59.848 | 71.19 | +0.13% | 0.76x |
| 3 | VVV/USD | 59.756 | 26.906 | +0.65% | 0.21x |
| 4 | XMR/USD | 59.089 | 498.01 | -0.07% | 0.53x |
| 5 | NEAR/USD | 58.797 | 3.0085 | +0.23% | 0.40x |
| 6 | ETH/USD | 57.629 | 1729 | +0.05% | 0.11x |
| 7 | XRP/USD | 57.138 | 0.9308 | +0.08% | 0.18x |
| 8 | CC/USD | 57.077 | 0.07579 | +0.60% | 1.07x |
| 9 | UNI/USD | 53.115 | 4.7752 | +0.36% | 0.21x |
| 10 | JUP/USD | 49.645 | 0.2312 | -0.57% | 0.80x |
| 11 | LINK/USD | 48.353 | 8.88243 | +0.34% | 0.27x |
| 12 | XAUT/USD | 37.128 | 3593.1 | -0.01% | 1.88x |

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

- Persisted scans: 1379; predictions: 11315; observations: 834916.
- Matured sampled outcomes across 1/6/24/48h: 18262; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 95 (sampled only; not a success-rate estimate).
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

**Writer:** 45110130912 · **Generation:** 1379 · **Legacy run:** 45110130912
**Main quote time:** 2026-11-23T04:11:27.863641+00:00 · **Legacy report time:** 2026-11-23T04:12:34.688060+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07579 | 60.79 | +0.60% | 1.07x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | SOL/USD | 71.19 | 58.09 | +0.13% | 0.76x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD | 26.906 | 55.11 | +0.65% | 0.21x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | XMR/USD | 498.01 | 54.00 | -0.07% | 0.53x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | NEAR/USD | 3.0085 | 53.98 | +0.23% | 0.40x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.9308 | 49.30 | +0.08% | 0.18x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1729 | 49.01 | +0.05% | 0.11x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 8 | UNI/USD | 4.7752 | 46.96 | +0.36% | 0.21x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 9 | XAUT/USD | 3593.1 | 45.94 | -0.01% | 1.88x | WEAK 43/100 | HIGH 66/100 | Watch |
| 10 | BLESS/USD | 0.017181 | 45.92 | -2.65% | 0.55x | WEAK 13/100 | EXTREME 100/100 | Do nothing |
| 11 | JUP/USD | 0.2312 | 44.76 | -0.57% | 0.80x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 12 | LINK/USD | 8.88243 | 42.77 | +0.34% | 0.27x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07578 | 72.62 | +0.60% | 1.07x | 3874 | STRONG 81/100 | HIGH 67/100 | Watch |
| 2 | ICNT/USD | 0.3596 | 56.97 | +0.28% | 2.74x | 2740 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
