# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:16:07.365837+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45693046333
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ae625a8e907a01aea8fe088d1665a559f68f805b (atomic ledger/results publication)
**Ledger generation:** 1762 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9557 | 89.165 | 68.387 | +2.47% | +1.16% | 3.59x | 7.8 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | CT/USD | 0.1348 | 74.081 | 68.578 | +6.73% | +0.75% | 1.18x | 14.9 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | ZEC/USD | 757.03 | 73.970 | 69.808 | +2.46% | +1.05% | 0.89x | 4.8 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 4 | LTC/USD | 42.47 | 73.595 | 80.406 | +3.97% | +0.17% | 0.24x | 4.7 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | HYPE/USD | 61.5 | 70.944 | 72.433 | +2.72% | +0.87% | 0.42x | 3.2 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XPL/USD | 0.048 | 64.284 | 71.949 | +9.09% | +0.00% | 0.23x | 20.8 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93798 | 63.911 | 65.731 | +1.56% | -0.07% | 0.86x | 0.3 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LINK/USD | 9.0814 | 63.526 | 63.732 | +2.72% | +0.08% | 0.94x | 4.8 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6616 | 63.099 | 69.489 | +2.18% | +0.00% | 0.36x | 1.5 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 70.44 | 58.717 | 62.739 | +1.21% | +0.19% | 0.51x | 1.4 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PAXG/USD | 3562.31 | 57.341 | 58.965 | +0.58% | +0.53% | 0.57x | 0.2 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.12744 | 56.770 | 61.946 | +2.73% | +0.26% | 0.35x | 3.6 | 2026-11-25T20:15:59.220980+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 80.406 | 42.47 | +0.17% | 0.24x |
| 2 | HYPE/USD | 72.433 | 61.5 | +0.87% | 0.42x |
| 3 | XPL/USD | 71.949 | 0.048 | +0.00% | 0.23x |
| 4 | ZEC/USD | 69.808 | 757.03 | +1.05% | 0.89x |
| 5 | SUI/USD | 69.489 | 0.6616 | +0.00% | 0.36x |
| 6 | CT/USD | 68.578 | 0.1348 | +0.75% | 1.18x |
| 7 | NEAR/USD | 68.387 | 2.9557 | +1.16% | 3.59x |
| 8 | XRP/USD | 65.731 | 0.93798 | -0.07% | 0.86x |
| 9 | LINK/USD | 63.732 | 9.0814 | +0.08% | 0.94x |
| 10 | SOL/USD | 62.739 | 70.44 | +0.19% | 0.51x |
| 11 | XLM/USD | 61.946 | 0.12744 | +0.26% | 0.35x |
| 12 | PAXG/USD | 58.965 | 3562.31 | +0.53% | 0.57x |

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

- Persisted scans: 1762; predictions: 14888; observations: 1068102.
- Matured sampled outcomes across 1/6/24/48h: 32630; gap abstentions: 22944. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45693046333 · **Generation:** 1762 · **Legacy run:** 45693046333
**Main quote time:** 2026-11-25T20:16:07.365837+00:00 · **Legacy report time:** 2026-11-25T20:17:01.208049+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9557 | 89.17 | +1.16% | 3.59x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | CT/USD | 0.1348 | 74.08 | +0.75% | 1.18x | MODERATE 67/100 | VERY_HIGH 80/100 | Watch |
| 3 | ZEC/USD | 757.03 | 73.97 | +1.05% | 0.89x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 4 | LTC/USD | 42.47 | 73.60 | +0.17% | 0.24x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | HYPE/USD | 61.5 | 70.94 | +0.87% | 0.42x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 6 | XPL/USD | 0.048 | 64.28 | +0.00% | 0.23x | WEAK 42/100 | VERY_HIGH 82/100 | Watch |
| 7 | XRP/USD | 0.93798 | 63.91 | -0.07% | 0.86x | WEAK 37/100 | HIGH 68/100 | Watch |
| 8 | LINK/USD | 9.0814 | 63.53 | +0.08% | 0.94x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6616 | 63.10 | +0.00% | 0.36x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 70.44 | 58.72 | +0.19% | 0.51x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | PAXG/USD | 3562.31 | 57.34 | +0.53% | 0.57x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD | 0.12744 | 56.77 | +0.26% | 0.35x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9711 | 92.77 | +1.16% | 3.59x | 14617 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HBAR/USD | 0.05177 | 73.86 | +0.31% | 1.01x | 5952 | STRONG 72/100 | HIGH 67/100 | Watch |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
