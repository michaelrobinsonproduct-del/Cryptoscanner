# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T06:27:30.841951+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45560378291
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d4d73217ed14b4fa669af95f0e55a8a8cf418d87 (atomic ledger/results publication)
**Ledger generation:** 1681 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01015 | 99.174 | 83.677 | +7.18% | +0.10% | 3.08x | 19.7 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Watch | WATCH |
| 2 | BABY/USD | 0.00886 | 89.540 | 71.670 | +7.26% | +0.57% | 3.14x | 11.3 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 25.036 | 70.621 | 64.612 | +2.03% | +0.22% | 1.49x | 9.2 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.513e-06 | 67.529 | 50.382 | +1.74% | +0.43% | 3.67x | 11.4 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 5 | DRV/USD | 0.33018 | 64.393 | 62.308 | +5.06% | +0.20% | 1.11x | 20.3 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0449 | 57.851 | 38.357 | +2.05% | +0.90% | 3.01x | 22.3 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | TRX/USD | 0.30857 | 57.540 | 42.298 | +0.28% | +0.05% | 10.55x | 1.4 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | PENGU/USD | 0.004254 | 57.257 | 38.831 | +0.90% | +0.69% | 8.69x | 2.4 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 9 | CAP/USD | 0.093282 | 52.698 | 36.479 | +0.93% | +0.24% | 4.65x | 4.6 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 10 | SYRUP/USD | 0.07197 | 45.595 | 45.843 | +3.30% | +0.91% | 0.52x | 18.1 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | SKY/USD | 0.04116 | 25.026 | 33.204 | +0.44% | -0.39% | 0.38x | 7.3 | 2026-11-25T06:27:22.818850+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 83.677 | 0.01015 | +0.10% | 3.08x |
| 2 | BABY/USD | 71.670 | 0.00886 | +0.57% | 3.14x |
| 3 | VVV/USD | 64.612 | 25.036 | +0.22% | 1.49x |
| 4 | DRV/USD | 62.308 | 0.33018 | +0.20% | 1.11x |
| 5 | PEPE/USD | 50.382 | 3.513e-06 | +0.43% | 3.67x |
| 6 | SYRUP/USD | 45.843 | 0.07197 | +0.91% | 0.52x |
| 7 | TRX/USD | 42.298 | 0.30857 | +0.05% | 10.55x |
| 8 | PENGU/USD | 38.831 | 0.004254 | +0.69% | 8.69x |
| 9 | XPL/USD | 38.357 | 0.0449 | +0.90% | 3.01x |
| 10 | CAP/USD | 36.479 | 0.093282 | +0.24% | 4.65x |
| 11 | SKY/USD | 33.204 | 0.04116 | -0.39% | 0.38x |

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

- Persisted scans: 1681; predictions: 14273; observations: 1018820.
- Matured sampled outcomes across 1/6/24/48h: 30416; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45560378291 · **Generation:** 1681 · **Legacy run:** 45560378291
**Main quote time:** 2026-11-25T06:27:30.841951+00:00 · **Legacy report time:** 2026-11-25T06:28:31.555758+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01015 | 99.17 | +0.10% | 3.08x | STRONG 100/100 | HIGH 61/100 | Watch |
| 2 | BABY/USD ⭐ | 0.00886 | 89.54 | +0.57% | 3.14x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 25.036 | 70.62 | +0.22% | 1.49x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.513e-06 | 67.53 | +0.43% | 3.67x | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 5 | DRV/USD ⭐ | 0.33018 | 64.39 | +0.20% | 1.11x | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |
| 6 | XPL/USD ⭐ | 0.0449 | 57.85 | +0.90% | 3.01x | STRONG 84/100 | VERY_HIGH 72/100 | Watch |
| 7 | TRX/USD | 0.30857 | 57.54 | +0.05% | 10.55x | STRONG 74/100 | HIGH 55/100 | Watch |
| 8 | PENGU/USD ⭐ | 0.004254 | 57.26 | +0.69% | 8.69x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 9 | CAP/USD ⭐ | 0.093282 | 52.70 | +0.24% | 4.65x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 10 | SYRUP/USD | 0.07197 | 45.59 | +0.91% | 0.52x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 11 | SKY/USD | 0.04116 | 25.03 | -0.39% | 0.38x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01019 | 89.47 | +0.10% | 3.08x | 18505 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | BABY/USD ⭐ | 0.00885 | 81.12 | +0.57% | 3.14x | 4054 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | DRV/USD ⭐ | 0.32945 | 75.26 | +0.20% | 1.11x | 8865 | STRONG 73/100 | VERY_HIGH 74/100 | Watch |
| 4 | VVV/USD ⭐ | 25.067 | 65.49 | +0.22% | 1.49x | 15085 | STRONG 83/100 | HIGH 61/100 | Watch |
| 5 | PEPE/USD ⭐ | 3.507e-06 | 58.39 | +0.43% | 3.67x | 5472 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | XPL/USD ⭐ | 0.0449 | 51.43 | +0.90% | 3.01x | 1568 | STRONG 76/100 | VERY_HIGH 82/100 | Watch |
| 7 | PENGU/USD ⭐ | 0.004255 | 50.98 | +0.69% | 8.69x | 3037 | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 8 | CAP/USD ⭐ | 0.093069 | 40.53 | +0.24% | 4.65x | 5263 | STRONG 80/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** MON/USD, BABY/USD, VVV/USD, PEPE/USD, DRV/USD, XPL/USD, PENGU/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
