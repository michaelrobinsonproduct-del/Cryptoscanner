# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T16:22:41.279489+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46164540584
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 32f652a862206c65bab7fa89f1f491dead042e1e (atomic ledger/results publication)
**Ledger generation:** 2177 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 422.36 | 75.968 | 74.652 | +3.71% | -0.99% | 1.63x | 12.6 | 2026-11-28T16:22:37.339179+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.749e-05 | 63.207 | 59.215 | +4.17% | +0.30% | 1.25x | 2.1 | 2026-11-28T16:22:37.339179+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05146 | 58.319 | 66.887 | +2.43% | -1.12% | 0.70x | 7.8 | 2026-11-28T16:22:37.339179+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.023866 | 42.868 | 32.775 | +0.64% | -0.98% | 2.52x | 6.3 | 2026-11-28T16:22:37.339179+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.652 | 422.36 | -0.99% | 1.63x |
| 2 | NIGHT/USD | 66.887 | 0.05146 | -1.12% | 0.70x |
| 3 | LUNA/USD | 59.215 | 4.749e-05 | +0.30% | 1.25x |
| 4 | SENT/USD | 32.775 | 0.023866 | -0.98% | 2.52x |

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

- Persisted scans: 2177; predictions: 19311; observations: 1318308.
- Matured sampled outcomes across 1/6/24/48h: 46672; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46164540584 · **Generation:** 2177 · **Legacy run:** 46164540584
**Main quote time:** 2026-11-28T16:22:41.279489+00:00 · **Legacy report time:** 2026-11-28T16:23:19.208195+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 422.36 | 75.97 | -0.99% | 1.63x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.749e-05 | 63.21 | +0.30% | 1.25x | STRONG 77/100 | HIGH 67/100 | Watch |
| 3 | NIGHT/USD | 0.05146 | 58.32 | -1.12% | 0.70x | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing |
| 4 | SENT/USD | 0.023866 | 42.87 | -0.98% | 2.52x | MODERATE 51/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.749e-05 | 60.82 | +0.30% | 1.25x | 1233 | STRONG 75/100 | HIGH 67/100 | Watch |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
