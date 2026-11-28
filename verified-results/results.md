# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T06:47:29.183887+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46118009158
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4f97c616b02aa8b920b0e104afc370a17c48eb24 (atomic ledger/results publication)
**Ledger generation:** 2119 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 431.22 | 94.357 | 92.106 | +5.88% | +0.05% | 1.20x | 8.1 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.73 | 72.572 | 56.077 | +0.38% | +0.30% | 2.71x | 3.1 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 26.272 | 52.006 | 55.035 | +2.03% | +0.20% | 0.60x | 8.8 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEC/USD | 740.42 | 51.336 | 58.547 | +0.80% | -0.19% | 0.38x | 4.1 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | CFG/USD | 0.0616 | 47.714 | 61.746 | +9.22% | -2.53% | 0.86x | 32.4 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | WEAK 19/100 | EXTREME 89/100 | Do nothing | WATCH |
| 6 | NEAR/USD | 3.0339 | 47.550 | 56.993 | +0.52% | -0.00% | 0.06x | 3.3 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | SHX/USD | 0.003369 | 39.839 | 17.307 | +0.63% | +1.51% | 10.89x | 35.6 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | SPACE/USD | 0.004231 | 17.826 | 33.709 | +1.27% | -1.37% | 0.10x | 11.8 | 2026-11-28T06:47:24.448658+00:00 | Not calibrated | WEAK 9/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 92.106 | 431.22 | +0.05% | 1.20x |
| 2 | CFG/USD | 61.746 | 0.0616 | -2.53% | 0.86x |
| 3 | ZEC/USD | 58.547 | 740.42 | -0.19% | 0.38x |
| 4 | NEAR/USD | 56.993 | 3.0339 | -0.00% | 0.06x |
| 5 | HYPE/USD | 56.077 | 63.73 | +0.30% | 2.71x |
| 6 | VVV/USD | 55.035 | 26.272 | +0.20% | 0.60x |
| 7 | SPACE/USD | 33.709 | 0.004231 | -1.37% | 0.10x |
| 8 | SHX/USD | 17.307 | 0.003369 | +1.51% | 10.89x |

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

- Persisted scans: 2119; predictions: 18996; observations: 1283160.
- Matured sampled outcomes across 1/6/24/48h: 44494; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46118009158 · **Generation:** 2119 · **Legacy run:** 46118009158
**Main quote time:** 2026-11-28T06:47:29.183887+00:00 · **Legacy report time:** 2026-11-28T06:48:07.466758+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 431.22 | 94.36 | +0.05% | 1.20x | STRONG 82/100 | HIGH 62/100 | Watch |
| 2 | HYPE/USD ⭐ | 63.73 | 72.57 | +0.30% | 2.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 26.272 | 52.01 | +0.20% | 0.60x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEC/USD | 740.42 | 51.34 | -0.19% | 0.38x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | CFG/USD | 0.0616 | 47.71 | -2.53% | 0.86x | WEAK 19/100 | EXTREME 89/100 | Do nothing |
| 6 | NEAR/USD | 3.0339 | 47.55 | -0.00% | 0.06x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | SHX/USD ⭐ | 0.003369 | 39.84 | +1.51% | 10.89x | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 8 | SPACE/USD | 0.004231 | 17.83 | -1.37% | 0.10x | WEAK 9/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 431.22 | 85.95 | +0.05% | 1.20x | 14918 | STRONG 73/100 | HIGH 68/100 | Watch |
| 2 | HYPE/USD ⭐ | 63.73 | 57.99 | +0.30% | 2.71x | 17275 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 3 | SHX/USD ⭐ | 0.003369 | 32.24 | +1.51% | 10.89x | 1411 | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 4 | SEI/USD | 0.03847 | 27.03 | +0.42% | 1.10x | 3833 | WEAK 44/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** XMR/USD, HYPE/USD, SHX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
