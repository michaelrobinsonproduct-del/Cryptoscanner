# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T07:47:28.032319+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46122589058
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** efa43999f341535ebb31ac4206907469309ca154 (atomic ledger/results publication)
**Ledger generation:** 2125 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 423.7 | 78.896 | 79.933 | +4.03% | -0.17% | 0.98x | 6.6 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004353 | 70.603 | 55.487 | +4.19% | +0.02% | 2.52x | 9.2 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05059 | 69.255 | 51.970 | +0.70% | +0.46% | 6.36x | 15.8 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0298 | 65.231 | 56.535 | +0.38% | -0.42% | 2.08x | 2.3 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZEC/USD | 738.23 | 61.694 | 56.727 | +0.50% | -0.15% | 1.57x | 3.5 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 6 | VVV/USD | 26.305 | 52.396 | 54.852 | +2.16% | +0.26% | 0.62x | 9.1 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 63.97 | 51.913 | 59.510 | +0.76% | +0.24% | 0.12x | 1.6 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.07535 | 36.319 | 40.856 | +1.62% | +0.24% | 0.43x | 9.3 | 2026-11-28T07:47:23.223231+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 79.933 | 423.7 | -0.17% | 0.98x |
| 2 | HYPE/USD | 59.510 | 63.97 | +0.24% | 0.12x |
| 3 | ZEC/USD | 56.727 | 738.23 | -0.15% | 1.57x |
| 4 | NEAR/USD | 56.535 | 3.0298 | -0.42% | 2.08x |
| 5 | SPACE/USD | 55.487 | 0.004353 | +0.02% | 2.52x |
| 6 | VVV/USD | 54.852 | 26.305 | +0.26% | 0.62x |
| 7 | NIGHT/USD | 51.970 | 0.05059 | +0.46% | 6.36x |
| 8 | CC/USD | 40.856 | 0.07535 | +0.24% | 0.43x |

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

- Persisted scans: 2125; predictions: 19037; observations: 1286796.
- Matured sampled outcomes across 1/6/24/48h: 44704; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46122589058 · **Generation:** 2125 · **Legacy run:** 46122589058
**Main quote time:** 2026-11-28T07:47:28.032319+00:00 · **Legacy report time:** 2026-11-28T07:48:06.385559+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 423.7 | 78.90 | -0.17% | 0.98x | WEAK 44/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD | 0.004353 | 70.60 | +0.02% | 2.52x | STRONG 80/100 | HIGH 67/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05059 | 69.25 | +0.46% | 6.36x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 4 | NEAR/USD | 3.0298 | 65.23 | -0.42% | 2.08x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | ZEC/USD | 738.23 | 61.69 | -0.15% | 1.57x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 6 | VVV/USD | 26.305 | 52.40 | +0.26% | 0.62x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD | 63.97 | 51.91 | +0.24% | 0.12x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.07535 | 36.32 | +0.24% | 0.43x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05067 | 56.64 | +0.46% | 6.36x | 18823 | STRONG 88/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
