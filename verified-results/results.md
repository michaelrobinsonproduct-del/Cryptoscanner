# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T17:47:36.247351+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45667931889
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5cf1662f31d25f92e7e6ac1bbe7529e16f33671e (atomic ledger/results publication)
**Ledger generation:** 1746 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.3431 | 92.043 | 71.389 | +9.17% | +1.65% | 2.24x | 24.8 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | STRONG 91/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 41.84 | 83.907 | 70.768 | +2.42% | +1.23% | 1.70x | 2.4 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 26.161 | 83.808 | 86.009 | +6.61% | +0.51% | 0.53x | 28.0 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | XPL/USD | 0.0474 | 63.177 | 60.318 | +7.73% | +1.28% | 0.65x | 42.3 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 97/100 | Do nothing | WATCH |
| 5 | INJ/USD | 5.903 | 60.906 | 41.818 | +0.94% | +0.82% | 6.47x | 6.8 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 514.4 | 52.780 | 54.584 | +0.94% | +1.36% | 0.14x | 14.0 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XLM/USD | 0.125288 | 52.632 | 48.059 | +0.99% | +1.18% | 0.87x | 4.8 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 8 | HBAR/USD | 0.05078 | 51.824 | 41.252 | +1.03% | +1.05% | 1.53x | 3.9 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | STRONG 71/100 | HIGH 60/100 | Watch | WATCH |
| 9 | CAP/USD | 0.093578 | 45.689 | 37.208 | +1.26% | +1.22% | 1.24x | 6.1 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 10 | ASTER/USD | 0.49139 | 42.950 | 46.245 | +2.20% | +0.67% | 0.33x | 3.7 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | FIL/USD | 0.535 | 37.594 | 25.647 | +0.38% | +1.13% | 1.63x | 18.7 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 12 | TIA/USD | 0.3238 | 37.312 | 30.548 | +0.40% | +1.56% | 0.89x | 6.2 | 2026-11-25T17:47:27.324121+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 86.009 | 26.161 | +0.51% | 0.53x |
| 2 | DRV/USD | 71.389 | 0.3431 | +1.65% | 2.24x |
| 3 | LTC/USD | 70.768 | 41.84 | +1.23% | 1.70x |
| 4 | XPL/USD | 60.318 | 0.0474 | +1.28% | 0.65x |
| 5 | XMR/USD | 54.584 | 514.4 | +1.36% | 0.14x |
| 6 | XLM/USD | 48.059 | 0.125288 | +1.18% | 0.87x |
| 7 | ASTER/USD | 46.245 | 0.49139 | +0.67% | 0.33x |
| 8 | INJ/USD | 41.818 | 5.903 | +0.82% | 6.47x |
| 9 | HBAR/USD | 41.252 | 0.05078 | +1.05% | 1.53x |
| 10 | CAP/USD | 37.208 | 0.093578 | +1.22% | 1.24x |
| 11 | TIA/USD | 30.548 | 0.3238 | +1.56% | 0.89x |
| 12 | FIL/USD | 25.647 | 0.535 | +1.13% | 1.63x |

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

- Persisted scans: 1746; predictions: 14696; observations: 1058358.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22592. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45667931889 · **Generation:** 1746 · **Legacy run:** 45667931889
**Main quote time:** 2026-11-25T17:47:36.247351+00:00 · **Legacy report time:** 2026-11-25T17:48:28.896769+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.3431 | 92.04 | +1.65% | 2.24x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 41.84 | 83.91 | +1.23% | 1.70x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 26.161 | 83.81 | +0.51% | 0.53x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 4 | XPL/USD | 0.0474 | 63.18 | +1.28% | 0.65x | MODERATE 47/100 | EXTREME 97/100 | Do nothing |
| 5 | INJ/USD | 5.903 | 60.91 | +0.82% | 6.47x | STRONG 85/100 | HIGH 55/100 | Watch |
| 6 | XMR/USD | 514.4 | 52.78 | +1.36% | 0.14x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 7 | XLM/USD | 0.125288 | 52.63 | +1.18% | 0.87x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 8 | HBAR/USD ⭐ | 0.05078 | 51.82 | +1.05% | 1.53x | STRONG 81/100 | HIGH 60/100 | Consider small entry |
| 9 | CAP/USD ⭐ | 0.093578 | 45.69 | +1.22% | 1.24x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 10 | ASTER/USD | 0.49139 | 42.95 | +0.67% | 0.33x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 11 | FIL/USD | 0.535 | 37.59 | +1.13% | 1.63x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 12 | TIA/USD | 0.3238 | 37.31 | +1.56% | 0.89x | MODERATE 49/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34414 | 85.20 | +1.65% | 2.24x | 11080 | STRONG 98/100 | HIGH 67/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 41.83 | 82.49 | +1.23% | 1.70x | 12996 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 3 | KAS/USD | 0.02681 | 63.65 | +0.94% | 2.48x | 2525 | STRONG 77/100 | VERY_HIGH 72/100 | Watch |
| 4 | HBAR/USD ⭐ | 0.05078 | 46.47 | +1.05% | 1.53x | 5537 | STRONG 78/100 | HIGH 60/100 | Consider small entry |
| 5 | CAP/USD ⭐ | 0.093577 | 45.36 | +1.22% | 1.24x | 3417 | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** DRV/USD, LTC/USD, HBAR/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
