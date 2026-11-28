# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T03:57:38.975182+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46105056456
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c70563409a6deeb5d0a155d62ccafd4b121d4443 (atomic ledger/results publication)
**Ledger generation:** 2102 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 421.34 | 74.425 | 74.670 | +3.45% | +0.37% | 0.79x | 9.0 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0566 | 69.771 | 62.106 | +1.27% | +0.08% | 1.73x | 3.6 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 751.27 | 61.988 | 69.317 | +2.27% | -0.14% | 0.34x | 3.2 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | HYPE/USD | 64.24 | 51.629 | 61.713 | +1.18% | -0.25% | 0.12x | 3.1 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | BCH/USD | 209.49 | 51.410 | 44.420 | +1.20% | +0.05% | 1.68x | 1.9 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | MODERATE 61/100 | HIGH 55/100 | Watch | WATCH |
| 6 | VVV/USD | 26.037 | 49.654 | 49.857 | +1.12% | -0.75% | 1.35x | 8.8 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SENT/USD | 0.024289 | 43.660 | 46.616 | +2.42% | -0.05% | 0.73x | 2.5 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.07552 | 34.345 | 41.557 | +1.85% | -0.80% | 0.68x | 11.9 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | WEAK 17/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2739 | 25.511 | 24.826 | +0.55% | -0.04% | 1.09x | 21.9 | 2026-11-28T03:57:33.914389+00:00 | Not calibrated | WEAK 13/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 74.670 | 421.34 | +0.37% | 0.79x |
| 2 | ZEC/USD | 69.317 | 751.27 | -0.14% | 0.34x |
| 3 | NEAR/USD | 62.106 | 3.0566 | +0.08% | 1.73x |
| 4 | HYPE/USD | 61.713 | 64.24 | -0.25% | 0.12x |
| 5 | VVV/USD | 49.857 | 26.037 | -0.75% | 1.35x |
| 6 | SENT/USD | 46.616 | 0.024289 | -0.05% | 0.73x |
| 7 | BCH/USD | 44.420 | 209.49 | +0.05% | 1.68x |
| 8 | CC/USD | 41.557 | 0.07552 | -0.80% | 0.68x |
| 9 | SPX/USD | 24.826 | 0.2739 | -0.04% | 1.09x |

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

- Persisted scans: 2102; predictions: 18873; observations: 1272858.
- Matured sampled outcomes across 1/6/24/48h: 43706; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46105056456 · **Generation:** 2102 · **Legacy run:** 46105056456
**Main quote time:** 2026-11-28T03:57:38.975182+00:00 · **Legacy report time:** 2026-11-28T03:58:29.309665+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 421.34 | 74.43 | +0.37% | 0.79x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0566 | 69.77 | +0.08% | 1.73x | STRONG 80/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD | 751.27 | 61.99 | -0.14% | 0.34x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 4 | HYPE/USD | 64.24 | 51.63 | -0.25% | 0.12x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | BCH/USD | 209.49 | 51.41 | +0.05% | 1.68x | MODERATE 61/100 | HIGH 55/100 | Watch |
| 6 | VVV/USD | 26.037 | 49.65 | -0.75% | 1.35x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 7 | SENT/USD | 0.024289 | 43.66 | -0.05% | 0.73x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 8 | CC/USD | 0.07552 | 34.35 | -0.80% | 0.68x | WEAK 17/100 | EXTREME 87/100 | Do nothing |
| 9 | SPX/USD | 0.2739 | 25.51 | -0.04% | 1.09x | WEAK 13/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0547 | 63.11 | +0.08% | 1.73x | 13018 | STRONG 77/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
