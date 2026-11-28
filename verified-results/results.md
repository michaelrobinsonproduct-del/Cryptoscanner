# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T06:07:44.334925+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46114927312
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 978882d750a964c3980e24af62b49e4cfb5fdcde (atomic ledger/results publication)
**Ledger generation:** 2115 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 418.14 | 67.192 | 65.436 | +2.67% | +0.31% | 1.02x | 16.5 | 2026-11-28T06:07:41.880836+00:00 | Not calibrated | MODERATE 64/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004264 | 61.442 | 39.294 | +2.06% | +1.43% | 11.43x | 11.7 | 2026-11-28T06:07:41.880836+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ZEC/USD | 736.48 | 55.590 | 56.752 | +0.26% | -0.66% | 1.21x | 0.1 | 2026-11-28T06:07:41.880836+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SENT/USD | 0.02424 | 54.286 | 42.626 | +2.22% | -0.67% | 3.02x | 7.8 | 2026-11-28T06:07:41.880836+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | VVV/USD | 26.035 | 49.150 | 48.543 | +1.11% | +0.06% | 1.03x | 9.6 | 2026-11-28T06:07:41.880836+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 65.436 | 418.14 | +0.31% | 1.02x |
| 2 | ZEC/USD | 56.752 | 736.48 | -0.66% | 1.21x |
| 3 | VVV/USD | 48.543 | 26.035 | +0.06% | 1.03x |
| 4 | SENT/USD | 42.626 | 0.02424 | -0.67% | 3.02x |
| 5 | SPACE/USD | 39.294 | 0.004264 | +1.43% | 11.43x |

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

- Persisted scans: 2115; predictions: 18967; observations: 1280736.
- Matured sampled outcomes across 1/6/24/48h: 44326; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46114927312 · **Generation:** 2115 · **Legacy run:** 46114927312
**Main quote time:** 2026-11-28T06:07:44.334925+00:00 · **Legacy report time:** 2026-11-28T06:08:40.367990+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 418.14 | 67.19 | +0.31% | 1.02x | STRONG 74/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004264 | 61.44 | +1.43% | 11.43x | STRONG 91/100 | VERY_HIGH 73/100 | Watch |
| 3 | ZEC/USD | 736.48 | 55.59 | -0.66% | 1.21x | WEAK 38/100 | HIGH 68/100 | Watch |
| 4 | SENT/USD | 0.02424 | 54.29 | -0.67% | 3.02x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 5 | VVV/USD ⭐ | 26.035 | 49.15 | +0.06% | 1.03x | MODERATE 60/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 419.85 | 75.07 | +0.31% | 1.02x | 14927 | STRONG 78/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004267 | 54.75 | +1.43% | 11.43x | 1974 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD ⭐ | 26.076 | 47.31 | +0.06% | 1.03x | 8026 | MODERATE 59/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD, SPACE/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
