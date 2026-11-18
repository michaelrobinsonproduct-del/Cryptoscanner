# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T12:45:09.400944+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44306821438
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** b8db564b90eefcbc50ad041a88e3f68fe0234312 (atomic ledger/results publication)
**Ledger generation:** 568 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019639 | 68.222 | 60.788 | +5.20% | +0.62% | 1.43x | 13.3 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | TRX/USD | 0.309581 | 59.805 | 45.131 | +0.55% | -0.07% | 4.20x | 0.0 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 3 | STABLE/USD | 0.02313 | 55.100 | 60.807 | +9.88% | -1.41% | 1.13x | 30.3 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | WEAK 28/100 | EXTREME 96/100 | Do nothing | WATCH |
| 4 | MNT/USD | 0.3856 | 52.952 | 52.177 | +3.29% | -0.34% | 1.25x | 7.8 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04623 | 46.845 | 58.393 | +2.99% | -0.65% | 0.17x | 21.6 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | WEAK 18/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | VVV/USD | 21.125 | 39.450 | 47.615 | +0.47% | -0.50% | 0.43x | 7.6 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.083 | 37.433 | 40.565 | +1.06% | -0.26% | 0.82x | 6.0 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.517 | 34.986 | 37.238 | +1.51% | -0.29% | 0.92x | 11.6 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.101775 | 28.773 | 19.980 | +0.79% | +0.42% | 1.67x | 33.8 | 2026-11-18T12:45:02.785380+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | STABLE/USD | 60.807 | 0.02313 | -1.41% | 1.13x |
| 2 | SENT/USD | 60.788 | 0.019639 | +0.62% | 1.43x |
| 3 | NIGHT/USD | 58.393 | 0.04623 | -0.65% | 0.17x |
| 4 | MNT/USD | 52.177 | 0.3856 | -0.34% | 1.25x |
| 5 | VVV/USD | 47.615 | 21.125 | -0.50% | 0.43x |
| 6 | TRX/USD | 45.131 | 0.309581 | -0.07% | 4.20x |
| 7 | CC/USD | 40.565 | 0.083 | -0.26% | 0.82x |
| 8 | AKT/USD | 37.238 | 0.517 | -0.29% | 0.92x |
| 9 | CAP/USD | 19.980 | 0.101775 | +0.42% | 1.67x |

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

- Persisted scans: 568; predictions: 4791; observations: 342919.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 12958. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44306821438 · **Generation:** 568 · **Legacy run:** 44306821438
**Main quote time:** 2026-11-18T12:45:09.400944+00:00 · **Legacy report time:** 2026-11-18T12:45:26.342892+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019639 | 68.22 | +0.62% | 1.43x | STRONG 84/100 | VERY_HIGH 73/100 | Watch |
| 2 | TRX/USD | 0.309581 | 59.80 | -0.07% | 4.20x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 3 | STABLE/USD | 0.02313 | 55.10 | -1.41% | 1.13x | WEAK 28/100 | EXTREME 96/100 | Do nothing |
| 4 | MNT/USD | 0.3856 | 52.95 | -0.34% | 1.25x | WEAK 36/100 | VERY_HIGH 73/100 | Watch |
| 5 | NIGHT/USD | 0.04623 | 46.85 | -0.65% | 0.17x | WEAK 18/100 | EXTREME 88/100 | Do nothing |
| 6 | VVV/USD | 21.125 | 39.45 | -0.50% | 0.43x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | CC/USD | 0.083 | 37.43 | -0.26% | 0.82x | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing |
| 8 | AKT/USD | 0.517 | 34.99 | -0.29% | 0.92x | WEAK 17/100 | VERY_HIGH 79/100 | Do nothing |
| 9 | CAP/USD ⭐ | 0.101775 | 28.77 | +0.42% | 1.67x | MODERATE 59/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019618 | 80.04 | +0.62% | 1.43x | 5602 | STRONG 95/100 | HIGH 67/100 | Watch |
| 2 | CAP/USD ⭐ | 0.101775 | 35.75 | +0.42% | 1.67x | 2579 | MODERATE 63/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** SENT/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
