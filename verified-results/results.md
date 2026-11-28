# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:42:46.207469+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46099156889
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0f0bf10ea1a4acccf73c29e80b0c738dee8757f0 (atomic ledger/results publication)
**Ledger generation:** 2094 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 756.04 | 77.324 | 73.211 | +2.92% | -0.43% | 1.63x | 4.5 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.3 | 74.591 | 63.153 | +1.28% | -0.20% | 2.24x | 1.6 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TAO/USD | 187.8759 | 69.311 | 56.062 | +0.49% | -0.35% | 14.73x | 4.8 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CC/USD | 0.07512 | 56.513 | 41.646 | +1.31% | -0.03% | 3.05x | 4.0 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 5 | BCH/USD | 209.15 | 54.837 | 43.524 | +1.04% | +0.11% | 2.08x | 2.4 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 410.37 | 51.831 | 46.896 | +0.76% | -0.52% | 1.75x | 26.9 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | VVV/USD | 26.123 | 50.854 | 53.157 | +1.45% | +0.35% | 0.60x | 8.0 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.0488 | 50.797 | 60.457 | +1.01% | -0.40% | 0.23x | 3.3 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | PUMP/USD | 0.002607 | 41.888 | 38.746 | +0.31% | -0.72% | 1.68x | 3.8 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | WEAK 41/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SPX/USD | 0.274 | 41.154 | 28.706 | +0.59% | -0.51% | 6.98x | 14.6 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | SENT/USD | 0.024138 | 34.772 | 41.717 | +1.79% | -0.93% | 0.77x | 3.3 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 12 | ONDO/USD | 0.2883 | 28.496 | 34.057 | +0.41% | -0.12% | 0.50x | 8.0 | 2026-11-28T02:42:38.037105+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 73.211 | 756.04 | -0.43% | 1.63x |
| 2 | HYPE/USD | 63.153 | 64.3 | -0.20% | 2.24x |
| 3 | NEAR/USD | 60.457 | 3.0488 | -0.40% | 0.23x |
| 4 | TAO/USD | 56.062 | 187.8759 | -0.35% | 14.73x |
| 5 | VVV/USD | 53.157 | 26.123 | +0.35% | 0.60x |
| 6 | XMR/USD | 46.896 | 410.37 | -0.52% | 1.75x |
| 7 | BCH/USD | 43.524 | 209.15 | +0.11% | 2.08x |
| 8 | SENT/USD | 41.717 | 0.024138 | -0.93% | 0.77x |
| 9 | CC/USD | 41.646 | 0.07512 | -0.03% | 3.05x |
| 10 | PUMP/USD | 38.746 | 0.002607 | -0.72% | 1.68x |
| 11 | ONDO/USD | 34.057 | 0.2883 | -0.12% | 0.50x |
| 12 | SPX/USD | 28.706 | 0.274 | -0.51% | 6.98x |

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

- Persisted scans: 2094; predictions: 18791; observations: 1268010.
- Matured sampled outcomes across 1/6/24/48h: 43312; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46099156889 · **Generation:** 2094 · **Legacy run:** 46099156889
**Main quote time:** 2026-11-28T02:42:46.207469+00:00 · **Legacy report time:** 2026-11-28T02:43:27.684679+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 756.04 | 77.32 | -0.43% | 1.63x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 64.3 | 74.59 | -0.20% | 2.24x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | TAO/USD | 187.8759 | 69.31 | -0.35% | 14.73x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | CC/USD | 0.07512 | 56.51 | -0.03% | 3.05x | MODERATE 58/100 | HIGH 66/100 | Watch |
| 5 | BCH/USD ⭐ | 209.15 | 54.84 | +0.11% | 2.08x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | XMR/USD | 410.37 | 51.83 | -0.52% | 1.75x | WEAK 36/100 | VERY_HIGH 73/100 | Watch |
| 7 | VVV/USD | 26.123 | 50.85 | +0.35% | 0.60x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 8 | NEAR/USD | 3.0488 | 50.80 | -0.40% | 0.23x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | PUMP/USD | 0.002607 | 41.89 | -0.72% | 1.68x | WEAK 41/100 | HIGH 61/100 | Watch |
| 10 | SPX/USD | 0.274 | 41.15 | -0.51% | 6.98x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 11 | SENT/USD | 0.024138 | 34.77 | -0.93% | 0.77x | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing |
| 12 | ONDO/USD | 0.2883 | 28.50 | -0.12% | 0.50x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BCH/USD ⭐ | 209.15 | 51.87 | +0.11% | 2.08x | 3017 | STRONG 81/100 | HIGH 55/100 | Watch |
| 2 | PAXG/USD | 3655.06 | 49.18 | +0.10% | 2.77x | 5214 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
