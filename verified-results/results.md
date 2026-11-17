# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T20:01:39.246020+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44164795667
**Source SHA:** 19d4b4203812bcae29aa50a9444ca1bb8d9760d3
**Previous ledger commit:** 7ce932f3d5fcc728e759ab7c15fca7a28718d4a2 (atomic ledger/results publication)
**Ledger generation:** 455 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.104 | 86.264 | 72.273 | +2.97% | +0.32% | 2.24x | 7.1 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 507.03 | 78.906 | 73.187 | +2.73% | +0.03% | 1.56x | 1.8 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 2.1038 | 76.615 | 70.244 | +7.80% | +0.15% | 1.56x | 11.9 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96287 | 70.732 | 60.894 | +0.85% | +0.09% | 1.94x | 0.1 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.1887 | 69.335 | 59.337 | +0.98% | +0.42% | 1.79x | 5.0 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 6 | AAVE/USD | 110.24 | 66.324 | 50.993 | +1.62% | +0.21% | 2.43x | 4.5 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 7 | UNI/USD | 5.2208 | 64.699 | 50.128 | +1.16% | -0.09% | 2.95x | 3.8 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZEC/USD | 916.37 | 58.670 | 61.947 | +1.39% | -0.19% | 0.77x | 5.6 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | SOL/USD | 72.63 | 57.930 | 65.176 | +1.55% | +0.03% | 0.26x | 1.4 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | VVV/USD | 20.535 | 51.786 | 56.105 | +1.92% | +0.20% | 0.47x | 6.8 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDC/USD | 0.03039 | 51.053 | 58.792 | +4.08% | -0.56% | 0.50x | 13.2 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 12 | TRX/USD | 0.307031 | 45.933 | 42.968 | +0.71% | -0.20% | 1.40x | 1.5 | 2026-11-17T20:01:30.513810+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 73.187 | 507.03 | +0.03% | 1.56x |
| 2 | INJ/USD | 72.273 | 7.104 | +0.32% | 2.24x |
| 3 | PIEVERSE/USD | 70.244 | 2.1038 | +0.15% | 1.56x |
| 4 | SOL/USD | 65.176 | 72.63 | +0.03% | 0.26x |
| 5 | ZEC/USD | 61.947 | 916.37 | -0.19% | 0.77x |
| 6 | XRP/USD | 60.894 | 0.96287 | +0.09% | 1.94x |
| 7 | NEAR/USD | 59.337 | 3.1887 | +0.42% | 1.79x |
| 8 | XDC/USD | 58.792 | 0.03039 | -0.56% | 0.50x |
| 9 | VVV/USD | 56.105 | 20.535 | +0.20% | 0.47x |
| 10 | AAVE/USD | 50.993 | 110.24 | +0.21% | 2.43x |
| 11 | UNI/USD | 50.128 | 5.2208 | -0.09% | 2.95x |
| 12 | TRX/USD | 42.968 | 0.307031 | -0.20% | 1.40x |

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

- Persisted scans: 455; predictions: 3941; observations: 274102.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12221. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44164795667 · **Generation:** 455 · **Legacy run:** 44164795667
**Main quote time:** 2026-11-17T20:01:39.246020+00:00 · **Legacy report time:** 2026-11-17T20:01:49.006339+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.104 | 86.26 | +0.32% | 2.24x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 507.03 | 78.91 | +0.03% | 1.56x | STRONG 74/100 | HIGH 55/100 | Watch |
| 3 | PIEVERSE/USD ⭐ | 2.1038 | 76.61 | +0.15% | 1.56x | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 4 | XRP/USD ⭐ | 0.96287 | 70.73 | +0.09% | 1.94x | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD | 3.1887 | 69.33 | +0.42% | 1.79x | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | AAVE/USD | 110.24 | 66.32 | +0.21% | 2.43x | STRONG 88/100 | HIGH 55/100 | Watch |
| 7 | UNI/USD | 5.2208 | 64.70 | -0.09% | 2.95x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | ZEC/USD | 916.37 | 58.67 | -0.19% | 0.77x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 9 | SOL/USD | 72.63 | 57.93 | +0.03% | 0.26x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | VVV/USD | 20.535 | 51.79 | +0.20% | 0.47x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDC/USD | 0.03039 | 51.05 | -0.56% | 0.50x | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing |
| 12 | TRX/USD | 0.307031 | 45.93 | -0.20% | 1.40x | WEAK 43/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.104 | 85.12 | +0.32% | 2.24x | 9909 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.96317 | 66.38 | +0.09% | 1.94x | 29293 | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | PIEVERSE/USD ⭐ | 2.1038 | 62.76 | +0.15% | 1.56x | 1360 | MODERATE 61/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** INJ/USD, PIEVERSE/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
