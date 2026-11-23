# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T19:01:53.641367+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45244180953
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cc2209971b1343ca6eb01b3073d68866ef034259 (atomic ledger/results publication)
**Ledger generation:** 1469 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.9232 | 99.672 | 84.225 | +5.17% | +0.09% | 5.13x | 7.5 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SOL/USD | 73.29 | 94.725 | 80.681 | +3.77% | -0.19% | 2.71x | 1.4 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 509.8 | 92.171 | 76.538 | +3.26% | +0.52% | 2.30x | 2.6 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | INJ/USD | 6.597 | 88.182 | 91.445 | +5.92% | +0.05% | 0.65x | 6.0 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.08403 | 80.912 | 87.978 | +11.40% | -0.15% | 0.37x | 5.9 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0572179 | 80.527 | 78.554 | +3.50% | -0.03% | 1.21x | 1.9 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 7 | LTC/USD | 41.81 | 79.671 | 82.563 | +4.11% | -0.50% | 0.96x | 2.4 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HYPE/USD | 65.39 | 79.359 | 80.099 | +3.69% | +0.12% | 0.86x | 1.5 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PAXG/USD | 3637.14 | 78.912 | 63.982 | +1.82% | -0.01% | 3.20x | 0.9 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XRP/USD | 0.9511 | 75.036 | 72.307 | +2.54% | +0.07% | 1.24x | 0.9 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 11 | CC/USD | 0.07811 | 74.792 | 80.255 | +6.61% | +0.10% | 0.40x | 2.6 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | ADA/USD | 0.150043 | 74.503 | 80.601 | +3.76% | -0.26% | 0.52x | 1.5 | 2026-11-23T19:01:44.870507+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 91.445 | 6.597 | +0.05% | 0.65x |
| 2 | ALGO/USD | 87.978 | 0.08403 | -0.15% | 0.37x |
| 3 | UNI/USD | 84.225 | 4.9232 | +0.09% | 5.13x |
| 4 | LTC/USD | 82.563 | 41.81 | -0.50% | 0.96x |
| 5 | SOL/USD | 80.681 | 73.29 | -0.19% | 2.71x |
| 6 | ADA/USD | 80.601 | 0.150043 | -0.26% | 0.52x |
| 7 | CC/USD | 80.255 | 0.07811 | +0.10% | 0.40x |
| 8 | HYPE/USD | 80.099 | 65.39 | +0.12% | 0.86x |
| 9 | XDG/USD | 78.554 | 0.0572179 | -0.03% | 1.21x |
| 10 | XMR/USD | 76.538 | 509.8 | +0.52% | 2.30x |
| 11 | XRP/USD | 72.307 | 0.9511 | +0.07% | 1.24x |
| 12 | PAXG/USD | 63.982 | 3637.14 | -0.01% | 3.20x |

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

- Persisted scans: 1469; predictions: 12395; observations: 889723.
- Matured sampled outcomes across 1/6/24/48h: 21856; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45244180953 · **Generation:** 1469 · **Legacy run:** 45244180953
**Main quote time:** 2026-11-23T19:01:53.641367+00:00 · **Legacy report time:** 2026-11-23T19:02:49.850853+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.9232 | 99.67 | +0.09% | 5.13x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD | 73.29 | 94.73 | -0.19% | 2.71x | STRONG 77/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD ⭐ | 509.8 | 92.17 | +0.52% | 2.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | INJ/USD | 6.597 | 88.18 | +0.05% | 0.65x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 5 | ALGO/USD | 0.08403 | 80.91 | -0.15% | 0.37x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 6 | XDG/USD | 0.0572179 | 80.53 | -0.03% | 1.21x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 7 | LTC/USD | 41.81 | 79.67 | -0.50% | 0.96x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 8 | HYPE/USD | 65.39 | 79.36 | +0.12% | 0.86x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 9 | PAXG/USD | 3637.14 | 78.91 | -0.01% | 3.20x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 10 | XRP/USD ⭐ | 0.9511 | 75.04 | +0.07% | 1.24x | STRONG 73/100 | HIGH 62/100 | Watch |
| 11 | CC/USD | 0.07811 | 74.79 | +0.10% | 0.40x | MODERATE 57/100 | VERY_HIGH 75/100 | Watch |
| 12 | ADA/USD | 0.150043 | 74.50 | -0.26% | 0.52x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.9232 | 96.62 | +0.09% | 5.13x | 9259 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 510.95 | 93.62 | +0.52% | 2.30x | 10016 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95184 | 82.29 | +0.07% | 1.24x | 39732 | STRONG 76/100 | HIGH 62/100 | Watch |

**Same-run overlap:** UNI/USD, XMR/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
