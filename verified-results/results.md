# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:21:34.126078+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45339607938
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6d8a0f60a44973fcabd56c7c682ce07d5f9f6a9e (atomic ledger/results publication)
**Ledger generation:** 1537 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.554e-06 | 90.055 | 76.178 | +3.86% | -0.22% | 2.88x | 2.8 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 25.49 | 87.985 | 79.529 | +4.26% | +0.61% | 1.54x | 10.6 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | BAT/USD | 0.08056 | 78.576 | 60.455 | +4.39% | +0.62% | 3.67x | 5.0 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | STRONG 94/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | ICNT/USD | 0.3366 | 74.819 | 67.007 | +8.90% | +2.94% | 0.31x | 20.9 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | NIGHT/USD | 0.04929 | 66.632 | 63.317 | +2.37% | +1.02% | 0.82x | 6.1 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LTC/USD | 41.86 | 63.948 | 61.241 | +1.06% | +0.07% | 1.23x | 2.4 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XLM/USD | 0.13044 | 61.566 | 56.328 | +0.34% | -0.23% | 1.64x | 2.1 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.0314 | 60.545 | 64.644 | +1.68% | -0.21% | 0.70x | 4.3 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95209 | 60.121 | 64.411 | +1.35% | -0.16% | 0.65x | 0.1 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XMR/USD | 495.27 | 55.127 | 60.845 | +1.90% | -0.04% | 0.45x | 15.0 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | LINK/USD | 9.11762 | 52.775 | 60.736 | +1.25% | -0.03% | 0.22x | 6.0 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0565696 | 52.606 | 57.908 | +0.47% | +0.04% | 0.45x | 0.8 | 2026-11-24T06:21:27.649048+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.529 | 25.49 | +0.61% | 1.54x |
| 2 | PEPE/USD | 76.178 | 3.554e-06 | -0.22% | 2.88x |
| 3 | ICNT/USD | 67.007 | 0.3366 | +2.94% | 0.31x |
| 4 | NEAR/USD | 64.644 | 3.0314 | -0.21% | 0.70x |
| 5 | XRP/USD | 64.411 | 0.95209 | -0.16% | 0.65x |
| 6 | NIGHT/USD | 63.317 | 0.04929 | +1.02% | 0.82x |
| 7 | LTC/USD | 61.241 | 41.86 | +0.07% | 1.23x |
| 8 | XMR/USD | 60.845 | 495.27 | -0.04% | 0.45x |
| 9 | LINK/USD | 60.736 | 9.11762 | -0.03% | 0.22x |
| 10 | BAT/USD | 60.455 | 0.08056 | +0.62% | 3.67x |
| 11 | XDG/USD | 57.908 | 0.0565696 | +0.04% | 0.45x |
| 12 | XLM/USD | 56.328 | 0.13044 | -0.23% | 1.64x |

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

- Persisted scans: 1537; predictions: 13177; observations: 931131.
- Matured sampled outcomes across 1/6/24/48h: 24716; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 137 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45339607938 · **Generation:** 1537 · **Legacy run:** 45339607938
**Main quote time:** 2026-11-24T06:21:34.126078+00:00 · **Legacy report time:** 2026-11-24T06:22:43.091700+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.554e-06 | 90.06 | -0.22% | 2.88x | STRONG 75/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 25.49 | 87.98 | +0.61% | 1.54x | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 3 | BAT/USD ⭐ | 0.08056 | 78.58 | +0.62% | 3.67x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | ICNT/USD | 0.3366 | 74.82 | +2.94% | 0.31x | MODERATE 57/100 | EXTREME 87/100 | Do nothing |
| 5 | NIGHT/USD | 0.04929 | 66.63 | +1.02% | 0.82x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | LTC/USD ⭐ | 41.86 | 63.95 | +0.07% | 1.23x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | XLM/USD | 0.13044 | 61.57 | -0.23% | 1.64x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | NEAR/USD | 3.0314 | 60.54 | -0.21% | 0.70x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | XRP/USD | 0.95209 | 60.12 | -0.16% | 0.65x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XMR/USD | 495.27 | 55.13 | -0.04% | 0.45x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | LINK/USD | 9.11762 | 52.77 | -0.03% | 0.22x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0565696 | 52.61 | +0.04% | 0.45x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.426 | 91.39 | +0.61% | 1.54x | 12420 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BAT/USD ⭐ | 0.08025 | 81.08 | +0.62% | 3.67x | 3294 | STRONG 91/100 | VERY_HIGH 72/100 | Watch |
| 3 | LTC/USD ⭐ | 41.76 | 58.22 | +0.07% | 1.23x | 13030 | MODERATE 64/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, BAT/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
