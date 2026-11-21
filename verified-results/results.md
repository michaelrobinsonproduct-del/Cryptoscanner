# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T10:20:49.675553+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44893795835
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 27ddb809e99590ef8d2c72e4b200d8119330ab2c (atomic ledger/results publication)
**Ledger generation:** 1120 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.69 | 96.708 | 80.900 | +4.59% | +0.16% | 5.39x | 12.4 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Watch | WATCH |
| 2 | TRX/USD | 0.302495 | 71.645 | 56.788 | +0.33% | -0.03% | 2.72x | 1.0 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ETH/USD | 1633.46 | 60.454 | 60.408 | +0.87% | -0.06% | 1.04x | 1.4 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XMR/USD | 461.81 | 54.199 | 59.898 | +1.21% | -0.06% | 0.46x | 7.1 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | USELESS/USD | 0.07629 | 37.253 | 38.738 | +2.40% | +1.06% | 0.32x | 35.5 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | ZAMA/USD | 0.05816 | 29.339 | 37.859 | +2.02% | -0.05% | 0.17x | 15.5 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | WEAK 15/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | SENT/USD | 0.020668 | 28.974 | 31.010 | +0.35% | +0.40% | 0.59x | 4.8 | 2026-11-21T10:20:43.388944+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.900 | 21.69 | +0.16% | 5.39x |
| 2 | ETH/USD | 60.408 | 1633.46 | -0.06% | 1.04x |
| 3 | XMR/USD | 59.898 | 461.81 | -0.06% | 0.46x |
| 4 | TRX/USD | 56.788 | 0.302495 | -0.03% | 2.72x |
| 5 | USELESS/USD | 38.738 | 0.07629 | +1.06% | 0.32x |
| 6 | ZAMA/USD | 37.859 | 0.05816 | -0.05% | 0.17x |
| 7 | SENT/USD | 31.010 | 0.020668 | +0.40% | 0.59x |

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

- Persisted scans: 1120; predictions: 8789; observations: 677319.
- Matured sampled outcomes across 1/6/24/48h: 11565; gap abstentions: 20318. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44893795835 · **Generation:** 1120 · **Legacy run:** 44893795835
**Main quote time:** 2026-11-21T10:20:49.675553+00:00 · **Legacy report time:** 2026-11-21T10:21:52.200034+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.69 | 96.71 | +0.16% | 5.39x | STRONG 98/100 | HIGH 61/100 | Watch |
| 2 | TRX/USD | 0.302495 | 71.64 | -0.03% | 2.72x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | ETH/USD | 1633.46 | 60.45 | -0.06% | 1.04x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | XMR/USD | 461.81 | 54.20 | -0.06% | 0.46x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | USELESS/USD | 0.07629 | 37.25 | +1.06% | 0.32x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | ZAMA/USD | 0.05816 | 29.34 | -0.05% | 0.17x | WEAK 15/100 | EXTREME 94/100 | Do nothing |
| 7 | SENT/USD | 0.020668 | 28.97 | +0.40% | 0.59x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.69 | 93.48 | +0.16% | 5.39x | 14829 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
