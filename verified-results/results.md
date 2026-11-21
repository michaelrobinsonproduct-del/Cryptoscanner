# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T14:30:46.763813+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44914192750
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 453a884a3981a0158b1f0539c6f7254daa1ebb19 (atomic ledger/results publication)
**Ledger generation:** 1145 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.054 | 102.812 | 97.179 | +11.16% | +0.94% | 1.09x | 5.6 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | USELESS/USD | 0.08226 | 91.616 | 82.694 | +10.42% | +1.49% | 1.15x | 7.3 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | STRONG 81/100 | HIGH 62/100 | Watch | WATCH |
| 3 | UNI/USD | 4.6991 | 84.132 | 89.103 | +5.19% | -0.34% | 0.67x | 4.5 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ETH/USD | 1690.36 | 80.704 | 85.680 | +4.39% | -0.10% | 0.55x | 0.1 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ZEC/USD | 790.89 | 80.472 | 83.625 | +4.35% | +0.62% | 0.37x | 3.7 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XMR/USD | 472.15 | 80.181 | 79.225 | +3.48% | -0.29% | 1.24x | 0.2 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ALGO/USD | 0.0749 | 74.912 | 54.989 | +2.38% | +0.98% | 3.57x | 2.7 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | SOL/USD | 70.48 | 72.936 | 72.323 | +2.58% | +0.16% | 0.98x | 1.4 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 8.64012 | 72.532 | 62.740 | +1.29% | +0.15% | 1.90x | 2.6 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 10 | TAO/USD | 187.0573 | 71.068 | 77.476 | +3.63% | +0.16% | 0.28x | 5.8 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60278.4 | 68.254 | 72.514 | +2.50% | +0.10% | 0.52x | 0.0 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92791 | 66.518 | 69.305 | +2.11% | +0.27% | 0.59x | 1.0 | 2026-11-21T14:30:38.316571+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 97.179 | 23.054 | +0.94% | 1.09x |
| 2 | UNI/USD | 89.103 | 4.6991 | -0.34% | 0.67x |
| 3 | ETH/USD | 85.680 | 1690.36 | -0.10% | 0.55x |
| 4 | ZEC/USD | 83.625 | 790.89 | +0.62% | 0.37x |
| 5 | USELESS/USD | 82.694 | 0.08226 | +1.49% | 1.15x |
| 6 | XMR/USD | 79.225 | 472.15 | -0.29% | 1.24x |
| 7 | TAO/USD | 77.476 | 187.0573 | +0.16% | 0.28x |
| 8 | XBT/USD | 72.514 | 60278.4 | +0.10% | 0.52x |
| 9 | SOL/USD | 72.323 | 70.48 | +0.16% | 0.98x |
| 10 | XRP/USD | 69.305 | 0.92791 | +0.27% | 0.59x |
| 11 | LINK/USD | 62.740 | 8.64012 | +0.15% | 1.90x |
| 12 | ALGO/USD | 54.989 | 0.0749 | +0.98% | 3.57x |

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

- Persisted scans: 1145; predictions: 9049; observations: 692519.
- Matured sampled outcomes across 1/6/24/48h: 11891; gap abstentions: 20517. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44914192750 · **Generation:** 1145 · **Legacy run:** 44914192750
**Main quote time:** 2026-11-21T14:30:46.763813+00:00 · **Legacy report time:** 2026-11-21T14:31:39.524722+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.054 | 102.81 | +0.94% | 1.09x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.08226 | 91.62 | +1.49% | 1.15x | STRONG 91/100 | HIGH 62/100 | Watch |
| 3 | UNI/USD | 4.6991 | 84.13 | -0.34% | 0.67x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 4 | ETH/USD | 1690.36 | 80.70 | -0.10% | 0.55x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | ZEC/USD | 790.89 | 80.47 | +0.62% | 0.37x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 6 | XMR/USD | 472.15 | 80.18 | -0.29% | 1.24x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 7 | ALGO/USD | 0.0749 | 74.91 | +0.98% | 3.57x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD | 70.48 | 72.94 | +0.16% | 0.98x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD | 8.64012 | 72.53 | +0.15% | 1.90x | STRONG 71/100 | HIGH 55/100 | Watch |
| 10 | TAO/USD | 187.0573 | 71.07 | +0.16% | 0.28x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60278.4 | 68.25 | +0.10% | 0.52x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.92791 | 66.52 | +0.27% | 0.59x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.106 | 88.19 | +0.94% | 1.09x | 15234 | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | SHX/USD | 0.003502 | 83.39 | +0.57% | 1.32x | 2993 | STRONG 87/100 | HIGH 60/100 | Watch |
| 3 | USELESS/USD ⭐ | 0.08195 | 81.84 | +1.49% | 1.15x | 5336 | STRONG 81/100 | HIGH 68/100 | Watch |
| 4 | AKT/USD | 0.53 | 80.82 | +1.75% | 1.88x | 5212 | STRONG 85/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, USELESS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
