# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:40:14.462220+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44315948228
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6f0dba48857045ad95ddfa9272484765a557cfe1 (atomic ledger/results publication)
**Ledger generation:** 579 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5248 | 69.098 | 50.934 | +3.04% | +0.63% | 4.80x | 5.7 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 2 | VVV/USD | 21.329 | 64.007 | 50.247 | +1.44% | -0.25% | 5.43x | 16.4 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | MODERATE 57/100 | HIGH 67/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98673 | 59.378 | 57.942 | +0.43% | +0.33% | 0.98x | 0.1 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04644 | 56.775 | 62.955 | +3.45% | +0.06% | 0.35x | 19.4 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | TRX/USD | 0.309617 | 47.521 | 45.518 | +0.56% | +0.02% | 1.19x | 0.0 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 6 | CC/USD | 0.08322 | 47.014 | 41.744 | +1.33% | -0.11% | 1.58x | 6.0 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | WEAK 44/100 | HIGH 66/100 | Watch | WATCH |
| 7 | USELESS/USD | 0.1003 | 45.720 | 52.400 | +2.79% | +0.10% | 0.28x | 18.0 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SENT/USD | 0.01923 | 41.931 | 47.901 | +3.00% | -1.23% | 1.02x | 8.3 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 9 | W/USD | 0.0091 | 39.265 | 39.540 | +1.90% | +0.33% | 0.81x | 11.0 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | CAP/USD | 0.101828 | 36.312 | 34.206 | +0.85% | +0.10% | 1.16x | 6.1 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | PEARL/USD | 1.8186 | 33.831 | 36.464 | +0.45% | +0.35% | 0.56x | 9.9 | 2026-11-18T13:40:06.415456+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 62.955 | 0.04644 | +0.06% | 0.35x |
| 2 | XRP/USD | 57.942 | 0.98673 | +0.33% | 0.98x |
| 3 | USELESS/USD | 52.400 | 0.1003 | +0.10% | 0.28x |
| 4 | AKT/USD | 50.934 | 0.5248 | +0.63% | 4.80x |
| 5 | VVV/USD | 50.247 | 21.329 | -0.25% | 5.43x |
| 6 | SENT/USD | 47.901 | 0.01923 | -1.23% | 1.02x |
| 7 | TRX/USD | 45.518 | 0.309617 | +0.02% | 1.19x |
| 8 | CC/USD | 41.744 | 0.08322 | -0.11% | 1.58x |
| 9 | W/USD | 39.540 | 0.0091 | +0.33% | 0.81x |
| 10 | PEARL/USD | 36.464 | 1.8186 | +0.35% | 0.56x |
| 11 | CAP/USD | 34.206 | 0.101828 | +0.10% | 1.16x |

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

- Persisted scans: 579; predictions: 4903; observations: 349618.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13064. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44315948228 · **Generation:** 579 · **Legacy run:** 44315948228
**Main quote time:** 2026-11-18T13:40:14.462220+00:00 · **Legacy report time:** 2026-11-18T13:40:39.166216+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5248 | 69.10 | +0.63% | 4.80x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | VVV/USD | 21.329 | 64.01 | -0.25% | 5.43x | MODERATE 57/100 | HIGH 67/100 | Watch |
| 3 | XRP/USD | 0.98673 | 59.38 | +0.33% | 0.98x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 4 | NIGHT/USD | 0.04644 | 56.77 | +0.06% | 0.35x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 5 | TRX/USD | 0.309617 | 47.52 | +0.02% | 1.19x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 6 | CC/USD | 0.08322 | 47.01 | -0.11% | 1.58x | WEAK 44/100 | HIGH 66/100 | Watch |
| 7 | USELESS/USD | 0.1003 | 45.72 | +0.10% | 0.28x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | SENT/USD | 0.01923 | 41.93 | -1.23% | 1.02x | WEAK 31/100 | VERY_HIGH 84/100 | Do nothing |
| 9 | W/USD | 0.0091 | 39.27 | +0.33% | 0.81x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 10 | CAP/USD | 0.101828 | 36.31 | +0.10% | 1.16x | WEAK 43/100 | VERY_HIGH 74/100 | Watch |
| 11 | PEARL/USD | 1.8186 | 33.83 | +0.35% | 0.56x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5248 | 69.91 | +0.63% | 4.80x | 4629 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
