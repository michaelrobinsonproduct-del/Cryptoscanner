# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:25:39.350613+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44855726300
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 46da1fc829c2b55ce5ed0cfa5dce3c1abd5f5f22 (atomic ledger/results publication)
**Ledger generation:** 1064 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.4795 | 63.311 | 47.181 | +0.28% | +0.23% | 20.94x | 5.1 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | VVV/USD | 21.103 | 62.657 | 63.261 | +1.76% | -0.79% | 1.33x | 8.1 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0546139 | 61.382 | 59.343 | +0.62% | +0.14% | 1.14x | 0.1 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ADA/USD | 0.1433 | 61.268 | 55.427 | +0.32% | +0.06% | 1.55x | 3.6 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 5 | CAP/USD | 0.094286 | 48.968 | 52.132 | +3.00% | +0.38% | 0.49x | 4.4 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | PENGU/USD | 0.004356 | 44.630 | 32.534 | +0.28% | +0.74% | 1.84x | 4.6 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | MODERATE 67/100 | HIGH 60/100 | Watch | WATCH |
| 7 | ALGO/USD | 0.07354 | 40.836 | 39.019 | +0.52% | +0.16% | 1.10x | 6.8 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | MODERATE 45/100 | HIGH 62/100 | Watch | WATCH |
| 8 | DOT/USD | 0.6674 | 36.371 | 38.748 | +0.97% | +0.18% | 0.67x | 4.5 | 2026-11-21T02:25:30.426103+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 63.261 | 21.103 | -0.79% | 1.33x |
| 2 | XDG/USD | 59.343 | 0.0546139 | +0.14% | 1.14x |
| 3 | ADA/USD | 55.427 | 0.1433 | +0.06% | 1.55x |
| 4 | CAP/USD | 52.132 | 0.094286 | +0.38% | 0.49x |
| 5 | UNI/USD | 47.181 | 4.4795 | +0.23% | 20.94x |
| 6 | ALGO/USD | 39.019 | 0.07354 | +0.16% | 1.10x |
| 7 | DOT/USD | 38.748 | 0.6674 | +0.18% | 0.67x |
| 8 | PENGU/USD | 32.534 | 0.004356 | +0.74% | 1.84x |

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

- Persisted scans: 1064; predictions: 8542; observations: 643272.
- Matured sampled outcomes across 1/6/24/48h: 10975; gap abstentions: 19400. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44855726300 · **Generation:** 1064 · **Legacy run:** 44855726300
**Main quote time:** 2026-11-21T02:25:39.350613+00:00 · **Legacy report time:** 2026-11-21T02:26:40.070925+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.4795 | 63.31 | +0.23% | 20.94x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 21.103 | 62.66 | -0.79% | 1.33x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0546139 | 61.38 | +0.14% | 1.14x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD ⭐ | 0.1433 | 61.27 | +0.06% | 1.55x | STRONG 76/100 | HIGH 55/100 | Watch |
| 5 | CAP/USD | 0.094286 | 48.97 | +0.38% | 0.49x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 6 | PENGU/USD | 0.004356 | 44.63 | +0.74% | 1.84x | MODERATE 67/100 | HIGH 60/100 | Watch |
| 7 | ALGO/USD | 0.07354 | 40.84 | +0.16% | 1.10x | MODERATE 45/100 | HIGH 62/100 | Watch |
| 8 | DOT/USD | 0.6674 | 36.37 | +0.18% | 0.67x | WEAK 38/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0546468 | 59.86 | +0.14% | 1.14x | 11941 | MODERATE 65/100 | HIGH 62/100 | Watch |
| 2 | UNI/USD ⭐ | 4.4836 | 54.08 | +0.23% | 20.94x | 8902 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.143345 | 50.19 | +0.06% | 1.55x | 17096 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UNI/USD, XDG/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
