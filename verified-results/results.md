# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:30:06.562358+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44199823124
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** 8230f5da7630445e176070ce0070f9a63b2b4520 (atomic ledger/results publication)
**Ledger generation:** 471 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 960.71 | 106.811 | 95.582 | +6.30% | -0.75% | 3.39x | 7.0 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SOL/USD | 74.96 | 100.480 | 88.002 | +4.81% | -0.50% | 4.12x | 1.3 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INJ/USD | 7.342 | 91.857 | 97.906 | +6.42% | -0.50% | 0.65x | 4.1 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.3636 | 90.389 | 97.473 | +6.52% | -0.46% | 0.52x | 5.1 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XRP/USD | 0.98456 | 90.155 | 76.239 | +3.12% | -0.22% | 15.08x | 1.2 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 6 | TAO/USD | 197.5481 | 89.206 | 74.484 | +3.32% | -0.06% | 2.54x | 7.5 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5082 | 88.554 | 73.686 | +6.23% | -0.02% | 2.50x | 3.9 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 8 | SUI/USD | 0.7368 | 83.485 | 71.252 | +2.42% | -0.55% | 15.37x | 1.4 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 9 | RENDER/USD | 1.477 | 82.602 | 72.152 | +7.26% | +0.48% | 1.81x | 13.6 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Consider small entry | WATCH |
| 10 | XDG/USD | 0.0599744 | 80.526 | 67.511 | +1.85% | -0.40% | 3.12x | 0.0 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 11 | AVAX/USD | 7.274 | 70.368 | 59.956 | +2.29% | -0.23% | 2.16x | 1.4 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XMR/USD | 510.29 | 69.242 | 74.287 | +3.39% | -0.04% | 0.52x | 8.8 | 2026-11-17T23:30:01.556606+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 97.906 | 7.342 | -0.50% | 0.65x |
| 2 | NEAR/USD | 97.473 | 3.3636 | -0.46% | 0.52x |
| 3 | ZEC/USD | 95.582 | 960.71 | -0.75% | 3.39x |
| 4 | SOL/USD | 88.002 | 74.96 | -0.50% | 4.12x |
| 5 | XRP/USD | 76.239 | 0.98456 | -0.22% | 15.08x |
| 6 | TAO/USD | 74.484 | 197.5481 | -0.06% | 2.54x |
| 7 | XMR/USD | 74.287 | 510.29 | -0.04% | 0.52x |
| 8 | AKT/USD | 73.686 | 0.5082 | -0.02% | 2.50x |
| 9 | RENDER/USD | 72.152 | 1.477 | +0.48% | 1.81x |
| 10 | SUI/USD | 71.252 | 0.7368 | -0.55% | 15.37x |
| 11 | XDG/USD | 67.511 | 0.0599744 | -0.40% | 3.12x |
| 12 | AVAX/USD | 59.956 | 7.274 | -0.23% | 2.16x |

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

- Persisted scans: 471; predictions: 4133; observations: 283846.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44199823124 · **Generation:** 471 · **Legacy run:** 44199823124
**Main quote time:** 2026-11-17T23:30:06.562358+00:00 · **Legacy report time:** 2026-11-17T23:30:13.922408+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 960.71 | 106.81 | -0.75% | 3.39x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD | 74.96 | 100.48 | -0.50% | 4.12x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | INJ/USD | 7.342 | 91.86 | -0.50% | 0.65x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 4 | NEAR/USD | 3.3636 | 90.39 | -0.46% | 0.52x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 5 | XRP/USD | 0.98456 | 90.15 | -0.22% | 15.08x | STRONG 75/100 | HIGH 61/100 | Watch |
| 6 | TAO/USD | 197.5481 | 89.21 | -0.06% | 2.54x | STRONG 75/100 | HIGH 61/100 | Watch |
| 7 | AKT/USD | 0.5082 | 88.55 | -0.02% | 2.50x | STRONG 74/100 | HIGH 66/100 | Watch |
| 8 | SUI/USD | 0.7368 | 83.49 | -0.55% | 15.37x | STRONG 72/100 | HIGH 61/100 | Watch |
| 9 | RENDER/USD | 1.477 | 82.60 | +0.48% | 1.81x | STRONG 81/100 | HIGH 66/100 | Consider small entry |
| 10 | XDG/USD | 0.0599744 | 80.53 | -0.40% | 3.12x | STRONG 70/100 | HIGH 61/100 | Watch |
| 11 | AVAX/USD | 7.274 | 70.37 | -0.23% | 2.16x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 12 | XMR/USD | 510.29 | 69.24 | -0.04% | 0.52x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.09839 | 89.50 | +1.87% | 18.37x | 4290 | STRONG 90/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
