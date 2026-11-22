# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:00:50.056917+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44969289274
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 177460d68e648bf9e885640d548a206489e59a14 (atomic ledger/results publication)
**Ledger generation:** 1211 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.419e-06 | 61.033 | 44.713 | +0.47% | +0.26% | 15.49x | 8.8 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33715 | 51.788 | 36.161 | +0.58% | +3.33% | 0.90x | 30.6 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 84/100 | Watch | WATCH |
| 3 | RENDER/USD | 1.308 | 41.097 | 36.384 | +0.31% | +0.38% | 1.28x | 7.7 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | MODERATE 56/100 | HIGH 55/100 | Watch | WATCH |
| 4 | CAP/USD | 0.092494 | 36.635 | 33.707 | +0.59% | -0.01% | 1.30x | 12.4 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 5 | BLESS/USD | 0.012445 | 19.967 | 24.963 | +0.89% | -0.13% | 0.56x | 42.0 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | WEAK 0/100 | EXTREME 98/100 | Do nothing | WATCH |
| 6 | TRAC/USD | 0.2793 | 18.978 | 25.206 | +0.98% | -0.39% | 0.57x | 25.0 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | WEAK 4/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | ZAMA/USD | 0.06062 | 18.947 | 28.465 | +0.30% | -0.10% | 0.10x | 9.9 | 2026-11-22T01:00:42.034908+00:00 | Not calibrated | WEAK 14/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEPE/USD | 44.713 | 3.419e-06 | +0.26% | 15.49x |
| 2 | RENDER/USD | 36.384 | 1.308 | +0.38% | 1.28x |
| 3 | DRV/USD | 36.161 | 0.33715 | +3.33% | 0.90x |
| 4 | CAP/USD | 33.707 | 0.092494 | -0.01% | 1.30x |
| 5 | ZAMA/USD | 28.465 | 0.06062 | -0.10% | 0.10x |
| 6 | TRAC/USD | 25.206 | 0.2793 | -0.39% | 0.57x |
| 7 | BLESS/USD | 24.963 | 0.012445 | -0.13% | 0.56x |

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

- Persisted scans: 1211; predictions: 9796; observations: 732646.
- Matured sampled outcomes across 1/6/24/48h: 13322; gap abstentions: 21769. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44969289274 · **Generation:** 1211 · **Legacy run:** 44969289274
**Main quote time:** 2026-11-22T01:00:50.056917+00:00 · **Legacy report time:** 2026-11-22T01:01:33.051075+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.419e-06 | 61.03 | +0.26% | 15.49x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD | 0.33715 | 51.79 | +3.33% | 0.90x | MODERATE 46/100 | VERY_HIGH 84/100 | Watch |
| 3 | RENDER/USD | 1.308 | 41.10 | +0.38% | 1.28x | MODERATE 56/100 | HIGH 55/100 | Watch |
| 4 | CAP/USD | 0.092494 | 36.64 | -0.01% | 1.30x | WEAK 23/100 | VERY_HIGH 72/100 | Do nothing |
| 5 | BLESS/USD | 0.012445 | 19.97 | -0.13% | 0.56x | WEAK 0/100 | EXTREME 98/100 | Do nothing |
| 6 | TRAC/USD | 0.2793 | 18.98 | -0.39% | 0.57x | WEAK 4/100 | EXTREME 100/100 | Do nothing |
| 7 | ZAMA/USD | 0.06062 | 18.95 | -0.10% | 0.10x | WEAK 14/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.12902 | 53.76 | +0.12% | 1.45x | 14033 | MODERATE 62/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 2.892 | 50.24 | +0.41% | 1.04x | 20702 | MODERATE 60/100 | HIGH 62/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.419e-06 | 45.92 | +0.26% | 15.49x | 5639 | STRONG 88/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
