# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T06:31:24.006863+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45952186569
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 665fa46b8806cbeaba2559ace6e329e3059ecba4 (atomic ledger/results publication)
**Ledger generation:** 1971 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 757.71 | 101.424 | 99.934 | +11.16% | -0.66% | 1.48x | 0.1 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 66.08 | 95.802 | 96.913 | +6.20% | -0.33% | 1.05x | 3.0 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ADA/USD | 0.15313 | 86.949 | 72.807 | +3.15% | -0.17% | 2.83x | 2.5 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LINK/USD | 9.63357 | 80.817 | 80.216 | +3.94% | -0.27% | 1.19x | 4.7 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0580248 | 80.791 | 66.516 | +2.93% | -0.14% | 8.72x | 0.0 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97062 | 74.634 | 75.642 | +2.96% | -0.11% | 0.96x | 0.1 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ETH/USD | 1733.8 | 73.515 | 74.100 | +2.73% | -0.31% | 1.09x | 0.1 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XLM/USD | 0.129733 | 71.121 | 55.338 | +2.47% | +0.16% | 3.58x | 1.1 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 72.94 | 68.969 | 74.049 | +2.82% | -0.31% | 0.65x | 1.4 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XBT/USD | 61660.6 | 65.193 | 68.444 | +1.92% | -0.32% | 0.84x | 0.0 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 11 | BNB/USD | 565.52 | 63.218 | 49.400 | +2.19% | -0.24% | 2.68x | 1.4 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6857 | 62.934 | 72.318 | +2.70% | -0.25% | 0.19x | 1.5 | 2026-11-27T06:31:16.001023+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.934 | 757.71 | -0.66% | 1.48x |
| 2 | HYPE/USD | 96.913 | 66.08 | -0.33% | 1.05x |
| 3 | LINK/USD | 80.216 | 9.63357 | -0.27% | 1.19x |
| 4 | XRP/USD | 75.642 | 0.97062 | -0.11% | 0.96x |
| 5 | ETH/USD | 74.100 | 1733.8 | -0.31% | 1.09x |
| 6 | SOL/USD | 74.049 | 72.94 | -0.31% | 0.65x |
| 7 | ADA/USD | 72.807 | 0.15313 | -0.17% | 2.83x |
| 8 | SUI/USD | 72.318 | 0.6857 | -0.25% | 0.19x |
| 9 | XBT/USD | 68.444 | 61660.6 | -0.32% | 0.84x |
| 10 | XDG/USD | 66.516 | 0.0580248 | -0.14% | 8.72x |
| 11 | XLM/USD | 55.338 | 0.129733 | +0.16% | 3.58x |
| 12 | BNB/USD | 49.400 | 565.52 | -0.24% | 2.68x |

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

- Persisted scans: 1971; predictions: 17354; observations: 1193666.
- Matured sampled outcomes across 1/6/24/48h: 38325; gap abstentions: 25578. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45952186569 · **Generation:** 1971 · **Legacy run:** 45952186569
**Main quote time:** 2026-11-27T06:31:24.006863+00:00 · **Legacy report time:** 2026-11-27T06:31:59.160601+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 757.71 | 101.42 | -0.66% | 1.48x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 66.08 | 95.80 | -0.33% | 1.05x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 3 | ADA/USD | 0.15313 | 86.95 | -0.17% | 2.83x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | LINK/USD | 9.63357 | 80.82 | -0.27% | 1.19x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 5 | XDG/USD | 0.0580248 | 80.79 | -0.14% | 8.72x | STRONG 70/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.97062 | 74.63 | -0.11% | 0.96x | WEAK 42/100 | HIGH 68/100 | Watch |
| 7 | ETH/USD | 1733.8 | 73.52 | -0.31% | 1.09x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 8 | XLM/USD | 0.129733 | 71.12 | +0.16% | 3.58x | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD | 72.94 | 68.97 | -0.31% | 0.65x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | XBT/USD | 61660.6 | 65.19 | -0.32% | 0.84x | WEAK 38/100 | HIGH 68/100 | Watch |
| 11 | BNB/USD | 565.52 | 63.22 | -0.24% | 2.68x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 12 | SUI/USD | 0.6857 | 62.93 | -0.25% | 0.19x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04997 | 86.17 | +0.38% | 5.64x | 8876 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 2 | TIA/USD | 0.3494 | 80.74 | +0.32% | 1.33x | 2604 | STRONG 85/100 | HIGH 67/100 | Watch |
| 3 | PEPE/USD | 3.603e-06 | 77.32 | +0.08% | 1.02x | 5308 | MODERATE 64/100 | HIGH 62/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
