# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:55:19.966752+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44432781332
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 295f56c2bb13f9e44df095095d2ba025afea1b21 (atomic ledger/results publication)
**Ledger generation:** 712 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PAXG/USD | 3746.57 | 61.069 | 45.189 | +0.41% | +0.18% | 3.16x | 0.2 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021444 | 59.802 | 56.864 | +4.07% | +1.31% | 0.64x | 6.1 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05753 | 58.412 | 43.401 | +2.73% | +1.64% | 1.68x | 13.9 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | TRX/USD | 0.310721 | 57.687 | 42.071 | +0.47% | +0.12% | 8.81x | 0.0 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XBT/USD | 63154.1 | 57.548 | 56.877 | +0.27% | +0.13% | 1.00x | 0.0 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ETH/USD | 1783.54 | 55.600 | 58.435 | +0.49% | +0.12% | 0.66x | 0.1 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ZEC/USD | 917.37 | 50.927 | 58.507 | +0.59% | +0.03% | 0.23x | 1.3 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0589101 | 47.996 | 51.596 | +0.35% | +0.06% | 0.61x | 0.0 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.3184 | 47.161 | 57.050 | +0.64% | -0.31% | 0.17x | 4.8 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LTC/USD | 44.23 | 46.043 | 48.788 | +0.50% | +0.29% | 0.58x | 2.3 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | BNB/USD | 584.06 | 41.335 | 41.006 | +0.48% | +0.09% | 0.99x | 1.4 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | WEAK 41/100 | HIGH 62/100 | Watch | WATCH |
| 12 | VVV/USD | 21.916 | 40.489 | 53.332 | +1.13% | -0.91% | 0.17x | 5.5 | 2026-11-19T00:55:14.138408+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 58.507 | 917.37 | +0.03% | 0.23x |
| 2 | ETH/USD | 58.435 | 1783.54 | +0.12% | 0.66x |
| 3 | NEAR/USD | 57.050 | 3.3184 | -0.31% | 0.17x |
| 4 | XBT/USD | 56.877 | 63154.1 | +0.13% | 1.00x |
| 5 | SENT/USD | 56.864 | 0.021444 | +1.31% | 0.64x |
| 6 | VVV/USD | 53.332 | 21.916 | -0.91% | 0.17x |
| 7 | XDG/USD | 51.596 | 0.0589101 | +0.06% | 0.61x |
| 8 | LTC/USD | 48.788 | 44.23 | +0.29% | 0.58x |
| 9 | PAXG/USD | 45.189 | 3746.57 | +0.18% | 3.16x |
| 10 | MEGA/USD | 43.401 | 0.05753 | +1.64% | 1.68x |
| 11 | TRX/USD | 42.071 | 0.310721 | +0.12% | 8.81x |
| 12 | BNB/USD | 41.006 | 584.06 | +0.09% | 0.99x |

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

- Persisted scans: 712; predictions: 5769; observations: 430615.
- Matured sampled outcomes across 1/6/24/48h: 5653; gap abstentions: 13424. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44432781332 · **Generation:** 712 · **Legacy run:** 44432781332
**Main quote time:** 2026-11-19T00:55:19.966752+00:00 · **Legacy report time:** 2026-11-19T00:55:50.165313+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3746.57 | 61.07 | +0.18% | 3.16x | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | SENT/USD | 0.021444 | 59.80 | +1.31% | 0.64x | MODERATE 60/100 | VERY_HIGH 82/100 | Watch |
| 3 | MEGA/USD | 0.05753 | 58.41 | +1.64% | 1.68x | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 4 | TRX/USD | 0.310721 | 57.69 | +0.12% | 8.81x | STRONG 74/100 | HIGH 55/100 | Watch |
| 5 | XBT/USD ⭐ | 63154.1 | 57.55 | +0.13% | 1.00x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 6 | ETH/USD | 1783.54 | 55.60 | +0.12% | 0.66x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 7 | ZEC/USD | 917.37 | 50.93 | +0.03% | 0.23x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD | 0.0589101 | 48.00 | +0.06% | 0.61x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 9 | NEAR/USD | 3.3184 | 47.16 | -0.31% | 0.17x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LTC/USD | 44.23 | 46.04 | +0.29% | 0.58x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | BNB/USD | 584.06 | 41.33 | +0.09% | 0.99x | WEAK 41/100 | HIGH 62/100 | Watch |
| 12 | VVV/USD | 21.916 | 40.49 | -0.91% | 0.17x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3746.57 | 57.87 | +0.18% | 3.16x | 4240 | STRONG 84/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 63176.1 | 56.02 | +0.13% | 1.00x | 153342 | MODERATE 63/100 | HIGH 62/100 | Watch |
| 3 | SOL/USD | 73.71 | 52.48 | +0.11% | 1.02x | 36318 | MODERATE 51/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PAXG/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
