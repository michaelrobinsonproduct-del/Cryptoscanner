# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T21:35:13.071997+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44402889681
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 3f50327a804cd05b0aa057849472c22efe7246cc (atomic ledger/results publication)
**Ledger generation:** 673 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020154 | 71.443 | 73.200 | +7.95% | +0.45% | 0.60x | 6.0 | 2026-11-18T21:35:08.866520+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | VVV/USD | 21.348 | 52.983 | 55.197 | +1.53% | +0.18% | 0.69x | 7.5 | 2026-11-18T21:35:08.866520+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | TRX/USD | 0.308692 | 42.083 | 41.739 | +0.26% | +0.11% | 0.98x | 0.1 | 2026-11-18T21:35:08.866520+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 4 | WINGS/USD | 0.001922 | 36.696 | 47.389 | +4.86% | -0.83% | 0.34x | 36.5 | 2026-11-18T21:35:08.866520+00:00 | Not calibrated | WEAK 8/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | AKT/USD | 0.5126 | 32.612 | 30.436 | +0.65% | +0.12% | 1.16x | 11.7 | 2026-11-18T21:35:08.866520+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.200 | 0.020154 | +0.45% | 0.60x |
| 2 | VVV/USD | 55.197 | 21.348 | +0.18% | 0.69x |
| 3 | WINGS/USD | 47.389 | 0.001922 | -0.83% | 0.34x |
| 4 | TRX/USD | 41.739 | 0.308692 | +0.11% | 0.98x |
| 5 | AKT/USD | 30.436 | 0.5126 | +0.12% | 1.16x |

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

- Persisted scans: 673; predictions: 5543; observations: 406864.
- Matured sampled outcomes across 1/6/24/48h: 5197; gap abstentions: 13146. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44402889681 · **Generation:** 673 · **Legacy run:** 44402889681
**Main quote time:** 2026-11-18T21:35:13.071997+00:00 · **Legacy report time:** 2026-11-18T21:35:48.375075+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020154 | 71.44 | +0.45% | 0.60x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 2 | VVV/USD | 21.348 | 52.98 | +0.18% | 0.69x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 3 | TRX/USD | 0.308692 | 42.08 | +0.11% | 0.98x | WEAK 41/100 | HIGH 62/100 | Watch |
| 4 | WINGS/USD | 0.001922 | 36.70 | -0.83% | 0.34x | WEAK 8/100 | EXTREME 100/100 | Do nothing |
| 5 | AKT/USD ⭐ | 0.5126 | 32.61 | +0.12% | 1.16x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5126 | 42.91 | +0.12% | 1.16x | 4287 | MODERATE 56/100 | HIGH 67/100 | Watch |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
