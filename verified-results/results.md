# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T04:11:02.552954+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44983799220
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 9e021eca8fd68f7799bda96089bf61feeb9b6551 (atomic ledger/results publication)
**Ledger generation:** 1231 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUMP/USD | 0.89 | 53.939 | 32.097 | +0.45% | +1.37% | 2.89x | 11.2 | 2026-11-22T04:10:58.148888+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.9698 | 39.922 | 36.002 | +1.10% | +0.22% | 1.28x | 29.0 | 2026-11-22T04:10:58.148888+00:00 | Not calibrated | MODERATE 45/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 3.4157 | 36.083 | 30.175 | +0.37% | +1.24% | 0.97x | 12.6 | 2026-11-22T04:10:58.148888+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | SPX/USD | 0.2813 | 26.827 | 28.637 | +0.68% | -0.39% | 1.01x | 17.8 | 2026-11-22T04:10:58.148888+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 36.002 | 1.9698 | +0.22% | 1.28x |
| 2 | TRUMP/USD | 32.097 | 0.89 | +1.37% | 2.89x |
| 3 | PIEVERSE/USD | 30.175 | 3.4157 | +1.24% | 0.97x |
| 4 | SPX/USD | 28.637 | 0.2813 | -0.39% | 1.01x |

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

- Persisted scans: 1231; predictions: 9899; observations: 744806.
- Matured sampled outcomes across 1/6/24/48h: 13943; gap abstentions: 21948. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 31 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44983799220 · **Generation:** 1231 · **Legacy run:** 44983799220
**Main quote time:** 2026-11-22T04:11:02.552954+00:00 · **Legacy report time:** 2026-11-22T04:12:06.341378+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUMP/USD ⭐ | 0.89 | 53.94 | +1.37% | 2.89x | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.9698 | 39.92 | +0.22% | 1.28x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 3 | PIEVERSE/USD | 3.4157 | 36.08 | +1.24% | 0.97x | WEAK 43/100 | VERY_HIGH 73/100 | Watch |
| 4 | SPX/USD | 0.2813 | 26.83 | -0.39% | 1.01x | WEAK 18/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUMP/USD ⭐ | 0.896 | 49.97 | +1.37% | 2.89x | 2933 | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.9699 | 44.77 | +0.22% | 1.28x | 9301 | MODERATE 57/100 | HIGH 67/100 | Watch |
| 3 | VVV/USD | 24.933 | 43.38 | +0.52% | 1.80x | 15288 | MODERATE 67/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD | 0.04453 | 42.22 | +0.77% | 1.01x | 10208 | MODERATE 51/100 | HIGH 68/100 | Watch |

**Same-run overlap:** TRUMP/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
