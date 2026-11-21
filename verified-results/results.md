# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T10:40:43.483124+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44895382851
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 6afd5aa0cfcb168f4b88cf53b6dc2e259de26275 (atomic ledger/results publication)
**Ledger generation:** 1122 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.833 | 99.076 | 87.805 | +5.28% | -0.13% | 2.19x | 8.2 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 468.93 | 82.353 | 67.129 | +2.77% | +1.02% | 2.01x | 14.5 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | STRONG 91/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | TRX/USD | 0.302631 | 72.471 | 57.385 | +0.37% | +0.02% | 2.87x | 0.5 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1637.75 | 59.530 | 62.936 | +1.14% | +0.03% | 0.64x | 0.1 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SENT/USD | 0.020788 | 42.393 | 31.744 | +0.94% | +0.14% | 1.99x | 11.6 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.07611 | 34.689 | 43.015 | +2.16% | -0.18% | 0.26x | 23.5 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | WEAK 12/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | ZAMA/USD | 0.05791 | 26.269 | 37.346 | +1.58% | -0.46% | 0.12x | 10.4 | 2026-11-21T10:40:38.657525+00:00 | Not calibrated | WEAK 13/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 87.805 | 21.833 | -0.13% | 2.19x |
| 2 | XMR/USD | 67.129 | 468.93 | +1.02% | 2.01x |
| 3 | ETH/USD | 62.936 | 1637.75 | +0.03% | 0.64x |
| 4 | TRX/USD | 57.385 | 0.302631 | +0.02% | 2.87x |
| 5 | USELESS/USD | 43.015 | 0.07611 | -0.18% | 0.26x |
| 6 | ZAMA/USD | 37.346 | 0.05791 | -0.46% | 0.12x |
| 7 | SENT/USD | 31.744 | 0.020788 | +0.14% | 1.99x |

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

- Persisted scans: 1122; predictions: 8803; observations: 678535.
- Matured sampled outcomes across 1/6/24/48h: 11584; gap abstentions: 20327. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44895382851 · **Generation:** 1122 · **Legacy run:** 44895382851
**Main quote time:** 2026-11-21T10:40:43.483124+00:00 · **Legacy report time:** 2026-11-21T10:41:32.959615+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.833 | 99.08 | -0.13% | 2.19x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD ⭐ | 468.93 | 82.35 | +1.02% | 2.01x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | TRX/USD | 0.302631 | 72.47 | +0.02% | 2.87x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1637.75 | 59.53 | +0.03% | 0.64x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 5 | SENT/USD ⭐ | 0.020788 | 42.39 | +0.14% | 1.99x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 6 | USELESS/USD | 0.07611 | 34.69 | -0.18% | 0.26x | WEAK 12/100 | EXTREME 88/100 | Do nothing |
| 7 | ZAMA/USD | 0.05791 | 26.27 | -0.46% | 0.12x | WEAK 13/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 468.04 | 75.07 | +1.02% | 2.01x | 11761 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.020788 | 40.70 | +0.14% | 1.99x | 4979 | MODERATE 65/100 | HIGH 67/100 | Watch |

**Same-run overlap:** XMR/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
