# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T09:11:55.554370+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45971358602
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 82c29bddd7e79d4d8d720769825b90a8318ed46c (atomic ledger/results publication)
**Ledger generation:** 1987 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 752.46 | 117.666 | 98.405 | +10.39% | +0.85% | 2.92x | 3.2 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.8944 | 94.307 | 78.560 | +5.25% | +0.15% | 2.51x | 5.5 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.64 | 86.319 | 91.953 | +5.50% | +0.31% | 0.28x | 3.0 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PAXG/USD | 3667.72 | 78.218 | 62.564 | +3.12% | +0.13% | 8.57x | 0.1 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.97697 | 77.398 | 79.846 | +3.63% | -0.01% | 0.76x | 1.1 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 73.44 | 77.073 | 78.988 | +3.52% | +0.15% | 0.73x | 1.4 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ENA/USD | 0.1075 | 74.504 | 76.931 | +7.07% | +0.84% | 0.34x | 9.3 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.1152 | 73.535 | 70.296 | +2.21% | +0.39% | 1.13x | 0.3 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 9 | AVAX/USD | 6.771 | 73.120 | 57.381 | +2.67% | +0.15% | 5.56x | 1.5 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 10 | LINK/USD | 9.59525 | 69.524 | 77.749 | +3.53% | -0.02% | 0.19x | 3.9 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0581398 | 69.386 | 68.935 | +3.13% | +0.17% | 0.96x | 0.4 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 12 | ETH/USD | 1728.85 | 65.790 | 71.585 | +2.44% | +0.14% | 0.35x | 1.0 | 2026-11-27T09:11:47.544702+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.405 | 752.46 | +0.85% | 2.92x |
| 2 | HYPE/USD | 91.953 | 65.64 | +0.31% | 0.28x |
| 3 | XRP/USD | 79.846 | 0.97697 | -0.01% | 0.76x |
| 4 | SOL/USD | 78.988 | 73.44 | +0.15% | 0.73x |
| 5 | UNI/USD | 78.560 | 4.8944 | +0.15% | 2.51x |
| 6 | LINK/USD | 77.749 | 9.59525 | -0.02% | 0.19x |
| 7 | ENA/USD | 76.931 | 0.1075 | +0.84% | 0.34x |
| 8 | ETH/USD | 71.585 | 1728.85 | +0.14% | 0.35x |
| 9 | NEAR/USD | 70.296 | 3.1152 | +0.39% | 1.13x |
| 10 | XDG/USD | 68.935 | 0.0581398 | +0.17% | 0.96x |
| 11 | PAXG/USD | 62.564 | 3667.72 | +0.13% | 8.57x |
| 12 | AVAX/USD | 57.381 | 6.771 | +0.15% | 5.56x |

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

- Persisted scans: 1987; predictions: 17546; observations: 1203314.
- Matured sampled outcomes across 1/6/24/48h: 38873; gap abstentions: 25715. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45971358602 · **Generation:** 1987 · **Legacy run:** 45971358602
**Main quote time:** 2026-11-27T09:11:55.554370+00:00 · **Legacy report time:** 2026-11-27T09:12:41.101293+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 752.46 | 117.67 | +0.85% | 2.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.8944 | 94.31 | +0.15% | 2.51x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 65.64 | 86.32 | +0.31% | 0.28x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 4 | PAXG/USD ⭐ | 3667.72 | 78.22 | +0.13% | 8.57x | STRONG 94/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD | 0.97697 | 77.40 | -0.01% | 0.76x | WEAK 44/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD | 73.44 | 77.07 | +0.15% | 0.73x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | ENA/USD | 0.1075 | 74.50 | +0.84% | 0.34x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 8 | NEAR/USD | 3.1152 | 73.53 | +0.39% | 1.13x | STRONG 72/100 | HIGH 62/100 | Watch |
| 9 | AVAX/USD | 6.771 | 73.12 | +0.15% | 5.56x | STRONG 82/100 | HIGH 55/100 | Watch |
| 10 | LINK/USD | 9.59525 | 69.52 | -0.02% | 0.19x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0581398 | 69.39 | +0.17% | 0.96x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 12 | ETH/USD | 1728.85 | 65.79 | +0.14% | 0.35x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 752.28 | 100.00 | +0.85% | 2.92x | 40774 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.8941 | 92.84 | +0.15% | 2.51x | 7496 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | PAXG/USD ⭐ | 3666.53 | 84.80 | +0.13% | 8.57x | 2528 | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | FET/USD | 0.1278 | 81.00 | +0.39% | 2.67x | 2836 | STRONG 85/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** ZEC/USD, UNI/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
