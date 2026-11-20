# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:15:45.862925+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44644256161
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b99f8e6c4a4dbc15e52060ffbb5e7bfb596fe0dc (atomic ledger/results publication)
**Ledger generation:** 885 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 895.44 | 71.105 | 55.328 | +0.25% | +0.16% | 6.38x | 2.9 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96223 | 58.427 | 57.123 | +0.31% | +0.25% | 1.00x | 0.1 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5422 | 55.390 | 34.122 | +1.63% | +1.25% | 5.67x | 20.3 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152177 | 52.590 | 55.116 | +0.27% | +0.28% | 0.61x | 3.6 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XMR/USD | 499.32 | 42.471 | 47.771 | +0.37% | +0.32% | 0.31x | 19.6 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.05336 | 41.709 | 31.204 | +0.38% | +0.43% | 1.83x | 9.4 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |
| 7 | PAXG/USD | 3610.86 | 38.587 | 45.098 | +0.41% | +0.38% | 0.16x | 0.9 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CAP/USD | 0.097238 | 38.251 | 30.624 | +0.64% | +0.77% | 1.38x | 17.0 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 9 | STRK/USD | 0.03192 | 37.703 | 35.958 | +0.73% | +0.50% | 0.92x | 9.4 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 10 | XAUT/USD | 3613 | 36.936 | 36.455 | +0.35% | +0.37% | 0.86x | 0.3 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 11 | ICNT/USD | 0.431 | 34.009 | 35.101 | +1.15% | +1.01% | 0.39x | 20.9 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | USELESS/USD | 0.09962 | 32.849 | 30.142 | +0.37% | +0.25% | 1.14x | 27.2 | 2026-11-20T00:15:37.066201+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 57.123 | 0.96223 | +0.25% | 1.00x |
| 2 | ZEC/USD | 55.328 | 895.44 | +0.16% | 6.38x |
| 3 | ADA/USD | 55.116 | 0.152177 | +0.28% | 0.61x |
| 4 | XMR/USD | 47.771 | 499.32 | +0.32% | 0.31x |
| 5 | PAXG/USD | 45.098 | 3610.86 | +0.38% | 0.16x |
| 6 | XAUT/USD | 36.455 | 3613 | +0.37% | 0.86x |
| 7 | STRK/USD | 35.958 | 0.03192 | +0.50% | 0.92x |
| 8 | ICNT/USD | 35.101 | 0.431 | +1.01% | 0.39x |
| 9 | AKT/USD | 34.122 | 0.5422 | +1.25% | 5.67x |
| 10 | PYTH/USD | 31.204 | 0.05336 | +0.43% | 1.83x |
| 11 | CAP/USD | 30.624 | 0.097238 | +0.77% | 1.38x |
| 12 | USELESS/USD | 30.142 | 0.09962 | +0.25% | 1.14x |

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

- Persisted scans: 885; predictions: 7723; observations: 534780.
- Matured sampled outcomes across 1/6/24/48h: 8364; gap abstentions: 16002. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44644256161 · **Generation:** 885 · **Legacy run:** 44644256161
**Main quote time:** 2026-11-20T00:15:45.862925+00:00 · **Legacy report time:** 2026-11-20T00:16:34.953846+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 895.44 | 71.11 | +0.16% | 6.38x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD ⭐ | 0.96223 | 58.43 | +0.25% | 1.00x | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5422 | 55.39 | +1.25% | 5.67x | STRONG 83/100 | VERY_HIGH 72/100 | Watch |
| 4 | ADA/USD | 0.152177 | 52.59 | +0.28% | 0.61x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 5 | XMR/USD | 499.32 | 42.47 | +0.32% | 0.31x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 6 | PYTH/USD | 0.05336 | 41.71 | +0.43% | 1.83x | MODERATE 66/100 | HIGH 60/100 | Watch |
| 7 | PAXG/USD | 3610.86 | 38.59 | +0.38% | 0.16x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | CAP/USD | 0.097238 | 38.25 | +0.77% | 1.38x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 9 | STRK/USD | 0.03192 | 37.70 | +0.50% | 0.92x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 10 | XAUT/USD | 3613 | 36.94 | +0.37% | 0.86x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 11 | ICNT/USD | 0.431 | 34.01 | +1.01% | 0.39x | WEAK 37/100 | VERY_HIGH 82/100 | Watch |
| 12 | USELESS/USD | 0.09962 | 32.85 | +0.25% | 1.14x | WEAK 41/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD | 1759.67 | 59.73 | +0.12% | 2.16x | 60566 | STRONG 75/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 895.68 | 59.37 | +0.16% | 6.38x | 24211 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.96196 | 54.50 | +0.25% | 1.00x | 33645 | STRONG 72/100 | HIGH 62/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5418 | 54.14 | +1.25% | 5.67x | 3664 | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 5 | AUD/USD | 0.66624 | 50.45 | +0.09% | 2.92x | 3889 | STRONG 70/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 66.9 | 49.94 | +0.13% | 1.07x | 15654 | MODERATE 50/100 | HIGH 62/100 | Watch |
| 7 | XDG/USD | 0.0582658 | 49.40 | +0.14% | 1.16x | 5219 | MODERATE 50/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, XRP/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
