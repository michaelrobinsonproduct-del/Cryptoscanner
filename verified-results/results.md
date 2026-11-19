# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T06:25:28.326942+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44471943032
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** fde3e4b339b21abad35febf3b24bdf4f063901b4 (atomic ledger/results publication)
**Ledger generation:** 776 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.025 | 101.721 | 95.426 | +6.25% | +0.86% | 1.20x | 6.5 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | LIGHTER/USD | 2.915 | 90.292 | 73.052 | +7.41% | +0.45% | 3.95x | 17.2 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | SOL/USD | 74.75 | 80.571 | 65.849 | +1.65% | +0.12% | 2.41x | 1.3 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1801.25 | 76.409 | 65.420 | +1.49% | +0.10% | 2.05x | 0.1 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ZEC/USD | 941.33 | 75.030 | 76.329 | +3.22% | +0.12% | 0.81x | 2.4 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.3922 | 72.949 | 73.209 | +2.88% | -0.04% | 0.99x | 3.8 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | USELESS/USD | 0.1031 | 70.793 | 74.220 | +7.89% | +0.30% | 0.51x | 18.4 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97636 | 65.728 | 62.185 | +1.03% | +0.23% | 1.24x | 0.1 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 9 | TAO/USD | 195.8348 | 64.451 | 67.538 | +2.02% | +0.30% | 0.54x | 3.2 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HYPE/USD | 68.06 | 64.425 | 66.616 | +1.76% | +0.24% | 0.66x | 1.5 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0592189 | 56.101 | 55.430 | +0.88% | +0.17% | 0.98x | 0.0 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 63444.4 | 55.331 | 60.103 | +0.73% | +0.08% | 0.48x | 0.0 | 2026-11-19T06:25:19.310945+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.426 | 23.025 | +0.86% | 1.20x |
| 2 | ZEC/USD | 76.329 | 941.33 | +0.12% | 0.81x |
| 3 | USELESS/USD | 74.220 | 0.1031 | +0.30% | 0.51x |
| 4 | NEAR/USD | 73.209 | 3.3922 | -0.04% | 0.99x |
| 5 | LIGHTER/USD | 73.052 | 2.915 | +0.45% | 3.95x |
| 6 | TAO/USD | 67.538 | 195.8348 | +0.30% | 0.54x |
| 7 | HYPE/USD | 66.616 | 68.06 | +0.24% | 0.66x |
| 8 | SOL/USD | 65.849 | 74.75 | +0.12% | 2.41x |
| 9 | ETH/USD | 65.420 | 1801.25 | +0.10% | 2.05x |
| 10 | XRP/USD | 62.185 | 0.97636 | +0.23% | 1.24x |
| 11 | XBT/USD | 60.103 | 63444.4 | +0.08% | 0.48x |
| 12 | XDG/USD | 55.430 | 0.0592189 | +0.17% | 0.98x |

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

- Persisted scans: 776; predictions: 6456; observations: 469590.
- Matured sampled outcomes across 1/6/24/48h: 6529; gap abstentions: 13847. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44471943032 · **Generation:** 776 · **Legacy run:** 44471943032
**Main quote time:** 2026-11-19T06:25:28.326942+00:00 · **Legacy report time:** 2026-11-19T06:26:18.184406+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.025 | 101.72 | +0.86% | 1.20x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | LIGHTER/USD ⭐ | 2.915 | 90.29 | +0.45% | 3.95x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 74.75 | 80.57 | +0.12% | 2.41x | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD ⭐ | 1801.25 | 76.41 | +0.10% | 2.05x | STRONG 93/100 | HIGH 55/100 | Watch |
| 5 | ZEC/USD | 941.33 | 75.03 | +0.12% | 0.81x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 6 | NEAR/USD | 3.3922 | 72.95 | -0.04% | 0.99x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | USELESS/USD | 0.1031 | 70.79 | +0.30% | 0.51x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.97636 | 65.73 | +0.23% | 1.24x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 9 | TAO/USD | 195.8348 | 64.45 | +0.30% | 0.54x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | HYPE/USD | 68.06 | 64.42 | +0.24% | 0.66x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0592189 | 56.10 | +0.17% | 0.98x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 63444.4 | 55.33 | +0.08% | 0.48x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23.031 | 96.41 | +0.86% | 1.20x | 9945 | STRONG 93/100 | HIGH 62/100 | Watch |
| 2 | LIGHTER/USD ⭐ | 2.935 | 83.37 | +0.45% | 3.95x | 4215 | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 74.73 | 74.75 | +0.12% | 2.41x | 35264 | STRONG 92/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD ⭐ | 1801.14 | 74.22 | +0.10% | 2.05x | 58296 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, LIGHTER/USD, SOL/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
