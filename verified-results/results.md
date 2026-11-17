# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:05:00.285184+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44196070791
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** b121633b481685c41344c0423bcb8ebfc7692bbd (atomic ledger/results publication)
**Ledger generation:** 466 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.26 | 103.945 | 88.876 | +5.23% | +0.01% | 3.80x | 5.5 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.3294 | 93.164 | 90.037 | +5.43% | -0.09% | 1.36x | 6.0 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 947.03 | 86.341 | 86.784 | +4.78% | -0.30% | 1.11x | 3.4 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 4 | STX/USD | 0.2783 | 85.151 | 66.156 | +5.90% | +0.80% | 2.60x | 14.4 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 5 | SOL/USD | 74.12 | 78.805 | 79.773 | +3.64% | +0.07% | 0.87x | 1.3 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | TAO/USD | 195.4247 | 77.727 | 68.401 | +2.21% | +0.29% | 1.79x | 4.1 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XMR/USD | 508.7 | 69.471 | 73.591 | +3.06% | +0.37% | 0.40x | 5.7 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | AVAX/USD | 7.208 | 66.249 | 52.617 | +1.36% | +0.01% | 2.36x | 1.4 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 9 | AAVE/USD | 112.05 | 61.462 | 64.628 | +3.29% | +0.01% | 0.68x | 1.8 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SUI/USD | 0.7331 | 60.522 | 66.966 | +1.90% | +0.01% | 0.35x | 2.7 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XRP/USD | 0.97443 | 59.982 | 68.138 | +2.06% | +0.11% | 0.13x | 2.6 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0597289 | 55.095 | 62.633 | +1.43% | +0.06% | 0.22x | 2.8 | 2026-11-17T23:04:53.659763+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 90.037 | 3.3294 | -0.09% | 1.36x |
| 2 | INJ/USD | 88.876 | 7.26 | +0.01% | 3.80x |
| 3 | ZEC/USD | 86.784 | 947.03 | -0.30% | 1.11x |
| 4 | SOL/USD | 79.773 | 74.12 | +0.07% | 0.87x |
| 5 | XMR/USD | 73.591 | 508.7 | +0.37% | 0.40x |
| 6 | TAO/USD | 68.401 | 195.4247 | +0.29% | 1.79x |
| 7 | XRP/USD | 68.138 | 0.97443 | +0.11% | 0.13x |
| 8 | SUI/USD | 66.966 | 0.7331 | +0.01% | 0.35x |
| 9 | STX/USD | 66.156 | 0.2783 | +0.80% | 2.60x |
| 10 | AAVE/USD | 64.628 | 112.05 | +0.01% | 0.68x |
| 11 | XDG/USD | 62.633 | 0.0597289 | +0.06% | 0.22x |
| 12 | AVAX/USD | 52.617 | 7.208 | +0.01% | 2.36x |

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

- Persisted scans: 466; predictions: 4073; observations: 280801.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44196070791 · **Generation:** 466 · **Legacy run:** 44196070791
**Main quote time:** 2026-11-17T23:05:00.285184+00:00 · **Legacy report time:** 2026-11-17T23:05:08.450494+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.26 | 103.94 | +0.01% | 3.80x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 3.3294 | 93.16 | -0.09% | 1.36x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD ⭐ | 947.03 | 86.34 | -0.30% | 1.11x | MODERATE 63/100 | HIGH 68/100 | Watch |
| 4 | STX/USD | 0.2783 | 85.15 | +0.80% | 2.60x | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 74.12 | 78.80 | +0.07% | 0.87x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 6 | TAO/USD ⭐ | 195.4247 | 77.73 | +0.29% | 1.79x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 7 | XMR/USD | 508.7 | 69.47 | +0.37% | 0.40x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | AVAX/USD | 7.208 | 66.25 | +0.01% | 2.36x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | AAVE/USD | 112.05 | 61.46 | +0.01% | 0.68x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 10 | SUI/USD | 0.7331 | 60.52 | +0.01% | 0.35x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | XRP/USD | 0.97443 | 59.98 | +0.11% | 0.13x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0597289 | 55.10 | +0.06% | 0.22x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 947.03 | 98.56 | +0.16% | 1.05x | 25872 | STRONG 84/100 | HIGH 62/100 | Watch |
| 2 | SOL/USD ⭐ | 74.21 | 96.14 | +0.50% | 1.05x | 35375 | STRONG 93/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD ⭐ | 195.4997 | 77.18 | +0.45% | 1.67x | 5040 | STRONG 94/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, SOL/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
