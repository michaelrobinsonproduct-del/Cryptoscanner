# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:00:24.706531+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44529041173
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** c4f42485bd77f6921b451b97be93b4e0738a1414 (atomic ledger/results publication)
**Ledger generation:** 777 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.906 | 96.333 | 93.361 | +5.70% | +0.72% | 0.94x | 3.1 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 2 | PEPE/USD | 4.009e-06 | 93.520 | 78.022 | +7.02% | +0.10% | 4.07x | 15.0 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 87/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 68.86 | 79.956 | 74.271 | +2.96% | +1.06% | 1.04x | 2.9 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XRP/USD | 0.9891 | 76.624 | 71.414 | +2.35% | +0.81% | 1.11x | 0.1 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ZEC/USD | 949.38 | 75.736 | 82.413 | +4.10% | +0.50% | 0.08x | 2.6 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.4038 | 75.120 | 75.529 | +3.23% | +0.65% | 0.63x | 4.1 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XLM/USD | 0.138131 | 68.061 | 59.460 | +0.68% | +0.70% | 1.51x | 0.7 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SENT/USD | 0.022024 | 67.517 | 74.419 | +6.89% | -0.00% | 0.31x | 7.7 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | ETH/USD | 1805 | 65.843 | 66.900 | +1.70% | +0.42% | 0.68x | 0.1 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ONDO/USD | 0.3061 | 63.378 | 54.519 | +2.84% | +0.51% | 1.63x | 0.3 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 11 | XBT/USD | 63813.6 | 60.380 | 64.207 | +1.32% | +0.13% | 0.55x | 0.0 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | BCH/USD | 209.19 | 52.679 | 35.060 | +0.47% | +0.52% | 2.85x | 5.7 | 2026-11-19T13:00:16.431594+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 93.361 | 22.906 | +0.72% | 0.94x |
| 2 | ZEC/USD | 82.413 | 949.38 | +0.50% | 0.08x |
| 3 | PEPE/USD | 78.022 | 4.009e-06 | +0.10% | 4.07x |
| 4 | NEAR/USD | 75.529 | 3.4038 | +0.65% | 0.63x |
| 5 | SENT/USD | 74.419 | 0.022024 | -0.00% | 0.31x |
| 6 | HYPE/USD | 74.271 | 68.86 | +1.06% | 1.04x |
| 7 | XRP/USD | 71.414 | 0.9891 | +0.81% | 1.11x |
| 8 | ETH/USD | 66.900 | 1805 | +0.42% | 0.68x |
| 9 | XBT/USD | 64.207 | 63813.6 | +0.13% | 0.55x |
| 10 | XLM/USD | 59.460 | 0.138131 | +0.70% | 1.51x |
| 11 | ONDO/USD | 54.519 | 0.3061 | +0.51% | 1.63x |
| 12 | BCH/USD | 35.060 | 209.19 | +0.52% | 2.85x |

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

- Persisted scans: 777; predictions: 6468; observations: 470182.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14916. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44529041173 · **Generation:** 777 · **Legacy run:** 44529041173
**Main quote time:** 2026-11-19T13:00:24.706531+00:00 · **Legacy report time:** 2026-11-19T13:01:09.061448+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.906 | 96.33 | +0.72% | 0.94x | STRONG 78/100 | HIGH 62/100 | Watch |
| 2 | PEPE/USD ⭐ | 4.009e-06 | 93.52 | +0.10% | 4.07x | STRONG 97/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD ⭐ | 68.86 | 79.96 | +1.06% | 1.04x | STRONG 85/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.9891 | 76.62 | +0.81% | 1.11x | STRONG 83/100 | HIGH 62/100 | Watch |
| 5 | ZEC/USD | 949.38 | 75.74 | +0.50% | 0.08x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 6 | NEAR/USD | 3.4038 | 75.12 | +0.65% | 0.63x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 7 | XLM/USD | 0.138131 | 68.06 | +0.70% | 1.51x | STRONG 79/100 | HIGH 55/100 | Watch |
| 8 | SENT/USD | 0.022024 | 67.52 | -0.00% | 0.31x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 9 | ETH/USD | 1805 | 65.84 | +0.42% | 0.68x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | ONDO/USD | 0.3061 | 63.38 | +0.51% | 1.63x | STRONG 77/100 | HIGH 60/100 | Watch |
| 11 | XBT/USD | 63813.6 | 60.38 | +0.13% | 0.55x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | BCH/USD | 209.19 | 52.68 | +0.52% | 2.85x | STRONG 81/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.01 | 87.75 | +1.06% | 1.04x | 14627 | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | PEPE/USD ⭐ | 4.002e-06 | 84.61 | +0.10% | 4.07x | 3898 | STRONG 97/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.98978 | 83.76 | +0.81% | 1.11x | 34324 | STRONG 87/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEPE/USD, HYPE/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
