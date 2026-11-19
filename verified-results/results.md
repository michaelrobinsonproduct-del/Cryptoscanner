# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:40:41.997165+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44639504337
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b6bb66a398db8296a3435308ec1a34ac9d9335d5 (atomic ledger/results publication)
**Ledger generation:** 881 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05927 | 81.516 | 67.858 | +5.84% | +0.03% | 2.35x | 10.1 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 2 | CSPR/USD | 0.001703 | 77.770 | 60.728 | +4.28% | +2.52% | 1.44x | 2.3 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5317 | 63.178 | 44.388 | +2.64% | +0.76% | 105.88x | 13.2 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SENT/USD | 0.021209 | 61.729 | 50.827 | +2.93% | -0.82% | 5.89x | 8.0 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 5 | INJ/USD | 7.047 | 60.229 | 50.109 | +0.95% | -0.13% | 2.08x | 4.3 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.0987 | 54.108 | 54.321 | +3.29% | -0.05% | 1.00x | 18.3 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 7 | VVV/USD | 21.828 | 50.364 | 56.864 | +0.72% | -0.00% | 0.35x | 6.4 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | BABY/USD | 0.00843 | 49.217 | 32.432 | +1.08% | +0.36% | 5.62x | 11.9 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | LIGHTER/USD | 2.752 | 47.412 | 39.201 | +1.40% | -0.07% | 1.86x | 10.9 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | TRX/USD | 0.310101 | 42.452 | 44.128 | +0.27% | +0.02% | 0.82x | 0.0 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 11 | PYTH/USD | 0.05303 | 40.541 | 32.087 | +0.51% | -0.08% | 1.88x | 9.5 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | WEAK 40/100 | HIGH 66/100 | Watch | WATCH |
| 12 | AKE/USD | 0.01052434 | 33.846 | 39.587 | +1.28% | +0.05% | 0.40x | 7.9 | 2026-11-19T23:40:33.647379+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 67.858 | 0.05927 | +0.03% | 2.35x |
| 2 | CSPR/USD | 60.728 | 0.001703 | +2.52% | 1.44x |
| 3 | VVV/USD | 56.864 | 21.828 | -0.00% | 0.35x |
| 4 | USELESS/USD | 54.321 | 0.0987 | -0.05% | 1.00x |
| 5 | SENT/USD | 50.827 | 0.021209 | -0.82% | 5.89x |
| 6 | INJ/USD | 50.109 | 7.047 | -0.13% | 2.08x |
| 7 | AKT/USD | 44.388 | 0.5317 | +0.76% | 105.88x |
| 8 | TRX/USD | 44.128 | 0.310101 | +0.02% | 0.82x |
| 9 | AKE/USD | 39.587 | 0.01052434 | +0.05% | 0.40x |
| 10 | LIGHTER/USD | 39.201 | 2.752 | -0.07% | 1.86x |
| 11 | BABY/USD | 32.432 | 0.00843 | +0.36% | 5.62x |
| 12 | PYTH/USD | 32.087 | 0.05303 | -0.08% | 1.88x |

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

- Persisted scans: 881; predictions: 7679; observations: 532368.
- Matured sampled outcomes across 1/6/24/48h: 8222; gap abstentions: 15891. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44639504337 · **Generation:** 881 · **Legacy run:** 44639504337
**Main quote time:** 2026-11-19T23:40:41.997165+00:00 · **Legacy report time:** 2026-11-19T23:41:31.000279+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05927 | 81.52 | +0.03% | 2.35x | STRONG 81/100 | HIGH 66/100 | Watch |
| 2 | CSPR/USD ⭐ | 0.001703 | 77.77 | +2.52% | 1.44x | STRONG 94/100 | HIGH 60/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5317 | 63.18 | +0.76% | 105.88x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 4 | SENT/USD | 0.021209 | 61.73 | -0.82% | 5.89x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 5 | INJ/USD | 7.047 | 60.23 | -0.13% | 2.08x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | USELESS/USD | 0.0987 | 54.11 | -0.05% | 1.00x | WEAK 32/100 | VERY_HIGH 74/100 | Do nothing |
| 7 | VVV/USD | 21.828 | 50.36 | -0.00% | 0.35x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | BABY/USD | 0.00843 | 49.22 | +0.36% | 5.62x | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 9 | LIGHTER/USD | 2.752 | 47.41 | -0.07% | 1.86x | WEAK 39/100 | VERY_HIGH 72/100 | Watch |
| 10 | TRX/USD | 0.310101 | 42.45 | +0.02% | 0.82x | WEAK 41/100 | HIGH 62/100 | Watch |
| 11 | PYTH/USD | 0.05303 | 40.54 | -0.08% | 1.88x | WEAK 40/100 | HIGH 66/100 | Watch |
| 12 | AKE/USD | 0.01052434 | 33.85 | +0.05% | 0.40x | WEAK 37/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CSPR/USD ⭐ | 0.0017021 | 80.50 | +2.52% | 1.44x | 6243 | STRONG 85/100 | VERY_HIGH 72/100 | Watch |
| 2 | AKT/USD ⭐ | 0.5317 | 65.49 | +0.76% | 105.88x | 3572 | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 3 | ADA/USD | 0.151473 | 54.66 | +0.06% | 3.22x | 11440 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** CSPR/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
