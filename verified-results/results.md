# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T14:12:29.196609+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46013375295
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fd4b4615cbbabdfbb9d9103c21dc49a1f885b1e5 (atomic ledger/results publication)
**Ledger generation:** 2018 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 604; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 752.77 | 111.604 | 98.605 | +10.43% | -0.40% | 4.59x | 2.8 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UNI/USD | 4.9107 | 98.045 | 82.587 | +5.60% | +0.09% | 2.53x | 4.5 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 66.03 | 92.295 | 96.350 | +6.12% | -0.44% | 0.81x | 3.0 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0588446 | 92.151 | 77.105 | +4.38% | +0.01% | 2.73x | 0.7 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 27.37 | 80.633 | 80.730 | +4.53% | -0.40% | 1.19x | 5.8 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 6 | INJ/USD | 6.481 | 80.017 | 71.478 | +4.67% | -0.20% | 1.95x | 4.6 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ETH/USD | 1721.36 | 69.343 | 68.940 | +2.00% | -0.28% | 1.18x | 0.1 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.96522 | 69.010 | 71.632 | +2.38% | -0.38% | 0.93x | 0.1 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | VIRTUAL/USD | 0.3856 | 68.560 | 70.283 | +5.82% | -0.08% | 0.87x | 5.2 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | SOL/USD | 73.08 | 65.941 | 75.432 | +3.02% | -0.42% | 0.26x | 1.4 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6853 | 64.983 | 72.107 | +2.64% | -0.39% | 0.48x | 1.5 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.616e-06 | 64.293 | 70.372 | +3.97% | -0.36% | 0.57x | 2.8 | 2026-11-27T14:12:21.432381+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.605 | 752.77 | -0.40% | 4.59x |
| 2 | HYPE/USD | 96.350 | 66.03 | -0.44% | 0.81x |
| 3 | UNI/USD | 82.587 | 4.9107 | +0.09% | 2.53x |
| 4 | VVV/USD | 80.730 | 27.37 | -0.40% | 1.19x |
| 5 | XDG/USD | 77.105 | 0.0588446 | +0.01% | 2.73x |
| 6 | SOL/USD | 75.432 | 73.08 | -0.42% | 0.26x |
| 7 | SUI/USD | 72.107 | 0.6853 | -0.39% | 0.48x |
| 8 | XRP/USD | 71.632 | 0.96522 | -0.38% | 0.93x |
| 9 | INJ/USD | 71.478 | 6.481 | -0.20% | 1.95x |
| 10 | PEPE/USD | 70.372 | 3.616e-06 | -0.36% | 0.57x |
| 11 | VIRTUAL/USD | 70.283 | 0.3856 | -0.08% | 0.87x |
| 12 | ETH/USD | 68.940 | 1721.36 | -0.28% | 1.18x |

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

- Persisted scans: 2018; predictions: 17918; observations: 1222004.
- Matured sampled outcomes across 1/6/24/48h: 39977; gap abstentions: 25888. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46013375295 · **Generation:** 2018 · **Legacy run:** 46013375295
**Main quote time:** 2026-11-27T14:12:29.196609+00:00 · **Legacy report time:** 2026-11-27T14:13:08.951894+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 752.77 | 111.60 | -0.40% | 4.59x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | UNI/USD ⭐ | 4.9107 | 98.05 | +0.09% | 2.53x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 66.03 | 92.30 | -0.44% | 0.81x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 4 | XDG/USD | 0.0588446 | 92.15 | +0.01% | 2.73x | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD | 27.37 | 80.63 | -0.40% | 1.19x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 6 | INJ/USD | 6.481 | 80.02 | -0.20% | 1.95x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | ETH/USD | 1721.36 | 69.34 | -0.28% | 1.18x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.96522 | 69.01 | -0.38% | 0.93x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | VIRTUAL/USD | 0.3856 | 68.56 | -0.08% | 0.87x | WEAK 39/100 | VERY_HIGH 73/100 | Watch |
| 10 | SOL/USD | 73.08 | 65.94 | -0.42% | 0.26x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 11 | SUI/USD | 0.6853 | 64.98 | -0.39% | 0.48x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | PEPE/USD | 3.616e-06 | 64.29 | -0.36% | 0.57x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.9083 | 92.59 | +0.09% | 2.53x | 7897 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
