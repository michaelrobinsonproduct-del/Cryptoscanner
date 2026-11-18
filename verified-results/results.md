# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:05:16.286637+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44310035829
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 4fc45db3148b65ac9d63573ebbb9d0c16ec7fd64 (atomic ledger/results publication)
**Ledger generation:** 572 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04615 | 75.175 | 63.934 | +2.81% | -0.75% | 4.87x | 8.7 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | STABLE/USD | 0.02347 | 64.207 | 63.189 | +11.50% | +1.73% | 0.24x | 25.6 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | MNT/USD | 0.3837 | 60.917 | 47.346 | +2.79% | -0.29% | 3.59x | 10.4 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.10014 | 58.704 | 58.778 | +2.62% | +0.03% | 0.98x | 3.0 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SENT/USD | 0.019465 | 53.872 | 58.572 | +4.26% | -0.74% | 0.90x | 4.6 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.08335 | 45.957 | 43.430 | +1.49% | +0.41% | 1.05x | 6.0 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 7 | ME/USD | 0.04 | 39.866 | 44.387 | +3.63% | -0.74% | 0.92x | 25.0 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | WEAK 15/100 | EXTREME 92/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.309428 | 36.393 | 43.581 | +0.50% | -0.18% | 0.37x | 2.7 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5175 | 32.673 | 35.975 | +1.61% | +0.06% | 0.64x | 15.5 | 2026-11-18T13:05:09.818576+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 63.934 | 0.04615 | -0.75% | 4.87x |
| 2 | STABLE/USD | 63.189 | 0.02347 | +1.73% | 0.24x |
| 3 | USELESS/USD | 58.778 | 0.10014 | +0.03% | 0.98x |
| 4 | SENT/USD | 58.572 | 0.019465 | -0.74% | 0.90x |
| 5 | MNT/USD | 47.346 | 0.3837 | -0.29% | 3.59x |
| 6 | ME/USD | 44.387 | 0.04 | -0.74% | 0.92x |
| 7 | TRX/USD | 43.581 | 0.309428 | -0.18% | 0.37x |
| 8 | CC/USD | 43.430 | 0.08335 | +0.41% | 1.05x |
| 9 | AKT/USD | 35.975 | 0.5175 | +0.06% | 0.64x |

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

- Persisted scans: 572; predictions: 4833; observations: 345355.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 12999. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44310035829 · **Generation:** 572 · **Legacy run:** 44310035829
**Main quote time:** 2026-11-18T13:05:16.286637+00:00 · **Legacy report time:** 2026-11-18T13:05:41.276855+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04615 | 75.17 | -0.75% | 4.87x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | STABLE/USD | 0.02347 | 64.21 | +1.73% | 0.24x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 3 | MNT/USD | 0.3837 | 60.92 | -0.29% | 3.59x | MODERATE 55/100 | VERY_HIGH 72/100 | Watch |
| 4 | USELESS/USD | 0.10014 | 58.70 | +0.03% | 0.98x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 5 | SENT/USD | 0.019465 | 53.87 | -0.74% | 0.90x | WEAK 32/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | CC/USD ⭐ | 0.08335 | 45.96 | +0.41% | 1.05x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 7 | ME/USD | 0.04 | 39.87 | -0.74% | 0.92x | WEAK 15/100 | EXTREME 92/100 | Do nothing |
| 8 | TRX/USD | 0.309428 | 36.39 | -0.18% | 0.37x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | AKT/USD | 0.5175 | 32.67 | +0.06% | 0.64x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.0833 | 47.12 | +0.41% | 1.05x | 4911 | MODERATE 69/100 | HIGH 67/100 | Watch |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
