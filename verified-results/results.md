# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:45:03.513392+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44232525816
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** a9be4cf2c392d3da5745e6c58382d29e339774da (atomic ledger/results publication)
**Ledger generation:** 522 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 2.1608 | 67.531 | 62.110 | +5.48% | +0.04% | 1.52x | 16.2 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019021 | 64.020 | 41.170 | +1.89% | +1.57% | 3.39x | 5.8 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5194 | 54.187 | 45.324 | +1.98% | +1.22% | 1.27x | 1.9 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | MODERATE 62/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06097 | 41.998 | 39.871 | +1.74% | +0.85% | 0.79x | 11.5 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.08333 | 40.465 | 43.039 | +1.46% | +0.36% | 0.56x | 4.8 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | TON/USD | 1.084 | 31.499 | 34.251 | +0.65% | +0.37% | 0.54x | 18.5 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.2793 | 28.901 | 35.023 | +1.16% | -1.06% | 0.92x | 10.7 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 8 | PEARL/USD | 1.8321 | 27.625 | 29.895 | +1.19% | +0.09% | 0.73x | 27.4 | 2026-11-18T03:44:58.712329+00:00 | Not calibrated | WEAK 24/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 62.110 | 2.1608 | +0.04% | 1.52x |
| 2 | AKT/USD | 45.324 | 0.5194 | +1.22% | 1.27x |
| 3 | CC/USD | 43.039 | 0.08333 | +0.36% | 0.56x |
| 4 | SENT/USD | 41.170 | 0.019021 | +1.57% | 3.39x |
| 5 | ZAMA/USD | 39.871 | 0.06097 | +0.85% | 0.79x |
| 6 | ICNT/USD | 35.023 | 0.2793 | -1.06% | 0.92x |
| 7 | TON/USD | 34.251 | 1.084 | +0.37% | 0.54x |
| 8 | PEARL/USD | 29.895 | 1.8321 | +0.09% | 0.73x |

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

- Persisted scans: 522; predictions: 4414; observations: 314905.
- Matured sampled outcomes across 1/6/24/48h: 3520; gap abstentions: 12427. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44232525816 · **Generation:** 522 · **Legacy run:** 44232525816
**Main quote time:** 2026-11-18T03:45:03.513392+00:00 · **Legacy report time:** 2026-11-18T03:45:21.427987+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 2.1608 | 67.53 | +0.04% | 1.52x | MODERATE 64/100 | HIGH 66/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019021 | 64.02 | +1.57% | 3.39x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.5194 | 54.19 | +1.22% | 1.27x | STRONG 72/100 | HIGH 60/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.06097 | 42.00 | +0.85% | 0.79x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.08333 | 40.46 | +0.36% | 0.56x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |
| 6 | TON/USD | 1.084 | 31.50 | +0.37% | 0.54x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | ICNT/USD | 0.2793 | 28.90 | -1.06% | 0.92x | WEAK 14/100 | VERY_HIGH 83/100 | Do nothing |
| 8 | PEARL/USD | 1.8321 | 27.62 | +0.09% | 0.73x | WEAK 24/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019021 | 61.29 | +1.57% | 3.39x | 3846 | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5194 | 53.22 | +0.41% | 2.19x | 3965 | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 3 | ZAMA/USD ⭐ | 0.06097 | 50.76 | +0.96% | 1.74x | 4480 | STRONG 75/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** SENT/USD, AKT/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
