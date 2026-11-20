# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:00:34.828451+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44642165515
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** d60e3264fc71a918172e9c3b6e248de3d986c0b3 (atomic ledger/results publication)
**Ledger generation:** 883 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002645 | 68.390 | 49.964 | +1.89% | +0.69% | 5.10x | 11.4 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05811 | 64.559 | 46.530 | +3.77% | +0.61% | 9.68x | 24.1 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | SKR/USD | 0.010053 | 57.410 | 57.252 | +4.36% | -0.34% | 1.18x | 8.9 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | INJ/USD | 7.09 | 55.907 | 53.818 | +1.56% | +0.20% | 1.11x | 5.6 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 5 | AKE/USD | 0.0105144 | 38.993 | 38.491 | +1.19% | -0.15% | 1.13x | 8.8 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | PYTH/USD | 0.05313 | 27.847 | 34.380 | +0.70% | +0.11% | 0.29x | 7.5 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing | WATCH |
| 7 | ZEREBRO/USD | 0.02199 | 25.801 | 27.168 | +0.78% | +0.09% | 0.82x | 18.2 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | CAP/USD | 0.096495 | 24.660 | 30.919 | +0.50% | +0.31% | 0.22x | 14.3 | 2026-11-20T00:00:29.539802+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKR/USD | 57.252 | 0.010053 | -0.34% | 1.18x |
| 2 | INJ/USD | 53.818 | 7.09 | +0.20% | 1.11x |
| 3 | PUMP/USD | 49.964 | 0.002645 | +0.69% | 5.10x |
| 4 | MEGA/USD | 46.530 | 0.05811 | +0.61% | 9.68x |
| 5 | AKE/USD | 38.491 | 0.0105144 | -0.15% | 1.13x |
| 6 | PYTH/USD | 34.380 | 0.05313 | +0.11% | 0.29x |
| 7 | CAP/USD | 30.919 | 0.096495 | +0.31% | 0.22x |
| 8 | ZEREBRO/USD | 27.168 | 0.02199 | +0.09% | 0.82x |

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

- Persisted scans: 883; predictions: 7699; observations: 533574.
- Matured sampled outcomes across 1/6/24/48h: 8311; gap abstentions: 15950. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44642165515 · **Generation:** 883 · **Legacy run:** 44642165515
**Main quote time:** 2026-11-20T00:00:34.828451+00:00 · **Legacy report time:** 2026-11-20T00:01:39.261132+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002645 | 68.39 | +0.69% | 5.10x | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 2 | MEGA/USD | 0.05811 | 64.56 | +0.61% | 9.68x | STRONG 77/100 | VERY_HIGH 72/100 | Watch |
| 3 | SKR/USD | 0.010053 | 57.41 | -0.34% | 1.18x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 4 | INJ/USD | 7.09 | 55.91 | +0.20% | 1.11x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 5 | AKE/USD | 0.0105144 | 38.99 | -0.15% | 1.13x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | PYTH/USD | 0.05313 | 27.85 | +0.11% | 0.29x | WEAK 34/100 | VERY_HIGH 75/100 | Do nothing |
| 7 | ZEREBRO/USD | 0.02199 | 25.80 | +0.09% | 0.82x | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | CAP/USD | 0.096495 | 24.66 | +0.31% | 0.22x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002645 | 62.16 | +0.69% | 5.10x | 3966 | STRONG 91/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
