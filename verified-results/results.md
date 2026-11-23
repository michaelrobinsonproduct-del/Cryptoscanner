# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T01:31:26.773342+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45094858271
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** de137700fbbee123091d5f16d59186a7e8ad3f54 (atomic ledger/results publication)
**Ledger generation:** 1362 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38852 | 72.261 | 76.480 | +5.33% | +0.18% | 0.49x | 12.1 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.016738 | 65.370 | 47.592 | +4.01% | +2.60% | 1.48x | 37.7 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PAXG/USD | 3603.71 | 63.399 | 48.736 | +0.88% | -0.07% | 12.95x | 3.4 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3585 | 45.658 | 34.376 | +1.79% | -0.74% | 4.05x | 22.3 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 5 | XAUT/USD | 3601.4 | 44.957 | 38.181 | +0.82% | +0.00% | 1.68x | 0.8 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | MODERATE 57/100 | HIGH 60/100 | Watch | WATCH |
| 6 | PEARL/USD | 2.1037 | 41.322 | 49.184 | +2.40% | -0.03% | 0.23x | 18.1 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | CPOOL/USD | 0.02272 | 17.220 | 35.922 | +1.75% | -2.88% | 0.57x | 17.6 | 2026-11-23T01:31:22.305151+00:00 | Not calibrated | WEAK 9/100 | EXTREME 91/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 76.480 | 0.38852 | +0.18% | 0.49x |
| 2 | PEARL/USD | 49.184 | 2.1037 | -0.03% | 0.23x |
| 3 | PAXG/USD | 48.736 | 3603.71 | -0.07% | 12.95x |
| 4 | BLESS/USD | 47.592 | 0.016738 | +2.60% | 1.48x |
| 5 | XAUT/USD | 38.181 | 3601.4 | +0.00% | 1.68x |
| 6 | CPOOL/USD | 35.922 | 0.02272 | -2.88% | 0.57x |
| 7 | ICNT/USD | 34.376 | 0.3585 | -0.74% | 4.05x |

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

- Persisted scans: 1362; predictions: 11179; observations: 824564.
- Matured sampled outcomes across 1/6/24/48h: 17697; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 74 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45094858271 · **Generation:** 1362 · **Legacy run:** 45094858271
**Main quote time:** 2026-11-23T01:31:26.773342+00:00 · **Legacy report time:** 2026-11-23T01:32:26.359964+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38852 | 72.26 | +0.18% | 0.49x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | BLESS/USD ⭐ | 0.016738 | 65.37 | +2.60% | 1.48x | STRONG 73/100 | HIGH 67/100 | Watch |
| 3 | PAXG/USD | 3603.71 | 63.40 | -0.07% | 12.95x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 4 | ICNT/USD | 0.3585 | 45.66 | -0.74% | 4.05x | WEAK 43/100 | VERY_HIGH 78/100 | Watch |
| 5 | XAUT/USD | 3601.4 | 44.96 | +0.00% | 1.68x | MODERATE 57/100 | HIGH 60/100 | Watch |
| 6 | PEARL/USD | 2.1037 | 41.32 | -0.03% | 0.23x | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | CPOOL/USD | 0.02272 | 17.22 | -2.88% | 0.57x | WEAK 9/100 | EXTREME 91/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.016738 | 84.74 | +2.60% | 1.48x | 5430 | STRONG 87/100 | HIGH 67/100 | Watch |

**Same-run overlap:** BLESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
