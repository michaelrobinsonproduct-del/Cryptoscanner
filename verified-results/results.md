# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:10:05.030856+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44228410900
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** d03eda8ee83ecaed9cba2ae140953b3347398c8f (atomic ledger/results publication)
**Ledger generation:** 515 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2839 | 60.290 | 39.768 | +2.83% | +1.83% | 2.14x | 24.6 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 2.15 | 58.401 | 62.062 | +4.95% | +0.04% | 0.62x | 8.8 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 3 | CC/USD | 0.08333 | 56.924 | 44.147 | +1.46% | +1.20% | 1.68x | 2.4 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06014 | 50.949 | 29.208 | +0.35% | +1.35% | 3.33x | 13.3 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5218 | 41.090 | 41.914 | +2.45% | +0.00% | 0.92x | 15.3 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | SENT/USD | 0.018761 | 39.517 | 32.431 | +0.49% | +0.99% | 1.21x | 3.7 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | TON/USD | 1.08 | 34.158 | 36.235 | +0.28% | +0.09% | 0.75x | 9.3 | 2026-11-18T03:10:01.579801+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 62.062 | 2.15 | +0.04% | 0.62x |
| 2 | CC/USD | 44.147 | 0.08333 | +1.20% | 1.68x |
| 3 | AKT/USD | 41.914 | 0.5218 | +0.00% | 0.92x |
| 4 | ICNT/USD | 39.768 | 0.2839 | +1.83% | 2.14x |
| 5 | TON/USD | 36.235 | 1.08 | +0.09% | 0.75x |
| 6 | SENT/USD | 32.431 | 0.018761 | +0.99% | 1.21x |
| 7 | ZAMA/USD | 29.208 | 0.06014 | +1.35% | 3.33x |

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

- Persisted scans: 515; predictions: 4358; observations: 310642.
- Matured sampled outcomes across 1/6/24/48h: 3503; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44228410900 · **Generation:** 515 · **Legacy run:** 44228410900
**Main quote time:** 2026-11-18T03:10:05.030856+00:00 · **Legacy report time:** 2026-11-18T03:10:22.055135+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2839 | 60.29 | +1.83% | 2.14x | STRONG 85/100 | VERY_HIGH 72/100 | Watch |
| 2 | PIEVERSE/USD | 2.15 | 58.40 | +0.04% | 0.62x | MODERATE 49/100 | VERY_HIGH 75/100 | Watch |
| 3 | CC/USD ⭐ | 0.08333 | 56.92 | +1.20% | 1.68x | STRONG 83/100 | HIGH 60/100 | Consider small entry |
| 4 | ZAMA/USD ⭐ | 0.06014 | 50.95 | +1.35% | 3.33x | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 5 | AKT/USD | 0.5218 | 41.09 | +0.00% | 0.92x | WEAK 36/100 | VERY_HIGH 73/100 | Watch |
| 6 | SENT/USD ⭐ | 0.018761 | 39.52 | +0.99% | 1.21x | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |
| 7 | TON/USD | 1.08 | 34.16 | +0.09% | 0.75x | WEAK 37/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2844 | 69.49 | +1.83% | 2.14x | 3727 | STRONG 90/100 | VERY_HIGH 72/100 | Watch |
| 2 | CC/USD ⭐ | 0.08333 | 54.32 | +1.20% | 1.68x | 3986 | STRONG 82/100 | HIGH 60/100 | Consider small entry |
| 3 | ZAMA/USD ⭐ | 0.06014 | 40.29 | +1.35% | 3.33x | 4484 | STRONG 80/100 | HIGH 66/100 | Consider small entry |
| 4 | SENT/USD ⭐ | 0.018754 | 39.33 | +0.99% | 1.21x | 3783 | MODERATE 65/100 | VERY_HIGH 74/100 | Watch |
| 5 | AKE/USD | 0.01000778 | 31.45 | +0.07% | 1.89x | 5447 | WEAK 41/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** ICNT/USD, CC/USD, ZAMA/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
