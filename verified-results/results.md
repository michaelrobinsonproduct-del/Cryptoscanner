# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:30:00.298335+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44223643885
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** c9f642efc2e65ff25d35b37a3bda68f3509c0943 (atomic ledger/results publication)
**Ledger generation:** 507 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5251 | 69.562 | 50.313 | +3.10% | +0.85% | 6.56x | 7.6 | 2026-11-18T02:29:57.727902+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 2 | UP/USD | 0.05505 | 53.270 | 54.197 | +3.89% | +0.13% | 0.84x | 9.1 | 2026-11-18T02:29:57.727902+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | CAP/USD | 0.101275 | 42.602 | 28.915 | +0.30% | -0.26% | 3.79x | 10.7 | 2026-11-18T02:29:57.727902+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | SENT/USD | 0.01877 | 39.422 | 33.041 | +0.54% | +0.21% | 1.53x | 3.2 | 2026-11-18T02:29:57.727902+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 5 | TON/USD | 1.089 | 34.775 | 42.232 | +1.11% | -0.46% | 0.48x | 9.2 | 2026-11-18T02:29:57.727902+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.2769 | 27.857 | 23.418 | +0.29% | +1.25% | 0.82x | 21.7 | 2026-11-18T02:29:57.727902+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 54.197 | 0.05505 | +0.13% | 0.84x |
| 2 | AKT/USD | 50.313 | 0.5251 | +0.85% | 6.56x |
| 3 | TON/USD | 42.232 | 1.089 | -0.46% | 0.48x |
| 4 | SENT/USD | 33.041 | 0.01877 | +0.21% | 1.53x |
| 5 | CAP/USD | 28.915 | 0.101275 | -0.26% | 3.79x |
| 6 | ICNT/USD | 23.418 | 0.2769 | +1.25% | 0.82x |

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

- Persisted scans: 507; predictions: 4316; observations: 305770.
- Matured sampled outcomes across 1/6/24/48h: 3474; gap abstentions: 12412. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44223643885 · **Generation:** 507 · **Legacy run:** 44223643885
**Main quote time:** 2026-11-18T02:30:00.298335+00:00 · **Legacy report time:** 2026-11-18T02:30:14.894510+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD | 0.5251 | 69.56 | +0.85% | 6.56x | STRONG 90/100 | HIGH 60/100 | Watch |
| 2 | UP/USD | 0.05505 | 53.27 | +0.13% | 0.84x | MODERATE 47/100 | VERY_HIGH 74/100 | Watch |
| 3 | CAP/USD | 0.101275 | 42.60 | -0.26% | 3.79x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 4 | SENT/USD | 0.01877 | 39.42 | +0.21% | 1.53x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 5 | TON/USD | 1.089 | 34.78 | -0.46% | 0.48x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | ICNT/USD ⭐ | 0.2769 | 27.86 | +1.25% | 0.82x | WEAK 44/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2769 | 30.17 | +1.10% | 1.02x | 3675 | MODERATE 50/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
