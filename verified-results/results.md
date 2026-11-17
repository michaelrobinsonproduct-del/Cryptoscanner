# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:25:07.889986+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44199110150
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** 6c9e8ee087a6f672645ea6cf29285f0e25b49c99 (atomic ledger/results publication)
**Ledger generation:** 470 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 960.51 | 112.226 | 96.469 | +6.27% | +1.38% | 1.89x | 4.9 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SOL/USD | 75.1 | 102.715 | 89.373 | +5.01% | -0.33% | 3.80x | 1.3 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.3649 | 98.304 | 97.622 | +6.56% | +1.05% | 0.54x | 4.8 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | INJ/USD | 7.331 | 97.980 | 95.417 | +6.26% | +0.81% | 0.85x | 6.8 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XRP/USD | 0.98517 | 97.626 | 77.245 | +3.19% | +1.08% | 6.58x | 0.1 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | RENDER/USD | 1.48 | 92.627 | 72.162 | +7.48% | +1.09% | 2.78x | 13.5 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 96/100 | HIGH 66/100 | Consider small entry | WATCH |
| 7 | TAO/USD | 196.963 | 88.591 | 73.468 | +3.01% | +0.02% | 2.97x | 5.3 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SUI/USD | 0.7378 | 85.197 | 71.549 | +2.56% | -0.27% | 14.44x | 2.7 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0600227 | 80.828 | 67.932 | +1.93% | -0.42% | 3.69x | 0.5 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 10 | WINGS/USD | 0.001925 | 74.827 | 73.710 | +8.21% | +0.26% | 0.98x | 5.2 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | XMR/USD | 509.55 | 69.567 | 75.980 | +3.24% | +0.17% | 0.28x | 3.3 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LTC/USD | 45.19 | 69.023 | 55.374 | +1.62% | -0.18% | 2.45x | 2.2 | 2026-11-17T23:24:59.812946+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 97.622 | 3.3649 | +1.05% | 0.54x |
| 2 | ZEC/USD | 96.469 | 960.51 | +1.38% | 1.89x |
| 3 | INJ/USD | 95.417 | 7.331 | +0.81% | 0.85x |
| 4 | SOL/USD | 89.373 | 75.1 | -0.33% | 3.80x |
| 5 | XRP/USD | 77.245 | 0.98517 | +1.08% | 6.58x |
| 6 | XMR/USD | 75.980 | 509.55 | +0.17% | 0.28x |
| 7 | WINGS/USD | 73.710 | 0.001925 | +0.26% | 0.98x |
| 8 | TAO/USD | 73.468 | 196.963 | +0.02% | 2.97x |
| 9 | RENDER/USD | 72.162 | 1.48 | +1.09% | 2.78x |
| 10 | SUI/USD | 71.549 | 0.7378 | -0.27% | 14.44x |
| 11 | XDG/USD | 67.932 | 0.0600227 | -0.42% | 3.69x |
| 12 | LTC/USD | 55.374 | 45.19 | -0.18% | 2.45x |

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

- Persisted scans: 470; predictions: 4121; observations: 283237.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44199110150 · **Generation:** 470 · **Legacy run:** 44199110150
**Main quote time:** 2026-11-17T23:25:07.889986+00:00 · **Legacy report time:** 2026-11-17T23:25:19.226867+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 960.51 | 112.23 | +1.38% | 1.89x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD | 75.1 | 102.71 | -0.33% | 3.80x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD | 3.3649 | 98.30 | +1.05% | 0.54x | STRONG 79/100 | VERY_HIGH 70/100 | Watch |
| 4 | INJ/USD | 7.331 | 97.98 | +0.81% | 0.85x | STRONG 79/100 | HIGH 62/100 | Watch |
| 5 | XRP/USD | 0.98517 | 97.63 | +1.08% | 6.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | RENDER/USD | 1.48 | 92.63 | +1.09% | 2.78x | STRONG 96/100 | HIGH 66/100 | Consider small entry |
| 7 | TAO/USD | 196.963 | 88.59 | +0.02% | 2.97x | STRONG 89/100 | HIGH 55/100 | Watch |
| 8 | SUI/USD | 0.7378 | 85.20 | -0.27% | 14.44x | STRONG 73/100 | HIGH 61/100 | Watch |
| 9 | XDG/USD | 0.0600227 | 80.83 | -0.42% | 3.69x | STRONG 70/100 | HIGH 61/100 | Watch |
| 10 | WINGS/USD | 0.001925 | 74.83 | +0.26% | 0.98x | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |
| 11 | XMR/USD | 509.55 | 69.57 | +0.17% | 0.28x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 12 | LTC/USD | 45.19 | 69.02 | -0.18% | 2.45x | MODERATE 65/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 962.13 | 93.02 | +0.37% | 2.66x | 26513 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | USELESS/USD | 0.09723 | 85.34 | +1.71% | 13.74x | 4199 | STRONG 88/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
