# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T05:37:49.826626+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46112725883
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4ed8d88219c2937ef3986c8800d0693eea32db1c (atomic ledger/results publication)
**Ledger generation:** 2112 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 418.55 | 69.338 | 69.859 | +2.77% | +0.21% | 0.84x | 9.1 | 2026-11-28T05:37:46.739369+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ZEC/USD | 743.3 | 59.596 | 62.174 | +1.19% | +0.25% | 0.62x | 2.3 | 2026-11-28T05:37:46.739369+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | CC/USD | 0.07499 | 50.383 | 38.368 | +1.13% | -0.07% | 2.23x | 8.0 | 2026-11-28T05:37:46.739369+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SENT/USD | 0.024695 | 48.709 | 57.293 | +4.14% | -1.29% | 0.79x | 5.3 | 2026-11-28T05:37:46.739369+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 5 | VVV/USD | 26.006 | 47.600 | 46.152 | +1.00% | -0.36% | 1.32x | 13.1 | 2026-11-28T05:37:46.739369+00:00 | Not calibrated | WEAK 39/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 69.859 | 418.55 | +0.21% | 0.84x |
| 2 | ZEC/USD | 62.174 | 743.3 | +0.25% | 0.62x |
| 3 | SENT/USD | 57.293 | 0.024695 | -1.29% | 0.79x |
| 4 | VVV/USD | 46.152 | 26.006 | -0.36% | 1.32x |
| 5 | CC/USD | 38.368 | 0.07499 | -0.07% | 2.23x |

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

- Persisted scans: 2112; predictions: 18953; observations: 1278918.
- Matured sampled outcomes across 1/6/24/48h: 44187; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46112725883 · **Generation:** 2112 · **Legacy run:** 46112725883
**Main quote time:** 2026-11-28T05:37:49.826626+00:00 · **Legacy report time:** 2026-11-28T05:38:30.852165+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 418.55 | 69.34 | +0.21% | 0.84x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD | 743.3 | 59.60 | +0.25% | 0.62x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 3 | CC/USD | 0.07499 | 50.38 | -0.07% | 2.23x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 4 | SENT/USD | 0.024695 | 48.71 | -1.29% | 0.79x | WEAK 29/100 | VERY_HIGH 84/100 | Do nothing |
| 5 | VVV/USD | 26.006 | 47.60 | -0.36% | 1.32x | WEAK 39/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
