# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T03:07:39.785175+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46101093712
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 81aec22aee4a508b0fa3e721465a60f06ecfc7ef (atomic ledger/results publication)
**Ledger generation:** 2097 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.39 | 75.003 | 64.146 | +1.42% | +0.23% | 1.97x | 1.6 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0476 | 68.797 | 60.670 | +0.97% | +0.08% | 1.77x | 2.3 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 750.54 | 65.162 | 67.352 | +2.17% | +0.30% | 0.63x | 5.7 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XMR/USD | 416.14 | 60.425 | 59.536 | +2.18% | +0.95% | 0.61x | 21.4 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024341 | 52.802 | 48.364 | +2.64% | +0.98% | 0.95x | 2.1 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | VVV/USD | 26.103 | 51.528 | 52.199 | +1.37% | +0.36% | 0.75x | 8.4 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 7 | BCH/USD | 209.14 | 38.676 | 42.730 | +1.03% | +0.11% | 0.54x | 3.8 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.0755 | 36.923 | 43.918 | +1.82% | +0.05% | 0.27x | 6.6 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | SHX/USD | 0.003376 | 34.248 | 17.273 | +0.84% | +0.54% | 2.43x | 38.5 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | SEI/USD | 0.03858 | 25.653 | 30.601 | +0.44% | +0.23% | 0.39x | 10.4 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | XTZ/USD | 0.22813 | 23.383 | 28.131 | +0.39% | +0.22% | 0.41x | 10.9 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | BIGTIME/USD | 0.00573 | 18.209 | 22.934 | +0.97% | -0.73% | 0.89x | 29.8 | 2026-11-28T03:07:31.648257+00:00 | Not calibrated | WEAK 4/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 67.352 | 750.54 | +0.30% | 0.63x |
| 2 | HYPE/USD | 64.146 | 64.39 | +0.23% | 1.97x |
| 3 | NEAR/USD | 60.670 | 3.0476 | +0.08% | 1.77x |
| 4 | XMR/USD | 59.536 | 416.14 | +0.95% | 0.61x |
| 5 | VVV/USD | 52.199 | 26.103 | +0.36% | 0.75x |
| 6 | SENT/USD | 48.364 | 0.024341 | +0.98% | 0.95x |
| 7 | CC/USD | 43.918 | 0.0755 | +0.05% | 0.27x |
| 8 | BCH/USD | 42.730 | 209.14 | +0.11% | 0.54x |
| 9 | SEI/USD | 30.601 | 0.03858 | +0.23% | 0.39x |
| 10 | XTZ/USD | 28.131 | 0.22813 | +0.22% | 0.41x |
| 11 | BIGTIME/USD | 22.934 | 0.00573 | -0.73% | 0.89x |
| 12 | SHX/USD | 17.273 | 0.003376 | +0.54% | 2.43x |

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

- Persisted scans: 2097; predictions: 18823; observations: 1269828.
- Matured sampled outcomes across 1/6/24/48h: 43442; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46101093712 · **Generation:** 2097 · **Legacy run:** 46101093712
**Main quote time:** 2026-11-28T03:07:39.785175+00:00 · **Legacy report time:** 2026-11-28T03:08:22.646142+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.39 | 75.00 | +0.23% | 1.97x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.0476 | 68.80 | +0.08% | 1.77x | STRONG 79/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD | 750.54 | 65.16 | +0.30% | 0.63x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 4 | XMR/USD | 416.14 | 60.42 | +0.95% | 0.61x | MODERATE 50/100 | VERY_HIGH 82/100 | Watch |
| 5 | SENT/USD | 0.024341 | 52.80 | +0.98% | 0.95x | MODERATE 56/100 | VERY_HIGH 74/100 | Watch |
| 6 | VVV/USD | 26.103 | 51.53 | +0.36% | 0.75x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 7 | BCH/USD | 209.14 | 38.68 | +0.11% | 0.54x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.0755 | 36.92 | +0.05% | 0.27x | WEAK 38/100 | VERY_HIGH 75/100 | Watch |
| 9 | SHX/USD | 0.003376 | 34.25 | +0.54% | 2.43x | MODERATE 57/100 | VERY_HIGH 79/100 | Watch |
| 10 | SEI/USD | 0.03858 | 25.65 | +0.23% | 0.39x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 11 | XTZ/USD | 0.22813 | 23.38 | +0.22% | 0.41x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 12 | BIGTIME/USD | 0.00573 | 18.21 | -0.73% | 0.89x | WEAK 4/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.39 | 70.48 | +0.23% | 1.97x | 18632 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.0464 | 60.64 | +0.08% | 1.77x | 13178 | STRONG 75/100 | HIGH 55/100 | Watch |
| 3 | AUD/USD | 0.66551 | 49.81 | +0.13% | 20.34x | 4027 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
