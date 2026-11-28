# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T03:38:48.508424+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46103515259
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8bbd9d7e5929dd96bb8d9f61279033b565960bc7 (atomic ledger/results publication)
**Ledger generation:** 2100 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 418.88 | 70.103 | 60.372 | +2.85% | +0.66% | 1.64x | 29.2 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ZEC/USD | 752.23 | 64.459 | 69.901 | +2.40% | -0.31% | 0.61x | 3.9 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | CC/USD | 0.07586 | 63.487 | 48.751 | +2.31% | -0.05% | 5.31x | 4.0 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0565 | 55.464 | 61.592 | +1.27% | -0.26% | 0.52x | 4.6 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 64.35 | 54.763 | 62.928 | +1.35% | -0.28% | 0.32x | 3.1 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | BCH/USD | 209.42 | 54.158 | 43.567 | +1.17% | -0.12% | 2.12x | 3.3 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | VVV/USD | 26.251 | 51.913 | 57.209 | +1.95% | -0.07% | 0.50x | 6.1 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.024247 | 40.187 | 46.424 | +2.25% | -0.56% | 0.65x | 0.4 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | WEAK 25/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2739 | 37.481 | 23.029 | +0.55% | -0.11% | 3.32x | 25.5 | 2026-11-28T03:38:43.962809+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 78/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 69.901 | 752.23 | -0.31% | 0.61x |
| 2 | HYPE/USD | 62.928 | 64.35 | -0.28% | 0.32x |
| 3 | NEAR/USD | 61.592 | 3.0565 | -0.26% | 0.52x |
| 4 | XMR/USD | 60.372 | 418.88 | +0.66% | 1.64x |
| 5 | VVV/USD | 57.209 | 26.251 | -0.07% | 0.50x |
| 6 | CC/USD | 48.751 | 0.07586 | -0.05% | 5.31x |
| 7 | SENT/USD | 46.424 | 0.024247 | -0.56% | 0.65x |
| 8 | BCH/USD | 43.567 | 209.42 | -0.12% | 2.12x |
| 9 | SPX/USD | 23.029 | 0.2739 | -0.11% | 3.32x |

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

- Persisted scans: 2100; predictions: 18855; observations: 1271646.
- Matured sampled outcomes across 1/6/24/48h: 43610; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46103515259 · **Generation:** 2100 · **Legacy run:** 46103515259
**Main quote time:** 2026-11-28T03:38:48.508424+00:00 · **Legacy report time:** 2026-11-28T03:39:36.407305+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 418.88 | 70.10 | +0.66% | 1.64x | STRONG 80/100 | HIGH 67/100 | Consider small entry |
| 2 | ZEC/USD | 752.23 | 64.46 | -0.31% | 0.61x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 3 | CC/USD | 0.07586 | 63.49 | -0.05% | 5.31x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 4 | NEAR/USD | 3.0565 | 55.46 | -0.26% | 0.52x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | HYPE/USD | 64.35 | 54.76 | -0.28% | 0.32x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | BCH/USD | 209.42 | 54.16 | -0.12% | 2.12x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | VVV/USD | 26.251 | 51.91 | -0.07% | 0.50x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SENT/USD | 0.024247 | 40.19 | -0.56% | 0.65x | WEAK 25/100 | EXTREME 88/100 | Do nothing |
| 9 | SPX/USD | 0.2739 | 37.48 | -0.11% | 3.32x | WEAK 39/100 | VERY_HIGH 78/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 420.03 | 79.15 | +0.66% | 1.64x | 14830 | STRONG 80/100 | VERY_HIGH 77/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
