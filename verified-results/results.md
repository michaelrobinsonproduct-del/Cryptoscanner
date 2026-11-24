# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T16:22:13.129123+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45435802562
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6533e17c3452287df0bfd9ca5de7b3cc65389fc5 (atomic ledger/results publication)
**Ledger generation:** 1597 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.609e-05 | 62.720 | 68.155 | +6.03% | +0.33% | 0.29x | 10.8 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | GBP/USD | 1.31138 | 62.321 | 59.252 | +0.62% | +0.07% | 1.27x | 0.2 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | MODERATE 56/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 494.33 | 60.528 | 60.791 | +1.71% | +0.10% | 0.92x | 12.4 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 4 | VVV/USD | 24.694 | 51.051 | 57.986 | +1.01% | +0.16% | 0.23x | 8.1 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.3217 | 48.042 | 49.138 | +4.08% | +1.23% | 0.28x | 24.9 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | WEAK 44/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01592 | 36.305 | 39.677 | +1.73% | -0.25% | 0.79x | 6.3 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66483 | 23.123 | 27.590 | +0.34% | +0.02% | 0.54x | 33.4 | 2026-11-24T16:22:09.713516+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 68.155 | 4.609e-05 | +0.33% | 0.29x |
| 2 | XMR/USD | 60.791 | 494.33 | +0.10% | 0.92x |
| 3 | GBP/USD | 59.252 | 1.31138 | +0.07% | 1.27x |
| 4 | VVV/USD | 57.986 | 24.694 | +0.16% | 0.23x |
| 5 | ICNT/USD | 49.138 | 0.3217 | +1.23% | 0.28x |
| 6 | 2Z/USD | 39.677 | 0.01592 | -0.25% | 0.79x |
| 7 | AUD/USD | 27.590 | 0.66483 | +0.02% | 0.54x |

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

- Persisted scans: 1597; predictions: 13738; observations: 967665.
- Matured sampled outcomes across 1/6/24/48h: 27376; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45435802562 · **Generation:** 1597 · **Legacy run:** 45435802562
**Main quote time:** 2026-11-24T16:22:13.129123+00:00 · **Legacy report time:** 2026-11-24T16:23:06.772269+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.609e-05 | 62.72 | +0.33% | 0.29x | MODERATE 56/100 | EXTREME 88/100 | Do nothing |
| 2 | GBP/USD ⭐ | 1.31138 | 62.32 | +0.07% | 1.27x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD | 494.33 | 60.53 | +0.10% | 0.92x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 4 | VVV/USD | 24.694 | 51.05 | +0.16% | 0.23x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 5 | ICNT/USD | 0.3217 | 48.04 | +1.23% | 0.28x | WEAK 44/100 | EXTREME 87/100 | Do nothing |
| 6 | 2Z/USD | 0.01592 | 36.30 | -0.25% | 0.79x | WEAK 23/100 | VERY_HIGH 80/100 | Do nothing |
| 7 | AUD/USD | 0.66483 | 23.12 | +0.02% | 0.54x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD ⭐ | 1.31134 | 60.59 | +0.07% | 1.27x | 20378 | MODERATE 65/100 | HIGH 55/100 | Watch |

**Same-run overlap:** GBP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
