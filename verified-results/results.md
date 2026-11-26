# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T19:01:21.854496+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45880204584
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 773d7b8ecabbc4010ecf80b6a4a0e3ad7de32b5c (atomic ledger/results publication)
**Ledger generation:** 1900 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.108 | 95.455 | 72.642 | +8.20% | +1.56% | 3.92x | 18.0 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | STRONG 98/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.150103 | 88.898 | 73.541 | +2.97% | +0.07% | 4.29x | 4.5 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5059 | 86.571 | 72.162 | +6.93% | -0.12% | 27.52x | 11.9 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | FET/USD | 0.1193 | 80.919 | 65.919 | +9.95% | +0.00% | 2.77x | 25.1 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04563 | 74.038 | 72.115 | +8.95% | +0.20% | 1.09x | 15.4 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | LTC/USD | 43.32 | 64.205 | 63.843 | +1.43% | -0.05% | 1.06x | 2.3 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 7 | LINK/USD | 9.25685 | 62.476 | 68.845 | +2.35% | +0.19% | 0.27x | 4.3 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95201 | 58.161 | 66.338 | +1.65% | -0.03% | 0.20x | 0.4 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SOL/USD | 71.18 | 58.115 | 62.154 | +1.12% | -0.01% | 0.60x | 1.4 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ETH/USD | 1697.32 | 53.545 | 57.832 | +0.41% | -0.11% | 0.62x | 0.1 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.67 | 51.833 | 57.524 | +0.56% | +0.24% | 0.31x | 1.5 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AVAX/USD | 6.649 | 40.035 | 41.154 | +0.42% | +0.20% | 0.79x | 4.5 | 2026-11-26T19:01:15.079106+00:00 | Not calibrated | WEAK 40/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ADA/USD | 73.541 | 0.150103 | +0.07% | 4.29x |
| 2 | ZRO/USD | 72.642 | 1.108 | +1.56% | 3.92x |
| 3 | AKT/USD | 72.162 | 0.5059 | -0.12% | 27.52x |
| 4 | SKY/USD | 72.115 | 0.04563 | +0.20% | 1.09x |
| 5 | LINK/USD | 68.845 | 9.25685 | +0.19% | 0.27x |
| 6 | XRP/USD | 66.338 | 0.95201 | -0.03% | 0.20x |
| 7 | FET/USD | 65.919 | 0.1193 | +0.00% | 2.77x |
| 8 | LTC/USD | 63.843 | 43.32 | -0.05% | 1.06x |
| 9 | SOL/USD | 62.154 | 71.18 | -0.01% | 0.60x |
| 10 | ETH/USD | 57.832 | 1697.32 | -0.11% | 0.62x |
| 11 | SUI/USD | 57.524 | 0.67 | +0.24% | 0.31x |
| 12 | AVAX/USD | 41.154 | 6.649 | +0.20% | 0.79x |

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

- Persisted scans: 1900; predictions: 16535; observations: 1151041.
- Matured sampled outcomes across 1/6/24/48h: 35828; gap abstentions: 25163. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45880204584 · **Generation:** 1900 · **Legacy run:** 45880204584
**Main quote time:** 2026-11-26T19:01:21.854496+00:00 · **Legacy report time:** 2026-11-26T19:02:12.363895+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD | 1.108 | 95.45 | +1.56% | 3.92x | STRONG 98/100 | HIGH 66/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.150103 | 88.90 | +0.07% | 4.29x | STRONG 99/100 | HIGH 55/100 | Watch |
| 3 | AKT/USD | 0.5059 | 86.57 | -0.12% | 27.52x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 4 | FET/USD | 0.1193 | 80.92 | +0.00% | 2.77x | STRONG 75/100 | VERY_HIGH 72/100 | Watch |
| 5 | SKY/USD ⭐ | 0.04563 | 74.04 | +0.20% | 1.09x | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |
| 6 | LTC/USD | 43.32 | 64.20 | -0.05% | 1.06x | WEAK 42/100 | HIGH 68/100 | Watch |
| 7 | LINK/USD | 9.25685 | 62.48 | +0.19% | 0.27x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.95201 | 58.16 | -0.03% | 0.20x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SOL/USD | 71.18 | 58.11 | -0.01% | 0.60x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ETH/USD | 1697.32 | 53.55 | -0.11% | 0.62x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SUI/USD | 0.67 | 51.83 | +0.24% | 0.31x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | AVAX/USD | 6.649 | 40.04 | +0.20% | 0.79x | WEAK 40/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.150267 | 92.31 | +0.07% | 4.29x | 10568 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04563 | 73.84 | +0.20% | 1.09x | 6586 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ADA/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
