# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:40:07.972323+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44231962156
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** ef5d85ace6248bb6cbed44711ba696ddb3e57b9b (atomic ledger/results publication)
**Ledger generation:** 521 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019003 | 63.239 | 41.816 | +1.79% | +1.28% | 2.74x | 3.2 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 2.167 | 61.848 | 56.428 | +5.78% | +0.04% | 1.52x | 31.8 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | XMR/USD | 510.29 | 61.715 | 49.395 | +0.28% | -0.54% | 5.41x | 15.1 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 4 | TON/USD | 1.084 | 54.807 | 38.908 | +0.65% | +0.65% | 2.26x | 9.2 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5213 | 52.011 | 43.148 | +2.36% | +1.22% | 1.27x | 11.5 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 6 | CC/USD | 0.08368 | 43.400 | 45.975 | +1.89% | +0.36% | 0.56x | 4.8 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06058 | 38.213 | 36.086 | +1.08% | +0.85% | 0.79x | 9.9 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8305 | 34.094 | 34.468 | +1.10% | +0.26% | 0.83x | 17.0 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | ICNT/USD | 0.2799 | 26.832 | 32.954 | +1.38% | -1.06% | 0.92x | 17.9 | 2026-11-18T03:40:03.172897+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 83/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 56.428 | 2.167 | +0.04% | 1.52x |
| 2 | XMR/USD | 49.395 | 510.29 | -0.54% | 5.41x |
| 3 | CC/USD | 45.975 | 0.08368 | +0.36% | 0.56x |
| 4 | AKT/USD | 43.148 | 0.5213 | +1.22% | 1.27x |
| 5 | SENT/USD | 41.816 | 0.019003 | +1.28% | 2.74x |
| 6 | TON/USD | 38.908 | 1.084 | +0.65% | 2.26x |
| 7 | ZAMA/USD | 36.086 | 0.06058 | +0.85% | 0.79x |
| 8 | PEARL/USD | 34.468 | 1.8305 | +0.26% | 0.83x |
| 9 | ICNT/USD | 32.954 | 0.2799 | -1.06% | 0.92x |

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

- Persisted scans: 521; predictions: 4406; observations: 314296.
- Matured sampled outcomes across 1/6/24/48h: 3520; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44231962156 · **Generation:** 521 · **Legacy run:** 44231962156
**Main quote time:** 2026-11-18T03:40:07.972323+00:00 · **Legacy report time:** 2026-11-18T03:40:27.313783+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019003 | 63.24 | +1.28% | 2.74x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 2 | PIEVERSE/USD | 2.167 | 61.85 | +0.04% | 1.52x | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 3 | XMR/USD | 510.29 | 61.72 | -0.54% | 5.41x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 4 | TON/USD ⭐ | 1.084 | 54.81 | +0.65% | 2.26x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 5 | AKT/USD ⭐ | 0.5213 | 52.01 | +1.22% | 1.27x | MODERATE 66/100 | HIGH 66/100 | Watch |
| 6 | CC/USD | 0.08368 | 43.40 | +0.36% | 0.56x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 7 | ZAMA/USD | 0.06058 | 38.21 | +0.85% | 0.79x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 8 | PEARL/USD | 1.8305 | 34.09 | +0.26% | 0.83x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 9 | ICNT/USD | 0.2799 | 26.83 | -1.06% | 0.92x | WEAK 13/100 | VERY_HIGH 83/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.018968 | 55.94 | +1.28% | 2.74x | 3857 | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5206 | 54.84 | +1.22% | 1.27x | 3945 | STRONG 72/100 | HIGH 60/100 | Watch |
| 3 | TON/USD ⭐ | 1.084 | 42.19 | +0.65% | 2.26x | 5384 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SENT/USD, TON/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
