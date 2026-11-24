# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T03:41:15.117506+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45321033070
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 17eb9e8552adcd895e79ff7e9abec91753749fc0 (atomic ledger/results publication)
**Ledger generation:** 1520 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01235 | 88.147 | 76.353 | +7.20% | +2.32% | 1.02x | 16.2 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | STRONG 74/100 | HIGH 68/100 | Watch | WATCH |
| 2 | AI/USD | 0.01609 | 70.984 | 67.566 | +5.65% | +1.77% | 0.46x | 6.2 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94526 | 69.794 | 58.792 | +0.62% | +0.81% | 1.69x | 1.2 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | INX/USD | 0.004018 | 59.405 | 43.038 | +3.08% | +3.19% | 1.04x | 19.8 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 90/100 | Do nothing | WATCH |
| 5 | BAT/USD | 0.07835 | 55.030 | 36.179 | +1.53% | +0.77% | 2.63x | 12.8 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.449e-06 | 53.718 | 51.803 | +0.79% | +0.97% | 0.71x | 5.8 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04859 | 47.356 | 51.523 | +0.91% | +0.39% | 0.39x | 8.2 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | BABY/USD | 0.00865 | 39.765 | 37.618 | +1.76% | +1.28% | 0.57x | 11.6 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | FIL/USD | 0.554 | 29.839 | 26.685 | +0.36% | +1.09% | 0.77x | 18.1 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | XTZ/USD | 0.21474 | 29.309 | 32.637 | +0.88% | +0.29% | 0.52x | 8.9 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | ACU/USD | 0.1115 | 23.841 | 23.753 | +0.27% | +0.00% | 1.01x | 18.0 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 12 | XDC/USD | 0.0261 | 20.255 | 30.890 | +0.46% | -1.14% | 0.51x | 15.4 | 2026-11-24T03:41:08.848568+00:00 | Not calibrated | WEAK 10/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.353 | 0.01235 | +2.32% | 1.02x |
| 2 | AI/USD | 67.566 | 0.01609 | +1.77% | 0.46x |
| 3 | XRP/USD | 58.792 | 0.94526 | +0.81% | 1.69x |
| 4 | PEPE/USD | 51.803 | 3.449e-06 | +0.97% | 0.71x |
| 5 | NIGHT/USD | 51.523 | 0.04859 | +0.39% | 0.39x |
| 6 | INX/USD | 43.038 | 0.004018 | +3.19% | 1.04x |
| 7 | BABY/USD | 37.618 | 0.00865 | +1.28% | 0.57x |
| 8 | BAT/USD | 36.179 | 0.07835 | +0.77% | 2.63x |
| 9 | XTZ/USD | 32.637 | 0.21474 | +0.29% | 0.52x |
| 10 | XDC/USD | 30.890 | 0.0261 | -1.14% | 0.51x |
| 11 | FIL/USD | 26.685 | 0.554 | +1.09% | 0.77x |
| 12 | ACU/USD | 23.753 | 0.1115 | +0.00% | 1.01x |

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

- Persisted scans: 1520; predictions: 12976; observations: 920778.
- Matured sampled outcomes across 1/6/24/48h: 24128; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45321033070 · **Generation:** 1520 · **Legacy run:** 45321033070
**Main quote time:** 2026-11-24T03:41:15.117506+00:00 · **Legacy report time:** 2026-11-24T03:41:59.785169+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01235 | 88.15 | +2.32% | 1.02x | STRONG 84/100 | HIGH 68/100 | Watch |
| 2 | AI/USD | 0.01609 | 70.98 | +1.77% | 0.46x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 3 | XRP/USD ⭐ | 0.94526 | 69.79 | +0.81% | 1.69x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 4 | INX/USD ⭐ | 0.004018 | 59.40 | +3.19% | 1.04x | STRONG 70/100 | EXTREME 90/100 | Do nothing |
| 5 | BAT/USD ⭐ | 0.07835 | 55.03 | +0.77% | 2.63x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 6 | PEPE/USD | 3.449e-06 | 53.72 | +0.97% | 0.71x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | NIGHT/USD | 0.04859 | 47.36 | +0.39% | 0.39x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 8 | BABY/USD | 0.00865 | 39.77 | +1.28% | 0.57x | MODERATE 45/100 | EXTREME 88/100 | Do nothing |
| 9 | FIL/USD | 0.554 | 29.84 | +1.09% | 0.77x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 10 | XTZ/USD | 0.21474 | 29.31 | +0.29% | 0.52x | MODERATE 45/100 | VERY_HIGH 82/100 | Watch |
| 11 | ACU/USD | 0.1115 | 23.84 | +0.00% | 1.01x | WEAK 32/100 | VERY_HIGH 80/100 | Do nothing |
| 12 | XDC/USD | 0.0261 | 20.25 | -1.14% | 0.51x | WEAK 10/100 | EXTREME 91/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01239 | 82.73 | +2.32% | 1.02x | 8250 | STRONG 81/100 | HIGH 68/100 | Watch |
| 2 | INX/USD ⭐ | 0.004031 | 71.96 | +3.19% | 1.04x | 2781 | STRONG 76/100 | EXTREME 90/100 | Do nothing |
| 3 | XRP/USD ⭐ | 0.94581 | 65.20 | +0.81% | 1.69x | 46674 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 4 | BAT/USD ⭐ | 0.07843 | 51.56 | +0.77% | 2.63x | 3027 | STRONG 81/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** MON/USD, XRP/USD, INX/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
