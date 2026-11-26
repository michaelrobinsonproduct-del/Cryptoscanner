# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T14:11:38.288985+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45836171376
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** adc4d0e4d52eeb4ada65b7b641d578752f2baff6 (atomic ledger/results publication)
**Ledger generation:** 1871 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 589; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.111 | 85.088 | 80.295 | +8.50% | +0.00% | 1.48x | 9.0 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 2 | FET/USD | 0.1155 | 83.040 | 69.772 | +6.45% | -0.35% | 4.05x | 17.3 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | 2Z/USD | 0.01758 | 76.123 | 73.268 | +6.42% | +1.56% | 0.51x | 5.7 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6682 | 72.373 | 56.248 | +0.29% | +0.23% | 4.71x | 1.5 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | INJ/USD | 6.196 | 71.674 | 69.615 | +4.06% | +0.10% | 1.16x | 3.2 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04675 | 71.582 | 76.570 | +11.63% | -1.31% | 1.16x | 6.4 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 7 | LTC/USD | 43.82 | 70.904 | 72.051 | +2.60% | +0.32% | 0.73x | 2.3 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | QNT/USD | 150.89 | 68.897 | 74.239 | +4.21% | -0.37% | 0.65x | 5.3 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ADA/USD | 0.149269 | 68.822 | 70.496 | +2.40% | +0.24% | 0.71x | 2.6 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.25383 | 65.090 | 68.874 | +2.31% | +0.13% | 0.56x | 3.3 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0569247 | 62.511 | 60.785 | +1.73% | +0.04% | 1.15x | 0.5 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.95172 | 62.064 | 66.278 | +1.62% | +0.13% | 0.51x | 0.1 | 2026-11-26T14:11:30.227050+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 80.295 | 1.111 | +0.00% | 1.48x |
| 2 | SKY/USD | 76.570 | 0.04675 | -1.31% | 1.16x |
| 3 | QNT/USD | 74.239 | 150.89 | -0.37% | 0.65x |
| 4 | 2Z/USD | 73.268 | 0.01758 | +1.56% | 0.51x |
| 5 | LTC/USD | 72.051 | 43.82 | +0.32% | 0.73x |
| 6 | ADA/USD | 70.496 | 0.149269 | +0.24% | 0.71x |
| 7 | FET/USD | 69.772 | 0.1155 | -0.35% | 4.05x |
| 8 | INJ/USD | 69.615 | 6.196 | +0.10% | 1.16x |
| 9 | LINK/USD | 68.874 | 9.25383 | +0.13% | 0.56x |
| 10 | XRP/USD | 66.278 | 0.95172 | +0.13% | 0.51x |
| 11 | XDG/USD | 60.785 | 0.0569247 | +0.04% | 1.15x |
| 12 | SUI/USD | 56.248 | 0.6682 | +0.23% | 4.71x |

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

- Persisted scans: 1871; predictions: 16187; observations: 1133832.
- Matured sampled outcomes across 1/6/24/48h: 35018; gap abstentions: 24888. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45836171376 · **Generation:** 1871 · **Legacy run:** 45836171376
**Main quote time:** 2026-11-26T14:11:38.288985+00:00 · **Legacy report time:** 2026-11-26T14:12:59.506364+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD | 1.111 | 85.09 | +0.00% | 1.48x | STRONG 78/100 | HIGH 55/100 | Watch |
| 2 | FET/USD | 0.1155 | 83.04 | -0.35% | 4.05x | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 3 | 2Z/USD | 0.01758 | 76.12 | +1.56% | 0.51x | MODERATE 68/100 | VERY_HIGH 82/100 | Watch |
| 4 | SUI/USD | 0.6682 | 72.37 | +0.23% | 4.71x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 5 | INJ/USD ⭐ | 6.196 | 71.67 | +0.10% | 1.16x | STRONG 71/100 | HIGH 62/100 | Watch |
| 6 | SKY/USD | 0.04675 | 71.58 | -1.31% | 1.16x | MODERATE 46/100 | VERY_HIGH 77/100 | Do nothing |
| 7 | LTC/USD | 43.82 | 70.90 | +0.32% | 0.73x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | QNT/USD | 150.89 | 68.90 | -0.37% | 0.65x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | ADA/USD | 0.149269 | 68.82 | +0.24% | 0.71x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.25383 | 65.09 | +0.13% | 0.56x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0569247 | 62.51 | +0.04% | 1.15x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.95172 | 62.06 | +0.13% | 0.51x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.196 | 87.13 | +0.10% | 1.16x | 6910 | STRONG 79/100 | HIGH 62/100 | Watch |
| 2 | SEI/USD | 0.03753 | 84.49 | +1.49% | 3.62x | 4015 | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 3 | PIEVERSE/USD | 4.016 | 78.57 | +0.11% | 1.40x | 3543 | MODERATE 59/100 | HIGH 67/100 | Watch |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
