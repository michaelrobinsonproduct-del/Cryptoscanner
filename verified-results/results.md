# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T19:52:18.415889+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46059383337
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8d0b63df9852aff9124274724e387c898487bfe6 (atomic ledger/results publication)
**Ledger generation:** 2052 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.43 | 96.406 | 97.240 | +8.91% | -0.19% | 1.01x | 5.5 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | UNI/USD | 4.8382 | 94.340 | 78.823 | +4.05% | +0.10% | 4.40x | 4.3 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05008 | 83.270 | 77.253 | +3.32% | +0.04% | 1.58x | 2.0 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ENA/USD | 0.1046 | 78.623 | 63.623 | +4.18% | +0.00% | 2.50x | 9.6 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | INJ/USD | 6.393 | 75.794 | 62.042 | +3.25% | -0.25% | 3.92x | 6.3 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SKY/USD | 0.04891 | 73.271 | 68.795 | +5.39% | +0.70% | 1.10x | 8.2 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 7 | LTC/USD | 43.94 | 65.455 | 57.063 | +0.46% | +0.14% | 1.77x | 2.3 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.057756 | 64.697 | 72.067 | +2.45% | -0.08% | 0.30x | 0.2 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | HYPE/USD | 63.83 | 63.923 | 72.330 | +2.59% | -0.22% | 0.27x | 1.6 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94804 | 62.364 | 58.717 | +0.56% | -0.26% | 1.49x | 0.4 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 11 | PAXG/USD | 3642.59 | 61.315 | 59.019 | +2.41% | +0.22% | 1.12x | 1.5 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6741 | 58.190 | 60.967 | +0.96% | -0.16% | 0.80x | 1.5 | 2026-11-27T19:52:09.663066+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.240 | 742.43 | -0.19% | 1.01x |
| 2 | UNI/USD | 78.823 | 4.8382 | +0.10% | 4.40x |
| 3 | NIGHT/USD | 77.253 | 0.05008 | +0.04% | 1.58x |
| 4 | HYPE/USD | 72.330 | 63.83 | -0.22% | 0.27x |
| 5 | XDG/USD | 72.067 | 0.057756 | -0.08% | 0.30x |
| 6 | SKY/USD | 68.795 | 0.04891 | +0.70% | 1.10x |
| 7 | ENA/USD | 63.623 | 0.1046 | +0.00% | 2.50x |
| 8 | INJ/USD | 62.042 | 6.393 | -0.25% | 3.92x |
| 9 | SUI/USD | 60.967 | 0.6741 | -0.16% | 0.80x |
| 10 | PAXG/USD | 59.019 | 3642.59 | +0.22% | 1.12x |
| 11 | XRP/USD | 58.717 | 0.94804 | -0.26% | 1.49x |
| 12 | LTC/USD | 57.063 | 43.94 | +0.14% | 1.77x |

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

- Persisted scans: 2052; predictions: 18326; observations: 1242569.
- Matured sampled outcomes across 1/6/24/48h: 41387; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46059383337 · **Generation:** 2052 · **Legacy run:** 46059383337
**Main quote time:** 2026-11-27T19:52:18.415889+00:00 · **Legacy report time:** 2026-11-27T19:52:54.439906+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 742.43 | 96.41 | -0.19% | 1.01x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | UNI/USD ⭐ | 4.8382 | 94.34 | +0.10% | 4.40x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD | 0.05008 | 83.27 | +0.04% | 1.58x | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | ENA/USD | 0.1046 | 78.62 | +0.00% | 2.50x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | INJ/USD | 6.393 | 75.79 | -0.25% | 3.92x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | SKY/USD ⭐ | 0.04891 | 73.27 | +0.70% | 1.10x | STRONG 82/100 | HIGH 67/100 | Watch |
| 7 | LTC/USD | 43.94 | 65.45 | +0.14% | 1.77x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD | 0.057756 | 64.70 | -0.08% | 0.30x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | HYPE/USD | 63.83 | 63.92 | -0.22% | 0.27x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.94804 | 62.36 | -0.26% | 1.49x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 11 | PAXG/USD ⭐ | 3642.59 | 61.31 | +0.22% | 1.12x | STRONG 76/100 | HIGH 62/100 | Watch |
| 12 | SUI/USD | 0.6741 | 58.19 | -0.16% | 0.80x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.8341 | 98.11 | +0.10% | 4.40x | 10107 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04895 | 78.33 | +0.70% | 1.10x | 6298 | STRONG 84/100 | HIGH 67/100 | Watch |
| 3 | PAXG/USD ⭐ | 3643.22 | 72.97 | +0.22% | 1.12x | 4778 | STRONG 81/100 | HIGH 62/100 | Watch |

**Same-run overlap:** UNI/USD, SKY/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
