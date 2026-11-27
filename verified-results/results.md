# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T03:22:00.325212+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45933503035
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8abcbe01c7bd45a4aa4d1155a8fc08642f385a17 (atomic ledger/results publication)
**Ledger generation:** 1952 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.83 | 95.290 | 94.854 | +5.80% | +1.21% | 0.44x | 1.5 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 751.42 | 94.991 | 97.270 | +10.23% | +0.64% | 0.45x | 5.5 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04927 | 89.864 | 75.950 | +6.16% | +1.89% | 1.45x | 4.1 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6818 | 78.369 | 68.433 | +2.11% | +0.01% | 1.99x | 1.5 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 72.84 | 76.007 | 73.062 | +2.68% | +0.40% | 1.09x | 1.4 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0577641 | 73.013 | 60.406 | +2.46% | +0.28% | 2.12x | 0.0 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XMR/USD | 470.44 | 68.328 | 74.390 | +2.95% | -0.73% | 0.76x | 2.6 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LINK/USD | 9.49152 | 66.654 | 70.422 | +2.41% | +0.04% | 0.60x | 2.9 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1729.37 | 64.667 | 72.263 | +2.47% | +0.14% | 0.17x | 0.1 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.114 | 62.871 | 68.254 | +2.17% | -0.02% | 0.47x | 3.9 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.96347 | 62.495 | 70.333 | +2.20% | +0.06% | 0.19x | 0.1 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AAVE/USD | 96.38 | 62.177 | 52.123 | +2.01% | +0.05% | 1.98x | 2.1 | 2026-11-27T03:21:52.637994+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.270 | 751.42 | +0.64% | 0.45x |
| 2 | HYPE/USD | 94.854 | 65.83 | +1.21% | 0.44x |
| 3 | SKY/USD | 75.950 | 0.04927 | +1.89% | 1.45x |
| 4 | XMR/USD | 74.390 | 470.44 | -0.73% | 0.76x |
| 5 | SOL/USD | 73.062 | 72.84 | +0.40% | 1.09x |
| 6 | ETH/USD | 72.263 | 1729.37 | +0.14% | 0.17x |
| 7 | LINK/USD | 70.422 | 9.49152 | +0.04% | 0.60x |
| 8 | XRP/USD | 70.333 | 0.96347 | +0.06% | 0.19x |
| 9 | SUI/USD | 68.433 | 0.6818 | +0.01% | 1.99x |
| 10 | NEAR/USD | 68.254 | 3.114 | -0.02% | 0.47x |
| 11 | XDG/USD | 60.406 | 0.0577641 | +0.28% | 2.12x |
| 12 | AAVE/USD | 52.123 | 96.38 | +0.05% | 1.98x |

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

- Persisted scans: 1952; predictions: 17126; observations: 1182236.
- Matured sampled outcomes across 1/6/24/48h: 37622; gap abstentions: 25476. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45933503035 · **Generation:** 1952 · **Legacy run:** 45933503035
**Main quote time:** 2026-11-27T03:22:00.325212+00:00 · **Legacy report time:** 2026-11-27T03:22:52.171061+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.83 | 95.29 | +1.21% | 0.44x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD | 751.42 | 94.99 | +0.64% | 0.45x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04927 | 89.86 | +1.89% | 1.45x | STRONG 100/100 | HIGH 60/100 | Watch |
| 4 | SUI/USD | 0.6818 | 78.37 | +0.01% | 1.99x | STRONG 74/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD ⭐ | 72.84 | 76.01 | +0.40% | 1.09x | STRONG 83/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD ⭐ | 0.0577641 | 73.01 | +0.28% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XMR/USD | 470.44 | 68.33 | -0.73% | 0.76x | WEAK 39/100 | HIGH 68/100 | Watch |
| 8 | LINK/USD | 9.49152 | 66.65 | +0.04% | 0.60x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1729.37 | 64.67 | +0.14% | 0.17x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 10 | NEAR/USD | 3.114 | 62.87 | -0.02% | 0.47x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.96347 | 62.50 | +0.06% | 0.19x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 12 | AAVE/USD | 96.38 | 62.18 | +0.05% | 1.98x | MODERATE 66/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.82 | 82.63 | +0.40% | 1.09x | 34257 | STRONG 86/100 | HIGH 62/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04933 | 80.36 | +1.89% | 1.45x | 7117 | STRONG 95/100 | HIGH 60/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0577641 | 79.24 | +0.28% | 2.12x | 5533 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SKY/USD, SOL/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
