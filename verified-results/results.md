# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:25:29.300112+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44645623893
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b4daaefd63040f67d15a4ff7a71608eee7e7ac46 (atomic ledger/results publication)
**Ledger generation:** 886 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 502.11 | 76.387 | 56.732 | +0.93% | +0.93% | 3.68x | 9.6 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.96303 | 71.153 | 57.706 | +0.39% | +0.21% | 2.24x | 0.1 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 895.46 | 69.228 | 55.454 | +0.26% | -0.25% | 2.51x | 2.7 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XBT/USD | 62077.3 | 57.139 | 56.844 | +0.26% | +0.22% | 0.92x | 0.0 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.03 | 56.407 | 56.759 | +0.46% | -0.03% | 0.98x | 3.0 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5393 | 53.255 | 34.895 | +1.09% | +0.67% | 5.64x | 11.1 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 7 | XLM/USD | 0.133299 | 51.613 | 57.184 | +0.45% | +0.30% | 0.29x | 2.0 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.152177 | 50.202 | 54.392 | +0.27% | +0.01% | 0.58x | 5.1 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ICNT/USD | 0.4294 | 42.363 | 35.948 | +0.77% | -0.14% | 1.71x | 14.0 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | WEAK 36/100 | HIGH 67/100 | Watch | WATCH |
| 10 | CAP/USD | 0.097656 | 42.103 | 36.584 | +1.08% | +0.25% | 1.43x | 11.2 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 11 | FET/USD | 0.1256 | 39.704 | 29.063 | +0.32% | +0.24% | 1.94x | 16.0 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 12 | STRK/USD | 0.03203 | 37.706 | 39.995 | +1.07% | +0.57% | 0.49x | 6.2 | 2026-11-20T00:25:20.585054+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 57.706 | 0.96303 | +0.21% | 2.24x |
| 2 | XLM/USD | 57.184 | 0.133299 | +0.30% | 0.29x |
| 3 | XBT/USD | 56.844 | 62077.3 | +0.22% | 0.92x |
| 4 | HYPE/USD | 56.759 | 67.03 | -0.03% | 0.98x |
| 5 | XMR/USD | 56.732 | 502.11 | +0.93% | 3.68x |
| 6 | ZEC/USD | 55.454 | 895.46 | -0.25% | 2.51x |
| 7 | ADA/USD | 54.392 | 0.152177 | +0.01% | 0.58x |
| 8 | STRK/USD | 39.995 | 0.03203 | +0.57% | 0.49x |
| 9 | CAP/USD | 36.584 | 0.097656 | +0.25% | 1.43x |
| 10 | ICNT/USD | 35.948 | 0.4294 | -0.14% | 1.71x |
| 11 | AKT/USD | 34.895 | 0.5393 | +0.67% | 5.64x |
| 12 | FET/USD | 29.063 | 0.1256 | +0.24% | 1.94x |

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

- Persisted scans: 886; predictions: 7735; observations: 535383.
- Matured sampled outcomes across 1/6/24/48h: 8400; gap abstentions: 16037. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44645623893 · **Generation:** 886 · **Legacy run:** 44645623893
**Main quote time:** 2026-11-20T00:25:29.300112+00:00 · **Legacy report time:** 2026-11-20T00:26:22.811099+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 502.11 | 76.39 | +0.93% | 3.68x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.96303 | 71.15 | +0.21% | 2.24x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD | 895.46 | 69.23 | -0.25% | 2.51x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | XBT/USD | 62077.3 | 57.14 | +0.22% | 0.92x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 5 | HYPE/USD | 67.03 | 56.41 | -0.03% | 0.98x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 6 | AKT/USD | 0.5393 | 53.25 | +0.67% | 5.64x | STRONG 77/100 | HIGH 66/100 | Watch |
| 7 | XLM/USD | 0.133299 | 51.61 | +0.30% | 0.29x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.152177 | 50.20 | +0.01% | 0.58x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 9 | ICNT/USD | 0.4294 | 42.36 | -0.14% | 1.71x | WEAK 36/100 | HIGH 67/100 | Watch |
| 10 | CAP/USD | 0.097656 | 42.10 | +0.25% | 1.43x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 11 | FET/USD | 0.1256 | 39.70 | +0.24% | 1.94x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 12 | STRK/USD | 0.03203 | 37.71 | +0.57% | 0.49x | MODERATE 49/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96244 | 60.74 | +0.21% | 2.24x | 33840 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 502.36 | 60.62 | +0.93% | 3.68x | 7846 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | BLESS/USD | 0.0125 | 47.40 | +1.03% | 1.10x | 1439 | MODERATE 49/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** XMR/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
