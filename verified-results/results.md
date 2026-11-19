# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T19:10:30.059168+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44595389852
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 6bef858f9194cfa6abfd619c90ea436c30100426 (atomic ledger/results publication)
**Ledger generation:** 841 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.1279 | 79.448 | 72.922 | +8.21% | -1.69% | 3.57x | 7.8 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 2 | VVV/USD | 22.489 | 68.399 | 77.864 | +3.77% | -0.59% | 0.35x | 7.1 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021438 | 67.297 | 58.224 | +4.04% | +0.14% | 1.83x | 8.9 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 4 | SOL/USD | 73.82 | 65.988 | 56.988 | +0.38% | -0.35% | 2.08x | 1.4 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010171 | 65.500 | 65.788 | +5.58% | +0.45% | 0.74x | 8.9 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5477 | 61.038 | 64.924 | +5.73% | -0.47% | 0.85x | 14.6 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | ADA/USD | 0.152918 | 60.777 | 61.263 | +1.10% | -0.32% | 1.11x | 2.9 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97056 | 57.115 | 57.211 | +0.43% | -0.25% | 1.12x | 1.6 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | HYPE/USD | 67.95 | 52.331 | 64.727 | +1.60% | -1.42% | 0.47x | 2.9 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 10 | TAO/USD | 194.7433 | 52.244 | 59.952 | +1.45% | -0.07% | 0.26x | 6.8 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ALEO/USD | 0.03083 | 47.642 | 53.397 | +2.84% | +0.10% | 0.38x | 3.2 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | BNB/USD | 585.14 | 46.529 | 45.003 | +0.66% | -0.27% | 1.29x | 1.7 | 2026-11-19T19:10:23.976096+00:00 | Not calibrated | WEAK 33/100 | HIGH 61/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.864 | 22.489 | -0.59% | 0.35x |
| 2 | CT/USD | 72.922 | 0.1279 | -1.69% | 3.57x |
| 3 | SKR/USD | 65.788 | 0.010171 | +0.45% | 0.74x |
| 4 | AKT/USD | 64.924 | 0.5477 | -0.47% | 0.85x |
| 5 | HYPE/USD | 64.727 | 67.95 | -1.42% | 0.47x |
| 6 | ADA/USD | 61.263 | 0.152918 | -0.32% | 1.11x |
| 7 | TAO/USD | 59.952 | 194.7433 | -0.07% | 0.26x |
| 8 | SENT/USD | 58.224 | 0.021438 | +0.14% | 1.83x |
| 9 | XRP/USD | 57.211 | 0.97056 | -0.25% | 1.12x |
| 10 | SOL/USD | 56.988 | 73.82 | -0.35% | 2.08x |
| 11 | ALEO/USD | 53.397 | 0.03083 | +0.10% | 0.38x |
| 12 | BNB/USD | 45.003 | 585.14 | -0.27% | 1.29x |

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

- Persisted scans: 841; predictions: 7236; observations: 508336.
- Matured sampled outcomes across 1/6/24/48h: 7247; gap abstentions: 15570. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44595389852 · **Generation:** 841 · **Legacy run:** 44595389852
**Main quote time:** 2026-11-19T19:10:30.059168+00:00 · **Legacy report time:** 2026-11-19T19:11:29.591089+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD | 0.1279 | 79.45 | -1.69% | 3.57x | STRONG 70/100 | VERY_HIGH 70/100 | Do nothing |
| 2 | VVV/USD | 22.489 | 68.40 | -0.59% | 0.35x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 3 | SENT/USD ⭐ | 0.021438 | 67.30 | +0.14% | 1.83x | STRONG 79/100 | HIGH 60/100 | Watch |
| 4 | SOL/USD | 73.82 | 65.99 | -0.35% | 2.08x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | SKR/USD | 0.010171 | 65.50 | +0.45% | 0.74x | MODERATE 63/100 | VERY_HIGH 82/100 | Watch |
| 6 | AKT/USD | 0.5477 | 61.04 | -0.47% | 0.85x | WEAK 31/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | ADA/USD | 0.152918 | 60.78 | -0.32% | 1.11x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.97056 | 57.12 | -0.25% | 1.12x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | HYPE/USD | 67.95 | 52.33 | -1.42% | 0.47x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |
| 10 | TAO/USD | 194.7433 | 52.24 | -0.07% | 0.26x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ALEO/USD | 0.03083 | 47.64 | +0.10% | 0.38x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |
| 12 | BNB/USD | 585.14 | 46.53 | -0.27% | 1.29x | WEAK 33/100 | HIGH 61/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021476 | 83.93 | +0.14% | 1.83x | 14636 | STRONG 87/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
