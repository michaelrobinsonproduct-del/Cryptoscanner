# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:39:39.440656+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44972372788
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 8f7f28d6e4ca6a16880d0d806d15d0479b557803 (atomic ledger/results publication)
**Ledger generation:** 1215 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9101 | 58.791 | 58.709 | +0.82% | +0.09% | 0.96x | 4.1 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.9911 | 55.492 | 47.231 | +2.20% | +2.17% | 0.74x | 22.2 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | DRV/USD | 0.3439 | 49.877 | 56.008 | +2.60% | -1.62% | 1.20x | 20.4 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 4 | ENA/USD | 0.0986 | 40.767 | 38.602 | +0.31% | -0.20% | 1.32x | 10.2 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | WEAK 35/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ZRO/USD | 1.195 | 40.745 | 44.958 | +1.88% | +0.17% | 0.49x | 16.8 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | RENDER/USD | 1.315 | 32.201 | 36.389 | +0.84% | +0.15% | 0.50x | 15.2 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | CAP/USD | 0.092485 | 31.490 | 37.416 | +0.58% | +0.21% | 0.30x | 3.6 | 2026-11-22T01:39:30.828930+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 58.709 | 2.9101 | +0.09% | 0.96x |
| 2 | DRV/USD | 56.008 | 0.3439 | -1.62% | 1.20x |
| 3 | PEARL/USD | 47.231 | 1.9911 | +2.17% | 0.74x |
| 4 | ZRO/USD | 44.958 | 1.195 | +0.17% | 0.49x |
| 5 | ENA/USD | 38.602 | 0.0986 | -0.20% | 1.32x |
| 6 | CAP/USD | 37.416 | 0.092485 | +0.21% | 0.30x |
| 7 | RENDER/USD | 36.389 | 1.315 | +0.15% | 0.50x |

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

- Persisted scans: 1215; predictions: 9823; observations: 735078.
- Matured sampled outcomes across 1/6/24/48h: 13480; gap abstentions: 21810. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 22 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44972372788 · **Generation:** 1215 · **Legacy run:** 44972372788
**Main quote time:** 2026-11-22T01:39:39.440656+00:00 · **Legacy report time:** 2026-11-22T01:40:42.175596+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 2.9101 | 58.79 | +0.09% | 0.96x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 2 | PEARL/USD | 1.9911 | 55.49 | +2.17% | 0.74x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 3 | DRV/USD | 0.3439 | 49.88 | -1.62% | 1.20x | WEAK 25/100 | VERY_HIGH 84/100 | Do nothing |
| 4 | ENA/USD | 0.0986 | 40.77 | -0.20% | 1.32x | WEAK 35/100 | HIGH 67/100 | Watch |
| 5 | ZRO/USD | 1.195 | 40.74 | +0.17% | 0.49x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 6 | RENDER/USD | 1.315 | 32.20 | +0.15% | 0.50x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | CAP/USD | 0.092485 | 31.49 | +0.21% | 0.30x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
