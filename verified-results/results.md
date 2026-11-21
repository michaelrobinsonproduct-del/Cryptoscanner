# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T06:50:33.857475+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44877370002
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 94bc93b46136ad772b05c54caff1c360d13d3006 (atomic ledger/results publication)
**Ledger generation:** 1098 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.633 | 117.557 | 77.557 | +4.31% | +6.11% | 15.10x | 15.2 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | ETH/USD | 1637.98 | 95.764 | 61.478 | +1.15% | +3.86% | 2.78x | 3.2 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 3 | DRV/USD | 0.26197 | 85.477 | 75.867 | +6.69% | +1.47% | 1.23x | 14.1 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | STRONG 73/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.05803 | 68.629 | 36.796 | +1.79% | +3.37% | 3.05x | 13.9 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 5 | XPL/USD | 0.046 | 61.332 | 30.707 | +0.66% | +3.12% | 3.73x | 21.7 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 6 | DCR/USD | 10.16 | 55.018 | 30.155 | +0.54% | +1.97% | 5.83x | 8.9 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Watch | WATCH |
| 7 | PI/USD | 0.05033 | 39.105 | 28.269 | +0.46% | +2.07% | 1.05x | 12.0 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | CAP/USD | 0.09306 | 37.721 | 42.231 | +1.66% | +0.32% | 0.39x | 6.1 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | BLUR/USD | 0.00732 | 29.473 | 20.114 | +0.27% | +2.38% | 0.75x | 27.5 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | RARE/USD | 0.01377 | 19.145 | 42.043 | +3.53% | -3.23% | 0.33x | 29.1 | 2026-11-21T06:50:27.130621+00:00 | Not calibrated | WEAK 5/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.557 | 21.633 | +6.11% | 15.10x |
| 2 | DRV/USD | 75.867 | 0.26197 | +1.47% | 1.23x |
| 3 | ETH/USD | 61.478 | 1637.98 | +3.86% | 2.78x |
| 4 | CAP/USD | 42.231 | 0.09306 | +0.32% | 0.39x |
| 5 | RARE/USD | 42.043 | 0.01377 | -3.23% | 0.33x |
| 6 | ZAMA/USD | 36.796 | 0.05803 | +3.37% | 3.05x |
| 7 | XPL/USD | 30.707 | 0.046 | +3.12% | 3.73x |
| 8 | DCR/USD | 30.155 | 10.16 | +1.97% | 5.83x |
| 9 | PI/USD | 28.269 | 0.05033 | +2.07% | 1.05x |
| 10 | BLUR/USD | 20.114 | 0.00732 | +2.38% | 0.75x |

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

- Persisted scans: 1098; predictions: 8647; observations: 663943.
- Matured sampled outcomes across 1/6/24/48h: 11225; gap abstentions: 20094. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44877370002 · **Generation:** 1098 · **Legacy run:** 44877370002
**Main quote time:** 2026-11-21T06:50:33.857475+00:00 · **Legacy report time:** 2026-11-21T06:51:15.558625+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.633 | 117.56 | +6.11% | 15.10x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 2 | ETH/USD ⭐ | 1637.98 | 95.76 | +3.86% | 2.78x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 3 | DRV/USD ⭐ | 0.26197 | 85.48 | +1.47% | 1.23x | STRONG 83/100 | HIGH 68/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.05803 | 68.63 | +3.37% | 3.05x | STRONG 94/100 | VERY_HIGH 83/100 | Watch |
| 5 | XPL/USD ⭐ | 0.046 | 61.33 | +3.12% | 3.73x | STRONG 86/100 | VERY_HIGH 77/100 | Watch |
| 6 | DCR/USD ⭐ | 10.16 | 55.02 | +1.97% | 5.83x | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 7 | PI/USD | 0.05033 | 39.11 | +2.07% | 1.05x | MODERATE 50/100 | VERY_HIGH 80/100 | Watch |
| 8 | CAP/USD | 0.09306 | 37.72 | +0.32% | 0.39x | MODERATE 49/100 | VERY_HIGH 75/100 | Watch |
| 9 | BLUR/USD | 0.00732 | 29.47 | +2.38% | 0.75x | WEAK 35/100 | EXTREME 87/100 | Do nothing |
| 10 | RARE/USD | 0.01377 | 19.14 | -3.23% | 0.33x | WEAK 5/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.773 | 100.00 | +6.11% | 15.10x | 13820 | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 2 | ETH/USD ⭐ | 1650.34 | 81.25 | +3.86% | 2.78x | 95343 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 3 | DRV/USD ⭐ | 0.26333 | 80.11 | +1.47% | 1.23x | 8705 | STRONG 80/100 | HIGH 68/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.05809 | 59.69 | +3.37% | 3.05x | 2428 | STRONG 90/100 | VERY_HIGH 83/100 | Watch |
| 5 | XPL/USD ⭐ | 0.0463 | 55.43 | +3.12% | 3.73x | 2334 | STRONG 83/100 | VERY_HIGH 77/100 | Watch |
| 6 | DCR/USD ⭐ | 10.16 | 39.22 | +1.97% | 5.83x | 2196 | STRONG 85/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** VVV/USD, ETH/USD, DRV/USD, ZAMA/USD, XPL/USD, DCR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
