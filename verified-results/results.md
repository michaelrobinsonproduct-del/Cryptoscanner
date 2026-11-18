# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:00:15.037914+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44319401896
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** cb492004841f21143d2cd146aaac6a5f0a224a1c (atomic ledger/results publication)
**Ledger generation:** 583 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04673 | 68.254 | 71.766 | +4.10% | +0.34% | 0.48x | 10.7 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019255 | 64.449 | 48.865 | +3.14% | +0.36% | 2.38x | 8.3 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 3 | TRX/USD | 0.309556 | 60.159 | 45.262 | +0.54% | -0.02% | 2.84x | 0.7 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05485 | 59.261 | 59.121 | +6.22% | +0.57% | 0.73x | 31.1 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | PEARL/USD | 1.8365 | 56.862 | 37.690 | +1.44% | +0.83% | 4.05x | 21.3 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 6 | VVV/USD | 21.158 | 55.664 | 48.632 | +0.63% | -1.08% | 2.24x | 8.0 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | MODERATE 58/100 | HIGH 65/100 | Watch | WATCH |
| 7 | XRP/USD | 0.98611 | 49.638 | 57.500 | +0.36% | -0.01% | 0.22x | 0.1 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5217 | 41.693 | 47.609 | +2.43% | -0.25% | 0.53x | 3.8 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.102437 | 41.388 | 23.487 | +1.45% | +0.58% | 3.16x | 35.9 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | W/USD | 0.00903 | 34.359 | 34.004 | +1.12% | -0.88% | 1.47x | 11.1 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 11 | CC/USD | 0.08298 | 33.748 | 40.260 | +1.03% | -0.22% | 0.46x | 4.8 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | USELESS/USD | 0.0993 | 33.062 | 43.500 | +1.76% | -0.80% | 0.36x | 21.2 | 2026-11-18T14:00:06.447964+00:00 | Not calibrated | WEAK 12/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 71.766 | 0.04673 | +0.34% | 0.48x |
| 2 | MEGA/USD | 59.121 | 0.05485 | +0.57% | 0.73x |
| 3 | XRP/USD | 57.500 | 0.98611 | -0.01% | 0.22x |
| 4 | SENT/USD | 48.865 | 0.019255 | +0.36% | 2.38x |
| 5 | VVV/USD | 48.632 | 21.158 | -1.08% | 2.24x |
| 6 | AKT/USD | 47.609 | 0.5217 | -0.25% | 0.53x |
| 7 | TRX/USD | 45.262 | 0.309556 | -0.02% | 2.84x |
| 8 | USELESS/USD | 43.500 | 0.0993 | -0.80% | 0.36x |
| 9 | CC/USD | 40.260 | 0.08298 | -0.22% | 0.46x |
| 10 | PEARL/USD | 37.690 | 1.8365 | +0.83% | 4.05x |
| 11 | W/USD | 34.004 | 0.00903 | -0.88% | 1.47x |
| 12 | CAP/USD | 23.487 | 0.102437 | +0.58% | 3.16x |

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

- Persisted scans: 583; predictions: 4951; observations: 352054.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13099. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44319401896 · **Generation:** 583 · **Legacy run:** 44319401896
**Main quote time:** 2026-11-18T14:00:15.037914+00:00 · **Legacy report time:** 2026-11-18T14:00:42.109212+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04673 | 68.25 | +0.34% | 0.48x | MODERATE 59/100 | VERY_HIGH 76/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019255 | 64.45 | +0.36% | 2.38x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 3 | TRX/USD | 0.309556 | 60.16 | -0.02% | 2.84x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | MEGA/USD | 0.05485 | 59.26 | +0.57% | 0.73x | MODERATE 50/100 | EXTREME 94/100 | Do nothing |
| 5 | PEARL/USD ⭐ | 1.8365 | 56.86 | +0.83% | 4.05x | STRONG 83/100 | HIGH 67/100 | Consider small entry |
| 6 | VVV/USD | 21.158 | 55.66 | -1.08% | 2.24x | MODERATE 58/100 | HIGH 65/100 | Watch |
| 7 | XRP/USD | 0.98611 | 49.64 | -0.01% | 0.22x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AKT/USD | 0.5217 | 41.69 | -0.25% | 0.53x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | CAP/USD | 0.102437 | 41.39 | +0.58% | 3.16x | MODERATE 61/100 | VERY_HIGH 79/100 | Watch |
| 10 | W/USD | 0.00903 | 34.36 | -0.88% | 1.47x | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing |
| 11 | CC/USD | 0.08298 | 33.75 | -0.22% | 0.46x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | USELESS/USD | 0.0993 | 33.06 | -0.80% | 0.36x | WEAK 12/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019266 | 74.28 | +0.36% | 2.38x | 5655 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.8365 | 54.71 | +0.83% | 4.05x | 6312 | STRONG 77/100 | VERY_HIGH 77/100 | Watch |

**Same-run overlap:** SENT/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
