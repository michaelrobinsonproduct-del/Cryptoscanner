# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T05:17:48.187787+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46111195691
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 39fe7355323f08e6249ea235a51d4d3139e84bc9 (atomic ledger/results publication)
**Ledger generation:** 2110 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKE/USD | 0.00112795 | 70.245 | 41.239 | +3.82% | +2.80% | 2.66x | 42.4 | 2026-11-28T05:17:44.545688+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | ZEC/USD | 740.45 | 69.942 | 58.575 | +0.80% | -0.73% | 19.53x | 4.1 | 2026-11-28T05:17:44.545688+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 416.65 | 67.864 | 66.442 | +2.30% | -0.19% | 1.24x | 9.4 | 2026-11-28T05:17:44.545688+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SENT/USD | 0.024642 | 54.927 | 55.099 | +3.91% | +0.71% | 0.63x | 6.5 | 2026-11-28T05:17:44.545688+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | VVV/USD | 26.212 | 49.886 | 54.889 | +1.80% | -0.54% | 0.77x | 7.6 | 2026-11-28T05:17:44.545688+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | BCH/USD | 207.56 | 49.627 | 36.260 | +0.27% | -0.33% | 7.01x | 3.4 | 2026-11-28T05:17:44.545688+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 66.442 | 416.65 | -0.19% | 1.24x |
| 2 | ZEC/USD | 58.575 | 740.45 | -0.73% | 19.53x |
| 3 | SENT/USD | 55.099 | 0.024642 | +0.71% | 0.63x |
| 4 | VVV/USD | 54.889 | 26.212 | -0.54% | 0.77x |
| 5 | AKE/USD | 41.239 | 0.00112795 | +2.80% | 2.66x |
| 6 | BCH/USD | 36.260 | 207.56 | -0.33% | 7.01x |

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

- Persisted scans: 2110; predictions: 18942; observations: 1277706.
- Matured sampled outcomes across 1/6/24/48h: 44097; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46111195691 · **Generation:** 2110 · **Legacy run:** 46111195691
**Main quote time:** 2026-11-28T05:17:48.187787+00:00 · **Legacy report time:** 2026-11-28T05:18:45.587646+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD | 0.00112795 | 70.25 | +2.80% | 2.66x | STRONG 75/100 | VERY_HIGH 82/100 | Watch |
| 2 | ZEC/USD | 740.45 | 69.94 | -0.73% | 19.53x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 416.65 | 67.86 | -0.19% | 1.24x | WEAK 44/100 | HIGH 68/100 | Watch |
| 4 | SENT/USD | 0.024642 | 54.93 | +0.71% | 0.63x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 5 | VVV/USD | 26.212 | 49.89 | -0.54% | 0.77x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 6 | BCH/USD | 207.56 | 49.63 | -0.33% | 7.01x | MODERATE 55/100 | HIGH 66/100 | Watch |

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
