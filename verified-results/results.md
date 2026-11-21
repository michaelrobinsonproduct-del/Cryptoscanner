# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T12:00:52.307354+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44901679227
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 6657643f6e4c1b9b35bfa1079e35b0eb7dc70f91 (atomic ledger/results publication)
**Ledger generation:** 1130 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.084 | 113.284 | 95.249 | +6.49% | +0.61% | 5.39x | 9.5 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ETH/USD | 1651.01 | 83.593 | 68.638 | +1.96% | -0.01% | 7.91x | 0.1 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 762.05 | 72.550 | 56.199 | +0.55% | +0.27% | 6.77x | 5.3 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 472.29 | 71.990 | 75.736 | +3.51% | +0.37% | 0.44x | 7.6 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | UNI/USD | 4.5034 | 71.862 | 58.562 | +0.81% | +0.44% | 2.11x | 4.2 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | TAO/USD | 181.0291 | 69.905 | 54.825 | +0.29% | +0.02% | 5.76x | 4.4 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 7 | TRX/USD | 0.3029 | 57.915 | 57.696 | +0.46% | +0.01% | 1.02x | 1.1 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 8 | AAVE/USD | 99.45 | 55.573 | 54.224 | +1.59% | +0.42% | 0.92x | 6.0 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 9 | AKT/USD | 0.506 | 48.014 | 32.222 | +0.42% | +0.16% | 3.80x | 7.9 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 10 | SKY/USD | 0.04445 | 32.848 | 41.903 | +1.39% | -0.76% | 0.47x | 4.5 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | SENT/USD | 0.020925 | 32.045 | 38.159 | +1.60% | +0.11% | 0.33x | 8.1 | 2026-11-21T12:00:43.237816+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.249 | 22.084 | +0.61% | 5.39x |
| 2 | XMR/USD | 75.736 | 472.29 | +0.37% | 0.44x |
| 3 | ETH/USD | 68.638 | 1651.01 | -0.01% | 7.91x |
| 4 | UNI/USD | 58.562 | 4.5034 | +0.44% | 2.11x |
| 5 | TRX/USD | 57.696 | 0.3029 | +0.01% | 1.02x |
| 6 | ZEC/USD | 56.199 | 762.05 | +0.27% | 6.77x |
| 7 | TAO/USD | 54.825 | 181.0291 | +0.02% | 5.76x |
| 8 | AAVE/USD | 54.224 | 99.45 | +0.42% | 0.92x |
| 9 | SKY/USD | 41.903 | 0.04445 | -0.76% | 0.47x |
| 10 | SENT/USD | 38.159 | 0.020925 | +0.11% | 0.33x |
| 11 | AKT/USD | 32.222 | 0.506 | +0.16% | 3.80x |

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

- Persisted scans: 1130; predictions: 8872; observations: 683399.
- Matured sampled outcomes across 1/6/24/48h: 11674; gap abstentions: 20362. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 14 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44901679227 · **Generation:** 1130 · **Legacy run:** 44901679227
**Main quote time:** 2026-11-21T12:00:52.307354+00:00 · **Legacy report time:** 2026-11-21T12:01:56.080243+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.084 | 113.28 | +0.61% | 5.39x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD | 1651.01 | 83.59 | -0.01% | 7.91x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD ⭐ | 762.05 | 72.55 | +0.27% | 6.77x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD | 472.29 | 71.99 | +0.37% | 0.44x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 5 | UNI/USD ⭐ | 4.5034 | 71.86 | +0.44% | 2.11x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | TAO/USD | 181.0291 | 69.91 | +0.02% | 5.76x | STRONG 80/100 | HIGH 55/100 | Watch |
| 7 | TRX/USD | 0.3029 | 57.91 | +0.01% | 1.02x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 8 | AAVE/USD | 99.45 | 55.57 | +0.42% | 0.92x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 9 | AKT/USD | 0.506 | 48.01 | +0.16% | 3.80x | MODERATE 69/100 | HIGH 60/100 | Watch |
| 10 | SKY/USD | 0.04445 | 32.85 | -0.76% | 0.47x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | SENT/USD | 0.020925 | 32.05 | +0.11% | 0.33x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.074 | 94.82 | +0.61% | 5.39x | 14429 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 763.79 | 68.02 | +0.27% | 6.77x | 58132 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.4917 | 50.09 | +0.44% | 2.11x | 12455 | STRONG 90/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, ZEC/USD, UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
