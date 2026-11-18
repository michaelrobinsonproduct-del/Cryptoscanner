# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T07:30:09.326600+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44259289305
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** bbc0f6dc93d8053b2099ae4e754ab71349f0f790 (atomic ledger/results publication)
**Ledger generation:** 567 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.99373 | 78.292 | 62.929 | +1.14% | +0.07% | 7.78x | 0.1 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019404 | 46.556 | 54.626 | +3.94% | -0.94% | 0.66x | 7.7 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | TRX/USD | 0.309597 | 40.106 | 44.397 | +0.55% | +0.04% | 0.55x | 0.0 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5176 | 35.906 | 39.952 | +1.63% | -0.60% | 0.89x | 7.7 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 5 | XDC/USD | 0.03088 | 35.509 | 44.916 | +1.85% | +0.00% | 0.06x | 13.0 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | TRUST/USD | 0.04787 | 30.714 | 36.627 | +1.53% | +0.04% | 0.39x | 14.6 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | CAP/USD | 0.102786 | 24.814 | 27.815 | +1.79% | +0.78% | 0.31x | 32.7 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | AKE/USD | 0.01006203 | 21.623 | 18.170 | +0.78% | -2.31% | 4.23x | 43.6 | 2026-11-18T07:30:03.704217+00:00 | Not calibrated | WEAK 26/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 62.929 | 0.99373 | +0.07% | 7.78x |
| 2 | SENT/USD | 54.626 | 0.019404 | -0.94% | 0.66x |
| 3 | XDC/USD | 44.916 | 0.03088 | +0.00% | 0.06x |
| 4 | TRX/USD | 44.397 | 0.309597 | +0.04% | 0.55x |
| 5 | AKT/USD | 39.952 | 0.5176 | -0.60% | 0.89x |
| 6 | TRUST/USD | 36.627 | 0.04787 | +0.04% | 0.39x |
| 7 | CAP/USD | 27.815 | 0.102786 | +0.78% | 0.31x |
| 8 | AKE/USD | 18.170 | 0.01006203 | -2.31% | 4.23x |

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

- Persisted scans: 567; predictions: 4782; observations: 342310.
- Matured sampled outcomes across 1/6/24/48h: 4136; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44259289305 · **Generation:** 567 · **Legacy run:** 44259289305
**Main quote time:** 2026-11-18T07:30:09.326600+00:00 · **Legacy report time:** 2026-11-18T07:30:33.246802+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.99373 | 78.29 | +0.07% | 7.78x | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | SENT/USD | 0.019404 | 46.56 | -0.94% | 0.66x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 3 | TRX/USD | 0.309597 | 40.11 | +0.04% | 0.55x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 4 | AKT/USD | 0.5176 | 35.91 | -0.60% | 0.89x | WEAK 23/100 | VERY_HIGH 73/100 | Do nothing |
| 5 | XDC/USD | 0.03088 | 35.51 | +0.00% | 0.06x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | TRUST/USD | 0.04787 | 30.71 | +0.04% | 0.39x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | CAP/USD | 0.102786 | 24.81 | +0.78% | 0.31x | WEAK 32/100 | EXTREME 94/100 | Do nothing |
| 8 | AKE/USD | 0.01006203 | 21.62 | -2.31% | 4.23x | WEAK 26/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.99313 | 72.96 | +0.07% | 7.78x | 32428 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
