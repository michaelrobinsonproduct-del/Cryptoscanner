# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T07:15:11.529644+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44257337844
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 26f9161a0c4386ac8d437150100aa6f36c96dab1 (atomic ledger/results publication)
**Ledger generation:** 564 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.99337 | 81.185 | 62.169 | +1.10% | +0.80% | 4.73x | 1.1 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ICNT/USD | 0.2985 | 74.514 | 65.635 | +8.11% | -1.22% | 3.25x | 26.7 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | SENT/USD | 0.019588 | 64.597 | 62.840 | +4.92% | +1.20% | 0.57x | 5.1 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | TRX/USD | 0.309473 | 59.807 | 44.109 | +0.51% | +0.14% | 2.55x | 0.0 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.9043 | 52.313 | 54.353 | +5.18% | -0.96% | 1.28x | 35.8 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5207 | 44.955 | 42.330 | +2.24% | +1.32% | 0.60x | 11.5 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | XDC/USD | 0.03088 | 37.370 | 46.554 | +1.85% | -0.19% | 0.18x | 9.7 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | TRUST/USD | 0.04785 | 35.067 | 38.463 | +1.48% | +0.61% | 0.36x | 10.5 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | MNT/USD | 0.3789 | 32.929 | 36.755 | +1.50% | +0.21% | 0.51x | 13.2 | 2026-11-18T07:15:02.746211+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 65.635 | 0.2985 | -1.22% | 3.25x |
| 2 | SENT/USD | 62.840 | 0.019588 | +1.20% | 0.57x |
| 3 | XRP/USD | 62.169 | 0.99337 | +0.80% | 4.73x |
| 4 | PEARL/USD | 54.353 | 1.9043 | -0.96% | 1.28x |
| 5 | XDC/USD | 46.554 | 0.03088 | -0.19% | 0.18x |
| 6 | TRX/USD | 44.109 | 0.309473 | +0.14% | 2.55x |
| 7 | AKT/USD | 42.330 | 0.5207 | +1.32% | 0.60x |
| 8 | TRUST/USD | 38.463 | 0.04785 | +0.61% | 0.36x |
| 9 | MNT/USD | 36.755 | 0.3789 | +0.21% | 0.51x |

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

- Persisted scans: 564; predictions: 4756; observations: 340483.
- Matured sampled outcomes across 1/6/24/48h: 4094; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44257337844 · **Generation:** 564 · **Legacy run:** 44257337844
**Main quote time:** 2026-11-18T07:15:11.529644+00:00 · **Legacy report time:** 2026-11-18T07:15:31.823103+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.99337 | 81.18 | +0.80% | 4.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ICNT/USD | 0.2985 | 74.51 | -1.22% | 3.25x | MODERATE 57/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | SENT/USD | 0.019588 | 64.60 | +1.20% | 0.57x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 4 | TRX/USD ⭐ | 0.309473 | 59.81 | +0.14% | 2.55x | STRONG 85/100 | HIGH 55/100 | Watch |
| 5 | PEARL/USD | 1.9043 | 52.31 | -0.96% | 1.28x | WEAK 21/100 | VERY_HIGH 78/100 | Do nothing |
| 6 | AKT/USD | 0.5207 | 44.95 | +1.32% | 0.60x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 7 | XDC/USD | 0.03088 | 37.37 | -0.19% | 0.18x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | TRUST/USD | 0.04785 | 35.07 | +0.61% | 0.36x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |
| 9 | MNT/USD | 0.3789 | 32.93 | +0.21% | 0.51x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.99355 | 74.46 | +0.80% | 4.73x | 32232 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TRX/USD ⭐ | 0.309701 | 56.92 | +0.14% | 2.55x | 4131 | STRONG 83/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
