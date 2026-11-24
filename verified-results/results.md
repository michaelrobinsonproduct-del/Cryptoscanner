# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T00:23:57.155387+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45296234243
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9e88a973381a87e722f0a530293def4f78854879 (atomic ledger/results publication)
**Ledger generation:** 1500 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.148984 | 72.681 | 55.585 | +0.36% | +0.42% | 2.97x | 3.9 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0052 | 66.524 | 57.805 | +0.81% | +0.72% | 1.51x | 5.7 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 488.35 | 58.688 | 57.434 | +0.48% | +0.66% | 0.80x | 1.8 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94195 | 58.017 | 56.855 | +0.27% | +0.40% | 0.92x | 0.1 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XLM/USD | 0.130593 | 57.126 | 58.111 | +0.46% | +0.39% | 0.71x | 0.2 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0564545 | 55.276 | 56.645 | +0.27% | +0.36% | 0.68x | 0.4 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | LINK/USD | 9.03507 | 52.518 | 55.649 | +0.33% | +0.38% | 0.50x | 3.4 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SUI/USD | 0.676 | 52.288 | 57.275 | +0.43% | +0.30% | 0.35x | 1.5 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 41.57 | 49.929 | 56.333 | +0.36% | +0.31% | 0.20x | 2.4 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | QNT/USD | 154.76 | 48.633 | 54.626 | +0.45% | +0.18% | 0.31x | 7.1 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | UNI/USD | 4.8721 | 47.367 | 53.678 | +0.70% | +0.57% | 0.08x | 5.3 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | BNB/USD | 557.13 | 46.318 | 42.252 | +0.33% | +0.30% | 1.26x | 2.0 | 2026-11-24T00:23:49.568173+00:00 | Not calibrated | MODERATE 58/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 58.111 | 0.130593 | +0.39% | 0.71x |
| 2 | NEAR/USD | 57.805 | 3.0052 | +0.72% | 1.51x |
| 3 | XMR/USD | 57.434 | 488.35 | +0.66% | 0.80x |
| 4 | SUI/USD | 57.275 | 0.676 | +0.30% | 0.35x |
| 5 | XRP/USD | 56.855 | 0.94195 | +0.40% | 0.92x |
| 6 | XDG/USD | 56.645 | 0.0564545 | +0.36% | 0.68x |
| 7 | LTC/USD | 56.333 | 41.57 | +0.31% | 0.20x |
| 8 | LINK/USD | 55.649 | 9.03507 | +0.38% | 0.50x |
| 9 | ADA/USD | 55.585 | 0.148984 | +0.42% | 2.97x |
| 10 | QNT/USD | 54.626 | 154.76 | +0.18% | 0.31x |
| 11 | UNI/USD | 53.678 | 4.8721 | +0.57% | 0.08x |
| 12 | BNB/USD | 42.252 | 557.13 | +0.30% | 1.26x |

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

- Persisted scans: 1500; predictions: 12757; observations: 908602.
- Matured sampled outcomes across 1/6/24/48h: 23416; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45296234243 · **Generation:** 1500 · **Legacy run:** 45296234243
**Main quote time:** 2026-11-24T00:23:57.155387+00:00 · **Legacy report time:** 2026-11-24T00:25:08.565738+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.148984 | 72.68 | +0.42% | 2.97x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.0052 | 66.52 | +0.72% | 1.51x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD | 488.35 | 58.69 | +0.66% | 0.80x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.94195 | 58.02 | +0.40% | 0.92x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 5 | XLM/USD | 0.130593 | 57.13 | +0.39% | 0.71x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | XDG/USD | 0.0564545 | 55.28 | +0.36% | 0.68x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | LINK/USD | 9.03507 | 52.52 | +0.38% | 0.50x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 8 | SUI/USD | 0.676 | 52.29 | +0.30% | 0.35x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 41.57 | 49.93 | +0.31% | 0.20x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 10 | QNT/USD | 154.76 | 48.63 | +0.18% | 0.31x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 11 | UNI/USD | 4.8721 | 47.37 | +0.57% | 0.08x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | BNB/USD | 557.13 | 46.32 | +0.30% | 1.26x | MODERATE 58/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.0781 | 63.83 | +1.96% | 2.96x | 4569 | STRONG 77/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0052 | 61.10 | +0.81% | 1.09x | 20397 | STRONG 76/100 | HIGH 62/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149002 | 58.44 | +0.53% | 3.36x | 14173 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.94167 | 56.01 | +0.35% | 1.54x | 43917 | STRONG 83/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ADA/USD, NEAR/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
