# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T08:50:42.888324+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44705623155
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 57036e8e4404729373159044d107de4b337b9911 (atomic ledger/results publication)
**Ledger generation:** 956 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4444 | 79.731 | 61.212 | +4.29% | +0.70% | 3.56x | 15.7 | 2026-11-20T08:50:37.526117+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | PROS/USD | 0.5813 | 62.200 | 65.528 | +7.91% | -0.22% | 0.78x | 20.6 | 2026-11-20T08:50:37.526117+00:00 | Not calibrated | WEAK 26/100 | EXTREME 92/100 | Do nothing | WATCH |
| 3 | XLM/USD | 0.133652 | 51.821 | 59.161 | +0.72% | -0.35% | 0.44x | 1.7 | 2026-11-20T08:50:37.526117+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | SKR/USD | 0.010376 | 51.559 | 49.606 | +3.28% | -2.61% | 3.47x | 9.6 | 2026-11-20T08:50:37.526117+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | ATOM/USD | 1.2655 | 30.060 | 31.337 | +0.32% | -0.59% | 1.17x | 7.1 | 2026-11-20T08:50:37.526117+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | TON/USD | 1.023 | 23.938 | 32.355 | +0.59% | +0.20% | 0.06x | 9.8 | 2026-11-20T08:50:37.526117+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 65.528 | 0.5813 | -0.22% | 0.78x |
| 2 | ICNT/USD | 61.212 | 0.4444 | +0.70% | 3.56x |
| 3 | XLM/USD | 59.161 | 0.133652 | -0.35% | 0.44x |
| 4 | SKR/USD | 49.606 | 0.010376 | -2.61% | 3.47x |
| 5 | TON/USD | 32.355 | 1.023 | +0.20% | 0.06x |
| 6 | ATOM/USD | 31.337 | 1.2655 | -0.59% | 1.17x |

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

- Persisted scans: 956; predictions: 8122; observations: 577655.
- Matured sampled outcomes across 1/6/24/48h: 9647; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44705623155 · **Generation:** 956 · **Legacy run:** 44705623155
**Main quote time:** 2026-11-20T08:50:42.888324+00:00 · **Legacy report time:** 2026-11-20T08:51:47.795612+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4444 | 79.73 | +0.70% | 3.56x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | PROS/USD | 0.5813 | 62.20 | -0.22% | 0.78x | WEAK 26/100 | EXTREME 92/100 | Do nothing |
| 3 | XLM/USD | 0.133652 | 51.82 | -0.35% | 0.44x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | SKR/USD | 0.010376 | 51.56 | -2.61% | 3.47x | MODERATE 56/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | ATOM/USD | 1.2655 | 30.06 | -0.59% | 1.17x | WEAK 25/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | TON/USD | 1.023 | 23.94 | +0.20% | 0.06x | WEAK 32/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4494 | 85.57 | +0.70% | 3.56x | 7975 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
