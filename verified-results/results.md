# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T02:59:14.309108+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43670222859
**Source SHA:** 19c5dd0cce72e8623387504f5a6a60fd3618c8c6
**Previous ledger commit:** 2068a8fbd3b54f76d428349214d73b351d7978af (atomic ledger/results publication)
**Ledger generation:** 428 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 911.94 | 102.483 | 88.247 | +5.56% | -0.15% | 3.47x | 11.4 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 18.253 | 100.355 | 84.803 | +5.20% | +0.11% | 2.58x | 8.8 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XRP/USD | 0.95406 | 93.128 | 85.804 | +4.41% | +0.62% | 1.42x | 0.1 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 4 | JUP/USD | 0.26344 | 88.014 | 84.478 | +6.25% | -0.15% | 1.43x | 7.6 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 5 | QNT/USD | 150.69 | 85.623 | 83.743 | +5.15% | +0.79% | 0.79x | 14.6 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 68/100 | HIGH 68/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.1459 | 79.611 | 79.495 | +3.86% | -0.20% | 1.11x | 5.1 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ASTER/USD | 0.52855 | 74.224 | 75.985 | +5.59% | +0.03% | 0.81x | 6.7 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 8 | HYPE/USD | 66.11 | 73.331 | 73.837 | +2.80% | -0.15% | 1.02x | 1.5 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.719 | 73.032 | 71.994 | +2.63% | +0.24% | 0.99x | 2.8 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ZRO/USD | 1.473 | 72.371 | 75.064 | +4.32% | -0.40% | 0.93x | 20.4 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0586319 | 71.266 | 71.073 | +2.30% | +0.32% | 0.86x | 0.0 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TAO/USD | 190.3882 | 67.573 | 74.189 | +3.54% | -0.27% | 0.48x | 11.2 | 2026-11-15T02:59:05.971854+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 88.247 | 911.94 | -0.15% | 3.47x |
| 2 | XRP/USD | 85.804 | 0.95406 | +0.62% | 1.42x |
| 3 | VVV/USD | 84.803 | 18.253 | +0.11% | 2.58x |
| 4 | JUP/USD | 84.478 | 0.26344 | -0.15% | 1.43x |
| 5 | QNT/USD | 83.743 | 150.69 | +0.79% | 0.79x |
| 6 | NEAR/USD | 79.495 | 3.1459 | -0.20% | 1.11x |
| 7 | ASTER/USD | 75.985 | 0.52855 | +0.03% | 0.81x |
| 8 | ZRO/USD | 75.064 | 1.473 | -0.40% | 0.93x |
| 9 | TAO/USD | 74.189 | 190.3882 | -0.27% | 0.48x |
| 10 | HYPE/USD | 73.837 | 66.11 | -0.15% | 1.02x |
| 11 | SUI/USD | 71.994 | 0.719 | +0.24% | 0.99x |
| 12 | XDG/USD | 71.073 | 0.0586319 | +0.32% | 0.86x |

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

- Persisted scans: 428; predictions: 3652; observations: 257711.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 10691. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43670222859 · **Generation:** 428 · **Legacy run:** 43670222859
**Main quote time:** 2026-11-15T02:59:14.309108+00:00 · **Legacy report time:** 2026-11-15T02:59:30.790445+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 911.94 | 102.48 | -0.15% | 3.47x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD ⭐ | 18.253 | 100.35 | +0.11% | 2.58x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.95406 | 93.13 | +0.62% | 1.42x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | JUP/USD | 0.26344 | 88.01 | -0.15% | 1.43x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 5 | QNT/USD | 150.69 | 85.62 | +0.79% | 0.79x | MODERATE 68/100 | HIGH 68/100 | Watch |
| 6 | NEAR/USD | 3.1459 | 79.61 | -0.20% | 1.11x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 7 | ASTER/USD | 0.52855 | 74.22 | +0.03% | 0.81x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 8 | HYPE/USD | 66.11 | 73.33 | -0.15% | 1.02x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.719 | 73.03 | +0.24% | 0.99x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 10 | ZRO/USD | 1.473 | 72.37 | -0.40% | 0.93x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |
| 11 | XDG/USD | 0.0586319 | 71.27 | +0.32% | 0.86x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 12 | TAO/USD | 190.3882 | 67.57 | -0.27% | 0.48x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95432 | 99.36 | +0.62% | 1.42x | 72365 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | LIGHTER/USD | 3.017 | 93.86 | +1.27% | 6.94x | 6981 | STRONG 97/100 | HIGH 61/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 18.225 | 90.30 | +0.11% | 2.58x | 11327 | STRONG 95/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
