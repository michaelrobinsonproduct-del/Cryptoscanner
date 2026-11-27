# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:32:23.448718+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46063980506
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a31f41d1b764381c34a7423aebd70e2cc61f2b7c (atomic ledger/results publication)
**Ledger generation:** 2057 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 741.23 | 115.926 | 99.933 | +8.74% | +0.20% | 3.03x | 0.1 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SKY/USD | 0.05048 | 93.263 | 76.647 | +8.77% | +1.39% | 1.97x | 7.9 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | STRONG 92/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 64.07 | 89.131 | 74.252 | +2.97% | +0.30% | 2.34x | 3.1 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SUI/USD | 0.6731 | 75.514 | 59.919 | +0.81% | +0.12% | 4.54x | 1.5 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05026 | 74.373 | 79.856 | +3.69% | -0.53% | 0.72x | 2.0 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8473 | 72.711 | 80.127 | +4.24% | +0.07% | 0.22x | 4.3 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | JUP/USD | 0.24858 | 65.780 | 65.171 | +5.08% | +0.01% | 1.05x | 6.8 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0576402 | 65.388 | 69.145 | +2.25% | -0.07% | 0.66x | 3.1 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 72.05 | 65.006 | 65.259 | +1.56% | +0.07% | 0.94x | 1.4 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 10 | RENDER/USD | 1.404 | 61.615 | 63.110 | +5.33% | +0.21% | 0.74x | 14.3 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | PAXG/USD | 3641.94 | 59.779 | 59.163 | +2.40% | -0.12% | 1.12x | 1.3 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 12 | ADA/USD | 0.14922 | 53.170 | 56.445 | +0.51% | +0.04% | 0.65x | 2.1 | 2026-11-27T20:32:16.742566+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.933 | 741.23 | +0.20% | 3.03x |
| 2 | UNI/USD | 80.127 | 4.8473 | +0.07% | 0.22x |
| 3 | NIGHT/USD | 79.856 | 0.05026 | -0.53% | 0.72x |
| 4 | SKY/USD | 76.647 | 0.05048 | +1.39% | 1.97x |
| 5 | HYPE/USD | 74.252 | 64.07 | +0.30% | 2.34x |
| 6 | XDG/USD | 69.145 | 0.0576402 | -0.07% | 0.66x |
| 7 | SOL/USD | 65.259 | 72.05 | +0.07% | 0.94x |
| 8 | JUP/USD | 65.171 | 0.24858 | +0.01% | 1.05x |
| 9 | RENDER/USD | 63.110 | 1.404 | +0.21% | 0.74x |
| 10 | SUI/USD | 59.919 | 0.6731 | +0.12% | 4.54x |
| 11 | PAXG/USD | 59.163 | 3641.94 | -0.12% | 1.12x |
| 12 | ADA/USD | 56.445 | 0.14922 | +0.04% | 0.65x |

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

- Persisted scans: 2057; predictions: 18386; observations: 1245594.
- Matured sampled outcomes across 1/6/24/48h: 41579; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46063980506 · **Generation:** 2057 · **Legacy run:** 46063980506
**Main quote time:** 2026-11-27T20:32:23.448718+00:00 · **Legacy report time:** 2026-11-27T20:33:08.419350+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 741.23 | 115.93 | +0.20% | 3.03x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.05048 | 93.26 | +1.39% | 1.97x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 64.07 | 89.13 | +0.30% | 2.34x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD | 0.6731 | 75.51 | +0.12% | 4.54x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.05026 | 74.37 | -0.53% | 0.72x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | UNI/USD | 4.8473 | 72.71 | +0.07% | 0.22x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | JUP/USD | 0.24858 | 65.78 | +0.01% | 1.05x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 8 | XDG/USD | 0.0576402 | 65.39 | -0.07% | 0.66x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 72.05 | 65.01 | +0.07% | 0.94x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 10 | RENDER/USD | 1.404 | 61.62 | +0.21% | 0.74x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 11 | PAXG/USD | 3641.94 | 59.78 | -0.12% | 1.12x | WEAK 40/100 | HIGH 68/100 | Watch |
| 12 | ADA/USD | 0.14922 | 53.17 | +0.04% | 0.65x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 741.77 | 100.00 | +0.20% | 3.03x | 38780 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD ⭐ | 64.06 | 90.62 | +0.30% | 2.34x | 19872 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SKY/USD ⭐ | 0.05044 | 81.39 | +1.39% | 1.97x | 6625 | STRONG 96/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, SKY/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
