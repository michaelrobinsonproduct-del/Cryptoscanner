# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-16T20:39:58.679140+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43952053372
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** fd3540c5bd1145e15b9b3ecb654be68c4d4f2768 (atomic ledger/results publication)
**Ledger generation:** 448 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UAI/USD | 0.03515 | 64.412 | 49.673 | +3.41% | +0.03% | 2.46x | 11.4 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | AERO/USD | 0.4378 | 63.139 | 46.536 | +3.06% | +0.32% | 3.00x | 16.0 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SENT/USD | 0.017624 | 55.484 | 59.010 | +4.59% | +0.57% | 0.36x | 8.5 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | XDC/USD | 0.02921 | 54.161 | 46.771 | +2.17% | +0.31% | 1.58x | 10.3 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.7224 | 53.345 | 40.554 | +0.81% | +1.50% | 1.53x | 3.5 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.881e-06 | 43.378 | 38.619 | +0.28% | -0.59% | 1.77x | 5.2 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | WEAK 42/100 | HIGH 61/100 | Watch | WATCH |
| 7 | RE/USD | 0.227 | 41.600 | 45.508 | +3.56% | +0.37% | 0.42x | 20.2 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | WEAK 41/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | DCR/USD | 10.674 | 39.149 | 41.348 | +2.12% | +0.03% | 0.77x | 8.4 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | XPL/USD | 0.045 | 24.422 | 30.857 | +1.12% | +0.00% | 0.36x | 22.2 | 2026-11-16T20:39:52.557595+00:00 | Not calibrated | WEAK 22/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 59.010 | 0.017624 | +0.57% | 0.36x |
| 2 | UAI/USD | 49.673 | 0.03515 | +0.03% | 2.46x |
| 3 | XDC/USD | 46.771 | 0.02921 | +0.31% | 1.58x |
| 4 | AERO/USD | 46.536 | 0.4378 | +0.32% | 3.00x |
| 5 | RE/USD | 45.508 | 0.227 | +0.37% | 0.42x |
| 6 | DCR/USD | 41.348 | 10.674 | +0.03% | 0.77x |
| 7 | PEARL/USD | 40.554 | 1.7224 | +1.50% | 1.53x |
| 8 | PEPE/USD | 38.619 | 3.881e-06 | -0.59% | 1.77x |
| 9 | XPL/USD | 30.857 | 0.045 | +0.00% | 0.36x |

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

- Persisted scans: 448; predictions: 3867; observations: 269851.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11895. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43952053372 · **Generation:** 448 · **Legacy run:** 43952053372
**Main quote time:** 2026-11-16T20:39:58.679140+00:00 · **Legacy report time:** 2026-11-16T20:40:11.968973+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UAI/USD | 0.03515 | 64.41 | +0.03% | 2.46x | STRONG 72/100 | VERY_HIGH 73/100 | Watch |
| 2 | AERO/USD ⭐ | 0.4378 | 63.14 | +0.32% | 3.00x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 3 | SENT/USD | 0.017624 | 55.48 | +0.57% | 0.36x | MODERATE 58/100 | VERY_HIGH 82/100 | Watch |
| 4 | XDC/USD ⭐ | 0.02921 | 54.16 | +0.31% | 1.58x | STRONG 77/100 | HIGH 61/100 | Consider small entry |
| 5 | PEARL/USD | 1.7224 | 53.35 | +1.50% | 1.53x | STRONG 72/100 | HIGH 60/100 | Watch |
| 6 | PEPE/USD | 3.881e-06 | 43.38 | -0.59% | 1.77x | WEAK 42/100 | HIGH 61/100 | Watch |
| 7 | RE/USD | 0.227 | 41.60 | +0.37% | 0.42x | WEAK 41/100 | EXTREME 94/100 | Do nothing |
| 8 | DCR/USD | 10.674 | 39.15 | +0.03% | 0.77x | WEAK 40/100 | VERY_HIGH 74/100 | Watch |
| 9 | XPL/USD | 0.045 | 24.42 | +0.00% | 0.36x | WEAK 22/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AERO/USD ⭐ | 0.4374 | 68.02 | +0.18% | 3.00x | 3124 | STRONG 79/100 | VERY_HIGH 72/100 | Watch |
| 2 | XDC/USD ⭐ | 0.02921 | 55.46 | +0.21% | 1.69x | 5402 | STRONG 78/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** AERO/USD, XDC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
