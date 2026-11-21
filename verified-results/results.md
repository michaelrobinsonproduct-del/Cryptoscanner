# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T10:10:46.642995+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44892982482
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** b83f85da56fc9c1034f90e908415282fae85ba4b (atomic ledger/results publication)
**Ledger generation:** 1119 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.679 | 95.409 | 82.109 | +4.53% | -0.31% | 2.49x | 9.2 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ETH/USD | 1635.68 | 72.937 | 62.011 | +1.01% | -0.08% | 2.13x | 0.1 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TRX/USD | 0.302431 | 58.040 | 57.136 | +0.31% | -0.02% | 1.10x | 0.0 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XMR/USD | 463.2 | 55.820 | 58.256 | +1.51% | +0.21% | 0.65x | 14.7 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.07566 | 37.998 | 36.550 | +1.56% | +1.38% | 0.46x | 27.8 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | ZAMA/USD | 0.05824 | 35.675 | 44.862 | +2.16% | -0.51% | 0.34x | 3.4 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | BEAM/USD | 0.003304 | 21.694 | 29.427 | +0.79% | +0.03% | 0.21x | 15.1 | 2026-11-21T10:10:39.894572+00:00 | Not calibrated | WEAK 26/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.109 | 21.679 | -0.31% | 2.49x |
| 2 | ETH/USD | 62.011 | 1635.68 | -0.08% | 2.13x |
| 3 | XMR/USD | 58.256 | 463.2 | +0.21% | 0.65x |
| 4 | TRX/USD | 57.136 | 0.302431 | -0.02% | 1.10x |
| 5 | ZAMA/USD | 44.862 | 0.05824 | -0.51% | 0.34x |
| 6 | USELESS/USD | 36.550 | 0.07566 | +1.38% | 0.46x |
| 7 | BEAM/USD | 29.427 | 0.003304 | +0.03% | 0.21x |

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

- Persisted scans: 1119; predictions: 8782; observations: 676711.
- Matured sampled outcomes across 1/6/24/48h: 11560; gap abstentions: 20315. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44892982482 · **Generation:** 1119 · **Legacy run:** 44892982482
**Main quote time:** 2026-11-21T10:10:46.642995+00:00 · **Legacy report time:** 2026-11-21T10:11:38.079319+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.679 | 95.41 | -0.31% | 2.49x | STRONG 78/100 | HIGH 61/100 | Watch |
| 2 | ETH/USD | 1635.68 | 72.94 | -0.08% | 2.13x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | TRX/USD | 0.302431 | 58.04 | -0.02% | 1.10x | WEAK 39/100 | HIGH 68/100 | Watch |
| 4 | XMR/USD | 463.2 | 55.82 | +0.21% | 0.65x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 5 | USELESS/USD | 0.07566 | 38.00 | +1.38% | 0.46x | WEAK 39/100 | VERY_HIGH 82/100 | Watch |
| 6 | ZAMA/USD | 0.05824 | 35.67 | -0.51% | 0.34x | WEAK 23/100 | EXTREME 88/100 | Do nothing |
| 7 | BEAM/USD | 0.003304 | 21.69 | +0.03% | 0.21x | WEAK 26/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
