# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:00:10.255693+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44309204850
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 8ed3bf4465a4e40f0e6a4f42c51f7f0b0463acc3 (atomic ledger/results publication)
**Ledger generation:** 571 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04635 | 73.553 | 68.337 | +3.25% | +0.48% | 1.28x | 6.5 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MNT/USD | 0.3854 | 63.001 | 49.269 | +3.24% | -0.05% | 2.40x | 13.0 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | USELESS/USD | 0.10001 | 60.646 | 55.805 | +2.49% | +0.19% | 1.39x | 7.0 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SENT/USD | 0.01956 | 59.206 | 61.130 | +4.77% | -0.22% | 0.92x | 6.6 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 5 | STABLE/USD | 0.02326 | 58.174 | 63.061 | +10.50% | +0.56% | 0.23x | 25.8 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.08327 | 46.407 | 42.150 | +1.39% | +0.33% | 1.26x | 7.2 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | MODERATE 58/100 | HIGH 60/100 | Watch | WATCH |
| 7 | AKT/USD | 0.5172 | 45.179 | 37.510 | +1.55% | +0.04% | 1.75x | 11.6 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 8 | ME/USD | 0.0402 | 42.870 | 48.084 | +4.15% | -0.25% | 0.60x | 24.9 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | WEAK 16/100 | EXTREME 100/100 | Do nothing | WATCH |
| 9 | VVV/USD | 21.1 | 38.436 | 45.574 | +0.35% | -0.12% | 0.35x | 10.0 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | TRX/USD | 0.309406 | 37.656 | 44.791 | +0.49% | -0.06% | 0.31x | 0.0 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | CAP/USD | 0.101568 | 24.032 | 30.622 | +0.59% | -0.20% | 0.44x | 9.7 | 2026-11-18T13:00:03.161207+00:00 | Not calibrated | WEAK 17/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 68.337 | 0.04635 | +0.48% | 1.28x |
| 2 | STABLE/USD | 63.061 | 0.02326 | +0.56% | 0.23x |
| 3 | SENT/USD | 61.130 | 0.01956 | -0.22% | 0.92x |
| 4 | USELESS/USD | 55.805 | 0.10001 | +0.19% | 1.39x |
| 5 | MNT/USD | 49.269 | 0.3854 | -0.05% | 2.40x |
| 6 | ME/USD | 48.084 | 0.0402 | -0.25% | 0.60x |
| 7 | VVV/USD | 45.574 | 21.1 | -0.12% | 0.35x |
| 8 | TRX/USD | 44.791 | 0.309406 | -0.06% | 0.31x |
| 9 | CC/USD | 42.150 | 0.08327 | +0.33% | 1.26x |
| 10 | AKT/USD | 37.510 | 0.5172 | +0.04% | 1.75x |
| 11 | CAP/USD | 30.622 | 0.101568 | -0.20% | 0.44x |

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

- Persisted scans: 571; predictions: 4824; observations: 344746.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 12991. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44309204850 · **Generation:** 571 · **Legacy run:** 44309204850
**Main quote time:** 2026-11-18T13:00:10.255693+00:00 · **Legacy report time:** 2026-11-18T13:00:31.204069+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04635 | 73.55 | +0.48% | 1.28x | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | MNT/USD | 0.3854 | 63.00 | -0.05% | 2.40x | MODERATE 57/100 | VERY_HIGH 72/100 | Watch |
| 3 | USELESS/USD ⭐ | 0.10001 | 60.65 | +0.19% | 1.39x | STRONG 75/100 | HIGH 55/100 | Watch |
| 4 | SENT/USD | 0.01956 | 59.21 | -0.22% | 0.92x | WEAK 35/100 | VERY_HIGH 80/100 | Watch |
| 5 | STABLE/USD | 0.02326 | 58.17 | +0.56% | 0.23x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |
| 6 | CC/USD ⭐ | 0.08327 | 46.41 | +0.33% | 1.26x | MODERATE 68/100 | HIGH 60/100 | Watch |
| 7 | AKT/USD | 0.5172 | 45.18 | +0.04% | 1.75x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 8 | ME/USD | 0.0402 | 42.87 | -0.25% | 0.60x | WEAK 16/100 | EXTREME 100/100 | Do nothing |
| 9 | VVV/USD | 21.1 | 38.44 | -0.12% | 0.35x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | TRX/USD | 0.309406 | 37.66 | -0.06% | 0.31x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | CAP/USD | 0.101568 | 24.03 | -0.20% | 0.44x | WEAK 17/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04634 | 74.61 | +0.48% | 1.28x | 16026 | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.10022 | 63.73 | +0.19% | 1.39x | 5311 | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | CC/USD ⭐ | 0.08327 | 49.69 | +0.33% | 1.26x | 4919 | STRONG 70/100 | HIGH 60/100 | Watch |

**Same-run overlap:** NIGHT/USD, USELESS/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
