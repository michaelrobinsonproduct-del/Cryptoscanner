# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:50:30.916565+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44591876997
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 1fcde03d29509441eefff19e1c673e5701b06664 (atomic ledger/results publication)
**Ledger generation:** 838 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.622 | 81.906 | 82.399 | +4.39% | -0.28% | 1.09x | 6.6 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 2 | HYPE/USD | 69.14 | 71.169 | 77.930 | +3.38% | -1.21% | 0.93x | 1.4 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 3 | CT/USD | 0.1293 | 69.434 | 65.237 | +9.39% | -1.37% | 2.10x | 23.3 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | AKT/USD | 0.5504 | 67.571 | 69.500 | +6.25% | -0.42% | 1.02x | 12.7 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | ADA/USD | 0.153283 | 61.485 | 62.661 | +1.34% | -0.47% | 1.12x | 3.5 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 6 | TRX/USD | 0.310575 | 58.486 | 43.831 | +0.42% | -0.07% | 4.96x | 0.0 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PUMP/USD | 0.002701 | 58.227 | 68.636 | +4.04% | -0.26% | 0.09x | 3.7 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | CSPR/USD | 0.0017543 | 57.571 | 65.176 | +7.42% | -1.05% | 0.76x | 22.9 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 24/100 | EXTREME 96/100 | Do nothing | WATCH |
| 9 | SKR/USD | 0.010125 | 55.791 | 64.888 | +5.11% | -1.04% | 0.61x | 4.0 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 33/100 | EXTREME 92/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.97201 | 54.065 | 59.034 | +0.58% | -0.39% | 0.70x | 0.1 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SOL/USD | 74.11 | 53.169 | 59.751 | +0.78% | -0.40% | 0.54x | 1.3 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | AVAX/USD | 7.04 | 43.905 | 46.246 | +0.27% | -0.58% | 1.06x | 4.3 | 2026-11-19T18:50:24.103103+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.399 | 22.622 | -0.28% | 1.09x |
| 2 | HYPE/USD | 77.930 | 69.14 | -1.21% | 0.93x |
| 3 | AKT/USD | 69.500 | 0.5504 | -0.42% | 1.02x |
| 4 | PUMP/USD | 68.636 | 0.002701 | -0.26% | 0.09x |
| 5 | CT/USD | 65.237 | 0.1293 | -1.37% | 2.10x |
| 6 | CSPR/USD | 65.176 | 0.0017543 | -1.05% | 0.76x |
| 7 | SKR/USD | 64.888 | 0.010125 | -1.04% | 0.61x |
| 8 | ADA/USD | 62.661 | 0.153283 | -0.47% | 1.12x |
| 9 | SOL/USD | 59.751 | 74.11 | -0.40% | 0.54x |
| 10 | XRP/USD | 59.034 | 0.97201 | -0.39% | 0.70x |
| 11 | AVAX/USD | 46.246 | 7.04 | -0.58% | 1.06x |
| 12 | TRX/USD | 43.831 | 0.310575 | -0.07% | 4.96x |

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

- Persisted scans: 838; predictions: 7200; observations: 506539.
- Matured sampled outcomes across 1/6/24/48h: 7199; gap abstentions: 15552. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44591876997 · **Generation:** 838 · **Legacy run:** 44591876997
**Main quote time:** 2026-11-19T18:50:30.916565+00:00 · **Legacy report time:** 2026-11-19T18:51:31.495742+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.622 | 81.91 | -0.28% | 1.09x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 2 | HYPE/USD | 69.14 | 71.17 | -1.21% | 0.93x | WEAK 41/100 | VERY_HIGH 72/100 | Do nothing |
| 3 | CT/USD | 0.1293 | 69.43 | -1.37% | 2.10x | MODERATE 55/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | AKT/USD | 0.5504 | 67.57 | -0.42% | 1.02x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 5 | ADA/USD | 0.153283 | 61.48 | -0.47% | 1.12x | WEAK 41/100 | HIGH 68/100 | Watch |
| 6 | TRX/USD | 0.310575 | 58.49 | -0.07% | 4.96x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 7 | PUMP/USD | 0.002701 | 58.23 | -0.26% | 0.09x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | CSPR/USD | 0.0017543 | 57.57 | -1.05% | 0.76x | WEAK 24/100 | EXTREME 96/100 | Do nothing |
| 9 | SKR/USD | 0.010125 | 55.79 | -1.04% | 0.61x | WEAK 33/100 | EXTREME 92/100 | Do nothing |
| 10 | XRP/USD | 0.97201 | 54.07 | -0.39% | 0.70x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SOL/USD | 74.11 | 53.17 | -0.40% | 0.54x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | AVAX/USD | 7.04 | 43.91 | -0.58% | 1.06x | WEAK 32/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.05622 | 76.65 | +0.37% | 3.93x | 2250 | STRONG 88/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
