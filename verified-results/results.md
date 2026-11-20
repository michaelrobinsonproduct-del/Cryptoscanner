# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T14:10:52.182824+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44750768625
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 95987cf9b17f8fdfa37da6cd88cbe9c0c9db35af (atomic ledger/results publication)
**Ledger generation:** 989 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021992 | 66.964 | 51.434 | +3.30% | +1.80% | 1.65x | 7.7 | 2026-11-20T14:10:47.518115+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 2 | MNT/USD | 0.3941 | 47.020 | 31.385 | +0.64% | +0.13% | 4.37x | 7.6 | 2026-11-20T14:10:47.518115+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MON/USD | 0.01388 | 44.830 | 36.127 | +0.87% | +0.65% | 1.54x | 7.2 | 2026-11-20T14:10:47.518115+00:00 | Not calibrated | MODERATE 67/100 | HIGH 60/100 | Watch | WATCH |
| 4 | CAP/USD | 0.09701 | 35.529 | 33.289 | +0.41% | +0.31% | 1.07x | 6.0 | 2026-11-20T14:10:47.518115+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.4275 | 28.575 | 31.696 | +0.33% | +0.64% | 0.37x | 16.4 | 2026-11-20T14:10:47.518115+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 51.434 | 0.021992 | +1.80% | 1.65x |
| 2 | MON/USD | 36.127 | 0.01388 | +0.65% | 1.54x |
| 3 | CAP/USD | 33.289 | 0.09701 | +0.31% | 1.07x |
| 4 | ICNT/USD | 31.696 | 0.4275 | +0.64% | 0.37x |
| 5 | MNT/USD | 31.385 | 0.3941 | +0.13% | 4.37x |

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

- Persisted scans: 989; predictions: 8244; observations: 597677.
- Matured sampled outcomes across 1/6/24/48h: 10078; gap abstentions: 17568. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44750768625 · **Generation:** 989 · **Legacy run:** 44750768625
**Main quote time:** 2026-11-20T14:10:52.182824+00:00 · **Legacy report time:** 2026-11-20T14:11:52.289956+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021992 | 66.96 | +1.80% | 1.65x | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 2 | MNT/USD ⭐ | 0.3941 | 47.02 | +0.13% | 4.37x | STRONG 79/100 | HIGH 67/100 | Watch |
| 3 | MON/USD ⭐ | 0.01388 | 44.83 | +0.65% | 1.54x | STRONG 77/100 | HIGH 60/100 | Consider small entry |
| 4 | CAP/USD ⭐ | 0.09701 | 35.53 | +0.31% | 1.07x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 5 | ICNT/USD | 0.4275 | 28.58 | +0.64% | 0.37x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021997 | 71.67 | +1.80% | 1.65x | 7008 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.01388 | 39.38 | +0.65% | 1.54x | 3531 | STRONG 75/100 | HIGH 60/100 | Consider small entry |
| 3 | CAP/USD ⭐ | 0.09701 | 35.29 | +0.31% | 1.07x | 5204 | MODERATE 63/100 | HIGH 67/100 | Watch |
| 4 | MNT/USD ⭐ | 0.3947 | 28.43 | +0.13% | 4.37x | 1214 | MODERATE 69/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, MNT/USD, MON/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
