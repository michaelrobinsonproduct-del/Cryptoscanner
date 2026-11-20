# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T14:00:55.091396+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44749197008
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 54b3acd84e051fe57747a3945688a98853f39580 (atomic ledger/results publication)
**Ledger generation:** 988 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021766 | 56.057 | 43.768 | +2.24% | +1.28% | 1.59x | 8.3 | 2026-11-20T14:00:50.324546+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31208 | 54.460 | 56.685 | +0.29% | +0.04% | 0.76x | 0.7 | 2026-11-20T14:00:50.324546+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3937 | 48.212 | 30.659 | +0.54% | +0.51% | 2.70x | 7.6 | 2026-11-20T14:00:50.324546+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 4 | MON/USD | 0.01387 | 33.172 | 31.957 | +0.80% | +1.39% | 0.43x | 14.5 | 2026-11-20T14:00:50.324546+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | GBP/USD | 56.685 | 1.31208 | +0.04% | 0.76x |
| 2 | SENT/USD | 43.768 | 0.021766 | +1.28% | 1.59x |
| 3 | MON/USD | 31.957 | 0.01387 | +1.39% | 0.43x |
| 4 | MNT/USD | 30.659 | 0.3937 | +0.51% | 2.70x |

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

- Persisted scans: 988; predictions: 8239; observations: 597070.
- Matured sampled outcomes across 1/6/24/48h: 10043; gap abstentions: 17550. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44749197008 · **Generation:** 988 · **Legacy run:** 44749197008
**Main quote time:** 2026-11-20T14:00:55.091396+00:00 · **Legacy report time:** 2026-11-20T14:02:05.408151+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021766 | 56.06 | +1.28% | 1.59x | STRONG 83/100 | HIGH 60/100 | Consider small entry |
| 2 | GBP/USD | 1.31208 | 54.46 | +0.04% | 0.76x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3937 | 48.21 | +0.51% | 2.70x | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 4 | MON/USD | 0.01387 | 33.17 | +1.39% | 0.43x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021687 | 51.96 | +1.28% | 1.59x | 7125 | STRONG 81/100 | HIGH 60/100 | Consider small entry |
| 2 | MNT/USD ⭐ | 0.3937 | 25.24 | +0.51% | 2.70x | 1206 | STRONG 78/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD, MNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
