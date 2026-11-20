# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T03:55:39.243166+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44670850824
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** c2d65a801384861bb299922411dc02de556288ff (atomic ledger/results publication)
**Ledger generation:** 919 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.96394 | 58.257 | 58.111 | +0.49% | +0.64% | 0.70x | 0.6 | 2026-11-20T03:55:34.733699+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04554 | 56.781 | 47.671 | +1.74% | +0.71% | 1.56x | 11.0 | 2026-11-20T03:55:34.733699+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XBT/USD | 62113.7 | 51.410 | 57.239 | +0.32% | +0.29% | 0.27x | 0.0 | 2026-11-20T03:55:34.733699+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | CT/USD | 0.1305 | 47.944 | 31.406 | +1.56% | +0.31% | 4.17x | 23.0 | 2026-11-20T03:55:34.733699+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.4286 | 30.186 | 33.603 | +0.59% | -0.14% | 0.73x | 16.4 | 2026-11-20T03:55:34.733699+00:00 | Not calibrated | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 58.111 | 0.96394 | +0.64% | 0.70x |
| 2 | XBT/USD | 57.239 | 62113.7 | +0.29% | 0.27x |
| 3 | NIGHT/USD | 47.671 | 0.04554 | +0.71% | 1.56x |
| 4 | ICNT/USD | 33.603 | 0.4286 | -0.14% | 0.73x |
| 5 | CT/USD | 31.406 | 0.1305 | +0.31% | 4.17x |

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

- Persisted scans: 919; predictions: 7926; observations: 555282.
- Matured sampled outcomes across 1/6/24/48h: 9076; gap abstentions: 16628. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44670850824 · **Generation:** 919 · **Legacy run:** 44670850824
**Main quote time:** 2026-11-20T03:55:39.243166+00:00 · **Legacy report time:** 2026-11-20T03:56:43.065974+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.96394 | 58.26 | +0.64% | 0.70x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04554 | 56.78 | +0.71% | 1.56x | STRONG 78/100 | HIGH 61/100 | Consider small entry |
| 3 | XBT/USD | 62113.7 | 51.41 | +0.29% | 0.27x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 4 | CT/USD ⭐ | 0.1305 | 47.94 | +0.31% | 4.17x | STRONG 79/100 | VERY_HIGH 72/100 | Watch |
| 5 | ICNT/USD | 0.4286 | 30.19 | -0.14% | 0.73x | WEAK 15/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04554 | 60.06 | +0.71% | 1.56x | 8432 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 2 | CT/USD ⭐ | 0.1308 | 53.01 | +0.31% | 4.17x | 2567 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** NIGHT/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
