# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T01:43:11.611604+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45306658643
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a989de3360607b8ec395a5f344ea8200fc6242b3 (atomic ledger/results publication)
**Ledger generation:** 1508 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.95219 | 79.827 | 64.433 | +1.36% | +0.08% | 6.25x | 0.2 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XLM/USD | 0.131786 | 76.340 | 62.449 | +1.38% | -0.22% | 2.51x | 4.4 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XBT/USD | 61411.8 | 71.927 | 57.422 | +0.35% | -0.10% | 3.37x | 0.0 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PAXG/USD | 3661.69 | 65.690 | 55.758 | +1.12% | +0.19% | 1.90x | 0.7 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 5 | UNI/USD | 4.9233 | 59.148 | 60.747 | +1.76% | +0.03% | 0.82x | 5.7 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SOL/USD | 72.44 | 57.826 | 59.273 | +0.71% | -0.17% | 0.94x | 1.4 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | XDG/USD | 0.0570204 | 57.785 | 63.884 | +1.27% | -0.07% | 0.42x | 0.0 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ZEC/USD | 784.47 | 57.051 | 61.896 | +1.20% | -0.18% | 0.61x | 3.1 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | PEPE/USD | 3.498e-06 | 56.566 | 60.781 | +2.22% | -0.09% | 0.62x | 5.7 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HYPE/USD | 64.26 | 56.332 | 61.042 | +0.97% | +0.03% | 0.51x | 1.6 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.150359 | 56.242 | 62.387 | +1.29% | +0.00% | 0.38x | 3.3 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | VVV/USD | 24.831 | 55.769 | 62.540 | +1.57% | -0.38% | 0.51x | 6.9 | 2026-11-24T01:43:03.787304+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 64.433 | 0.95219 | +0.08% | 6.25x |
| 2 | XDG/USD | 63.884 | 0.0570204 | -0.07% | 0.42x |
| 3 | VVV/USD | 62.540 | 24.831 | -0.38% | 0.51x |
| 4 | XLM/USD | 62.449 | 0.131786 | -0.22% | 2.51x |
| 5 | ADA/USD | 62.387 | 0.150359 | +0.00% | 0.38x |
| 6 | ZEC/USD | 61.896 | 784.47 | -0.18% | 0.61x |
| 7 | HYPE/USD | 61.042 | 64.26 | +0.03% | 0.51x |
| 8 | PEPE/USD | 60.781 | 3.498e-06 | -0.09% | 0.62x |
| 9 | UNI/USD | 60.747 | 4.9233 | +0.03% | 0.82x |
| 10 | SOL/USD | 59.273 | 72.44 | -0.17% | 0.94x |
| 11 | XBT/USD | 57.422 | 61411.8 | -0.10% | 3.37x |
| 12 | PAXG/USD | 55.758 | 3661.69 | +0.19% | 1.90x |

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

- Persisted scans: 1508; predictions: 12853; observations: 913473.
- Matured sampled outcomes across 1/6/24/48h: 23702; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 134 (sampled only; not a success-rate estimate).
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

**Writer:** 45306658643 · **Generation:** 1508 · **Legacy run:** 45306658643
**Main quote time:** 2026-11-24T01:43:11.611604+00:00 · **Legacy report time:** 2026-11-24T01:44:18.096757+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95219 | 79.83 | +0.08% | 6.25x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | XLM/USD | 0.131786 | 76.34 | -0.22% | 2.51x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | XBT/USD | 61411.8 | 71.93 | -0.10% | 3.37x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | PAXG/USD ⭐ | 3661.69 | 65.69 | +0.19% | 1.90x | STRONG 78/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.9233 | 59.15 | +0.03% | 0.82x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 6 | SOL/USD | 72.44 | 57.83 | -0.17% | 0.94x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 7 | XDG/USD | 0.0570204 | 57.79 | -0.07% | 0.42x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ZEC/USD | 784.47 | 57.05 | -0.18% | 0.61x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | PEPE/USD | 3.498e-06 | 56.57 | -0.09% | 0.62x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HYPE/USD | 64.26 | 56.33 | +0.03% | 0.51x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD | 0.150359 | 56.24 | +0.00% | 0.38x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | VVV/USD | 24.831 | 55.77 | -0.38% | 0.51x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95197 | 76.10 | +0.08% | 6.25x | 45112 | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | PAXG/USD ⭐ | 3663.45 | 64.09 | +0.19% | 1.90x | 5836 | STRONG 77/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
