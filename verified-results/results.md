# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:12:40.762683+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46096670917
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3750eb250e1d8f42312626f4fe729741658a252e (atomic ledger/results publication)
**Ledger generation:** 2091 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0541 | 74.634 | 63.163 | +1.19% | -0.06% | 2.18x | 0.3 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 755.94 | 65.335 | 72.521 | +2.91% | -0.35% | 0.45x | 5.7 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XBT/USD | 60139 | 64.009 | 58.210 | +0.46% | -0.00% | 1.58x | 0.0 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 26.016 | 61.300 | 50.964 | +1.04% | +1.26% | 1.40x | 6.9 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1668.85 | 61.119 | 57.867 | +0.48% | -0.01% | 1.33x | 1.0 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XMR/USD | 410.35 | 59.664 | 55.908 | +0.76% | +0.85% | 0.95x | 8.8 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 7 | HYPE/USD | 64.55 | 58.895 | 65.138 | +1.67% | -0.17% | 0.46x | 3.1 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | XRP/USD | 0.95433 | 54.778 | 59.584 | +0.66% | +0.06% | 0.49x | 0.1 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0580213 | 52.949 | 59.012 | +0.61% | +0.02% | 0.38x | 0.5 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | QNT/USD | 146.77 | 52.806 | 38.690 | +0.33% | -0.18% | 6.11x | 6.1 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SOL/USD | 72.12 | 52.217 | 58.697 | +0.73% | -0.07% | 0.39x | 2.8 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TAO/USD | 188.7584 | 51.260 | 57.169 | +0.97% | -0.22% | 0.52x | 9.2 | 2026-11-28T02:12:32.302413+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 72.521 | 755.94 | -0.35% | 0.45x |
| 2 | HYPE/USD | 65.138 | 64.55 | -0.17% | 0.46x |
| 3 | NEAR/USD | 63.163 | 3.0541 | -0.06% | 2.18x |
| 4 | XRP/USD | 59.584 | 0.95433 | +0.06% | 0.49x |
| 5 | XDG/USD | 59.012 | 0.0580213 | +0.02% | 0.38x |
| 6 | SOL/USD | 58.697 | 72.12 | -0.07% | 0.39x |
| 7 | XBT/USD | 58.210 | 60139 | -0.00% | 1.58x |
| 8 | ETH/USD | 57.867 | 1668.85 | -0.01% | 1.33x |
| 9 | TAO/USD | 57.169 | 188.7584 | -0.22% | 0.52x |
| 10 | XMR/USD | 55.908 | 410.35 | +0.85% | 0.95x |
| 11 | VVV/USD | 50.964 | 26.016 | +1.26% | 1.40x |
| 12 | QNT/USD | 38.690 | 146.77 | -0.18% | 6.11x |

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

- Persisted scans: 2091; predictions: 18755; observations: 1266192.
- Matured sampled outcomes across 1/6/24/48h: 43181; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46096670917 · **Generation:** 2091 · **Legacy run:** 46096670917
**Main quote time:** 2026-11-28T02:12:40.762683+00:00 · **Legacy report time:** 2026-11-28T02:13:21.458118+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0541 | 74.63 | -0.06% | 2.18x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 755.94 | 65.34 | -0.35% | 0.45x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 3 | XBT/USD | 60139 | 64.01 | -0.00% | 1.58x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 26.016 | 61.30 | +1.26% | 1.40x | STRONG 76/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1668.85 | 61.12 | -0.01% | 1.33x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 6 | XMR/USD | 410.35 | 59.66 | +0.85% | 0.95x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 7 | HYPE/USD | 64.55 | 58.89 | -0.17% | 0.46x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | XRP/USD | 0.95433 | 54.78 | +0.06% | 0.49x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | XDG/USD | 0.0580213 | 52.95 | +0.02% | 0.38x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 10 | QNT/USD | 146.77 | 52.81 | -0.18% | 6.11x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 11 | SOL/USD | 72.12 | 52.22 | -0.07% | 0.39x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TAO/USD | 188.7584 | 51.26 | -0.22% | 0.52x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
