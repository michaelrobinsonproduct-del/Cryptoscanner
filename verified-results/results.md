# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:15:13.890851+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44322104631
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** bcf8ab41f4cd5e1ca1155811bd1339ee15a6dc11 (atomic ledger/results publication)
**Ledger generation:** 586 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04679 | 74.091 | 72.762 | +4.23% | +0.13% | 1.07x | 10.7 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019401 | 68.886 | 56.188 | +3.92% | +0.76% | 1.89x | 4.6 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.8758 | 59.166 | 53.963 | +3.61% | +2.14% | 0.45x | 19.5 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | VVV/USD | 21.214 | 52.124 | 52.765 | +0.89% | +0.26% | 0.80x | 3.8 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XRP/USD | 0.98592 | 50.498 | 56.857 | +0.34% | -0.02% | 0.38x | 1.1 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | TRX/USD | 0.309568 | 46.995 | 45.487 | +0.54% | +0.00% | 1.15x | 0.0 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 7 | CC/USD | 0.08317 | 42.492 | 41.857 | +1.27% | +0.23% | 0.95x | 4.8 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 8 | CAP/USD | 0.102152 | 42.477 | 28.868 | +1.17% | -0.28% | 2.59x | 21.2 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | WEAK 41/100 | EXTREME 85/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5212 | 41.185 | 47.871 | +2.34% | -0.10% | 0.38x | 1.9 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 10 | USELESS/USD | 0.0986 | 28.608 | 38.274 | +1.05% | -0.70% | 0.39x | 21.3 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | WEAK 9/100 | EXTREME 88/100 | Do nothing | WATCH |
| 11 | W/USD | 0.00899 | 24.964 | 30.854 | +0.67% | -0.44% | 0.63x | 11.1 | 2026-11-18T14:15:05.982529+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 72.762 | 0.04679 | +0.13% | 1.07x |
| 2 | XRP/USD | 56.857 | 0.98592 | -0.02% | 0.38x |
| 3 | SENT/USD | 56.188 | 0.019401 | +0.76% | 1.89x |
| 4 | PEARL/USD | 53.963 | 1.8758 | +2.14% | 0.45x |
| 5 | VVV/USD | 52.765 | 21.214 | +0.26% | 0.80x |
| 6 | AKT/USD | 47.871 | 0.5212 | -0.10% | 0.38x |
| 7 | TRX/USD | 45.487 | 0.309568 | +0.00% | 1.15x |
| 8 | CC/USD | 41.857 | 0.08317 | +0.23% | 0.95x |
| 9 | USELESS/USD | 38.274 | 0.0986 | -0.70% | 0.39x |
| 10 | W/USD | 30.854 | 0.00899 | -0.44% | 0.63x |
| 11 | CAP/USD | 28.868 | 0.102152 | -0.28% | 2.59x |

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

- Persisted scans: 586; predictions: 4985; observations: 353881.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44322104631 · **Generation:** 586 · **Legacy run:** 44322104631
**Main quote time:** 2026-11-18T14:15:13.890851+00:00 · **Legacy report time:** 2026-11-18T14:15:39.755903+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04679 | 74.09 | +0.13% | 1.07x | MODERATE 67/100 | HIGH 68/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019401 | 68.89 | +0.76% | 1.89x | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 3 | PEARL/USD | 1.8758 | 59.17 | +2.14% | 0.45x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 4 | VVV/USD | 21.214 | 52.12 | +0.26% | 0.80x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 5 | XRP/USD | 0.98592 | 50.50 | -0.02% | 0.38x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | TRX/USD | 0.309568 | 46.99 | +0.00% | 1.15x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 7 | CC/USD | 0.08317 | 42.49 | +0.23% | 0.95x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 8 | CAP/USD | 0.102152 | 42.48 | -0.28% | 2.59x | WEAK 41/100 | EXTREME 85/100 | Do nothing |
| 9 | AKT/USD | 0.5212 | 41.19 | -0.10% | 0.38x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 10 | USELESS/USD | 0.0986 | 28.61 | -0.70% | 0.39x | WEAK 9/100 | EXTREME 88/100 | Do nothing |
| 11 | W/USD | 0.00899 | 24.96 | -0.44% | 0.63x | WEAK 12/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04675 | 81.68 | +0.13% | 1.07x | 15805 | STRONG 71/100 | HIGH 68/100 | Watch |
| 2 | SENT/USD ⭐ | 0.019442 | 77.07 | +0.76% | 1.89x | 5686 | STRONG 94/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
