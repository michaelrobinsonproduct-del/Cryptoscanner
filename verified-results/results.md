# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T07:57:45.326443+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46123338811
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ff898e727af3ab95b87fe6483258af156036d975 (atomic ledger/results publication)
**Ledger generation:** 2126 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 422.76 | 79.362 | 77.720 | +3.80% | +0.16% | 1.08x | 7.8 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05045 | 67.764 | 52.963 | +0.42% | -0.04% | 15.30x | 9.9 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004338 | 60.746 | 51.792 | +3.83% | -1.21% | 2.90x | 11.5 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 4 | HYPE/USD | 63.9 | 52.815 | 57.956 | +0.65% | +0.14% | 0.42x | 3.1 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | VVV/USD | 26.349 | 51.182 | 56.842 | +2.33% | -0.11% | 0.49x | 7.6 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | ZEC/USD | 736.54 | 47.032 | 54.909 | +0.27% | +0.06% | 0.18x | 3.9 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SEI/USD | 0.0386 | 36.430 | 31.995 | +0.49% | -0.13% | 1.51x | 7.8 | 2026-11-28T07:57:41.403468+00:00 | Not calibrated | WEAK 38/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 77.720 | 422.76 | +0.16% | 1.08x |
| 2 | HYPE/USD | 57.956 | 63.9 | +0.14% | 0.42x |
| 3 | VVV/USD | 56.842 | 26.349 | -0.11% | 0.49x |
| 4 | ZEC/USD | 54.909 | 736.54 | +0.06% | 0.18x |
| 5 | NIGHT/USD | 52.963 | 0.05045 | -0.04% | 15.30x |
| 6 | SPACE/USD | 51.792 | 0.004338 | -1.21% | 2.90x |
| 7 | SEI/USD | 31.995 | 0.0386 | -0.13% | 1.51x |

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

- Persisted scans: 2126; predictions: 19044; observations: 1287402.
- Matured sampled outcomes across 1/6/24/48h: 44755; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46123338811 · **Generation:** 2126 · **Legacy run:** 46123338811
**Main quote time:** 2026-11-28T07:57:45.326443+00:00 · **Legacy report time:** 2026-11-28T07:58:42.616983+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 422.76 | 79.36 | +0.16% | 1.08x | STRONG 75/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD | 0.05045 | 67.76 | -0.04% | 15.30x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | SPACE/USD | 0.004338 | 60.75 | -1.21% | 2.90x | MODERATE 55/100 | VERY_HIGH 83/100 | Do nothing |
| 4 | HYPE/USD | 63.9 | 52.82 | +0.14% | 0.42x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 5 | VVV/USD | 26.349 | 51.18 | -0.11% | 0.49x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | ZEC/USD | 736.54 | 47.03 | +0.06% | 0.18x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 7 | SEI/USD | 0.0386 | 36.43 | -0.13% | 1.51x | WEAK 38/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 422.75 | 84.22 | +0.16% | 1.08x | 14764 | STRONG 77/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
