# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T03:31:20.197134+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45934471098
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fa7e8decc2fdfbf8d0fd2eceb5314cc2d7a9d4c6 (atomic ledger/results publication)
**Ledger generation:** 1953 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 756.41 | 107.654 | 95.425 | +10.97% | +0.33% | 2.06x | 9.1 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 66.76 | 95.404 | 98.499 | +7.30% | +0.09% | 0.65x | 3.0 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SUI/USD | 0.684 | 79.712 | 70.933 | +2.44% | -0.10% | 1.93x | 1.5 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04961 | 75.587 | 73.826 | +6.90% | +0.63% | 0.86x | 12.1 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SOL/USD | 73.03 | 74.899 | 74.938 | +2.95% | +0.12% | 0.93x | 1.4 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 6 | VVV/USD | 26.916 | 71.945 | 70.318 | +2.80% | +0.21% | 1.06x | 8.6 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ETH/USD | 1728.66 | 69.599 | 71.968 | +2.43% | -0.10% | 0.81x | 0.1 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0578931 | 68.821 | 61.585 | +2.69% | +0.03% | 1.71x | 0.9 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XRP/USD | 0.96538 | 63.036 | 71.336 | +2.40% | -0.05% | 0.20x | 0.9 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XMR/USD | 468.13 | 63.001 | 68.493 | +2.45% | -0.45% | 0.68x | 7.3 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 61553.7 | 62.818 | 67.207 | +1.75% | +0.07% | 0.53x | 0.0 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 9.51297 | 61.506 | 70.576 | +2.64% | +0.02% | 0.08x | 5.8 | 2026-11-27T03:31:12.015167+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 98.499 | 66.76 | +0.09% | 0.65x |
| 2 | ZEC/USD | 95.425 | 756.41 | +0.33% | 2.06x |
| 3 | SOL/USD | 74.938 | 73.03 | +0.12% | 0.93x |
| 4 | SKY/USD | 73.826 | 0.04961 | +0.63% | 0.86x |
| 5 | ETH/USD | 71.968 | 1728.66 | -0.10% | 0.81x |
| 6 | XRP/USD | 71.336 | 0.96538 | -0.05% | 0.20x |
| 7 | SUI/USD | 70.933 | 0.684 | -0.10% | 1.93x |
| 8 | LINK/USD | 70.576 | 9.51297 | +0.02% | 0.08x |
| 9 | VVV/USD | 70.318 | 26.916 | +0.21% | 1.06x |
| 10 | XMR/USD | 68.493 | 468.13 | -0.45% | 0.68x |
| 11 | XBT/USD | 67.207 | 61553.7 | +0.07% | 0.53x |
| 12 | XDG/USD | 61.585 | 0.0578931 | +0.03% | 1.71x |

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

- Persisted scans: 1953; predictions: 17138; observations: 1182837.
- Matured sampled outcomes across 1/6/24/48h: 37658; gap abstentions: 25480. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45934471098 · **Generation:** 1953 · **Legacy run:** 45934471098
**Main quote time:** 2026-11-27T03:31:20.197134+00:00 · **Legacy report time:** 2026-11-27T03:32:02.607441+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 756.41 | 107.65 | +0.33% | 2.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD | 66.76 | 95.40 | +0.09% | 0.65x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 3 | SUI/USD | 0.684 | 79.71 | -0.10% | 1.93x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | SKY/USD | 0.04961 | 75.59 | +0.63% | 0.86x | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |
| 5 | SOL/USD | 73.03 | 74.90 | +0.12% | 0.93x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 6 | VVV/USD ⭐ | 26.916 | 71.94 | +0.21% | 1.06x | STRONG 81/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD | 1728.66 | 69.60 | -0.10% | 0.81x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | XDG/USD | 0.0578931 | 68.82 | +0.03% | 1.71x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 9 | XRP/USD | 0.96538 | 63.04 | -0.05% | 0.20x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XMR/USD | 468.13 | 63.00 | -0.45% | 0.68x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 61553.7 | 62.82 | +0.07% | 0.53x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 9.51297 | 61.51 | +0.02% | 0.08x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 754.54 | 100.00 | +0.33% | 2.06x | 38129 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | WLD/USD | 0.2511 | 83.79 | +0.08% | 3.79x | 2342 | STRONG 87/100 | HIGH 60/100 | Watch |
| 3 | VVV/USD ⭐ | 27.005 | 75.53 | +0.21% | 1.06x | 14926 | STRONG 78/100 | HIGH 68/100 | Watch |

**Same-run overlap:** ZEC/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
