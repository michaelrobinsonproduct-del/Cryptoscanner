# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T23:51:13.732165+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45085315253
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 48509d7c5e251bbf74db6d88c1f32135e20122ae (atomic ledger/results publication)
**Ledger generation:** 1352 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.32 | 99.483 | 90.582 | +5.70% | -0.26% | 2.02x | 5.7 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PUMP/USD | 0.002583 | 92.151 | 83.157 | +10.20% | +0.39% | 1.71x | 7.7 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | PEARL/USD | 2.0506 | 84.520 | 75.767 | +5.25% | +0.82% | 1.46x | 2.9 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ZEC/USD | 792.88 | 82.861 | 67.917 | +1.89% | -0.01% | 3.56x | 0.6 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04946 | 79.745 | 89.983 | +11.70% | -0.40% | 0.18x | 10.1 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.7129 | 78.296 | 78.178 | +9.10% | +0.00% | 1.01x | 15.1 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9707 | 72.998 | 73.954 | +2.92% | -0.11% | 0.96x | 3.0 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.91 | 71.391 | 72.498 | +2.73% | +0.03% | 0.87x | 3.2 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 61189.2 | 70.774 | 67.798 | +1.83% | +0.11% | 1.24x | 0.0 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ETH/USD | 1719.69 | 62.931 | 70.217 | +2.22% | -0.08% | 0.31x | 0.7 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 70.51 | 61.420 | 57.682 | +0.48% | -0.01% | 1.38x | 1.4 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XMR/USD | 493.03 | 55.419 | 53.605 | +0.25% | -0.37% | 1.37x | 6.3 | 2026-11-22T23:51:07.082238+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.582 | 26.32 | -0.26% | 2.02x |
| 2 | NIGHT/USD | 89.983 | 0.04946 | -0.40% | 0.18x |
| 3 | PUMP/USD | 83.157 | 0.002583 | +0.39% | 1.71x |
| 4 | PIEVERSE/USD | 78.178 | 3.7129 | +0.00% | 1.01x |
| 5 | PEARL/USD | 75.767 | 2.0506 | +0.82% | 1.46x |
| 6 | NEAR/USD | 73.954 | 2.9707 | -0.11% | 0.96x |
| 7 | HYPE/USD | 72.498 | 62.91 | +0.03% | 0.87x |
| 8 | ETH/USD | 70.217 | 1719.69 | -0.08% | 0.31x |
| 9 | ZEC/USD | 67.917 | 792.88 | -0.01% | 3.56x |
| 10 | XBT/USD | 67.798 | 61189.2 | +0.11% | 1.24x |
| 11 | SOL/USD | 57.682 | 70.51 | -0.01% | 1.38x |
| 12 | XMR/USD | 53.605 | 493.03 | -0.37% | 1.37x |

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

- Persisted scans: 1352; predictions: 11143; observations: 818475.
- Matured sampled outcomes across 1/6/24/48h: 17318; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 62 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45085315253 · **Generation:** 1352 · **Legacy run:** 45085315253
**Main quote time:** 2026-11-22T23:51:13.732165+00:00 · **Legacy report time:** 2026-11-22T23:52:01.992706+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.32 | 99.48 | -0.26% | 2.02x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002583 | 92.15 | +0.39% | 1.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEARL/USD ⭐ | 2.0506 | 84.52 | +0.82% | 1.46x | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | ZEC/USD | 792.88 | 82.86 | -0.01% | 3.56x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04946 | 79.74 | -0.40% | 0.18x | WEAK 40/100 | VERY_HIGH 82/100 | Watch |
| 6 | PIEVERSE/USD | 3.7129 | 78.30 | +0.00% | 1.01x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 7 | NEAR/USD | 2.9707 | 73.00 | -0.11% | 0.96x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | HYPE/USD | 62.91 | 71.39 | +0.03% | 0.87x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD ⭐ | 61189.2 | 70.77 | +0.11% | 1.24x | STRONG 70/100 | HIGH 62/100 | Watch |
| 10 | ETH/USD | 1719.69 | 62.93 | -0.08% | 0.31x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 70.51 | 61.42 | -0.01% | 1.38x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 12 | XMR/USD | 493.03 | 55.42 | -0.37% | 1.37x | MODERATE 48/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.0506 | 89.75 | +0.82% | 1.46x | 6234 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | PUMP/USD ⭐ | 0.002595 | 81.24 | +0.39% | 1.71x | 4391 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 3 | XBT/USD ⭐ | 61194 | 75.31 | +0.11% | 1.24x | 131825 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PUMP/USD, PEARL/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
