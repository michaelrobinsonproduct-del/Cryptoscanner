# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T22:21:25.872504+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45077076500
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** e3872c06130f93667127a54f22a121919f3b3783 (atomic ledger/results publication)
**Ledger generation:** 1344 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37246 | 98.024 | 86.505 | +11.12% | -0.51% | 2.41x | 5.1 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 26.096 | 93.763 | 88.048 | +4.80% | +1.03% | 1.06x | 1.1 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 82/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.00256 | 92.584 | 82.836 | +9.21% | -0.31% | 2.13x | 7.8 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PIEVERSE/USD | 3.6985 | 92.484 | 76.956 | +8.68% | +0.11% | 4.12x | 17.3 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.0493 | 90.938 | 86.895 | +11.34% | +0.14% | 1.33x | 14.2 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.987 | 82.339 | 77.581 | +3.49% | +0.05% | 1.45x | 3.7 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ZEC/USD | 791.54 | 80.348 | 65.827 | +1.72% | -0.10% | 2.58x | 2.4 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 8 | STBL/USD | 0.017193 | 77.091 | 73.712 | +7.43% | +0.19% | 1.24x | 4.6 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | XBT/USD | 60799.6 | 72.813 | 63.259 | +1.18% | +0.11% | 1.90x | 0.0 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 10 | LINK/USD | 8.76854 | 71.638 | 56.528 | +2.02% | +0.02% | 3.08x | 1.4 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 11 | HYPE/USD | 62.47 | 69.721 | 68.259 | +2.01% | -0.05% | 1.17x | 1.6 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 12 | ETH/USD | 1714.21 | 64.043 | 68.257 | +1.90% | +0.15% | 0.50x | 0.1 | 2026-11-22T22:21:17.777765+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 88.048 | 26.096 | +1.03% | 1.06x |
| 2 | NIGHT/USD | 86.895 | 0.0493 | +0.14% | 1.33x |
| 3 | DRV/USD | 86.505 | 0.37246 | -0.51% | 2.41x |
| 4 | PUMP/USD | 82.836 | 0.00256 | -0.31% | 2.13x |
| 5 | NEAR/USD | 77.581 | 2.987 | +0.05% | 1.45x |
| 6 | PIEVERSE/USD | 76.956 | 3.6985 | +0.11% | 4.12x |
| 7 | STBL/USD | 73.712 | 0.017193 | +0.19% | 1.24x |
| 8 | HYPE/USD | 68.259 | 62.47 | -0.05% | 1.17x |
| 9 | ETH/USD | 68.257 | 1714.21 | +0.15% | 0.50x |
| 10 | ZEC/USD | 65.827 | 791.54 | -0.10% | 2.58x |
| 11 | XBT/USD | 63.259 | 60799.6 | +0.11% | 1.90x |
| 12 | LINK/USD | 56.528 | 8.76854 | +0.02% | 3.08x |

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

- Persisted scans: 1344; predictions: 11047; observations: 813603.
- Matured sampled outcomes across 1/6/24/48h: 16953; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45077076500 · **Generation:** 1344 · **Legacy run:** 45077076500
**Main quote time:** 2026-11-22T22:21:25.872504+00:00 · **Legacy report time:** 2026-11-22T22:22:33.418575+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.37246 | 98.02 | -0.51% | 2.41x | STRONG 79/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 26.096 | 93.76 | +1.03% | 1.06x | STRONG 92/100 | HIGH 62/100 | Watch |
| 3 | PUMP/USD | 0.00256 | 92.58 | -0.31% | 2.13x | STRONG 76/100 | HIGH 61/100 | Watch |
| 4 | PIEVERSE/USD ⭐ | 3.6985 | 92.48 | +0.11% | 4.12x | STRONG 96/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.0493 | 90.94 | +0.14% | 1.33x | STRONG 85/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD ⭐ | 2.987 | 82.34 | +0.05% | 1.45x | STRONG 86/100 | HIGH 55/100 | Watch |
| 7 | ZEC/USD | 791.54 | 80.35 | -0.10% | 2.58x | STRONG 70/100 | HIGH 61/100 | Watch |
| 8 | STBL/USD ⭐ | 0.017193 | 77.09 | +0.19% | 1.24x | STRONG 74/100 | VERY_HIGH 74/100 | Watch |
| 9 | XBT/USD ⭐ | 60799.6 | 72.81 | +0.11% | 1.90x | STRONG 81/100 | HIGH 55/100 | Watch |
| 10 | LINK/USD | 8.76854 | 71.64 | +0.02% | 3.08x | STRONG 81/100 | HIGH 55/100 | Watch |
| 11 | HYPE/USD | 62.47 | 69.72 | -0.05% | 1.17x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 12 | ETH/USD | 1714.21 | 64.04 | +0.15% | 0.50x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.074 | 91.04 | +1.03% | 1.06x | 11990 | STRONG 91/100 | HIGH 62/100 | Watch |
| 2 | NEAR/USD ⭐ | 2.987 | 88.46 | +0.05% | 1.45x | 12678 | STRONG 89/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.0494 | 86.13 | +0.14% | 1.33x | 10192 | STRONG 88/100 | HIGH 55/100 | Watch |
| 4 | PIEVERSE/USD ⭐ | 3.6985 | 84.69 | +0.11% | 4.12x | 5871 | STRONG 92/100 | HIGH 61/100 | Watch |
| 5 | XBT/USD ⭐ | 60780.3 | 69.69 | +0.11% | 1.90x | 128465 | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | STBL/USD ⭐ | 0.017208 | 68.03 | +0.19% | 1.24x | 1877 | MODERATE 69/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** VVV/USD, PIEVERSE/USD, NIGHT/USD, NEAR/USD, STBL/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
