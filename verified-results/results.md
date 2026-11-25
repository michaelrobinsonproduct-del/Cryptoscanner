# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T18:45:57.905674+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45678226125
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c18ea0639f33ec39a31a9854340b19eef63e837c (atomic ledger/results publication)
**Ledger generation:** 1752 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.718 | 91.496 | 95.318 | +8.88% | -0.13% | 0.68x | 9.4 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XPL/USD | 0.048 | 80.028 | 71.271 | +9.09% | +0.84% | 1.46x | 20.8 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 3 | DRV/USD | 0.34898 | 75.120 | 78.990 | +11.04% | -0.56% | 0.89x | 10.0 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | LTC/USD | 41.93 | 71.122 | 71.121 | +2.64% | +0.17% | 0.92x | 4.8 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HYPE/USD | 60.51 | 69.523 | 60.830 | +1.07% | +0.12% | 1.81x | 3.3 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ZEC/USD | 744.14 | 68.408 | 56.887 | +0.71% | +0.56% | 1.87x | 6.2 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6547 | 64.906 | 61.257 | +1.11% | +0.23% | 1.25x | 3.1 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XMR/USD | 517.68 | 62.733 | 58.946 | +1.59% | +0.66% | 1.05x | 14.3 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | MODERATE 61/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.928 | 62.614 | 58.273 | +0.48% | +0.25% | 1.31x | 0.1 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ETH/USD | 1681.92 | 57.604 | 55.954 | +0.25% | -0.06% | 1.19x | 1.6 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XLM/USD | 0.126319 | 50.215 | 54.161 | +1.83% | +0.09% | 0.56x | 4.2 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ASTER/USD | 0.49217 | 47.844 | 45.918 | +2.36% | +0.11% | 1.14x | 6.7 | 2026-11-25T18:45:51.007257+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.318 | 26.718 | -0.13% | 0.68x |
| 2 | DRV/USD | 78.990 | 0.34898 | -0.56% | 0.89x |
| 3 | XPL/USD | 71.271 | 0.048 | +0.84% | 1.46x |
| 4 | LTC/USD | 71.121 | 41.93 | +0.17% | 0.92x |
| 5 | SUI/USD | 61.257 | 0.6547 | +0.23% | 1.25x |
| 6 | HYPE/USD | 60.830 | 60.51 | +0.12% | 1.81x |
| 7 | XMR/USD | 58.946 | 517.68 | +0.66% | 1.05x |
| 8 | XRP/USD | 58.273 | 0.928 | +0.25% | 1.31x |
| 9 | ZEC/USD | 56.887 | 744.14 | +0.56% | 1.87x |
| 10 | ETH/USD | 55.954 | 1681.92 | -0.06% | 1.19x |
| 11 | XLM/USD | 54.161 | 0.126319 | +0.09% | 0.56x |
| 12 | ASTER/USD | 45.918 | 0.49217 | +0.11% | 1.14x |

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

- Persisted scans: 1752; predictions: 14768; observations: 1062012.
- Matured sampled outcomes across 1/6/24/48h: 32526; gap abstentions: 22717. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45678226125 · **Generation:** 1752 · **Legacy run:** 45678226125
**Main quote time:** 2026-11-25T18:45:57.905674+00:00 · **Legacy report time:** 2026-11-25T18:47:11.735652+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.718 | 91.50 | -0.13% | 0.68x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | XPL/USD ⭐ | 0.048 | 80.03 | +0.84% | 1.46x | STRONG 85/100 | HIGH 67/100 | Watch |
| 3 | DRV/USD | 0.34898 | 75.12 | -0.56% | 0.89x | WEAK 38/100 | VERY_HIGH 74/100 | Watch |
| 4 | LTC/USD | 41.93 | 71.12 | +0.17% | 0.92x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 5 | HYPE/USD ⭐ | 60.51 | 69.52 | +0.12% | 1.81x | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | ZEC/USD ⭐ | 744.14 | 68.41 | +0.56% | 1.87x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 7 | SUI/USD ⭐ | 0.6547 | 64.91 | +0.23% | 1.25x | STRONG 77/100 | HIGH 62/100 | Watch |
| 8 | XMR/USD | 517.68 | 62.73 | +0.66% | 1.05x | MODERATE 61/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.928 | 62.61 | +0.25% | 1.31x | STRONG 76/100 | HIGH 55/100 | Watch |
| 10 | ETH/USD | 1681.92 | 57.60 | -0.06% | 1.19x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | XLM/USD | 0.126319 | 50.22 | +0.09% | 0.56x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 12 | ASTER/USD ⭐ | 0.49217 | 47.84 | +0.11% | 1.14x | MODERATE 59/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XPL/USD ⭐ | 0.0479 | 74.39 | +0.84% | 1.46x | 2166 | STRONG 77/100 | VERY_HIGH 82/100 | Watch |
| 2 | ZEC/USD ⭐ | 744.74 | 66.40 | +0.56% | 1.87x | 35780 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6549 | 64.35 | +0.23% | 1.25x | 7169 | STRONG 77/100 | HIGH 62/100 | Watch |
| 4 | HYPE/USD ⭐ | 60.44 | 60.40 | +0.12% | 1.81x | 22446 | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | ASTER/USD ⭐ | 0.49236 | 58.99 | +0.11% | 1.14x | 3049 | MODERATE 64/100 | HIGH 67/100 | Watch |

**Same-run overlap:** XPL/USD, HYPE/USD, ZEC/USD, SUI/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
