# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T00:25:28.150561+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44843618134
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 26847a27d3a40eec55c39131065d53966d17cabd (atomic ledger/results publication)
**Ledger generation:** 1045 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5057 | 48.856 | 30.372 | +0.36% | +0.70% | 3.10x | 9.9 | 2026-11-21T00:25:23.186065+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 2 | CAP/USD | 0.091954 | 45.107 | 35.264 | +0.45% | -0.13% | 2.05x | 1.2 | 2026-11-21T00:25:23.186065+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 3 | DRV/USD | 0.24656 | 41.011 | 35.611 | +0.42% | +0.29% | 1.39x | 5.3 | 2026-11-21T00:25:23.186065+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |
| 4 | BLUR/USD | 0.00734 | 20.867 | 22.129 | +0.55% | +0.82% | 0.46x | 27.4 | 2026-11-21T00:25:23.186065+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | ZBCN/USD | 0.001598 | 19.392 | 25.739 | +0.44% | -0.06% | 0.40x | 18.8 | 2026-11-21T00:25:23.186065+00:00 | Not calibrated | WEAK 10/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 35.611 | 0.24656 | +0.29% | 1.39x |
| 2 | CAP/USD | 35.264 | 0.091954 | -0.13% | 2.05x |
| 3 | AKT/USD | 30.372 | 0.5057 | +0.70% | 3.10x |
| 4 | ZBCN/USD | 25.739 | 0.001598 | -0.06% | 0.40x |
| 5 | BLUR/USD | 22.129 | 0.00734 | +0.82% | 0.46x |

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

- Persisted scans: 1045; predictions: 8353; observations: 631720.
- Matured sampled outcomes across 1/6/24/48h: 10927; gap abstentions: 18994. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44843618134 · **Generation:** 1045 · **Legacy run:** 44843618134
**Main quote time:** 2026-11-21T00:25:28.150561+00:00 · **Legacy report time:** 2026-11-21T00:26:17.953497+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5057 | 48.86 | +0.70% | 3.10x | STRONG 89/100 | HIGH 60/100 | Consider small entry |
| 2 | CAP/USD | 0.091954 | 45.11 | -0.13% | 2.05x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 3 | DRV/USD ⭐ | 0.24656 | 41.01 | +0.29% | 1.39x | STRONG 76/100 | HIGH 60/100 | Watch |
| 4 | BLUR/USD | 0.00734 | 20.87 | +0.82% | 0.46x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 5 | ZBCN/USD | 0.001598 | 19.39 | -0.06% | 0.40x | WEAK 10/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD | 68.83 | 54.83 | +0.10% | 1.83x | 43630 | MODERATE 62/100 | HIGH 55/100 | Watch |
| 2 | DRV/USD ⭐ | 0.24688 | 46.78 | +0.29% | 1.39x | 5957 | STRONG 78/100 | HIGH 60/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5061 | 39.02 | +0.70% | 3.10x | 4595 | STRONG 85/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** AKT/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
