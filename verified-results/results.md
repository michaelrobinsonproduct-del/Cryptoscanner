# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T01:51:07.687641+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44973250956
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 71cbd3e0fdbb8d29d3761f8af3f8b0275bec7f30 (atomic ledger/results publication)
**Ledger generation:** 1217 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 186.8566 | 58.550 | 56.810 | +0.61% | +0.51% | 0.92x | 4.9 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NEAR/USD | 2.9105 | 58.208 | 59.323 | +0.84% | +0.29% | 0.74x | 3.1 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 782.8 | 53.960 | 58.012 | +0.59% | +0.81% | 0.19x | 2.3 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.45 | 53.390 | 56.587 | +0.34% | +0.33% | 0.52x | 1.6 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | LTC/USD | 39.83 | 51.732 | 54.734 | +0.25% | +0.33% | 0.54x | 2.5 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.995 | 46.949 | 48.393 | +2.40% | +0.19% | 0.76x | 22.7 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 7 | RENDER/USD | 1.327 | 46.276 | 46.890 | +1.76% | +1.07% | 0.41x | 7.5 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | BNB/USD | 549.33 | 39.712 | 46.206 | +0.35% | +0.30% | 0.20x | 0.7 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ZRO/USD | 1.193 | 38.648 | 43.718 | +1.71% | +0.34% | 0.32x | 16.8 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | PENGU/USD | 0.004296 | 31.479 | 36.393 | +0.40% | +0.42% | 0.30x | 2.3 | 2026-11-22T01:50:58.943257+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 59.323 | 2.9105 | +0.29% | 0.74x |
| 2 | ZEC/USD | 58.012 | 782.8 | +0.81% | 0.19x |
| 3 | TAO/USD | 56.810 | 186.8566 | +0.51% | 0.92x |
| 4 | HYPE/USD | 56.587 | 61.45 | +0.33% | 0.52x |
| 5 | LTC/USD | 54.734 | 39.83 | +0.33% | 0.54x |
| 6 | PEARL/USD | 48.393 | 1.995 | +0.19% | 0.76x |
| 7 | RENDER/USD | 46.890 | 1.327 | +1.07% | 0.41x |
| 8 | BNB/USD | 46.206 | 549.33 | +0.30% | 0.20x |
| 9 | ZRO/USD | 43.718 | 1.193 | +0.34% | 0.32x |
| 10 | PENGU/USD | 36.393 | 0.004296 | +0.42% | 0.30x |

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

- Persisted scans: 1217; predictions: 9841; observations: 736294.
- Matured sampled outcomes across 1/6/24/48h: 13528; gap abstentions: 21831. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 22 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44973250956 · **Generation:** 1217 · **Legacy run:** 44973250956
**Main quote time:** 2026-11-22T01:51:07.687641+00:00 · **Legacy report time:** 2026-11-22T01:52:06.452779+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD | 186.8566 | 58.55 | +0.51% | 0.92x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 2 | NEAR/USD | 2.9105 | 58.21 | +0.29% | 0.74x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD | 782.8 | 53.96 | +0.81% | 0.19x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 4 | HYPE/USD | 61.45 | 53.39 | +0.33% | 0.52x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | LTC/USD | 39.83 | 51.73 | +0.33% | 0.54x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEARL/USD | 1.995 | 46.95 | +0.19% | 0.76x | WEAK 33/100 | VERY_HIGH 74/100 | Do nothing |
| 7 | RENDER/USD | 1.327 | 46.28 | +1.07% | 0.41x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 8 | BNB/USD | 549.33 | 39.71 | +0.30% | 0.20x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | ZRO/USD | 1.193 | 38.65 | +0.34% | 0.32x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 10 | PENGU/USD | 0.004296 | 31.48 | +0.42% | 0.30x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD | 1684.31 | 56.00 | +0.31% | 1.43x | 63175 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
