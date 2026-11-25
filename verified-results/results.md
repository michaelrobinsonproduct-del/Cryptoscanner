# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T23:56:40.340358+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45724864897
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 604516c2efa397aae55ba1000e3c29503db2c5da (atomic ledger/results publication)
**Ledger generation:** 1784 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.75 | 102.807 | 85.218 | +4.65% | +0.52% | 3.70x | 4.7 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 774.1 | 102.480 | 84.350 | +4.77% | +0.63% | 3.82x | 8.0 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.0477 | 99.041 | 92.143 | +5.66% | +0.79% | 1.30x | 4.9 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | TRUMP/USD | 0.888 | 91.367 | 70.672 | +6.09% | +1.14% | 3.78x | 11.3 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | STRONG 96/100 | HIGH 66/100 | Consider small entry | WATCH |
| 5 | ETH/USD | 1693.17 | 76.832 | 61.421 | +0.92% | +0.08% | 2.58x | 0.1 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 61.67 | 71.279 | 75.235 | +3.01% | +0.36% | 0.42x | 1.6 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XBT/USD | 60447.5 | 66.216 | 63.266 | +1.18% | +0.22% | 1.18x | 0.0 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93733 | 60.238 | 65.345 | +1.49% | +0.05% | 0.47x | 0.1 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04897 | 56.574 | 43.103 | +0.31% | -0.31% | 12.80x | 6.1 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 10 | UNI/USD | 4.739 | 52.281 | 52.812 | +0.59% | +0.39% | 0.75x | 4.2 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0559709 | 49.773 | 57.439 | +1.33% | +0.20% | 0.13x | 0.0 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.474e-06 | 46.904 | 46.920 | +0.61% | +0.52% | 0.74x | 2.9 | 2026-11-25T23:56:33.383249+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 92.143 | 3.0477 | +0.79% | 1.30x |
| 2 | LTC/USD | 85.218 | 42.75 | +0.52% | 3.70x |
| 3 | ZEC/USD | 84.350 | 774.1 | +0.63% | 3.82x |
| 4 | HYPE/USD | 75.235 | 61.67 | +0.36% | 0.42x |
| 5 | TRUMP/USD | 70.672 | 0.888 | +1.14% | 3.78x |
| 6 | XRP/USD | 65.345 | 0.93733 | +0.05% | 0.47x |
| 7 | XBT/USD | 63.266 | 60447.5 | +0.22% | 1.18x |
| 8 | ETH/USD | 61.421 | 1693.17 | +0.08% | 2.58x |
| 9 | XDG/USD | 57.439 | 0.0559709 | +0.20% | 0.13x |
| 10 | UNI/USD | 52.812 | 4.739 | +0.39% | 0.75x |
| 11 | PEPE/USD | 46.920 | 3.474e-06 | +0.52% | 0.74x |
| 12 | NIGHT/USD | 43.103 | 0.04897 | -0.31% | 12.80x |

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

- Persisted scans: 1784; predictions: 15152; observations: 1081500.
- Matured sampled outcomes across 1/6/24/48h: 32937; gap abstentions: 23435. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45724864897 · **Generation:** 1784 · **Legacy run:** 45724864897
**Main quote time:** 2026-11-25T23:56:40.340358+00:00 · **Legacy report time:** 2026-11-25T23:57:57.417236+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.75 | 102.81 | +0.52% | 3.70x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 774.1 | 102.48 | +0.63% | 3.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.0477 | 99.04 | +0.79% | 1.30x | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | TRUMP/USD | 0.888 | 91.37 | +1.14% | 3.78x | STRONG 96/100 | HIGH 66/100 | Consider small entry |
| 5 | ETH/USD | 1693.17 | 76.83 | +0.08% | 2.58x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 61.67 | 71.28 | +0.36% | 0.42x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | XBT/USD | 60447.5 | 66.22 | +0.22% | 1.18x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 8 | XRP/USD | 0.93733 | 60.24 | +0.05% | 0.47x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | NIGHT/USD | 0.04897 | 56.57 | -0.31% | 12.80x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 10 | UNI/USD | 4.739 | 52.28 | +0.39% | 0.75x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0559709 | 49.77 | +0.20% | 0.13x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 12 | PEPE/USD | 3.474e-06 | 46.90 | +0.52% | 0.74x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.73 | 100.00 | +0.52% | 3.70x | 14002 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 771.36 | 100.00 | +0.63% | 3.82x | 43906 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.0488 | 94.36 | +0.79% | 1.30x | 17380 | STRONG 92/100 | HIGH 55/100 | Watch |
| 4 | XLM/USD | 0.127977 | 78.37 | +0.21% | 1.56x | 8317 | STRONG 84/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** LTC/USD, ZEC/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
