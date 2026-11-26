# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T03:25:51.694011+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45748717418
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 685276e7bf6183b5606c4f7424bb8e082253896b (atomic ledger/results publication)
**Ledger generation:** 1806 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.14848 | 75.913 | 66.767 | +1.86% | +0.38% | 1.72x | 2.5 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SYRUP/USD | 0.07052 | 74.892 | 64.184 | +6.41% | -0.86% | 3.11x | 25.5 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 3 | HYPE/USD | 61.87 | 72.841 | 57.031 | +0.41% | +0.16% | 2.71x | 1.6 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | TIA/USD | 0.3493 | 70.469 | 57.039 | +3.80% | -0.31% | 5.18x | 2.9 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 65/100 | HIGH 66/100 | Watch | WATCH |
| 5 | XBT/USD | 60678.2 | 67.576 | 58.582 | +0.51% | +0.13% | 1.83x | 0.0 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95778 | 67.565 | 70.808 | +2.27% | +0.35% | 0.50x | 0.1 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1695.3 | 67.470 | 56.995 | +0.29% | +0.05% | 2.02x | 0.1 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 8 | TAO/USD | 184.5925 | 65.808 | 63.716 | +1.65% | +0.12% | 1.15x | 5.7 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LTC/USD | 43.6 | 63.846 | 68.440 | +2.08% | +0.32% | 0.38x | 2.3 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 71.08 | 58.776 | 61.158 | +0.98% | +0.04% | 0.74x | 1.4 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PEPE/USD | 3.552e-06 | 57.713 | 57.516 | +1.95% | +0.60% | 0.72x | 2.8 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6736 | 57.639 | 61.185 | +1.10% | +0.33% | 0.48x | 3.0 | 2026-11-26T03:25:43.929969+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 70.808 | 0.95778 | +0.35% | 0.50x |
| 2 | LTC/USD | 68.440 | 43.6 | +0.32% | 0.38x |
| 3 | ADA/USD | 66.767 | 0.14848 | +0.38% | 1.72x |
| 4 | SYRUP/USD | 64.184 | 0.07052 | -0.86% | 3.11x |
| 5 | TAO/USD | 63.716 | 184.5925 | +0.12% | 1.15x |
| 6 | SUI/USD | 61.185 | 0.6736 | +0.33% | 0.48x |
| 7 | SOL/USD | 61.158 | 71.08 | +0.04% | 0.74x |
| 8 | XBT/USD | 58.582 | 60678.2 | +0.13% | 1.83x |
| 9 | PEPE/USD | 57.516 | 3.552e-06 | +0.60% | 0.72x |
| 10 | TIA/USD | 57.039 | 0.3493 | -0.31% | 5.18x |
| 11 | HYPE/USD | 57.031 | 61.87 | +0.16% | 2.71x |
| 12 | ETH/USD | 56.995 | 1695.3 | +0.05% | 2.02x |

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

- Persisted scans: 1806; predictions: 15407; observations: 1094898.
- Matured sampled outcomes across 1/6/24/48h: 33443; gap abstentions: 23775. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45748717418 · **Generation:** 1806 · **Legacy run:** 45748717418
**Main quote time:** 2026-11-26T03:25:51.694011+00:00 · **Legacy report time:** 2026-11-26T03:26:42.353193+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.14848 | 75.91 | +0.38% | 1.72x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | SYRUP/USD | 0.07052 | 74.89 | -0.86% | 3.11x | MODERATE 57/100 | VERY_HIGH 78/100 | Watch |
| 3 | HYPE/USD | 61.87 | 72.84 | +0.16% | 2.71x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | TIA/USD | 0.3493 | 70.47 | -0.31% | 5.18x | MODERATE 65/100 | HIGH 66/100 | Watch |
| 5 | XBT/USD | 60678.2 | 67.58 | +0.13% | 1.83x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD | 0.95778 | 67.57 | +0.35% | 0.50x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1695.3 | 67.47 | +0.05% | 2.02x | STRONG 79/100 | HIGH 55/100 | Watch |
| 8 | TAO/USD ⭐ | 184.5925 | 65.81 | +0.12% | 1.15x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 9 | LTC/USD | 43.6 | 63.85 | +0.32% | 0.38x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 71.08 | 58.78 | +0.04% | 0.74x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | PEPE/USD | 3.552e-06 | 57.71 | +0.60% | 0.72x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6736 | 57.64 | +0.33% | 0.48x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.148686 | 71.84 | +0.38% | 1.72x | 11303 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 184.5925 | 62.49 | +0.12% | 1.15x | 9338 | MODERATE 66/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ADA/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
