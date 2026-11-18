# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:20:09.712642+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44312557493
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7f7a130c28f62bc86a98e8dd8f4f8ec42a670171 (atomic ledger/results publication)
**Ledger generation:** 575 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04638 | 82.671 | 70.673 | +3.32% | +0.39% | 2.00x | 2.2 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.5231 | 70.951 | 50.540 | +2.71% | +1.08% | 2.50x | 1.9 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | USELESS/USD | 0.10084 | 59.104 | 59.929 | +3.34% | +0.70% | 0.57x | 10.9 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | STABLE/USD | 0.02323 | 53.148 | 65.204 | +10.36% | -1.06% | 0.33x | 21.6 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | VVV/USD | 21.345 | 50.593 | 46.024 | +1.52% | +1.49% | 0.71x | 25.8 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | CC/USD | 0.0833 | 48.910 | 45.029 | +1.42% | -0.06% | 1.42x | 1.2 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | WEAK 44/100 | HIGH 66/100 | Watch | WATCH |
| 7 | SENT/USD | 0.01941 | 48.251 | 54.700 | +3.97% | -0.36% | 0.54x | 8.2 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | WEAK 29/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.309578 | 42.032 | 44.322 | +0.54% | +0.13% | 0.71x | 1.9 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | CAP/USD | 0.101555 | 25.869 | 33.438 | +0.58% | +0.33% | 0.08x | 3.8 | 2026-11-18T13:20:03.659582+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 70.673 | 0.04638 | +0.39% | 2.00x |
| 2 | STABLE/USD | 65.204 | 0.02323 | -1.06% | 0.33x |
| 3 | USELESS/USD | 59.929 | 0.10084 | +0.70% | 0.57x |
| 4 | SENT/USD | 54.700 | 0.01941 | -0.36% | 0.54x |
| 5 | AKT/USD | 50.540 | 0.5231 | +1.08% | 2.50x |
| 6 | VVV/USD | 46.024 | 21.345 | +1.49% | 0.71x |
| 7 | CC/USD | 45.029 | 0.0833 | -0.06% | 1.42x |
| 8 | TRX/USD | 44.322 | 0.309578 | +0.13% | 0.71x |
| 9 | CAP/USD | 33.438 | 0.101555 | +0.33% | 0.08x |

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

- Persisted scans: 575; predictions: 4862; observations: 347182.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13027. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44312557493 · **Generation:** 575 · **Legacy run:** 44312557493
**Main quote time:** 2026-11-18T13:20:09.712642+00:00 · **Legacy report time:** 2026-11-18T13:20:34.883341+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04638 | 82.67 | +0.39% | 2.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5231 | 70.95 | +1.08% | 2.50x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | USELESS/USD | 0.10084 | 59.10 | +0.70% | 0.57x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 4 | STABLE/USD | 0.02323 | 53.15 | -1.06% | 0.33x | WEAK 22/100 | EXTREME 100/100 | Do nothing |
| 5 | VVV/USD | 21.345 | 50.59 | +1.49% | 0.71x | MODERATE 45/100 | VERY_HIGH 82/100 | Watch |
| 6 | CC/USD | 0.0833 | 48.91 | -0.06% | 1.42x | WEAK 44/100 | HIGH 66/100 | Watch |
| 7 | SENT/USD | 0.01941 | 48.25 | -0.36% | 0.54x | WEAK 29/100 | EXTREME 88/100 | Do nothing |
| 8 | TRX/USD | 0.309578 | 42.03 | +0.13% | 0.71x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 9 | CAP/USD | 0.101555 | 25.87 | +0.33% | 0.08x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04633 | 83.14 | +0.39% | 2.00x | 15915 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5229 | 64.80 | +1.08% | 2.50x | 4561 | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 3 | XRP/USD | 0.9851 | 58.63 | +0.21% | 1.77x | 35846 | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | ME/USD | 0.0401 | 58.12 | +0.25% | 1.34x | 1015 | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** NIGHT/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
