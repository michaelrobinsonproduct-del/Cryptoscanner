# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T04:11:37.691458+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45938284897
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 76b0a71a010dc6591f6852847548f46852a1768e (atomic ledger/results publication)
**Ledger generation:** 1957 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.12 | 95.577 | 98.121 | +6.27% | +0.08% | 0.71x | 1.5 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 759.58 | 92.424 | 97.100 | +11.43% | +0.39% | 0.34x | 5.8 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | LINK/USD | 9.50016 | 85.385 | 71.306 | +2.50% | -0.18% | 2.67x | 2.4 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 27.222 | 82.675 | 78.372 | +3.97% | +0.98% | 0.94x | 8.8 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SOL/USD | 72.58 | 76.252 | 70.494 | +2.31% | -0.26% | 1.71x | 1.4 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XBT/USD | 61406.5 | 68.095 | 65.504 | +1.50% | -0.15% | 1.33x | 0.0 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.1076 | 67.702 | 66.779 | +1.96% | +0.07% | 1.06x | 3.9 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ETH/USD | 1728.07 | 64.926 | 71.724 | +2.39% | -0.13% | 0.39x | 0.1 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ADA/USD | 0.151526 | 63.859 | 66.015 | +2.07% | -0.17% | 0.87x | 3.4 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XMR/USD | 465.49 | 63.334 | 66.685 | +1.87% | +0.16% | 0.59x | 2.8 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | UNI/USD | 4.8298 | 63.183 | 67.609 | +3.86% | +0.10% | 0.51x | 4.5 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.95958 | 63.111 | 67.444 | +1.79% | -0.33% | 0.73x | 0.1 | 2026-11-27T04:11:29.257853+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 98.121 | 66.12 | +0.08% | 0.71x |
| 2 | ZEC/USD | 97.100 | 759.58 | +0.39% | 0.34x |
| 3 | VVV/USD | 78.372 | 27.222 | +0.98% | 0.94x |
| 4 | ETH/USD | 71.724 | 1728.07 | -0.13% | 0.39x |
| 5 | LINK/USD | 71.306 | 9.50016 | -0.18% | 2.67x |
| 6 | SOL/USD | 70.494 | 72.58 | -0.26% | 1.71x |
| 7 | UNI/USD | 67.609 | 4.8298 | +0.10% | 0.51x |
| 8 | XRP/USD | 67.444 | 0.95958 | -0.33% | 0.73x |
| 9 | NEAR/USD | 66.779 | 3.1076 | +0.07% | 1.06x |
| 10 | XMR/USD | 66.685 | 465.49 | +0.16% | 0.59x |
| 11 | ADA/USD | 66.015 | 0.151526 | -0.17% | 0.87x |
| 12 | XBT/USD | 65.504 | 61406.5 | -0.15% | 1.33x |

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

- Persisted scans: 1957; predictions: 17186; observations: 1185241.
- Matured sampled outcomes across 1/6/24/48h: 37814; gap abstentions: 25496. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45938284897 · **Generation:** 1957 · **Legacy run:** 45938284897
**Main quote time:** 2026-11-27T04:11:37.691458+00:00 · **Legacy report time:** 2026-11-27T04:12:29.474608+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 66.12 | 95.58 | +0.08% | 0.71x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD | 759.58 | 92.42 | +0.39% | 0.34x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 3 | LINK/USD | 9.50016 | 85.39 | -0.18% | 2.67x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 27.222 | 82.67 | +0.98% | 0.94x | STRONG 71/100 | HIGH 62/100 | Watch |
| 5 | SOL/USD | 72.58 | 76.25 | -0.26% | 1.71x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 6 | XBT/USD | 61406.5 | 68.10 | -0.15% | 1.33x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 7 | NEAR/USD ⭐ | 3.1076 | 67.70 | +0.07% | 1.06x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 8 | ETH/USD | 1728.07 | 64.93 | -0.13% | 0.39x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | ADA/USD | 0.151526 | 63.86 | -0.17% | 0.87x | WEAK 37/100 | HIGH 68/100 | Watch |
| 10 | XMR/USD | 465.49 | 63.33 | +0.16% | 0.59x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | UNI/USD | 4.8298 | 63.18 | +0.10% | 0.51x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.95958 | 63.11 | -0.33% | 0.73x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.1023 | 73.21 | +0.07% | 1.06x | 13891 | STRONG 72/100 | HIGH 62/100 | Watch |
| 2 | USELESS/USD | 0.07722 | 72.99 | +1.33% | 1.01x | 2161 | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
