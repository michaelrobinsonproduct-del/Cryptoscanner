# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T05:25:35.333101+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44870750862
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** da396071d9aa7cf73a8fa92c7f0b148d43cbe7c6 (atomic ledger/results publication)
**Ledger generation:** 1089 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 607; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.014869 | 78.829 | 65.444 | +7.97% | +2.06% | 1.31x | 31.6 | 2026-11-21T05:25:32.403870+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | CAP/USD | 0.094995 | 51.830 | 52.924 | +3.77% | +0.92% | 0.43x | 14.3 | 2026-11-21T05:25:32.403870+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | DRV/USD | 0.25331 | 44.998 | 55.324 | +3.16% | -0.88% | 0.41x | 8.3 | 2026-11-21T05:25:32.403870+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | RARE/USD | 0.0136 | 39.023 | 32.694 | +2.26% | -1.73% | 4.49x | 29.5 | 2026-11-21T05:25:32.403870+00:00 | Not calibrated | WEAK 40/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 65.444 | 0.014869 | +2.06% | 1.31x |
| 2 | DRV/USD | 55.324 | 0.25331 | -0.88% | 0.41x |
| 3 | CAP/USD | 52.924 | 0.094995 | +0.92% | 0.43x |
| 4 | RARE/USD | 32.694 | 0.0136 | -1.73% | 4.49x |

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

- Persisted scans: 1089; predictions: 8618; observations: 658471.
- Matured sampled outcomes across 1/6/24/48h: 11177; gap abstentions: 19884. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44870750862 · **Generation:** 1089 · **Legacy run:** 44870750862
**Main quote time:** 2026-11-21T05:25:35.333101+00:00 · **Legacy report time:** 2026-11-21T05:26:15.896550+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.014869 | 78.83 | +2.06% | 1.31x | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 2 | CAP/USD | 0.094995 | 51.83 | +0.92% | 0.43x | MODERATE 51/100 | VERY_HIGH 81/100 | Watch |
| 3 | DRV/USD | 0.25331 | 45.00 | -0.88% | 0.41x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | RARE/USD | 0.0136 | 39.02 | -1.73% | 4.49x | WEAK 40/100 | EXTREME 89/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.014869 | 81.15 | +2.06% | 1.31x | 2971 | STRONG 81/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** BLESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
