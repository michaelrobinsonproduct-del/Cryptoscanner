# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T08:07:54.168315+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46124101347
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** abfb85d5c47fec5c7cddf02708cc26974743af5b (atomic ledger/results publication)
**Ledger generation:** 2127 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05051 | 72.474 | 56.779 | +0.54% | +0.14% | 10.10x | 4.0 | 2026-11-28T08:07:51.067093+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004393 | 72.310 | 62.210 | +5.15% | +1.69% | 1.16x | 9.1 | 2026-11-28T08:07:51.067093+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | XMR/USD | 422.61 | 71.933 | 72.120 | +3.77% | -0.72% | 1.34x | 18.5 | 2026-11-28T08:07:51.067093+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 4 | VVV/USD | 26.607 | 70.431 | 63.800 | +3.33% | +0.69% | 1.32x | 8.3 | 2026-11-28T08:07:51.067093+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.9 | 54.381 | 58.737 | +0.65% | -0.22% | 0.67x | 1.6 | 2026-11-28T08:07:51.067093+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 72.120 | 422.61 | -0.72% | 1.34x |
| 2 | VVV/USD | 63.800 | 26.607 | +0.69% | 1.32x |
| 3 | SPACE/USD | 62.210 | 0.004393 | +1.69% | 1.16x |
| 4 | HYPE/USD | 58.737 | 63.9 | -0.22% | 0.67x |
| 5 | NIGHT/USD | 56.779 | 0.05051 | +0.14% | 10.10x |

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

- Persisted scans: 2127; predictions: 19049; observations: 1288008.
- Matured sampled outcomes across 1/6/24/48h: 44797; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46124101347 · **Generation:** 2127 · **Legacy run:** 46124101347
**Main quote time:** 2026-11-28T08:07:54.168315+00:00 · **Legacy report time:** 2026-11-28T08:08:35.963092+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05051 | 72.47 | +0.14% | 10.10x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004393 | 72.31 | +1.69% | 1.16x | STRONG 81/100 | VERY_HIGH 74/100 | Watch |
| 3 | XMR/USD | 422.61 | 71.93 | -0.72% | 1.34x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 4 | VVV/USD ⭐ | 26.607 | 70.43 | +0.69% | 1.32x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | HYPE/USD | 63.9 | 54.38 | -0.22% | 0.67x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004393 | 72.22 | +1.69% | 1.16x | 2164 | STRONG 81/100 | VERY_HIGH 74/100 | Watch |
| 2 | VVV/USD ⭐ | 26.564 | 72.07 | +0.69% | 1.32x | 7541 | STRONG 86/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05039 | 49.00 | +0.14% | 10.10x | 18925 | STRONG 74/100 | HIGH 61/100 | Watch |

**Same-run overlap:** NIGHT/USD, SPACE/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
