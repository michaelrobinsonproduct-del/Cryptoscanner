# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T07:37:33.900154+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45569212093
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c21c45215ab92a78d1282ece4dd5ba66fbd9d159 (atomic ledger/results publication)
**Ledger generation:** 1688 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01039 | 95.692 | 84.677 | +9.71% | +1.84% | 1.18x | 19.3 | 2026-11-25T07:37:29.025490+00:00 | Not calibrated | STRONG 78/100 | HIGH 68/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33128 | 59.894 | 68.081 | +5.41% | -0.24% | 0.30x | 14.2 | 2026-11-25T07:37:29.025490+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.093385 | 34.148 | 36.522 | +1.05% | -0.13% | 0.83x | 6.1 | 2026-11-25T07:37:29.025490+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 4 | XPL/USD | 0.0448 | 33.929 | 36.782 | +1.82% | -0.22% | 0.83x | 22.5 | 2026-11-25T07:37:29.025490+00:00 | Not calibrated | WEAK 12/100 | EXTREME 85/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07126 | 18.641 | 27.266 | +2.28% | -0.45% | 0.36x | 40.9 | 2026-11-25T07:37:29.025490+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 84.677 | 0.01039 | +1.84% | 1.18x |
| 2 | DRV/USD | 68.081 | 0.33128 | -0.24% | 0.30x |
| 3 | XPL/USD | 36.782 | 0.0448 | -0.22% | 0.83x |
| 4 | CAP/USD | 36.522 | 0.093385 | -0.13% | 0.83x |
| 5 | SYRUP/USD | 27.266 | 0.07126 | -0.45% | 0.36x |

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

- Persisted scans: 1688; predictions: 14331; observations: 1023083.
- Matured sampled outcomes across 1/6/24/48h: 30664; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45569212093 · **Generation:** 1688 · **Legacy run:** 45569212093
**Main quote time:** 2026-11-25T07:37:33.900154+00:00 · **Legacy report time:** 2026-11-25T07:38:28.536768+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01039 | 95.69 | +1.84% | 1.18x | STRONG 88/100 | HIGH 68/100 | Watch |
| 2 | DRV/USD | 0.33128 | 59.89 | -0.24% | 0.30x | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | CAP/USD | 0.093385 | 34.15 | -0.13% | 0.83x | WEAK 22/100 | VERY_HIGH 73/100 | Do nothing |
| 4 | XPL/USD | 0.0448 | 33.93 | -0.22% | 0.83x | WEAK 12/100 | EXTREME 85/100 | Do nothing |
| 5 | SYRUP/USD | 0.07126 | 18.64 | -0.45% | 0.36x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01037 | 87.82 | +1.84% | 1.18x | 18897 | STRONG 84/100 | HIGH 68/100 | Watch |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
