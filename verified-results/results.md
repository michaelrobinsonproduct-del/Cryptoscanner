# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:35:11.939016+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44315102803
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 076f28abaca53a104840a447e619929e8cfd8190 (atomic ledger/results publication)
**Ledger generation:** 578 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.445 | 71.329 | 53.986 | +1.99% | +0.47% | 4.56x | 16.8 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.5237 | 64.017 | 48.443 | +2.83% | +0.11% | 5.50x | 7.6 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04646 | 60.053 | 66.517 | +3.50% | +0.00% | 0.35x | 12.9 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XRP/USD | 0.98701 | 58.743 | 58.141 | +0.46% | +0.22% | 0.95x | 0.1 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | CC/USD | 0.08348 | 49.929 | 44.014 | +1.64% | +0.22% | 1.48x | 6.0 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.10086 | 45.777 | 53.061 | +3.36% | +0.02% | 0.26x | 24.8 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 7 | SENT/USD | 0.019285 | 44.745 | 50.756 | +3.30% | -0.56% | 0.68x | 6.7 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.309649 | 41.456 | 45.467 | +0.57% | +0.02% | 0.59x | 0.0 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XPL/USD | 0.0475 | 38.469 | 38.711 | +2.37% | +0.42% | 0.76x | 21.1 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | CAP/USD | 0.101737 | 35.841 | 33.574 | +0.76% | +0.18% | 1.14x | 6.1 | 2026-11-18T13:35:05.277390+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 66.517 | 0.04646 | +0.00% | 0.35x |
| 2 | XRP/USD | 58.141 | 0.98701 | +0.22% | 0.95x |
| 3 | VVV/USD | 53.986 | 21.445 | +0.47% | 4.56x |
| 4 | USELESS/USD | 53.061 | 0.10086 | +0.02% | 0.26x |
| 5 | SENT/USD | 50.756 | 0.019285 | -0.56% | 0.68x |
| 6 | AKT/USD | 48.443 | 0.5237 | +0.11% | 5.50x |
| 7 | TRX/USD | 45.467 | 0.309649 | +0.02% | 0.59x |
| 8 | CC/USD | 44.014 | 0.08348 | +0.22% | 1.48x |
| 9 | XPL/USD | 38.711 | 0.0475 | +0.42% | 0.76x |
| 10 | CAP/USD | 33.574 | 0.101737 | +0.18% | 1.14x |

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

- Persisted scans: 578; predictions: 4892; observations: 349009.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13050. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44315102803 · **Generation:** 578 · **Legacy run:** 44315102803
**Main quote time:** 2026-11-18T13:35:11.939016+00:00 · **Legacy report time:** 2026-11-18T13:35:34.846244+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.445 | 71.33 | +0.47% | 4.56x | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5237 | 64.02 | +0.11% | 5.50x | STRONG 87/100 | HIGH 60/100 | Watch |
| 3 | NIGHT/USD | 0.04646 | 60.05 | +0.00% | 0.35x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 4 | XRP/USD | 0.98701 | 58.74 | +0.22% | 0.95x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 5 | CC/USD | 0.08348 | 49.93 | +0.22% | 1.48x | STRONG 70/100 | HIGH 60/100 | Watch |
| 6 | USELESS/USD | 0.10086 | 45.78 | +0.02% | 0.26x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 7 | SENT/USD | 0.019285 | 44.75 | -0.56% | 0.68x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 8 | TRX/USD | 0.309649 | 41.46 | +0.02% | 0.59x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 9 | XPL/USD | 0.0475 | 38.47 | +0.42% | 0.76x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 10 | CAP/USD | 0.101737 | 35.84 | +0.18% | 1.14x | WEAK 43/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5238 | 73.36 | +0.11% | 5.50x | 4584 | STRONG 92/100 | HIGH 60/100 | Watch |
| 2 | VVV/USD ⭐ | 21.404 | 64.03 | +0.47% | 4.56x | 7059 | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 3 | AKE/USD | 0.01021753 | 55.12 | +0.62% | 1.27x | 3129 | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
