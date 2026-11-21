# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T09:20:35.454192+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44889037974
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** b0676c9e2b625d6c6ef9aef21ac8444a74a239bf (atomic ledger/results publication)
**Ledger generation:** 1114 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.563 | 76.740 | 78.406 | +3.97% | +0.47% | 0.60x | 8.8 | 2026-11-21T09:20:28.951576+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TRX/USD | 0.302639 | 72.807 | 57.619 | +0.38% | +0.04% | 4.68x | 0.0 | 2026-11-21T09:20:28.951576+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ETH/USD | 1630.21 | 58.369 | 59.677 | +0.67% | +0.07% | 0.84x | 0.1 | 2026-11-21T09:20:28.951576+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.05745 | 51.231 | 28.818 | +0.77% | +1.48% | 5.64x | 15.7 | 2026-11-21T09:20:28.951576+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CAP/USD | 0.093709 | 43.706 | 47.207 | +2.37% | -0.68% | 0.99x | 6.0 | 2026-11-21T09:20:28.951576+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | RARE/USD | 0.01351 | 34.867 | 31.846 | +1.58% | -0.81% | 1.71x | 22.2 | 2026-11-21T09:20:28.951576+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 78/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 78.406 | 21.563 | +0.47% | 0.60x |
| 2 | ETH/USD | 59.677 | 1630.21 | +0.07% | 0.84x |
| 3 | TRX/USD | 57.619 | 0.302639 | +0.04% | 4.68x |
| 4 | CAP/USD | 47.207 | 0.093709 | -0.68% | 0.99x |
| 5 | RARE/USD | 31.846 | 0.01351 | -0.81% | 1.71x |
| 6 | ZAMA/USD | 28.818 | 0.05745 | +1.48% | 5.64x |

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

- Persisted scans: 1114; predictions: 8745; observations: 673671.
- Matured sampled outcomes across 1/6/24/48h: 11514; gap abstentions: 20284. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44889037974 · **Generation:** 1114 · **Legacy run:** 44889037974
**Main quote time:** 2026-11-21T09:20:35.454192+00:00 · **Legacy report time:** 2026-11-21T09:21:14.922851+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.563 | 76.74 | +0.47% | 0.60x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 2 | TRX/USD | 0.302639 | 72.81 | +0.04% | 4.68x | STRONG 81/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD | 1630.21 | 58.37 | +0.07% | 0.84x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.05745 | 51.23 | +1.48% | 5.64x | STRONG 86/100 | VERY_HIGH 73/100 | Watch |
| 5 | CAP/USD | 0.093709 | 43.71 | -0.68% | 0.99x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | RARE/USD | 0.01351 | 34.87 | -0.81% | 1.71x | WEAK 27/100 | VERY_HIGH 78/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZAMA/USD ⭐ | 0.05745 | 44.20 | +1.48% | 5.64x | 2609 | STRONG 82/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
