# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:40:02.511513+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44192186560
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** f5e0d00a34197a778a88ec3c8807346e1473572e (atomic ledger/results publication)
**Ledger generation:** 461 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3189 | 104.978 | 89.958 | +5.10% | +1.05% | 1.98x | 1.5 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 948.24 | 104.736 | 88.199 | +4.92% | +1.25% | 2.03x | 2.4 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | INJ/USD | 7.253 | 101.159 | 87.469 | +5.13% | +1.10% | 1.82x | 6.9 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LUNA/USD | 4.115e-05 | 85.993 | 70.627 | +10.32% | +0.07% | 4.09x | 14.6 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5024 | 83.157 | 66.168 | +5.02% | +1.23% | 2.08x | 2.0 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 97/100 | HIGH 60/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 73.92 | 81.562 | 77.813 | +3.36% | +0.41% | 1.17x | 1.4 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XMR/USD | 505.77 | 79.396 | 67.837 | +2.47% | -0.22% | 2.26x | 8.9 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97146 | 77.231 | 66.832 | +1.75% | +0.21% | 1.94x | 0.8 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | WINGS/USD | 0.001922 | 75.488 | 65.778 | +8.04% | +1.70% | 1.12x | 20.8 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | MODERATE 63/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | VVV/USD | 20.95 | 74.406 | 74.709 | +3.98% | +1.74% | 0.10x | 0.5 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TRUST/USD | 0.04735 | 70.176 | 75.843 | +10.09% | +0.21% | 0.33x | 4.2 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | JUP/USD | 0.25786 | 69.852 | 72.708 | +7.19% | +0.62% | 0.41x | 10.9 | 2026-11-17T22:39:56.008815+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 89.958 | 3.3189 | +1.05% | 1.98x |
| 2 | ZEC/USD | 88.199 | 948.24 | +1.25% | 2.03x |
| 3 | INJ/USD | 87.469 | 7.253 | +1.10% | 1.82x |
| 4 | SOL/USD | 77.813 | 73.92 | +0.41% | 1.17x |
| 5 | TRUST/USD | 75.843 | 0.04735 | +0.21% | 0.33x |
| 6 | VVV/USD | 74.709 | 20.95 | +1.74% | 0.10x |
| 7 | JUP/USD | 72.708 | 0.25786 | +0.62% | 0.41x |
| 8 | LUNA/USD | 70.627 | 4.115e-05 | +0.07% | 4.09x |
| 9 | XMR/USD | 67.837 | 505.77 | -0.22% | 2.26x |
| 10 | XRP/USD | 66.832 | 0.97146 | +0.21% | 1.94x |
| 11 | AKT/USD | 66.168 | 0.5024 | +1.23% | 2.08x |
| 12 | WINGS/USD | 65.778 | 0.001922 | +1.70% | 1.12x |

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

- Persisted scans: 461; predictions: 4013; observations: 277756.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44192186560 · **Generation:** 461 · **Legacy run:** 44192186560
**Main quote time:** 2026-11-17T22:40:02.511513+00:00 · **Legacy report time:** 2026-11-17T22:40:12.190151+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3189 | 104.98 | +1.05% | 1.98x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 948.24 | 104.74 | +1.25% | 2.03x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | INJ/USD ⭐ | 7.253 | 101.16 | +1.10% | 1.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LUNA/USD | 4.115e-05 | 85.99 | +0.07% | 4.09x | STRONG 83/100 | HIGH 66/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5024 | 83.16 | +1.23% | 2.08x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 6 | SOL/USD | 73.92 | 81.56 | +0.41% | 1.17x | STRONG 76/100 | HIGH 62/100 | Watch |
| 7 | XMR/USD | 505.77 | 79.40 | -0.22% | 2.26x | STRONG 70/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.97146 | 77.23 | +0.21% | 1.94x | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 9 | WINGS/USD ⭐ | 0.001922 | 75.49 | +1.70% | 1.12x | STRONG 73/100 | EXTREME 86/100 | Do nothing |
| 10 | VVV/USD | 20.95 | 74.41 | +1.74% | 0.10x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 11 | TRUST/USD | 0.04735 | 70.18 | +0.21% | 0.33x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 12 | JUP/USD | 0.25786 | 69.85 | +0.62% | 0.41x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.319 | 100.00 | +0.34% | 5.92x | 14952 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.249 | 99.12 | +0.72% | 9.06x | 9739 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 948.24 | 98.43 | +0.88% | 2.11x | 25889 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | AKT/USD ⭐ | 0.5024 | 88.83 | +0.60% | 2.20x | 2962 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 5 | WINGS/USD ⭐ | 0.001922 | 82.59 | +2.23% | 1.14x | 3894 | STRONG 86/100 | VERY_HIGH 74/100 | Watch |
| 6 | RENDER/USD | 1.437 | 79.37 | +0.07% | 3.30x | 2387 | STRONG 85/100 | HIGH 60/100 | Watch |

**Same-run overlap:** NEAR/USD, ZEC/USD, INJ/USD, AKT/USD, WINGS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
