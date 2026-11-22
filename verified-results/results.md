# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:41:02.160187+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45003836734
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** d26ba7a32a23c782d40bbe8e27ddc958fa2af4aa (atomic ledger/results publication)
**Ledger generation:** 1258 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 796.71 | 87.859 | 69.607 | +2.38% | +0.65% | 5.80x | 4.1 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.603 | 84.199 | 70.074 | +2.82% | -0.09% | 2.46x | 9.4 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.915 | 77.572 | 59.391 | +0.99% | +0.64% | 17.35x | 5.1 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 189.3824 | 77.224 | 65.943 | +1.97% | +0.35% | 1.95x | 5.7 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ZBCN/USD | 0.001853 | 76.395 | 55.663 | +7.30% | +1.15% | 4.25x | 43.4 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | LINK/USD | 8.68766 | 74.853 | 58.425 | +1.08% | +0.29% | 5.04x | 3.1 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ETH/USD | 1687.53 | 74.582 | 57.155 | +0.31% | +0.49% | 3.87x | 0.1 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | INJ/USD | 6.096 | 65.781 | 51.191 | +2.06% | -0.08% | 7.07x | 6.6 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ASTER/USD | 0.49931 | 65.400 | 50.440 | +2.81% | -0.01% | 4.05x | 7.4 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6507 | 62.823 | 57.909 | +0.53% | +0.62% | 1.18x | 1.5 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.609 | 59.568 | 48.907 | +0.70% | +0.52% | 1.81x | 1.5 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 12 | W/USD | 0.00817 | 46.705 | 29.248 | +0.62% | +0.49% | 19.70x | 12.3 | 2026-11-22T08:40:56.194651+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 70.074 | 25.603 | -0.09% | 2.46x |
| 2 | ZEC/USD | 69.607 | 796.71 | +0.65% | 5.80x |
| 3 | TAO/USD | 65.943 | 189.3824 | +0.35% | 1.95x |
| 4 | NEAR/USD | 59.391 | 2.915 | +0.64% | 17.35x |
| 5 | LINK/USD | 58.425 | 8.68766 | +0.29% | 5.04x |
| 6 | SUI/USD | 57.909 | 0.6507 | +0.62% | 1.18x |
| 7 | ETH/USD | 57.155 | 1687.53 | +0.49% | 3.87x |
| 8 | ZBCN/USD | 55.663 | 0.001853 | +1.15% | 4.25x |
| 9 | INJ/USD | 51.191 | 6.096 | -0.08% | 7.07x |
| 10 | ASTER/USD | 50.440 | 0.49931 | -0.01% | 4.05x |
| 11 | AVAX/USD | 48.907 | 6.609 | +0.52% | 1.81x |
| 12 | W/USD | 29.248 | 0.00817 | +0.49% | 19.70x |

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

- Persisted scans: 1258; predictions: 10024; observations: 761231.
- Matured sampled outcomes across 1/6/24/48h: 14445; gap abstentions: 22113. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45003836734 · **Generation:** 1258 · **Legacy run:** 45003836734
**Main quote time:** 2026-11-22T08:41:02.160187+00:00 · **Legacy report time:** 2026-11-22T08:41:48.571801+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 796.71 | 87.86 | +0.65% | 5.80x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 25.603 | 84.20 | -0.09% | 2.46x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | NEAR/USD ⭐ | 2.915 | 77.57 | +0.64% | 17.35x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 189.3824 | 77.22 | +0.35% | 1.95x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 5 | ZBCN/USD ⭐ | 0.001853 | 76.39 | +1.15% | 4.25x | STRONG 88/100 | VERY_HIGH 82/100 | Watch |
| 6 | LINK/USD | 8.68766 | 74.85 | +0.29% | 5.04x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 7 | ETH/USD ⭐ | 1687.53 | 74.58 | +0.49% | 3.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | INJ/USD | 6.096 | 65.78 | -0.08% | 7.07x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 9 | ASTER/USD | 0.49931 | 65.40 | -0.01% | 4.05x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 10 | SUI/USD ⭐ | 0.6507 | 62.82 | +0.62% | 1.18x | STRONG 76/100 | HIGH 62/100 | Watch |
| 11 | AVAX/USD | 6.609 | 59.57 | +0.52% | 1.81x | STRONG 75/100 | HIGH 55/100 | Watch |
| 12 | W/USD | 0.00817 | 46.70 | +0.49% | 19.70x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD ⭐ | 0.001853 | 82.84 | +1.15% | 4.25x | 3179 | STRONG 96/100 | VERY_HIGH 72/100 | Watch |
| 2 | ZEC/USD ⭐ | 795.48 | 73.64 | +0.65% | 5.80x | 29239 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 189.6089 | 67.86 | +0.35% | 1.95x | 7248 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 2.9164 | 62.76 | +0.64% | 17.35x | 12399 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1687.27 | 59.45 | +0.49% | 3.87x | 46008 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 6 | SUI/USD ⭐ | 0.6512 | 55.67 | +0.62% | 1.18x | 7352 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, NEAR/USD, TAO/USD, ZBCN/USD, ETH/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
