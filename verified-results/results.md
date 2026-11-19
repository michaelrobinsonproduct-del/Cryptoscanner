# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:45:20.913843+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44467236829
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6a2e3993241c8f01f1f1b08dbea03c14eb710055 (atomic ledger/results publication)
**Ledger generation:** 768 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.653 | 86.860 | 83.766 | +4.53% | +0.19% | 1.22x | 5.3 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 2 | TAO/USD | 194.5536 | 75.692 | 60.563 | +1.35% | +0.03% | 3.82x | 7.8 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 936.19 | 73.599 | 71.421 | +2.66% | +0.09% | 1.17x | 4.4 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SUI/USD | 0.7222 | 72.383 | 57.521 | +0.46% | -0.03% | 11.97x | 1.4 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.3763 | 66.214 | 68.935 | +2.39% | -0.61% | 1.03x | 5.6 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 74.51 | 64.227 | 63.562 | +1.32% | +0.05% | 1.04x | 1.3 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 7 | HYPE/USD | 67.83 | 59.468 | 64.206 | +1.42% | +0.03% | 0.51x | 1.5 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1798.21 | 57.807 | 64.221 | +1.32% | +0.08% | 0.32x | 0.1 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 44.41 | 56.856 | 56.825 | +0.91% | +0.09% | 0.96x | 2.3 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XRP/USD | 0.97244 | 55.890 | 59.346 | +0.63% | -0.09% | 0.70x | 0.1 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ADA/USD | 0.152722 | 55.270 | 59.568 | +0.97% | -0.00% | 0.57x | 4.5 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XBT/USD | 63297.5 | 53.660 | 58.471 | +0.50% | -0.12% | 0.58x | 0.0 | 2026-11-19T05:45:13.203805+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 83.766 | 22.653 | +0.19% | 1.22x |
| 2 | ZEC/USD | 71.421 | 936.19 | +0.09% | 1.17x |
| 3 | NEAR/USD | 68.935 | 3.3763 | -0.61% | 1.03x |
| 4 | ETH/USD | 64.221 | 1798.21 | +0.08% | 0.32x |
| 5 | HYPE/USD | 64.206 | 67.83 | +0.03% | 0.51x |
| 6 | SOL/USD | 63.562 | 74.51 | +0.05% | 1.04x |
| 7 | TAO/USD | 60.563 | 194.5536 | +0.03% | 3.82x |
| 8 | ADA/USD | 59.568 | 0.152722 | -0.00% | 0.57x |
| 9 | XRP/USD | 59.346 | 0.97244 | -0.09% | 0.70x |
| 10 | XBT/USD | 58.471 | 63297.5 | -0.12% | 0.58x |
| 11 | SUI/USD | 57.521 | 0.7222 | -0.03% | 11.97x |
| 12 | LTC/USD | 56.825 | 44.41 | +0.09% | 0.96x |

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

- Persisted scans: 768; predictions: 6360; observations: 464718.
- Matured sampled outcomes across 1/6/24/48h: 6384; gap abstentions: 13782. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44467236829 · **Generation:** 768 · **Legacy run:** 44467236829
**Main quote time:** 2026-11-19T05:45:20.913843+00:00 · **Legacy report time:** 2026-11-19T05:46:02.181710+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.653 | 86.86 | +0.19% | 1.22x | STRONG 78/100 | HIGH 62/100 | Watch |
| 2 | TAO/USD | 194.5536 | 75.69 | +0.03% | 3.82x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 936.19 | 73.60 | +0.09% | 1.17x | STRONG 72/100 | HIGH 62/100 | Watch |
| 4 | SUI/USD | 0.7222 | 72.38 | -0.03% | 11.97x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 3.3763 | 66.21 | -0.61% | 1.03x | WEAK 43/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD ⭐ | 74.51 | 64.23 | +0.05% | 1.04x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | HYPE/USD | 67.83 | 59.47 | +0.03% | 0.51x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD | 1798.21 | 57.81 | +0.08% | 0.32x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 44.41 | 56.86 | +0.09% | 0.96x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 10 | XRP/USD | 0.97244 | 55.89 | -0.09% | 0.70x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ADA/USD | 0.152722 | 55.27 | -0.00% | 0.57x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XBT/USD | 63297.5 | 53.66 | -0.12% | 0.58x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.693 | 91.57 | +0.19% | 1.22x | 9809 | STRONG 81/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 940.63 | 81.56 | +0.09% | 1.17x | 22311 | STRONG 76/100 | HIGH 62/100 | Watch |
| 3 | SOL/USD ⭐ | 74.56 | 66.28 | +0.05% | 1.04x | 35105 | MODERATE 68/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, ZEC/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
