# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T23:01:45.405815+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45284801818
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1af80c096f1aec59297922fcb6c4d3c3c650bb55 (atomic ledger/results publication)
**Ledger generation:** 1493 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.42 | 102.996 | 97.126 | +9.05% | +0.43% | 1.37x | 5.7 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08089 | 98.143 | 91.195 | +7.24% | +0.14% | 1.63x | 7.4 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0562499 | 82.564 | 67.144 | +1.75% | +0.08% | 6.14x | 0.2 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ATOM/USD | 1.2697 | 81.438 | 72.245 | +8.34% | +0.90% | 1.47x | 11.8 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Watch | WATCH |
| 5 | SOL/USD | 72.05 | 74.570 | 68.379 | +2.01% | -0.11% | 1.67x | 1.4 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LTC/USD | 41.25 | 73.142 | 72.786 | +2.71% | +0.29% | 0.89x | 2.4 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | CAP/USD | 0.102293 | 70.965 | 76.104 | +9.32% | +0.48% | 0.24x | 6.2 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | PEARL/USD | 2.2819 | 70.108 | 90.359 | +11.07% | -3.13% | 0.54x | 19.3 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | WEAK 35/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6696 | 66.857 | 69.092 | +2.12% | +0.33% | 0.61x | 1.5 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SHX/USD | 0.003594 | 64.739 | 72.172 | +6.49% | -0.50% | 0.51x | 8.3 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | TRX/USD | 0.309305 | 61.383 | 50.443 | +1.35% | +0.05% | 2.07x | 1.0 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XRP/USD | 0.93922 | 59.234 | 63.761 | +1.26% | +0.19% | 0.45x | 0.1 | 2026-11-23T23:01:38.607590+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.126 | 156.42 | +0.43% | 1.37x |
| 2 | ALGO/USD | 91.195 | 0.08089 | +0.14% | 1.63x |
| 3 | PEARL/USD | 90.359 | 2.2819 | -3.13% | 0.54x |
| 4 | CAP/USD | 76.104 | 0.102293 | +0.48% | 0.24x |
| 5 | LTC/USD | 72.786 | 41.25 | +0.29% | 0.89x |
| 6 | ATOM/USD | 72.245 | 1.2697 | +0.90% | 1.47x |
| 7 | SHX/USD | 72.172 | 0.003594 | -0.50% | 0.51x |
| 8 | SUI/USD | 69.092 | 0.6696 | +0.33% | 0.61x |
| 9 | SOL/USD | 68.379 | 72.05 | -0.11% | 1.67x |
| 10 | XDG/USD | 67.144 | 0.0562499 | +0.08% | 6.14x |
| 11 | XRP/USD | 63.761 | 0.93922 | +0.19% | 0.45x |
| 12 | TRX/USD | 50.443 | 0.309305 | +0.05% | 2.07x |

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

- Persisted scans: 1493; predictions: 12683; observations: 904339.
- Matured sampled outcomes across 1/6/24/48h: 23032; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45284801818 · **Generation:** 1493 · **Legacy run:** 45284801818
**Main quote time:** 2026-11-23T23:01:45.405815+00:00 · **Legacy report time:** 2026-11-23T23:02:55.369828+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.42 | 103.00 | +0.43% | 1.37x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ALGO/USD ⭐ | 0.08089 | 98.14 | +0.14% | 1.63x | STRONG 94/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0562499 | 82.56 | +0.08% | 6.14x | STRONG 96/100 | HIGH 55/100 | Watch |
| 4 | ATOM/USD ⭐ | 1.2697 | 81.44 | +0.90% | 1.47x | STRONG 91/100 | HIGH 66/100 | Watch |
| 5 | SOL/USD | 72.05 | 74.57 | -0.11% | 1.67x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | LTC/USD | 41.25 | 73.14 | +0.29% | 0.89x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | CAP/USD | 0.102293 | 70.97 | +0.48% | 0.24x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 8 | PEARL/USD | 2.2819 | 70.11 | -3.13% | 0.54x | WEAK 35/100 | EXTREME 86/100 | Do nothing |
| 9 | SUI/USD | 0.6696 | 66.86 | +0.33% | 0.61x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | SHX/USD | 0.003594 | 64.74 | -0.50% | 0.51x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 11 | TRX/USD | 0.309305 | 61.38 | +0.05% | 2.07x | STRONG 76/100 | HIGH 55/100 | Watch |
| 12 | XRP/USD | 0.93922 | 59.23 | +0.19% | 0.45x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.34 | 91.28 | +0.43% | 1.37x | 12409 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ALGO/USD ⭐ | 0.08089 | 87.53 | +0.14% | 1.63x | 10106 | STRONG 89/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0561927 | 79.52 | +0.08% | 6.14x | 10262 | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | ATOM/USD ⭐ | 1.2676 | 76.47 | +0.90% | 1.47x | 3710 | STRONG 88/100 | HIGH 66/100 | Watch |

**Same-run overlap:** QNT/USD, ALGO/USD, XDG/USD, ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
