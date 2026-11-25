# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T18:15:49.324163+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45673107325
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0470e6bf3b8c94407accc4c2c26063cdc510f05f (atomic ledger/results publication)
**Ledger generation:** 1749 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.247 | 100.532 | 93.529 | +6.96% | +0.33% | 1.54x | 12.9 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.34933 | 78.493 | 73.330 | +11.15% | +1.71% | 0.66x | 21.5 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XPL/USD | 0.0478 | 66.958 | 71.109 | +8.64% | +0.21% | 0.48x | 20.9 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | HYPE/USD | 60.33 | 66.875 | 59.550 | +0.77% | +1.02% | 1.22x | 1.7 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 5 | LTC/USD | 41.78 | 64.476 | 69.740 | +2.28% | +0.19% | 0.38x | 2.4 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | LINK/USD | 8.89837 | 60.140 | 47.251 | +0.65% | +0.29% | 2.15x | 4.9 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6512 | 57.932 | 58.232 | +0.57% | +0.43% | 0.75x | 1.5 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 8 | STBL/USD | 0.018761 | 56.234 | 53.257 | +5.16% | -0.69% | 1.64x | 27.2 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | WEAK 38/100 | EXTREME 85/100 | Do nothing | WATCH |
| 9 | BCH/USD | 199.88 | 52.188 | 40.342 | +1.37% | -0.03% | 2.20x | 6.0 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 10 | XMR/USD | 511.98 | 51.068 | 52.893 | +0.47% | -0.28% | 0.96x | 10.8 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 11 | ASTER/USD | 0.4919 | 46.151 | 46.902 | +2.30% | +0.10% | 0.88x | 3.9 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |
| 12 | AAVE/USD | 94.65 | 46.057 | 42.818 | +0.80% | +0.50% | 1.07x | 5.3 | 2026-11-25T18:15:42.610841+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 93.529 | 26.247 | +0.33% | 1.54x |
| 2 | DRV/USD | 73.330 | 0.34933 | +1.71% | 0.66x |
| 3 | XPL/USD | 71.109 | 0.0478 | +0.21% | 0.48x |
| 4 | LTC/USD | 69.740 | 41.78 | +0.19% | 0.38x |
| 5 | HYPE/USD | 59.550 | 60.33 | +1.02% | 1.22x |
| 6 | SUI/USD | 58.232 | 0.6512 | +0.43% | 0.75x |
| 7 | STBL/USD | 53.257 | 0.018761 | -0.69% | 1.64x |
| 8 | XMR/USD | 52.893 | 511.98 | -0.28% | 0.96x |
| 9 | LINK/USD | 47.251 | 8.89837 | +0.29% | 2.15x |
| 10 | ASTER/USD | 46.902 | 0.4919 | +0.10% | 0.88x |
| 11 | AAVE/USD | 42.818 | 94.65 | +0.50% | 1.07x |
| 12 | BCH/USD | 40.342 | 199.88 | -0.03% | 2.20x |

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

- Persisted scans: 1749; predictions: 14732; observations: 1060185.
- Matured sampled outcomes across 1/6/24/48h: 32510; gap abstentions: 22637. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45673107325 · **Generation:** 1749 · **Legacy run:** 45673107325
**Main quote time:** 2026-11-25T18:15:49.324163+00:00 · **Legacy report time:** 2026-11-25T18:16:51.530899+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.247 | 100.53 | +0.33% | 1.54x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD | 0.34933 | 78.49 | +1.71% | 0.66x | MODERATE 59/100 | VERY_HIGH 82/100 | Watch |
| 3 | XPL/USD | 0.0478 | 66.96 | +0.21% | 0.48x | MODERATE 53/100 | EXTREME 87/100 | Do nothing |
| 4 | HYPE/USD ⭐ | 60.33 | 66.87 | +1.02% | 1.22x | STRONG 78/100 | HIGH 62/100 | Watch |
| 5 | LTC/USD | 41.78 | 64.48 | +0.19% | 0.38x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 6 | LINK/USD | 8.89837 | 60.14 | +0.29% | 2.15x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | SUI/USD | 0.6512 | 57.93 | +0.43% | 0.75x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 8 | STBL/USD | 0.018761 | 56.23 | -0.69% | 1.64x | WEAK 38/100 | EXTREME 85/100 | Do nothing |
| 9 | BCH/USD | 199.88 | 52.19 | -0.03% | 2.20x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 10 | XMR/USD | 511.98 | 51.07 | -0.28% | 0.96x | WEAK 26/100 | VERY_HIGH 74/100 | Do nothing |
| 11 | ASTER/USD | 0.4919 | 46.15 | +0.10% | 0.88x | WEAK 43/100 | HIGH 67/100 | Watch |
| 12 | AAVE/USD | 94.65 | 46.06 | +0.50% | 1.07x | MODERATE 58/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.506 | 88.13 | +0.33% | 1.54x | 10101 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 60.74 | 63.50 | +1.02% | 1.22x | 21670 | STRONG 77/100 | HIGH 62/100 | Watch |
| 3 | HBAR/USD | 0.05117 | 55.49 | +0.18% | 1.14x | 5603 | MODERATE 53/100 | HIGH 67/100 | Watch |

**Same-run overlap:** VVV/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
