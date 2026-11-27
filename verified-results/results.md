# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:12:17.122709+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46061682898
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8a53c4844a97122be51f3ff3f47c1494a60d3323 (atomic ledger/results publication)
**Ledger generation:** 2054 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 740.09 | 96.494 | 95.676 | +8.57% | -0.02% | 1.09x | 8.6 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05063 | 89.441 | 85.207 | +4.46% | +0.84% | 1.00x | 2.0 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0575867 | 83.749 | 69.574 | +2.15% | -0.17% | 3.06x | 1.0 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04927 | 79.021 | 75.354 | +6.16% | +0.78% | 0.98x | 6.1 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 5 | RENDER/USD | 1.395 | 77.972 | 61.894 | +4.65% | +0.22% | 2.67x | 7.2 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | STRONG 94/100 | HIGH 60/100 | Consider small entry | WATCH |
| 6 | LTC/USD | 43.99 | 73.660 | 57.864 | +0.57% | +0.16% | 2.89x | 2.3 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6718 | 72.886 | 58.554 | +0.61% | -0.13% | 4.82x | 1.5 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 8 | UNI/USD | 4.8307 | 69.044 | 76.498 | +3.88% | -0.02% | 0.27x | 6.6 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 71.94 | 68.702 | 64.172 | +1.41% | +0.00% | 1.45x | 1.4 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94723 | 66.939 | 58.168 | +0.48% | -0.03% | 1.89x | 0.3 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 11 | HYPE/USD | 63.73 | 63.627 | 70.418 | +2.43% | -0.03% | 0.34x | 3.1 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | PAXG/USD | 3644.55 | 55.507 | 59.694 | +2.47% | +0.03% | 0.57x | 1.0 | 2026-11-27T20:12:10.963447+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 95.676 | 740.09 | -0.02% | 1.09x |
| 2 | NIGHT/USD | 85.207 | 0.05063 | +0.84% | 1.00x |
| 3 | UNI/USD | 76.498 | 4.8307 | -0.02% | 0.27x |
| 4 | SKY/USD | 75.354 | 0.04927 | +0.78% | 0.98x |
| 5 | HYPE/USD | 70.418 | 63.73 | -0.03% | 0.34x |
| 6 | XDG/USD | 69.574 | 0.0575867 | -0.17% | 3.06x |
| 7 | SOL/USD | 64.172 | 71.94 | +0.00% | 1.45x |
| 8 | RENDER/USD | 61.894 | 1.395 | +0.22% | 2.67x |
| 9 | PAXG/USD | 59.694 | 3644.55 | +0.03% | 0.57x |
| 10 | SUI/USD | 58.554 | 0.6718 | -0.13% | 4.82x |
| 11 | XRP/USD | 58.168 | 0.94723 | -0.03% | 1.89x |
| 12 | LTC/USD | 57.864 | 43.99 | +0.16% | 2.89x |

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

- Persisted scans: 2054; predictions: 18350; observations: 1243779.
- Matured sampled outcomes across 1/6/24/48h: 41483; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46061682898 · **Generation:** 2054 · **Legacy run:** 46061682898
**Main quote time:** 2026-11-27T20:12:17.122709+00:00 · **Legacy report time:** 2026-11-27T20:13:01.470388+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 740.09 | 96.49 | -0.02% | 1.09x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05063 | 89.44 | +0.84% | 1.00x | STRONG 90/100 | HIGH 62/100 | Watch |
| 3 | XDG/USD | 0.0575867 | 83.75 | -0.17% | 3.06x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | SKY/USD | 0.04927 | 79.02 | +0.78% | 0.98x | STRONG 70/100 | HIGH 67/100 | Watch |
| 5 | RENDER/USD | 1.395 | 77.97 | +0.22% | 2.67x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 6 | LTC/USD | 43.99 | 73.66 | +0.16% | 2.89x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | SUI/USD | 0.6718 | 72.89 | -0.13% | 4.82x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 8 | UNI/USD | 4.8307 | 69.04 | -0.02% | 0.27x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 71.94 | 68.70 | +0.00% | 1.45x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 10 | XRP/USD | 0.94723 | 66.94 | -0.03% | 1.89x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 11 | HYPE/USD | 63.73 | 63.63 | -0.03% | 0.34x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | PAXG/USD | 3644.55 | 55.51 | +0.03% | 0.57x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05064 | 94.63 | +0.84% | 1.00x | 17955 | STRONG 92/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
