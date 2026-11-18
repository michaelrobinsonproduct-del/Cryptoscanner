# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:50:04.096395+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44233098426
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** a3efcf0a4ad920a82af850b793780d1ffd72284d (atomic ledger/results publication)
**Ledger generation:** 523 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019024 | 57.320 | 40.235 | +1.90% | +0.42% | 3.54x | 7.9 | 2026-11-18T03:49:59.663601+00:00 | Not calibrated | STRONG 84/100 | HIGH 67/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5175 | 54.723 | 41.743 | +1.61% | -0.40% | 3.39x | 3.9 | 2026-11-18T03:49:59.663601+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 3 | ZAMA/USD | 0.06124 | 54.285 | 41.423 | +2.19% | +0.94% | 1.82x | 14.7 | 2026-11-18T03:49:59.663601+00:00 | Not calibrated | MODERATE 67/100 | HIGH 66/100 | Watch | WATCH |
| 4 | CC/USD | 0.08384 | 50.615 | 48.061 | +2.08% | -0.11% | 1.31x | 3.6 | 2026-11-18T03:49:59.663601+00:00 | Not calibrated | MODERATE 45/100 | HIGH 66/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.83 | 32.257 | 32.613 | +1.08% | -0.03% | 0.98x | 20.3 | 2026-11-18T03:49:59.663601+00:00 | Not calibrated | WEAK 11/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.2787 | 24.840 | 29.900 | +0.94% | +0.22% | 0.39x | 17.9 | 2026-11-18T03:49:59.663601+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CC/USD | 48.061 | 0.08384 | -0.11% | 1.31x |
| 2 | AKT/USD | 41.743 | 0.5175 | -0.40% | 3.39x |
| 3 | ZAMA/USD | 41.423 | 0.06124 | +0.94% | 1.82x |
| 4 | SENT/USD | 40.235 | 0.019024 | +0.42% | 3.54x |
| 5 | PEARL/USD | 32.613 | 1.83 | -0.03% | 0.98x |
| 6 | ICNT/USD | 29.900 | 0.2787 | +0.22% | 0.39x |

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

- Persisted scans: 523; predictions: 4420; observations: 315514.
- Matured sampled outcomes across 1/6/24/48h: 3529; gap abstentions: 12427. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44233098426 · **Generation:** 523 · **Legacy run:** 44233098426
**Main quote time:** 2026-11-18T03:50:04.096395+00:00 · **Legacy report time:** 2026-11-18T03:50:22.574175+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019024 | 57.32 | +0.42% | 3.54x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 2 | AKT/USD | 0.5175 | 54.72 | -0.40% | 3.39x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 3 | ZAMA/USD ⭐ | 0.06124 | 54.29 | +0.94% | 1.82x | STRONG 77/100 | HIGH 66/100 | Consider small entry |
| 4 | CC/USD ⭐ | 0.08384 | 50.61 | -0.11% | 1.31x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 5 | PEARL/USD | 1.83 | 32.26 | -0.03% | 0.98x | WEAK 11/100 | EXTREME 85/100 | Do nothing |
| 6 | ICNT/USD | 0.2787 | 24.84 | +0.22% | 0.39x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08384 | 58.98 | +0.20% | 1.69x | 4029 | STRONG 84/100 | HIGH 60/100 | Consider small entry |
| 2 | ZAMA/USD ⭐ | 0.06124 | 56.40 | +0.94% | 1.82x | 4482 | STRONG 78/100 | HIGH 66/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.01903 | 54.97 | +0.42% | 3.54x | 3874 | STRONG 92/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD, ZAMA/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
