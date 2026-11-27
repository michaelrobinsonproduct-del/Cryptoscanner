# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T07:51:39.210165+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45961133882
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 08cac42b7a7ffb201c4cb7a319070ad959831dd0 (atomic ledger/results publication)
**Ledger generation:** 1979 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 741.8 | 96.651 | 96.292 | +8.82% | -0.90% | 1.49x | 7.4 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.97807 | 95.059 | 80.407 | +3.75% | -0.07% | 3.42x | 1.6 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.61075 | 94.954 | 78.162 | +3.69% | +0.36% | 4.82x | 5.4 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | UNI/USD | 4.9054 | 92.916 | 78.202 | +5.49% | -0.06% | 5.47x | 8.4 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 73.22 | 92.226 | 76.815 | +3.21% | +0.08% | 2.53x | 1.4 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 65.29 | 91.258 | 88.007 | +4.93% | -1.08% | 1.86x | 3.1 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | MODERATE 66/100 | HIGH 65/100 | Watch | WATCH |
| 7 | ETH/USD | 1732.17 | 76.706 | 72.847 | +2.64% | -0.19% | 1.48x | 1.2 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XBT/USD | 61639.4 | 69.289 | 68.199 | +1.89% | -0.31% | 1.26x | 0.0 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ENA/USD | 0.1065 | 69.012 | 73.249 | +6.08% | +0.38% | 0.39x | 9.4 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6842 | 64.272 | 70.836 | +2.47% | -0.09% | 0.39x | 2.9 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ADA/USD | 0.153214 | 63.771 | 71.666 | +3.20% | +0.07% | 0.18x | 4.5 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | VVV/USD | 27.079 | 63.340 | 70.071 | +3.42% | -0.67% | 0.66x | 17.8 | 2026-11-27T07:51:32.762100+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.292 | 741.8 | -0.90% | 1.49x |
| 2 | HYPE/USD | 88.007 | 65.29 | -1.08% | 1.86x |
| 3 | XRP/USD | 80.407 | 0.97807 | -0.07% | 3.42x |
| 4 | UNI/USD | 78.202 | 4.9054 | -0.06% | 5.47x |
| 5 | LINK/USD | 78.162 | 9.61075 | +0.36% | 4.82x |
| 6 | SOL/USD | 76.815 | 73.22 | +0.08% | 2.53x |
| 7 | ENA/USD | 73.249 | 0.1065 | +0.38% | 0.39x |
| 8 | ETH/USD | 72.847 | 1732.17 | -0.19% | 1.48x |
| 9 | ADA/USD | 71.666 | 0.153214 | +0.07% | 0.18x |
| 10 | SUI/USD | 70.836 | 0.6842 | -0.09% | 0.39x |
| 11 | VVV/USD | 70.071 | 27.079 | -0.67% | 0.66x |
| 12 | XBT/USD | 68.199 | 61639.4 | -0.31% | 1.26x |

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

- Persisted scans: 1979; predictions: 17450; observations: 1198490.
- Matured sampled outcomes across 1/6/24/48h: 38573; gap abstentions: 25649. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45961133882 · **Generation:** 1979 · **Legacy run:** 45961133882
**Main quote time:** 2026-11-27T07:51:39.210165+00:00 · **Legacy report time:** 2026-11-27T07:52:21.574841+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 741.8 | 96.65 | -0.90% | 1.49x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.97807 | 95.06 | -0.07% | 3.42x | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD ⭐ | 9.61075 | 94.95 | +0.36% | 4.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | UNI/USD | 4.9054 | 92.92 | -0.06% | 5.47x | STRONG 76/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD ⭐ | 73.22 | 92.23 | +0.08% | 2.53x | STRONG 100/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 65.29 | 91.26 | -1.08% | 1.86x | MODERATE 66/100 | HIGH 65/100 | Watch |
| 7 | ETH/USD | 1732.17 | 76.71 | -0.19% | 1.48x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 8 | XBT/USD | 61639.4 | 69.29 | -0.31% | 1.26x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 9 | ENA/USD | 0.1065 | 69.01 | +0.38% | 0.39x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 10 | SUI/USD | 0.6842 | 64.27 | -0.09% | 0.39x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | ADA/USD | 0.153214 | 63.77 | +0.07% | 0.18x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 12 | VVV/USD | 27.079 | 63.34 | -0.67% | 0.66x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.60403 | 100.00 | +0.36% | 4.82x | 7764 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 73.17 | 93.34 | +0.08% | 2.53x | 33366 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
