# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:00:08.534508+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44234194448
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 72778c63be48d064dd9d70ae4e3f297f64ddf729 (atomic ledger/results publication)
**Ledger generation:** 525 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.08406 | 68.802 | 49.422 | +2.35% | +0.88% | 6.38x | 4.8 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | STRONG 89/100 | HIGH 60/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04504 | 61.356 | 43.117 | +0.33% | +0.65% | 6.40x | 11.1 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | STRONG 81/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019064 | 57.341 | 41.210 | +2.12% | +0.23% | 6.41x | 8.9 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | STRONG 84/100 | HIGH 67/100 | Watch | WATCH |
| 4 | XDC/USD | 0.03061 | 55.122 | 39.304 | +0.96% | +0.16% | 14.08x | 9.8 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | MELANIA/USD | 0.0512 | 48.933 | 47.010 | +5.13% | +0.39% | 1.00x | 39.2 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5179 | 48.832 | 38.415 | +1.69% | -0.29% | 2.19x | 11.6 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06097 | 41.995 | 39.043 | +1.74% | +0.00% | 1.30x | 13.1 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | WEAK 41/100 | HIGH 66/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8351 | 32.085 | 35.143 | +1.36% | +0.16% | 0.61x | 19.1 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | ICNT/USD | 0.2794 | 23.212 | 29.901 | +1.20% | +0.04% | 0.31x | 21.5 | 2026-11-18T04:00:02.434574+00:00 | Not calibrated | WEAK 22/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CC/USD | 49.422 | 0.08406 | +0.88% | 6.38x |
| 2 | MELANIA/USD | 47.010 | 0.0512 | +0.39% | 1.00x |
| 3 | NIGHT/USD | 43.117 | 0.04504 | +0.65% | 6.40x |
| 4 | SENT/USD | 41.210 | 0.019064 | +0.23% | 6.41x |
| 5 | XDC/USD | 39.304 | 0.03061 | +0.16% | 14.08x |
| 6 | ZAMA/USD | 39.043 | 0.06097 | +0.00% | 1.30x |
| 7 | AKT/USD | 38.415 | 0.5179 | -0.29% | 2.19x |
| 8 | PEARL/USD | 35.143 | 1.8351 | +0.16% | 0.61x |
| 9 | ICNT/USD | 29.901 | 0.2794 | +0.04% | 0.31x |

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

- Persisted scans: 525; predictions: 4437; observations: 316732.
- Matured sampled outcomes across 1/6/24/48h: 3534; gap abstentions: 12451. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44234194448 · **Generation:** 525 · **Legacy run:** 44234194448
**Main quote time:** 2026-11-18T04:00:08.534508+00:00 · **Legacy report time:** 2026-11-18T04:00:25.846349+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08406 | 68.80 | +0.88% | 6.38x | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04504 | 61.36 | +0.65% | 6.40x | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.019064 | 57.34 | +0.23% | 6.41x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 4 | XDC/USD ⭐ | 0.03061 | 55.12 | +0.16% | 14.08x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | MELANIA/USD | 0.0512 | 48.93 | +0.39% | 1.00x | WEAK 39/100 | EXTREME 86/100 | Do nothing |
| 6 | AKT/USD | 0.5179 | 48.83 | -0.29% | 2.19x | MODERATE 49/100 | VERY_HIGH 72/100 | Watch |
| 7 | ZAMA/USD | 0.06097 | 42.00 | +0.00% | 1.30x | WEAK 41/100 | HIGH 66/100 | Watch |
| 8 | PEARL/USD | 1.8351 | 32.08 | +0.16% | 0.61x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | ICNT/USD | 0.2794 | 23.21 | +0.04% | 0.31x | WEAK 22/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08391 | 61.85 | +0.88% | 6.38x | 4073 | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.019064 | 56.59 | +0.23% | 6.41x | 3887 | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04504 | 51.86 | +0.65% | 6.40x | 13760 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | XDC/USD ⭐ | 0.03061 | 46.47 | +0.16% | 14.08x | 5935 | STRONG 73/100 | HIGH 61/100 | Watch |

**Same-run overlap:** CC/USD, NIGHT/USD, SENT/USD, XDC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
