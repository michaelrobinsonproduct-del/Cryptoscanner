# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T23:41:19.058187+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45084423646
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** be3bd97535c86c36cff630f48ef0f54688c1a85d (atomic ledger/results publication)
**Ledger generation:** 1351 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.501 | 108.746 | 94.104 | +6.43% | -0.07% | 2.54x | 9.1 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 3.6926 | 95.639 | 78.896 | +8.51% | +0.35% | 3.67x | 13.5 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04959 | 89.967 | 91.054 | +11.99% | +0.69% | 0.55x | 8.1 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEC/USD | 794.84 | 86.090 | 68.423 | +2.14% | +0.53% | 10.92x | 3.1 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PUMP/USD | 0.00258 | 84.692 | 81.178 | +10.07% | +0.47% | 1.12x | 11.6 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | STRONG 72/100 | HIGH 68/100 | Watch | WATCH |
| 6 | HYPE/USD | 62.99 | 75.237 | 74.209 | +2.86% | +0.62% | 0.79x | 1.6 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XBT/USD | 61213.8 | 72.390 | 68.084 | +1.87% | +0.47% | 1.20x | 0.0 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 8 | NEAR/USD | 2.9787 | 70.675 | 75.899 | +3.20% | +0.23% | 0.36x | 3.0 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | DRV/USD | 0.36889 | 69.241 | 76.949 | +10.05% | -0.49% | 0.47x | 23.6 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | WEAK 30/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | ETH/USD | 1722.01 | 67.915 | 71.503 | +2.36% | +0.20% | 0.54x | 0.1 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SOL/USD | 70.6 | 62.160 | 58.581 | +0.61% | +0.16% | 1.28x | 1.4 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | MODERATE 56/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XMR/USD | 494.27 | 59.538 | 55.073 | +0.50% | -0.11% | 1.50x | 6.9 | 2026-11-22T23:41:12.017981+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.104 | 26.501 | -0.07% | 2.54x |
| 2 | NIGHT/USD | 91.054 | 0.04959 | +0.69% | 0.55x |
| 3 | PUMP/USD | 81.178 | 0.00258 | +0.47% | 1.12x |
| 4 | PIEVERSE/USD | 78.896 | 3.6926 | +0.35% | 3.67x |
| 5 | DRV/USD | 76.949 | 0.36889 | -0.49% | 0.47x |
| 6 | NEAR/USD | 75.899 | 2.9787 | +0.23% | 0.36x |
| 7 | HYPE/USD | 74.209 | 62.99 | +0.62% | 0.79x |
| 8 | ETH/USD | 71.503 | 1722.01 | +0.20% | 0.54x |
| 9 | ZEC/USD | 68.423 | 794.84 | +0.53% | 10.92x |
| 10 | XBT/USD | 68.084 | 61213.8 | +0.47% | 1.20x |
| 11 | SOL/USD | 58.581 | 70.6 | +0.16% | 1.28x |
| 12 | XMR/USD | 55.073 | 494.27 | -0.11% | 1.50x |

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

- Persisted scans: 1351; predictions: 11131; observations: 817866.
- Matured sampled outcomes across 1/6/24/48h: 17268; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 62 (sampled only; not a success-rate estimate).
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

**Writer:** 45084423646 · **Generation:** 1351 · **Legacy run:** 45084423646
**Main quote time:** 2026-11-22T23:41:19.058187+00:00 · **Legacy report time:** 2026-11-22T23:42:25.117888+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.501 | 108.75 | -0.07% | 2.54x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | PIEVERSE/USD ⭐ | 3.6926 | 95.64 | +0.35% | 3.67x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04959 | 89.97 | +0.69% | 0.55x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEC/USD ⭐ | 794.84 | 86.09 | +0.53% | 10.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PUMP/USD ⭐ | 0.00258 | 84.69 | +0.47% | 1.12x | STRONG 82/100 | HIGH 68/100 | Watch |
| 6 | HYPE/USD | 62.99 | 75.24 | +0.62% | 0.79x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 7 | XBT/USD ⭐ | 61213.8 | 72.39 | +0.47% | 1.20x | STRONG 81/100 | HIGH 62/100 | Watch |
| 8 | NEAR/USD | 2.9787 | 70.67 | +0.23% | 0.36x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 9 | DRV/USD | 0.36889 | 69.24 | -0.49% | 0.47x | WEAK 30/100 | EXTREME 88/100 | Do nothing |
| 10 | ETH/USD | 1722.01 | 67.91 | +0.20% | 0.54x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 11 | SOL/USD | 70.6 | 62.16 | +0.16% | 1.28x | MODERATE 56/100 | HIGH 55/100 | Watch |
| 12 | XMR/USD | 494.27 | 59.54 | -0.11% | 1.50x | MODERATE 50/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.6926 | 86.37 | +0.35% | 3.67x | 5848 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 794.95 | 81.69 | +0.53% | 10.92x | 18227 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PUMP/USD ⭐ | 0.002588 | 79.11 | +0.47% | 1.12x | 4387 | STRONG 80/100 | HIGH 68/100 | Watch |
| 4 | XBT/USD ⭐ | 61131.3 | 74.95 | +0.47% | 1.20x | 131383 | STRONG 82/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PIEVERSE/USD, ZEC/USD, PUMP/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
