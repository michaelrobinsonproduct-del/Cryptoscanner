# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T05:17:21.740032+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45552192809
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a3ebb6142fcb3c91de32b3378df0c8d5492a9fc3 (atomic ledger/results publication)
**Ledger generation:** 1674 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.018 | 66.515 | 65.695 | +1.96% | -0.12% | 1.14x | 6.0 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 2 | MON/USD | 0.00979 | 58.728 | 66.579 | +3.38% | -0.81% | 0.62x | 10.2 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | XMR/USD | 512.75 | 57.199 | 55.564 | +0.62% | +0.06% | 1.13x | 4.9 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 4 | DRV/USD | 0.32849 | 50.229 | 63.319 | +4.52% | -0.86% | 0.12x | 10.0 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | BLESS/USD | 0.017756 | 43.530 | 26.482 | +0.94% | +1.01% | 2.20x | 34.4 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 6 | CT/USD | 0.1284 | 40.689 | 30.765 | +1.66% | +0.31% | 1.84x | 23.5 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | CAP/USD | 0.092785 | 25.550 | 32.878 | +0.40% | -0.70% | 0.62x | 4.3 | 2026-11-25T05:17:15.368985+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 66.579 | 0.00979 | -0.81% | 0.62x |
| 2 | VVV/USD | 65.695 | 25.018 | -0.12% | 1.14x |
| 3 | DRV/USD | 63.319 | 0.32849 | -0.86% | 0.12x |
| 4 | XMR/USD | 55.564 | 512.75 | +0.06% | 1.13x |
| 5 | CAP/USD | 32.878 | 0.092785 | -0.70% | 0.62x |
| 6 | CT/USD | 30.765 | 0.1284 | +0.31% | 1.84x |
| 7 | BLESS/USD | 26.482 | 0.017756 | +1.01% | 2.20x |

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

- Persisted scans: 1674; predictions: 14217; observations: 1014557.
- Matured sampled outcomes across 1/6/24/48h: 30139; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45552192809 · **Generation:** 1674 · **Legacy run:** 45552192809
**Main quote time:** 2026-11-25T05:17:21.740032+00:00 · **Legacy report time:** 2026-11-25T05:18:15.785028+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.018 | 66.52 | -0.12% | 1.14x | WEAK 43/100 | HIGH 68/100 | Watch |
| 2 | MON/USD | 0.00979 | 58.73 | -0.81% | 0.62x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | XMR/USD ⭐ | 512.75 | 57.20 | +0.06% | 1.13x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 4 | DRV/USD | 0.32849 | 50.23 | -0.86% | 0.12x | WEAK 25/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | BLESS/USD ⭐ | 0.017756 | 43.53 | +1.01% | 2.20x | STRONG 77/100 | HIGH 67/100 | Consider small entry |
| 6 | CT/USD ⭐ | 0.1284 | 40.69 | +0.31% | 1.84x | MODERATE 65/100 | VERY_HIGH 79/100 | Watch |
| 7 | CAP/USD | 0.092785 | 25.55 | -0.70% | 0.62x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 512.66 | 46.26 | +0.06% | 1.13x | 6906 | MODERATE 58/100 | HIGH 62/100 | Watch |
| 2 | BLESS/USD ⭐ | 0.017756 | 45.36 | +1.01% | 2.20x | 3461 | STRONG 73/100 | HIGH 67/100 | Watch |
| 3 | CT/USD ⭐ | 0.1284 | 35.89 | +0.31% | 1.84x | 1334 | MODERATE 63/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** XMR/USD, BLESS/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
