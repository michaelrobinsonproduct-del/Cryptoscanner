# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T21:51:25.327046+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45074247230
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** dce6f13c89cdc4217662b121a4282448c1b29249 (atomic ledger/results publication)
**Ledger generation:** 1340 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002579 | 98.582 | 82.804 | +10.03% | +0.16% | 2.83x | 7.7 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04939 | 91.630 | 90.550 | +11.54% | +1.17% | 0.52x | 6.1 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | DRV/USD | 0.37505 | 89.598 | 86.449 | +11.89% | -0.39% | 1.51x | 5.3 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 25.925 | 75.800 | 80.150 | +4.12% | -0.05% | 0.59x | 7.3 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | STBL/USD | 0.017218 | 73.547 | 67.582 | +7.59% | +0.37% | 1.41x | 16.9 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | NEAR/USD | 3 | 73.398 | 80.241 | +3.94% | +0.01% | 0.31x | 4.7 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1720.84 | 71.422 | 71.016 | +2.29% | -0.04% | 1.06x | 0.1 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ZEC/USD | 793.9 | 65.955 | 67.513 | +2.02% | +0.31% | 0.69x | 3.3 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.68 | 64.597 | 69.864 | +2.35% | +0.14% | 0.40x | 3.2 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | BNB/USD | 557.3 | 64.473 | 48.826 | +1.81% | +0.13% | 2.57x | 2.2 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6571 | 63.429 | 64.685 | +1.51% | +0.11% | 0.82x | 1.5 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 60929.4 | 61.047 | 64.771 | +1.40% | +0.03% | 0.61x | 0.0 | 2026-11-22T21:51:17.230592+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 90.550 | 0.04939 | +1.17% | 0.52x |
| 2 | DRV/USD | 86.449 | 0.37505 | -0.39% | 1.51x |
| 3 | PUMP/USD | 82.804 | 0.002579 | +0.16% | 2.83x |
| 4 | NEAR/USD | 80.241 | 3 | +0.01% | 0.31x |
| 5 | VVV/USD | 80.150 | 25.925 | -0.05% | 0.59x |
| 6 | ETH/USD | 71.016 | 1720.84 | -0.04% | 1.06x |
| 7 | HYPE/USD | 69.864 | 62.68 | +0.14% | 0.40x |
| 8 | STBL/USD | 67.582 | 0.017218 | +0.37% | 1.41x |
| 9 | ZEC/USD | 67.513 | 793.9 | +0.31% | 0.69x |
| 10 | XBT/USD | 64.771 | 60929.4 | +0.03% | 0.61x |
| 11 | SUI/USD | 64.685 | 0.6571 | +0.11% | 0.82x |
| 12 | BNB/USD | 48.826 | 557.3 | +0.13% | 2.57x |

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

- Persisted scans: 1340; predictions: 10999; observations: 811168.
- Matured sampled outcomes across 1/6/24/48h: 16845; gap abstentions: 22368. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45074247230 · **Generation:** 1340 · **Legacy run:** 45074247230
**Main quote time:** 2026-11-22T21:51:25.327046+00:00 · **Legacy report time:** 2026-11-22T21:52:22.251740+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002579 | 98.58 | +0.16% | 2.83x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.04939 | 91.63 | +1.17% | 0.52x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 3 | DRV/USD | 0.37505 | 89.60 | -0.39% | 1.51x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 25.925 | 75.80 | -0.05% | 0.59x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 5 | STBL/USD | 0.017218 | 73.55 | +0.37% | 1.41x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 6 | NEAR/USD | 3 | 73.40 | +0.01% | 0.31x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1720.84 | 71.42 | -0.04% | 1.06x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | ZEC/USD | 793.9 | 65.96 | +0.31% | 0.69x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 9 | HYPE/USD | 62.68 | 64.60 | +0.14% | 0.40x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 10 | BNB/USD | 557.3 | 64.47 | +0.13% | 2.57x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | SUI/USD | 0.6571 | 63.43 | +0.11% | 0.82x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 60929.4 | 61.05 | +0.03% | 0.61x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002579 | 84.80 | +0.16% | 2.83x | 4219 | STRONG 97/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
