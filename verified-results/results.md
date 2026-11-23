# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T17:02:32.535509+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45222667766
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 129c6caef595ce933be950d08182a9bb0d67a029 (atomic ledger/results publication)
**Ledger generation:** 1457 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.7004 | 115.213 | 98.571 | +6.82% | +0.33% | 3.09x | 2.9 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 5.0323 | 114.093 | 94.199 | +7.50% | +0.98% | 7.05x | 3.8 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SOL/USD | 74.36 | 108.180 | 91.295 | +5.28% | +0.38% | 3.30x | 1.3 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | INJ/USD | 6.79 | 106.683 | 94.878 | +9.02% | +1.35% | 1.50x | 5.9 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | LINK/USD | 9.2019 | 103.419 | 85.082 | +4.43% | +0.67% | 9.40x | 1.9 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | NEAR/USD | 3.1206 | 99.106 | 86.002 | +4.66% | +0.84% | 1.89x | 3.2 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XRP/USD | 0.97062 | 98.909 | 87.357 | +4.64% | +0.00% | 2.15x | 0.3 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0580429 | 96.240 | 89.694 | +4.99% | +0.44% | 1.43x | 0.5 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ZEC/USD | 841.56 | 96.234 | 90.390 | +5.52% | +0.79% | 1.19x | 6.5 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 83/100 | HIGH 62/100 | Watch | WATCH |
| 10 | HYPE/USD | 65.83 | 93.892 | 84.989 | +4.39% | +1.13% | 1.32x | 1.5 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ADA/USD | 0.152723 | 92.927 | 92.409 | +5.62% | +0.45% | 0.83x | 3.8 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 12 | LTC/USD | 42.39 | 87.522 | 91.508 | +5.55% | -0.02% | 0.61x | 4.7 | 2026-11-23T17:02:23.994130+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SUI/USD | 98.571 | 0.7004 | +0.33% | 3.09x |
| 2 | INJ/USD | 94.878 | 6.79 | +1.35% | 1.50x |
| 3 | UNI/USD | 94.199 | 5.0323 | +0.98% | 7.05x |
| 4 | ADA/USD | 92.409 | 0.152723 | +0.45% | 0.83x |
| 5 | LTC/USD | 91.508 | 42.39 | -0.02% | 0.61x |
| 6 | SOL/USD | 91.295 | 74.36 | +0.38% | 3.30x |
| 7 | ZEC/USD | 90.390 | 841.56 | +0.79% | 1.19x |
| 8 | XDG/USD | 89.694 | 0.0580429 | +0.44% | 1.43x |
| 9 | XRP/USD | 87.357 | 0.97062 | +0.00% | 2.15x |
| 10 | NEAR/USD | 86.002 | 3.1206 | +0.84% | 1.89x |
| 11 | LINK/USD | 85.082 | 9.2019 | +0.67% | 9.40x |
| 12 | HYPE/USD | 84.989 | 65.83 | +1.13% | 1.32x |

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

- Persisted scans: 1457; predictions: 12251; observations: 882415.
- Matured sampled outcomes across 1/6/24/48h: 21244; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45222667766 · **Generation:** 1457 · **Legacy run:** 45222667766
**Main quote time:** 2026-11-23T17:02:32.535509+00:00 · **Legacy report time:** 2026-11-23T17:03:23.707677+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD ⭐ | 0.7004 | 115.21 | +0.33% | 3.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 5.0323 | 114.09 | +0.98% | 7.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 74.36 | 108.18 | +0.38% | 3.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | INJ/USD ⭐ | 6.79 | 106.68 | +1.35% | 1.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 9.2019 | 103.42 | +0.67% | 9.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | NEAR/USD ⭐ | 3.1206 | 99.11 | +0.84% | 1.89x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD | 0.97062 | 98.91 | +0.00% | 2.15x | STRONG 94/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD ⭐ | 0.0580429 | 96.24 | +0.44% | 1.43x | STRONG 100/100 | HIGH 55/100 | Watch |
| 9 | ZEC/USD ⭐ | 841.56 | 96.23 | +0.79% | 1.19x | STRONG 93/100 | HIGH 62/100 | Watch |
| 10 | HYPE/USD ⭐ | 65.83 | 93.89 | +1.13% | 1.32x | STRONG 100/100 | HIGH 55/100 | Watch |
| 11 | ADA/USD | 0.152723 | 92.93 | +0.45% | 0.83x | STRONG 76/100 | HIGH 62/100 | Watch |
| 12 | LTC/USD | 42.39 | 87.52 | -0.02% | 0.61x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.77 | 100.00 | +1.13% | 1.32x | 20367 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 9.20375 | 100.00 | +0.67% | 9.40x | 7571 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.1083 | 100.00 | +0.84% | 1.89x | 18400 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 74.32 | 100.00 | +0.38% | 3.30x | 42855 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SUI/USD ⭐ | 0.7 | 100.00 | +0.33% | 3.09x | 10786 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XDG/USD ⭐ | 0.0579492 | 100.00 | +0.44% | 1.43x | 9185 | STRONG 100/100 | HIGH 55/100 | Watch |
| 7 | UNI/USD ⭐ | 5.0323 | 99.03 | +0.98% | 7.05x | 8873 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | QNT/USD | 160.71 | 98.31 | +0.48% | 1.15x | 10648 | STRONG 84/100 | HIGH 62/100 | Watch |
| 9 | INJ/USD ⭐ | 6.786 | 95.92 | +1.35% | 1.50x | 8143 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | XLM/USD | 0.132975 | 94.64 | +0.31% | 1.34x | 17967 | STRONG 92/100 | HIGH 55/100 | Watch |
| 11 | AVAX/USD | 6.944 | 91.27 | +0.23% | 1.90x | 4788 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 12 | ZEC/USD ⭐ | 837.78 | 90.96 | +0.79% | 1.19x | 31482 | STRONG 90/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SUI/USD, UNI/USD, SOL/USD, INJ/USD, LINK/USD, NEAR/USD, XDG/USD, ZEC/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
