# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:41:40.058399+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45342089256
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** db338568b91c287fe7c1e8ffde1e351ee8c68aa3 (atomic ledger/results publication)
**Ledger generation:** 1539 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.38 | 74.749 | 80.109 | +3.81% | -0.20% | 0.56x | 3.2 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.17 | 74.271 | 59.271 | +0.83% | +0.00% | 7.77x | 3.1 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 496.88 | 71.741 | 64.485 | +2.23% | +0.38% | 1.54x | 12.3 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 41.69 | 69.389 | 58.364 | +0.65% | -0.05% | 2.13x | 2.4 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.536e-06 | 66.082 | 72.425 | +3.33% | +0.03% | 0.35x | 2.8 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94785 | 65.339 | 61.251 | +0.90% | -0.16% | 1.49x | 0.1 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0564645 | 58.633 | 56.973 | +0.28% | +0.10% | 1.12x | 0.0 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 9.09625 | 56.901 | 61.130 | +1.01% | +0.08% | 0.54x | 1.9 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6843 | 54.903 | 43.237 | +1.30% | -0.18% | 2.25x | 1.5 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.0203 | 54.201 | 62.028 | +1.31% | +0.10% | 0.17x | 4.3 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NIGHT/USD | 0.04911 | 52.021 | 60.641 | +1.99% | -0.41% | 0.34x | 6.1 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TIA/USD | 0.3431 | 45.120 | 44.288 | +2.17% | -0.03% | 1.10x | 5.8 | 2026-11-24T06:41:31.268207+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.109 | 25.38 | -0.20% | 0.56x |
| 2 | PEPE/USD | 72.425 | 3.536e-06 | +0.03% | 0.35x |
| 3 | XMR/USD | 64.485 | 496.88 | +0.38% | 1.54x |
| 4 | NEAR/USD | 62.028 | 3.0203 | +0.10% | 0.17x |
| 5 | XRP/USD | 61.251 | 0.94785 | -0.16% | 1.49x |
| 6 | LINK/USD | 61.130 | 9.09625 | +0.08% | 0.54x |
| 7 | NIGHT/USD | 60.641 | 0.04911 | -0.41% | 0.34x |
| 8 | HYPE/USD | 59.271 | 64.17 | +0.00% | 7.77x |
| 9 | LTC/USD | 58.364 | 41.69 | -0.05% | 2.13x |
| 10 | XDG/USD | 56.973 | 0.0564645 | +0.10% | 1.12x |
| 11 | TIA/USD | 44.288 | 0.3431 | -0.03% | 1.10x |
| 12 | DOT/USD | 43.237 | 0.6843 | -0.18% | 2.25x |

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

- Persisted scans: 1539; predictions: 13201; observations: 932349.
- Matured sampled outcomes across 1/6/24/48h: 24793; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45342089256 · **Generation:** 1539 · **Legacy run:** 45342089256
**Main quote time:** 2026-11-24T06:41:40.058399+00:00 · **Legacy report time:** 2026-11-24T06:42:52.415989+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.38 | 74.75 | -0.20% | 0.56x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 2 | HYPE/USD | 64.17 | 74.27 | +0.00% | 7.77x | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 496.88 | 71.74 | +0.38% | 1.54x | STRONG 86/100 | HIGH 61/100 | Consider small entry |
| 4 | LTC/USD | 41.69 | 69.39 | -0.05% | 2.13x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | PEPE/USD | 3.536e-06 | 66.08 | +0.03% | 0.35x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.94785 | 65.34 | -0.16% | 1.49x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0564645 | 58.63 | +0.10% | 1.12x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD | 9.09625 | 56.90 | +0.08% | 0.54x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 9 | DOT/USD | 0.6843 | 54.90 | -0.18% | 2.25x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 10 | NEAR/USD | 3.0203 | 54.20 | +0.10% | 0.17x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | NIGHT/USD | 0.04911 | 52.02 | -0.41% | 0.34x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TIA/USD | 0.3431 | 45.12 | -0.03% | 1.10x | WEAK 33/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD | 0.0089 | 82.34 | +1.14% | 10.40x | 3145 | STRONG 86/100 | VERY_HIGH 79/100 | Watch |
| 2 | XMR/USD ⭐ | 495.93 | 64.75 | +0.38% | 1.54x | 11728 | STRONG 82/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
