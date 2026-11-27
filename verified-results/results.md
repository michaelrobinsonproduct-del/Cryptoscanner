# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T03:11:55.001951+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45932517709
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bd35350f0d93838c438cb340c5b1d0a746f3d2a1 (atomic ledger/results publication)
**Ledger generation:** 1951 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.15 | 97.840 | 97.702 | +6.32% | +1.55% | 0.24x | 3.0 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 752.75 | 94.774 | 95.681 | +10.43% | +1.27% | 0.28x | 8.6 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04928 | 87.429 | 72.974 | +6.18% | +1.34% | 1.78x | 10.2 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | STRONG 84/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 471.59 | 83.817 | 74.034 | +3.20% | -0.05% | 2.00x | 6.8 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 72.9 | 75.282 | 73.654 | +2.76% | +0.69% | 0.82x | 1.4 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SUI/USD | 0.683 | 74.826 | 69.073 | +2.29% | +0.28% | 1.44x | 1.5 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LINK/USD | 9.50389 | 68.701 | 69.836 | +2.54% | +0.04% | 0.87x | 5.9 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.1342 | 68.091 | 72.747 | +2.83% | +0.57% | 0.25x | 4.1 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.96455 | 66.701 | 70.772 | +2.31% | +0.56% | 0.31x | 0.8 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1729.23 | 65.442 | 71.713 | +2.46% | +0.52% | 0.11x | 1.0 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61537.8 | 63.784 | 67.023 | +1.72% | +0.41% | 0.47x | 0.0 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0578863 | 62.249 | 60.864 | +2.68% | +0.63% | 0.82x | 0.3 | 2026-11-27T03:11:47.043088+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 97.702 | 66.15 | +1.55% | 0.24x |
| 2 | ZEC/USD | 95.681 | 752.75 | +1.27% | 0.28x |
| 3 | XMR/USD | 74.034 | 471.59 | -0.05% | 2.00x |
| 4 | SOL/USD | 73.654 | 72.9 | +0.69% | 0.82x |
| 5 | SKY/USD | 72.974 | 0.04928 | +1.34% | 1.78x |
| 6 | NEAR/USD | 72.747 | 3.1342 | +0.57% | 0.25x |
| 7 | ETH/USD | 71.713 | 1729.23 | +0.52% | 0.11x |
| 8 | XRP/USD | 70.772 | 0.96455 | +0.56% | 0.31x |
| 9 | LINK/USD | 69.836 | 9.50389 | +0.04% | 0.87x |
| 10 | SUI/USD | 69.073 | 0.683 | +0.28% | 1.44x |
| 11 | XBT/USD | 67.023 | 61537.8 | +0.41% | 0.47x |
| 12 | XDG/USD | 60.864 | 0.0578863 | +0.63% | 0.82x |

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

- Persisted scans: 1951; predictions: 17114; observations: 1181635.
- Matured sampled outcomes across 1/6/24/48h: 37574; gap abstentions: 25472. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45932517709 · **Generation:** 1951 · **Legacy run:** 45932517709
**Main quote time:** 2026-11-27T03:11:55.001951+00:00 · **Legacy report time:** 2026-11-27T03:12:46.513381+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 66.15 | 97.84 | +1.55% | 0.24x | STRONG 79/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD | 752.75 | 94.77 | +1.27% | 0.28x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04928 | 87.43 | +1.34% | 1.78x | STRONG 94/100 | HIGH 66/100 | Consider small entry |
| 4 | XMR/USD | 471.59 | 83.82 | -0.05% | 2.00x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 72.9 | 75.28 | +0.69% | 0.82x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 6 | SUI/USD ⭐ | 0.683 | 74.83 | +0.28% | 1.44x | STRONG 92/100 | HIGH 55/100 | Watch |
| 7 | LINK/USD | 9.50389 | 68.70 | +0.04% | 0.87x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 8 | NEAR/USD | 3.1342 | 68.09 | +0.57% | 0.25x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.96455 | 66.70 | +0.56% | 0.31x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1729.23 | 65.44 | +0.52% | 0.11x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61537.8 | 63.78 | +0.41% | 0.47x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0578863 | 62.25 | +0.63% | 0.82x | MODERATE 61/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04919 | 79.98 | +1.34% | 1.78x | 6979 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.6835 | 76.39 | +0.28% | 1.44x | 4940 | STRONG 93/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SKY/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
