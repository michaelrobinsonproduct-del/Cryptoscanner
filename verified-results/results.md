# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T22:10:23.018472+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44408835170
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7d575587b0733218514d05baa4dd1eae784a9a12 (atomic ledger/results publication)
**Ledger generation:** 680 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WINGS/USD | 0.001932 | 90.527 | 53.928 | +5.40% | +4.32% | 5.79x | 31.1 | 2026-11-18T22:10:19.761184+00:00 | Not calibrated | STRONG 90/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | SENT/USD | 0.020573 | 80.702 | 61.349 | +10.20% | +0.87% | 2.55x | 29.7 | 2026-11-18T22:10:19.761184+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | VVV/USD | 21.163 | 55.155 | 47.612 | +0.65% | -0.90% | 2.21x | 8.5 | 2026-11-18T22:10:19.761184+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01029321 | 43.986 | 48.005 | +3.09% | +0.10% | 0.55x | 16.4 | 2026-11-18T22:10:19.761184+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 61.349 | 0.020573 | +0.87% | 2.55x |
| 2 | WINGS/USD | 53.928 | 0.001932 | +4.32% | 5.79x |
| 3 | AKE/USD | 48.005 | 0.01029321 | +0.10% | 0.55x |
| 4 | VVV/USD | 47.612 | 21.163 | -0.90% | 2.21x |

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

- Persisted scans: 680; predictions: 5570; observations: 411127.
- Matured sampled outcomes across 1/6/24/48h: 5298; gap abstentions: 13170. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44408835170 · **Generation:** 680 · **Legacy run:** 44408835170
**Main quote time:** 2026-11-18T22:10:23.018472+00:00 · **Legacy report time:** 2026-11-18T22:10:50.816455+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.001932 | 90.53 | +4.32% | 5.79x | STRONG 100/100 | VERY_HIGH 82/100 | Watch |
| 2 | SENT/USD ⭐ | 0.020573 | 80.70 | +0.87% | 2.55x | STRONG 95/100 | VERY_HIGH 79/100 | Watch |
| 3 | VVV/USD | 21.163 | 55.15 | -0.90% | 2.21x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | AKE/USD | 0.01029321 | 43.99 | +0.10% | 0.55x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.001932 | 87.01 | +4.32% | 5.79x | 4604 | STRONG 99/100 | VERY_HIGH 82/100 | Watch |
| 2 | SENT/USD ⭐ | 0.02056 | 79.55 | +0.87% | 2.55x | 6433 | STRONG 100/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** WINGS/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
