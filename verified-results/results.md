# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T15:41:20.921846+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45039524723
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 1e7e0dfe332509c6bdfb3028e8162fa634ce7a57 (atomic ledger/results publication)
**Ledger generation:** 1302 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04875 | 83.754 | 87.118 | +10.09% | +0.45% | 0.44x | 10.3 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | DRV/USD | 0.36533 | 83.197 | 86.575 | +8.99% | -0.78% | 1.05x | 4.4 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0031 | 81.014 | 81.162 | +4.05% | -0.07% | 1.02x | 4.3 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 4 | TAO/USD | 190.5806 | 78.726 | 64.608 | +2.61% | -0.18% | 5.47x | 5.3 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 25.539 | 77.930 | 70.221 | +2.57% | -0.31% | 1.93x | 5.5 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 8.79675 | 76.560 | 60.586 | +2.35% | +0.19% | 3.34x | 1.9 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.93 | 74.355 | 73.523 | +2.76% | +0.40% | 0.88x | 1.6 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ETH/USD | 1714.92 | 71.245 | 68.552 | +1.94% | +0.05% | 1.24x | 0.1 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6558 | 65.617 | 62.667 | +1.31% | -0.06% | 1.33x | 3.0 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ZEC/USD | 795.61 | 61.033 | 68.928 | +2.24% | +0.01% | 0.21x | 3.5 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60752.8 | 58.819 | 62.714 | +1.10% | -0.10% | 0.66x | 0.0 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | STBL/USD | 0.016994 | 57.249 | 65.591 | +6.19% | -0.63% | 0.48x | 17.1 | 2026-11-22T15:41:13.037887+00:00 | Not calibrated | WEAK 29/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 87.118 | 0.04875 | +0.45% | 0.44x |
| 2 | DRV/USD | 86.575 | 0.36533 | -0.78% | 1.05x |
| 3 | NEAR/USD | 81.162 | 3.0031 | -0.07% | 1.02x |
| 4 | HYPE/USD | 73.523 | 62.93 | +0.40% | 0.88x |
| 5 | VVV/USD | 70.221 | 25.539 | -0.31% | 1.93x |
| 6 | ZEC/USD | 68.928 | 795.61 | +0.01% | 0.21x |
| 7 | ETH/USD | 68.552 | 1714.92 | +0.05% | 1.24x |
| 8 | STBL/USD | 65.591 | 0.016994 | -0.63% | 0.48x |
| 9 | TAO/USD | 64.608 | 190.5806 | -0.18% | 5.47x |
| 10 | XBT/USD | 62.714 | 60752.8 | -0.10% | 0.66x |
| 11 | SUI/USD | 62.667 | 0.6558 | -0.06% | 1.33x |
| 12 | LINK/USD | 60.586 | 8.79675 | +0.19% | 3.34x |

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

- Persisted scans: 1302; predictions: 10543; observations: 788026.
- Matured sampled outcomes across 1/6/24/48h: 15482; gap abstentions: 22312. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45039524723 · **Generation:** 1302 · **Legacy run:** 45039524723
**Main quote time:** 2026-11-22T15:41:20.921846+00:00 · **Legacy report time:** 2026-11-22T15:42:25.594256+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04875 | 83.75 | +0.45% | 0.44x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 2 | DRV/USD | 0.36533 | 83.20 | -0.78% | 1.05x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 3 | NEAR/USD | 3.0031 | 81.01 | -0.07% | 1.02x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 4 | TAO/USD | 190.5806 | 78.73 | -0.18% | 5.47x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD | 25.539 | 77.93 | -0.31% | 1.93x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD ⭐ | 8.79675 | 76.56 | +0.19% | 3.34x | STRONG 93/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD | 62.93 | 74.35 | +0.40% | 0.88x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 8 | ETH/USD ⭐ | 1714.92 | 71.24 | +0.05% | 1.24x | STRONG 71/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6558 | 65.62 | -0.06% | 1.33x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | ZEC/USD | 795.61 | 61.03 | +0.01% | 0.21x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60752.8 | 58.82 | -0.10% | 0.66x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | STBL/USD | 0.016994 | 57.25 | -0.63% | 0.48x | WEAK 29/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 8.80681 | 78.79 | +0.19% | 3.34x | 4848 | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | ETH/USD ⭐ | 1715.86 | 76.97 | +0.05% | 1.24x | 39383 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LINK/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
