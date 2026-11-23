# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T14:51:42.268469+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45198359710
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ac8bbe2151f7765eebf8612f591d48beea0cc138 (atomic ledger/results publication)
**Ledger generation:** 1444 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 67.53 | 96.472 | 97.779 | +7.09% | -1.02% | 1.38x | 4.4 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Watch | WATCH |
| 2 | SOL/USD | 76.45 | 95.733 | 99.346 | +8.24% | -0.85% | 1.07x | 1.3 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98888 | 93.640 | 98.584 | +6.61% | -1.45% | 1.23x | 2.8 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 4 | ZEC/USD | 860.61 | 90.101 | 96.047 | +7.91% | -1.14% | 0.97x | 7.9 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | LTC/USD | 43.07 | 90.070 | 94.178 | +7.25% | -0.39% | 0.79x | 4.7 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0588226 | 87.022 | 98.448 | +6.40% | -0.75% | 0.23x | 2.7 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.1691 | 86.632 | 95.682 | +6.29% | -1.24% | 0.72x | 6.6 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | SUI/USD | 0.7119 | 86.474 | 98.595 | +8.57% | -1.35% | 0.46x | 2.8 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | XLM/USD | 0.134547 | 81.801 | 90.106 | +5.50% | -0.73% | 0.54x | 6.8 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ADA/USD | 0.153226 | 81.039 | 92.826 | +5.96% | -0.82% | 0.23x | 7.8 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | LINK/USD | 9.30796 | 81.013 | 86.998 | +5.64% | -0.74% | 0.77x | 2.8 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 12 | INJ/USD | 6.859 | 80.464 | 89.482 | +10.13% | -0.59% | 0.39x | 8.7 | 2026-11-23T14:51:35.661539+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 99.346 | 76.45 | -0.85% | 1.07x |
| 2 | SUI/USD | 98.595 | 0.7119 | -1.35% | 0.46x |
| 3 | XRP/USD | 98.584 | 0.98888 | -1.45% | 1.23x |
| 4 | XDG/USD | 98.448 | 0.0588226 | -0.75% | 0.23x |
| 5 | HYPE/USD | 97.779 | 67.53 | -1.02% | 1.38x |
| 6 | ZEC/USD | 96.047 | 860.61 | -1.14% | 0.97x |
| 7 | NEAR/USD | 95.682 | 3.1691 | -1.24% | 0.72x |
| 8 | LTC/USD | 94.178 | 43.07 | -0.39% | 0.79x |
| 9 | ADA/USD | 92.826 | 0.153226 | -0.82% | 0.23x |
| 10 | XLM/USD | 90.106 | 0.134547 | -0.73% | 0.54x |
| 11 | INJ/USD | 89.482 | 6.859 | -0.59% | 0.39x |
| 12 | LINK/USD | 86.998 | 9.30796 | -0.74% | 0.77x |

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

- Persisted scans: 1444; predictions: 12095; observations: 874498.
- Matured sampled outcomes across 1/6/24/48h: 20620; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45198359710 · **Generation:** 1444 · **Legacy run:** 45198359710
**Main quote time:** 2026-11-23T14:51:42.268469+00:00 · **Legacy report time:** 2026-11-23T14:52:49.073157+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 67.53 | 96.47 | -1.02% | 1.38x | MODERATE 68/100 | HIGH 65/100 | Watch |
| 2 | SOL/USD | 76.45 | 95.73 | -0.85% | 1.07x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 3 | XRP/USD | 0.98888 | 93.64 | -1.45% | 1.23x | MODERATE 57/100 | VERY_HIGH 72/100 | Do nothing |
| 4 | ZEC/USD | 860.61 | 90.10 | -1.14% | 0.97x | MODERATE 50/100 | VERY_HIGH 72/100 | Watch |
| 5 | LTC/USD | 43.07 | 90.07 | -0.39% | 0.79x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 6 | XDG/USD | 0.0588226 | 87.02 | -0.75% | 0.23x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 7 | NEAR/USD | 3.1691 | 86.63 | -1.24% | 0.72x | MODERATE 48/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | SUI/USD | 0.7119 | 86.47 | -1.35% | 0.46x | MODERATE 48/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | XLM/USD | 0.134547 | 81.80 | -0.73% | 0.54x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 10 | ADA/USD | 0.153226 | 81.04 | -0.82% | 0.23x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 11 | LINK/USD | 9.30796 | 81.01 | -0.74% | 0.77x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 12 | INJ/USD | 6.859 | 80.46 | -0.59% | 0.39x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
