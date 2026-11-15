# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T23:31:30.567288+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43775235687
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 8c740af90fd75ce62933e895c09502ce64bf41a7 (atomic ledger/results publication)
**Ledger generation:** 444 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.97045 | 113.236 | 97.639 | +6.20% | +0.12% | 3.30x | 1.5 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | HYPE/USD | 67.71 | 103.254 | 90.530 | +5.29% | -0.46% | 9.53x | 3.0 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 495.39 | 102.957 | 90.421 | +5.36% | -0.04% | 2.27x | 1.6 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SUI/USD | 0.7337 | 102.185 | 87.390 | +4.72% | -0.04% | 3.55x | 1.4 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XDG/USD | 0.059619 | 100.951 | 82.734 | +4.02% | +0.64% | 7.59x | 0.8 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ZEC/USD | 906.25 | 99.046 | 89.286 | +4.91% | -0.16% | 2.05x | 0.1 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XLM/USD | 0.140814 | 98.081 | 82.290 | +3.93% | +0.16% | 5.90x | 0.5 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.1951 | 97.523 | 92.314 | +5.49% | -0.13% | 1.59x | 2.2 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 9 | UNI/USD | 5.1519 | 96.310 | 82.987 | +5.53% | +0.21% | 2.23x | 5.2 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | AAVE/USD | 108.71 | 95.636 | 85.321 | +8.12% | -0.03% | 2.05x | 5.5 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ETH/USD | 1828.16 | 94.618 | 78.722 | +3.39% | +0.18% | 4.01x | 0.1 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 12 | ADA/USD | 0.154724 | 92.339 | 86.405 | +4.79% | +0.23% | 1.48x | 4.2 | 2026-11-15T23:31:22.121479+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 97.639 | 0.97045 | +0.12% | 3.30x |
| 2 | NEAR/USD | 92.314 | 3.1951 | -0.13% | 1.59x |
| 3 | HYPE/USD | 90.530 | 67.71 | -0.46% | 9.53x |
| 4 | XMR/USD | 90.421 | 495.39 | -0.04% | 2.27x |
| 5 | ZEC/USD | 89.286 | 906.25 | -0.16% | 2.05x |
| 6 | SUI/USD | 87.390 | 0.7337 | -0.04% | 3.55x |
| 7 | ADA/USD | 86.405 | 0.154724 | +0.23% | 1.48x |
| 8 | AAVE/USD | 85.321 | 108.71 | -0.03% | 2.05x |
| 9 | UNI/USD | 82.987 | 5.1519 | +0.21% | 2.23x |
| 10 | XDG/USD | 82.734 | 0.059619 | +0.64% | 7.59x |
| 11 | XLM/USD | 82.290 | 0.140814 | +0.16% | 5.90x |
| 12 | ETH/USD | 78.722 | 1828.16 | +0.18% | 4.01x |

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

- Persisted scans: 444; predictions: 3844; observations: 267423.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11342. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43775235687 · **Generation:** 444 · **Legacy run:** 43775235687
**Main quote time:** 2026-11-15T23:31:30.567288+00:00 · **Legacy report time:** 2026-11-15T23:31:45.782082+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.97045 | 113.24 | +0.12% | 3.30x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD | 67.71 | 103.25 | -0.46% | 9.53x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 495.39 | 102.96 | -0.04% | 2.27x | STRONG 80/100 | HIGH 61/100 | Watch |
| 4 | SUI/USD | 0.7337 | 102.19 | -0.04% | 3.55x | STRONG 80/100 | HIGH 61/100 | Watch |
| 5 | XDG/USD ⭐ | 0.059619 | 100.95 | +0.64% | 7.59x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | ZEC/USD | 906.25 | 99.05 | -0.16% | 2.05x | STRONG 80/100 | HIGH 61/100 | Watch |
| 7 | XLM/USD ⭐ | 0.140814 | 98.08 | +0.16% | 5.90x | STRONG 100/100 | HIGH 55/100 | Watch |
| 8 | NEAR/USD | 3.1951 | 97.52 | -0.13% | 1.59x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 9 | UNI/USD ⭐ | 5.1519 | 96.31 | +0.21% | 2.23x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | AAVE/USD | 108.71 | 95.64 | -0.03% | 2.05x | STRONG 78/100 | HIGH 61/100 | Watch |
| 11 | ETH/USD ⭐ | 1828.16 | 94.62 | +0.18% | 4.01x | STRONG 100/100 | HIGH 55/100 | Watch |
| 12 | ADA/USD ⭐ | 0.154724 | 92.34 | +0.23% | 1.48x | STRONG 100/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1827.28 | 100.00 | +0.18% | 4.01x | 70308 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.059619 | 100.00 | +0.64% | 7.59x | 14446 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XLM/USD ⭐ | 0.140741 | 100.00 | +0.16% | 5.90x | 13233 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD ⭐ | 0.96989 | 100.00 | +0.12% | 3.30x | 42026 | STRONG 100/100 | HIGH 55/100 | Watch |
| 5 | LINK/USD | 9.25212 | 94.95 | +0.20% | 5.42x | 8716 | STRONG 92/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD ⭐ | 0.154724 | 94.45 | +0.23% | 1.48x | 17117 | STRONG 100/100 | HIGH 55/100 | Watch |
| 7 | UNI/USD ⭐ | 5.1519 | 92.53 | +0.21% | 2.23x | 9675 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | HBAR/USD | 0.059 | 88.14 | +0.19% | 1.99x | 7950 | STRONG 79/100 | HIGH 55/100 | Watch |
| 9 | TAO/USD | 194.0821 | 87.41 | +0.29% | 1.08x | 8755 | STRONG 79/100 | HIGH 62/100 | Watch |
| 10 | DOT/USD | 0.7352 | 87.34 | +0.33% | 1.34x | 11131 | STRONG 89/100 | HIGH 60/100 | Watch |

**Same-run overlap:** XRP/USD, XDG/USD, XLM/USD, UNI/USD, ETH/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
