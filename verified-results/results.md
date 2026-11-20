# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:55:19.551856+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44649575875
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b9c3b653c9f059bd6522eb886d7229ad0da03045 (atomic ledger/results publication)
**Ledger generation:** 891 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | RARE/USD | 0.01391 | 69.397 | 51.209 | +4.90% | +4.12% | 0.76x | 28.7 | 2026-11-20T00:55:15.768078+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 96/100 | Do nothing | WATCH |
| 2 | XLM/USD | 0.133184 | 63.910 | 55.901 | +0.36% | +0.04% | 1.78x | 3.3 | 2026-11-20T00:55:15.768078+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 499.26 | 55.873 | 56.503 | +0.36% | -0.34% | 1.11x | 2.0 | 2026-11-20T00:55:15.768078+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.09773 | 36.196 | 36.474 | +1.56% | +0.87% | 0.54x | 12.3 | 2026-11-20T00:55:15.768078+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05877 | 31.399 | 26.490 | +0.88% | -1.12% | 2.05x | 23.8 | 2026-11-20T00:55:15.768078+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 56.503 | 499.26 | -0.34% | 1.11x |
| 2 | XLM/USD | 55.901 | 0.133184 | +0.04% | 1.78x |
| 3 | RARE/USD | 51.209 | 0.01391 | +4.12% | 0.76x |
| 4 | SYRUP/USD | 36.474 | 0.09773 | +0.87% | 0.54x |
| 5 | MEGA/USD | 26.490 | 0.05877 | -1.12% | 2.05x |

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

- Persisted scans: 891; predictions: 7769; observations: 538398.
- Matured sampled outcomes across 1/6/24/48h: 8489; gap abstentions: 16115. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44649575875 · **Generation:** 891 · **Legacy run:** 44649575875
**Main quote time:** 2026-11-20T00:55:19.551856+00:00 · **Legacy report time:** 2026-11-20T00:56:02.274212+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD | 0.01391 | 69.40 | +4.12% | 0.76x | MODERATE 55/100 | EXTREME 96/100 | Do nothing |
| 2 | XLM/USD | 0.133184 | 63.91 | +0.04% | 1.78x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD | 499.26 | 55.87 | -0.34% | 1.11x | WEAK 38/100 | HIGH 68/100 | Watch |
| 4 | SYRUP/USD | 0.09773 | 36.20 | +0.87% | 0.54x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |
| 5 | MEGA/USD | 0.05877 | 31.40 | -1.12% | 2.05x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |

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
