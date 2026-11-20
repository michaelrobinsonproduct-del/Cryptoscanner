# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T11:50:42.714392+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44730726972
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 868411b316f3d74615d5a2e5874e021c6dba2ad4 (atomic ledger/results publication)
**Ledger generation:** 974 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021938 | 53.314 | 50.405 | +3.05% | +0.18% | 1.20x | 7.7 | 2026-11-20T11:50:38.898897+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 2 | AERO/USD | 0.4174 | 42.083 | 33.203 | +0.58% | -0.29% | 2.03x | 7.2 | 2026-11-20T11:50:38.898897+00:00 | Not calibrated | MODERATE 51/100 | HIGH 66/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.4313 | 37.963 | 34.837 | +1.22% | -0.23% | 1.43x | 23.2 | 2026-11-20T11:50:38.898897+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 4 | BMT/USD | 0.02065 | 22.981 | 34.105 | +2.84% | -0.91% | 0.34x | 33.9 | 2026-11-20T11:50:38.898897+00:00 | Not calibrated | WEAK 6/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 50.405 | 0.021938 | +0.18% | 1.20x |
| 2 | ICNT/USD | 34.837 | 0.4313 | -0.23% | 1.43x |
| 3 | BMT/USD | 34.105 | 0.02065 | -0.91% | 0.34x |
| 4 | AERO/USD | 33.203 | 0.4174 | -0.29% | 2.03x |

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

- Persisted scans: 974; predictions: 8201; observations: 588572.
- Matured sampled outcomes across 1/6/24/48h: 9850; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44730726972 · **Generation:** 974 · **Legacy run:** 44730726972
**Main quote time:** 2026-11-20T11:50:42.714392+00:00 · **Legacy report time:** 2026-11-20T11:51:48.118855+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021938 | 53.31 | +0.18% | 1.20x | MODERATE 62/100 | HIGH 67/100 | Watch |
| 2 | AERO/USD | 0.4174 | 42.08 | -0.29% | 2.03x | MODERATE 51/100 | HIGH 66/100 | Watch |
| 3 | ICNT/USD | 0.4313 | 37.96 | -0.23% | 1.43x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |
| 4 | BMT/USD | 0.02065 | 22.98 | -0.91% | 0.34x | WEAK 6/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021938 | 61.69 | +0.18% | 1.20x | 8217 | MODERATE 66/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
