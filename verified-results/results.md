# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T23:12:19.650249+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46080882473
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 999940084b8124690127be38cb10a44ce15f9730 (atomic ledger/results publication)
**Ledger generation:** 2073 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 729.25 | 94.218 | 98.148 | +6.98% | +0.41% | 0.40x | 3.7 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XDG/USD | 0.0574446 | 84.203 | 68.070 | +1.90% | +0.23% | 4.34x | 0.4 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 44.54 | 82.242 | 66.680 | +1.83% | +0.11% | 3.25x | 2.2 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.05024 | 73.886 | 79.567 | +3.65% | +0.42% | 0.22x | 2.0 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.71 | 71.686 | 70.978 | +2.39% | +0.31% | 0.91x | 1.6 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 6 | UNI/USD | 4.816 | 71.566 | 73.995 | +3.57% | +0.22% | 0.64x | 5.4 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SKY/USD | 0.05176 | 65.541 | 79.108 | +11.53% | -2.08% | 0.68x | 9.7 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | SPACE/USD | 0.004161 | 63.785 | 70.985 | +7.46% | +0.43% | 0.06x | 9.6 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | PAXG/USD | 3647.08 | 62.637 | 61.649 | +2.54% | +0.01% | 1.09x | 1.3 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.528e-06 | 56.252 | 53.980 | +1.44% | +0.09% | 1.18x | 2.8 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 11 | FET/USD | 0.1258 | 55.088 | 64.386 | +4.49% | +0.00% | 0.07x | 7.9 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 71.38 | 53.553 | 58.641 | +0.62% | +0.06% | 0.46x | 1.4 | 2026-11-27T23:12:13.080312+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.148 | 729.25 | +0.41% | 0.40x |
| 2 | NIGHT/USD | 79.567 | 0.05024 | +0.42% | 0.22x |
| 3 | SKY/USD | 79.108 | 0.05176 | -2.08% | 0.68x |
| 4 | UNI/USD | 73.995 | 4.816 | +0.22% | 0.64x |
| 5 | SPACE/USD | 70.985 | 0.004161 | +0.43% | 0.06x |
| 6 | HYPE/USD | 70.978 | 63.71 | +0.31% | 0.91x |
| 7 | XDG/USD | 68.070 | 0.0574446 | +0.23% | 4.34x |
| 8 | LTC/USD | 66.680 | 44.54 | +0.11% | 3.25x |
| 9 | FET/USD | 64.386 | 0.1258 | +0.00% | 0.07x |
| 10 | PAXG/USD | 61.649 | 3647.08 | +0.01% | 1.09x |
| 11 | SOL/USD | 58.641 | 71.38 | +0.06% | 0.46x |
| 12 | PEPE/USD | 53.980 | 3.528e-06 | +0.09% | 1.18x |

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

- Persisted scans: 2073; predictions: 18578; observations: 1255286.
- Matured sampled outcomes across 1/6/24/48h: 42383; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46080882473 · **Generation:** 2073 · **Legacy run:** 46080882473
**Main quote time:** 2026-11-27T23:12:19.650249+00:00 · **Legacy report time:** 2026-11-27T23:13:03.718075+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 729.25 | 94.22 | +0.41% | 0.40x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0574446 | 84.20 | +0.23% | 4.34x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 44.54 | 82.24 | +0.11% | 3.25x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD | 0.05024 | 73.89 | +0.42% | 0.22x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 5 | HYPE/USD | 63.71 | 71.69 | +0.31% | 0.91x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 6 | UNI/USD | 4.816 | 71.57 | +0.22% | 0.64x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | SKY/USD | 0.05176 | 65.54 | -2.08% | 0.68x | WEAK 38/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | SPACE/USD | 0.004161 | 63.79 | +0.43% | 0.06x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 9 | PAXG/USD | 3647.08 | 62.64 | +0.01% | 1.09x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 10 | PEPE/USD | 3.528e-06 | 56.25 | +0.09% | 1.18x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 11 | FET/USD | 0.1258 | 55.09 | +0.00% | 0.07x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 71.38 | 53.55 | +0.06% | 0.46x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0574458 | 83.45 | +0.23% | 4.34x | 13340 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 44.54 | 77.80 | +0.11% | 3.25x | 15398 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XDG/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
