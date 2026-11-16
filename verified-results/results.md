# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-16T10:35:42.097800+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43850170340
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 941edc7b262f55007f601a75a3220f43d0ae8942 (atomic ledger/results publication)
**Ledger generation:** 446 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.017534 | 70.321 | 55.352 | +4.06% | +1.80% | 1.60x | 8.0 | 2026-11-16T10:35:38.922865+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | SKR/USD | 0.010332 | 65.585 | 67.860 | +9.47% | -2.22% | 1.88x | 23.2 | 2026-11-16T10:35:38.922865+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | XDC/USD | 0.02944 | 47.950 | 54.157 | +2.97% | -0.14% | 0.45x | 3.4 | 2026-11-16T10:35:38.922865+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 4 | BEAM/USD | 0.004175 | 38.700 | 35.883 | +1.83% | +1.04% | 0.76x | 16.8 | 2026-11-16T10:35:38.922865+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | ZRO/USD | 1.411 | 19.181 | 33.854 | +0.28% | -1.33% | 0.20x | 14.2 | 2026-11-16T10:35:38.922865+00:00 | Not calibrated | WEAK 10/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKR/USD | 67.860 | 0.010332 | -2.22% | 1.88x |
| 2 | SENT/USD | 55.352 | 0.017534 | +1.80% | 1.60x |
| 3 | XDC/USD | 54.157 | 0.02944 | -0.14% | 0.45x |
| 4 | BEAM/USD | 35.883 | 0.004175 | +1.04% | 0.76x |
| 5 | ZRO/USD | 33.854 | 1.411 | -1.33% | 0.20x |

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

- Persisted scans: 446; predictions: 3852; observations: 268637.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11690. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 43850170340 · **Generation:** 446 · **Legacy run:** 43850170340
**Main quote time:** 2026-11-16T10:35:42.097800+00:00 · **Legacy report time:** 2026-11-16T10:35:53.174613+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.017534 | 70.32 | +1.80% | 1.60x | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 2 | SKR/USD | 0.010332 | 65.59 | -2.22% | 1.88x | WEAK 43/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | XDC/USD | 0.02944 | 47.95 | -0.14% | 0.45x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |
| 4 | BEAM/USD | 0.004175 | 38.70 | +1.04% | 0.76x | WEAK 44/100 | VERY_HIGH 80/100 | Watch |
| 5 | ZRO/USD | 1.411 | 19.18 | -1.33% | 0.20x | WEAK 10/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.017511 | 77.42 | +1.80% | 1.60x | 4058 | STRONG 89/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
