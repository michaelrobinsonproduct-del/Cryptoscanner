# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T01:11:25.300482+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45920946451
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2495d50e3fa249d56e96c16538ac47f115762553 (atomic ledger/results publication)
**Ledger generation:** 1938 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 703.29 | 93.508 | 75.648 | +3.17% | +0.57% | 2.64x | 3.1 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 44.29 | 79.488 | 62.673 | +1.26% | +0.36% | 4.74x | 2.3 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.34755 | 74.811 | 59.747 | +0.85% | +0.01% | 5.00x | 2.5 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 26.316 | 70.104 | 53.420 | +0.51% | +0.34% | 6.23x | 10.3 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Consider small entry | WATCH |
| 5 | ETH/USD | 1700.4 | 67.462 | 59.776 | +0.75% | +0.14% | 1.70x | 1.0 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 469.17 | 67.150 | 66.473 | +2.67% | +1.15% | 0.49x | 14.5 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | HYPE/USD | 63.1 | 66.361 | 63.315 | +1.41% | -0.10% | 1.35x | 3.2 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.0823 | 65.437 | 61.115 | +1.13% | -0.01% | 1.44x | 3.6 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XBT/USD | 60730.7 | 59.310 | 57.684 | +0.38% | +0.14% | 1.09x | 0.0 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 71.35 | 59.241 | 58.345 | +0.58% | +0.13% | 1.03x | 1.4 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94726 | 58.648 | 58.085 | +0.48% | +0.13% | 0.99x | 0.5 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | DOT/USD | 0.6789 | 56.514 | 38.623 | +0.95% | +0.58% | 24.07x | 1.5 | 2026-11-27T01:11:17.721533+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 75.648 | 703.29 | +0.57% | 2.64x |
| 2 | XMR/USD | 66.473 | 469.17 | +1.15% | 0.49x |
| 3 | HYPE/USD | 63.315 | 63.1 | -0.10% | 1.35x |
| 4 | LTC/USD | 62.673 | 44.29 | +0.36% | 4.74x |
| 5 | NEAR/USD | 61.115 | 3.0823 | -0.01% | 1.44x |
| 6 | ETH/USD | 59.776 | 1700.4 | +0.14% | 1.70x |
| 7 | LINK/USD | 59.747 | 9.34755 | +0.01% | 5.00x |
| 8 | SOL/USD | 58.345 | 71.35 | +0.13% | 1.03x |
| 9 | XRP/USD | 58.085 | 0.94726 | +0.13% | 0.99x |
| 10 | XBT/USD | 57.684 | 60730.7 | +0.14% | 1.09x |
| 11 | VVV/USD | 53.420 | 26.316 | +0.34% | 6.23x |
| 12 | DOT/USD | 38.623 | 0.6789 | +0.58% | 24.07x |

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

- Persisted scans: 1938; predictions: 16958; observations: 1173823.
- Matured sampled outcomes across 1/6/24/48h: 37172; gap abstentions: 25421. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45920946451 · **Generation:** 1938 · **Legacy run:** 45920946451
**Main quote time:** 2026-11-27T01:11:25.300482+00:00 · **Legacy report time:** 2026-11-27T01:12:17.200852+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 703.29 | 93.51 | +0.57% | 2.64x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 44.29 | 79.49 | +0.36% | 4.74x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD | 9.34755 | 74.81 | +0.01% | 5.00x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD | 26.316 | 70.10 | +0.34% | 6.23x | STRONG 85/100 | HIGH 61/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1700.4 | 67.46 | +0.14% | 1.70x | STRONG 79/100 | HIGH 55/100 | Watch |
| 6 | XMR/USD | 469.17 | 67.15 | +1.15% | 0.49x | MODERATE 59/100 | VERY_HIGH 76/100 | Watch |
| 7 | HYPE/USD | 63.1 | 66.36 | -0.10% | 1.35x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | NEAR/USD | 3.0823 | 65.44 | -0.01% | 1.44x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | XBT/USD ⭐ | 60730.7 | 59.31 | +0.14% | 1.09x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD ⭐ | 71.35 | 59.24 | +0.13% | 1.03x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 11 | XRP/USD | 0.94726 | 58.65 | +0.13% | 0.99x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | DOT/USD ⭐ | 0.6789 | 56.51 | +0.58% | 24.07x | STRONG 93/100 | HIGH 60/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 703.07 | 87.43 | +0.57% | 2.64x | 33469 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 44.3 | 71.94 | +0.36% | 4.74x | 14398 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1700.26 | 64.04 | +0.14% | 1.70x | 29375 | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | XBT/USD ⭐ | 60727.7 | 57.32 | +0.14% | 1.09x | 130854 | MODERATE 64/100 | HIGH 62/100 | Watch |
| 5 | DOT/USD ⭐ | 0.6787 | 56.47 | +0.58% | 24.07x | 5868 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 6 | SOL/USD ⭐ | 71.33 | 56.28 | +0.13% | 1.03x | 33025 | MODERATE 63/100 | HIGH 62/100 | Watch |
| 7 | TIA/USD | 0.3403 | 48.15 | +0.41% | 1.07x | 3550 | MODERATE 59/100 | HIGH 67/100 | Watch |

**Same-run overlap:** ZEC/USD, LTC/USD, ETH/USD, XBT/USD, SOL/USD, DOT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
