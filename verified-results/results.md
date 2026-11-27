# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T14:02:41.066476+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46011863869
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9899df4be3aba0b45c9e22991e76e8b63b53374a (atomic ledger/results publication)
**Ledger generation:** 2017 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 754.7 | 109.233 | 98.541 | +10.71% | -0.04% | 2.09x | 2.9 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 66.04 | 95.724 | 96.462 | +6.14% | +0.17% | 0.84x | 3.0 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 3 | VVV/USD | 27.427 | 81.837 | 81.862 | +4.75% | +0.51% | 0.74x | 7.3 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0588827 | 81.803 | 77.518 | +4.45% | +0.22% | 1.32x | 0.7 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6867 | 79.512 | 73.641 | +2.85% | +0.03% | 1.57x | 1.5 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SOL/USD | 73.25 | 77.297 | 77.111 | +3.26% | +0.14% | 0.95x | 1.4 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 7 | INJ/USD | 6.471 | 77.075 | 71.093 | +4.51% | -0.49% | 1.84x | 3.1 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 8 | PEPE/USD | 3.624e-06 | 74.305 | 71.999 | +4.20% | -0.08% | 1.27x | 2.8 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XBT/USD | 61385.4 | 73.128 | 65.260 | +1.47% | +0.08% | 1.75x | 0.0 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ETH/USD | 1721.82 | 72.306 | 69.131 | +2.02% | +0.19% | 1.22x | 0.1 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XRP/USD | 0.96732 | 71.915 | 73.192 | +2.61% | -0.04% | 0.89x | 0.1 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 12 | ENA/USD | 0.1065 | 70.669 | 74.815 | +6.08% | +0.09% | 0.54x | 9.4 | 2026-11-27T14:02:33.285407+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.541 | 754.7 | -0.04% | 2.09x |
| 2 | HYPE/USD | 96.462 | 66.04 | +0.17% | 0.84x |
| 3 | VVV/USD | 81.862 | 27.427 | +0.51% | 0.74x |
| 4 | XDG/USD | 77.518 | 0.0588827 | +0.22% | 1.32x |
| 5 | SOL/USD | 77.111 | 73.25 | +0.14% | 0.95x |
| 6 | ENA/USD | 74.815 | 0.1065 | +0.09% | 0.54x |
| 7 | SUI/USD | 73.641 | 0.6867 | +0.03% | 1.57x |
| 8 | XRP/USD | 73.192 | 0.96732 | -0.04% | 0.89x |
| 9 | PEPE/USD | 71.999 | 3.624e-06 | -0.08% | 1.27x |
| 10 | INJ/USD | 71.093 | 6.471 | -0.49% | 1.84x |
| 11 | ETH/USD | 69.131 | 1721.82 | +0.19% | 1.22x |
| 12 | XBT/USD | 65.260 | 61385.4 | +0.08% | 1.75x |

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

- Persisted scans: 2017; predictions: 17906; observations: 1221400.
- Matured sampled outcomes across 1/6/24/48h: 39941; gap abstentions: 25883. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46011863869 · **Generation:** 2017 · **Legacy run:** 46011863869
**Main quote time:** 2026-11-27T14:02:41.066476+00:00 · **Legacy report time:** 2026-11-27T14:03:35.412250+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 754.7 | 109.23 | -0.04% | 2.09x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 66.04 | 95.72 | +0.17% | 0.84x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD | 27.427 | 81.84 | +0.51% | 0.74x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0588827 | 81.80 | +0.22% | 1.32x | STRONG 96/100 | HIGH 55/100 | Watch |
| 5 | SUI/USD | 0.6867 | 79.51 | +0.03% | 1.57x | STRONG 75/100 | HIGH 55/100 | Watch |
| 6 | SOL/USD | 73.25 | 77.30 | +0.14% | 0.95x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 7 | INJ/USD | 6.471 | 77.08 | -0.49% | 1.84x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 8 | PEPE/USD | 3.624e-06 | 74.31 | -0.08% | 1.27x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 9 | XBT/USD | 61385.4 | 73.13 | +0.08% | 1.75x | STRONG 72/100 | HIGH 55/100 | Watch |
| 10 | ETH/USD ⭐ | 1721.82 | 72.31 | +0.19% | 1.22x | STRONG 71/100 | HIGH 62/100 | Watch |
| 11 | XRP/USD | 0.96732 | 71.91 | -0.04% | 0.89x | WEAK 41/100 | HIGH 68/100 | Watch |
| 12 | ENA/USD | 0.1065 | 70.67 | +0.09% | 0.54x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0589461 | 95.04 | +0.22% | 1.32x | 6043 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ETH/USD ⭐ | 1722.7 | 78.25 | +0.19% | 1.22x | 36470 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XDG/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
