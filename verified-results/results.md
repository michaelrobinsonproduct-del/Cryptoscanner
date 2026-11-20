# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T10:41:03.900926+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44721094625
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 776cf0063764d664fcc2e329a5be822b55b2e09f (atomic ledger/results publication)
**Ledger generation:** 967 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022124 | 86.790 | 56.578 | +3.92% | +3.57% | 2.24x | 8.1 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | STRONG 98/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XBT/USD | 62157.4 | 75.782 | 57.749 | +0.39% | +0.61% | 3.05x | 0.0 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.96561 | 56.811 | 59.589 | +0.66% | +0.57% | 0.44x | 0.1 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XLM/USD | 0.13352 | 53.949 | 58.352 | +0.62% | +0.58% | 0.27x | 1.9 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | HBAR/USD | 0.05424 | 47.628 | 43.780 | +0.89% | +1.14% | 0.82x | 5.5 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.012354 | 42.108 | 24.931 | +1.35% | +1.50% | 1.97x | 34.8 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.4277 | 33.582 | 22.084 | +0.38% | +2.80% | 0.75x | 37.4 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 8 | SKR/USD | 0.010171 | 31.089 | 34.712 | +1.24% | -0.25% | 0.76x | 10.8 | 2026-11-20T10:40:57.382075+00:00 | Not calibrated | WEAK 16/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 59.589 | 0.96561 | +0.57% | 0.44x |
| 2 | XLM/USD | 58.352 | 0.13352 | +0.58% | 0.27x |
| 3 | XBT/USD | 57.749 | 62157.4 | +0.61% | 3.05x |
| 4 | SENT/USD | 56.578 | 0.022124 | +3.57% | 2.24x |
| 5 | HBAR/USD | 43.780 | 0.05424 | +1.14% | 0.82x |
| 6 | SKR/USD | 34.712 | 0.010171 | -0.25% | 0.76x |
| 7 | BLESS/USD | 24.931 | 0.012354 | +1.50% | 1.97x |
| 8 | ICNT/USD | 22.084 | 0.4277 | +2.80% | 0.75x |

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

- Persisted scans: 967; predictions: 8165; observations: 584323.
- Matured sampled outcomes across 1/6/24/48h: 9807; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44721094625 · **Generation:** 967 · **Legacy run:** 44721094625
**Main quote time:** 2026-11-20T10:41:03.900926+00:00 · **Legacy report time:** 2026-11-20T10:41:52.948625+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022124 | 86.79 | +3.57% | 2.24x | STRONG 100/100 | VERY_HIGH 70/100 | Watch |
| 2 | XBT/USD ⭐ | 62157.4 | 75.78 | +0.61% | 3.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD | 0.96561 | 56.81 | +0.57% | 0.44x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | XLM/USD | 0.13352 | 53.95 | +0.58% | 0.27x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | HBAR/USD | 0.05424 | 47.63 | +1.14% | 0.82x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 6 | BLESS/USD ⭐ | 0.012354 | 42.11 | +1.50% | 1.97x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 7 | ICNT/USD | 0.4277 | 33.58 | +2.80% | 0.75x | WEAK 32/100 | VERY_HIGH 74/100 | Do nothing |
| 8 | SKR/USD | 0.010171 | 31.09 | -0.25% | 0.76x | WEAK 16/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022116 | 83.48 | +3.57% | 2.24x | 8881 | STRONG 100/100 | VERY_HIGH 76/100 | Watch |
| 2 | XBT/USD ⭐ | 62167.6 | 66.71 | +0.61% | 3.05x | 157536 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD | 1757.2 | 56.78 | +0.47% | 1.55x | 68290 | STRONG 73/100 | HIGH 55/100 | Watch |
| 4 | BLESS/USD ⭐ | 0.012411 | 47.37 | +1.50% | 1.97x | 1859 | MODERATE 69/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** SENT/USD, XBT/USD, BLESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
