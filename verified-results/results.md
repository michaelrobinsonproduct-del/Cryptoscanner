# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T08:46:08.851217+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45785731077
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fdc091602d0442e4cb3d5594d4ebd7fc3d721e42 (atomic ledger/results publication)
**Ledger generation:** 1838 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.202 | 88.699 | 70.939 | +4.17% | +0.55% | 2.76x | 1.6 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.95457 | 84.950 | 68.147 | +1.92% | +0.36% | 2.92x | 0.6 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.19274 | 82.697 | 65.499 | +1.64% | +0.44% | 3.46x | 0.5 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 43.44 | 75.053 | 65.813 | +1.71% | +0.37% | 1.74x | 2.3 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 60686.1 | 74.158 | 58.673 | +0.53% | +0.10% | 2.68x | 0.0 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0565398 | 72.922 | 57.143 | +1.04% | +0.16% | 3.54x | 0.2 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.0724 | 72.895 | 71.821 | +9.25% | -1.28% | 1.75x | 11.0 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AAVE/USD | 96.34 | 65.885 | 48.120 | +1.03% | +0.55% | 4.46x | 2.1 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ADA/USD | 0.147911 | 64.119 | 63.591 | +1.47% | +0.20% | 0.95x | 3.4 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 10 | DOT/USD | 0.6706 | 60.998 | 45.475 | +1.87% | +0.10% | 3.30x | 1.5 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 11 | SOL/USD | 70.88 | 58.383 | 59.167 | +0.70% | +0.01% | 0.91x | 1.4 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | NEAR/USD | 3.0748 | 55.041 | 58.925 | +0.82% | +0.72% | 0.25x | 3.6 | 2026-11-26T08:45:59.837142+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 71.821 | 0.0724 | -1.28% | 1.75x |
| 2 | INJ/USD | 70.939 | 6.202 | +0.55% | 2.76x |
| 3 | XRP/USD | 68.147 | 0.95457 | +0.36% | 2.92x |
| 4 | LTC/USD | 65.813 | 43.44 | +0.37% | 1.74x |
| 5 | LINK/USD | 65.499 | 9.19274 | +0.44% | 3.46x |
| 6 | ADA/USD | 63.591 | 0.147911 | +0.20% | 0.95x |
| 7 | SOL/USD | 59.167 | 70.88 | +0.01% | 0.91x |
| 8 | NEAR/USD | 58.925 | 3.0748 | +0.72% | 0.25x |
| 9 | XBT/USD | 58.673 | 60686.1 | +0.10% | 2.68x |
| 10 | XDG/USD | 57.143 | 0.0565398 | +0.16% | 3.54x |
| 11 | AAVE/USD | 48.120 | 96.34 | +0.55% | 4.46x |
| 12 | DOT/USD | 45.475 | 0.6706 | +0.10% | 3.30x |

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

- Persisted scans: 1838; predictions: 15791; observations: 1114384.
- Matured sampled outcomes across 1/6/24/48h: 34214; gap abstentions: 24365. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45785731077 · **Generation:** 1838 · **Legacy run:** 45785731077
**Main quote time:** 2026-11-26T08:46:08.851217+00:00 · **Legacy report time:** 2026-11-26T08:47:05.843819+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.202 | 88.70 | +0.55% | 2.76x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95457 | 84.95 | +0.36% | 2.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.19274 | 82.70 | +0.44% | 3.46x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 43.44 | 75.05 | +0.37% | 1.74x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD | 60686.1 | 74.16 | +0.10% | 2.68x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD | 0.0565398 | 72.92 | +0.16% | 3.54x | STRONG 81/100 | HIGH 55/100 | Watch |
| 7 | SYRUP/USD | 0.0724 | 72.89 | -1.28% | 1.75x | MODERATE 51/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AAVE/USD | 96.34 | 65.89 | +0.55% | 4.46x | STRONG 88/100 | HIGH 55/100 | Watch |
| 9 | ADA/USD | 0.147911 | 64.12 | +0.20% | 0.95x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 10 | DOT/USD | 0.6706 | 61.00 | +0.10% | 3.30x | STRONG 75/100 | HIGH 60/100 | Watch |
| 11 | SOL/USD | 70.88 | 58.38 | +0.01% | 0.91x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | NEAR/USD | 3.0748 | 55.04 | +0.72% | 0.25x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.202 | 88.36 | +0.55% | 2.76x | 6726 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95568 | 82.75 | +0.36% | 2.92x | 41443 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.1969 | 77.73 | +0.44% | 3.46x | 9131 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD ⭐ | 43.5 | 73.67 | +0.37% | 1.74x | 15488 | STRONG 92/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** INJ/USD, XRP/USD, LINK/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
